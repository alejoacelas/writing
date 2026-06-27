# Make your LLMs ready to hand

*Source: https://wow.pjh.is/journal/make-llms-ready-to-hand*  ·  *Published: 2025-08-12*

---

If you want to use LLMs more often, put them within easy reach. When you're working, they should be less than one second away.

## On your smartphone

Easy: add the apps to your home screen.

## On your MacBook

I'll describe a couple of different methods. Overview:

| Method            | Setup Time    | Rating    |
| ----------------- | ------------- | --------- |
| Browser shortcuts | < 1 minute    | 2/5 stars |
| Desktop apps      | 5 minutes     | 2/5 stars |
| Dedicated browser | 10-15 minutes | 4/5 stars |
| Terminal helper   | 10-15 minutes | 5/5 stars |
| Raycast AI        | 5 minutes     | 3/5 stars |

I strongly recommend taking the time to set up one or both of the "dedicated browser" and "terminal helper" methods.[1](#user-content-fn-1)

### Method 1: Browser shortcuts

In your web browser, type `Command + T` to open a new tab. Type `"cl"` or `"ch"` and press enter.

If that doesn't work, go to chatgpt.com and claude.ai, and add them to your bookmarks (`Command + D`).

**Rating:** 2/5 stars—it's too slow. Several keystrokes are requried, and you have to wait for the app to load. It's also hard to find that tab again, if you're switching between the LLM and other tabs.

### Method 2: Desktop apps

Download the desktop app for [ChatGPT](https://chatgpt.com/features/desktop/) or [Claude](https://claude.ai/download).

With ChatGPT installed, you can access it by pressing `Option + Spacebar`.

With Claude, open "Settings" and set the shortcut to `Control + Spacebar`. (N.B. Not the `Command` key).

**Rating:** 2/5 stars. The desktop apps have some major limitations. Critically: in ChatGPT you can't attach Google Docs. In both, you can't easily switch between multiple parallel conversations. This method doesn't give you easy access to Gemini and Grok. And you can't use [BetterChat](https://hartreeworks.org/better-chat).

## Method 3: Dedicated browser

1. Download a web browser you don't use by default (e.g. [Edge](https://www.microsoft.com/en-us/edge/download) or [Brave](https://brave.com/download/)).[2](#user-content-fn-2)
2. Open that browser and disable the annoying default features (e.g. AI chat sidebar, crypto stuff, news articles on the new tab screen).
3. Add ChatGPT, Claude, Gemini and Grok to the bookmarks toolbar.
4. Configure a keyboard shortcut to switch to that browser.[3](#user-content-fn-3)

**Rating:** 4/5 stars. Setup is a faff, but it's great once done.

## Method 4: Terminal helper

If you use [Claude Code](https://wow.pjh.is/journal/everyone-should-use-claude-code), install my [Ask Many Models](https://github.com/HartreeWorks/skill--ask-many-models) skill. Say "ask many models: \[your question\]" or run `amm` from the terminal. It queries GPT, Claude, Gemini, and Grok in parallel, then synthesises the results into a single document.

**Rating:** 5/5 stars. Setup is a faff, but it's then very easy to query many models at once and get an automatic synthesis of their replies.

## Method 5: Raycast AI

[Raycast](https://www.raycast.com/core-features/ai) has a built-in AI chat that supports 30+ models from OpenAI, Anthropic, Google, xAI, and others. Access it via hotkey from anywhere on your Mac.

**Rating:** 3/5 stars. Quick setup and easy to use. But the responses aren't formatted as well as when you use the native apps (method 3), and you can't easily query several models at once (method 4).

## How to prompt many models at once

Often, it makes sense to [ask many models](https://wow.pjh.is/journal/ask-many-models). Try [Tile](https://wow.pjh.is/journal/use-tile-to-ask-many-models) for that, or use the terminal helper above.

## Appendix 1\. Keyboard shortcuts within ChatGPT and Claude

I've made a tool for that: [BetterChat](https://hartreeworks.org/better-chat).

## Footnotes

1. I'm frustrated that I haven't found a method with lower setup time. I'll keep trying... [↩](#user-content-fnref-1)
2. If you go for Firefox or Safari, you won't be able to use browser extensions like [BetterChat](https://hartreeworks.org/better-chat). [↩](#user-content-fnref-2)
3. I recommend [this method](https://notes.pjh.is/Use+the+CAPS+LOCK+key+for+custom+keyboard+shortcuts). [↩](#user-content-fnref-3)
