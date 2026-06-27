# Tell your AI to flag ambiguous data, not silently guess what it means

*Source: https://wow.pjh.is/journal/flag-ambiguous-data*  ·  *Published: 2026-06-02*

---

I recently added the following to my `AGENTS.md` file:

Motivation: last week I nearly made a >$10K mistake while working with AI.

I was doing a personal finance review. A high-stakes question came up: whether to sell or hold a large ITM options position. I pasted screenshots of the position details, consulted Claude, then used [ask many models](https://wow.pjh.is/journal/ask-many-models) to get a second opinion from GPT-5.5 Pro, Gemini Pro and Grok. All of them agreed on the bottom line, with high confidence.

But the bottom line surprised me. So I asked Claude to triple-check everything—and specifically to re-examine the position details we'd sent via ask many models. Claude noticed my screenshots didn't include column headings, and that it wasn't entirely sure about the meanings of some of the columns. I pasted in unambiguous screenshots, and Claude confirmed that it had misread the columns. Correcting the numbers flipped the conclusion (for Claude, and all other models).

I could easily have skipped this triple-check and gone ahead with the trade. That would have been a >$10K mistake.

The two heuristics that saved me:

- For high-stakes decisions, triple-check, and be sure to think for yourself.
- If a model output is surprising, be skeptical.

This illustrates a broader failure mode: "model makes a confident, incorrect assumption and doesn't flag it". I [often run into this problem](https://wow.pjh.is/journal/incorrect-assumptions) when trying ambitious delegation of non-coding tasks.
