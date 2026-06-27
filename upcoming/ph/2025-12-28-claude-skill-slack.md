# Skill: Read and post Slack messages

*Source: https://wow.pjh.is/journal/claude-skill-slack*  ·  *Published: 2025-12-28*

---

I've made a [Slack Skill for Claude Code](https://github.com/HartreeWorks/claude-skill--slack), so now I can ask:

> Hey Claude, what happened on Slack this week?

Of course, you can post messages too.

Here's a weekly Slack digest of new feedback that a client received on their podcast episodes. The data is drawn from a Google Sheet, using the [Workspace MCP](https://wow.pjh.is/journal/claude-code-google-workspace-mcp).

## Limits & warnings

The setup process for this skill is [a little tricky](https://github.com/HartreeWorks/claude-skill--slack/blob/main/SKILL.md)—if you've not used Claude Code before, it's probably not the place to start. Your IT security team may or may not be happy about you doing this, so check with them first.[1](#user-content-fn-1)

This skill only works with Claude Code. To access Slack from the Claude web app, you'll have to wait for the official [MCP server](https://docs.slack.dev/ai/mcp-server/) to be released, then talk to your workspace administrator. Meantime, you can [talk to Claude from inside Slack](https://claude.com/claude-in-slack), if your workspace administrator has enabled it.

## Footnotes

1. I feel conflicted about whether to recommend this to people. It's fine if you know what you're doing, questionable if you don't. I'll write a blog post about this soon. [↩](#user-content-fnref-1)
