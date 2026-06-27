# Claude creates my invoices, sends them, and verifies payment

*Source: https://wow.pjh.is/journal/claude-skill-send-my-invoices*  ·  *Published: 2025-12-05*

---

As a freelancer, every month I have to:

1. Review the work I did
2. Create and send invoices
3. Check the previous month's invoices were paid

There's quite some complexity in this process. Different clients have different hourly rates. I invoice coaching clients per session, not by the hour. Projects have fixed quotes sometimes. And so on.

**Claude now handles >90% of the work.** What was a 1-hour task now takes 5 minutes.

## What the skill does

The parts in <span style={{ color: 'red' }}>red require manual action from me. The rest are handled by Claude:

1. Create a monthly admin task list in Obsidian.
2. Download time reports from Toggl, extract the billable hours for each client, save PDFs for my records.  
   1. <span style={{ color: 'red' }}>Ask me to check before proceeding.
3. Create invoices:  
   1. For hourly clients, draft invoices based on Toggl data.  
   2. For coaching clients, get session counts from Google Calendar.  
   3. <span style={{ color: 'red' }}>Ask me to check before proceeding.[1](#user-content-fn-1)  
   4. Create invoices in Xero.
4. Email invoices to my clients.  
   1. <span style={{ color: 'red' }}>Remind me to manually submit invoices for one client via Deel.
5. Confirm that last month's invoices were paid:  
   1. Search Gmail for payment notifications and cross-check with Xero.  
   2. <span style={{ color: 'red' }}>Ask me to check before proceeding.  
   3. Mark invoices as paid in Xero.

## How I made this

In short:

I use [Claude Code](https://www.claude.com/product/claude-code), which might look a little scary. But it's just like the chat app you're used to, with extra powers.[2](#user-content-fn-2) [Everyone should use it](https://wow.pjh.is/journal/everyone-should-use-claude-code).

Creating the skill took 1-2 hours. It was all done in conversation with Claude—I didn't write any code. At times my software engineering background was helpful, but this could be done without that—it just might take a little longer.

## Footnotes

1. If corrections are needed, I just explain them verbally—just as I would to a human assistant. I don't have to suddenly start coding to handle an edge case. [↩](#user-content-fnref-1)
2. The Claude web app has a restrictive security sandbox. So, if there's no [connector](https://www.claude.com/connectors), you can't interact with apps like Xero or Toggl. It also can't automatically download and manipulate files on your computer. Finally: creating Claude skills is faster with Claude Code. [↩](#user-content-fnref-2)
