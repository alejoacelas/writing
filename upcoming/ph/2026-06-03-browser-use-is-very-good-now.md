# Browser use is very good now

*Source: https://wow.pjh.is/journal/browser-use-is-very-good-now*  ·  *Published: 2026-06-03*

---

Since [April](https://wow.pjh.is/journal/claude-for-chrome-is-much-better-now), [Claude in Chrome](https://claude.com/blog/claude-for-chrome) has become even faster and even more reliable. I now use it routinely for admin tasks, such as:

1. Create invoice on Indy.fr
2. Submit timesheet via Deel
3. Search flights on Skyscanner
4. [Add a hold bag to existing flight booking](https://wow.pjh.is/journal/examples-of-mundane-utility)
5. Find best product on Amazon (with delivery tomorrow)
6. Submit monthly income declarations to tax authorities
7. [Request a product replacement](https://wow.pjh.is/journal/examples-of-mundane-utility)
8. [Add friends to my car insurance](https://wow.pjh.is/journal/examples-of-mundane-utility)

Claude reliably asks before taking important, irreversible actions (e.g. actually submitting a form). I've never seen it fail to do this. So I don't watch Claude work—it runs in the background while I do other things.

It usually completes tasks in 1.5–3x the clock time it'd take me. With some extra setup, it can do some tasks at superhuman speed (see below).

Some issues that still cause friction:

1. It can't upload files.[1](#user-content-fn-1)
2. It often refuses to login to websites on your behalf. So before you delegate a task, you need to make sure your Chrome profile is logged in to the relevant websites.
3. It refuses to enter payment information or interact with banking websites. Probably for the best.
4. When Anthropic's GPUs are melting, things get very slow.

## How to handle authentication

Run Claude in your regular Chrome profile, so if you're logged into a website, it does not need to log in again. This is a bit YOLO, but I trust it. You must grant Claude browsing permission on a per-domain basis, which is a nice guardrail here.[2](#user-content-fn-2)

## Speed up recurring tasks

For recurring tasks, you may be able to speed things up a lot by telling Claude:

For some tasks (e.g. [reconciling 50 transactions in Xero](https://wow.pjh.is/journal/claude-code-does-my-bookkeeping#reconciliation)), scripting interactions can make Claude's task completion much faster than human.

**Coming soon:** It's time I re-tested the "computer use" tools in Claude and Codex. I hear the Codex version is approaching human speed.

## Footnotes

1. This is due to limits on what browser extensions can do, not Claude's capabilities. It'll only be solved with full computer use. [↩](#user-content-fnref-1)
2. If you want to tighten things: use a dedicated Chrome profile with the 1Password CLI. The implementation is nice: you get a "touch to approve" prompt every time the agent requests access to a secret. But, since a recent update, Claude often refuses to login to websites even when asked. [↩](#user-content-fnref-2)
