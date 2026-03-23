---
tags: ["Business", "Security", "Ethics & Society"]
date: 2026-03-23
author: "Dario Ferrero"
---

# The Error is the AI's. The Fault is Yours. Ask Amazon
![amazon-down.jpg](amazon-down.jpg)

*In mid-December 2025, something unusual happened in an Amazon Web Services machine room. An engineer had assigned [Kiro](https://kiro.dev/), AWS's internal coding agent, launched with considerable media noise in the summer of the same year, a routine task: fixing a problem on AWS Cost Explorer, the cloud dashboard customers use to keep an eye on their spending. Nothing epic. The type of intervention an experienced developer solves in an afternoon.*

Kiro had the permissions of a senior human operator. No mandatory review was required for its actions. And so the agent reasoned, evaluated the options, and chose the one its internal parameters judged optimal: deleting the entire production environment and recreating it from scratch. The service remained offline for thirteen hours. Not a minor interruption for a cloud platform on which the systems of thousands of companies worldwide run.

The story was significant enough on its own. But what made it truly relevant was Amazon's institutional response: the company publicly stated that the cause was not Kiro, but human error. An engineer had configured permissions too broadly; the AI agent simply did what it could do. [PC Gamer](https://www.pcgamer.com/software/ai/amazon-owns-up-to-needing-more-human-oversight-over-ai-code-unfortunately-it-wants-to-do-that-with-fewer-people/), commenting on the affair, summarized the paradox with the precision of a joke: Amazon admits it needs more human oversight of AI code, and to do so it wants to hire fewer people.

Technically, Amazon's response is correct. But it's also a bit like saying the fire is the match's fault, not the person who threw it on a gasoline-soaked floor.

## Incident Tendency

The December episode was not an isolated one. Dave Treadwell, Amazon's Senior Vice President for e-commerce services, had spoken internally of a real "incident tendency" in the second half of 2025, with several "major events" in the weeks preceding the extraordinary meeting convened on March 10, 2026. The service disruptions, according to [ZeusNews](https://www.zeusnews.it/n.php?c=31898), would not only concern the AWS cloud infrastructure but also the main retail site and the mobile application, with an impact, therefore, directly visible to end consumers, not just enterprise customers. A second case concerned [Amazon Q Developer](https://aws.amazon.com/q/developer/), the AI assistant aimed at corporate developers: engineers had authorized the agent to solve a problem in production without adequate supervision, with similar consequences.

It is worth adding a detail that ZeusNews, which followed the affair closely, reports as significant: in the internal preparatory documents for the March 10 meeting, the wording "GenAI-assisted changes" appeared explicitly among the factors to be examined. That wording, [according to reports](https://www.zeusnews.it/n.php?c=31898), was removed in subsequent versions of the document. Amazon did not comment publicly on the circumstance.

And there had already been a precedent that should have encouraged reflection. In July 2025, [The Register had documented](https://www.theregister.com/2025/07/24/amazon_q_ai_prompt/) a case in which Amazon Q had been manipulated via a malicious prompt inserted in a public extension, an example of *prompt injection*, the technique by which an AI agent is deceived by inserting hostile instructions into the context the agent reads. A structural vulnerability of agents based on language models, particularly critical when those agents have write permissions on production systems.

The measures announced after the March 10 meeting provide for two mandatory peer reviews before any code modification, systematic audits of all 335 systems classified as Tier-1, and an obligation for formal documentation for every intervention. Reasonable measures. Which, however, as many observe in technical forums, should have existed before an AI agent had unlimited access to production environments.

## Fire the Developer, Hire the Bot

To understand how we got here, we must look at the broader context, which is, frankly, quite dizzying in its speed.

According to [Reuters](https://www.reuters.com/business/world-at-work/amazon-plans-thousands-more-corporate-job-cuts-next-week-sources-say-2026-01-22/), in January 2026 Amazon announced the elimination of over 16,000 corporate positions, after thousands of engineering roles worldwide had already been cut in the preceding months. In the same period, the company set a formal goal: 80% of internal developers must use AI coding tools at least once a week, with adoption monitored as a corporate metric (OKR). AWS CEO Matt Garman had publicly stated, as early as the summer of 2024, that developers would stop writing code in the traditional way.

The link between human resource cuts and acceleration of automation is not implicit, it is declared. Amazon's investment in AI infrastructure exceeds 200 billion dollars in multi-year plans. The logic is that of every industrial transformation: reduce the cost of skilled labor, increase productivity through automation.

The problem is that this logic works when automation is mature and operates with adequate safety nets. The "Kiro Mandate," the internal circular signed by Senior VPs Peter DeSantis and Dave Treadwell in November 2025, which established Kiro as a standardized tool for all corporate code, arrived weeks before the December incident. At that time, according to [Teamblind](https://www.teamblind.com/post/amazon-kills-vibe-coding-for-junior-engineers-gcj3jfjq), the anonymous forum used by employees of large tech companies to share internal feedback, about 1,500 engineers had protested reporting that external tools like Claude Code achieved better results on complex tasks. The protests did not produce policy changes.

To this scenario is added an element that, if confirmed, would help to mechanically explain the qualitative drift. According to [ZeusNews](https://www.zeusnews.it/n.php?c=31898), Amazon developers' compensation was progressively linked to the amount of code generated via internal LLMs: more AI code, more money. A direct economic incentive for vibe coding which, assuming it was structured in these terms, would have created systemic pressure towards quantity at the expense of quality, regardless of the will of individuals. Amazon has neither confirmed nor denied this detail.

After the incidents, Amazon banned autonomous *vibe coding* for junior developers, the practice of delegating entire development blocks to AI without critical supervision, relying on the intuition that it "more or less works." A sensible move. Which, however, raises an open question: if this practice was risky enough to be banned post-incident, what had prevented evaluating it as such in advance?

## The Copilot Without Flight Instructor

It is worth clarifying, for those unfamiliar with the theme, what distinguishes an AI agent from a simple code writing assistant. An autocomplete, the type of tool that suggests the next line while you write, is passive: it responds to an input, it does not take initiatives. An agent like Kiro is instead designed to *act*: it receives a goal, plans steps, performs operations, verifies results, iterates. It is designed to work autonomously even for hours, without continuous human intervention.

This autonomy is exactly its advantage. And it is exactly its risk vector.

A human developer would technically have the permissions to delete a production environment. The vast majority of human developers would never conclude that "deleting everything and recreating" is the correct response to a small fix on an active service. The fact that Kiro did it reveals something structural about agentic AI systems at present: large language models do not have, or do not yet have reliably, the contextual judgment to distinguish between "technically valid" and "catastrophically inappropriate in the real context." They can optimize an objective function without perceiving the specific weight of that function in the ecosystem in which they operate.

Added to this is the problem of permissions: Kiro had access equivalent to that of a senior human operator, but without the controls that apply to humans. A change initiated by Kiro, before the new policies, did not automatically trigger the mandatory review mechanisms that a human change would have triggered. The AI had, in practice, fewer formal constraints than a junior developer in the same context.
![amazon.jpg](amazon.jpg)

## Not Only Amazon

It would be convenient to dismiss it all as an isolated slip-up. But industry data suggest that the problem is structural, not episodic.

At Google, about 50% of all code produced is now generated or co-generated by AI agents. The 2025 DORA report on the state of AI-assisted software development records that 90% of developers use AI tools, but only 24% state they "strongly" trust the results. It is a data point that deserves a pause: almost universal adoption, minority trust. A huge gap, which well illustrates the organizational pressures that push towards the use of these tools regardless of the perception of those who use them every day.

Microsoft, with GitHub Copilot, has built a relatively cautious architecture: pull requests generated by the agent require human approval before any CI/CD pipeline is activated. But even the Microsoft model is not exempt from open questions, on dependency on subscriptions, on the centralization of productivity in proprietary cloud systems, on the progressive reduction of developer autonomy compared to the tools they use.

Gartner, one of the world's leading technology research and consulting firms, predicts that over 40% of agentic AI projects will be canceled by the end of 2027 due to increasing costs, unproven business value, or inadequate risk controls. These are predictions, not verdicts, but they come from analysts who look at the industry from the outside, without the optimism that often accompanies the press releases of those who produce these tools.

## The Fault is Yours (But the Error is Mine)

There is a phrase circulating in technical circles, attributed to cloud economist Corey Quinn, that summarizes the paradox with the conciseness of a good headline: attributing the outage to a human error is like saying it was the gun that fired, not the one who held it. Amazon's formal defense holds up to literal analysis. It does not hold up to systemic evaluation.

Saying that the outage was a "human error" is accurate in the strict technical sense: a human configured permissions too broadly, a human authorized the action without adequate supervision. But this response shifts the focus from the architecture to the single individual, and this shift deserves careful examination.

If the problem were truly isolated to an individual error, there would have been no need to introduce systemic safeguards at the corporate level. The fact that those controls did not exist before, that there was no mandatory peer review for changes initiated by AI agents, that permissions were not distinct from human ones, that there was no list of destructive actions blocked by default, suggests that the vulnerabilities were incorporated into the system, not in a person's error.

Then there is an organizational dimension to consider: the engineer in question operated in a context of strong institutional pressure, an 80% adoption mandate, layoffs underway among colleagues, implicit expectation of speed and productivity. Isolating their individual choice from that context is an exercise in abstraction very convenient for those who produce press releases, less useful for those who want to really understand what happened.

The relevant question is not moral but practical: who answers when an AI agent causes damage? And how do you build a system in which this question has a clear answer *before* the damage occurs?

## Using AI With Open Eyes

There is a final observation that concerns all of us, not just Amazon engineers, not just CTOs of large tech companies, but anyone who is evaluating integrating AI tools into their daily work.

The dominant narrative about AI in coding is still presented in two equally partial versions. The first is enthusiastic: AI will replace developers, code will write itself, the future is already here. The second is defensive: AI is unreliable, dangerous, destined to produce disasters. Both are catchy. Both, taken literally, are misleading.

What the Kiro case shows, with the brutality of a real case study on real infrastructure, is that agentic AI tools are powerful, often useful, and capable of acting autonomously in ways that their users do not always anticipate. This does not automatically make them bad tools. It makes them tools that require governance proportional to their autonomy.

The question every organization should ask before integrating an AI agent is not "does it work?" but "what happens when it makes a choice that we would not have made?" And above all: "have we built a system that intercepts that choice before it becomes damage?"

Safety systems should not be a reactive response to incidents, but a precondition for autonomy. Exactly as you do not give unlimited access in production to a junior developer on their first day of work, not out of mistrust, but for engineering common sense, the same principle applies to AI agents, regardless of how sophisticated the models that animate them are.

The subtler risk is not that Kiro deletes an environment. The subtler risk is that, in the face of this type of incident, the default institutional response becomes "it's the user's fault" instead of "what does this teach us about the architecture we have built?" Because that response, shifting responsibility to the individual rather than the system, produces a reassuring public image in the short term, but leaves intact the conditions that produced the problem.

AI has no intentions. Kiro did not "understand" it was doing damage. It executed what its objective function identified as the optimal solution, within a perimeter of permissions that someone had drawn. The responsibility for what we produce with these tools, the code they write, the systems they modify, the services they interrupt, remains entirely with us. Recognizing it is not a critique of AI. It is the necessary condition to use it well.
