# Brainstorming with AI: early experiments

*Source: https://wow.pjh.is/journal/brainstorming*  ·  *Published: 2025-11-07*

---

_Epistemic status: Rough notes. I've spent some hours experimenting with this, but I feel I've barely begun._

Below are some ways to brainstorm with AI...

## The minimalist method

1. Open your default model.
2. Say something like: “I’m thinking about X, because Y. Please brainstorm on Z.”
3. (optional) Add context e.g. relevant Google Docs.
4. (recommended) Send the same prompt to several other models.

## Structured prompting with an interview step

Let's say you want to do a MECE brainstorm. You might try a prompt like this:

You'll probably want to do the interview step with a ["standard" model](https://wow.pjh.is/journal/which-model), and then run the actual brainstorm with a "heavy" model.

## Meta-prompting

The flow is:

1. **Brainstorm useful brainstorming techniques.** Tell the AI what you're thinking about, and ask it to brainstorm the kinds of brainstorming techniques that might be most useful.
2. **Write a meta prompt.** Ask the AI to write a meta-prompt that'll generate brainstorming prompts for the kinds of brainstorms you want to run (see [Appendix 1 for an example](#appendix-1-example-meta-prompt)).
3. **Run the brainstorm prompt.** Try several models.

## Vibe-code your brainstorm review interface

You could ask Claude to present brainstorm results [in a custom UI](https://claude.ai/public/artifacts/efa29c0f-1e81-424a-885d-b03649f65010) ([chat thread](https://claude.ai/share/0e7b3641-5652-4933-98dc-13c1f8bdc800)).

I've not figured out anything good yet, but maybe you can! [1](#user-content-fn-1)

## Multi-stage prompting with OpenAI Agent Builder

Perhaps you'd like to start several separate GPT-5 Pro brainstorms with a single prompt? Try prompt-chaining with [OpenAI Agent Builder](https://wow.pjh.is/journal/openai-agent-builder).

## There is _so much_ to figure out here

Some challenges:

- The consumer chat app interfaces are very bad for ambitious brainstorming. We need custom interfaces and model orchestration.
- There are many different use cases for brainstorming.
- Evaluating and iterating on prompts and models is difficult, because the outputs are long and difficult to grade.
- You need to filter for the good stuff, and present it in a way that's easy to engage.

Please [share your ideas and experiences](mailto:wow@pjh.is).

## Appendix 1\. Example meta prompt

The research topic I chose:

Example outputs (Claude Opus 4.1):

- [Baseline](https://claude.ai/share/027ca8fc-bfe1-4b92-b3e7-073cd76d8afa)
- [Expert panel](https://claude.ai/share/16ebbf8a-0042-4199-a185-524530dd976a)
- [Force novel ideas](https://claude.ai/share/714dd977-31be-4795-a64a-5479ab850a21)
- [Analogical reasoning (pharmaceutical industry)](https://claude.ai/share/cb983de4-93c1-4d16-a2ea-ea8d06ef7f30)

## Appendix 2\. A custom interface for brainstorming critiques

Here's a prototype I made for [Forethought Research](https://forethought.org/) recently:

## Footnotes

1. You could also build an interface for _running_ prompts (c.f. [prototyping with Claude artifacts](https://wow.pjh.is/journal/claude-artifacts-prototyping)). It's reasonable to _prototype_ a prompting UI like this, but note that if you actually run brainstorm prompts via Claude artifacts, you can't use the strongest AI models. So you'd want to take the prototype and build a proper app with Replit, Cursor, Codex, or whatever. [↩](#user-content-fnref-1)
