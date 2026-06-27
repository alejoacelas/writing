# Every tip Claude Code shows while it works

*Source: https://wow.pjh.is/journal/claude-code-spinner-tips*  ·  *Published: 2026-05-26*

---

While Claude Code is thinking, it sometimes shows a tip next to the spinner. Here's the full set, as of version v2.1.150.

## Workflow

- Run `claude --continue` or `claude --resume` to resume a conversation.
- Ask Claude to create a todo list when working on complex tasks to track progress and remain on track.
- Say "fan out subagents" and Claude sends a team. Each one digs deep so nothing gets missed.
- Use `--agent <agent_name>` to directly start a conversation with a subagent.
- Use git worktrees to run multiple Claude sessions in parallel.
- Running multiple Claude sessions? Use `/color` and `/rename` to tell them apart at a glance.
- Create skills by adding .md files to `.claude/skills/` in your project or `~/.claude/skills/` for skills that work in any project.

## Slash-command nudges

- `/loop` runs any prompt on a recurring schedule. Great for monitoring deploys, babysitting PRs, or polling status.
- Set an objective with `/goal`—Claude keeps working until it's met. (Variant: Use `/goal all tests pass` and Claude keeps going until they do. Step away and come back to a finished task.)
- Use `/memory` to view and manage Claude memory.
- Use `/theme` to change the color theme.
- Use `/statusline` to set up a custom status line that will display beneath the input box.
- Use `/permissions` to pre-approve and pre-deny bash, edit, and MCP tools.
- Use `/voice` to enable push-to-talk dictation.
- Use `/agents` to optimise specific tasks, e.g. Software Architect, Code Writer, Code Reviewer.
- Use `/feedback` to help us improve!
- Name your conversations with `/rename` to find them easily in `/resume` later.
- Run `/team-onboarding` to turn your Claude usage into an onboarding guide—share it with your team in one link.

## Keyboard and terminal

- Hit shift+tab to cycle between default mode, auto-accept edit mode, and plan mode.
- Press Shift+Enter (or Option+Enter on Apple Terminal) to send a multi-line message.
- Run `/terminal-setup` to enable Shift+Enter (or Option+Enter) for new lines.
- Use ctrl+v to paste images from your clipboard.
- Paste images into Claude Code using control+v (not cmd+v!).
- Did you know you can drag and drop image files into your terminal?
- Double-tap esc to rewind the conversation to a previous point in time.
- Double-tap esc to rewind the code and/or conversation to a previous point in time.
- Hit Enter to queue up additional messages while Claude is working.
- Send messages to Claude while it works to steer Claude in real time.
- Try setting environment variable `COLORTERM=truecolor` for richer colors.
- Set `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` to enable the PowerShell tool (preview).
- Try smoother rendering, lower memory usage, mouse support, and better formatting of copied text · `/tui fullscreen`.

## Integrations and surfaces

- Open the Command Palette (Cmd+Shift+P) and run "Shell Command: Install ... command in PATH" to enable IDE integration.
- Connect Claude to your IDE · `/ide`.
- Run `/install-github-app` to tag @claude right from your GitHub issues and PRs.
- Run `/install-slack-app` to use Claude in Slack.
- Run Claude Code locally or remotely using the Claude desktop app: clau.de/desktop.
- Continue your session in Claude Code Desktop with `/desktop`.
- Working on UI? See a live preview in Claude Code Desktop · run `/desktop`.
- Run tasks in the cloud while you keep coding locally · clau.de/web.
- Control this session from the Claude mobile app · run `/remote-control`.
- Get pinged on your phone when long tasks finish · enable push notifications in `/config`.
- Build your AI product with Claude API. Run `/claude-api` to get started.

## Plugin upsells (triggered by repo contents)

- Working with HTML/CSS? Install the frontend-design plugin: `/plugin install frontend-design@...`
- Working with Vercel? `/plugin install vercel@...`
- Working with Stripe? `/plugin install stripe@...`

## Onboarding

- New to Claude Code? Run `/powerup` for a quick interactive tutorial.
- Start with small features or bug fixes, tell Claude to propose a plan, and verify its suggested edits.
- Use Plan Mode to prepare for a complex request before making changes. Press shift+tab twice to enable.
- Use `/config` to change your default permission mode (including Plan Mode).

## Other

- Share Claude Code and earn \[X\] in usage credits · `/passes`.
- Your default model setting is Opus Plan Mode. Press shift+tab twice to activate Plan Mode and plan with Claude Opus.

Each tip has a cooldown (sessions between showings) and a relevance check (terminal type, startup count, whether you've already used the feature). You can disable them with `spinnerTipsEnabled: false` or override the set with `spinnerTipsOverride` in settings.
