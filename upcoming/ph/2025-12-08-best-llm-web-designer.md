# Web design in December: Claude Opus 4.5, or Gemini 3 Pro

*Source: https://wow.pjh.is/journal/best-llm-web-designer*  ·  *Published: 2025-12-08*

---

[Claire Vo](https://clairevo.com/) asked Claude, Gemini and ChatGPT to [redesign her blog](https://www.youtube.com/watch?v=6w0i2Wp0knM).

Claude won by a decent margin.

Gemini did fine, and ChatGPT's performance—which would have amazed me a few months ago—was just "meh" by comparison.[1](#user-content-fn-1)

Claire shipped the [redesign](https://www.chatprd.ai/blog) on the same day.

## The prompt

Claire used [Cursor](https://cursor.com/) with the following prompt:[2](#user-content-fn-2)

She tagged the codebase of her previous blog, which looked like this:

## Claude 4.5 Opus

Claude's one-shot:

Design: good layout, and it nailed nearly all the details.[3](#user-content-fn-3)

Function: Claire reports that functionality, including the SEO features, are perfectly implemented. It could be shipped as-is.

## Gemini 3 Pro

Design: reasonable layout, but some problems in the details.

Function: the job was less finished than Claude's. Opus 4.5 _keeps going until it's done_ in a way that Gemini, for now, does not.

## GPT-5.1

Design: the layout is illogical, and many visual details are off.

Function: the work was unfinished in many basic respects.

## Appendix 1\. Watch the screencast

To understand the differences in more detail, watch the full screencast:

Claire's podcast, [How I AI](https://www.lennysnewsletter.com/s/how-i-ai), is consistently good.

## Footnotes

1. Claire's results are consistent with my own [vibe](https://wow.pjh.is/journal/claude-code-vs-codex-december) [checks](https://wow.pjh.is/journal/claude-front-end-design-skill), though Twitter has not reached consensus between Gemini and Claude. [↩](#user-content-fnref-1)
2. A lazy prompt—not best practice. But ideally, things should just work, even with lazy prompting. Claire used Cursor, rather than the official CLIs, which may distort things. [↩](#user-content-fnref-2)
3. If I had to complain: on the blog subtitle "10x PM" needs a non-breaking space so that it doesn't split onto two lines. And "Latest Articles" should be sentence case, for consistency with the blog post titles. [↩](#user-content-fnref-3)
