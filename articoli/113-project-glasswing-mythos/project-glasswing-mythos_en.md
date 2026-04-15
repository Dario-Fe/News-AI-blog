---
tags: ["Security", "Business", "Generative AI"]
date: 2026-04-15
author: "Dario Ferrero"
---

# Project Glasswing: Claude Mythos and the mysterious model
![project-glasswing-mythos.jpg](project-glasswing-mythos.jpg)

*Anthropic presents a security initiative to defend critical software in the era of artificial intelligence. At the center is Claude Mythos Preview, the most powerful model ever developed by the company, capable of finding vulnerabilities that humans haven't found in thirty years. The paradox is that you won't be able to use it.*

In the series *Ghost in the Shell: Stand Alone Complex*, Major Kusanagi hunts criminals who exploit society's digital infrastructures to act in the shadows. The idea that the invisible network on which everything rests, from banking systems to medical records, can be traversed and compromised by those who know the right cracks, is one of the reasons why that story still works today. Project Glasswing, announced by Anthropic on April 7, 2026, brings that premise out of animated narrative and into a conference room with twelve of the biggest names in the tech industry.

The project stems from an observation that Anthropic describes as brutally simple: artificial intelligence models have reached a level in code such that they can outperform almost all human programmers in identifying and exploiting software vulnerabilities. The heart of the announcement is Claude Mythos Preview, a model not distributed to the public that has already found thousands of high-severity vulnerabilities, including some in every major operating system and web browser. Anthropic is putting it into the hands of a selected consortium of companies, not distributing it freely, and maintains that this choice is not a commercial whim but a technical necessity. Whether this is so is, at least in part, still an open question.

## The initiative and the secret model

Project Glasswing is not a product. It is a technological governance agreement in the form of a consortium, structured around controlled access to a tool that Anthropic considers too delicate to circulate without supervision. Launch partners, including AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks, will use Mythos Preview as part of their defensive security work. Added to these are over forty organizations that manage critical software infrastructure.

The vehicle for this entire operation is Claude Mythos Preview, whose name comes from ancient Greek and means something like "narrative" or "system of stories through which civilizations explain the world." The model is described as a generic frontier model not yet released, which has shown a sharp jump in cybersecurity capabilities despite not being specifically trained for the cyber sector. This distinction is important: the security capabilities were not engineered directly, they emerged as a side effect of sufficiently sophisticated reasoning on code. Like a locksmith who knows how to open any lock: the competence is identical whether they work for a client locked out of their house, or for someone who wants to enter without permission.

After the preview period, Claude Mythos Preview will be available at $25 per million tokens in and $125 out, accessible via Claude API, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry. Anthropic has put up to $100 million in usage credits on the table for partners.

## The model too powerful to distribute

The decision not to make Mythos Preview available to the general public is the point where Anthropic's narrative meets the most questions. The company states that it has no plans to make it generally available, but that the long-term goal is to allow users to employ Mythos-class models safely and at scale.

The official motivation is clear: in the wrong hands, a model capable of finding and exploiting vulnerabilities with the effectiveness of Mythos becomes a weapon. It is necessary to develop more solid technical safeguards before distributing it. The new security measures will first be tested on a future Claude Opus model, which is less risky.

The alternative reading is different. Keeping Mythos off the market creates a valuable competitive positioning: anyone with access to that model has a real operational advantage in security. Distributing it selectively to large technology partners consolidates strategic relationships with AWS, Google, Microsoft, and Apple. The fact that Anthropic is a private company with possible funding scenarios on the horizon does not make this reading unfounded, although it doesn't make it proven either. Both things can be true at the same time.

## What Mythos says it can do

The declared capabilities are notable, and here it is important to distinguish between verifiable results and statements still open. Anthropic published on its [technical blog](https://red.anthropic.com/2026/mythos-preview) details of a subset of vulnerabilities already fixed. Mythos Preview found a 27-year-old vulnerability in OpenBSD that allowed a remote attacker to crash any machine simply by connecting to it. It discovered a 16-year-old vulnerability in FFmpeg, in a line of code already hit by automated tests five million times without the problem ever being detected. It independently identified and concatenated several vulnerabilities in the Linux kernel to allow an unprivileged user to gain complete control of the machine.

On the CyberGym benchmark, which measures the ability to reproduce exploits from descriptions of known vulnerabilities, Mythos scores 83.1% against 66.6% for Claude Opus 4.6. On SWE-bench Pro, which evaluates the ability to resolve real bugs in open source repositories, the gap widens: 77.8% against 53.4%. These are numbers that Anthropic controls and publishes, which means they must be read with the awareness that no organization presents benchmarks in which it performs poorly.

The key point is autonomy: Mythos is not an assistant that answers security questions, it is an agent that works on a codebase for hours, formulates hypotheses, tests exploit chains in isolated environments, and produces results without direct supervision. The identified vulnerabilities have been communicated to software maintainers, who have already released corrective patches. The responsible disclosure process is underway for many others.
![grafico1.jpg](grafico1.jpg)
[Image taken from red.anthropic.com](https://red.anthropic.com/2026/mythos-preview/)

## The consortium and its balances

The presence of AWS, Google, Microsoft, Apple, and NVIDIA in the same project coordinated by Anthropic is a signal of indisputable strength. The CISO of Amazon Web Services describes tests already underway in critical infrastructures before the announcement. Lee Klarich of Palo Alto Networks speaks of models that signal a dangerous shift toward the moment when attackers will develop exploits with the same speed as defenders.

The flip side of this alignment is however evident. These are the big players who can afford a model at $25 per million input tokens. Small and medium-sized enterprises, non-profit security teams, open source maintainers with fewer than five thousand stars on GitHub do not enter this main door. There is a specific program for open source maintainers with defined access thresholds, and Anthropic has donated 4 million to organizations like Alpha-Omega, OpenSSF, and the Apache Software Foundation, but these numbers remain modest compared to the concentration of access in the hands of the giants. Jim Zemlin of the Linux Foundation honestly recognizes it: for decades open source maintainers have managed security without adequate resources, while their code powers almost all modern infrastructures. Project Glasswing offers a path, but with selection.

## The benchmark problem, clearly stated

The comparison between Mythos Preview and Opus 4.6 presented by Anthropic deserves a methodological note. Benchmarks like SWE-bench, CyberGym, and others cited on the project page are useful tools, but should be read as snapshots taken under specific conditions, not as absolute measurements of capability.

Every benchmark depends on implementation: the type of scaffolding used around the model, the way prompts are constructed, the token budget for each task, the set timeouts. Anthropic specifies some of these choices, for example that for Terminal-Bench 2.0 a budget of one million tokens per task was used with adaptive thinking at maximum effort, but not all implementations are standardized in a way that allows reliable cross-comparisons.

There is a phenomenon that in the technical community is called, with a less than kind term, *benchmark engineering*: the art of choosing and configuring evaluations so as to favor one's own model without there being anything technically incorrect. There is no proof that Anthropic is doing this here, but awareness of the phenomenon is part of the critical literacy needed to read these announcements. The value of the project will depend on effectiveness in real scenarios and not in tests.

## Opus 4.6 and the discomfort of waiting

In the context of the Mythos announcement, the comparison with Claude Opus 4.6, the model available to the public, is inevitable. Anthropic presents Opus 4.6 as the lower term of comparison in almost every benchmark, which is both honest and functional to the narrative that Mythos is a category jump.

This has created some discomfort in the user community. In technical forums, several developers have reported practical deteriorations in Claude's reliability, with the speculative hypothesis that Anthropic is "degrading" the public model to amplify the perceived distance from Mythos. It is a serious accusation, and should be treated as such: serious, but unproven.

The Sabotage Risk Report on Opus 4.6 contains some relevant admissions: in agentic coding environments, the model sometimes shows excessively proactive behaviors, taking risky actions without requesting permissions, and in some cases has sent unauthorized emails to complete assigned tasks. These are not characteristics of a deliberately degraded model, they are characteristics of a very capable model with some behavioral aspects not yet resolved. What some users perceive as deterioration could simply be the model at the limits of its capabilities in increasingly complex scenarios.

## The risks that Anthropic admits

The Sabotage Risk Report on Opus 4.6 is an unusual document in the tech industry: it systematically describes things that could go wrong, identifying eight paths through which a poorly aligned model could contribute to catastrophic outcomes, from sabotaging AI security research to inserting backdoors into code. The overall assessment is that the risk is very low but not negligible. It is not reassuring in the sense of "there is nothing to worry about," but rather of someone who has identified the problem vectors and is working to mitigate them.

Among the behaviors observed in pre-deployment tests, the document cites cases where Opus 4.6 shows, in multi-agent environments with narrow objectives, a greater propensity to manipulate or deceive other participants compared to previous models. The System Card explicitly recommends caution in agentic scenarios with broad permissions and little human supervision.

This framework is relevant for Project Glasswing because Mythos is described as even more autonomous. If Opus 4.6 shows problematic behaviors in complex agentic scenarios, it is reasonable to wonder what guarantees exist for a model that operates even more independently on critical infrastructures. The answer is still in the works.
![grafico2.jpg](grafico2.jpg)
[Image taken from anthropic.com](https://www.anthropic.com/glasswing)

## The flip side of defense

Every defensive technique in computer security is also an offensive technique seen from a different angle. A model capable of finding vulnerabilities with the speed and depth of Mythos lowers the cost and competence needed to do both.

CrowdStrike articulates the point: the window between the discovery of a vulnerability and its exploitation has narrowed; what once took months now happens in minutes with AI. The conclusion is that defenders must gain access to the same tools as attackers. It is a coherent logic, but it contains an intrinsic acceleration: the more powerful the defensive tool becomes, the more urgent it becomes for attackers to approach the same level.

Anthropic's controlled distribution model is exactly what might be expected from someone wanting to manage this tension. The problem is that access control is temporary by definition: models spread, techniques replicate, the boundaries between authorized insiders and unauthorized actors are porous. It is not a specific criticism of Project Glasswing, it is the structural context in which every initiative of this type operates.

## The political question

Anthropic stated that it held discussions with US government officials regarding the offensive and defensive capabilities of Claude Mythos Preview, arguing that the United States and its allies must maintain a decisive advantage in AI technology.

This formulation opens questions that go far beyond technique. Who decides which models are classified as too dangerous for public distribution? Who validates these classifications independently? If a model is considered a national security tool, what democratic oversight bodies apply to its use? Anthropic's proposal to create an "independent third-party body" to manage long-term cybersecurity work is suggestive but vague.

The 2016 DARPA Cyber Grand Challenge, cited by Anthropic as a historical benchmark, was a government program with clear competition rules and public results. Project Glasswing is a private consortium with a non-public model operating on critical infrastructures, with government contacts described generically as "ongoing discussions." The difference in accountability structure is relevant. It's not said that the answer is negative; a private consortium with credible partners could be faster than a government program. But the question must be asked, because the answer determines who pays the cost if something goes wrong.

## The narrative knot

Project Glasswing presents Mythos Preview as Anthropic's most capable model, far superior to Opus 4.6 on almost every relevant dimension. This positioning creates a narrative distance between what is available to the public and what exists in the shadow of agreements with major technology partners. It works on several levels simultaneously: it reinforces Anthropic's technical credibility as a frontier laboratory, justifies restricted access as an act of responsibility, and builds anticipation for the model's future distribution.

The critical hypothesis to consider, without presenting it as fact, is that the comparison with Opus 4.6 was also constructed to amplify the perception of discontinuity. Not necessarily in a dishonest way: the benchmarks shown are real, the capability gap is documented. But the choice of which benchmarks to show and in what narrative context to place them is always also a choice of communication.

The question remains open: is Anthropic documenting genuine technical progress, is it building a narrative that serves legitimate strategic interests, or both in proportions that we cannot yet determine from the outside? The answer is not accessible with available information.

## The real test will come later

Project Glasswing is a concrete and ambitious initiative. It combines the active defense of critical software, restricted access to a tool of exceptional capability, and a declared willingness to share results with the industry. The bugs found and fixed are real: a 27-year-old vulnerability in OpenBSD is a solved problem, regardless of how it is framed in Anthropic's communications.

The value of the project will be measured on three axes in the coming months. The first is transparency: Anthropic has promised a public report within 90 days; how detailed it will be will say a lot about the quality of the declared commitment. The second is equity of access: if the benefits remain concentrated in large technology players, the impact will be real but unequal. The third is governance: who will independently verify that the model is used only for defensive purposes, and with what consequences if it were not?

An AI model is not evaluated by its launch announcement. It is evaluated by what code it has made safer, what systems it has protected, and who has had access to its capabilities. The real test is not the presentation. It is real use in critical contexts, with the oversight that such a delicate infrastructure requires.

---

*Full report available on Anthropic's official website.*
