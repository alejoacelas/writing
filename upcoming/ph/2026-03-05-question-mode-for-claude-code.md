# Question mode for Claude Code

*Source: https://wow.pjh.is/journal/question-mode-for-claude-code*  ·  *Published: 2026-03-05*

---

Claude is sometimes too proactive. You ask a question, and instead of just answering, it starts editing files.

The fix: add a "question mode" instruction to your `CLAUDE.md`:

## Usage

If you know you want question mode before you start writing:

> ? why does this return null sometimes

If you realise afterwards:

> why does this return null sometimes
> 
> ?

Or if you're using voice input:

> question: why does this return null sometimes?

> I'm thinking of splitting this into two services, thoughts?
