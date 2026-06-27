# Can ChatGPT Agent book a hotel? Yes.

*Source: https://wow.pjh.is/journal/can-chatgpt-agent-book-hotel*  ·  *Published: 2025-08-18*

---

Can [ChatGPT Agent](https://help.openai.com/en/articles/11752874-chatgpt-agent) do this?

Specifically: can it consider my preferences and select the hotel that I would have chosen?

In short: **yes**. Will I actually use it? Borderline, but yes.

## How to make this work

To efficiently delegate to a human assistant, you need to write detailed instructions. Same goes for an AI agent.

Further reasons that ChatGPT Agent needs instructions:

1. Without guidance, the agent is likely to search many different websites. For each new website, it has to figure out the UI. It usually succeeds, but it can take a fair bit of trial and error. So it ends up running for 20+ mins. And at that point it starts crashing.
2. UK banks currently block ChatGPT from starting the "3D Secure" payment authentication flow [1](#user-content-fn-1). Probably US banks do too.

If you _just_ say the "Please book a hotel for date X at venue Y", the process will—at best—take longer than searching yourself. At worst it'll fail because the agent tries to book via a website it can't handle.

You need to give instructions like this:

Critical features of these instructions:

1. They specify Booking.com.
2. They use the exact Booking.com filter names. This helps the agent find them more quickly.
3. They use my Booking.com account, so credit card authentication is not required. [2](#user-content-fn-2)

I ran this prompt three times. Each time it correctly chose my preferred option at Gatwick Airport, and browsed all the way to the "enter CVC to confirm booking" screen, where it asked me to take control.

Each run took 5-10 minutes.

I also tried this for Stanstead airport, again with success.

Finally, I tried this for Reykjavík, with a small addition to my default preferences:

On the first run, it failed to find any hotels that met my criteria. The issue was that hotels in Reykjavík mostly don't bother mentioning that they have air conditioning, so that filter ruled out all the options that had a gym.

I asked it to try again without the air conditioning requirement. The results were excellent! I know the west side of Reykjavík very well, but its top choice was a hotel I didn't know, and that was solidly better than the other options. Nice.

## Issues

1. In Agent mode, ChatGPT ignores "project instructions". So you need to paste the instructions into the chat window each time. 🤦
2. As mentioned above: the "3D Secure" payment authentication flow will probably be blocked by your bank.
3. Minor inaccuracies: on one run, the agent reported a hotel as four stars when it was actually three. On another, it reported a 100 yard walk to the terminal when it is actually 5 minutes. This makes me nervous—what caused these errors? [3](#user-content-fn-3) Might it make sometimes make important mistakes?
4. You can only trigger ChatGPT Agents via the chat window (not via e.g. Zapier). For frequently repeated use cases (e.g. refund a customer), this would be annoying (I'd try Lindy.ai instead).

## For _finding_ hotels, why not use ChatGPT 5 instead of ChatGPT Agent?

Only the Agent can click buttons to check prices and availability for a given date.[4](#user-content-fn-4)

## Will I use this?

Yes, because it's an interesting capability eval.

If I exclude that motivation, the answer is "borderline yes, for places I don't know". Here's what that'd look like:

1. I'll make the request.
2. I'll do other tasks while I wait.
3. I'll check the top suggestion by reading the listings for the hotel it suggests, and the two runner ups. I'll also glance at the full Booking.com search results.[5](#user-content-fn-5)
4. If the suggested option is good, I'll click "take control", enter the CVC code, and press "confirm booking". Otherwise, I'll book something else via my regular browser.

I've booked more London airport hotels than I care to remember, so for those it just wouldn't save me any time.

I wasn't expecting this to work as well as it did. In particular, the UI navigation was much faster and more reliable than previous computer use demos I've played with.

## Footnotes

1. "3D Secure" is the thing where you have to verify with your phone. Some websites skip this flow after the first purchase. [↩](#user-content-fnref-1)
2. On the first run (but not subsequent runs), the agent prompts me to take control and login to booking.com. [↩](#user-content-fnref-2)
3. My guess: hallucination. For some reason, the agent doesn't manage to extract the info while browsing. Then, when writing up the answer, it choses the next token based on its pre-trained knowledge. Often that works out fine, since the training data contained the info. But sometimes it won't, and then you get the hallucination. [↩](#user-content-fnref-3)
4. GPT-5 Thinking gave a good list of hotels, but was unable to get availability or prices for a specific date. It took 10 minutes. GPT-5 Pro gave an [excellent answer](https://chatgpt.com/share/68a57e42-74fc-8008-abbb-bbf5bce5d720), but did not check live prices. It explained that it's unable to press buttons. GPT-5 Pro with Deep Research gave a [solid answer](https://chatgpt.com/share/68a582d8-62e0-8008-b1ee-a43f0578cdea), but it wasn't super clear that it had checked the live prices and availability for the specified dates. The prices it gave were approximate and did not match the ones I see when I search. The "Thinking" log suggested that it _was_ searching specific dates, but I suspect it wasn't, again due to inablity to press buttons. [↩](#user-content-fnref-4)
5. My prompt makes this much easier, by making sure that the agent's response includes the links for this. [↩](#user-content-fnref-5)
