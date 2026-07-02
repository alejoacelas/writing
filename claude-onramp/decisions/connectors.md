# Which connectors are worth it?

**Recommendation: connect Google Drive, Gmail, and Calendar right away. Add
others only when a task actually needs them.**

Connectors are how Cowork reaches your apps. Each one you add is an account you
let Claude read and (sometimes) act in. More isn't better — each is a bit of
access you're granting, and unused ones are just surface area. So connect the
few that pay off immediately and leave the rest until you have a reason.

## The ones that pay off immediately

- **Google Drive** — lets Claude read and work from your documents. High value,
  low risk (it's mostly reading).
- **Gmail** — reading and triaging email is one of the most useful things Cowork
  does.
- **Google Calendar** — needed for anything scheduling-related.

## Add when needed

- **Slack, Notion, and similar** — genuinely useful, but connect them when you
  have a task in hand, not preemptively.
- **Anything that can send or post on your behalf** — worth a moment's thought
  before connecting, because those actions are the irreversible kind (see
  [trust and permissions](trust-and-permissions.md)).

## The limit to know about

Cowork's built-in Google connectors mostly **read**. When you want Claude to
*write* — send an email, edit a doc with formatting — you'll hit their ceiling.
That's the moment to move to the [Google Workspace CLI setup in Part 3](../03-power-ups.md),
which gives Claude Code full read-and-write control. Connectors get you started;
the CLI is the upgrade.
