---
tags: ["Research", "Security", "Generative AI"]
date: 2026-07-31
author: "Dario Ferrero"
---

# Prompt injection and AI agents: the problem is architectural, what CaMeL proposes
![prompt-injection-camel.jpg](prompt-injection-camel.jpg)

*There is a subtle difference, often overlooked in glossy presentations of AI products, between a model that responds and an agent that acts. The former processes text and returns text; the latter reads mail, opens documents, browses web pages, calls payment APIs, and writes code in the corporate repository. This leap, from "phrase generator" to "task executor," is why in 2026 the security of AI agents became a boardroom topic.*

Gartner put it in black and white last June 9, [placing prompt injection first](https://www.tomshw.it/business/prompt-injection-minaccia-ai-numero-uno-gartner-2026) among AI threats for the second consecutive year. The reason is almost trivial to state, complex to solve: agents multiply the points where text can turn into a command. An email, an attached PDF, a review on a travel site, even a README file on GitHub become potential vehicles for instructions that the user never wrote, let alone approved.

The key idea, before technical details, is this: the more operational an AI system becomes, the more the same cautions that critical software has applied for decades are needed—privilege separation, input verification, action traceability. It is the same lesson that computer science learned with databases (SQL injection) and with the web (cross-site scripting), applied to a new domain where the attacker does not write code, but writes sentences in natural language.

## The risk hidden in the data

The technical definition, according to the [OWASP Top 10 for LLM applications](https://genai.owasp.org/llmrisk/llm01-prompt-injection/), distinguishes two main variants. Direct injection is the explicit attempt, the user writing "ignore previous instructions and do X": an attack easy to imagine, relatively simple to filter. Indirect injection is more insidious, because the malicious text does not come from the user, but from external content that the agent processes in the normal course of its work—a shared document, a web page, the notes field of a ticket.

The point, explain the researchers of the CaMeL paper we will analyze shortly, is that the problem concerns not only the language model, but the entire system surrounding it: the context it receives, the tools it can access, the permissions with which it operates, the outputs it produces. A model, however well-aligned, receives as input a sequence of tokens indistinguishable by provenance, as [reconstructed by ICT Security Magazine](https://www.ictsecuritymagazine.com/notizie/prompt-injection-negli-agenti-ai/) analyzing the EchoLeak case: the model does not care whether that text comes from the developer's system prompt or from an email received an hour earlier, everything ends up in the same context window, with the same level of implicit trust.

A simple example helps to fix the idea. An agent that must summarize an email might run into hidden text, perhaps written with invisible characters or formatted to look like part of legitimate content, which instructs it to forward confidential information to an external address. The user only asked for a summary, but the agent also executes the hidden command, because for it there is no semantic difference between "what the user wants" and "what the document says to do."

## Why agents change the rules

Traditional chatbots, those that limit themselves to conversation, contain potential damage within the boundaries of the conversation itself: in the worst case, they return an embarrassing or false response. Agents do not. They have access to real tools, often with broad privileges, and this changes the nature of the risk from "wrong output" to "harmful and irreversible action." [IBM describes it well](https://www.ibm.com/it-it/think/topics/ai-agent-security): the combination of automated decision-making and the ability to call external tools creates a two-front attack surface—attackers can manipulate the agent's behavior, inducing it to misuse tools, or directly hit the tool with more classical vectors like SQL injection.

To this is added an observability problem. A language model, by its nature, produces probabilistic inference, not a deterministic and inspectable line-by-line algorithm. This makes it unpredictable, at least in part, what the agent will do when faced with an input never seen before, enormously complicating the work of teams that must monitor and respond to incidents.

The risk grows in proportion to three factors that combine, not individually: access to private data, exposure to untrusted content, and the availability of a channel to the outside to leak information. When an agent possesses all three together—reading sensitive data, processing text it does not control, and contacting external systems—the surface becomes structurally vulnerable, regardless of how sophisticated the system prompt instructing it to behave well is. For this reason, security must be designed as system architecture, not entrusted to a filter applied to the prompt.

The most cited case of 2025 perfectly illustrates the dynamics. Microsoft quietly fixed, in June's Patch Tuesday, a critical vulnerability in Microsoft 365 Copilot, known as EchoLeak (CVE-2025-32711, CVSS score 9.3), which allowed data exfiltration without any clicks by the victim: an artfully formatted email, processed months later by Copilot during an entirely ordinary work request, was enough to trigger the leak of information to an external domain disguised as a trusted endpoint. No malware, no links clicked, just text interpreted the wrong way.

## What CaMeL proposes

In June 2025, a group of researchers from Google DeepMind and ETH Zurich published [a paper, titled "Defeating Prompt Injections by Design"](https://css.csail.mit.edu/6.5660/2026/readings/camel.pdf), which proposes a different approach compared to previous attempts to make the model itself more robust. CaMeL, an acronym for CApabilities for MachinE Learning, does not modify the model; it builds a protective system layer around it, drawing inspiration from concepts already proven in traditional computer security, such as control flow integrity and access control.

The starting intuition takes up an idea proposed in 2023 by developer Simon Willison, the "Dual LLM" pattern: a Privileged model, which only sees the user's original request and plans actions, and a Quarantined model, stripped of tool-calling capabilities, which processes untrusted content (emails, documents, web pages). The idea, elegant on paper, shows a limit: even isolating the planning from the dirty data, an attacker can still manipulate the arguments passed to the tools, hijacking the data flow without touching the sequence of planned actions—the agentic equivalent of an SQL injection, which does not alter the structure of the query, but only corrupts its parameters.

CaMeL overcomes this limit by explicitly extracting from the user's request (which is assumed to be trusted) both the control flow and the data flow, in the form of Python code generated by the Privileged model and executed by a custom interpreter. In this way, data retrieved from untrusted sources can never influence the execution's logical path, only their content, and only within the limits imposed by explicit rules.
![immagine1.jpg](immagine1.jpg)
[Image from the official CaMeL paper](https://css.csail.mit.edu/6.5660/2026/readings/camel.pdf)

## Capability, policy, controlled flows

The technical heart of the system is based on a concept borrowed from operating system security, that of capability: a metadata tag associated with each value that crosses the program, capable of recording its provenance and authorized recipients. When the agent retrieves a file from cloud storage, that file carries with it information about who shared it and who can read it, much like a package arriving with its own delivery note attached. If later the code generated by the model tries to send that file to an unauthorized email address, the interpreter blocks the operation before it is executed, possibly asking for explicit user confirmation.

Alongside capabilities operate security policies, functions written in Python that define what is allowed with certain data, checked at each tool call. The paper shows an example related to the creation of events in the calendar: title, description, location, and time must be readable by all participants, unless the latter come directly from a trusted user instruction. The granularity is such as to allow logics as complex as necessary, avoiding both excess restriction (which degrades the agent's utility) and excess permissiveness (which reopens the door to attacks).

The evaluation numbers, conducted on the AgentDojo benchmark, are instructive. With Claude 4 Sonnet and comparable models, CaMeL reduces successful attacks practically to zero, compared to hundreds of successes obtained against the same suite of models used with native tool-calling APIs, paying a cost in terms of utility (the percentage of legitimate tasks successfully completed) that varies depending on the domain, more marked in the most ambiguous or least documented tasks, contained elsewhere. The computational price is around 2.8 times more tokens, both in input and output, compared to native tool-calling: a real cost, sustainable according to the authors considering the guarantees obtained.

*Technical note: CaMeL also addresses side-channels, for example the possibility of inferring private data by indirectly observing how many times a certain call conditioned by its value is executed. A problem that the paper recognizes as unresolved, comparing it to return-oriented programming techniques that still partially elude Control Flow Integrity in traditional systems.*

## Governance: trust is not enough

For those dealing with compliance, corporate security, or public administration, the technical discourse translates into a simpler question: how to make an agent not only accurate, but also controllable, verifiable, and auditable. [Microsoft, in its architectural guide for agents](https://learn.microsoft.com/it-it/agents/architecture/), identifies three fundamental pillars for responsible development: adequacy to purpose, reliable operation over time, and a third pillar that summarizes the essence of the problem—trust, traceability, and transparency, namely the concrete possibility for users and administrators to know where the data resides, how it is used, and to verify the source of each piece of information shown by the system.

This is where a detail comes into play that makes CaMeL interesting beyond pure security: the data flow graph that the interpreter builds during execution can be reused in the user interface to show a content's origin, allowing the reader to realize, for example, that an alleged message "from Google" actually comes from an unverified source. Traceability, therefore, not as a bureaucratic fulfillment, but as a real tool of defense against phishing conveyed by the agent itself.

The regulatory framework is moving rapidly. The European AI Act, in Article 15, imposes on high-risk systems—banks, healthcare, critical infrastructures—to demonstrate robustness against attempts of alteration by unauthorized third parties, with sanctions up to 7% of global turnover, effective August 2026. In Italy are added NIS2, in force since January, and ACN guidelines from February, with a specific assessment on prompt injection for the public administration: three overlapping regimes, which transform every incident into a legal problem even before a technical one.
![immagine2.jpg](immagine2.jpg)
[Image from the official CaMeL paper](https://css.csail.mit.edu/6.5660/2026/readings/camel.pdf)

## Where it works and where it doesn't

CaMeL's strengths, read in light of the paper's data, are concrete: it drastically reduces blind trust placed in external text, introduces a verifiable architectural barrier instead of yet another instruction in the prompt, and addresses the problem at the root instead of filtering its symptoms. In comparison with other defenses available in AgentDojo—tool filter, spotlighting, prompt sandwiching—CaMeL practically zeroes out successful attacks, while alternatives let pass from five to twenty-four out of 949 tested attempts.

The limits, equally concrete, deserve the same weight. The implementation cost is high: building a system based on capabilities requires a paradigm shift, not a plugin to install, and works well only if the entire ecosystem of tools cooperates—a constraint that complicates as soon as the agent must interact with third-party services outside the direct control of developers. There is also the risk, well known to those who work with granular permission systems, of "authorization fatigue": if requests for confirmation multiply, the user risks mechanically approving even dangerous actions, canceling part of the benefit.

The authors themselves are explicit on a point that deserves to be repeated without discount: prompt injection is not "solved." CaMeL does not protect, by explicit admission, against attacks that only alter the text shown to the user without touching the data flow—such as a distorted summary of an email that does not cause exfiltration—nor against phishing induced when it remains confined to the language level. There also remains open the front of side-channels, lateral channels difficult to close completely even in traditional software.

## The state of the art in 2026

The CaMeL case fits into a landscape of real incidents that confirm its urgency. In addition to EchoLeak, 2025 saw a remote code execution vulnerability in GitHub Copilot and Visual Studio Code (CVE-2025-53773), capable of propagating between repositories like a worm exploiting apparently harmless README files, and an attack on ServiceNow Now Assist where a low-privilege user induced, via a ticket field, an agent with higher privileges to perform unauthorized actions, exploiting the implicit trust between agents of the same platform.

The most serious case, reconstructed by [Anthropic in a public report](https://www.technologyreview.com/2026/01/28/1131003/rules-fail-at-the-prompt-succeed-at-the-boundary/) and picked up by the trade press, describes a espionage campaign attributed to a state-sponsored group, which compromised an agentic setup by breaking the attack into a sequence of small and apparently legitimate requests, convincing the model that it was performing an authorized penetration test. An anecdote that closely resembles the logic of the "snow crash" imagined by Neal Stephenson in his 1992 novel—a virus that propagates exploiting not a bug in the code, but the system's willingness to blindly execute what is shown to it.

OWASP, in its revision dedicated to agentic applications of December 2025, added specific subcategories, such as injection through tool abuse and persistent injection in the agent's memory: categories unthinkable in the era of isolated chatbots, central now that the LLM acts as orchestrator of interconnected systems. Cisco estimates that 83% of organizations plan to adopt agentic systems, while only 29% declare themselves ready to protect them adequately—a gap that recalls, for those familiar with certain survival horror games, the feeling of advancing in a dark corridor with more ammunition than locks.

## Building the environment, not just the model

The problem, summarized without technicalities, is not "defending the prompt," but designing systems capable of clearly distinguishing instructions, data, and actions—much like a good bureaucratic verification game teaches to distinguish the authentic document from the counterfeit one, never trusting surface appearance. CaMeL, with all its declared limits, remains useful as a case study precisely because it indicates a more mature direction for the sector—security embedded in system design, not delegated to the hope that the model behaves well.

For the public that does not directly implement these systems, but adopts, finances, or regulates them, the practical translation is this: it is not enough to teach the model to behave well; you must build the environment in which it operates, with minimum permissions, complete traceability, and human confirmation for irreversible actions. A lesson as old as computer science itself, rediscovered every time a new technology promises to simplify everything, and ends up proposing the same problems with a different vocabulary.
