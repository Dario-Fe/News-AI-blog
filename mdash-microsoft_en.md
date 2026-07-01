---
tags: ["Security", "Applications", "Generative AI"]
date: 2026-05-22
author: "Dario Ferrero"
---

# MDASH: Microsoft's System Challenging Mythos on Cybersecurity
![mdash-microsoft.jpg](mdash-microsoft.jpg)

*There was a vulnerability in the Windows TCP/IP kernel waiting to be found. Technically, it's called use-after-free: an operating system component continued to use a pointer in a memory area that had already been freed, like someone who continues to turn a door handle after the lock has been dismantled. On systems with multiple processors, that moment of inattention can become a window through which a remote attacker, without credentials and without needing to authenticate, could take control of the machine. The vulnerability was not in the obscurity of a secondary driver: it was in tcpip.sys, the component that has managed the network traffic of every Windows installation for nearly three decades.*

On May 12, 2026, Microsoft released the Patch Tuesday that corrected this and fifteen other similar vulnerabilities, four of which were classified as Critical for their ability to allow remote execution of arbitrary code. They had not been found by a human researcher. They had been found by MDASH, an artificial intelligence system assembled by Microsoft's internal team called Autonomous Code Security, abbreviated as ACS.

The announcement is [published on the official Microsoft Security blog](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/) signed by Taesoo Kim, Vice President of Agentic Security—the same researcher who led Team Atlanta, the group that in 2024 won the DARPA AI Cyber Challenge, taking home $29.5 million by building an autonomous system capable of finding and correcting real bugs in complex open-source projects. That competition was a sort of Grand Prix for autonomous security: teams built systems that competed without human supervision on code never seen before. Team Atlanta won. Then Microsoft acquired the team.

The four critical vulnerabilities deserve separate attention because they illustrate exactly the type of problem that resists traditional tools. CVE-2026-33827 lives in tcpip.sys and concerns the incorrect management of the lifecycle of a Path object during the processing of IPv4 packets with the Strict Source and Record Route option. The code releases a reference to the object and then uses it again: in a multiprocessor system, between those two moments, another thread may have already freed the memory. The result is a race condition that a remote attacker can exploit by sending specially crafted IPv4 packets without any authentication. CVE-2026-33824, instead, resides in ikeext.dll, the component that manages the IKEv2 protocol for VPN connections: a double-free memory error caused by just two UDP packets, no timing race necessary, executing in the LocalSystem context—the highest privilege level of the operating system. On any machine configured as an IKEv2 responder—corporate VPN infrastructures, DirectAccess, Always-On VPN—the two packets are enough.

The other twelve vulnerabilities cover dnsapi.dll, netlogon.dll, http.sys, and telnet.exe: denial of service, privilege escalation, information disclosure. The perimeter is the Windows networking stack. The question worth asking is not only "how did it find them?" but "why had no one found them before?"

## The Orchestra Instead of the Soloist

MDASH is an acronym that Microsoft has carefully constructed: **M**ulti-mo**D**el **A**gentic **S**canning **H**arness. An "harness" is the assembly that holds the pieces of a complex system together; the term comes from the automotive industry, where it refers to the wiring bundle that carries power and signals throughout the vehicle. The choice is not accidental: Microsoft wants to communicate that the value is not in any single component, but in the architecture that connects them.

The official blog says it explicitly, with a formulation worth quoting in substance: *"the model is one input, the system is the product."* MDASH is not an artificial intelligence model. It is a system that coordinates over one hundred specialized agents distributed across a set of different models—some large for heavy reasoning, some distilled for high-volume steps, and a second frontier model as an independent counter-check.

The workflow is divided into five phases. In the Prepare phase, the system ingests the source code, builds semantic indexes, and maps the attack surface by analyzing the commit history. In the Scan phase, agents specialized in the role of "auditors" traverse candidate code paths, formulating hypotheses and collecting evidence. In the Validate phase, a second group of agents, the "debaters," argue against every finding: they try to dismantle it, to demonstrate that the path is not reachable or that the necessary conditions cannot occur simultaneously. The Dedup phase collapses semantic duplicates. Finally, the Prove phase builds and executes real trigger inputs: if the system claims a bug exists, it must also prove it by generating the input that manifests it in a controlled environment.

The architecturally most interesting aspect is the disagreement mechanism. When an auditor agent flags something as suspicious and the debater fails to refute it, the credibility of the finding increases. The contrast between models becomes a diagnostic signal: if a frontier system and a distilled one agree on a vulnerability after a debate cycle, the probability of a false positive drops drastically. It is a mechanism that recalls scientific peer review more than classic static scanners, and it is exactly the type of architecture that no single model, however sophisticated, can replicate alone.

The system also includes a plugin mechanism that allows specialized teams to inject context that foundational models cannot deduce autonomously: Windows kernel calling conventions, lock invariants, IPC trust boundaries. The specific plugin for CLFS, the Common Log File System, knows how to build a trigger log file given a candidate finding: it knows the container layout on disk, the block validation sequence, and the in-memory state machine. This modular approach allowed MDASH to reach 96% recall on historical MSRC cases in clfs.sys and 100% in tcpip.sys over five years of confirmed vulnerabilities.

For CVE-2026-33827, the bug was invisible to local analysis: the lifecycle violation of the Path object is not contained within a single function but distributed across non-trivial control flow, alternative branches, and early exit conditions. No traditional tool sees the link between the reference release and the subsequent pointer reuse. For CVE-2026-33824, the situation was even more complex: the bug aliasing that leads to double-free memory spans six different source files, and the strongest proof of its existence is an identical pattern correctly implemented in one of the six files—the deviation from the correct case is visible only to someone who knows both implementations. MDASH found it because its auditor agents are built to search for exactly these comparative inconsistencies between different files.

## The Numbers: What the Benchmark Says, and Who Counted Them

The quantitative strength of the Microsoft announcement is the score on the CyberGym benchmark: 88.45%, first place in the public ranking at the time of publication, about five points above the runner-up. The benchmark is developed by UC Berkeley and includes 1,507 real tasks extracted from 188 OSS-Fuzz projects—autonomous execution of exploits on documented vulnerabilities. It is not a synthetic test: the tasks come from real vulnerabilities in real open-source projects, and the metric measures how many exploit reproductions the system can complete autonomously.

The runner-up at the time of the announcement was Anthropic's Mythos, at 83.1%. Third was OpenAI's GPT-5.5, at about 81.8%.

Here a distinction is necessary that the Microsoft announcement does not explicitly make, but which is methodologically relevant. CyberGym is a public and independent benchmark: anyone can submit their results, the methodology is verifiable, and comparison with other systems is generally fair—at least to the extent that benchmarks of this type can be. The numbers on the CyberGym leaderboard therefore have a degree of credibility that other data in the announcement cannot claim.

Internal tests, on the other hand, are all self-produced. The test on StorageDrive, a private driver with 21 planted vulnerabilities, was not validated by third parties. The 96% recall on clfs.sys and 100% on tcpip.sys is based on Microsoft's internal MSRC cases on proprietary code that no external evaluator can independently examine. The sixteen Patch Tuesday vulnerabilities are real and correct, which is the most concrete validation possible—the bugs really existed—but it does not answer the question of how many similar bugs the system missed, nor how many false positives it produced in analysis cycles that did not end up in a press release.

Microsoft itself is honest about some limitations: the analysis of failures in the remaining 12% of CyberGym reveals that 82% of errors come from tasks with vague descriptions lacking function or file identifiers, and that some cases fail due to format mismatch between system-generated inputs and expected fuzzing harnesses. It is not an infallible system. But the overall picture emerging from the announcement is built with the selection typical of any corporate communication: showing the best numbers and contextualizing limits without emphasizing them.

The CyberGym benchmark is the number to keep. The others should be read knowing where they come from.
![grafico1.jpg](grafico1.jpg)
[Image taken from microsoft.com](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/)

## Mythos versus MDASH: Two Philosophies Compared

Anyone who read our [article on Project Glasswing and Claude Mythos](https://aitalk.it/it/project-glasswing-mythos.html) will immediately recognize the narrative polarity: Anthropic on one side with a single, ultra-powerful model with deliberately restricted access; Microsoft on the other with an agent system that orchestrates generally available market models.

The difference is not only technical. It is philosophical, almost political.

Mythos is what in computer science would be called a closed-world system: a frontier model not yet released to the general public, accessible only to selected partners in the context of Project Glasswing. Anthropic announced the model in April 2026, explicitly saying they have no immediate plans for general distribution, citing the need to develop more robust technical guarantees before putting it into circulation. The model found 27-year-old vulnerabilities in OpenBSD and identified bugs in FFmpeg that 5 million automatic test runs had never caught. It achieved 83.1% on CyberGym not as a complex agentic system, but as the intrinsic capability of a single model.

MDASH is the opposite: Microsoft explicitly states that the results were obtained using generally available models—no secret proprietary model in the harness. The value lies in the architecture that coordinates them, not in the weights of any specific model. This choice has a relevant architectural consequence: when a new, better model becomes available on the market, MDASH incorporates it by changing a configuration. The investment in plugins, validation processes, and agent specializations survives model changes.

From the perspective of those working in security, the practical question is different for the two systems. Mythos is accessible today only to those in the inner circle of Glasswing partners—big names like AWS, Google, Apple, Cisco—with pricing of $25 per million input tokens once available, rates that cut out most medium-sized organizations. MDASH is in private preview, with the possibility to sign up through a public form, and Microsoft indicates a desire to make it available to a growing set of customers.

Neither is democratically accessible, at least today. But the trajectories are different: Mythos is built around the exceptionality of a single, non-replicable artifact; MDASH around an architecture that is in principle independent of any specific model.

There is also a subtler question regarding benchmark comparisons. Mythos achieves 83.1% on CyberGym as a relatively direct system, without elaborate agentic scaffolding in support. MDASH achieves 88.45% with that same architecture coordinating publicly available models. This means the five-point gap could narrow or reverse if Anthropic applied the same type of agentic scaffolding to Mythos as MDASH, or if Microsoft integrated Mythos as a component of the harness. Benchmarks compare specific configurations, not absolute capabilities.

## The Arms Race: Defense and Attack Are One and the Same

There is a point that both Microsoft and Anthropic touch on delicately in their announcements and that is worth addressing without euphemisms: any system capable of finding vulnerabilities autonomously is, from a technical standpoint, indistinguishable from a system capable of exploiting them.

Microsoft's blog accurately describes how CVE-2026-33824 produces a double-free memory error of a fixed-size chunk, "a well-understood corruption primitive in modern Windows memory management," and then stops there, without publishing further exploitation details. It is exactly the line of responsible disclosure: enough detail to convince that the bug is real and severe, enough restraint not to hand over a working exploit to anyone reading the blog.

But the system that found the bug knows the details the blog omits. And the question that does not yet have a satisfactory public answer is: who controls access to that knowledge, with what supervision, and with what consequences if that access is compromised or abused?

The logic of proactive defense is consistent: defenders must find vulnerabilities before attackers. But every jump in defensive capability also lowers the entry cost for offense. A system like MDASH in the hands of a hostile actor, with access to the right models and the architecture described in Microsoft's public blog, would be an extremely effective offensive reconnaissance tool. This is not a remote hypothesis: it is the structural logic of any dual-use technology.

Microsoft currently keeps MDASH in private preview with manual selection of participants, and Taesoo Kim stated that discussions with U.S. government officials are ongoing. This is not sufficient guarantee for those thinking in terms of a ten-year horizon; models spread, techniques are replicated, and the boundaries between insiders and outsiders are porous by definition. This is not a specific criticism of Microsoft: it is the structural context in which any initiative of this type operates, and it is a conversation the industry continues to postpone.

The comparison that comes to mind is not the most reassuring: it resembles the dynamic described in Naoki Urasawa's manga *Pluto*, where the most powerful robots in history are built to bring peace, and this very capability makes them the most dangerous weapons ever created. Technology has no intentions. The governance architectures surrounding it do.
![grafico2.jpg](grafico2.jpg)
[Image taken from microsoft.com](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/)

## Conclusion: Not Which Model, but Which System

The point that MDASH demonstrates most clearly does not concern Microsoft, or Anthropic, or the comparison between their respective CyberGym scores. It concerns a paradigm transition that was expected but now has concrete data: AI for security has crossed the threshold from experimentation to production.

Sixteen real, correctable vulnerabilities, fixed in a real Patch Tuesday. Four of them would have allowed an unauthenticated remote attacker to execute arbitrary code on Windows systems. They were not in niche code: they were in the networking stack that governs every network connection on every active Windows today. And no one had found them with traditional tools.

The architectural lesson—that the system is worth more than the model, that portability across model generations is the most durable property, and that validation is itself a separate pipeline—is probably the most important thing emerging from the announcement, more than the benchmark numbers. It is a lesson for anyone building AI-based security tools, regardless of the models they choose to use today.

The data issue remains: Microsoft's internal numbers on StorageDrive and MSRC cases are corporate claims, not independent audits. The CyberGym benchmark is the ground where the comparison is verifiable. And it is on that ground that, at the time of publication, MDASH occupies first place.

How long depends on what Anthropic decides to do with Mythos in an agentic system. And, above all, on what comes next.

---
*Microsoft has opened registration for the [private preview of MDASH](https://aka.ms/AI-drivenScanningHarness).*
