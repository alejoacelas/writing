# Claude Code: allow web fetch on all domains

*Source: https://wow.pjh.is/journal/claude-code-allow-webfetch-all-domains*  ·  *Published: 2026-03-02*

---

By default, Claude Code asks for permission every time it fetches content from a domain you haven't already whitelisted.

I went along with this for a while, gradually adding more and more domains to the global whitelist in `~/.claude/settings.json`, while omitting domains I consider higher risk (e.g. github.com).

On reflection, I think that the "always ask if not whitelisted" default doesn't make sense for most users:

- Key reason: permission fatigue kills the security value. You quickly start hitting enter reflexively on these prompts. You're never actually going to check each web page. So the prompts do roughly nothing other than slow you down. The most likely case where it might catch something: if there were an obviously questionable imitation domain (e.g. github.net) that you managed to notice before hitting "Enter".
- Prompt-injection attacks are scary in theory, but very rare in the wild (so far). For now, I'm more worried that Claude will take some destructive action that you I didn't intend due to it's misjudgement/my miscommunication. An unexpected `WebFetch` probably won't be the cause of that.
- Unwanted agent behaviour is better mitigated by [PreToolUse hooks](https://docs.anthropic.com/en/docs/claude-code/hooks), [sandboxing](https://code.claude.com/docs/en/sandboxing), or [containerisation](https://code.claude.com/docs/en/devcontainer).
- The cost of this default—constant interruptions—is very high.

So now, my `settings.json` just has:

```json
{
  "permissions": {
    "allow": [
      "WebFetch",
      // ...
    ]
  }
}

```

See also: [my permissions whitelist](https://wow.pjh.is/journal/claude-code-permissions-whitelist).
