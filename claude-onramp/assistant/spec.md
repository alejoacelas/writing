# Sidebar assistant — behavior & build spec

The guide ships with an assistant docked in the sidebar of every page. Its job:
unstick people fast, without breaking their flow. This file specifies behavior;
the draft system prompt is in [`system-prompt.md`](system-prompt.md).

## Behavior

- **Full guide in context.** The entire guide text is in its system prompt, plus
  the title of the page the user is on. It answers from the guide first.
- **Diagnostic by habit.** It prefers "run this and paste the output" or "send a
  screenshot" over guessing — and whenever it asks for terminal output or a
  screenshot, it appends the exact keys for the user's OS, unprompted. (This is
  why the copy/paste/screenshot instructions live in the system prompt.)
- **Screenshot-first.** A prominent paste/upload affordance; the assistant is
  told images beat descriptions and to ask for one when a user is stuck.
- **One step at a time.** Next single action, then wait — never a ten-step dump.
- **Restricted web search.** Allowed to search, but only within an allowlist
  (Claude/Anthropic docs & support, GitHub docs, super.engineering, gogcli.sh,
  wisprflow.ai, and similar). Guide first; search only to confirm a current
  detail.

## Feedback loop (the important part)

Every mainline step carries a one-tap **"this step didn't work for me"** control.
A tap logs: which step, the user's OS, and an optional note. That log is the
queue for new stuck-modules — the guide improves from observed friction, not
from guessing. This is the whole reason the assistant is worth building rather
than shipping static pages: it's the sensor that tells us where people actually
get stuck.

Two streams feed the same queue:
1. Explicit "didn't work" taps (step + OS + note).
2. Questions the assistant itself fumbles or has to search for — logged for
   review, since each one is a gap in the guide.

Weekly, whoever maintains the guide reads the queue and turns the top items into
new stuck-modules or mainline fixes.

## Build sketch (do this last)

The guide must work as plain markdown first; the site is a presentation layer.

- **Static site** (Astro or Next.js) rendering the markdown files in this repo.
  Sidebar nav from the file order; stuck-modules render as collapsible blocks
  (they're already `<details>` in the markdown, so they work even with no site).
- **Assistant** = one API route calling Claude (Opus) with
  `system-prompt.md` + the concatenated guide as the system prompt, and the
  `web_search` tool restricted to the domain allowlist. Streaming response.
- **Feedback** = a tiny endpoint appending `{step, os, note, timestamp}` to a
  log (a file or a single table). No user accounts; nothing else persists.
- **Cost/keys** = the assistant needs an API key and a deploy target. That's the
  one step that spends money and exposes a surface, so it's deliberately last
  and gated on a human decision.
