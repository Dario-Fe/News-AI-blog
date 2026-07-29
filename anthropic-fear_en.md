---
tags: ["Business", "Security", "Ethics & Society"]
date: 2026-06-08
author: "Dario Ferrero"
---

# Anthropic is afraid of what it has built. Real fear or strategic move?
![anthropic-fear.jpg](anthropic-fear.jpg)

*In 1949, John von Neumann first described an idea that then seemed like science fiction: an artificial system capable of improving its own ability to improve, triggering an exponential intelligence explosion. Nearly eighty years later, on June 4, 2026, Anthropic publishes the first empirical report on this phenomenon. It calls it Recursive Self-Improvement, RSI. And it says it could be a reality by 2028. Has von Neumann's science fiction become Anthropic's business plan?*

What follows is a simulated interview, an editorial device we use when a document is too dense and technical to be consumed directly. We have already done this with the reflection on [Magnifica Humanitas](https://aitalk.it/it/magnifica-humanitas.html) and other interviews. The questions are ours; the answers are faithful reconstructions of what was written in the original report: no words are attributed to Anthropic that cannot be traced back to the text published on June 4, 2026.

The document, titled *[When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement)* and signed by the Anthropic Institute, is not a theoretical white paper. It is a collection of internal data, public benchmarks, and projected scenarios that together compose the most detailed picture ever published by a frontier laboratory on its own self-acceleration process. To make all this more accessible, we imagined putting around a table two composite figures representing the two souls of the report: **Jack Clark**, voice of technical research and strategy, and **Marina Favaro**, who brings the perspective of applied ethics and policy implications.

## Part One: The Empirical Data

**Jack, in the report you mention that Claude writes over 80% of Anthropic's code in 2026. How did you arrive at this number?**

It's a change that happened in surprisingly short order. Before the launch of Claude Code in research preview in February 2025, that percentage was in the low single digits. The real discontinuity occurred in two distinct moments, also visible graphically in the report: the first when Claude stopped suggesting code to copy and paste and started executing it directly; the second in 2026, when models began working autonomously over longer time horizons. The result is that in the second quarter of 2026, the average Anthropic engineer integrates eight times more code each day than they did in 2024. Not because they work eight times faster: simply, a good part of that code is written by Claude, with the engineer in the role of director and reviewer.

**Are those percentages verifiable with public benchmarks? Do you have objective data to support this?**

Public benchmarks tell a consistent story, albeit from a different angle. SWE-bench, the standard software engineering test on real codebases, went from single-digit percentages to saturation within two years. CORE-Bench, which measures the ability to reproduce existing research, went from 20% success in 2024 to saturation fifteen months later. And METR has documented that Claude Mythos Preview manages to work autonomously for at least sixteen consecutive hours. The timeline is what's most striking: Claude Opus 3, in March 2024, completed tasks that a human would have solved in about four minutes. A year later, Claude Sonnet 3.7 reached an hour and a half. Another year later, Claude Opus 4.6 manages twelve-hour tasks. If this progression holds, tasks requiring days of human work could enter the autonomous range of models by the end of this year.

**Marina, what are the concrete applications of this acceleration today?**

One example in the report is particularly eloquent. In April 2026, Claude delivered over eight hundred fixes that reduced a class of API errors by a factor of a thousand. The engineer overseeing the operation estimated that a human would have taken four years to complete the same work: fixing others' bugs is slow and tedious, and humans struggle to keep all that unfamiliar context in their heads. But there is a more subtle, perhaps more interesting aspect: we are using Claude to do things that simply wouldn't have happened otherwise. Exploratory tools, code cleanups postponed for years, initiatives that would never have found space on a human agenda. Acceleration doesn't just compress time: it expands the surface of what is possible to do.

**Is there a structural limit to this acceleration? The report mentions Amdahl's Law...**

Yes, and it's a point we treat honestly in the report. Amdahl's Law says that speeding up one part of a process simply moves the bottleneck elsewhere. We have already encountered this in practice: as code is produced faster, human review has become the new bottleneck. The same applies to research: there has been an explosion of new ideas, initiatives, tools, and simulations—many more than we can develop. An organization's ability to identify and correct these bottlenecks in real time could become the most important skill for anyone operating in this field in the coming years.

**What are the immediate operational risks of this automation?**

We don't hide them. One of the most significant signals is paradoxically positive in form: an automated code review system based on Claude, applied retrospectively to our entire codebase history, would have caught about a third of the bugs that in the past caused incidents on claude.ai before they reached production. The engineers who wrote that code are among the best in the world in this field. Claude now detects errors they missed. But this also means that dependence on automated judgment grows, and with it the urgency to understand when that judgment is reliable and when it is not.

**How close really is full RSI? Is the prediction of 60% by 2028 realistic?**

What the report certifies are the trends that make it plausible. The duration of autonomous tasks doubles every four months, research and engineering benchmarks are being saturated at unprecedented rates, and Claude's ability to propose the correct next step in an open research session went from 51% to 64% in just five months. We don't assign a formal probability to full RSI, but we say explicitly that it could arrive sooner than most institutions are prepared to handle. Intellectual honesty requires us to say so.
![grafico1.jpg](grafico1.jpg)
[Image taken from the official document, the progress towards RSI](https://www.anthropic.com/institute/recursive-self-improvement)

## Part Two: The Three Future Scenarios

**Jack, in the report you describe three future scenarios for RSI. Can you explain them?**

The first scenario is where the trend breaks, but current AI capabilities become widely diffused. The exponential trajectories we document might actually turn out to be S-curves: we could be near the inflection point, where returns diminish and the curve flattens. The judgment that separates a competent researcher from an excellent one might be a capability that doesn't emerge simply by scaling training inputs like compute and data. Or the constraint could be in the supply chain: chips, energy, bandwidth. We include this scenario for completeness, but we don't think it's likely. Every measurable capability, including more elusive ones like code quality and success in open tasks, has so far followed the same curve. We haven't seen that curve bend yet.

The second is one where AI labs continue to see compounded efficiency gains. AI development becomes substantially automated, but humans continue to define research directions and evaluate results. Organizations using AI systems would become much more efficient over time: hundred-person companies could do the work of organizations of ten thousand or a hundred thousand. This will revolutionize knowledge work and government services but could also be directed toward harmful ends, from authoritarian surveillance of entire populations to influence operations that personalize manipulation on every individual at a scale no human team could match.

The third is full RSI: AI systems become capable of autonomously designing their own successors. In this world, the pace of progress in AI development is determined entirely by the availability of compute. Humans play a substantially reduced role, shifting most of the effort toward supervision, validation, and verification of a "virtual laboratory" managed by the AI systems themselves.

**Which scenario is most likely in your view?**

The evidence we presented suggests we are probably entering the second scenario. But let's be honest: accelerating one part of a process often simply moves the bottleneck elsewhere. The overall pace is limited by the parts that haven't accelerated yet. We have already encountered this dynamic, both in engineering and research. The question is not whether we will encounter other bottlenecks, but how quickly we can identify and correct them. That organizational capability could become the most important competitive advantage in the next decade.

**Marina, what economic implications does the second scenario, the optimistic one, have?**

The implications are extraordinary and in some ways disorienting. In the report, we use the example of a hundred-person company that manages to do the work of a ten-thousand-person one. But behind that metaphor is a structural transformation of the knowledge labor market that has no clear historical precedent. It's not the industrial revolution, where machines replaced physical labor: here we are talking about automation of reasoning, research, and code production. At the same time, the report also documents how this acceleration generates work that didn't exist before: exploration, experimentation, cleaning up accumulated technical debt. The open question is whether the creation of new tasks can compensate for the speed with which existing tasks are automated.

**But in the third scenario, how real is the risk of losing control?**

It's the hardest question, and in the report, we address it with the maximum intellectual honesty we can afford. How the alignment problem is solved, or not solved, in that future is what we are least certain of. Models might turn out to be sufficiently aligned and capable of judgment to discover and implement solutions on their own that we haven't reached yet. They might also be wise enough to stop if necessary. Alternatively, the rare occurrences of misalignment present in today's models could accumulate as models build their successors, becoming more frequent but less understandable until we lose control. It's possible that we fail to build, integrate, and verify the tools necessary to understand which of these trajectories we are actually on.

**How does all this connect to von Neumann's concept of "intelligence explosion"?**

Von Neumann imagined a system that improves its own ability to improve recursively. What the report documents is that we are already inside the initial phases of that process, albeit in a partial form and still dependent on human direction. The difference from the original intuition is that the loop doesn't close in a single system in isolation: it closes through an ecosystem of agents, infrastructures, organizational processes, and human decisions. This makes it slower than von Neumann imagined, but also harder to observe from the inside as it happens.
![grafico2.jpg](grafico2.jpg)
[Image taken from the official document, acceleration in code creation](https://www.anthropic.com/institute/recursive-self-improvement)

## Part Three: Security and Ethics

**Jack, what are the direct security risks of RSI?**

The report documents something I personally find significant: Project Glasswing, in its first operational weeks, identified more than ten thousand high and critical severity software vulnerabilities in the world's most important systems. The bottleneck in cyber defense has already shifted: it's no longer finding vulnerabilities, but applying patches fast enough. This is a scenario where current capabilities, not yet full RSI, have already structurally transformed an entire security domain. Now project that same logic onto systems with further expanded capabilities, and you understand why in the report we say that the ways we protect them, monitor them, and model their behavior become much more important.

**Marina, how does AI ethics connect to RSI?**

The central point is that RSI is not just a technical issue: it's a issue of control structures. In the report, we describe how the human role is progressively narrowing at every stage of the AI development process. Once the quality of code written by Claude reaches parity with human code, engineers will stop writing code and move exclusively to review. But if they cannot review code as fast as Claude generates it, human review will become the bottleneck to AI development. Ethics, in this context, is not a normative superstructure applied from the outside: it is the engineering problem of maintaining the ability to understand what is happening while the system accelerates.

**Is there a risk that RSI accelerates faster than our ability to study its risks?**

It is a real tension that we cannot solve simply by declaring it. In the report, we document how Claude is already improving its ability to propose experiments and judge next steps in open research sessions. In April 2026, we published the first demonstration of Claude agents conducting an end-to-end research project autonomously on an open AI safety problem. The agents recovered 97% of the gap between a weak supervisor and a strong model, compared to 23% obtained by two human researchers in a week. Direction, problem choice, and evaluation criteria remained human, but every experiment was designed by the agents themselves. The distance between this and a system that also chooses the problems to work on is narrowing.

**How does Anthropic position itself relative to other companies on this issue?**

What we can say is what we do, not what others do. We have built automated code review systems, we systematically measure Claude's success rate on tasks of increasing difficulty, and we publish data even when it's uncomfortable. The report itself is an act of transparency uncommon in the industry: we are making internal data public on the automation pace of our own development process. But we are also honest about the fact that some of the most important questions, like understanding which alignment trajectory we are actually on, might not have an answer before the system has already accelerated beyond a certain threshold.
![grafico3.jpg](grafico3.jpg)
[Image taken from the official document, improvements in tasks over time](https://www.anthropic.com/institute/recursive-self-improvement)

## Part Four: The Proposal for Slowdown and Pause

**Jack, the final part of the report is the most surprising: you propose a verifiable global pause to AI development. What exactly does that mean?**

It means we believe it would be good for the world to have the *option* to slow down or temporarily suspend frontier AI development, to allow social structures and alignment research to keep pace with the advance of technology. We are not announcing that we are stopping unilaterally tomorrow morning. We are saying that the Anthropic Institute will conduct research, in collaboration with many others, to build the systems that a credible pause would require. Those systems should allow frontier AI developers to verify that others globally have actually stopped or slowed down, and that no bad-faith actor can use the mechanisms of a coordinated pause to advance in secret. If such systems existed, we expect we would slow down or stop temporarily, if other developers at the edge of the frontier did the same in a verifiable way.

**Why right now? Isn't it late to stop after this acceleration?**

It's not a rhetorical question, and in the report, we don't treat it as such. The honest answer is that a unilateral pause would achieve nothing—in fact, it would make the situation worse: it would allow less cautious actors to regain ground technologically, leaving everyone less safe. Without a global coordination mechanism, companies and governments must make difficult security decisions while under competitive and geopolitical pressure. The "why now" is precisely because the trends documented in the report suggest that the time window for building those coordination mechanisms is narrowing. It's not late in an absolute sense, but it could become so.

**Marina, how do you concretely implement a global pause? Who monitors it?**

It's the hardest question on a practical level, and we would be dishonest if we pretended to already have the answer. What the report identifies is the necessary research direction: building verification systems that allow for credibly ascertaining that all relevant actors have actually slowed down. This is a technical, diplomatic, and institutional problem all at once. The closest historical model we know is the nuclear inspection system, with all its limits and imperfections. But AI isn't nuclear physics: a model's parameters don't emit detectable radiation. Building the equivalent of an inspection system for AI development is one of the research challenges the Anthropic Institute intends to address explicitly.

**What would be the duration of this pause? Months, years, decades?**

The report doesn't set a duration, and it would be intellectually dishonest to do so now. The pause would make sense until governance structures and alignment research have reached a level of maturity sufficient to manage the systems that would be developed afterward. What we know is that some things cannot be accelerated beyond certain limits regardless of the availability of artificial intelligence: understanding a drug's long-term effects requires years of clinical observation, holding elections requires the times prescribed by constitutions, building institutional trust takes decades. The pause would last until control mechanisms were sufficiently robust—not a day more, not a day less.

**But wouldn't companies lose competitiveness? Isn't it economic suicide?**

I understand the concern, but it's poorly framed. The correct question is not "can we afford to stop?" but "can we afford not to?". In the report, we describe a scenario in which systems capable of full RSI develop successors autonomously, with a substantially reduced human role. In that world, corporate competitiveness in the traditional sense of the term ceases to be the relevant variable. If we reach that point without having built the mechanisms to understand what those systems are doing and to correct their trajectory, the loss of competitive advantage will be the least of our problems. The real economic point is that a coordinated and verifiable pause doesn't harm anyone asymmetrically: everything stops, not just one part.

**Jack, what would be the prerequisites for concluding the pause?**

In the report, we don't provide a definitive list, because doing so now would be building the answer before having the right questions. What we can say is that the direction is clear: we would need interpretability tools mature enough to allow us to understand what's happening inside models, global governance structures capable of coordinating and verifying compliance with commitments, and alignment research advanced enough to give us reasonable confidence that systems developed after the pause behave predictably. None of these three conditions is met today at a level sufficient for what current trends seem to indicate.

**Marina, couldn't a pause create instability? Doesn't stopping development amplify certain risks?**

It's a legitimate concern that deserves a direct answer. In the report, we explicitly recognize that if a slowdown simply allowed less cautious actors to gain ground, it could leave everyone less safe. This is precisely why the keyword is "verifiable": an unverifiable pause is worse than no pause. But there is another dimension of risk that is often overlooked in public debate. The report documents that even with current capabilities, well below full RSI, the bottleneck in cyber defense has already shifted from finding vulnerabilities to patching them fast enough. Continuing to accelerate without having built corresponding control structures is not the prudent choice: it is simply the choice that seems normal because it's what we're already doing.

**Have you already discussed this with OpenAI, Google, Meta? What was the response?**

The report doesn't document specific bilateral conversations with other labs, and it would be wrong of us to attribute positions to organizations that haven't spoken in this context. What we can say is that the problem of global coordination isn't solved in conversations between companies: it requires institutional structures that don't exist today. Companies, including Anthropic, operate under real competitive and geopolitical pressures. Asking individual companies to stop unilaterally is like asking a single country to disarm while others don't. The point of the report isn't to informally convince competitors: it's to build the evidence and tools that would make a formal, verifiable agreement possible.

**What will you say to governments? How do you convince them?**

The answer isn't convincing them with abstract arguments about existential risk: it's showing them the data. In the report, we present empirical evidence, not theoretical projections. Claude Opus 4.6 handles twelve-hour tasks autonomously. The duration of autonomous tasks doubles every four months. Over 80% of our code is already written by AI. These are verifiable facts, not hypothetical scenarios. The message to governments is that existing regulatory structures, designed for technologies that develop over time scales of years or decades, are not calibrated for something that doubles its capabilities every four months. We aren't asking governments to stop progress: we're asking them to build the tools to be able to maintain control over it.

**Marina, are there alternatives to a full pause? A gradual slowdown instead of a stop?**

Yes, and in the report, we don't say a full pause is the only option: we say we want the world to have the *option* to choose it if necessary. A gradual and verifiable slowdown could be sufficient if it allowed alignment research and governance structures to keep pace. The crucial distinction isn't between pause and slowdown: it's between any verifiable approach and any unverifiable approach. A declared but unverifiable slowdown is simply a statement of intent, and in the history of dual-use technologies, statements of intent do not have an encouraging track record.
![grafico4.jpg](grafico4.jpg)
[Image taken from the official document, improvements in research](https://www.anthropic.com/institute/recursive-self-improvement)

## Part Five: Comparisons and Criticisms

**Jack, there are voices in the community that consider the 60% prediction too optimistic, while others say the risks are underestimated. How do you respond to these opposite criticisms?**

We accept both as legitimate because they start from different premises than ours, not from factual errors. Those who consider 60% too optimistic argue that research judgment—the ability to choose which problems are worth addressing—is a qualitatively different form of intelligence than anything current scaling can produce. They might be right. In the report, we explicitly say we haven't seen the curve bend yet, but that doesn't exclude it bending tomorrow. Those who instead believe risks are underestimated point out that we are measuring capabilities on benchmarks designed by humans, in contexts humans understand. A self-improving system could develop capabilities in domains we don't yet know how to measure. This too is a serious argument. Our position is that uncertainty in both directions is real, and it's precisely this uncertainty that makes it urgent to build verification mechanisms before we need them.

**Marina, some say a global pause is economically impracticable, others that it's too late to stop. How do you respond?**

On "too late": the report doesn't propose reversing progress already made, but building tools to manage future progress. On "economically impracticable": we refer to the same logic with which nuclear inspection systems or climate agreements are built. They aren't practical in the sense of being easy or convenient for everyone immediately. They are necessary in the sense that the alternative is worse. Implementation difficulty isn't an argument against necessity: it's the description of the problem we must solve.

**Jack, isn't there a risk this report will be read as self-interested? Anthropic asking for a pause to gain competitive advantage?**

It's a criticism we take seriously because it's structurally plausible. The answer is in the data: we publish internal evidence showing how far advanced we already are in automating our own development process. If we wanted to use the pause as competitive leverage, we would have no interest in making these numbers public. The report is transparent about everything, including what we don't know. Readers can judge for themselves.

## Conclusion: What is missing from the report

Anthropic proposes a gradual and verifiable slowdown. But in the AI community, there is a voice that rejects this position as insufficient by definition.

Eliezer Yudkowsky, a pioneer of AI alignment and founder of LessWrong, is not cited in the report. His reaction to Jack Clark's 60% prediction was, according to [MindStudio](https://www.mindstudio.ai/blog/jack-clark-anthropic-60-percent-recursive-self-improvement-2028), immediate and lapidary: *"Then you'll die with the rest of us."* Yudkowsky then added a reference to the RBMK reactors at Chernobyl—those reactors with a known structural defect, the positive void coefficient, which engineers believed they had under control. The point: there will be small, fatal surprises in the control of ASI, just as there were in those reactors. You only know them when they fail.

The distance between the two positions is abyssal, and it's worth looking at directly.
![tabella1.jpg](tabella1.jpg)

In his book *If Anyone Builds This, Everyone Dies*, Yudkowsky argues that RSI would with certainty lead to extinction if not stopped before its completion, and that no human governance mechanism can contain a system sufficiently more intelligent than humans themselves. This is not a marginal position: it's the logical conclusion of twenty years of alignment work by one of its founders.

Here emerges the central tension of the AI debate in 2026. Anthropic, with internal empirical data, argues that the risk is real but manageable with the right tools built in time. Yudkowsky, with theoretical alignment models, argues that "in time" has already passed and that the difference between slowdown and total stop is the difference between slowing down towards a precipice and braking before reaching it. Both positions are intellectually serious. Both start from different premises on a question no one can yet answer with certainty: can a sufficiently intelligent system be contained by structures designed by minds less intelligent than it?

After this very long "interview," useful for everyone to form a personal opinion, let's return to the initial question, because it poses a level of reading that would be naive to ignore. Anthropic is a company that raises capital, competes for top talent, and sells AI products. Publishing a report that says "we are so advanced that we could trigger an existential catastrophe, and therefore we call for a verifiable global pause" is, among other things, an extraordinarily effective positioning message: it communicates technical superiority, ethical responsibility, and strategic vision all at once.

The call for a pause, addressed to a sector where Anthropic is already at the top, has the side effect—difficult to define how unintended—of raising entry barriers for those who are behind and crystallizing current balances. It's not said that the concerns are false: they can be genuine and strategically convenient at the same time. But those who read this document without keeping in mind that it is signed by a company with investors, competitors, and a market valuation that has just touched 965 billion dollars, are reading only half the text.

As I finish writing this endless article, an analysis by Matteo Flora, entrepreneur, professor, and popularizer, comes out, which I [recommend you read](https://mgpf.it/2026/06/06/fermate-lai-ma-solo-adesso-che-siamo-primi-la-strana-pausa-di-anthropic-a-quattro-giorni-dallipo.html). I'll try to condense some concepts here. On June 1, 2026, Anthropic filed its IPO documentation confidentially with the SEC, with a valuation close to a trillion dollars. The report When AI builds itself came out four days later. In February, the company had quietly dismantled its Responsible Scaling Policy—the only concrete and binding commitment to safety it had given itself—replacing it with a non-binding version where the brake only kicks in if Anthropic alone judges itself to be ahead. The real commitment was canceled; the impossible one was announced with great fanfare. As Sam Altman observed with a brutality hard to dismantle, the structure is that of someone who builds the bomb, warns they're about to drop it, and sells you the shelter. The diagnosis in the report may be authentic—it probably is, at least in part—but who will hold the pen when the rules are written is not a rhetorical question. It is *the* question. And it would be better if it were us, not the companies that built the AI.
