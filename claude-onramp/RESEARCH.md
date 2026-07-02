# Research notes (2026-07-02)

Facts the guide relies on, gathered via web search before drafting. **All of
this drifts — reverify against the linked official sources before publishing,
especially prices, plan names, and install commands.**

## Claude Code
- **Install** — Mac: `curl -fsSL https://claude.ai/install.sh | bash`; Windows
  (PowerShell): `irm https://claude.ai/install.ps1 | iex`. No Node/git required
  to install. Sign in by running `claude` → browser auth → pick account.
- **Permission modes** — `default` (prompts; the default), `acceptEdits`
  (auto-applies edits), `plan` (read-only). **Shift+Tab** cycles
  default→acceptEdits→plan. `auto` is a broader research-preview mode gated on
  account eligibility + Sonnet 4.6/Opus 4.6. `--dangerously-skip-permissions`
  = bypass everything (containers/VMs only).
- **Skills** — folder + `SKILL.md` in `~/.claude/skills/` (or project
  `.claude/skills/`); invoke `/name`.
- Source: https://code.claude.com/docs/en/quickstart, /permission-modes, /skills

## Claude Cowork
- In the Claude **desktop app** (claude.com/download), "Cowork" tab. First run
  downloads a ~2 GB sandbox. On **paid** plans (Pro/Max/Team-premium/Enterprise)
  — **not Free or Team Standard**.
- **Windows** needs Hyper-V "Virtual Machine Platform" enabled (Turn Windows
  features on or off → restart); Windows 10 22H2+. Mac: no setup (Apple
  Virtualization). *(22H2 / 2 GB figures are third-party, medium confidence.)*
- **Connectors:** app menu → Connectors → Manage connectors → Google
  Drive/Gmail/Calendar → OAuth. Built-in Google connectors are largely
  **read-only**; writing needs an MCP/CLI. Enterprise Google accounts need admin
  allowlisting.
- **Limitations:** Linux VM (no macOS `open`, no host apps); filtered network
  egress (no arbitrary POST); browser automation drives host Chrome via
  extension, not in-VM. **CLI auth (gh/gcloud login) inside the VM: plausibly
  blocked but NOT officially documented — stated softly in the guide.**
- **Skills:** yes; built-in pdf/docx/pptx/xlsx/canvas; custom via `SKILL.md`.
- Source: https://www.anthropic.com/product/claude-cowork ;
  https://support.claude.com/en/articles/13345190 ,
  /articles/14479288 (architecture), /articles/10166901 (Google connectors)

## Superconductor (super.engineering)
- Native **macOS** app (Apple Silicon), runs many coding-agent sessions in
  parallel over isolated git worktrees, with built-in diff/review + one-click
  PR. Agent-agnostic (drives Claude Code etc. as subprocesses with **your own**
  auth). **Free during alpha**; no published paid tier. Windows/Linux planned,
  not yet available.
- **Do not conflate** with superconductor.com (a separate cloud product; the
  "$20 free credits" offer is theirs, not super.engineering's).
- Source: https://super.engineering , https://github.com/oscardobsonbrown/superconductor
  *(super.engineering blocked automated fetch — verify pricing/prereqs on the
  live site before publishing.)*

## Google Workspace CLIs + Google Cloud setup
- **`gog`** (gogcli.sh, repo github.com/openclaw/gogcli) — broad: Gmail,
  Calendar, Drive, Docs, Sheets, more. **`gdoc`** (github.com/LucaDeLeo/gdoc) —
  focused Google Docs/Sheets editing for agents (markdown round-trip, comments,
  revisions, conflict guards, token-efficient).
- Both need **your own Google Cloud project + OAuth "Desktop app" credentials.**
  Setup ~5–15 min: create project → enable APIs → configure OAuth consent screen
  → create Desktop credentials → download JSON → run tool's auth.
- **Publish gotcha:** consent screen left in "Testing" (External) → Google
  **revokes tokens every 7 days.** Fix: set to "In production" (personal use is
  fine without full verification) or "Internal" for a Workspace org.
- Source: https://gogcli.sh , https://github.com/LucaDeLeo/gdoc ,
  https://support.google.com/cloud/answer/15549945

## Claude plans (volatile — check claude.com/pricing)
- Free $0 (no Code/Cowork) · Pro ~$20 (unlocks Code + Cowork) · Max 5× ~$100 /
  20× ~$200 (more usage) · Team ~$25–125/seat (SSO, admin, shared billing;
  **Cowork on premium seats, not Standard**) · Enterprise custom.
- **Team** = org governance/SSO/shared billing. **Max** = personal usage
  ceiling. Some heavy users keep both.
- Source: https://claude.com/pricing ; support.claude.com articles 11049741
  (Max), 9266767 (Team)
