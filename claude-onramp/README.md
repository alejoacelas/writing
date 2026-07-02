# Claude On-Ramp

A guide that takes a smart, non-technical person from *using Claude in a
browser* to *delegating real work to Claude Cowork and Claude Code.*

## Read it

Start at **[00-start-here.md](00-start-here.md)** and follow the links. Reading
order:

1. [Start here](00-start-here.md)
2. [Part 1 — Claude Cowork](01-cowork.md)
3. [Part 2 — Claude Code](02-claude-code.md)
4. [Part 3 — Power-ups](03-power-ups.md) *(optional)*
5. [Now what — actually delegating](04-now-what.md)

Or open **[`site/index.html`](site/index.html)** for the rendered version, with
a working sidebar and collapsible help.

## How it's built

Three kinds of page, kept strictly separate so the main path stays short while
still catching everyone who gets stuck:

- **Mainline** (the numbered parts) — one opinionated path. A reader who never
  hesitates reads only this.
- **Decision pages** ([`decisions/`](decisions/)) — the reasoning behind each
  default the mainline asserts. Linked, never inlined.
- **Stuck-modules** — collapsible `<details>` blocks at each likely snag point.
  Invisible unless you open them.

Plus a **sidebar assistant** with the whole guide in context — spec in
[`assistant/`](assistant/).

## Status

First full draft, 2026-07-02. Content is written and accurate to research done at
draft time; **prices, plan names, and install commands drift — verify against
official sources before publishing.** See [`plan.md`](plan.md) for the design
rationale, open decisions, and the dogfooding process still to run.
