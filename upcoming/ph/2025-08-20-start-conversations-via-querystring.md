# You can link to pre-populated chats

*Source: https://wow.pjh.is/journal/start-conversations-via-querystring*  ·  *Published: 2025-08-20*

---

How can I give someone a link to a chat, where the first turn is pre-populated?

## ChatGPT: Use the "share" function

Start a chat, submit the first message, then use the "Share" button to get a link.

People who view the link can then continue the conversation in their own account ([example](https://chatgpt.com/share/68a5f7f7-5564-8008-9eab-46c8b234be14)).

You can append a `model` query parameter to specify the model you want to use:

- <https://chatgpt.com/share/68a5f7f7-5564-8008-9eab-46c8b234be14?model=gpt-5-thinking>

## ChatGPT & Claude: use the querystring

To link to a "new chat" with the first turn pre-populated, you can do:

- <https://chatgpt.com?q=Hey+ChatGPT>
- <https://claude.ai/new?q=Hey+Claude>

You can pass about 750 words into ChatGPT, or 1500 words into Claude.[1](#user-content-fn-1)

You can specify the model:

- <https://chatgpt.com/?q=Hey+ChatGPT&model=gpt-5-thinking>
- <https://claude.ai/new?model=claude-sonnet-4-5-20250929>

**Issues with the querystring approach:**

- These features are undocumented. They have been available since early/mid 2024\. But, they might break unexpectedly.
- If the user is not already logged in, they'll be prompted to login then redirected to a new chat without the pre-populated text.
- You'll want to [URL encode](https://www.urlencoder.org/) the text.

## Footnotes

1. Up to 6,000 characters for ChatGPT. 10,000 characters for Claude. [↩](#user-content-fnref-1)
