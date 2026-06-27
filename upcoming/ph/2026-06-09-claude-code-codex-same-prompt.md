# CLI utility to prompt both Claude Code and Codex

*Source: https://wow.pjh.is/journal/claude-code-codex-same-prompt*  ·  *Published: 2026-06-09*

---

I often want to send the same prompt to Claude Code and Codex, then compare what they come up with.

Building on my [project switcher](https://wow.pjh.is/journal/claude-code-project-switcher), I've made a `c2` utility. Here's the flow:

1. Type `c2`
2. Enter prompt.
3. Select project folder using project switcher.
4. Codex opens in the current pane, and Claude opens in a new pane, both running the prompt.

As a one-liner, I can do `c2 <project_id> <prompt>` to skip steps (2) and (3).

The [script](https://gist.github.com/peterhartree/ae82a7c0aa20e2fe8d9093e4daffe54f) is made for [Warp](https://wow.pjh.is/journal/warp-llm-terminal), but you can adapt it to your favourite terminal.
