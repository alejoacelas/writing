# How to let agents read your WhatsApp

*Source: https://wow.pjh.is/journal/let-claude-read-my-whatsapp*  ·  *Published: 2026-06-15*

---

I have a small Go bridge ([whatsapp-mcp](https://github.com/lharries/whatsapp-mcp), built on `whatsmeow`), which runs on my Mac Mini.

It's linked to my account as a "WhatsApp Web" device via QR code. The bridge writes every message I send and receive into a local SQLite database.

I've blocked the "send" function.
