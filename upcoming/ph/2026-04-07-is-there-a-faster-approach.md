# It is often worth asking: is there a faster approach?

*Source: https://wow.pjh.is/journal/is-there-a-faster-approach*  ·  *Published: 2026-04-07*

---

For long, complex tasks, it's often worth saying:

This is especially worth doing when Claude is using Chrome for data extraction—you may be able to cut task duration from 10+ minutes to seconds.[1](#user-content-fn-1)

It's also good if you're running a series of steps that could be parallelised, since Claude often forgets it can do this (especially for non-programming tasks).

I've added the following to my global `AGENTS.md`:

```
## Task efficiency

- **Delegate to faster models:** For straightforward lookup-and-summarise tasks (e.g. searching email, reading a series of messages, fetching billing amounts), delegate to a Haiku subagent rather than doing it on Opus. Save Opus for tasks that require judgement, planning, or complex reasoning.

- **Parallel processing:** When handling multiple independent items, use parallel subagents rather than sequential loops.

- **Browser automation:** For repetitive or multi-step browser interactions, consider using JavaScript injection to replace screenshot-click cycles. For data extraction or bulk operations, look for the page's underlying API.

```

## Footnotes

1. For example, I recently wanted to scrape data from an event listing website. The "is there a faster way?" nudge cut the task duration from \~10 mins to 3 seconds, because Claude decided to reverse engineer the data API rather than click through the web interface. The task needed to be done in Chrome browser because the event data was behind a login wall, so Claude wrote a script and injected it into the web page. [↩](#user-content-fnref-1)
