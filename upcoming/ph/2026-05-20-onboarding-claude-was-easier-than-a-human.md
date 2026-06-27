# Onboarding Claude was easier than onboarding a human

*Source: https://wow.pjh.is/journal/onboarding-claude-was-easier-than-a-human*  ·  *Published: 2026-05-20*

---

[TYPE III AUDIO](https://type3.audio/) (T3A) provides bespoke AI narration services for the AI safety and effective altruism communities. The project was my main focus during [2023](https://blog.type3.audio/year-1-review/index.html), and I've since run it in "maintenance mode"—serving existing clients but rarely onboarding new ones—while I prioritise other things.

This is a painful situation: many orgs in the community would benefit from narration services and I'd love to serve them. The bottleneck: onboarding new clients is a surprisingly complex process that takes 1–5 days of work. I've not found a contractor who can handle this.

But: whenever you want to hire these days, you should ask "can I just hire an AI?"

So I tried that approach for our latest client, [Epoch AI](https://epoch.ai/).

This post describes how I approached this, and how it went.

## tl;dr

Claude saved me roughly a day of work, despite the one-off investment in training it. I guess it'd save as much as 2–3 days for the next comparable client.

To give a sense of the complexity of our client onboarding process, here's what the final skills look like:

- 1.1K lines / 8K words of procedural instructions in SKILL.md files.
- 14 reference files totalling 1K lines / 8K words.
- \~150 numbered steps.
- \~30 code blocks (SQL, bash, curl, TypeScript).
- 35 checklist items.

## Getting started

I asked Claude to read over all of T3A's internal documentation and client notes, and then write a comprehensive overview of "what T3A does, and how everything works". Then I had it draft a detailed description of the client onboarding process, which we iterated on together. My main input was a long, stream-of-consciousness context dump, then voice notes on some of the specifics.

The output was a first draft of a `t3a-client-onboarding` skill.

## Preparing the service contract

Once the client and I had informally scoped the project and agreed to go ahead, the next step was to formalise it into a service contract. I asked Claude to handle this, giving it the client correspondence (emails and call transcripts) as context.

Claude looked at previous service contracts in my Drive, and drafted a new one. To do that, it merged in the service details agreed with this client, found client details online (registered address, charity number, etc), created a Google Doc, and downloaded a PDF ready for signature.

My role in this:

- The contract draft required minor stylistic edits on my side, and I added one clarificatory detail that I'd neglected to include on previous contracts.
- Claude's browser use function created a new item for signature via Signwell, but was unable to use the file upload dialog. I could have asked Claude Cowork to do this via Computer Use—or just switched to a document signing service that has an API—but I just did it myself.

## Adding the client to Slack and our internal portal

With contracts signed, the next step was to create a Slack Connect channel and invite the client. Claude made the Slack channel via browser use (having looked at our existing pattern for channel names) and then gave me the Slack connect link to send to the client.

For our client portal, we need to add some info to a database, and then grant client access via Cloudflare. Claude did the former. For security, I decided not to automate the latter step via browser use, asking Claude to just open the Cloudflare dashboard to the correct URL, and remind me of a Cloudflare UI gotcha that once caught me out in the past.

## Website analysis and preprocessing

Now the work proper. To make an audio narration, our narration system takes the original article text and generates a _narration script_, the text that will actually be read by the narrator. For the best result, we tailor the narration script pipeline to each individual client.

Step one is to test the basics. Are we extracting title, author, metadata, and post content correctly? Are we excluding obvious noise (e.g. footnote sections, author bios, newsletter CTAs)?

From there, we crawl a bunch of articles, identify all the special components—graphs, images, tables, LaTeX formulae, asides, footnotes, collapsible elements—and set general rules for how best to narrate them. For images, this might mean narrating captions that the client already provides, or generating an LLM description with a prompt that might need tailoring to the client's content. For asides, perhaps we should completely omit them, unless condition X applies. Etc.

Claude did a solid first pass on this—roughly as good as an untrained human might, though with a few glaring errors that a conscientious human would not have made. I gave a bunch of feedback, and we generated detailed guidelines. These will enable far better performance next time Claude does this.

At this point, we have a plan for how to tailor our narration system to the client's content. Now we need to implement it in our codebase. Predictably—but let's not forget how incredible this is—Claude more or less one-shotted the work. Iteration was only required where I didn't fully realise what I wanted until I saw the initial results.

Writing this, I realise that I've never tried to get Claude to do a great job of substituting for my review at this step—not bugfixing, but rather asking _again_ "what makes sense here?", "how could this be better?", "what was my initial vision missing?". I might try making a general skill for this.

With this initial work on the narration script system done, it was time for proof-listening. Claude suggested a handful of articles to test, and generated the MP3s. I also asked it to crawl the site and look for especially tricky passages (e.g. lots of technical notation) and make short MP3s for me to check there. It did a great job of this.

I have tried getting AIs to proof-listen audio files for TTS mispronunciations, but none of them can do this reliably right now. So that remains a time-consuming human task. I considered asking Claude to hire and manage a contractor on Upwork for this stage, but felt it would add too much calendar time delay. I will try this soon, though.

While doing this, it occurred to me that, now that coding is automated, it'd take just a few minutes to greatly improve our internal proof-listening tool. So we did.

## Client notes and sample narrations

From there, I needed to create sample narrations to share with the client, and share notes on the narration approach for discussion.

Claude handled the former with ease. And it did a fine job listing the key judgement calls we'd made that might be worth discussing with the client.

## Audio player mockups

Another task at this stage is to create visual mockups of how the client could add the audio player to their website. Claude did an amazing job of this, making a copy of the client layout from their live site, adding their brand colours to the audio player attributes, and so on. My main input was suggesting three different ways the web design could work.

Claude even created the screenshots of each layout for this preview page.

## Narration podcast feed

Clients make narrations available via their websites, but also via an automatically updating podcast feed. Claude one-shotted the setup—even creating the podcast cover art after downloading the client's logo from their website and checking the iTunes store docs for the required image dimensions. I used an image editor to manually make minor improvements to the cover art it generated.

## Messaging the client

With the above work done, I asked Claude to draft the status update message I'd send to the client. The draft was verbose and horrible in other ways, so I just re-wrote from scratch.

Throughout the whole project, all client communications were written almost from scratch by me.

Why? My style is _much_ more concise than Claude wants to be—more telegraphic, more bullet points. I didn't try hard to improve the style imitation, because drafting from scratch also helps me check that everything has been done properly.

The main way to get Claude's help at this stage is to ask it to generate a bullet list of points I might want to cover, and then to check the draft message for clarity.

## Stepping back

Onboarding a complex client like Epoch typically requires 4–5 days of full-time work.

For this client, Claude saved me roughly a full day of full-time work, despite the one-off training investment. I guess it'd save as much as 2–3 days for the next comparable client.

Most striking: "hiring" and onboarding Claude was _much_ easier than hiring and onboarding a human contractor. Ballpark 1 day for Claude, versus 3–5 days for a human. And Claude isn't going to go on holiday, or quit 6 months later.

If I had a dream colleague, I'd be able to simply say "please onboard this client, figure it all out, use your judgement, complete the task"—and they'd do it. For a client like Epoch, that's completely unrealistic for the human contractors I could plausibly hire. Claude definitely can't work with that level of autonomy either—yet.

That said: some clients have much simpler requirements than Epoch, e.g. make a narration podcast for a Substack newsletter. I expect Claude could cut the onboarding work for such a client from 5–10 hours to 3–5 hours, perhaps even 1–3 hours if I spent a day further streamlining the process. In that scenario, my time would mostly go to client comms, proof-listening, and other "oversee your employee"-style checks.

## What's next

Overall, this went well enough that I'd like to test the skill with another comparably challenging client sometime soon. If it goes well, perhaps I can onboard a bunch more during the summer.

The work is now awaiting feedback from Epoch—the narration service will soon go live on their website.
