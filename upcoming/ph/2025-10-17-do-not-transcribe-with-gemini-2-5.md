# Do not use Gemini 2.5 models for audio transcription

*Source: https://wow.pjh.is/journal/do-not-transcribe-with-gemini-2-5*  ·  *Published: 2025-10-17*

---

Google Gemini 2.5 can transcribe MP3 files.

However, the transcription sometimes silently omits major fragments of the conversation, or invents sentences or sections that were not spoken. This is difficult to detect—the inventions are plausible, and the start and end of the transcript is often accurate.

With a handful of tests, I found that this issue almost always occurs for MP3s longer than 1 hour. I've not seen it for audio files less than 30 minutes, but I've not tested enough to be confident it's reliable for shorter audio.

Several colleagues have reported similar issues.

The issue affects Gemini 2.5 Pro and Gemini 2.5 Flash, whether accessed via the Gemini web app or via Google AI Studio (with output token limit set to the maximum).

So—avoid.

See also: [how to transcribe an MP3 file](https://wow.pjh.is/journal/how-to-transcribe-an-mp3-file).
