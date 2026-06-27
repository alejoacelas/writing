# Project switcher for Claude Code & Codex

*Source: https://wow.pjh.is/journal/claude-code-project-switcher*  ·  *Published: 2026-03-05*

---

To work on a project, one must run `claude` or `codex` in the project directory. That can be a lot of `cd`.

So I've made a helper for that.

I type `cc` (Claude) or `cx` (Codex) in the terminal. This opens a project switcher:

```
  Good morning, Peter!

  Projects & repos:
  ┌───┬──────────────────┬────┬──────────────────────┐
  │ 1 │ Plans and Reviews│ r1 │ wow.pjh.is           │
  ├───┼──────────────────┼────┼──────────────────────┤
  │ 2 │ Infra            │ r2 │ hartreeworks.org     │
  ├───┼──────────────────┼────┼──────────────────────┤
  │ 3 │ AI Wow           │ r3 │ api.type3.audio      │
  ├───┼──────────────────┼────┼──────────────────────┤
  │ 4 │ TYPE III AUDIO   │ r4 │ .agents              │
  ├───┼──────────────────┼────┼──────────────────────┤
  │ 5 │ HartreeWorks     │ r5 │ skills               │
  └───┴──────────────────┴────┴──────────────────────┘

  Recent:
  ┌───┬───────────────────────────────────────┐
  │ a │ _try/2026-03-04-ai-character          │
  ├───┼───────────────────────────────────────┤
  │ b │ _try/2026-01-22-t3a-crunch-accounting │
  └───┴───────────────────────────────────────┘

  Current: /Users/ph/Documents/www/AI Wow/wow.pjh.is ⏎

```

I press a key and the helper changes directory and launches the agent. Or, I pass a memorised key directly (e.g. `cc 3`) to skip the menu.

The project and repo lists are populated from `yaml` files. [1](#user-content-fn-1) The "recents" list contains other directories where I recently ran `claude` or `codex` (e.g. my [tries](https://wow.pjh.is/journal/use-try-for-quick-experiments)).

I also have fast-mode variants that use fast models, invoked with `ccf` and `cxf` on the command line.

## Setup

Add this to your `.zshrc`:

```bash
# Record a directory in the recents list (the launcher filters out
# dirs that shouldn't be remembered).
_agent_record_recent_dir() {
    python3 ~/.agents/scripts/agents/coding_agent_launcher.py --recordable "$1" && echo "$1" >> ~/.cc_recent_dirs
}

cc() {
    local select_arg=""
    case "$1" in
        [1-9]|[a-z]|r[1-9]) select_arg="--select $1"; shift ;;
    esac
    # Expand --r to --resume
    local args=()
    for arg in "$@"; do
        [[ "$arg" == "--r" ]] && args+=(--resume) || args+=("$arg")
    done
    local result
    result=$(python3 ~/.agents/scripts/agents/coding_agent_launcher.py "$PWD" ${=select_arg})
    local exit_code=$?
    if [ $exit_code -eq 0 ] && [ -n "$result" ] && [ -d "$result" ]; then
        _agent_record_recent_dir "$result"
        cd "$result" && claude --model opus "${args[@]}"
    fi
}

cx() {
    local select_arg=""
    case "$1" in
        [1-9]|[a-z]|r[1-9]) select_arg="--select $1"; shift ;;
    esac
    local result
    result=$(python3 ~/.agents/scripts/agents/coding_agent_launcher.py "$PWD" ${=select_arg})
    local exit_code=$?
    if [ $exit_code -eq 0 ] && [ -n "$result" ] && [ -d "$result" ]; then
        _agent_record_recent_dir "$result"
        cd "$result" && codex "$@"
    fi
}

```

And the `coding_agent_launcher.py` script is [here](https://gist.github.com/peterhartree/490b849614848dcc961e522bfa5de98a).

## Footnotes

1. The project list is managed by my [project-management plugin](https://github.com/HartreeWorks/skill--project-management), which maintains a `projects.yaml` file. The repo list comes from a separate `repositories.yaml` file that I created manually. [↩](#user-content-fnref-1)
