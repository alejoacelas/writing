# Create keyboard shortcuts for any web app

*Source: https://wow.pjh.is/journal/shortcuts-for-any-web-app*  ·  *Published: 2025-12-02*

---

Many web apps are missing _so many keyboard shortcuts_. 😭

But: you can add them! You just have to make a browser extension.

Browser extensions are harder to vibe-code than other software, because:

1. You're modifying an existing app with features that you can't control.
2. Your coding assistant can't see the code of the app you want to modify (unless you share it).
3. Installing and sharing custom browser extensions is a bit fiddly.

So, I've written a [Claude Skill](https://wow.pjh.is/journal/claude-skills) to make it much easier—even for someone with minimal coding experience—to add shortcuts to any web app.

## Demo: add shortcuts to Salesforce

Let's add the following shortcuts for the Salesforce contact view:

```
CTRL + M: new email
CTRL + E: new event
CTRL + T: new task
CTRL + L: show / hide todo list
CTRL + C: new call 
CTRL + O: new opportunity
CTRL + U: upload file

```

Screencast:

Claude one-shots 6/7 of the shortcuts.

It then helps me debug and fix the remaining one.

The screencast also explains how to share the extension with your colleagues.

If you'd like to try the Salesforce extension, [download the .zip](https://github.com/HartreeWorks/claude-skill-browser-extension/raw/refs/heads/main/salesforce-shortcuts.zip) and then [install](https://www.loom.com/share/49a916423f87471fb082f5c225e3e971?t=211).

## Try this yourself

First, install the Claude Skill:

- **Claude web app:** [download the .zip](https://github.com/HartreeWorks/claude-skill-browser-extension/archive/refs/heads/main.zip) and then [install here](https://claude.ai/settings/capabilities#skills).
- **Claude Code:** tag the [repository URL](https://github.com/HartreeWorks/claude-skill-browser-extension) and say "please install this skill globally".

Second, tell Claude the shortcuts you'd like to add.

## Next steps

If you try this, please [let me know how you get on](mailto:wow@pjh.is)! If you get stuck, I'll try to help.

Keyboard shortcuts are a great place to start, but there's much more you can do to [customise your favourite web apps](https://wow.pjh.is/journal/ph-mods).

## Appendix 1\. Keyboard shortcuts for ChatGPT, Claude, Gemini & Grok

If you've read this far, you might like [BetterChat](https://hartreeworks.org/better-chat).
