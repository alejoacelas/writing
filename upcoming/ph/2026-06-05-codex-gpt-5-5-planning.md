# Codex with GPT-5.5 is still better than Claude Code with Opus 4.8, especially at the planning stage

*Source: https://wow.pjh.is/journal/codex-gpt-5-5-planning*  ·  *Published: 2026-06-05*

---

For non-trivial coding tasks, I always [give my initial prompt](https://wow.pjh.is/journal/claude-code-codex-same-prompt) to Claude Code _and_ Codex, and ask them both to write a plan. I'll then read both plans, and decide which to run with.

Sometimes I'll ask Codex to comment on Claude's plan, or vice versa.

Since early May, I've seen that:

1. GPT 5.5 is faster than Opus 4.7 (often >2x).[1](#user-content-fn-1)
2. Plan quality is often roughly tied, but Codex plans sometimes beat Claude Code by a large margin. Claude Code rarely beats Codex.

I'm seeing the same with Opus 4.8.

To be clear: I always use the default effort settings: in Codex, it's `GPT 5.5 high fast`, and in Claude Code it was `xhigh` for Opus 4.7, and now `high` for 4.8.

An example case:

> TYPE III AUDIO creates audio narrations using the Azure TTS API. When Azure completes the narration, it sends a payload containing the MP3 URL and narration metadata, including the MP3 filesize. I'd noticed a bug: the filesize was not being saved to our database. Both Claude and Codex identified the commit which introduced the bug: a switch to a different Azure region. Claude Code proposed fixing this by adding code which sends a HEAD request to the MP3 file URL, to get the filesize directly from the MP3\. Codex, by contrast, looked at the payload received from Azure in the new region, noticed the format had changed slightly, and suggested the one-line code change.

Claude Code's proposal was so much worse here, and also surprisingly silly—it could see that we'd switched regions, so checking the Azure response format was an obvious step to take. When Codex plans beat Claude Code, it's usually for this kind of reason—one big oversight.

When it comes to _executing_ on big plans, I use Claude Code roughly half the time, even though it's slower. The reason: in May, Claude was better at testing its work with a web browser. Codex is catching up, though. It may have reached parity now—I've not tested enough to know.

## Footnotes

1. It fluctuates, so I guess this is partly due to Anthropic's troubles with server capacity. [↩](#user-content-fnref-1)
