# FluidVoice dictation runs locally, but I don’t recommend it (unless you’re desperate for the privacy guarantee)

*Source: https://wow.pjh.is/journal/fluidvoice-dictation*  ·  *Published: 2025-10-16*

---

[FluidVoice](https://altic.dev/fluid) is an alternative to [Wispr Flow](https://wisprflow.ai/) that transcribes dictations locally on your Mac.

The best features:

1. It is faster than Wispr Flow, and works offline. Accuracy is similar.
2. You don't have to trust a third-party to process your dictations.
3. It's free.

But there's a major problem: **it can't tidy up your dictations unless you enable cloud-based processing**. 🤦

That means:

- It leaves in the ums and ahs.
- It doesn't fix your self-corrections.
- It doesn't add paragraphs, bullet points or numbered lists.
- No custom dictionary to fix transcription errors (e.g. it always transcribes "80K" as "ADK", and I can't fix that).

Here's the kind of thing you'll get:

> Um I think I'm gonna go to the cafe this morning. Oh wait, sorry, the uh bookshop this morning. Then I'm gonna go to the market. Shopping list is uh number one, eggs, number two, tomatoes, and number three, flour. And then I'll start work on the narration project for ADK.

The option to tidy dictations locally is "under development".

Smaller issues:

1. In my test, the onboarding experience had two major bugs. It took me a couple of minutes to get past them—I nearly gave up.
2. For the cloud-based post-processing, you have to bring your own API key. Headache for non-technical users.

Overall: this is one to watch, but I do not recommend it unless your work is so sensitive that you cannot trust a third-party API.[1](#user-content-fn-1)

When someone finally makes a great local-only dictation tool, I'll definitely feature it in the newsletter!

## Footnotes

1. [GitHub](https://github.com/altic-dev/Fluid-oss) suggests that the pace of development is fairly slow. But I'll check back in a month or two. [↩](#user-content-fnref-1)
