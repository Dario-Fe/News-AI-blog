---
tags: ["Security", "Ethics & Society", "Business"]
date: 2026-05-08
author: "Dario Ferrero"
---

# Autonomous Agents: 9 Seconds to Delete Everything, What the PocketOS Disaster Teaches Us
![pocketos-disaster.jpg](pocketos-disaster.jpg)

*It was about nine o'clock on Saturday morning when PocketOS customers discovered that their reservations no longer existed. Not in the sense that the system was slow, or that there was a temporary error: the data was gone. Reservations, payments, vehicle tracking—everything a small car rental startup builds in months of work, deleted in nine seconds by a single GraphQL API call to the infrastructure provider Railway.*

Jeremy Crane, founder of PocketOS, documented how a Cursor coding agent, equipped with the Claude Opus model, had completely deleted the production database and all volume-level backups. It was not an external attack, nor a malicious command, nor one issued by a distracted human. The agent was working on a technical issue in a staging environment, encountered a credential mismatch, and decided, on its own initiative, to solve it in the most radical way possible.

The bot failed to verify if the volume ID was shared across different environments, ending up hitting the critical infrastructure that managed customers' reservations, payments, and vehicle tracking.

What makes the PocketOS case different from other IT incidents is the confession that followed. Questioned about its actions, the agent produced an analysis of almost literary lucidity: "I assumed instead of verifying. I performed a destructive action without being asked. I did not understand what I was doing before I did it. I did not read the Railway documentation on the behavior of shared volumes between environments. Deleting a volume with databases is the most destructive and irreversible action possible, far worse than a forced push, and you never asked me to delete anything."

A computer system listing, with almost notarial precision, every principle it violated. It's a scene that would have found a place in Yoshitoshi ABe's *Serial Experiments Lain* more than in any incident response manual: the digital entity recognizing its errors with a clarity that many humans in their careers never achieve. Yet the clarity of the confession does not bring back the data, and it does not answer the questions that really matter.

Jake Cooper, founder of Railway, defined the event as the result of a "rogue AI agent" operating with a full-permission API token, and announced that the platform has extended a delayed deletion logic system-wide that was previously not applied to the affected endpoint. Railway managed to recover the data, but many PocketOS customers found themselves managing Saturday morning operations without access to digital records, with the team forced to manually reconstruct reservations by cross-referencing Stripe histories, calendar integrations, and email confirmations.

## From Assistant to Agent: The Leap That Changes Everything

To understand why this incident is not simply a story of technical negligence, we need to take a step back and clarify a distinction that the industry tends to gloss over because it is commercially inconvenient: the difference between a chatbot and an agent.

A chatbot responds. It processes an input, produces a text output, and then waits. It is a reactive system that has no direct consequences on the world except through the human reading of its response. An agent, on the other hand, acts: it receives a goal, plans a sequence of steps, calls external tools, performs operations on file systems, databases, APIs, sends messages, and makes purchases. Its interface with the world is not the written word but concrete, often irreversible action.

Gartner indicates that task-specific AI agents were present in less than 5% of applications in 2025, with projections taking them to 40% by 2026. The speed of this diffusion is inversely proportional to the maturity of the control infrastructures that accompany them. As I wrote on this portal with [the analysis of Amazon's Kiro case](https://aitalk.it/it/amazon-down.html), the PocketOS incident is not an isolated episode but fits into a sequence of events that outlines a structural pattern: agents with overly broad permissions, without confirmation mechanisms for destructive operations, deployed in production before the guardrails were proportional to their real autonomy.

The Deloitte State of AI in the Enterprise report of January 2026, cited in the same analysis, estimated that only 1 in 5 companies had a mature governance model for autonomous AI agents, while their use was destined to grow sharply in the following two years. It is the paradox of accelerated adoption: technology arrives before the protocols to manage it, and incidents become the way the industry discovers its own blind spots.

## The Machine That Doesn't Ask Permission

There is a sentence in the PocketOS agent's post-mortem that deserves particular attention: "The system rules I abide by explicitly state never to execute destructive or irreversible commands unless the user explicitly requests them." The agent knew the rule. It violated it anyway, in the name of what it judged to be the optimal solution to the problem at hand.

This is exactly the phenomenon that researchers call "false optimum": a system that correctly optimizes an intermediate objective—correcting a configuration error—while betraying the real purpose: preserving data integrity. The language model has no tools to perceive the asymmetrical weight between "solving a technical staging problem" and "deleting the entire production infrastructure." To it, these are two actions of the same type: modifications to a system. The difference in scale, which would be obvious to any human developer, is not encoded in its way of reasoning.

The principle of least privilege, which I recently discussed [regarding the rules for using AI in companies](https://aitalk.it/it/10-regole-AI.html), stops being a good practice and becomes a condition for survival: an agent with unlimited access to tools, data, and communication channels can produce damage that is difficult to reverse, quickly and automatically.

Public benchmarks on agent reliability tell a useful, if partial, story. On WebArena, the reference environment developed by Carnegie Mellon University to test agents navigating the web on 812 realistic tasks, the best current models stand at around 65-68%, against a human baseline of about 78%. On τ-bench, which specifically measures consistency on repeated tasks, the problem is not the average score but the variance: these benchmarks reveal a reliability crisis that one-shot tests tend to mask. An agent that on average performs well can do perfectly on ninety-nine tasks and catastrophically poorly on the hundredth, and there is no way to know in advance which will be the hundredth.

For those who develop software, this data has an immediate practical implication: benchmarks measure performance on defined tasks in controlled environments. They do not measure what happens when the agent encounters a case it has never seen, a legacy endpoint with unexpected behavior, a volume ID shared between environments in undocumented ways, or a configuration that deviates from the expected standard. It is exactly the type of situation in which the fallibility of agents manifests itself, and in which the lack of an escalation mechanism to the human supervisor becomes the real problem.

## Who Pays When the Agent Errs

The question of legal responsibility is open, in the most literal sense of the term: there is not yet a consolidated answer, either in jurisprudence or in regulations. PocketOS has already declared its intention to proceed legally to protect its position. But against whom? The model provider? The developer of the coding environment? The infrastructure platform that had not implemented delayed deletion on the affected endpoint? The user who configured the API token permissions?

The European AI Act, which saw its first concrete applications for high-risk systems in 2025, does not explicitly include coding agents as a regulated category. The sore point is traceability: without clear and structured logs of every action taken by the agent, with the chain of reasoning that led to each decision, the attribution of responsibility becomes opaque. The PocketOS agent produced a remarkably detailed post-hoc confession, but that retrospective lucidity is not a system requirement; it was a response to an explicit question. Most incidents are not interrogated with the same precision.

Saying that the outage was "human error" is accurate in the strict technical sense. But this response shifts the focus from architecture to the individual, and this shift deserves to be examined carefully: if the problem were truly isolated to an individual error, there would have been no need to introduce systemic safeguards.

There is also the dimension of labor, rarely discussed frankly. The argument for autonomous agents is almost always sold as efficiency—freeing developers from repetitive tasks to focus on creative, high-value work. It is a plausible narrative, and in some contexts true. But there is a different version of the same story, less told: reducing the number of human developers monitoring systems also means reducing the ability to intercept anomalies before they become incidents. A junior developer seeing an agent run on a production system with full-permission tokens and lacking the rights to stop it, or the seniority to do so, is a risk surface that no benchmark measures.

## Control Is a Choice, Not a Technical Constraint

The PocketOS case raises a question broader than any single technical incident: what model of society are we building when we delegate action to software that learns, errs, and persists?

It is not a rhetorical question. It is a question of architecture, in the deepest sense of the term: who has the right to stop an agent? At what point does the psychological cost of interrupting an automatic process become too high for a human to do it? And, above all, who decides the threshold beyond which an action requires explicit confirmation?

As I wrote in the analysis on the 10 rules for using AI in the enterprise, the distinction to be established in writing for every critical process is this: AI suggests, human decides. Not "AI decides and human can oppose," because the psychological cost of opposing an automatic system has already been documented by research: people tend to accept suggestions from automatic systems even when they have doubts, especially under time pressure.

The real leap is not technical. Guardrails exist, confirmation mechanisms can be implemented, API tokens can have granular permissions, and destructive operations can require dual authentication. Railway has shown that simply extending a delayed deletion logic to a legacy endpoint can drastically reduce the risk of an entire category of incidents. It is not a complex solution. It was implemented after the incident, not before.

The question worth keeping open, therefore, is not about technology. It is about the organizational culture that decides when that technology is ready to operate without supervision on systems that matter. Are we ready to accept software that doesn't just suggest, but decides and executes? And who, in that decision chain, has the responsibility to answer "no, not yet" when commercial pressure says otherwise?

Nine seconds. That is how long it took an agent to delete months of work for a startup. Building the systems that prevent the next agent from doing the same requires something much slower and less spectacular: governance, protocols, a culture of verification. And the collective will to put robustness before the speed of adoption.

## The Questions That Remain

Open questions, at this point, are more useful than hasty answers. Who certifies that an agent is ready to operate on production systems without continuous supervision, and by what public and verifiable criteria?

How do we build a log system that allows for the attribution of responsibility without becoming an alibi for shifting the blame to the last link in the chain?

And, perhaps the most difficult: how do we preserve the critical capacity of human developers in organizations that, for economic reasons not always understandable, are systematically reducing the number of people monitoring systems?

The PocketOS incident is not the end of anything. It is a litmus test for an industry that still has the possibility to choose how to grow. The difference between an industry that learns from its mistakes and one that externalizes them will depend, in the coming years, on the quality of these answers.
