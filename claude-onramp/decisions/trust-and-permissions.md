# How much should you trust the agent?

Both Cowork and Claude Code will ask your permission before doing certain
things, and you get to decide how much to wave through. Here's how to think
about it.

## What you're actually deciding

When a permission prompt appears, you're **not** judging whether Claude is
competent enough to do the thing. You're judging one question: **if this goes
wrong, can I undo it?**

- **Reversible** — editing a file, writing a draft, reorganizing a folder,
  reading things. Let these through freely. If Claude gets it wrong, you fix it
  or revert it in seconds. Stopping to approve each one costs you more than the
  mistakes ever will.
- **Irreversible or outward-facing** — sending an email, publishing, paying,
  deleting something not in version control. *These* are the prompts to
  actually read. The cost of a mistake here isn't "undo"; it's a message you
  can't unsend.

This is why, in Claude Code, we recommend turning on auto-accept for edits (see
below): once your work is under git, every edit is reversible, so approving each
one is pure friction guarding against nothing.

## The prompt-injection worry

Many people hesitate to connect their email or let an agent browse the web
because of *prompt injection* — the fear that a malicious web page or email
could smuggle in an instruction that hijacks your assistant into leaking data
or spending your money.

The honest state of things (mid-2026): this attack is real in theory and
**vanishingly rare in practice.** Across the major assistants from Anthropic,
OpenAI, and Google, there have been no publicly documented cases of large
financial harm from it. The labs are, for now, winning the defense-vs-offense
race, and your realistic chance of six-figure harm this year is well under one
in a thousand. Ordinary user error — you telling it to do the wrong thing — is
more than ten times likelier to cause you trouble.

That may change as attackers put more effort in. But today the calculus is
clear: **connect your accounts and enable browsing.** The productivity is real
and immediate; the injection risk is speculative and tiny. Spend your caution
on the irreversible-action prompts above, not on whether to plug in at all.

## The spectrum, and where we land

- **Paranoid:** a dedicated VM or container per project, strict allowlists.
  Reasonable for some; overkill for most.
- **Our default:** allow the reversible freely, keep prompts on the
  irreversible, keep your work in git so "undo" is always available.
- **YOLO:** skip all permission checks (`--dangerously-skip-permissions`). Too
  risky on your real machine; fine only inside a throwaway sandbox.

Land in the middle. It's where the friction and the risk are both low.
