# Using LLMs to critique your research

*Source: https://wow.pjh.is/journal/research-critique*  ·  *Published: 2025-10-30*

---

_Epistemic status: early notes. Much more to follow in the coming months, I hope._

## The basics

Before reading the below, read: [which model should I ask?](https://wow.pjh.is/journal/which-model).

For critique that requires extensive web search: use "Deep Research" mode, and always ask all three of Gemini, Claude and ChatGPT.

## How to avoid overwhelm

Current models can provide useful critique, but they can also generate a lot of slop.

To make results easier to engage with, tell them to write plainly. For example:

Also, specify the output format. For example:

## Example prompts

### Fact-check my paper

Try the following prompt with GPT-5 Pro and Gemini 2.5 Pro with "Deep Research" enabled:

### Critique my philosophy paper

Here's an okay-ish "critique my paper" prompt:

Some example critiques of notable philosophy papers:

- **[Taking AI Welfare Seriously](https://chatgpt.com/share/6904a489-4618-8008-a78f-c8f16b10d7fe)**, by Rob Long et al.
- **[Against the Social Discount Rate](https://chatgpt.com/share/6904a4ab-d454-8008-9867-5d27d437daae)**, by Tyler Cowen and Derek Parfit
- **[Philosophy as a Humanistic Discipline](https://chatgpt.com/share/6904a463-f630-8008-9efe-fe800914ea6c)**, by Bernard Williams

This particular prompt rarely surfaces novel or surprising critiques. But they're often reasonable, and sometimes helpful, if only to help you communicate better (e.g. by clarifying your writing, or adding something to anticipate an objection that a reader might raise).

[](https://chatgpt.com/share/6904a489-4618-8008-a78f-c8f16b10d7fe)

[](https://chatgpt.com/share/6904a4ab-d454-8008-9867-5d27d437daae)

[](https://chatgpt.com/share/6904a463-f630-8008-9efe-fe800914ea6c)

Example critiques of more technical papers by \[Forethought\](https://forethought.org/):
- **[Persistent Path-Dependence](https://chatgpt.com/share/69049f1b-6aa8-8008-9839-81ffe80b492f)**, by William MacAskill
- **[Will Compute Bottlenecks Prevent a Software Intelligence Explosion?](https://chatgpt.com/share/69049e8a-a5dc-8008-98d7-03178faf43b6)**, by Tom Davidson
- **[How to make the Future Better](https://chatgpt.com/share/6904a27b-cf6c-8008-a343-64b3fea64f30)**, by William MacAskill
- **[The Scaling Paradox](https://chatgpt.com/share/69049f5b-f404-8008-8b48-b002d725fb93)**, by Toby Ord

## Appendix 1\. People are building...

Some public projects I'm following:

- [Roast My Post](https://roastmypost.org/) ([example critique](https://www.roastmypost.org/docs/jfmvvy5KCsE5WetqQA4pK/reader); [Github](https://github.com/quantified-uncertainty/roast-my-post))
- [Refine](https://www.refine.ink/) ([2-min demo](https://www.loom.com/share/2e1b53ec979744bcb916946b1f7775c4))
- [Conceptual reasoning benchmark](https://www.andrew.cmu.edu/user/coesterh/conceptual%5Freasoning%5Fbenchmark.html)
- [ImpactAI](https://impactai.worldbank.org/) (from the World Bank) is trying to automate Givewell-style research.

Many groups are experimenting internally. For example:

- GiveWell has explored red-teaming their research with AI (public write-up coming soon). They're now exploring custom software for fact-checking and literature review.
- I did a brief, exploratory project for [Forethought Research](https://forethought.org/), which included experimentation with [OpenAI Agent Builder](https://wow.pjh.is/journal/openai-agent-builder) and a day of vibe-coding a custom interface for GPT-5 Pro critique (see below).

The current generation of AI models are capable of providing useful critique, but they also generate a _lot_ of slop. Some key challenges:

1. Find the diamonds in the slop, to avoid overwhelming researchers.
2. Prompt engineering to get the best out of the models.
3. Make the affordances easy, with well-designed interfaces.

To do (1) and (2), you need good automated evaluation of LLM outputs. That's the hard part, right now.

## Appendix 2\. A custom interface for brainstorming critiques

Here's a prototype I made for [Forethought Research](https://forethought.org/):
