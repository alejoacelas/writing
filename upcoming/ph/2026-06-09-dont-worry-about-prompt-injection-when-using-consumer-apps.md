# It is totally fine to connect Google Workspace to Claude, ChatGPT and Gemini (and to enable browser use)

*Source: https://wow.pjh.is/journal/dont-worry-about-prompt-injection-when-using-consumer-apps*  ·  *Published: 2026-06-09*

---

Many people worry about granting access to their Google Workspace (Gmail, Google Docs, etc)—and enabling [browser use](https://claude.com/claude-for-chrome)—due to concerns about prompt injection.

How does prompt injection work? In short: some malicious third party gets a prompt into your AI assistant, and that prompt makes it do something you don't want (e.g. send them your private data, or your Bitcoins).

Prompt injection comes in three flavours:

- **Indirect prompt injection (IPI):** the nasty prompt comes from an external source, which is consulted while the agent runs (e.g. a website, email or calendar invitation).
- **Direct prompt injection (DPI):** the nasty prompt is entered by the user. That might be a rogue employee, or an attacker that has gained access to your AI assistant (e.g. someone who stole your ChatGPT login).
- **User-mediated prompt injection (UMPI):** you enter the nasty prompt yourself, after being tricked into pasting or uploading it. [1](#user-content-fn-1)

DPI is familiar—a consequence of "someone got access to my stuff". The protections are the standard ones: 2-factor authentication, don't tell Bill Gates your password when he calls you, etc.

IPI is the _new thing_ that many people are afraid of. It is scary in theory, but empirically we've seen no real-world incidents causing harm on the order of $1M or more.[2](#user-content-fn-2) We've seen just one case with harm on the order of $100K.[3](#user-content-fn-3)

In short, I think:

1. When it comes to IPI, the major labs are winning the defence vs offence battle so far.[4](#user-content-fn-4)
2. When using consumer apps from Anthropic, OpenAI or Google, most people's chance of suffering $100K+ harm due to IPI during 2026 is near zero (less than 1/1000). That is, perhaps $100 in expectation.[5](#user-content-fn-5)
3. User error is >10x more likely to cause trouble when using these apps. We should focus on that risk, and mostly stop thinking about IPI.
4. UMPI is a bit more concerning than IPI: it's harder for AI companies to detect. For now though, base rates suggest that most people's risk of major harm in 2026 is also less than 1/1000.

## Will prompt injection risk increase soon?

In April 2026, [Google security researchers](https://blog.google/security/prompt-injections-web/) found no evidence of significant harms via IPI so far. However, they wrote:

> In general, threat actors tend to engage based on cost/benefit considerations. In the past, IPI attacks were considered exotic and difficult. And even when compromised, AI systems often were not able to execute malicious actions reliably.
> 
> We believe that this could change soon. Today’s AI systems are much more capable, increasing their value as targets, while threat actors have simultaneously begun automating their operations with agentic AI, bringing down the cost of attack. As a result, we expect both the scale and sophistication of attempted IPI attacks to grow in the near future.

They're right: attacker efforts will increase, and the total risk of prompt injection may also increase. But my risk guesstimate for 2026 (claim #2 above) tries to adjust for that.

Clearly there's uncertainty here (AI progress, eek!), and all bets are off for 2027\. But do you really think it's 1/100, or 1/10, in 2026?

We could BOTEC this as follows:

```
P($100K+ harm/user-year)
  ~= N risky agent tasks
   * P(malicious injection exposure per task)
   * P(costly intent | exposure)
   * P(model + orchestration fail | costly attack)
   * P(agent has $100K-relevant authority | attack succeeds)
   * P(user fails to catch/stop/reverse it)
   * P(loss is irreversible and reaches $100K)

```

My numbers are [here](https://docs.google.com/spreadsheets/d/1YWqlJhl%5F3cVRmYyogJKmNOKf3b%5Fcs3xwIt0LSEaDBdE/edit?gid=80318169#gid=80318169).

How to square this with all the scary research papers, including scary numbers from the model system cards themselves? In short: they're almost always testing models without the full-stack of orchestration safeguards that are applied to the consumer apps from Anthropic, OpenAI and Google.

## Apps that are not made by Anthropic, OpenAI and Google are much more risky

The agents in even "second tier" apps like Cursor, Cline and Replit have weaker safeguards.[6](#user-content-fn-6) I would hesitate to give these broad access to sensitive data, or enable browser use on anything other than local development domains.

It's the same heuristic as with other software procurement: the very top companies have the very strongest security teams, and are just miles safer than even the second tier. Your bar for using e.g. Typeform over Google Forms should be high.

## What about Claude Code, Codex and Gemini CLI?

I'd guess that agent CLI safeguards are somewhat less conservative. But again, empirically we've seen no IPI horror stories. So: as with the consumer apps, I treat IPI risk as low enough to largely ignore in practice. The main time I think about it is when installing third-party skills or MCP servers—I'll check for credibility signals, ask my assistant to audit the files, and sometimes skim-read files myself.

## User error is much more likely to cause trouble than prompt injection

So—IPI is overrated in these contexts. A better reason to worry about granting access: user error, without malicious prompts involved (e.g. user gives an ambiguous prompt and the AI makes a [costly wrong assumption](https://wow.pjh.is/journal/flag-ambiguous-data); user gives a good prompt but the AI just does something stupid). In 2026, this seems far more likely to cause someone $100K+ of trouble than IPI. Let's say: >10x more likely, for an upper bound of \~1/100.

But again: the consumer apps have pretty good guardrails against user error. And everyone has continuous backups via Backblaze or similar (right)? So far, I've heard of no major incidents ($1M+).

Novices who make heavy use of Claude Code or Codex seem more likely to get into trouble, but even there, `auto` mode offers strong protection.

## Bottom line: just grant access

All-things-considered, I think the cost:benefit unambiguously says that nearly all[7](#user-content-fn-7) users of Anthropic, OpenAI and Google apps should:

1. Connect Google Drive and Gmail (read and write[8](#user-content-fn-8)).
2. Enable browser use (in their usual authenticated Chrome profile[9](#user-content-fn-9)).
3. Focus their caution on user error, not IPI.

Is this a controversial take among experts? I don't think so. I shared a draft of this post with several AI power users, and a couple of people who work on AI adoption and security at large orgs in the EA / AI safety community. All agreed with the bottom line.[10](#user-content-fn-10)

The labs apparently think this too, since they're offering the features. Anthropic's [help docs](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely#h%5F66ba46aa5e) say "be cautious \[when\] granting access to sensitive information like financial documents, credentials, or personal records". But they do not say: "don't do it". This is striking—one might expect them to cover their backs harder here.

The same bottom line holds for Claude Code and Codex users, though it's less clear cut for people without a technical background. If you're shipping code to production systems, I'd add some [deterministic hooks](https://wow.pjh.is/journal/claude-code-permissions-whitelist) on top of `auto` mode.

To repeat: I am only advocating this bottom line for apps created by Anthropic, OpenAI and Google. I would be more cautious elsewhere (though I'm sure the cost:benefit would go through in some cases).

Given the above, the message for your team should be:

> It is totally fine to connect Google Workspace to Claude, ChatGPT and Gemini, and to enable browser use. Worry about user error, not IPI.

In an organisational context, access should be granted via managed MCP servers (e.g. the team/enterprise version for the consumer apps; perhaps something like [MintMCP](https://www.mintmcp.com/) for the CLIs).[11](#user-content-fn-11)

The case for this "totally fine to connect" bottom line should be re-assessed every couple of months. The risk of costly incidents of user error, IPI, UMPI—or something else associated with high-privilege agent access—may increase significantly. But I would be fairly surprised if it increased _enough_ to change the bottom line anytime soon.

## Appendix 1\. What if I'm unusually likely to be personally targeted by hackers?

Are the bottom lines different if you're a public figure, CEO, etc? So far as IPI goes, no. You should worry >10x more about social engineering attacks, such as phishing. 2FA everywhere, right? UMPI is a new kind of social engineering. Currently it is very rare, but if you're copy-pasting prompts into your assistant, read the prompt before you send it.

If you're making heavy use of agent CLIs, you should either have a technical background or have your setup audited \~monthly by someone who does (mainly to reduce your risk of user error).

## Appendix 2\. What about computer use?

In this post, I won't take a position on this. If the cost:benefit doesn't go through right now, it's because of the risk of user error.

## Appendix 3\. What about Hermes and OpenClaw?

My view on IPI risk with Hermes is mainly based on two heuristics:

- For: Nous Research give off lots of "high competence" signals.
- Against: "Trust top companies more".

On balance I end up with the same bottom line: I'm not worrying about IPI with Hermes, and am >10x more worried about user error.

OpenClaw: I stopped using it partly due to security concerns. Not a specific concern about IPI, but rather just a general heuristic of "seems like a mess, some incidents suggest incompetence".

## Footnotes

1. UMPI is my own coinage—there's no standard label for this. [↩](#user-content-fnref-1)
2. Simon Willison (January 2026): ["Every six months I predict that a headline-grabbing prompt injection attack is coming soon, and every six months it doesn’t happen."](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/) [↩](#user-content-fnref-2)
3. An [incident](https://oecd.ai/en/incidents/2026-05-04-4a73) involving Grok, from May 2026\. [↩](#user-content-fnref-3)
4. They’re combining model training with application-layer guardrails on top. The latter do a lot of the work, and include a bunch of deterministic safeguards. [↩](#user-content-fnref-4)
5. I get this number by [rounding up an already conservative BOTEC](https://docs.google.com/spreadsheets/d/1YWqlJhl%5F3cVRmYyogJKmNOKf3b%5Fcs3xwIt0LSEaDBdE/edit?gid=80318169#gid=80318169). Of course: [expected value reasoning should be tempered when there is risk of ruin](https://claude.ai/share/c3a58cb6-8dde-4804-8e72-e1a8437e0ce7). But I don't think that changes the bottom line. [↩](#user-content-fnref-5)
6. I mainly think this on priors. Empirical evidence is limited, but supportive. See e.g. [this study](https://arxiv.org/html/2603.21642v1) (spring 2026). [↩](#user-content-fnref-6)
7. Are you handling catastrophic infohazards? Well ok then. [↩](#user-content-fnref-7)
8. By default, the consumer apps always seek approval before they send an email. That's a good safeguard against user error. [↩](#user-content-fnref-8)
9. Anthropic docs currently [recommend](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely) using a dedicated profile. But they know that roughly nobody will do this. Moreover, their current "grant access per domain" safeguard reduces the marginal benefit of using a dedicated profile to roughly nil. [↩](#user-content-fnref-9)
10. If you disagree, please [email me](mailto:wow@pjh.is), or [suggest a time to call](https://pjh.is/call). [↩](#user-content-fnref-10)
11. I've not tested this particular service, nor thought deeply about this product category. [↩](#user-content-fnref-11)
