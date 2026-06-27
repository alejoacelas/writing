# How to share skills between Claude Code, Codex and Gemini

*Source: https://wow.pjh.is/journal/share-skills-between-coding-agents*  ·  *Published: 2026-02-18*

---

Places you can store global skill files:

```
# Read by Codex and Gemini, but not Claude Code
~/.agents/skills/ 

# Read by Claude
~/.claude/skills/ 

# Read by Codex
~/.codex/skills/

# Read by Gemini
~/.gemini/skills/

```

So: the easiest way to make skills available to all three agents is to put them in `~/.agents/skills/` and then symlink that folder to `~/.claude/skills/`.

```bash
# Symlink ~/.agents/skills to ~/.claude/skills
ln -sfn ~/.agents/skills ~/.claude/skills

```

I expect Claude Code will add support for the `~/.agents` directory soon.

You can use the same pattern for project-specific skills.
