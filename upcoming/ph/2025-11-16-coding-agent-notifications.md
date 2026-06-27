# Get notified when Codex and Claude Code finish work

*Source: https://wow.pjh.is/journal/coding-agent-notifications*  ·  *Published: 2025-11-16*

---

Oddly, neither Codex nor Claude Code have good built-in notifications settings.

I'd like a notification every time the agent finishes work:

And here's how to get it...

## Requirements

Install [Terminal Notifier](https://github.com/julienXX/terminal-notifier):

```bash
brew install terminal-notifier

```

## Codex CLI

Add the following to your `~/.codex/config.toml` file:

```toml
notify = ["python3", "/Users/ph/.codex/scripts/notify.py"]

```

Then create `~/.codex/scripts/notify.py` with the following contents:

```python
#!/usr/bin/env python3
"""
Codex notify hook: show macOS notification via terminal-notifier.
Receives a single JSON string argument as described in docs/config.md#notify.
"""

from __future__ import annotations

import json
import subprocess
import sys
import os
from typing import Any, Dict, List

def main(argv: List[str]) -> int:
    if len(argv) != 2:
        return 1

    try:
        payload: Dict[str, Any] = json.loads(argv[1])
    except json.JSONDecodeError:
        return 1

    if payload.get("type") != "agent-turn-complete":
        return 0

    group = payload.get("cwd") or "codex"
    dir_name = os.path.basename(group.rstrip("/")) if group else ""
    title = "Codex" + (f" ({dir_name})" if dir_name else "")
    input_messages = payload.get("input-messages", [])
    subtitle = "You: " + input_messages[-1] if input_messages else ""
    message = "Codex: " + (payload.get("last-assistant-message") or "Turn complete.")

    # Fire and forget; avoid raising if terminal-notifier is missing.
    try:
        subprocess.run(
            [
                "terminal-notifier",
                "-group",
                group,
                "-title",
                title,
                "-subtitle",
                subtitle,
                "-message",
                message,
                "-sound",
                "Glass"
            ],
            check=False,
        )
    except FileNotFoundError:
        return 1

    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

```

## Claude Code

Add this to your `~/.claude/settings.json` file:

```
"hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/scripts/notify.py Notification"
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/scripts/notify.py Stop"
          }
        ]
      }
    ]
  }

```

Then create `~/.claude/scripts/notify.py` with the following contents:

```python
#!/usr/bin/env python3
import json
import os
import sys
import subprocess
from typing import Any, List, Dict

def expand_path(path: str) -> str:
    """Expand leading ~ in paths if present."""
    if not path:
        return ""
    if path.startswith("~"):
        return os.path.expanduser(path)
    return path

def flatten_content(content: Any) -> str:
    """
    Flatten Claude-style message content into a string.

    * If it's a string, return as-is.
    * If it's a list, join:
      * objects: .text or .content
      * strings: as-is
    * Otherwise, return empty string.
    """
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts: List[str] = []
        for item in content:
            if isinstance(item, dict):
                v = item.get("text") or item.get("content") or ""
                if isinstance(v, str):
                    parts.append(v)
            elif isinstance(item, str):
                parts.append(item)
        return " ".join(parts)

    return ""

def load_transcript(path: str) -> List[Dict[str, Any]]:
    """
    Load the transcript file.

    Tries:
    * JSON array
    * JSON Lines (one JSON object per line)
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
    except OSError:
        return []

    # Try as a single JSON value
    try:
        data = json.loads(raw)
        if isinstance(data, list):
            return data
        # If it's a single object, wrap in a list
        if isinstance(data, dict):
            return [data]
    except json.JSONDecodeError:
        pass

    # Fallback: JSON Lines
    messages: List[Dict[str, Any]] = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            messages.append(obj)
    return messages

def get_last_turn_text(messages: List[Dict[str, Any]]) -> str:
    """
    Last conversation turn (user or assistant), following the jq logic.
    """
    filtered: List[Any] = []
    for m in messages:
        if m.get("type") in ("user", "assistant"):
            filtered.append(m.get("message", ""))

    if not filtered:
        return ""

    msg = filtered[-1]
    if not isinstance(msg, dict):
        return ""

    role = msg.get("role")
    if role == "user":
        content = msg.get("content") or ""
    else:
        # assistant: content defaults to [] in the jq script
        content = msg.get("content") or []

    return flatten_content(content)

def get_last_user_text(messages: List[Dict[str, Any]]) -> str:
    """
    Last *user* message, following the jq logic.
    """
    filtered: List[Any] = []
    for m in messages:
        if m.get("type") == "user":
            filtered.append(m.get("message", ""))

    if not filtered:
        return ""

    msg = filtered[-1]
    if not isinstance(msg, dict):
        return ""

    content = msg.get("content") or ""
    return flatten_content(content)

def main() -> None:
    # First argument = hook event type ("Notification", "Stop", etc.)
    event_type = sys.argv[1] if len(sys.argv) > 1 else "Notification"

    # Read hook JSON input from stdin
    try:
        input_json_str = sys.stdin.read()
        hook = json.loads(input_json_str) if input_json_str.strip() else {}
    except json.JSONDecodeError:
        hook = {}

    # Extract cwd, transcript_path, and notification_type from hook input
    cwd = hook.get("cwd", "") or ""
    transcript_path_raw = hook.get("transcript_path", "") or ""
    notification_type = hook.get("notification_type", "") or ""

    # Do nothing if notification type is "idle_prompt"
    #
    # This fires 60 seconds after the previous notification—it's annoying
    # to get a "follow-up" notification
    if notification_type == "idle_prompt":
        sys.exit(0)

    transcript_path = expand_path(transcript_path_raw)

    # Direct parent directory name from cwd
    if cwd:
        dir_name = os.path.basename(cwd)
        if not dir_name:
            dir_name = "(no-cwd)"
    else:
        dir_name = "(no-cwd)"

    preview = "(no transcript entries yet)"
    subtitle = "(no recent user message)"

    if transcript_path and os.path.isfile(transcript_path):
        messages = load_transcript(transcript_path)

        last_turn_text = get_last_turn_text(messages)
        last_user_text = get_last_user_text(messages)

        if last_turn_text:
            preview = "Code: " + last_turn_text

        if last_user_text:
            user_snippet = last_user_text
            subtitle = f"You: {user_snippet}"
        else:
            subtitle = "(no recent user message)"

    title = f"Claude ({dir_name})"

    # Call terminal-notifier
    subprocess.run(
        [
            "terminal-notifier",
            "-title",
            title,
            "-subtitle",
            subtitle,
            "-message",
            preview,
            "-sound",
            "Glass",
        ],
        check=False,
    )

if __name__ == "__main__":
    main()

```

Thanks to [JP Addison](https://www.jpaddison.net/) for the inspiration.
