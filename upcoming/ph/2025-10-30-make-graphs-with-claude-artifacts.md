# Make graphs from screenshots with Claude

*Source: https://wow.pjh.is/journal/make-graphs-with-claude-artifacts*  ·  *Published: 2025-10-30*

---

You can take a screenshot of some data, and ask Claude to make a graph.

This can be much faster than e.g. exporting a CSV from Mixpanel, importing to Google Sheets, then making a graph there.

In fact, I often use Claude to make graphs from data that's already in a Google Sheet. Reasons:

1. Claude makes better looking graphs, with good formatting choices (e.g. informative subtitles).
2. It often makes the graphs interactive in useful ways. Sometimes it's nice to paste a screenshot of the Claude graph into a Slack discussion or Google Doc report, _and_ link to the interactive artifact.
3. Using Sonnet 4.5, it typically takes 5-15 seconds. For me, that's roughly as quick as making a decent graph in Google Sheets.

Say "Use React" in your prompt to force Claude to make an interactive Artifact. Without that, it'll sometimes decide to make a rather ugly graph using Python.

[](https://claude.ai/public/artifacts/f7d59807-750e-4366-87e5-6d7158dc0c7d)

I've never seen OCR mistakes or hallucinations. My datasets always contain less than 100 cells. For larger datasets, I'd cross-check carefully (or just upload a CSV rather than a screenshot).

If you have particular requirements or style preferences for your graphs, tell Claude (once) by defining a [Claude Skill](https://support.claude.com/en/articles/12512176-what-are-skills).

ChatGPT and Gemini can do this too, but their graphs are ugly, and their defaults worse.
