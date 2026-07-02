# Part 1 — Claude Cowork

Cowork is Claude with hands. You describe an outcome; it plans, works across
your files and connected apps for several steps, and hands back finished work.
It lives inside the Claude desktop app, and it's the fastest way to feel what
delegating to an agent is actually like.

By the end of this part you'll have delegated a few real tasks and picked up the
four ideas the rest of the guide relies on.

## 1. Install the desktop app

Download the Claude desktop app from **[claude.com/download](https://claude.com/download)**
and sign in. Open the **Cowork** tab. The first time you do, Claude downloads a
small sandbox (~2 GB) where it runs its work safely — give it a minute.

<details>
<summary>Your computer is warning you about the app you downloaded →</summary>

That's normal. Any app downloaded from the internet gets a one-time "are you
sure?" check.

- **Mac:** if it says the app "can't be opened because Apple cannot check it,"
  open **System Settings → Privacy & Security**, scroll down, and click **Open
  Anyway**. This is expected for a fresh download.
- **Windows:** if you see a blue "Windows protected your PC" box, click **More
  info → Run anyway**.

You're approving *this* app, which you chose to download. That's fine.
</details>

<details>
<summary>You need Cowork on Windows →</summary>

Cowork runs its sandbox in a lightweight virtual machine, so Windows needs one
feature turned on first. You need **Windows 10 (22H2) or newer**.

If you hit the error **"Virtual Machine Platform not enabled":**
1. Press Start, type **"Turn Windows features on or off,"** open it.
2. Tick **Virtual Machine Platform**.
3. Click OK and **restart** your PC.

Then reopen Cowork. (This is Windows' built-in virtualization — not the same as
WSL, and you don't need to install anything else.)
</details>

<details>
<summary>You're on a work laptop and something's blocked →</summary>

Managed laptops sometimes block new apps or the Google sign-in you'll do in a
minute. If you see "blocked by your administrator" or "access blocked — admin
needs to review," that's IT policy, not you. Ask your IT contact to allowlist
the Claude desktop app (and, for connectors, Claude in the Google Admin
console). The assistant can draft that message for you — just ask.
</details>

## 2. Delegate your first task

Point Cowork at a folder and give it something concrete. A good first task: pick
a messy folder — a downloads pile, an unsorted project — and say:

> *"Look through this folder, tell me what's in it, and propose a way to
> organize it. Don't move anything yet — just show me the plan."*

Watch what happens. Cowork reads the files, thinks, and comes back with a
proposal. That's the whole model in miniature: **you hand it a folder and an
outcome; it works; it shows you.** You stay in the loop by reacting, not by
doing the steps yourself.

Pick something where a wrong answer costs you nothing. The point right now is to
feel the handoff, not to get a perfect result.

## 3. Stop typing — talk to it

The habit that most improves what you get back: **say your request out loud
instead of typing it.** When you type, you tidy up and leave out context. When
you talk, you ramble — and the ramble (why you care, what you're torn about,
what you're unsure of) is exactly what makes the answer fit.

Install a dictation tool and use it for anything longer than a sentence. Our
pick is Wispr Flow. → [Which dictation tool, and why talking beats typing →](decisions/dictation.md)

## 4. Use the best model

Somewhere in the interface is a model picker (Claude's models, fast to most-
capable, are Haiku, Sonnet, Opus). Set it to the best one and leave it there.
The reasons you'd pick a weaker model — speed, cost — both have better answers
than "use a weaker model." → [Why: just use the best model →](decisions/which-model.md)

## 5. Permissions: what you're really approving

Before Cowork does anything with consequences — sending, deleting, sharing — it
asks. The right instinct is simple: **you're not judging whether Claude is
capable; you're judging whether you could undo it.**

- Reversible (editing a file, drafting, reorganizing)? Wave it through.
- Irreversible (sending an email, deleting, publishing)? *That's* the prompt to
  actually read.

Cowork is built to make this safe — it runs in a sandbox and asks before the
scary stuff. → [How much to trust the agent (and why prompt injection shouldn't stop you) →](decisions/trust-and-permissions.md)

## 6. Connect your apps

Cowork gets far more useful once it can reach your email, calendar, and files.
In the desktop app, open the menu → **Connectors → Manage connectors**, and
connect **Google Drive**, then **Gmail** and **Google Calendar**. Each opens a
Google sign-in where you grant access.

A connector is just an account you've plugged in. Once connected, Claude can act
there — with the same permission prompts as everything else.

<details>
<summary>A browser tab opened and I'm not sure what to do →</summary>

That's the normal sign-in ("OAuth") dance. Google opens in your browser, asks
you to pick your account and approve access, then hands you back to Claude.
Approve the access it asks for, and return to the Claude app — the connector
will now show as connected. If the tab seems to hang, come back to Claude
anyway; it often already worked.
</details>

<details>
<summary>Google says "access blocked" or "admin needs to review" →</summary>

On a work Google account, your organization has to allow Claude first. That's an
IT setting (Google Admin console → API controls), not something you can fix from
here. Ask your admin to approve Claude; the assistant can draft the request.
</details>

The built-in Google connectors mostly *read* (search your mail, read a doc). To
have Claude *write* — send mail, edit docs — you'll want the deeper setup in
[Part 3](03-power-ups.md), or Claude Code. → [Which connectors are worth it →](decisions/connectors.md)

## 7. Save everything — ask for a running file

Get in the habit of asking Cowork to **keep a markdown file as it works** — a
running plan, notes, the output so far:

> *"Keep a file called `plan.md` as you go, and update it at each step."*

This isn't housekeeping. It does four things at once:

- **Visibility** — you see the intermediate steps, not just the final answer.
- **Course-correction** — you catch a wrong turn while it's cheap to fix.
- **Specific asks** — you can point at a section and say "redo this part."
- **Reuse** — a good file is something you can hand back tomorrow to pick up
  where you left off.

That last one is the seed of the next idea.

## 8. Teach it once: reusable instructions

Once you've written the same context into three different chats — how you like
things formatted, what your project is, who the audience is — stop retyping it.
Put it in a file (or Cowork's instructions/memory) and point Claude at it. You've
just gone from *re-explaining every time* to *teaching once*. In Claude Code
this becomes a file called `CLAUDE.md` that's read automatically every session
(Part 2); the habit starts here.

## 9. Reuse becomes sharing: skills

A **skill** is a saved capability Claude can reuse by name. Cowork already ships
with some (it knows how to make PDFs, Word docs, slide decks, spreadsheets). You
can add your own: a folder with a `SKILL.md` file describing a task you do often
— "draft the weekly update from these sources," "turn a transcript into a
summary." Cowork discovers it and runs it when it fits.

The pairing to hold onto: **a reusable file is reuse for you; a skill is how
that reuse becomes something you can share** — with your future self, or with a
teammate who just runs it by name. We'll build a real one in Part 2.

## 10. Context windows: start fresh often

Claude reads your whole conversation every time it replies. Long chats get
slower, foggier, and more likely to lose the thread. So **start a new chat for
each new task.** Don't worry about "losing" what mattered — the memory that
counts lives in your files and your reusable instructions, not in the chat
history.

## 11. What Cowork can't do — and why that's fine

Cowork is deliberately fenced so it's safe the moment you install it. The fence
has real edges:

- It runs in a **Linux sandbox**, separate from your actual computer — so it
  can't drive your Mac's apps or touch files outside what you give it.
- Its **internet access is filtered** — it can use official connectors and
  approved tools, but not make arbitrary calls to any service on the web.
- It **can't log into command-line tools** (the `gh`, `gcloud`-style logins
  some workflows need).

None of this is a flaw — it's the trade for "works out of the box, safely." But
every item on that list is exactly what the next tool removes. When you want the
fence gone, you want Claude Code.

**→ [Part 2: Claude Code](02-claude-code.md)**
