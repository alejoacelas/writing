# Spreadsheet data enrichment: Google Sheets vs Shortcut vs Airtable

*Source: https://wow.pjh.is/journal/spreadsheet-data-enrichment*  ·  *Published: 2025-08-07*

---

I have a list of names and email addresses. I want to enrich this data with job titles, organisation names, and job descriptions.

I tried [Google Sheets](https://sheet.new), [Shortcut](https://tryshortcut.ai), and [Airtable](https://airtable.com). Airtable was the best.

## Google Sheets can't do it

The Gemini sidebar and the `AI` function can't do web searches.

So, Google Sheets can't help me. [1](#user-content-fn-1)

## Shortcut was ok

I asked the chat:

It worked! It took about 3 minutes to run through 33 names and add the info.

Problems:

- Shortcut can only import .xlsx files, not .csv. So I copy-pasted the data from Google Sheets.
- Shortcut imitates the UI of Microsoft Excel. For a Google Sheets user, it's not immediately intuitive.
- Shortcut is an early beta, not a mature product. I saw rough edges, and bugs.

## Airtable was great

I gave Airtable chat the same prompt as Shortcut.

Initially, the agent tried searching the web itself for each contact, right within the chat. It made it through about five contacts and then crashed.

Then I asked:

It took about 30 seconds to create the [Airtable AI fields](https://www.airtable.com/guides/scale/how-to-use-airtable-ai), then another minute or so to run them. This got me all the data that I wanted.

## Data accuracy

**In 4/33 cases, Airtable hallucinated the job description.** The hallucinated text was the same in all four cases, and taken from the correct org's website. **The field prompt that Airtable generated had the obvious major problem of not telling the AI it can return "not found", or flag uncertainty:**

I fixed it by editing the prompt.

In some cases, people had one job title on LinkedIn and one job title on their organisation website. Shortcut and Airtable made different decisions about which one to prioritize. Ideally, the field prompts would have anticipated this edge case and told the AI to flag uncertainties like this.

So: next time, when I ask the Airtable assistant to write a retrieval prompt, I would explicitly say that the prompt should: (a) say "not found" if it can't find it and (b) add a "comments" column to flag uncertainty or other issues.

Aside from that, both Shortcut and Airtable gave mostly accurate data. They correctly marked a few contacts as "couldn't find the info".

## Bottom line

I'll use Airtable for data enrichment going forward. It's very good, and very easy.

To improve accuracy: before running the prompts it generates, I'll copy-paste them into ChatGPT and ask it to check for issues. Then carefully read the final prompt myself.

## Appendix 1\. Example use cases for Airtable AI

## Footnotes

1. Note that you _can_ import data from a specific URL using the `IMPORTHTML` or `IMPORTXML` functions. [↩](#user-content-fnref-1)
