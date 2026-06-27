# Use gdoc to edit Google Docs

*Source: https://wow.pjh.is/journal/use-gdoc-for-google-docs*  ·  *Published: 2026-03-16*

---

The [gdoc CLI](https://github.com/LucaDeLeo/gdoc) is better than the main alternatives.[1](#user-content-fn-1) In particular, it can:

- Edit any part of a Google Doc, including specific tabs.
- Make edits with proper formatting—headings, bullets, bold, italic, links, tables, etc.

With this, I can _finally_ [fully automate](https://github.com/HartreeWorks/skill--summarise-granola/blob/main/SKILL.md) the process from transcribing a call through to putting a summary into (the right place in) [my meeting doc](https://notes.pjh.is/useful/The+meeting+doc+and+person+log), and emailing it to participants.

FYI: both `gdoc` and `gog` can read comment threads, with proper author attribution.

## Footnotes

1. These are: [gog](https://gogcli.sh/), Claude's built-in [Google Docs connector](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors), the [semi-official Google Workspace CLI](https://github.com/googleworkspace/cli), and the [Google Workspace MCP](https://wow.pjh.is/journal/claude-code-google-workspace-mcp). Strictly speaking `gog` can be wrangled into doing everything that `gdoc` can do, but it's awkward (lots of commands needed), so your agent will constantly fall over. [↩](#user-content-fnref-1)
