# Skill: Make an OKR progress report

*Source: https://wow.pjh.is/journal/okr-progress-report-claude-skill*  ·  *Published: 2025-12-03*

---

I have a client who wants their staff to share weekly OKR progress reports in a spreadsheet.

We want to make this easy.

## The vision

Staff should ask Claude for a summary of their progress, and Claude should:

1. Know about their OKRs.
2. Pull in relevant info from their Google Drive, [Notion](https://wow.pjh.is/journal/how-to-connect-notion-to-claude), Gmail, Google Calendar, [call transcripts](https://wow.pjh.is/journal/give-claude-call-transcripts), and other sources
3. Draft the progress report.

Something like this:

But: each staff member has different OKRs, workflows, and data sources they need to check. So rather than making a single generic skill for all staff, we need to make a meta-skill: _a skill that helps them create a skill_ that is personalised for them.

That meta-skill should walk them through the process. Something like this:

## How I did this

In short:

1. Make an OKR digest skill for myself.
2. Generalise it into a meta skill ([view result](https://github.com/HartreeWorks/claude-skill--create-okr-digest-metaskill/blob/main/SKILL.md)).

This screencast goes into more detail:

Some things I learnt since making the screencast:

- You can easily [pull in data from Notion](https://wow.pjh.is/journal/how-to-connect-notion-to-claude).
- Same goes for [Fireflies](https://wow.pjh.is/journal/give-claude-call-transcripts#fireflies), [Granola](https://wow.pjh.is/journal/give-claude-call-transcripts#granola), and [many other sources](https://www.claude.com/connectors).
- You can use Zapier to escape the Claude.ai security sandbox and [pull in data from any public URL](https://wow.pjh.is/journal/claude-ai-access-any-url).[1](#user-content-fn-1)

## Footnotes

1. Alternatively, just use [Claude Code](https://www.claude.com/product/claude-code) instead of the web app. [↩](#user-content-fnref-1)
