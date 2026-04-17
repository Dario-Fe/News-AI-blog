---
tags: [" Generative AI", "Security", "Business"]
date: 2026-04-15
author: "Dario Ferrero"
---

# 10 rules for using AI in business
![10-regole-AI.jpg](10-regole-AI.jpg)

*Let's start with a fact that serves as a mirror. According to the [McKinsey State of AI report of November 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai), 88% of organizations already use AI in at least one business function. Yet, in the same period, the World Economic Forum and Accenture estimated that less than 1% of these have fully operationalized a responsible AI approach, while 81% remain in the most embryonic stages of governance maturity. The paradox is served: almost everyone uses AI, almost no one really governs it.*

The most stinging confirmation comes from [an EY survey of February 2026](https://www.ey.com/en_us/newsroom/2026/03/ey-survey-autonomous-ai-adoption-surges-at-tech-companies-as-oversight-falls-behind) of 500 technology executives: 45% declared that their organization has suffered a confirmed or suspected leak of sensitive data in the last twelve months caused by employees using unauthorized generative AI tools—ChatGPT, Claude, Gemini—often with sensitive company data pasted into a prompt, without IT knowing anything. The [PEX Report 2025/26](https://www.aidataanalytics.network/data-science-ai/news-trends/less-than-half-of-businesses-have-an-ai-governance-policy) closes the picture: only 43% of organizations have a formal AI governance policy, while almost a third, 29%, have none at all.

This piece does not want to be a lecture from above. It is more like that useful conversation you have with a colleague before an important choice: something that helps you understand where you are stepping, with concrete examples and verifiable references. Ten rules, ten controls, ten errors not to repeat.

## First of all: AI security is not IT security with a new hat

Those who work in IT know that there is already a consolidated arsenal of tools for system protection: firewalls, identity management, encryption, vulnerability assessment. The problem is that AI introduces a risk surface that these tools do not see.

A language model can produce false answers with the same confidence with which it produces correct ones, a phenomenon called hallucination in the field, which in business contexts can translate into wrong decisions based on invented information. A RAG (retrieval-augmented generation) system that accesses internal documents can be manipulated through an instruction hidden in a seemingly harmless file: this is what the [OWASP LLM Top 10](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/) calls *prompt injection*, and which in 2025 has already been exploited in real environments. The data you enter into the system can be stored, recorded, or sent to external infrastructures that you do not control.

The [NIST AI Risk Management Framework](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/), updated and increasingly adopted as a global reference, organizes the response to these risks into four functions: *Govern, Map, Measure, Manage*. They are not sequential steps, they are wheels that turn continuously. And this is where it is convenient to start.

## Governance before technology

Before any tool, you need a clear answer to three questions: who decides what can be done with AI in the company? Who is responsible if something goes wrong? To whom is the problem escalated?

ISO/IEC 42001, the international standard for AI management systems published in December 2023 and already adopted as a reference by [KPMG](https://kpmg.com/ch/en/insights/artificial-intelligence/iso-iec-42001.html) and other major consulting players, answers these questions with a simple concept: you need an *AI Management System* with appointed roles, documented processes, and continuous improvement cycles. It's not bureaucracy for its own sake: it's the way not to find yourself managing an incident without knowing who has the authority to shut down the system.

ISO/IEC 42001:2023 remains the current standard and the certifiable reference for AI management systems. It is worth noting, however, that in April 2025 ISO published [ISO/IEC 42005:2025](https://www.aarc-360.com/understanding-iso-iec-42005-2025/), a complementary standard dedicated specifically to impact assessments of AI systems—a tool that helps measure the social and individual effects of AI throughout the lifecycle, not just technical risks. It is not mandatory for 42001 certification, but in practice it fills exactly the gap between "we have governance" and "we know what our system concretely produces on people."

### The invisible problem: shadow AI

Even before talking about risk classification, there is a phenomenon that is worth naming explicitly because it is the most widespread and the least monitored: *shadow AI*. It works exactly like the shadow IT of the 2000s, when employees started using personal Dropbox and Gmail for work files because company tools were slow, only the consequences are more immediate and less reversible.

A financial sector employee pasting an unconsolidated balance sheet into ChatGPT to get help writing a commentary, a recruiter uploading candidate CVs to an external tool to get a pre-selection, a lawyer using a consumer LLM to draft a contractual clause: in all these cases the data leave the company infrastructure, end up on third-party servers with retention policies the company has not negotiated, and potentially contribute to the training of future models. The EY figure cited at the beginning—45% of data leaks from unauthorized tools—is not an exception: it is the silent norm.

The answer is not to ban everything, because unmonitored bans do not work, as the history of shadow IT teaches. The answer is to build governed alternatives that are good enough not to push people to seek external solutions, accompanied by a clear policy on what is allowed, with which tools, and under what conditions. This is exactly the starting point of AI governance.
![grafico1.jpg](grafico1.jpg)
[Image taken from blog.getpolicyguard.com](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/)

## Rule 1 — Classify use cases by risk level, before deployment

Not all AI uses are equal. An internal chatbot for answering questions about holidays is different from a system that evaluates HR candidates or assigns a credit rating to customers. The [NIST AI RMF](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/) uses the *Map* function exactly for this: to create an inventory of AI systems in use and classify them by potential impact level.

The [EU AI Act](https://www.lw.com/en/insights/eu-ai-act-obligations-for-deployers-of-high-risk-ai-systems), with full applicability to high-risk uses by August 2027, identifies high-risk systems as those used for selection and monitoring of employees, for credit, and for profiling individuals. For each of these cases, obligations increase significantly: impact assessment, human oversight, logging, incident notification.

A concrete example: if your company uses an LLM to support recruiters in CV pre-selection, that system is high-risk under the EU AI Act. If the same model is used only to generate draft job descriptions, the risk is much lower. Classification must be done on a case-by-case basis, not by generic category of tool.

## Rule 2 — Limit the data entering the system

The principle is the same as for a diet: not everything you can eat should you eat. In the AI field, it's called *data minimization*, and it's the first defense against the risk of *data leakage*.

The guide published by [CISA, NSA, and FBI in May 2025](https://www.insidegovernmentcontracts.com/2025/06/cisa-releases-ai-data-security-guidance/) is explicit: organizations must classify data before using them in AI systems, apply rigorous access controls, and never assume that datasets are clean and free of malicious content. The same guide introduces the concept of *data provenance*: knowing where the data the model works with come from is not a formality, it is a security requirement.

In practice: establish by policy which categories of data can never enter an AI system (trade secrets, credentials, personal data not strictly necessary, information subject to regulatory constraints). A useful example for the financial sector: unconsolidated balance sheet data should never be used as context in a generic company chatbot accessible to the entire organization.

## Rule 3 — Govern providers, models, and integrations

Corporate AI is rarely a monolithic system that you control in its entirety. It is usually an assembly: a SaaS platform, a third-party foundational model, plugins, external tools connected via API. Each of these components is a potential entry point for risks you haven't evaluated directly.

The [joint 2025 CISA guide](https://www.insidegovernmentcontracts.com/2025/06/cisa-releases-ai-data-security-guidance/) devotes an entire section to the risks of the *data supply chain*, with particular attention to *data poisoning*: the manipulation of training data by malicious actors, which can occur through datasets collected from the web, expired domains bought back on purpose, or injections of false examples into the corpora used for fine-tuning.

The practical control is a structured provider assessment: for each AI component provider, verify where interaction logs are recorded, if and how your data are used to train models, what contractual guarantees exist on data treatment. ISO/IEC 42001 explicitly provides for *third-party supplier oversight* as a management system requirement.

## Rule 4 — Test the system before release

No AI system should go into production without having gone through a test cycle that includes abuse scenarios. The EU AI Act, for high-risk systems, explicitly requires this as part of the *quality management system*: checks on accuracy, robustness, bias, and unexpected behaviors before go-live.

*Red teaming*—the simulation of attacks and improper uses by an internal or external team—is not a practice reserved for big tech companies. Tools like [Promptfoo](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/) allow automating tests based on the OWASP LLM Top 10 even without a dedicated security team.

A concrete example for customer service: before releasing a conversational assistant that has access to customer data, systematically check if it responds differently to users with names of different cultural origin (bias test), if it reveals information about users other than the authenticated one (leakage test), if it can be induced to ignore system instructions with elaborate prompts (jailbreak test).

## Rule 5 — Protect yourself from prompt injection and dangerous output

This is the most technical rule, but it is worth understanding because it is also the most undervalued. *Prompt injection* works like this: a user, or external content that the model reads, inserts instructions that overwrite the original system ones. The model does not distinguish between its operator's instructions and the injected ones: it executes both, and often prefers the most recent ones.

The [OWASP LLM Top 10](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/), the reference document for the security of language models, indicates this as risk number one. Operational countermeasures include: architecturally separating system instructions from user inputs, limiting the tools the model has access to (an assistant answering questions about products doesn't need to be able to send emails or modify databases), applying filters on output to intercept responses containing sensitive structured data.

The agentic age has already begun and is beyond chatbots and copilots; agents do not just answer a question but execute sequences of actions, navigate sites, read and write files, call APIs, send emails, with minimal or no human supervision. The [Deloitte State of AI in the Enterprise report of January 2026](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html) estimates that only 1 in 5 companies today has a mature governance model for autonomous AI agents, while their use is set to grow significantly in the next two years.

In this context, the principle of least privilege stops being a good practice and becomes a condition of survival: an agent with unlimited access to tools, data, and communication channels can produce damage that is difficult to reverse, quickly and automatically. Before deploying any agentic system, the question to ask is: if this agent misunderstands the instruction in the most reasonably wrong way possible, what happens?
![grafico2.jpg](grafico2.jpg)
[Image taken from mckinsey.com](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)

## Rule 6 — Maintain real human oversight, not just formal

There is an empty version of *human oversight*: you put a signature at the bottom of a document saying that a human supervised the decision, even if in reality no one really checked anything. The EU AI Act, in the articles dedicated to the obligations of deployers of high-risk systems, is specific on this point: human oversight must be substantial, not decorative. Overseers must have the competence to interpret the outputs, the ability to interrupt the system, and the authority to do so.

The practical distinction to establish in writing in every critical process is this: AI suggests, human decides. Not "AI decides and human can oppose," because the psychological cost of opposition to an automatic system has already been documented by research: people tend to accept suggestions from automatic systems even when they have doubts, especially under time pressure. In HR, finance, compliance, and health contexts, this dynamic is not acceptable.

## Rule 7 — Monitor the system after go-live

Launch is not the arrival: it's the departure. AI systems degrade over time for reasons that are not always obvious: user language changes, input data shift relative to the original distribution (this is what the [CISA guidance](https://www.insidegovernmentcontracts.com/2025/06/cisa-releases-ai-data-security-guidance/) calls *data drift*), abuse patterns evolve. You need a logging system that records a sample of outputs, automatic alerts when quality metrics deviate from the baseline, and an incident response process that answers the question: if the system does something wrong tonight, who notices and in how much time?

The EU AI Act requires the retention of logs for at least six months for high-risk systems, and notification to authorities in case of serious incidents. ISO/IEC 42001 provides for periodic reviews of the management system. The NIST AI RMF, in the *Manage* function, insists on active monitoring that feeds the improvement cycle.

## Rule 8 — Document everything, really

If it's not documented, it's not governable. It's a phrase that sounds obvious but in daily operation is systematically ignored. Documentation of an AI system is not the user manual: it is the set of approved policies, risk assessments, test results, versions of the model in production, decisions taken, and motivations.

This documentation serves three concrete things: demonstrating regulatory compliance in case of audit, understanding what changed when something stops working, and improving the system over time by learning from errors. The format is not prescriptive, but it must be traceable and accessible to those who need it. A log of model versions in production, kept on a shared Excel file updated manually, is already worth more than nothing.

For those who want to structure this step rigorously, [ISO/IEC 42005:2025](https://www.aarc-360.com/understanding-iso-iec-42005-2025/) offers a specific framework for documenting the impact of AI systems, including sensitive uses, predictable abuses, and unintentional applications, mapped directly onto the controls of ISO/IEC 42001.

## Rule 9 — Train the people who use the system

Human error remains one of the broadest risk surfaces, and training is the most economical defense against it. But there is a fact that transforms this principle from generic common sense to a measurable strategic lever: according to the [CSA and Google Cloud report of December 2025](https://cloudsecurityalliance.org/blog/2025/12/18/ai-security-governance-your-maturity-multiplier), 65% of organizations with full AI governance already train their personnel on AI tools, against only 27% of those with partial policies and 14% of those still in the development phase. It's not a detail: training is one of the most discriminating indicators between those who really govern AI and those who limit themselves to writing policies that no one reads.

AI training is not a mandatory one-hour course that everyone clicks through without looking: it must be role-specific and must address three distinct things. The first is the correct use of tools: how to use the system, what can be asked, what should never be entered. The second is the recognition of limits: employees must know that language models can be wrong with great confidence, and they must have the authority not to trust the output when they have well-founded doubts. The third is incident management: what to do when something goes wrong, whom to report it to, how to document it. The EU AI Act explicitly requires *AI literacy training* for all users of high-risk systems: it's not a regulatory detail, it's operational common sense with a deadline.

## Rule 10 — Update the rules over time

AI is perhaps the only field in which operational instructions age faster than the systems they govern. A governance framework written at the beginning of 2024 does not take into account the agentic capabilities of current models, the new attack vectors documented in 2025, or the approaching EU AI Act regulatory deadlines. Both the [NIST AI RMF](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/) and [ISO/IEC 42001](https://kpmg.com/ch/en/insights/artificial-intelligence/iso-iec-42001.html) are built around the principle of continuous improvement: policies should be reviewed at least once a year, and any significant incident must trigger an immediate review of related controls.

The minimum practicable frequency is this: annual review of the overall framework, semi-annual review of data policies, immediate review after any incident or significant change in the models in use. It is not a heavy cycle: it is the difference between living governance and a document that no one updates.

## Conclusion

Taking a metaphor from *Ghost in the Shell*, not the Hollywood movie, but the original manga by Masamune Shirow, the problem is never the system itself, but who built it and with what intention. Corporate AI works when those who adopted it know exactly what they want to achieve, know the risks it carries with it, and have built a structure capable of responding when things don't go as planned.

The question to ask yourself is not "are we using AI?". Almost certainly yes. The question is: "do we know with what rules?"
