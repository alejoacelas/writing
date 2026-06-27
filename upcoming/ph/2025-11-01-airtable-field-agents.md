# Use Airtable field agents to prompt LLMs in bulk

*Source: https://wow.pjh.is/journal/airtable-field-agents*  ·  *Published: 2025-11-01*

---

Airtable field agents let you quickly send lots of prompts to LLMs, and get the results back in a spreadsheet.

Field agents can do most things you can do via the consumer web app, including:

- Answer questions
- Summarise texts
- Search the web (e.g. read someone's online profiles and write a bio)
- Extract data from PDFs (e.g. get employment history from a CV)
- Classify text or images

Airtable are [weirdly bad](https://support.airtable.com/v1/docs/using-airtable-ai-in-fields) at quickly illustrating the feature. So here's a 1-minute demo:

You can select models from OpenAI, Anthropic and Google.

By default, field agents use GPT 4.1, which runs fast, but sometimes fails at basic tasks. Bulk queries to the smartest models can take minutes or hours, and quickly run down your [credits](https://support.airtable.com/docs/airtable-ai-billing)—so try Claude Haiku or Gemini Flash before dialling up further. GPT-5 Pro is not an option, sadly.

**It may take longer than you think to get things working reliably.** If your prompt fails 1/20 times, and you have 1000 rows... you'll want to [systematically iterate on your prompts](https://wow.pjh.is/journal/prompt-evaluation-with-airtable).

You may want to combine this with [Airtable Automations](https://support.airtable.com/docs/getting-started-with-airtable-automations), which is basically a subset of [Zapier](https://zapier.com/), built-into Airtable.

## Appendix 1\. Airtable is easier to learn these days

If you mainly use Google Sheets, learning Airtable can be a headache. Happily, their Omni sidebar assistant [makes it much easier to get started](https://wow.pjh.is/journal/airtable-spreadsheet-assistant).

## Appendix 2\. Google Sheets also has AI fields

[Google Sheets also has AI fields](https://support.google.com/docs/answer/15877199). But—at the time of writing—they're very limited compared to Airtable. They're worth a try, but it's nearly always worth using Airtable, even if you normally work in Sheets.
