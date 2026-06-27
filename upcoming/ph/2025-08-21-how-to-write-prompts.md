# Ask your LLM to help you write prompts

*Source: https://wow.pjh.is/journal/how-to-write-prompts*  ·  *Published: 2025-08-21*

---

How to quickly write structured prompts for conversational assistants?

Simple—ask your LLM for help:

## Why write a structured prompt?

Conversational assistants like ChatGPT and Claude are already very good at handling short, natural-language prompts. This may be all you need! For example, my ["summarise call transcript" prompt](https://wow.pjh.is/journal/text-expander-prompts) is only one-sentence, but the outputs are great.[1](#user-content-fn-1)

One major benefit of writing a structured prompt is that it _forces you to think_ about what the ideal assistant would do. So, instead of "correct my French", you might ask ["correct my French and help me learn"](https://wow.pjh.is/journal/correct-my-french-teachable-moments). And, when I wanted to [make a call transcript readable](https://wow.pjh.is/journal/prompt-format-call-transcript), I realised that I had specific requirements about e.g. keeping expressions of uncertainty verbatim.

## Prompting best practice

Sometime soon, I will write a more carefully-researched note about "prompting best practice" for conversational assistants. Meantime, here are my takes:

1. Start simple. It's easy to overthink this.
2. Spend 2-10 minutes on your first version. Then use it and iterate as you go.
3. Imagine you're writing instructions for a human. How would you balance high-level goal setting, specificity, and letting the person use their own judgement? Would you explain the _why_ as well as the _what_? What other context would they need?
4. Structure: 1-2 sentence description of what you want => detailed instructions => guardrails (optional) => examples (optional) => output format (optional).
5. Word count: aim for 100-500, usually 100-300.[2](#user-content-fn-2)
6. Examples: do not include example outputs in your first version. It's probably overkill, and may degrade your results.[3](#user-content-fn-3)

As you refine the draft, consider asking the LLM things like:

- How can we improve this prompt further?
- What else might I care about that's not yet mentioned in these instructions?
- Please ask me questions to help you better understand my needs.
- Please write three different prompts and discuss the pros and cons of each.
- How can we make this more robust?

If you want to go deeper:

- How can we help the model make tradeoffs and balance objectives that are tension?
- Should we give the model permission to flag edge cases and uncertainty?
- What guardrails should we add?
- Are we being too specific? Where might it be better to let the model use its own judgement?
- Should we add 1-2 examples, and 1-2 negative examples?
- Is any of this overkill?

The internet has lots of questionable and conflicting advice on prompting. Best practices are changing rapidly, and vary by model. Much of the advice is aimed at people who are writing applications, rather than using conversational assistants. Don't over think it.

## Footnotes

1. In fact, they're better than what I got when I briefly tried to write a more structured prompt. My calls are varied enough that it was not easy to give specific instructions that didn't degrade things in some cases. [↩](#user-content-fnref-1)
2. If you go longer than 500 words, you may be micromanaging. Let the model use its own judgement. If you genuinely need to give more complex instructions, consider breaking them into several prompts. [↩](#user-content-fnref-2)
3. This advice may be controversial, but I consider "giving examples" a fairly advanced technique. Common failure modes: the model anchors too hard on the examples you give; your examples don't properly reflect your instructions. [↩](#user-content-fnref-3)
