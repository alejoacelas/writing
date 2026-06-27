# Create Claude Skills for recurring tasks

*Source: https://wow.pjh.is/journal/claude-skills*  ·  *Published: 2025-10-31*

---

Want to teach Claude to do recurring tasks according to your instructions? It's now best to use [Claude Skills](https://support.claude.com/en/articles/12512176-what-are-skills)—not projects.

From the [Claude docs](https://support.claude.com/en/articles/12512176-what-are-skills):

> Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.
> 
> \[...\]
> 
> When you ask Claude to complete a task, it reviews available Skills, loads relevant ones, and applies their instructions.

See [appendix 1](#appendix-1-a-technical-sketch) for a more technical explanation.

## What can I do with Skills?

Some examples:

- [Create invoices, send them, and verify payment](https://wow.pjh.is/journal/claude-skill-send-my-invoices).
- [Review, edit and publish a blog post](https://wow.pjh.is/journal/publish-blog-post-claude-skill).
- [Make an OKR progress report](https://wow.pjh.is/journal/okr-progress-report-claude-skill).
- [Use a web browser to review messages on a government portal](https://wow.pjh.is/journal/claude-skill-computer-use-urssaf).
- [Make an AI Chief of Staff](https://wow.pjh.is/journal/ai-chief-of-staff).

Some things that Skills can do:

- Use all the standard tools and connectors (e.g. create Asana tasks, draft emails, get calendar events, search the web).
- Run scripts (in the consumer web app: Python, Node.js, C++, Perl & Bash).
- Modify files on your computer (using [Claude Code](https://www.claude.com/product/claude-code)).
- Invoke other skills.

## How to make a Skill

Start a new chat, and say something like:

You'll end up with a skill file like this:

## What's the difference between Skills, Projects and Custom Instructions?

> ### Skills vs. Projects
> 
> Projects provide static background knowledge that's always loaded when you start chats within them. Skills provide specialized procedures that activate dynamically when needed and work everywhere across Claude.
> 
> ### Skills vs. Custom Instructions
> 
> Custom instructions apply broadly to all your conversations. Skills are task-specific and only load when relevant, making them better for specialized workflows.

## Further reading

- [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [How to create a skill with Claude through conversation](https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation)
- [Agent skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

## Appendix 1\. A technical sketch

From [Anthropic Engineering](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills):

> Skills use "progressive disclosure" - Claude only loads skill information as needed rather than putting everything in context upfront. Like a well-organized manual that starts with a table of contents, then specific chapters, and finally a detailed appendix, skills let Claude load information only as needed. This means that the amount of context that can be bundled into a skill is effectively unbounded.

You can bundle context files into a skill:

And you can also bundle code, when you want deterministic logic, API calls, config files, or whatever else:
