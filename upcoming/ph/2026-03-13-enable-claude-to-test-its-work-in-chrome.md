# Enable Claude to test its work in Chrome

*Source: https://wow.pjh.is/journal/enable-claude-to-test-its-work-in-chrome*  ·  *Published: 2026-03-13*

---

You should give your coding agent everything it needs to fully test its work _before_ it submits for your review. This saves a bunch of time.

Often, to do a full test, the agent needs to open a web browser and _actually use_ your app.

To give Claude Code this ability:

1. Type `/chrome` in Claude Code (or go to `Settings > Connectors` in Claude Desktop).
2. Select "Enabled by default".

Then, when making plans, tell Claude "test in Chrome".

Claude for Chrome uses your regular Chrome profile. This avoids hassle from bot-blockers and login walls. The security:convenience tradeoff makes sense for most people.

If you need to test a browser extension, use [this skill](https://github.com/HartreeWorks/skill--chrome-extension-dev).

**Power user?** Try [Playwright CLI](https://github.com/microsoft/playwright-cli) or [Stagehand](https://github.com/browserbase/skills).
