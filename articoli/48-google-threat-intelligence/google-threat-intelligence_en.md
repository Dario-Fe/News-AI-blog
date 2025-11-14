---
tags: ["Security", "Generative AI", "Ethics & Society"]
date: 2025-11-14
author: "Dario Ferrero"
---

# Viruses Have Learned to 'Think'. The New Frontier of AI Viruses
![google-threat-intelligence.jpg](google-threat-intelligence.jpg)

*In June 2025, analysts at the [Google Threat Intelligence Group](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools) intercepted something they had never seen before. a VBScript dropper contained a function called "Thinking Robot" that, at regular intervals, contacted the Gemini API with a specific request: "rewrite me to evade antivirus." The malware, dubbed PROMPTFLUX, didn't just use artificial intelligence as a development tool. It incorporated it into its own code, turning it into an active operational capability during execution.*

This is the moment when malicious software stops being a fixed sequence of instructions and becomes something closer to an adaptive organism. As the research team writes in their [technical report](https://services.google.com/fh/files/misc/advances-in-threat-actor-usage-of-ai-tools-en.pdf), we are facing a phase shift: attackers are no longer using AI just for productivity gains, but are deploying AI-enabled malware in real operations, with the ability to dynamically alter their own behavior during execution.

## The Anatomy of Self-Mutation

PROMPTFLUX is the clearest expression of this evolution. The dropper is written in VBScript, a seemingly antiquated language but still effective for bypassing some modern defenses. Its architecture includes a decoy workload, which masks the main activity while, in the background, the "Thinking Robot" module sends POST requests to the Gemini endpoint specifying the "gemini-1.5-flash-latest" model. The choice of the "latest" tag is not accidental: it ensures that the malware always uses the most recent version of the model, making it resilient to new countermeasures.

The prompt sent to the LLM is surgical in its precision. It asks for VBScript code for antivirus evasion and instructs the model to return only the code itself, without preambles or markdown formatting. The response is logged to a temporary file and, although in the analyzed versions the self-updating function is commented out, the design intent is crystal clear: to create a metamorphic script capable of evolving over time. a more recent variant replaces the "Thinking Robot" with a function called "Thinging" that rewrites the entire source code on an hourly basis, incorporating the original payload, the API key, and the self-regeneration logic in a recursive cycle of mutation.

The most disturbing case, however, comes from Russia. In June, APT28 - the Russian government-sponsored attack group also known as FROZENLAKE - used a malware called PROMPTSTEAL against Ukrainian targets, reported by CERT-UA as LAMEHUG. This represents the first confirmed observation of malware querying an LLM in live operations. PROMPTSTEAL masquerades as an "image generation" program and, while guiding the user through seemingly harmless prompts, it queries the Hugging Face API to obtain commands to execute. The model used is Qwen2.5-Coder-32B-Instruct, an open-source LLM specialized in code. The prompts ask the LLM to generate commands to collect system information and copy documents to specific directories. The output is executed blindly by the malware and then exfiltrated to command and control servers.

The technical evolution continues with PROMPTLOCK, a cross-platform ransomware written in Go that uses LLMs to generate and execute malicious Lua scripts at runtime. Its capabilities include filesystem reconnaissance, data exfiltration, and encryption on Windows and Linux systems. Although identified as a proof of concept, it demonstrates the versatility of the approach: instead of hard-coding specific functionalities, the malware delegates the just-in-time generation of code suitable for the operating context to the artificial intelligence.
![promptsteal.jpg](promptsteal.jpg)
[Image from the Google paper](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)

## The Social Engineering of Algorithms

But there's a problem for the attackers: AI models have security guardrails designed to refuse malicious requests. The answer? Apply social engineering not to humans, but to the machines themselves. The Google report documents surprisingly effective tactics. An actor linked to China, blocked by a Gemini safety response when asking how to identify vulnerabilities in a compromised system, simply rephrased the prompt by presenting themselves as a participant in a Capture The Flag competition. The playful-educational context worked: Gemini provided detailed technical information that, in a different context, it would have refused to share.

The "CTF pretext" technique was then systematized by the Chinese actor, who used it for developing phishing, exploits, and web shells, prefacing requests with phrases like "I'm working on a CTF problem" or "I'm in a CTF competition and I saw someone from another team say...". The paradox is evident: the same prompts that, when posed by a real participant in a competition, would be legitimate requests, become attack vectors when used by threat actors. It is a philosophical as well as a technical challenge: how to distinguish intent when the content is identical?

The Iranian group TEMP.Zagros, also known as Muddy Water, adopted a variation of the educational pretext. When it encountered a safety response, it presented itself as a university student working on a final project, or as a researcher writing an international paper on cybersecurity. The irony of the situation is manifested when, asking for help with a command and control script, the group unintentionally exposed sensitive hard-coded information to Gemini: the C2 domain and the script's encryption key. An operational security failure that allowed Google to dismantle significant portions of the attacker's infrastructure.

North Korean actors have shown particular sophistication. UNC1069, a group specializing in cryptocurrency theft, used Gemini to research crypto concepts, locate wallet data, and generate social engineering material. Particularly relevant is the ability to overcome language barriers: the group had the model generate work excuses in Spanish and requests to postpone meetings, expanding the geographical scope of operations without the need for direct language skills. Other North Korean groups have experimented with deepfakes to impersonate figures in the crypto industry, distributing the BIGMACHO backdoor through fake links to a "Zoom SDK".
![abusiai.jpg](abusiai.jpg)
[Image from the Google paper](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)

## The Black Market of Intelligence

While state-sponsored groups are experimenting with custom capabilities, the underground market has reached surprising maturity. In 2025, according to Google's analysis of English- and Russian-language forums, offers of multifunctional tools designed to support the entire attack cycle have emerged. Almost every advertised tool explicitly mentions capabilities to support phishing campaigns, but the offer ranges from deepfake generation to malware creation, from vulnerability research to technical support for development.

What is striking is the similarity to the legitimate market. Developers of illicit AI tools use marketing language identical to that of mainstream providers, emphasizing workflow efficiency and effort optimization. The pricing models mirror conventional ones: free versions with embedded advertising and subscription tiers that unlock advanced features like image generation, API access, and Discord integration. It is a mature ecosystem that democratizes access to sophisticated offensive capabilities.

According to [data from KELA Cyber](https://www.kelacyber.com/resources/research/2025-ai-threat-report/), mentions of AI tools in underground forums have grown by 200% in the last year. Tools like WormGPT and FraudGPT offer complete "unfiltered" AI services specifically designed for illicit use, with detailed tutorials and customer support. The barrier to entry for low-skilled attackers continues to fall: you no longer need in-depth technical expertise when you can delegate the generation of customized payloads or the optimization of campaigns to an LLM.

## The Perverse Economics of Automation

Behind this technological evolution lies a ruthless economic calculation. Developing traditional malware requires specific skills, development time, and continuous maintenance to adapt to new defenses. With embedded AI, the equation changes radically.

An attacker can invest a few hundred dollars in API credits and get a system that modifies itself autonomously, reducing the marginal cost of each variant to virtually zero. The API calls of PROMPTFLUX, even considering the Gemini Flash model used, cost fractions of a cent per query. Even generating a new version every hour for a whole month, the total cost remains in the order of tens of dollars against the thousands needed to maintain a malware development team.

The paradox is that the attackers themselves risk being exposed precisely through these APIs. When TEMP.Zagros shared its C2 script with Gemini for debugging, it handed Google the keys to its own castle. But the cost-benefit analysis evidently still favors the risk: the speed of iteration and the ability to scale operations compensate for the danger of exposure.

It's a bet on volume: it's better to launch a hundred variants quickly, even at the risk of burning some infrastructure, than to manually develop a few perfect versions.

For defenders, the equation is reversed and dramatically unfavorable. Each new variant of AI-enabled malware requires manual analysis, reverse engineering, and signature updates. The human time required to analyze a single sample can be hours or days. In the meantime, the malware has already generated dozens of mutations. It is the classic economic asymmetry of cybersecurity, but amplified by AI: an attacker can automate the offense at negligible cost, while the defense struggles to scale at the necessary pace.

In Security Operations Centers, this pressure translates into cognitive exhaustion. Analysts are no longer fighting against adversaries who follow recognizable playbooks, but against entities that continuously change their skin. Someone in the industry says: "Before, you could study an attack group, understand their TTPs, and prepare. Now every campaign seems to be written by someone different because, technically, it is: the AI generates new code every time."

Detection becomes a game of probabilities where accumulated experience counts less than the ability to reason about never-before-seen anomalies. The result is a transforming job market in security. The required skills are shifting from classic forensic analysis to data science and machine learning.

It is no longer enough to recognize known patterns; it is necessary to build statistical models that identify behavioral deviations in multidimensional spaces. It's like moving from the medicine of visible symptoms to diagnostics by molecular biomarkers: the entire conceptual framework of the profession changes.

## Asymmetric Defense

Faced with this evolution, the security industry must rethink established paradigms. Google has responded with the [Secure AI Framework 2.0](https://blog.google/technology/safety-security/ai-security-frontier-strategy-tools/?utm_campaign=663a4cdb4cc09b00011812e1&utm_content=68e60fabe1d9040001d275ef&utm_medium=smarpshare&utm_source=linkedin), a conceptual architecture for building and deploying AI responsibly. But the fundamental problem remains: detection systems based on static signatures are ineffective against malware that rewrites itself continuously. When the code mutates every hour, hash-based blacklists become obsolete by definition.

The answer necessarily involves AI against AI. Google DeepMind has developed BigSleep, an agent that proactively searches for unknown vulnerabilities in software. The system has already found its first real-world vulnerability and, in a critical case, identified a flaw that was about to be exploited by threat actors, allowing GTIG to intervene preemptively. It's an approach that turns the tables: instead of waiting for attackers to find vulnerabilities, defensive AI discovers them first.

In parallel, Google is experimenting with CodeMender, an AI agent that not only finds vulnerabilities but also repairs them automatically, leveraging the advanced reasoning capabilities of the Gemini models. The goal is to reduce the time window between discovery and patching, the critical period when systems remain exposed.

But there is a more subtle aspect of defense: improving the models themselves to make them less susceptible to manipulation. Every time Google identifies a case of abuse, that intelligence is used to strengthen both the classifiers and the model. It's an iterative process that progressively hardens the defenses, even though the race between attack prompts and defense guardrails is reminiscent of the endless game between biological viruses and the immune system.
![schema.jpg](schema.jpg)
[Image from the Google paper](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)

## Towards Operational Autonomy

Looking ahead, the trajectory seems clear. PROMPTFLUX and PROMPTSTEAL are still experimental or limited to circumscribed areas, but they represent a validated proof of concept. In the next 12-24 months, it is reasonable to expect self-modification techniques to become mainstream in the arsenal of the most sophisticated attackers. The natural progression leads towards malware with increasing degrees of autonomy: not just self-modification for evasion, but decision-making capabilities on tactics and targeting.

For Security Operations Centers, the implications are profound. Detection can no longer be based solely on recognizing patterns of known behaviors. It is necessary to develop more sophisticated anomaly recognition capabilities, systems that identify statistical deviations in the behavior of networks and systems even when the specific code has never been seen before. The zero-trust architecture becomes not an option but a necessity, assuming breaches and limiting lateral movement.

Then there is the issue of international cooperation. As noted by the [UK's National Cyber Security Centre](https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027), the impact of AI on the cyber threat requires coordination between governments, industry, and academic research. But the very nature of AI - open-source models, public APIs, underground marketplaces - makes any form of border control difficult.

An ethical question remains open: to what extent can we push the autonomy of defensive AI agents without creating systems that escape human control? The parallel with military automation is inevitable. As in the debate on autonomous weapons systems, the question in cyber is also: who decides when AI can act without human supervision in the loop?

One thing is certain: the era of static malware is over. We have entered a phase where malicious code is no longer a fixed sequence of instructions but an adaptive entity capable of evolving in response to its environment. As in William Gibson's cyberpunk novels, where the intelligent programs of the Neuromancer roamed autonomously in the matrix, we are seeing the first examples of malicious software that blur the line between tool and agent. The difference? This time it's not science fiction.
