# ChatGPT: how does memory work?

*Source: https://wow.pjh.is/journal/chatgpt-memory*  ·  *Published: 2025-08-15*

---

**In short:** ChatGPT now gets to know you, a bit like a human would. I've kept this enabled.

## What is ChatGPT memory?

ChatGPT memory has two separate features. Quoting from their [FAQ](https://help.openai.com/en/articles/8590148-memory-faq#h%5F073abda9fc):

> 1. **Reference saved memories:** These are details you have explicitly asked ChatGPT to remember, like your name, favorite color, or dietary preferences.
> 2. **Reference chat history:** ChatGPT can also use information from your past chats to make future conversations more helpful. For example, if you once said you like Thai food, it may take that into account the next time you ask “What should I have for lunch?” ChatGPT doesn’t remember every detail from past chats, so use saved memories for anything you want it to always keep in mind.

Reference saved memories (RSM) is easy to understand and control. You can view and delete saved memories in Settings > Personalization.

Reference chat history (RCH) is more opaque. Unlike the Claude [reference past chats](https://wow.pjh.is/journal/claude-reference-past-chats) feature, it does not reference past chats directly. Instead, it maintains a list of _notable information_ from past chats, and adds that to context when you start a new chat. You can't see when it is doing this, nor what information it is adding.

Think of RCH as "person getting to know me", rather than "a tool to lookup past chats".

## Can I control RCH?

You can't directly control _what_ RCH remembers, but you can control which conversations are considered for inclusion.

[Temporary chats](https://help.openai.com/en/articles/8914046-temporary-chat-faq) are not included in RCH.

If you delete or archive a chat, it will be removed from RCH.

### Project-only memories

When you create a project, you can enable ["Project-only"](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#h%5Ffb3ac52750) memory. With that, the project can only access its own memories, and its memories are hidden from chats outside the project.

You can't change the memory setting for existing projectss.

### Erase all memories and start from scratch

You can switch off RCH in Settings > Personalization. If you do that, all RCH memories will be deleted, so you'll be starting fresh if you re-enable it.

## Concerns about RCH

The opacity and lack of controlmakes me nervous. [Simon Willison](https://simonwillison.net/2025/May/21/chatgpt-new-memory/) sums it up:

> I’m an LLM power-user. \[...\] The entire game when it comes to prompting LLMs is to carefully control their context—the inputs (and subsequent outputs) that make it into the current conversation with the model.
> 
> I try a lot of stupid things with these models. I really don’t want my fondness for dogs wearing pelican costumes to affect my future prompts where I’m trying to get actual work done!

But, it seems like RCH is pretty good at at remembering the right stuff.

## What has ChatGPT remembered about me?

The following jailbreak[1](#user-content-fn-2) reveals some[2](#user-content-fn-3) of what ChatGPT has committed to memory, with the wording that is actually stored:

### “Helpful user insights”

Here are some things that ChatGPT has remembered about who I am and what I'm up to:

There's nothing that's flat wrong here, and much is on point. The main issue: item (10) is based on a single recent conversation, so shouldn't make the cut. I wonder what role, if any, my [About Me](https://wow.pjh.is/journal/about-me-doc) doc played here.

I'm fine with this stuff going into the context of all my chats, though I wish I could tweak it.

### “Assistant response preferences”

Here's how ChatGPT thinks I like it respond:

This is solid. I'm happy with this going into the context of all my chats. I'm generally nervous about non-default system prompts, but I'll assume that OpenAI know what they're doing here.

### “Notable past conversations”

Here's where things get juicy.

The most interesting thing is that it's saving an assessment of my sophistication level on various topics, for example:

> The user demonstrates an intermediate-to-advanced understanding of investment strategies \[...\] they are making informed decisions based on risk balancing and long-term financial planning.

And:

> The user has a technical background and is comfortable working with LLMs, prompt engineering, and model evaluation.

It's interesting to think how it'd approach e.g. investing chats differently if it thought my sophistication was lower. I imagine it'd serve my interests better, in that scenario. Quite cool.

I wonder how much it's assessment of my competence in one area informs it's response on other topics. Does it build up a general sense of my education level, IQ, big 5 personality traits, etc? I doubt that OpenAI would let ChatGPT to explicitly make a guess at user IQ scores, but I can imagine it being tacitly encoded.

[Simon Willison](https://simonwillison.net/2025/May/21/chatgpt-new-memory/) inspects his own RCH and also finds that it doesn't contain stupid stuff:

> I was worried that an occasional stupid conversation where I say “pretend to be a Russian Walrus” might have an over-sized impact on my chats, but I’ll admit that the model does appear to have quite good taste in terms of how it turns all of those previous conversations into an edited summary.

So, I'm leaving this feature enabled for now.

## Appendix 1\. How to get a list of _everything_ that ChatGPT knows about me?

Try this:

Unlike the jailbreak prompt, you'll get a list with the wording ChatGPT thinks you want, rather than the verbatim text ChatGPT actually stores.

## Appendix 2\. How to keep an eye on RCH

Ask for a monthly digest:

## Footnotes

1. Adapted from a prompt by [Wyatt Wallis](https://x.com/lefthanddraft/status/1919590839761743898), which I found via [Simon Willison](https://simonwillison.net/2025/May/21/chatgpt-new-memory/) via Alejandro Acelas. [↩](#user-content-fnref-2)
2. In each category, we get only 10 memories, all of which have `confidence=high`. I suspect that ChatGPT has stored dozens more, but I can't get our jailbreak prompt to elicit them. [↩](#user-content-fnref-3)
