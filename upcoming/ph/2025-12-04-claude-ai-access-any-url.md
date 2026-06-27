# How to let Claude.ai read any URL

*Source: https://wow.pjh.is/journal/claude-ai-access-any-url*  ·  *Published: 2025-12-04*

---

Claude Code can, with your permission, read any web page.

The Claude.ai web app, by contrast, has a security sandbox that strictly limits the domains it can access.

To work around this, use the [Claude Zapier Connector](https://www.claude.com/connectors/zapier) with the [URL to Text](https://urltotext.com/) service:

I won't explain the steps in detail here. If you can't easily figure this out for yourself, then you shouldn't enable this workaround.[1](#user-content-fn-1)

The one tip I _will_ give: for the sake of speed, specify default settings in your [system instructions](https://claude.ai/settings/general). Something like this:

## Footnotes

1. The default URL restrictions are there to protect you from [prompt injection](https://en.wikipedia.org/wiki/Prompt%5Finjection). You should never let Claude crawl URLs that you do not trust. [↩](#user-content-fnref-1)
