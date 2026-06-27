# Create Asana tasks in Claude

*Source: https://wow.pjh.is/journal/create-asana-tasks-claude*  ·  *Published: 2025-07-24*

---

Enable the [Claude Asana connector](https://support.anthropic.com/en/articles/10168395-setting-up-claude-integrations) to create tasks in Claude.

With that—plus some extra setup I'll describe below—you can say things like:

> Create tasks: water plants 9am tomorrow, buy milk 10am Friday.

Or paste a screenshot and say:

> Create tasks for each item in the screenshot. All should be due 10am Friday, except the last one, which should be 5pm today.

Or be more specific:

> Create task for Claire, in the home workspace: water plants 9am tomorrow.

This works on both desktop and the mobile app. Use voice input!

To make this fast, update your Claude preferences ("Settings > Profile") to:

1. Set default task settings.
2. Provide workspace, project and user IDs (so Claude doesn't have to look them up each time).

Your preferences should look something like this:

```
# Asana tasks

**Default task settings:**
When creating tasks, use these defaults unless I specify otherwise:

- Workspace ID: 313980294991451
- Assignee: me

**Due date handling:**
- Time only (e.g., "create task at 9am"):
  - Current time is 8:30am → Due date: Today at 9:00am
  - Current time is 2:00pm → Due date: Tomorrow at 9:00am
- No time/date specified: Leave blank (no due date)

**Asana reference data:**
{
  "workspace": {
    "gid": "313980294991451",
    "name": "Work"
  },
  "users": [
    {
      "gid": "313980286430634",
      "name": "Peter Hartree"
    },
    {
      "gid": "1210877503922028",
      "name": "Paul Bacon"
    }
  ],
  "projects": [
    {
      "gid": "313980295761318",
      "name": "AI Wow"
    },
    {
      "gid": "313980295761321",
      "name": "TYPE III AUDIO"
    },
    {
      "gid": "313982453556107",
      "name": "80,000 Hours"
    }
  ]
}

```

To get the "Asana reference data", just ask Claude:

> Please get all of the workspace IDs, user IDs and project IDs in my Asana, and return them as a JSON object.

If your workspace has 20+ people, just include the people you'll assign to most often.

I've tested this workflow, but I've not used it heavily, since I don't use Asana. If you try it, please [let me know](mailto:wow@pjh.is) how you get on.

Personally, I use Todoist instead of Asana, because [adding tasks in Todoist is so much easier](https://www.todoist.com/help/articles/use-task-quick-add-in-todoist-va4Lhpzz). The key thing is that Todoist lets you set dates using natural language—and set priorities, assignees etc—all from a single text input.

## Appendix 1\. How to avoid duplicate tasks?

Let's say you want to add meeting events to Asana, but some of them might already be in there.

I'd try adding something like this to the prompt above:

I've not _actually_ tried this. If you do, please let me know how you get on.
