# How to fix one-day-off date errors

*Source: https://wow.pjh.is/journal/fix-llm-date-errors*  ·  *Published: 2026-02-02*

---

When Claude gets more than a few days' worth of calendar data using [Google Workspace MCP](https://wow.pjh.is/journal/claude-code-google-workspace-mcp), it'll sometimes offset dates by a day. It'll mention a non-existent date like Monday 3rd February (instead of Monday **2nd** February) and then allocate events to the wrong day.

## The fix

Add these instructions to `~/.claude/CLAUDE.md`:

The [Python script](https://gist.github.com/peterhartree/65da7054d4c859ad17f4504974fd22cb) takes output from the Google Calendar MCP server, and outputs a schedule that my "chief of staff" skill can return verbatim:

```
### Monday 03 February 2026
  * 09:00–10:00 Team standup
  * 14:00–15:30 Project review (Room 3)

### Tuesday 04 February 2026
  * [All day] Public holiday
  * 16:00–17:00 1:1 with Sarah

```

Takeaway: if an LLM is unreliable at a deterministic task, delegate it to a deterministic tool.
