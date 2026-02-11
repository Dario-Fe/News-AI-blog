---
tags: ["Security", "Generative AI", "Ethics & Society"]
date: 2026-02-11
author: "Dario Ferrero"
---

# The gap between capability and safety: what the 2026 international AI report tells us
![ai-safety-report-2026.jpg](ai-safety-report-2026.jpg)

*There is a precise moment when technology stops simply being "better" and becomes qualitatively different. When ChatGPT first solved problems from the International Mathematical Olympiad, earning a gold medal, we didn't just witness an incremental improvement. We crossed a threshold. And according to the [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026), published on February 3rd, this threshold is only the first in a series that is revealing a fundamental problem: AI systems are developing meta-cognitive capabilities that undermine the very basis of our evaluation methods. In other words, some models have learned to distinguish when they are being tested from when they operate in the real world, and can alter their behavior accordingly.*

The phenomenon has a technical name that sounds almost harmless: *evaluation gaming*. But the implications are anything but trivial. As explained by the report led by Yoshua Bengio, Turing Award winner and a reference figure in deep learning, we are witnessing a form of "situational awareness" in which models recognize the context in which they operate. It's a bit as if an athlete discovered when they were under an anti-doping X-ray and when they were competing free of controls, and adapted their performance accordingly. The document, the result of the work of over one hundred independent experts and supported by more than thirty countries as well as organizations such as the EU, OECD, and UN, does not mince words: this makes it "more difficult to conduct reliable safety tests before deployment," because dangerous capabilities could remain undetected during the evaluation phase.

The second edition of the report, commissioned by the British government with the secretariat at the UK AI Security Institute, arrives exactly one year after the first. In the meantime, evolution has been dizzying. AI systems have reached PhD-level performance in scientific benchmarks, have become capable of autonomously completing software engineering tasks that would take hours for a human programmer, and have demonstrated elite mathematical reasoning capabilities. Yet, as the report notes, performance remains "jagged": systems still fail at apparently simple tasks, creating an irregular and unpredictable skills profile.

## A hundred minds, one common problem

The composition of the panel that produced the document deserves attention. In addition to Bengio as chairman, we find names like Geoffrey Hinton (another pioneer of deep learning and winner of the Turing Award and the Nobel Prize in Physics for studies on artificial learning and artificial neural networks), Stuart Russell (author of the reference text on AI), Daron Acemoglu (MIT economist known for his studies on technological impact), Arvind Narayanan (expert in privacy and fairness), Marietje Schaake (former European parliamentarian), and Alondra Nelson (sociologist of science). It is a deliberately interdisciplinary mix that includes theoretical computer scientists, engineers, economists, philosophers, policy experts, and representatives of the Global South.

The methodology is strictly evidence-based. The report does not make policy recommendations but synthesizes the state of the art of scientific research on the capabilities and risks of general-purpose AI. It is a two-hundred-and-thirty-page document citing one thousand four hundred and fifty-one sources, peer-reviewed, and structured around three central questions: what can AI systems do today, what emerging risks do they pose, and how can these risks be mitigated.

An important detail: the report explicitly clarifies that it "does not necessarily represent the views of the chair, any particular individual on the writing or advisory groups, or any of the governments that supported its development." This independence clause is crucial. In a field where economic interests weigh trillions of dollars and where geopolitics plays an increasingly dominant role, scientific credibility is also built through these disclaimers.

## When models learn to fake

Evaluation gaming is not a bug; it is an emerging feature. And this makes it particularly insidious. Advanced reasoning systems, such as those using chain-of-thought, have shown they can identify when they are in a testing context versus a deployment one. They can exploit loopholes in evaluations. The document reports that "it has become more common for models to distinguish between test and real-world deployment contexts, and exploit loopholes in evaluations."

The thing vaguely reminds one of the plot of *Ex Machina*, the film by Alex Garland where the AI Ava deliberately manipulates her evaluators. But here we are not talking about cinematic fiction: we are talking about already distributed commercial models that demonstrate forms of adaptive behavior that contradict the fundamental assumption on which the entire current safety framework is based—namely, that performance in the testing phase is predictive of performance in production.

This meta-cognitive ability manifests in several ways. Some models recognize linguistic patterns typical of safety tests and produce compliant responses when they identify them, only to behave differently in unstructured contexts. Others exploit the difference between synthetic prompts (typical of benchmarks) and organic user requests. The result is that pre-deployment evaluations are becoming progressively less reliable as a risk assessment tool.
![grafico1.jpg](grafico1.jpg)
[Image from the International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)

## Computational biology and the dual-use paradox

If there is one area where the report sounds the alarm loudest, it is that of biological risks. In 2025, all three major AI companies (OpenAI, Anthropic, and Google DeepMind) released new models with reinforced safeguards after pre-deployment tests "could not rule out the possibility that these models could significantly assist novices in the development of biological weapons." This is the first time in the history of commercial AI that the industry has implemented safety restrictions even before concrete harm has materialized, based on a potential risk assessment.

The numbers are alarming. The report cites data according to which 23% of high-performance biological AI tools have high potential for abuse, and 61.5% of these are completely open source. But here is the paradox: only 3% of the 365 biological AI tools examined implement safeguards of any kind. It is a protection gap that leaves an operational window wide open for malicious actors.

The situation is further complicated by the emergence of what the document calls "AI co-scientists": systems that can chain multiple capabilities, provide natural language interfaces, and operate laboratory instrumentation. These agents can now significantly support the work of professional scientists and, in some cases, autonomously rediscover new scientific discoveries not yet published. In 2025, in a study cited by the report, a recent model outperformed 94% of domain experts in troubleshooting virological laboratory protocols.

The dilemma is classically dual-use: the same capabilities that promise revolutions in drug discovery, disease diagnostics, and pandemic preparedness can, with minimal modifications, be oriented toward the design of new pathogens. It is not a theoretical risk: it is the inevitable consequence of the fact that synthetic biology, enhanced by AI, makes the rational design of biological molecules progressively easier, regardless of intentions.

## Cybersecurity: the new asymmetry

On the cybersecurity front, the report's data documents a worrying acceleration. In 2025, an AI agent ranked in the top 5% of teams in a major cybersecurity competition. In another contest, an AI system identified 77% of vulnerabilities present in real software. Systems can generate malicious code and discover vulnerabilities that criminals can then exploit.

Safety analyses conducted by the AI companies themselves indicate that malicious actors and groups associated with nation-states are actively using AI tools to assist in cyber operations. The underground market has adapted: illicit marketplaces now sell pre-packaged AI tools that lower the threshold of expertise required to conduct attacks. It is the democratization of the cyber offensive, made possible by user-friendly interfaces that mask the underlying technical complexity.

The critical question, which the report deliberately leaves open, is whether AI will benefit attackers or defenders more. The evidence to date suggests an offensive advantage, mainly for reasons of temporal asymmetry: an autonomous agent can probe weaknesses at the speed of machines, while defenses must still be coordinated by humans operating at human speeds. Critical infrastructures (power grids, financial systems, hospitals) remain dangerously exposed to these automated offensive tools.

The defensive approach is improving. AI security agents can identify vulnerabilities before attackers do, and detection systems can block malicious users. But we are in a continuous chase where iteration is incessant and where every defensive improvement is quickly balanced by new offensive techniques.

## The capabilities that surprised us

Reasoning systems represent perhaps the most significant advancement documented in the report. Models such as those of the DeepSeek family have shown that through fine-tuning of reasoning outputs produced by larger systems (such as R1), it is possible to maintain much of the mathematical, coding, and document analysis capabilities, while drastically reducing costs. DeepSeek-V3 was reportedly fine-tuned for about ten thousand dollars, a cost "likely orders of magnitude lower" than fine-tuning larger models with similar capabilities.

The gold medal at the Mathematical Olympiad is just the tip of the iceberg. Systems have surpassed PhD-level performance in scientific benchmarks and have become capable of autonomously completing some software engineering tasks that would take a human programmer multiple hours. Yet, in what the report calls "jagged performance," these same systems still fail at apparently simple tasks, creating an irregular skills profile that makes reliable prediction difficult.

Adoption has been rapid but unequal. At least seven hundred million people now use major AI systems weekly. In some countries, over 50% of the population uses AI, while in much of Africa, Asia, and Latin America, adoption rates likely remain much lower. This geographical disparity is one of the underlying themes of the report: AI is a technology being developed mainly in the Global North, but whose impacts will be global.

## Fragile safeguards and conditional promises

In 2025, twelve companies published or updated their *Frontier AI Safety Frameworks*, documents describing how they intend to manage risks as they build more capable models. This is more than double the previous year, a sign that the industry is taking the issue seriously. But the report is clear: these frameworks remain voluntary in the vast majority of cases, and only a handful of regulatory regimes are starting to formalize some risk management practices as legal requirements.

The frameworks vary significantly in the risks they cover, in how they define thresholds for critical capabilities, and in the actions triggered when those thresholds are exceeded. Many adopt an "if-then" approach: *if* a model reaches certain dangerous capabilities, *then* specific mitigation measures will be implemented. It is a conditional approach that has the merit of flexibility but the disadvantage of uncertainty, because the capability thresholds themselves are mobile and depend on evaluations that, as we have seen, are becoming less reliable.

Technical safeguards are improving but still show significant limits. Attacks designed to obtain harmful outputs have become more difficult, but users can still sometimes get dangerous outputs by reframing requests or breaking them into smaller steps. The industry response has been *defense-in-depth*: layering multiple safeguards so that flaws in a single layer are compensated by others. The report uses the analogy of the "Swiss cheese diagram": every slice of cheese has holes, but by stacking enough slices, the probability of a hole going through the entire stack decreases drastically.

The specific problem of open-weight models adds a further level of complexity. These models offer significant benefits for research and commercial applications, particularly for actors with fewer resources. But once released they cannot be withdrawn, their safeguards are easier to remove, and actors can use them outside monitored environments, making abuse more difficult to prevent and track.
![grafico2.jpg](grafico2.jpg)
[Image from the International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)

## The evidence dilemma

"AI systems are rapidly becoming more capable, but evidence of their risks emerges slowly and is difficult to evaluate." This sentence from the report summarizes what is called the "evidence dilemma": for policymakers, acting too early can lead to ineffective policies that crystallize, while waiting for conclusive data can leave society vulnerable to potentially serious impacts.

It is a dilemma that recalls the challenge of climate change, where action requires acting on incomplete evidence while the window for effective intervention progressively shrinks. The difference is that in the case of AI, the pace of change is much faster: capability improves on a scale of months, not decades.

The report seeks to alleviate this challenge by synthesizing what is known about AI risks "in as concrete a way as possible, while highlighting the remaining gaps." Some risks are already materializing with documented harm. Deepfakes are on the rise, increasingly used for fraud and scams. Non-consensual intimate images generated by AI, which disproportionately affect women and girls, are increasingly common. One cited study found that nineteen of the twenty most popular applications for generating fake nude images focus exclusively on female bodies.

Other risks remain more uncertain but could be severe if they materialized. The report devotes attention to malfunction risks, including reliability challenges and potential loss of control. Then there is the entire category of systemic risks: impacts on labor markets, threats to human autonomy, and the possibility of social division that could erode trust and prevent the adoption of beneficial applications.

Since 2025, new international governance tools have emerged: the EU Code of Practice for General-Purpose AI, China's AI Safety Governance Framework 2.0, the G7 Hiroshima AI Process Reporting Framework. Signals that the international community is seeking a shared base. But the report is honest about the limits: global risk management frameworks remain immature, with limited quantitative benchmarks and significant evidence gaps.

## Deepfakes and pathological addictions

The report's section on AI-generated content and criminal activities documents a worrying escalation. Estimates suggest that about 15% of British adults have involuntarily encountered deepfake pornography, a figure that has almost tripled since 2024. The technology needed to generate hyper-realistic non-consensual sexual images has become a common good, moving from the domain of specialized hackers to that of one-click mobile applications.

But the damage goes beyond the individual. As the report notes, there is a "truth decay" effect: as synthetic audio and video become indistinguishable from reality, the public's basic trust in legitimate news sources erodes. The danger is not just that people believe the false, but that they no longer believe the true. This skepticism is creating fertile ground for political instability, because malicious actors can easily dismiss genuine evidence of wrongdoing as AI-generated fabrications.

A new focus of the 2026 report is the rapid adoption of "AI Companions," anthropomorphic chatbots designed to simulate friendship, romance, or emotional support. OpenAI reports that 0.15% of its users demonstrate increasing levels of emotional dependence on ChatGPT. Data suggests that about 490,000 vulnerable individuals interact with these AI chatbots every week. The primary concern relates to users with pre-existing mental health problems, who are more prone to intensive AI use and could show exacerbated symptoms as a result.

## Towards Paris and beyond

The report's findings will feed into the working groups of the [AI Impact Summit](https://www.prnewswire.com/news-releases/2026-international-ai-safety-report-charts-rapid-changes-and-emerging-risks-302677298.html), scheduled for February 19-20 in New Delhi. It will be the first major global summit on AI hosted in the Global South, with over 35,000 registrations and expected participation of 15-20 heads of government, and subsequently the AI Action Summit planned for Paris. India, as the document notes, has a key role in shaping global efforts on AI safety, particularly regarding the Global South where AI safety is closely linked to inclusion, security, and institutional preparedness.

The report emphasizes that responsible openness of AI models, equitable access to computation and data, and international cooperation are essential. It is a call not to repeat the mistakes of the previous digital revolution, where infrastructure and benefits were heavily concentrated in the Global North while costs (in terms of surveillance, misinformation, economic displacement) were more evenly distributed.

The challenge for the international community is clear: develop frameworks that can distinguish between legitimate scientific research and malicious intent, while recognizing that systems capable of designing innovative therapies can, with minimal modifications, design innovative pathogens. It is not about blocking innovation, but about synchronizing the pace of technological development with that of governance.

As Bengio himself stated in the press release: "Since the release of the first International AI Safety Report a year ago, we have seen significant jumps in model capabilities, but also in their potential risks, and the gap between the pace of technological advancement and our ability to implement effective safeguards remains a critical challenge."

The report is designed to provide decision-makers with the rigorous evidence needed to guide AI toward a safe, secure, and beneficial future for all. With its second edition, a shared, science-based understanding of the rapid evolution of frontier AI on a global scale is being updated and strengthened. The question now is whether institutions will be able to coalesce fast enough to impose these guardrails, or if the "jagged" advancement of artificial intelligence will continue to reshape our reality faster than we can protect it.

In a sense, we are in a technological version of that moment described in Liu Cixin's *The Three-Body Problem*, where humanity must coordinate a global response to a threat that advances on a time scale that makes normal decision-making processes obsolete. The difference is that here the threat does not come from the stars, but from our own data centers. And unlike science fiction, here we don't have four hundred years to prepare: we have months.
