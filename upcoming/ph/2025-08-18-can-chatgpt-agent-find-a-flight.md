# Can ChatGPT Agent find me a flight? Yes, and I will use it.

*Source: https://wow.pjh.is/journal/can-chatgpt-agent-find-a-flight*  ·  *Published: 2025-08-18*

---

Can [ChatGPT Agent](https://help.openai.com/en/articles/11752874-chatgpt-agent) do this?

Answer: yes. It [found](https://chatgpt.com/share/68a86638-6a08-8008-9f01-9ca105d2f8da) the best option, and two of the least-bad alternatives.

This request was fairly easy: there are very few direct flights from London to Clermont-Ferrand.

To find my best option for London to San Francisco, I'd need to give it much more detailed instructions, just as I would a human.

So, I'll ask ChatGPT to help me write the instructions:

<Prompt content={\` I'd like to develop detailed instructions for finding and booking flights options. Please could you interview me to figure out my key preferences, and then help me write the prompt?

To get us started, below are some notes I made for a human assistant a while ago.

---

### Booking travel - meal preference

Please always select vegetarian if given the option.

### Booking flights

If booking EasyJet flights, please always select the "up front" seats (first couple rows) that come with a larger hand luggage allowance and speedy boarding.

Favourite seat is 1D (first row, right hand aisle). Generally prefer right hand aisle seats but other seat types in first few rows are fine.

Please book directly via the airline and avoid third party agents. If booking via an agent seems >30% cheaper please pause and ask me whether to book via agent.

If you're asked to pay extra to book meals, please skip booking meals. \`}/>

After a bit of iteration, here's what we ended up with:

<Prompt content={\` Please book a flight to Iceland from London on September 25.

---

# INSTRUCTIONS

Use ONLY Skyscanner for flight search/discovery.

## Trip brief

- **From:** \[origin(s)\]. London→EEA: prefer LGW. London→USA: no preference.
- **To:** \[destination\]
- **Ticket type:** one-way (unless flying to the USA, in which case assume round-trip and request the return date if not specified).
- **Dates:** \[target dates\]. Assume ±2 days flexibility and search all five dates.
- **Cabin:** Premium Economy for transatlantic; Economy otherwise.
- **Travellers:** Book for 1 adult unless stated otherwise.
- **Traveller details:** Peter John Hartree, DOB \[REDACTED\], phone \[REDACTED\].

## Standing rules

- Prefer EasyJet for EEA flights; book "Up Front" seats (aim 1D, otherwise right-hand aisle in first rows).
- Prefer direct flights; if none exist across all ±2 days, consider 1-stop. No multi-day stopovers.
- If meals are included in the base fare, select vegetarian. Otherwise do not reserve a meal.
- **Times:** prefer depart ≥10:00 (earliest acceptable 07:00) and arrive ≤21:00 (more flexible for transatlantic).
- **Bags:** book personal item + overhead carry-on. Assume no hold luggage required. If carry-on is not included, assume £50 per person per direction.
- **Seats:** pay for front-of-cabin and ideally extra-legroom. If any single seat fee >£50 short-haul or >£100 long-haul, flag and ask before including.
- **Price vs convenience:** value 1 hour reduction in total travel time at £50\. Choose cheapest sensible non-refundable fare. No insurance.
- If a third-party agent is >30% cheaper than booking direct, pause and ask before using the agent.
- Self-transfer itineraries are allowed. Require ≥3h buffers internationally (≥4h if airport change).

## Definitions

- **"Direct"** \= no plane change. Technical stops count as a stop.
- **"Transatlantic"** \= any Europe⇄North America crossing.
- **"Total journey time"** \= block time incl. layovers (not ground travel). Times are local, 24-hour, include date if crossing midnight.
- **"Carry-on"** \= under-seat personal item + overhead cabin bag.

## Search & output

1. On Skyscanner, run searches for the target date and ±2 days. Apply filters:  
   - **Stops:** Direct only. If no direct on a date, also run a 1-stop search for that date.  
   - **Times:** depart ≥10:00 (earliest 07:00); arrive ≤21:00 (flexible for transatlantic).  
   - **Cabin:** Premium Economy for transatlantic; Economy otherwise.
2. For each date searched, include the Skyscanner results link you actually used (label date, origin, destination, and filters).
3. For top candidates, open the airline site from Skyscanner to verify:  
   - Final total in GBP, fare type (non-ref), cabin, baggage inclusions, and seat availability (front/extra-legroom; EasyJet Up Front; chance of 1D/right-aisle).

## Present (strict format)

- **Top 3 options** (each as a block):  
   - **Summary line:** **£TOTAL (incl. seat + carry-on add-ons)**• \[Airline\] \[Flight no(s)\] • \[Cabin\] • \[Date\] \[Dep time\] \[Dep airport/terminal\] → \[Date\] \[Arr time\] \[Arr airport/terminal\] • Duration \[h:mm\] • \[Direct/1 stop at XXX for mm\]  
   - **Baggage:** \[state inclusions\]. Add-ons assumed: \[list with £\].  
   - **Seats:** \[front/extra-legroom availability; EasyJet Up Front yes/no; likelihood of 1D/right-aisle\].  
   - **Why ranked #n:** apply £50/hour rule explicitly (show time vs price deltas).  
   - **Pros:** \[one line\]  
   - **Cons:** \[one line\]  
   - **Skyscanner flight details page:** \[link\]
- **Longer shortlist:** bullet list of remaining viable options with £total, times, stops, key differences.
- **Searched links:** list every Skyscanner results URL used, clearly labelled (e.g. "LGW→SFO 2025-11-18 (Direct) – \[link\]" and "LGW→SFO 2025-11-18 (≤1 stop) – \[link\]").
- **Deviations & assumptions:** call out any rule you relaxed (e.g. used LHR for EEA, seat fees above caps, no Premium Economy offered).

## URL validation checks

- Skyscanner search results and flight details page URLs always include a querystring. Do not omit the querystring parameters, and make sure they are prefixed with a "?".  
   - Correct example (search results): \`[https://www.skyscanner.net/transport/flights/lond/sfo/250831/250914/?adults=1&cabinclass=premiumeconomy\\\`](https://www.skyscanner.net/transport/flights/lond/sfo/250831/250914/?adults=1&cabinclass=premiumeconomy%5C%60)  
   - Correct example (flight details page): \`[https://www.skyscanner.net/transport/flights/lond/sfo/250831/250914/config/13554-2508311115--31697-0-16216-2508311415%7C16216-2509141605--31697-0-13554-2509151025?adults=1&cabinclass=premiumeconomy\\\`](https://www.skyscanner.net/transport/flights/lond/sfo/250831/250914/config/13554-2508311115--31697-0-16216-2508311415%7C16216-2509141605--31697-0-13554-2509151025?adults=1&cabinclass=premiumeconomy%5C%60)  
   - Incorrect example ("?" missing): \`[https://www.skyscanner.net/transport/flights/lond/sfo/250831/250914adults=1&cabinclass=premiumeconomy\\\`](https://www.skyscanner.net/transport/flights/lond/sfo/250831/250914adults=1&cabinclass=premiumeconomy%5C%60).
- Same thing for Skyscanner flight details pages.

## Red-flags (ask before proceeding)

- If I request a transatlantic flight, check whether I want one-way or a round-trip before starting the search.
- Only 1-stop options exist across all ±2 days.
- Any seat fee exceeds the caps above.
- Total exceeds my implicit time-value rule but you still prefer it.
- Third-party >30% cheaper than direct.

Then wait for approval before booking direct with the airline following the checklist. \`}/>

With that, **ChatGPT Agent found me the flight I'd actually book in 3/3 of my tests**.

The runs took 10-30 minutes.

## Can ChatGPT Agent actually book the flight?

From a "computer use" perspective, yes. However, in my tests I found that:

- The EasyJet and British Airways websites block ChatGPT Agent.
- ChatGPT is consistently blocked by the "3D Secure" payment authentication flow.

So, I would just click the "flight details" button that ChatGPT Agent provides, then book the flight myself.

## Will I use this for search?

Yes, it's faster than doing it myself, and probably more thorough.
