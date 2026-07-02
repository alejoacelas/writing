# Connector, MCP, or CLI for Google Workspace?

**Recommendation: start with Cowork's built-in connectors. When you need Claude
to reliably *write* — send mail, edit docs — move to the `gog` and `gdoc`
command-line tools in Claude Code.**

There are three ways to give Claude access to your Google apps, in increasing
order of power and setup.

## Connector — rented hands

The built-in connectors you set up in [Cowork](../01-cowork.md). Anthropic's
servers act on your behalf.

- **Best for:** reading — search mail, pull a doc, check the calendar.
- **Setup:** a click and a Google sign-in.
- **Limit:** mostly read-only; writing is capped or unavailable.

## MCP server — a middle option

A connector you install yourself that exposes more of an app's abilities to
Claude. More capable than the built-in connectors, more setup than a click.
Reasonable if you want write access without committing to CLI tools — but for
Google specifically, the CLIs below are the better-trodden path.

## CLI — your own hands

Command-line tools that run on your machine with full access:

- **`gog`** ([gogcli.sh](https://gogcli.sh)) — broad: Gmail, Calendar, Drive,
  and light Docs/Sheets across all of Workspace.
- **`gdoc`** ([GitHub](https://github.com/LucaDeLeo/gdoc)) — focused: real Google
  Docs editing with proper formatting, comments, and revisions, built to be
  cheap for agents to use.

- **Best for:** actually doing things — sending, editing, automating — and using
  inside skills.
- **Setup:** a one-time Google Cloud project (~10 min; the tedious part, walked
  through in [Part 3](../03-power-ups.md)).
- **Payoff:** everything connectors can't do, scriptable and reusable.

## The path

Connectors to start, because they're free and instant. The day you find yourself
wishing Claude could *send* that email or *format* that doc instead of just
reading it, do the Part 3 CLI setup once and don't look back.
