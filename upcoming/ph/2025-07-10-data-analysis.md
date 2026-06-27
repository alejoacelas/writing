# Data analysis: clean your CSVs, and use o3 or Gemini (not Claude)

*Source: https://wow.pjh.is/journal/data-analysis*  ·  *Published: 2025-07-10*

---

_Epistemic status: based on a single test, plus memory of previous results. I do "light" data analysis tasks every month, but not every week._

This week I did a personal finance review. The review required some simple spreadsheet analysis.

I sent the following prompt to o3, o3-pro, Claude 4 Opus (Thinking), Gemini 2.5 Pro, and Grok 3 (Thinking):

Observations:

1. Initially, I uploaded a somewhat messy CSV that contained a bunch of irrelevant information. o3 and Gemini 2.5 Pro made mistakes while trying to identify the correct information.
2. With the cleaned CSV, o3, o3-pro, Gemini 2.5 Pro and Grok 3 (Thinking) did well and their numbers agreed with each other.
3. Claude 4 Opus failed. I sent the same prompt three times: first time it gave up, second time it threw a server error (Anthropic really struggle with capacity), and third time it gave incorrect results.
4. All the models (with possible exception of Grok [1](#user-content-fn-1)) used code, without an explicit prompt to do so.

My takeaways: clean your CSVs; don't use Claude.

## Footnotes

1. The Grok UI did not show that it used code. It might have done under the hood. [↩](#user-content-fnref-1)
