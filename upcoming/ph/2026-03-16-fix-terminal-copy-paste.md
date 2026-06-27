# Remove unwanted new lines when copy-pasting from a narrow Terminal pane

*Source: https://wow.pjh.is/journal/fix-terminal-copy-paste*  ·  *Published: 2026-03-16*

---

Hopefully, your work sessions often look like this:

But with lots of narrow panes, text wraps. And then, when you copy-paste a URL, you end up with something like this:

```
https://wow.pjh.is/journal/google-cloud-
  console-setup-for-cli-tools

```

The line was wrapped to fit the pane width, and clipboard preserved the newline. Broken link. 🤦

Same thing happens with commands.

## The fix

A [script](https://github.com/HartreeWorks/scripts--clipboard-unwrap-from-terminal) that:

1. Monitors the clipboard when Warp, Terminal, or iTerm2 is frontmost.
2. Detects soft-wrapped text, and silently rejoins it.
