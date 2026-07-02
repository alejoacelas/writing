# Onramp — plan

A guide that takes someone from "I've used Claude in a browser" to "I delegate
real work to Claude Cowork and Claude Code." Smart audience, zero setup
experience. This file is the plan; nothing is implemented yet.

## The shape of the thing

Three kinds of page, strictly separated:

1. **Mainline** — the steps. One path, opinionated, no branching prose. A user
   who never hesitates reads only this, and it reads like a good recipe.
2. **Decision pages** — wiki-style. Wherever the mainline states a default
   ("use a Team account", "use Opus", "use auto mode"), the default links to a
   page with the considerations and a final recommendation. The mainline never
   argues; the decision page does.
3. **Stuck modules** — collapsed inline expanders at the exact point of
   friction ("A dialog is asking for your password — that's normal, here's
   why"). Invisible unless you hesitate. Every module ends the same way:
   "Still stuck? Tell the assistant what you see."

Plus a **sidebar assistant** on every page (spec below).

This separation is what lets the writing satisfy both core principles at once:
the mainline stays hard-to-summarize short, while the anticipation of stuck
points lives one click away instead of clogging the prose.

## Writing rules

- Paul Graham test: if a section can be summarized without losing anything,
  the section is too long. Push shorter until something important would fall
  out, then stop.
- Introduce each concept once, at the moment it's first needed, in the fewest
  words that make the next action make sense. Never front-load a "concepts"
  chapter.
- Concepts ride on actions: you learn what a model is while picking one, what
  a permission is while granting one, what git is while Claude commits.
- Tone: Peter Hartree's concision and directness (`upcoming/ph/` is the
  reference corpus), plus the stuck-point anticipation he mostly skips.
- Assume intelligence, not knowledge. Never explain why something matters at
  length; never assume they know what a terminal is.

## Guide outline

### Part 0 — Orientation (one page, ~150 words)

You already know Claude the chatbot. This guide gives Claude hands: first your
files and apps (Cowork), then your whole computer (Claude Code). By the end
you'll hand it real work — "reconcile these invoices", "draft the report from
these transcripts" — and review results instead of doing tasks.

One choice up front: **account**. Default: your Claude Team account; personal
Max works too. → *Decision page: Team vs personal, and which tier.*

### Part 1 — Claude Cowork

1. **Install the Claude desktop app.** Mac / Windows tabs. Windows includes
   the virtualization/VM setup step. ⚑ *needs research: current Windows Cowork
   requirements.* Stuck modules: OS security dialogs ("App downloaded from the
   internet…" — what's normal to approve), corporate-managed laptop blockers.
2. **First delegation.** A concrete starter task on a folder they give Cowork
   access to — e.g. point it at a messy folder: "make an inventory of what's
   in here and propose an organization." Concept introduced: *the agent works
   in a folder you hand it; it acts, then shows you.* Chosen so the payoff is
   visible in one minute and mistakes don't matter.
3. **Models.** Introduced here because the picker is now visible. Colleague
   analogy: Opus is the senior colleague, Sonnet the fast one, Haiku the
   instant one. Default: Opus for anything you care about. → *Decision page:
   which model, and when speed beats depth.*
4. **Permissions.** Cowork asks before doing anything irreversible (send,
   publish, delete). Concept: *you're not approving competence, you're
   approving consequences.* One line on why it's fine to say yes a lot. →
   *Decision page: how much to trust the agent (includes the
   prompt-injection reassurance, borrowing PH's risk framing).*
5. **Connectors.** Connect Google Drive; then Gmail and Calendar. Concept:
   *a connector is an account you've plugged in; Claude can then act there
   with the same permission prompts.* → *Decision page: which connectors are
   worth it.* Stuck module: the OAuth dance ("a browser tab opened — approve
   there, come back here").
6. **Context windows.** Introduced at the moment it bites: long chats degrade;
   start fresh per task; the folder is the memory, not the chat. This is the
   last concept Cowork needs.
7. **What Cowork can't do.** One honest paragraph (no POST requests, no CLI
   auth, sandboxed VM — condensed from PH's Cowork-limitations post). This is
   the bridge: everything on that list is the reason Part 2 exists.

### Part 2 — Claude Code

1. **Why graduate.** Claude Code is the same colleague without the sandbox:
   any tool your computer runs, real network access, long autonomous runs.
   Costs you: a terminal and ~30 minutes of setup.
2. **The terminal.** 50 words: it's a chat window for your computer; you type,
   it answers; that's it. You will mostly watch Claude type into it.
3. **GitHub account + git.** Framed as *save-points, not engineering*: git
   means every change Claude makes is undoable, which is what makes auto mode
   safe. Stuck modules: the git installer's wall of yes-yes-yes dialogs
   (Windows), `xcode-select` popup (Mac), GitHub 2FA/passkey signup steps.
4. **Install Claude Code, sign in.** ⚑ *needs research: current recommended
   install path (native installer vs npm) per OS.* Stuck modules: "command
   not found" (restart terminal), PATH issues.
5. **First session.** Run it in a folder, give the same starter task as
   Cowork got — the contrast *is* the lesson. Then a task Cowork couldn't do.
6. **Auto mode.** Default: accept-edits/auto on your local machine. The
   argument (one line in mainline): permission fatigue costs more than the
   risk, given git save-points. → *Decision page: permissions philosophy —
   spectrum from paranoid to YOLO, where we land and why (PH's whitelist post
   is the seed).* ⚑ *needs research: exact current mode names and defaults.*
7. **Mac: Superconductor (super.engineering).** The opinionated upgrade: run
   several Claude Code sessions in parallel with an interface that doesn't
   feel like a terminal. → *Decision page: Superconductor vs plain terminal vs
   VS Code; what Windows users should do instead.* ⚑ *needs research: current
   onboarding, pricing, Windows story.*

### Part 3 — Power-ups (optional, each self-contained)

1. **Google Workspace from Claude Code.** The distinction to teach: Cowork's
   connectors are rented hands (Anthropic's servers, capped abilities); a CLI
   like `gog`/`gdoc` is your own hands (full read-write, scriptable, usable in
   skills). You can reuse Cowork's MCPs in Claude Code, so this is optional —
   the gain is everything connectors can't do. → *Decision page: connector vs
   MCP vs CLI, per app.* ⚑ *needs research: current best picks; PH says gdoc
   for Docs, gog for Gmail/Calendar.*
2. **The Google Cloud project.** The one genuinely unpleasant setup in the
   whole guide (~10 min of console clicking). Suggested move: have the Codex
   desktop app do the clicking via computer use while you watch. Critical
   stuck module (from PH): **publish the app** — testing mode logs you out
   every 7 days. ⚑ *needs research: whether Codex computer use reliably
   completes this today; fallback is guided manual steps.*
3. **A first skill.** (Tentative — include only if it fits the
   hard-to-summarize bar.) Teach Claude a recurring task once, reuse forever.

### End state

Close with a "now what" page: the 5x rule (anything you do 5+ times, ask
whether Claude can), three example delegations matched to the reader's likely
work, and a pointer back to the assistant for anything else.

## Stuck-module inventory

The support layer, drafted once and reused. Each ≤5 lines + assistant handoff:

- OS install dialogs: what's normal to approve, on both OSes.
- Windows terminal copy-paste (Ctrl+Shift+C/V, right-click paste) — placed
  everywhere we say "paste the result".
- Mac Terminal folder-access prompts.
- "Command not found" after installing anything.
- OAuth flows that open a browser and seem to do nothing.
- 2FA/passkey walls during signups.
- Managed/corporate laptop: what needs IT, how to ask.
- Hitting usage limits mid-task.
- Screenshot how-to (Cmd-Shift-4 / Win-Shift-S) — feeds the assistant flow.

## Decision-page inventory

Team vs personal account · which model · which connectors · how much to trust
the agent (permissions + prompt injection) · Cowork vs Claude Code for a given
task · Superconductor vs terminal vs IDE · connector vs MCP vs CLI for Google
Workspace. Each: considerations, then a committed recommendation — never "it
depends" as the last word.

## Sidebar assistant

- **Context**: full guide text in the system prompt — a hard budget that
  reinforces the concision rule — plus the page the user is on.
- **Web search** restricted to an allowlist (claude.com docs & support,
  github.com docs, super.engineering, gogcli.sh, and the like).
- **Diagnostic habit**, in the system prompt: prefer "run this and paste the
  output"; whenever it asks for terminal output or a screenshot, it appends
  the per-OS copy-paste/screenshot instructions unprompted.
- **Screenshot-first**: prominent paste/upload affordance; the assistant is
  told screenshots beat descriptions and should ask for them.
- **Feedback capture** (workspace principle: build in the loop): a one-tap
  "this step didn't work for me" on every mainline step, logging step + OS +
  optional note. That log is the queue for new stuck modules.

Implementation sketch, when we get there: static site (Astro or Next.js),
assistant as one API route calling Claude (Opus) with the guide as system
prompt and the `web_search` tool's domain allowlist. No accounts, no DB beyond
the feedback log.

## Process

1. Draft the mainline end-to-end first — no modules, no decision pages. Get
   the spine readable in one sitting (~15 min).
2. Run the PG test per section; cut.
3. Add stuck modules from the inventory; add decision pages.
4. Dogfood on a clean machine (fresh Mac user account; Windows VM).
5. Watch 2–3 real target users go through it; every place they hesitate
   becomes a module; every question they ask the assistant that it fumbles
   becomes an assistant-prompt fix.
6. Build the site last — the guide must work as plain markdown first.

## Research flags (⚑ recap — do before drafting the affected sections)

1. Cowork on Windows: exact current VM/virtualization steps.
2. Claude Code install: current recommended method per OS.
3. Permission modes: current official names, what "auto" precisely is.
4. Superconductor: onboarding, pricing, Mac-only?
5. Google Workspace tooling: current best CLI/MCP picks and setup steps;
   whether a GCP project is still required for gog/gdoc.
6. Codex desktop computer use: can it reliably complete the GCP console flow?
7. Team vs personal plans: current tiers, limits, prices.

## Guesses I made (easy to reverse)

- **Name: `onramp`**, at the root of `writing/` since you said "put it on the
  folder here". Alternative: `upcoming/2026-07-onramp/` per the workspace
  default — one `mv` to change.
- **Three-page-type architecture** (mainline / decision / stuck) as *the*
  organizing idea. Alternative: single pages with inline collapsibles only,
  no separate decision pages — simpler site, muddier writing.
- **Cowork before Claude Code**, same starter task in both so the contrast
  teaches. Alternative: parallel tracks with a chooser up front.
- **Git framed as save-points** and taught implicitly. Alternative: skip
  GitHub entirely until a task needs it — lighter Part 2, but weakens the
  auto-mode safety argument.
- **Skills left tentative** in Part 3; cut them if they bloat.
- Starter task = messy-folder inventory. Alternative: transcript → summary
  doc, closer to real knowledge work but needs the user to have a transcript.
