# Claude Cowork is a very restricted version of Claude Code

*Source: https://wow.pjh.is/journal/claude-cowork-is-not-claude-code*  ·  *Published: 2026-02-03*

---

Claude Cowork is not simply "Claude Code with a nice UI". It's a sandboxed version of Claude Code with major restrictions, that aim to prevent non-technical users from getting into trouble. Many "power-user" workflows cannot be implemented in Cowork.

Below are some of the limitations I've found so far.

## Network access

WebFetch can get text from a URL, but not HTML.

It can make `GET` requests only—no `POST`, no custom headers.

This means you can only interact with services that have an [official connector](https://www.claude.com/connectors), or an MCP you can setup manually. You can't run skills that call external APIs, e.g. my [invoicing skill](https://wow.pjh.is/journal/claude-skill-send-my-invoices) that queries my time tracking software and creates invoices in Xero, or my [ask many models](https://wow.pjh.is/journal/ask-many-models#how-to-quickly-ask-many-models) skill that queries models from Google, OpenAI, Grok and Anthropic all at once.

## No OAuth or CLI auth flows

CLI tools that require browser-based authentication won't work in the sandboxed VM. This includes:

- `gh auth login` (GitHub CLI)
- `gcloud auth login` (Google Cloud)
- `aws sso login`
- `npx vercel login`

If your skill depends on authenticated CLI tools, it won't run in Cowork.

## Limited package managers and tools

| Tool               | Available        |
| ------------------ | ---------------- |
| npm                | Yes (v10.9.4)    |
| pnpm               | No               |
| yarn               | No               |
| jq                 | Yes (v1.6)       |
| macOS open command | No (VM is Linux) |

## Browser automation has heavy guardrails

Claude in Chrome exists in Cowork, but with significant restrictions. Many actions require explicit per-action confirmation in chat—even if you've already described your intent.

| Action                           | Cowork behaviour                   |
| -------------------------------- | ---------------------------------- |
| Enter passwords                  | Prohibited—you must do it yourself |
| Enter credit card / bank details | Prohibited                         |
| Create accounts                  | Prohibited                         |
| Modify sharing permissions       | Prohibited                         |
| Accept terms & conditions        | Requires confirmation              |
| Send emails / messages           | Requires confirmation              |
| Download files                   | Requires confirmation              |
| Click "submit" / "publish"       | Requires confirmation              |

This makes Cowork unsuitable for fully autonomous browser workflows. Every "irreversible" action becomes a back-and-forth.
