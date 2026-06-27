# How to plan agent coding projects

*Source: https://wow.pjh.is/journal/how-to-plan-agent-coding-projects*  ·  *Published: 2026-03-12*

---

Making something? Planning is the most important part. With a good plan, you're much less likely to waste time building the wrong thing, the wrong way.

Quick tips on planning:

1. Mindset: you're part of a team. Your agent is a product designer, and an engineer. Work together to make a great plan.
2. Start by telling the agent about your **problem**—not the thing you think you want to build.
3. Ask yourself, and your agent: what are the stakes here? Is it worth spending minutes, hours or days to solve this? Do a BOTEC.
4. Ask the agent to brainstorm ways to solve the problem. Try requesting that brainstorm before you share your own thoughts on what to build.
5. If the agent is too eager to switch from thought partnership to building, [use question mode](https://wow.pjh.is/journal/question-mode-for-claude-code).
6. Consider wireframing user interfaces before you build a working app. When you see a wireframe, you'll have insights about what you need. It's much faster to iterate on wireframes than a fully working prototype.
7. After open discussion, switch to plan mode (`Shift + Tab`).
8. Review the agent's plan carefully. Ask it to explain things you don't understand, or that strike you as questionable.
9. Make big plans, so the agent can run independently for longer. Ask it to build the whole thing; assign 10 tickets at a time.
10. Your plan should usually include "comprehensively test using Chrome" and "do code review". [Make sure the agent can use Chrome](https://wow.pjh.is/journal/enable-claude-to-test-its-work-in-chrome). To test a browser extension, use [this skill](https://github.com/HartreeWorks/skill--chrome-extension-dev).
11. For web apps, use an agent-friendly framework like [Next.js](https://nextjs.org/) or [Convex](https://www.convex.dev/). Deploy to Vercel or Railway.
12. For planning, Codex 5.4 is as good or better than Opus 4.6\. YMMV.
13. For big projects, consider writing a full PRD. If you're doing this often, try [ChatPRD](https://chatprd.com/).
14. When planning, consider using fast mode (`/fast on`). You'll save a bunch of time, and the cost may make you think harder.[1](#user-content-fn-1)
15. For difficult projects, [ask several models](https://github.com/HartreeWorks/skill--ask-many-models).

## Footnotes

1. With Claude Code, you'll typically spend $5–25 per plan. On Codex, fast mode uses your ChatGPT Pro plan quota at 2x. [↩](#user-content-fnref-1)
