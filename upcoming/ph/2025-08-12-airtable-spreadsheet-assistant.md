# The Airtable sidebar assistant is great

*Source: https://wow.pjh.is/journal/airtable-spreadsheet-assistant*  ·  *Published: 2025-08-12*

---

The Airtable sidebar assistant ("Airtable Omni") is good.

I decided to play around some more, after having a great time with [data enrichment](https://wow.pjh.is/journal/spreadsheet-data-enrichment) and specifically [Airtable AI fields](https://www.airtable.com/guides/scale/how-to-use-airtable-ai).

I started with a sheet like this:

```
Name, Email, Job title, Organization, Job description

```

Some prompts I tried:

Result: a column with the following forula:

```
"https://tally.so/r/mKjgXD?name=" & ENCODE_URL_COMPONENT(scheduler_display_name) & "&email=" & ENCODE_URL_COMPONENT(scheduler_email) & "&job_title=" & ENCODE_URL_COMPONENT({AI Job Title (internet)})

```

Perfect.

Next:

Bad. Most of the profile links were hallucinated.

I tried again:

It worked. All the links were valid, and the correct person. Some cells were correctly marked as "Profile not found".

Why did it work the second time? Airtable had written a prompt for the AI field, and the first draft was bad.

Next:

Result:

Solid.

It worked.

Result:

Nice!
