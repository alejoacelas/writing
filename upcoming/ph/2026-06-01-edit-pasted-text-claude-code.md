# How to edit pasted text blocks in Claude Code and Codex

*Source: https://wow.pjh.is/journal/edit-pasted-text-claude-code*  ·  *Published: 2026-06-01*

---

When you paste a long text into Claude Code or Codex, it collapses into a placeholder like `[Pasted text #1 +4 lines]`. That's handy unless you want to edit or review what you wrote.

Some ways to deal with this:

1. **Open the prompt in your editor.** Press `Ctrl+G` to open the current prompt in your default editor. I recently switched my default editor to VS Code, which opens fast. You edit, then hit `Cmd+S` `Cmd+W` to save and close the tab. You'll find the prompt is back in your agent, ready to submit.
2. **Claude Code-only: paste again to expand.** Press `Cmd+V` twice and the placeholder expands in full, inline. If you use [Wispr Flow](https://wow.pjh.is/journal/voice-input-with-wisprflow), you can set a shortcut to paste your most recent dictation.
3. **Press "enter" then immediately hit "escape".** In Claude Code, hit "enter" to submit your prompt, then "escape" to cancel. You'll be back in the edit box for your prompt, with the full text expanded. In Codex, hit "enter" then "escape" twice, then "enter" again.

For now, neither Claude Code nor Codex has an option to disable this feature entirely.[1](#user-content-fn-1)

## Footnotes

1. A Codex developer recently [considered and rejected the idea](https://github.com/openai/codex/issues/17332). [↩](#user-content-fnref-1)
