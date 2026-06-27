# Claude Code: my permissions whitelist

*Source: https://wow.pjh.is/journal/claude-code-permissions-whitelist*  ·  *Published: 2026-01-20*

---

Claude Code can work autonomously for minutes, even hours. But not if it's constantly asking for permission to act. Just like a human, you need to trust it (but not too much).

## My philosophy

Claude's default approach: blacklist most things, ask for permissions, gradually accrue a whitelist. Worry about prompt injection.

My approach: whitelist most things, then add safeguards on top. Don't worry about prompt injection.

Other common approaches:

- Paranoia: use containers, or a dedicated VPS for each project. Over the top for me, but reasonable for some.
- YOLO: just run `claude --dangerously-skip-permissions`. Too risky for me.

## My \~/.claude/settings.json

First up, enable sandbox:

```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "allowUnsandboxedCommands": false,
    "network": {
      "allowedDomains": ["*"]
    }
  }
}

```

The sandbox prevents Claude from running `bash` commands that affect files outside your working directory (the directory where you run `claude`).

Surprisingly, the sandbox does **not** prevent Claude from modifying files outside your working directory using its other tools (e.g. `write`). We'll handle that with security hooks in a moment.

I whitelist all network requests, because prompt injection is currently not a major risk, and, for my purposes, maintaining a domain whitelist is too much faff.[1](#user-content-fn-1)

Here's are my tool permissions:

```json
{
  "permissions": {
    "allow": [
      "Bash",
      "Write",
      "Edit",
      "Glob",
      "Grep",
      "Read",
      "NotebookEdit",
      "WebFetch",
      "WebSearch",
      "mcp__plugin_context7_context7__*",
      "mcp__context7__*",
      "mcp__claude_ai_Google_Calendar__*",
      "Skill(project-management:*)",
      "Skill(plugin-dev:*)",
      "Skill(pr-review-toolkit:*)",
      "Skill(frontend-design:*)"
      // ... and nearly all my other skills.
    ]
  }
}

```

Again, WebFetch is enabled for all domains.

I globally whitelist nearly all my skills, with the exception of `send-email`.

### Let Claude read web pages from any domain

Whitelisting `WebFetch` means giving Claude permission to read any web page on the internet.

With the default setup, Claude asks permissions before accessing any domain you haven't previously whitelisted. This is tolerable for coding tasks—80% of requests probably go to just 30-50 domains, so there aren't too many to whitelist. But it's absolutely horrible for any kind of research.

If you're getting far too many permission requests, the security value quickly declines to \~0, since you'll develop prompt fatigue and just reflexively approve every request.

Furthermore: the main reason to watch `WebFetch` is to guard against [prompt injection](https://en.wikipedia.org/wiki/Prompt%5Finjection) attacks. But, the absolute level of security risk from prompt injection is currently low. This attack vector is scary in theory but—so far—vanishingly rare in the wild.

Bottom line: whitelisting `WebFetch` passes the cost:benefit, for now.

### The bash safety hook

Whitelisting `bash` is a bold move—bash commands can do more or less anything.

I mitigate that with a [PreToolUse hook](https://code.claude.com/docs/en/hooks) that:

1. **Hard blocks** `rm`, `shred`, `unlink`, `find -delete` and forces Claude to use `trash` instead. With `trash`, files are easily restored from your trash can. With `rm`, you'll need to get them from your backups.
2. **Prompts for permission** on potential RCE vectors, exfiltration attempts, and persistence mechanisms.

In `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bun run ~/.claude/hooks/security/bash-safety.ts"
          }
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bun run ~/.claude/hooks/security/deploy-guard.ts"
          }
        ]
      }
    ]
  }
}

```

The scripts: [bash-safety.ts](https://gist.github.com/peterhartree/23ea4d9ded2c699b4c00357a48f1a9f4), [deploy-guard.ts](https://gist.github.com/peterhartree/34e5c99acd6f3465e98716b1d3c1130c). I'm keen for ideas on how to improve them.

### Git security

My `claude.md` also says:

```
## Git security
Only clone repositories (`git clone`, `gh repo clone`) that the user has
explicitly requested by URL or name. If a task seems to require cloning
a repo the user hasn't specifically mentioned, ask first before cloning.

```

## Recovery from accidental deletion

### Use version control

Most of my work is version controlled with Git. If something untoward happens, just restore from history.

### Use `trash`, not `rm`

The trash command sends files to your Trash folder instead of deleting them permanently. This enables recovery if you're not already tracking files in git.

The safety script blocks `rm` commands, pausing execution and telling Claude to use `trash` instead. But ideally Claude just uses `trash` directly. So I tell Claude about this in my global `~/.claude/CLAUDE.md`:

```markdown
## Required

- **NEVER use `rm -rf`**—it's blocked by the command-validator hook for safety
- Use `trash` instead: `trash folder-name` or `trash file.txt`
  - Works exactly like `rm -rf` but moves to Trash instead of permanent deletion

```

### Continuous backups

[Backblaze](https://www.backblaze.com/cloud-backup/personal) continuously backs up my work, keeping [version history forever](https://www.backblaze.com/computer-backup/docs/set-up-extended-version-history). So, if Claude actually deletes something I care about, it'll be recoverable.

## Key uncertainty: sandbox or not?

Right now my biggest uncertainty is: should I run Claude Code with [sandbox mode](https://code.claude.com/docs/en/sandboxing) enabled?

I worry that it'll add too much friction. To my surprise, it seems that it only constrains `bash` commands to the current working directory, yet Claude's own "read/write/edit" tool remains free to access your entire machine (if you've whitelisted it, per my config above).

I'm going to play around with this in the coming days, and will update the post.

## How to implement

If you want something like this, just paste the link to this blog post into Claude, and ask Claude to implement it.

## Footnotes

1. I do a lot of research queries. If I were only using Claude Code for coding, it might be more feasible to just whitelist the 30-50 most common domains and tolerate permission prompts for the rest. [↩](#user-content-fnref-1)
