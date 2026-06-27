# How to connect Notion to Claude

*Source: https://wow.pjh.is/journal/how-to-connect-notion-to-claude*  ·  *Published: 2025-12-03*

---

Claude can search for information from Notion, create or edit pages, add or retrieve comments, and [much else](https://developers.notion.com/docs/mcp-supported-tools).

To enable that: open your [Claude Connector settings](https://claude.ai/settings/connectors), then click "Browse connectors > Notion > Connect".

The connector works well, but it's often slow, because it has to do a bunch of searching to find the relevant documents every time. Just like with [Asana](https://wow.pjh.is/journal/create-asana-tasks-claude), you can speed things up (a lot) by adding information about how to navigate your Notion (e.g. links to key pages; the names of databases you often use) to your [system instructions](https://claude.ai/settings/general) (currently called "personal preferences" in the web app).

If you run into a slow query, just say something like:

You should end up with something like this:
