# Prompt: zero-to-delegation guide for Claude Cowork and Claude Code

Create a getting-started guide that takes people from zero — they've used LLMs
only from a browser chat interface, quite possibly only Claude, never touched a
setting, don't know Opus from Sonnet — to confidently delegating important
tasks to Claude Cowork and Claude Code. The audience is extremely smart, so the
final level we aim for is high; we just introduce concepts one at a time and
explain as we go, woven into the act of installing and using the tools.

Rough contents I have in mind:

- Install the Claude desktop app and get Cowork running (Windows people have
  some virtual machine setup step).
- Connect Cowork to Google Drive and maybe a few other connectors; explain
  permissions.
- Note that most users will be on a Claude Team account, but some on personal —
  one of several places where we state a default and link, wiki-style, to a
  page giving the considerations and a final recommendation.
- For Claude Code: set up a GitHub account (fast), install, run it in auto mode
  on their local machine. For Mac users, opinionated suggestion:
  superconductor / super.engineering — really intuitive.
- Optional connectors for Claude Code: Google Workspace and the gog CLI.
  Explain the difference from Cowork's connectors — what extra you gain — since
  you can reuse the same MCPs from Cowork in Claude Code. Suggest using the
  Codex desktop app (its computer use is good) to click through the Google
  Cloud project credential setup, which involves a lot of uncomfortable
  clicking around.

Core principles:

1. **Proactively address stuck points, modularly.** Anticipate the places a
   user might get stuck (permission dialogs when installing git, Windows
   copy-paste in terminals, etc.) and address them — but keep that support
   short and modular, so the mainline reads fluidly for users who just want to
   do the thing. Hesitant users click/interact to get support.
2. **Hard-to-summarize writing.** Paul Graham's test: writing so distilled that
   any summary loses something important. Push constantly shorter; stop only
   when shortening would drop something important.
3. **Opinionated defaults, reasoning one click away.** State the default in the
   mainline; link to a wiki-style page with the considerations and a final
   recommendation.

The website should have a sidebar assistant with the full guide loaded in
context, web search restricted to a set of domains, easy screenshot sharing,
and the habit of suggesting ways users can feed it context ("run this command
and paste the result here") — again proactively smoothing what might stop them
(e.g., confusing Windows terminal copy-paste commands).

Don't implement anything yet — write a plan first. Style inspiration for
concision and clarity: Peter Hartree (writing in `upcoming/ph/`), though he
mostly doesn't do the proactive stuck-point support we want.
