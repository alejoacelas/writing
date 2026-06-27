# Skill: use a web browser to review tax messages on a government portal

*Source: https://wow.pjh.is/journal/claude-skill-computer-use-urssaf*  ·  *Published: 2025-12-15*

---

As a tax-resident in France, I get 30-50 emails a year that look like this:

In >80% of cases, no action is required. But to determine that, I have to log into the portal, wait for it to load (\~5 seconds), click several buttons, download the PDF, and finally open the PDF to actually read the message.

Could Claude do all this for me?

In short: yes. With less than 30 minutes' work, I created a skill that reliably checks the inbox and gives me an output like this:

All I have to do is say "hey Claude, check my URSSAF messages".

Watch Claude complete the task:[1](#user-content-fn-1)

Here's how I made it:[2](#user-content-fn-2)

Pre-requisites: [Claude Code](https://claude.com/product/claude-code) with the [Browserbase Automation Skill](https://github.com/browserbase/agent-browse). Coding knowledge _not_ required.

**Update 2026-01-16:** Claude Code now has [browser use built-in](https://code.claude.com/docs/en/chrome). So you don't need Browserbase, you can just run `claude --chrome`.

## Footnotes

1. For the first few runs, I keep computer use tasks running on one of my [LLM screens](https://wow.pjh.is/journal/llm-screen). But once I trust them, I just hide them and wait for Claude to let me know when it's done. [↩](#user-content-fnref-1)
2. I'm sorry for the audio quality. Forgot to use [the lapel](https://wow.pjh.is/journal/lapel-mic). [↩](#user-content-fnref-2)
