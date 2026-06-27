# How to evaluate AI prompts and models

*Source: https://wow.pjh.is/journal/prompt-evaluation-with-airtable*  ·  *Published: 2025-11-01*

---

I'll write a post on this soon. Meantime:

Shreya uses Google Sheets to run her evals, but [Airtable field agents](https://wow.pjh.is/journal/airtable-field-agents) are a better "no-code" option.

If you're a developer, try [PromptFoo](https://www.promptfoo.dev/docs/getting-started/).

Ideally, your evaluations are based on deterministic code (e.g. "pass" if response contains a string, "fail" otherwise). But you'll often have to use an LLM to judge your outputs. They share an example at [48:50](https://www.youtube.com/watch?time%5Fcontinue=2930&v=BsWxPI9UM4c).
