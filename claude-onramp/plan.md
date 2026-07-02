# claude-onramp — plan

A guide that takes someone from "I've used Claude in a browser" to "I delegate
real work to Claude Cowork and Claude Code." Smart audience, zero setup
experience.

> **Status (2026-07-02): first full draft written.** Guide content lives in the
> numbered `NN-*.md` files, `decisions/`, and `assistant/`; `site/index.html` is
> the rendered version (rebuild with `python3 site/build.py`). Research flags
> below were resolved via web search before drafting — see
> [`RESEARCH.md`](RESEARCH.md) for the sourced facts and their freshness
> caveats. Still to do: dogfood on a clean machine, watch real users, build the
> live assistant. This plan is retained as the design rationale.

---

## The point of the whole thing

Frame borrowed from Alejandro's workshop material, because it's the real reason
to bother: coding agents matter not because they connect to tools or write
code, but because they collapse the friction of *delegating hard tasks* — the
ones too technical, too small, too time-consuming, too draining, or too vague
to start alone. Everything in the guide serves that end state. The reader
should finish able to hand off a task they wouldn't otherwise do, and to
decompose it into steps they can **verify, trust, or not care about**.

Three lessons run underneath the mechanics and surface repeatedly:

- **Talk, don't type.** State the problem, ramble, hedge, name your
  uncertainties. Voice makes this natural.
- **Run many at once.** Agents are slow; you are not idle. Open another tab.
- **Save everything, so you can see and reuse it.** Visibility now, reuse
  later. This is the thread that leads to reusable instructions and skills.

## The shape of the thing

Two guides, three page types, one assistant.

**Two guides, either entry point valid.** Cowork works out of the box (one app,
no terminal). Claude Code does more but costs ~30 min of setup. Cowork is the
recommended on-ramp because it teaches the ideas Code assumes — but a reader who
already gets those ideas should be able to start straight in Claude Code. So the
Code guide opens with a short "you'll want these four intuitions (folders,
models, permissions, context); if you have them, skip ahead; if not, do Cowork
first" affordance. Be genuinely positive about Code as the destination, and
genuinely honest that Cowork is the softer landing.

**Three page types, strictly separated** — this is what lets the writing stay
short while still anticipating every stuck point:

1. **Mainline** — the steps. One opinionated path, no branching prose. A reader
   who never hesitates reads only this.
2. **Decision pages** — wiki-style, behind every stated default. Considerations
   plus a committed recommendation. The mainline never argues; these do.
3. **Stuck modules** — collapsed one-liners at the point of friction, expanding
   in place. Invisible unless you hesitate. (Mechanism detailed below.)

## How stuck modules work

*The part that was underspecified before.*

- **Surface (what the user sees):** under a mainline step likely to snag, a
  muted collapsed line — "Something's asking for your password? →", "On Windows,
  paste isn't Ctrl+V →". Click expands it in place (≤5 lines). Default collapsed
  so the mainline reads clean. Each module ends: "Still stuck? Tell the
  assistant what you see." The assistant is the catch-all.
- **Discovery (how we find which to write), four sources, increasing truth:**
  1. Up-front anticipation — the inventory below.
  2. Dogfooding on a clean machine (see Process).
  3. Watching 2–3 real target users.
  4. The assistant's feedback log — every "this step didn't work" tap and every
     question the assistant fumbles is a candidate module.
  The module set *grows from observed friction*; it isn't guessed once and
  frozen.

## Writing rules

- **Precision first, friendliness later.** Present what the reader needs to
  know; make each sentence carry exact weight. Warmth can be layered on after
  the spine is right — don't reach for it early.
- **Paul Graham test:** if a section survives summary with nothing lost, it's
  too long. Cut until removing more would drop something that changes what the
  reader does.
- **One concept, once, at first need.** No front-loaded concepts chapter.
  Models are explained while picking one; permissions while granting one; git
  while Claude commits.
- **Tone:** Peter Hartree (`upcoming/ph/`) is *inspiration for concision and
  directness, not a template to imitate*. Default to a clear voice I'm
  comfortable sustaining — Alejandro's own workshop writing (precise claim →
  correct the obvious-wrong reason → give the real one) is the closer model for
  register. Anchor to neither; write well.
- Assume intelligence, not knowledge. Never over-explain why something matters;
  never assume they know what a terminal is.

## Guide outline

### Part 0 — Start here (one short page)

**Draft (react to tone/precision):**

> # Start here
>
> This guide gives Claude your files, your apps, and — by the end — your whole
> computer, so you can hand off work instead of doing it.
>
> There are two tools. **Claude Cowork** works out of the box: install one app,
> connect your accounts, delegate. **Claude Code** does more — any tool your
> computer can run, real network access, hours of unattended work — for about
> thirty minutes of setup.
>
> Start with Cowork. It teaches the four ideas Claude Code assumes — folders,
> models, permissions, context — while you install nothing but one app. Already
> have those? Skip to Claude Code.
>
> One choice first: **which account.** Use your Claude Team account. [On
> personal, or unsure which tier? →]

### Part 1 — Claude Cowork

1. **Install the desktop app.** Mac / Windows tabs; Windows carries the
   virtualization/VM step. ⚑ *research: current Windows Cowork requirements.*
   Stuck modules: OS "downloaded from the internet" dialogs; managed-laptop
   blockers.
2. **First delegation.** Point Cowork at a messy folder: "inventory what's here
   and propose an organization." Concept: *the agent works in a folder you hand
   it; it acts, then shows you.* Payoff visible in a minute; mistakes harmless.
3. **Talk, don't type.** Introduced right after the first task, because it
   changes everything downstream. Dictate your requests; ramble and hedge on
   purpose. Recommend **Wispr Flow** as the tool. → *Decision page: dictation
   tools.* This is lesson #1 from the workshop, surfaced early.
4. **Models — just use the best one.**

   **Draft (react — this is the opinion you want stated hard):**
   > A stronger model is worth it on anything you care about. Two reasons you
   > might reach for a weaker one, and what to do instead:
   >
   > - *It's slower.* Don't wait on it — open another tab and set it on the
   >   next piece of work. Speed you buy with parallelism, not with a worse
   >   model.
   > - *It costs more.* It will be worth more than Anthropic charges you. You
   >   may not believe that yet; you will. If you run out of credits, buy more.
   >
   > So: default to the best model, always. [What the tiers actually are →]
5. **Permissions.** Cowork asks before anything irreversible (send, publish,
   delete). **Draft framing (react — unsure this is how you think about it):**
   *"You're not vouching for whether Claude is capable — you're deciding whether
   the consequence is one you'd accept. Reversible thing? Wave it through.
   Irreversible? That's the one to read."* → *Decision page: how much to trust
   the agent, incl. the prompt-injection reassurance (PH's risk framing).*
6. **Connectors.** Connect Google Drive, then Gmail/Calendar. Concept: *a
   connector is an account you've plugged in.* → *Decision page: which
   connectors earn their keep.* Stuck module: the OAuth browser dance.
7. **Save everything → markdown files.** Ask Claude to keep a running markdown
   file as it works. Why this is a load-bearing habit, not housekeeping:
   - **Visibility** — you see the intermediate steps, not just the result.
   - **Course-correction** — you can catch a wrong turn mid-task.
   - **Specific asks** — you can request a particular section or format.
   - **Reuse** — a good file (a plan, a spec, an output) is reusable tomorrow.
   This is the on-ramp to the next idea.
8. **Reusable instructions.** A markdown file you keep pointing Claude at is a
   short step from *teaching Claude how you work once.* Introduce persistent
   instructions here (Cowork's memory/instructions; the CLAUDE.md idea proper
   lands in Part 2). Lesson: reuse beats re-explaining.
9. **Skills — sharing.** Skills package a capability so you (and others) can
   reuse it by name. Cowork can create and run skills. Keep this light in
   Cowork; the deeper treatment is in Part 2. The pairing to teach: *markdown
   files are reuse for yourself; skills are how reuse becomes sharing.* ⚑
   *research: current Cowork skill-creation flow.*
10. **Context windows.** At the moment it bites: long chats degrade; start
    fresh per task; the folder and your files are the memory, not the chat.
11. **What Cowork can't do.** One honest, positive paragraph (no POST, no CLI
    auth, sandboxed Linux VM — condensed from PH's limitations post). Framed as:
    Cowork is deliberately fenced so it's safe out of the box; everything on
    this list is exactly what Claude Code unfences. The bridge to Part 2.

### Part 2 — Claude Code

Opens with the skip-affordance (see "two guides" above).

1. **Why graduate.** Same colleague, no sandbox: any tool, real network, long
   autonomous runs. Cost: a terminal and ~30 min.
2. **The terminal.** ~50 words: a chat window for your computer. You'll mostly
   watch Claude type into it.
3. **GitHub + git as save-points.** Framed as undo, not engineering: every
   change Claude makes is reversible, which is what makes auto mode safe. Stuck
   modules: git installer's yes-yes-yes dialogs; `xcode-select` popup (Mac);
   GitHub 2FA/passkey signup.
4. **Install Claude Code, sign in.** ⚑ *research: current recommended install
   path per OS.* Stuck modules: "command not found" (restart terminal); PATH.
5. **First session.** Same messy-folder task Cowork got — the contrast *is* the
   lesson — then one task Cowork couldn't do.
6. **Auto mode.** Default: accept-edits/auto on your local machine. Mainline
   line: permission fatigue costs more than the risk, given git save-points. →
   *Decision page: permissions philosophy, paranoid→YOLO, where we land (PH's
   whitelist post).* ⚑ *research: exact current mode names/defaults.*
7. **CLAUDE.md — reusable instructions, properly.** The full version of the
   Part 1 idea: a file that teaches Claude how you work, every session. Show a
   small real one. This is the reuse lesson's home.
8. **Skills — sharing, properly.** Build one skill for a recurring task; run it
   by name forever; share it with a teammate. The sharing lesson's home. ⚑
   *research: current skill authoring flow.*
9. **Mac: Superconductor (super.engineering).** The opinionated upgrade: many
   parallel Claude Code sessions in an interface that isn't a raw terminal —
   the "run many at once" lesson, operationalized. → *Decision page:
   Superconductor vs plain terminal vs IDE; what Windows users do instead.* ⚑
   *research: current onboarding, pricing, Windows story.*

### Part 3 — Power-ups (optional, self-contained)

1. **Google Workspace from Claude Code — one lesson, setup included.** Merged
   per your note. Teach the distinction (Cowork connectors = rented hands,
   capped; a CLI like `gog`/`gdoc` = your own hands, full read-write,
   scriptable, usable in skills), *and* walk the setup in the same page —
   including the Google Cloud project (~10 min of console clicking). Suggested
   move: let the Codex desktop app do the clicking via computer use while you
   watch. Critical stuck module (PH): **publish the app**, or testing mode logs
   you out every 7 days. ⚑ *research: current best CLI picks; whether a GCP
   project is still required; whether Codex computer use reliably completes the
   flow (fallback: guided manual steps).*

### End state — "now what"

The 5x rule (anything you'll do 5+ times, ask whether Claude can), three
example delegations matched to the reader's likely work, and the workshop's
decomposition rule stated plainly: for every piece, decide whether you'll
verify it, trust it, or not care. Pointer back to the assistant.

## Stuck-module inventory

Drafted once, reused; each ≤5 lines + assistant handoff:
OS install dialogs (both OSes) · Windows terminal copy-paste (Ctrl+Shift+C/V,
right-click) — everywhere we say "paste" · Mac Terminal folder-access prompts ·
"command not found" · OAuth flows that open a browser and seem to stall ·
2FA/passkey walls · managed/corporate laptop (what needs IT) · hitting usage
limits mid-task · screenshot how-to (Cmd-Shift-4 / Win-Shift-S), feeding the
assistant.

## Decision-page inventory

Each gets a real articulation — short is fine, but every default we assert
carries its reason. Where I'm unsure of *your* reasoning, I'll ask before
writing (flagged ⚑ below):
Team vs personal account ⚑ · which model (best, always — reasoning above) ·
dictation tools · which connectors · how much to trust the agent (permissions +
prompt injection) · Cowork vs Claude Code for a task · Superconductor vs
terminal vs IDE · connector vs MCP vs CLI for Workspace.

## Sidebar assistant

- **Context:** full guide text in the system prompt (a hard budget that
  reinforces concision) + the current page.
- **Web search**, allowlisted (claude.com docs & support, github.com docs,
  super.engineering, gogcli.sh, wisprflow, and the like).
- **Diagnostic habit** in the prompt: prefer "run this and paste the output";
  whenever it asks for terminal output or a screenshot, it appends the per-OS
  copy-paste/screenshot instructions unprompted.
- **Screenshot-first:** prominent paste/upload; told screenshots beat prose and
  to ask for them.
- **Feedback capture:** one-tap "this step didn't work" on every mainline step
  (logs step + OS + optional note). That log is the stuck-module queue — the
  workspace "build in the feedback loop" principle, made literal.

Build sketch (later): static site (Astro or Next.js); assistant as one API
route calling Claude (Opus) with the guide as system prompt and a
domain-allowlisted `web_search` tool. No accounts; only the feedback log
persists.

## Process

1. Draft the mainline end-to-end — no modules, no decision pages — until the
   spine reads in one sitting.
2. PG-test each section; cut.
3. Add stuck modules and decision pages.
4. **Dogfood on a clean machine.** You have a second Mac — that's the real
   test: a fresh macOS user account, follow the guide verbatim, log every
   hesitation. Automating it is hard (real installs, real OAuth, real
   dialogs); the realistic version is a scripted-but-manual runbook we execute
   on the second Mac and, for Windows, a throwaway VM. ⚑ *open question: how
   much of this can be driven by Claude-for-Chrome / Codex computer use vs.
   must be human hands — worth a spike.*
5. Watch 2–3 real target users; every hesitation → a module; every assistant
   fumble → a prompt fix.
6. Build the site last; the guide must work as plain markdown first.

## Research flags (⚑ — resolve before drafting the affected section)

1. Cowork on Windows: current VM/virtualization steps.
2. Claude Code install: current recommended method per OS.
3. Permission modes: current official names; what "auto" precisely is.
4. Superconductor: onboarding, pricing, Mac-only?
5. Workspace tooling: current best CLI/MCP picks; is a GCP project still
   required; does Codex computer use complete the console flow reliably.
6. Skills: current authoring flow in both Cowork and Code.
7. Team vs personal plans: current tiers, limits, prices.

## Decisions from your feedback (locked)

- Name → **`claude-onramp`** (done, folder renamed).
- Models → hard opinion: best model always; buy speed with tabs, cost with
  credits.
- Google Workspace + Google Cloud project → **one merged lesson.**
- Claude Code guide → **startable independently**, with a skip-affordance for
  readers who already have the four intuitions.
- Reuse/share arc → **markdown files (visibility) → CLAUDE.md (reusable
  instructions) → skills (sharing)**, seeded in Cowork, deepened in Code.
- Voice → **first-class**, introduced early, Wispr Flow recommended.
- Tone → PH is inspiration, not anchor; write in a comfortable clear voice.

## Guesses still open (easy to reverse)

- **Skills = one session vs. a broader "sharing" session.** I've drafted it as
  the sharing end of a reuse→share arc (markdown → CLAUDE.md → skills) rather
  than a standalone skills tutorial, because that ties it to the visibility
  habit you care about. Alternative: a dedicated skills chapter. Tell me which.
- **Voice as its own step** (Part 1 step 3) vs. a recurring aside. I made it a
  step; easy to demote.
- **Starter task = messy-folder inventory.** Alternative: transcript → summary
  doc (closer to real knowledge work, needs the reader to have a transcript).
- **Permissions framing** ("consequences, not competence") — drafted above;
  swap freely if it's not how you think.
