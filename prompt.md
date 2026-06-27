# Prompt: short, principle-based agent instructions

Make edits to CLAUDE.md and AGENTS.md, like the global settings. An edit I want
to make: currently they have instructions stating that the instruction files
should be kind of short and concise and in bullet points. I feel there's
something more I want to do, which is to try to extract the core principles.
Currently, a lot of the instructions there feel like they come from a core
principle that could be stated instead — it's the difference between describing
each element and describing the criteria for inclusion in that set.

I want something like that in many cases where we're showing, through individual
rules, what we want the agent to do. Oftentimes there's this inclusion
principle, this criterion, that we could describe that would let the agent
re-derive those rules. I'd like you to create a markdown in the nonce folder
explaining what the core principles might be behind the current rules we have,
and how you would summarize them. It doesn't have to be a short sentence, but it
does need to be a really clear sentence — like a Paul Graham sentence — such
that our instructions can be shorter, cleaner, and more generalizable.

For that, we need to discuss what the underlying principle is. Maybe we can
include an instruction in CLAUDE.md and AGENTS.md that tells the agent to add
things in this way. What's the underlying principle — the generating principle —
that we're trying to use for adding things to CLAUDE.md? And then, if the agent
makes edits, it should look for that principle and explain to the user how it
arrived at that principle, including any principled alternatives for how to do
it. Give it a shot.
