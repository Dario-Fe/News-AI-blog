---
tags: ["Research", "Ethics & Society", "Generative AI"]
date: 2025-12-15
author: "Dario Ferrero"
---

# When the Algorithm Makes a Diagnosis: FDA and EMA Clear AI for Pharmaceutical Trials
![fda-ema-aim-nash-ai.jpg](fda-ema-aim-nash-ai.jpg)

*There's a scene in *Ghost in the Shell* where Major Kusanagi questions the nature of her own consciousness, wondering if it's truly human or just a sophisticated simulation. It's a question that resonates unexpectedly in the pathology lab when an artificial intelligence algorithm produces a diagnosis that diverges from a human's. Who is right? Or rather: does a single "right" answer still exist when clinical decisions become computational?*

On December 8, 2025, the U.S. Food and Drug Administration [qualified AIM-NASH](https://www.fda.gov/drugs/drug-safety-and-availability/fda-qualifies-first-ai-drug-development-tool-will-be-used-mash-clinical-trials), the first artificial intelligence-based tool as a Drug Development Tool for clinical trials on metabolic steatohepatitis, better known by the acronym MASH. The same technology, rebranded as AIM-MASH for the European market, had already obtained a [Qualification Opinion](https://www.ema.europa.eu/en/news/ema-qualifies-first-artificial-intelligence-tool-diagnose-inflammatory-liver-disease-mash-biopsy-samples) from the European Medicines Agency eight months earlier. This is not an approval for direct clinical use in patients, but something potentially more profound: the recognition that an algorithm can replace the consensus of three expert pathologists in evaluating liver biopsies during the development of new drugs.

MASH represents an advanced stage of non-alcoholic fatty liver disease, a condition affecting about one-third of the adult population in Western countries. When fat accumulates beyond five percent of the liver's weight, it can trigger an inflammatory process leading to cellular swelling, the formation of scar tissue, and, in severe cases, cirrhosis or hepatocellular carcinoma. The problem is that accurately diagnosing MASH requires a liver biopsy, and the interpretation of that biopsy is far from simple.

The NASH Clinical Research Network has developed a scoring system over the years that evaluates four main parameters: steatosis (fat accumulation), lobular inflammation, hepatocyte ballooning, and fibrosis. Each element receives a score ranging from zero to three or four, and the overall sum determines the severity of the disease. It seems straightforward on paper, but the reality is quite different. Studies published in specialized journals show that the agreement between pathologists, even experts, ranges from kappa values of 0.25 for cellular ballooning to 0.62 for steatosis. In practical terms, this means that two pathologists looking at the same biopsy could reach different conclusions in forty percent of cases.

This is where PathAI, a Boston-based startup founded in 2016 by Andrew Beck, a pathologist at Beth Israel Deaconess Medical Center, and Aditya Khosla, a computer scientist specializing in machine learning, comes in. The company has raised over $255 million in five funding rounds, involving investors such as General Atlantic, Kaiser Permanente, and Bristol Myers Squibb. Their AISight platform promises to transform digital pathology from an artisanal process into an industrial workflow, with AI as the central element.

## PathAI: From Boston to the Regulatory Table

PathAI did not achieve FDA qualification by chance. The company has systematically built a portfolio of technologies covering the entire spectrum of computational pathology: from detecting tumor biomarkers like PD-L1 and HER2 to characterizing the tumor microenvironment. Their system for MASH, however, represents something different: not just a decision support tool, but a tool that can replace the multiple-consensus required by experimental protocols.

The model was trained on over one hundred thousand annotations from 59 pathologists who evaluated more than five thousand liver biopsies collected from nine major clinical trials. This is not a laboratory dataset, but material from real studies, with all the variability and complexity of the real world. The algorithm uses deep learning techniques to analyze digitized images of the biopsies, identifying microscopic patterns that the human eye might overlook or interpret differently.

The validation presented to the FDA and EMA demonstrated that AIM-NASH evaluations, verified by a single expert pathologist, achieve a level of concordance with the consensus of three experts comparable to what any single pathologist would have with the same consensus. In other words, AI plus one human performs as well as three humans together, with significant savings in time and resources. The intraclass correlation exceeds 0.90 for all major parameters, a value considered "excellent" in scientific literature.

But one element distinguishes this result from the usual tech industry proclamations: regulatory transparency. PathAI submitted its algorithm to the FDA's Drug Development Tool Qualification Program, a path that requires years of work and rigorous demonstration that the tool produces scientifically valid and reproducible data. The fact that the algorithm is "locked," meaning frozen in a specific version that cannot be modified without a new qualification, represents a guarantee of stability and traceability that traditional machine learning rarely offers.

## AIM-NASH/MASH: Anatomy of a Qualification

The FDA qualification of AIM-NASH fits into a precise regulatory framework, that of Drug Development Tools, established by the 21st Century Cures Act of 2016. This is not an approval for direct clinical use, but the recognition that a tool can be used to generate data in regulated contexts like clinical trials. It's a subtle but crucial distinction: AIM-NASH does not diagnose patients in hospitals, but supports the evaluation of endpoints in trials for anti-MASH drugs.

The context of use is specific: evaluation of liver biopsies in clinical studies that use the NASH Clinical Research Network scoring system. The process involves the pathologist uploading the digitized biopsy image to PathAI's cloud platform, the algorithm producing scores for each parameter (steatosis, inflammation, ballooning, fibrosis), and the pathologist reviewing the output before accepting or rejecting it. The final step is crucial: the ultimate responsibility remains human, but the decision-making process is machine-assisted.

The European Medicines Agency followed a parallel but not identical path. The Qualification Opinion issued by the CHMP (Committee for Medicinal Products for Human Use) on March 20, 2025, presents some substantial differences compared to the FDA qualification. While the FDA qualified a specific tool for a defined context of use, the EMA issued an opinion on an innovative methodology that can be adopted by pharmaceutical developers in their studies.

The distinction is subtle but important. In the European system, a company wishing to use AIM-MASH in a trial must still submit its plan of use to the EMA, which will evaluate it in the specific context. The qualification is not a universal "stamp of approval," but an indication that the methodology is scientifically valid and can be considered acceptable. It is a more flexible but also more complex approach for pharmaceutical sponsors to navigate.
![fda-screenshot.jpg](fda-screenshot.jpg)
[Image from fda.gov](https://www.fda.gov/drugs/drug-safety-and-availability/fda-qualifies-first-ai-drug-development-tool-will-be-used-mash-clinical-trials)

## Transatlantic Parallelism with Substantial Differences

Looking at the timelines, the European path was slightly ahead: the EMA opinion arrived in March 2025, the FDA's in December of the same year. PathAI had to navigate two distinct regulatory processes, adapting documentation and validation studies to the specifics of each system. The fact that both agencies reached convergent conclusions is an important signal for the industry: AI in pathology is no longer considered an experimental technology, but a mature tool for regulated contexts.

However, the underlying philosophies differ. The FDA system is more geared towards qualifying specific tools that, once approved, can be used by any sponsor without further case-by-case evaluations. The EMA system, on the other hand, favors a methodological approach, where each specific application requires a contextual assessment. Both models have advantages and limitations: the former offers greater predictability and lower costs for sponsors, while the latter ensures tighter control over how the technology is actually used.

Another point of divergence concerns the concept of a "single reader" versus consensus. Traditionally, MASH trials require three independent pathologists to evaluate each biopsy, with the final result determined by consensus. This is a costly and slow process, which can take weeks or months to complete the analysis of hundreds of samples. AIM-NASH/MASH proposes a different model: a single expert pathologist, assisted by the algorithm, can produce evaluations comparable to the triple consensus.

Both the FDA and EMA have accepted this proposition, but with different limitations. The EMA stressed that the model is "locked" and that any substantial improvements will require re-qualification. It also encouraged continuous optimization, recognizing that machine learning is inherently evolutionary. The FDA was more pragmatic, focusing on the context of use and the demonstration that the tool produces reliable data for regulatory endpoints.

## The Achilles' Heel: Bias and Representativeness

Despite the enthusiasm, there is an elephant in the room that neither the FDA nor the EMA could completely ignore: the representativeness of the training dataset. The more than five thousand samples used to train AIM-NASH come predominantly from clinical trials conducted in North America, Europe, and China, with an overrepresentation of Caucasian and Asian populations. Samples from Latin America, Africa, and the Middle East are substantially absent.

This is not a technical problem, but an epistemological one. An algorithm trained on biopsies from Caucasian patients may not recognize pathological patterns with the same accuracy in tissues of other ethnicities, where genetic, metabolic, and environmental factors produce different histological manifestations. Recent studies in computational pathology have documented significant disparities in the performance of diagnostic algorithms when applied to populations not represented in the training set.

PathAI is aware of the problem and has stated its intention to expand the dataset with more diverse samples. However, the qualified model is "locked," which means that any substantial integration would require new validation and re-qualification. This creates a paradox: on the one hand, the stability and traceability of the model are fundamental regulatory guarantees; on the other, they limit the ability to correct biases identified after qualification.

A second order of problems concerns geographical generalizability. MASH trials are global, involving centers in dozens of countries with different histological processing standards. Biopsies are prepared, stained, and digitized with protocols that vary between laboratories, scanners, and operators. Is the algorithm robust to these variations? The validation presented to the FDA and EMA suggests so, but the publicly available data does not cover the full range of technical variability encountered in real practice.

Then there is the issue of sampling bias in the most literal sense: a liver biopsy captures only a tiny fraction of the liver, typically a 1-2 centimeter tissue cylinder. If steatosis or inflammation is unevenly distributed, the sample may not be representative of the overall state of the organ. This is an intrinsic limitation of the procedure, not of the AI, but artificial intelligence cannot correct for inadequate sampling; it can only analyze it with greater consistency.
![ema-screenshot.jpg](ema-screenshot.jpg)
[Image from ema.europa.eu](https://www.ema.europa.eu/en/news/ema-qualifies-first-artificial-intelligence-tool-diagnose-inflammatory-liver-disease-mash-biopsy-samples)

## Pathologists on the Verge of Extinction?

The question that looms in every discussion about medical AI is always the same: are we building tools to assist professionals or to replace them? In the case of AIM-NASH, the official answer is clear: to assist. The pathologist retains final responsibility, reviews every algorithmic output, and can accept or reject it. The system is "AI-assisted," not "AI-driven."

But economic realities suggest more complex dynamics. If a single pathologist with AIM-NASH can do the work of three pathologists without AI, what happens to the two surplus pathologists? In the short term, they might be reassigned to other diagnostic tasks where demand exceeds supply. In the long term, the demand for pathologists specializing in MASH could contract.

PathAI emphasizes that the problem in pathology is not a lack of work, but a shortage of experts. There are more biopsies to evaluate than available pathologists, and waiting times for specialized reports can be weeks. In this scenario, AI becomes a capacity multiplier that allows for scaling without proportionally increasing the number of professionals. It is the classic argument for automation: it frees humans from repetitive tasks, allowing them to focus on complex cases.

However, there is an unresolved tension between the training model of pathology and the direction AI is pushing. Pathologists train through years of practice on thousands of cases, developing an intuition that goes beyond codifiable rules. If more and more routine diagnoses are delegated to algorithms, where will future pathologists train? How will they develop the clinical sensitivity that allows them to recognize anomalous patterns that the AI has never seen?

This is the paradox of automated expertise: algorithms need experts to be validated and supervised, but their very existence reduces the training opportunities that produce those experts. It is not an immediate problem, but it will become one in the next decade if the educational models of diagnostic medicine are not rethought.

## Follow the money: resmetirom and beyond

Behind the regulatory enthusiasm for AIM-NASH lies a very concrete economic reality: MASH represents one of the most promising pharmaceutical markets of the decade. For years, the disease was considered intractable, with no approved therapies beyond lifestyle management. But in recent years, the pipeline has filled with late-stage candidates, and some are reaching regulatory milestones.

Resmetirom, developed by Madrigal Pharmaceuticals, [received FDA approval](https://www.fda.gov/news-events/press-announcements/fda-approves-first-treatment-patients-liver-scarring-due-fatty-liver-disease) in March 2024 as the first specific treatment for MASH with fibrosis. The drug, a selective thyroid hormone receptor-beta agonist, has been shown in trials to reduce inflammation and improve fibrosis markers. Its development required multicenter trials on thousands of patients, with repeated histological evaluations that were a major bottleneck.

Other candidates are following similar paths. Semaglutide, Novo Nordisk's blockbuster already approved for diabetes and obesity, is being evaluated for MASH with promising results. Akero Therapeutics' efruxifermin, an FGF21 analog, has shown significant reductions in fibrosis in phase 2 trials. Boehringer Ingelheim's survodutide, a dual GLP-1/glucagon agonist, is entering phase 3 with ambitious endpoints.

All these trials require liver biopsies as a primary or secondary endpoint, and the variability in histological assessment is a serious statistical problem. If the measurement noise is high, larger samples are needed to detect significant differences between treatment and placebo. Larger samples mean higher costs, longer timelines, and delays in patient access to therapies.

AIM-NASH promises to reduce that noise. If algorithmic evaluations are more consistent than human ones, fewer patients are needed to demonstrate a drug's efficacy. PathAI's estimates suggest that using the tool could reduce the required sample size by twenty to thirty percent in some experimental designs. Translated into numbers: a trial that would have required a thousand patients could stop at seven hundred, with savings in the tens of millions of dollars.

It is not hard to understand why companies like Bristol Myers Squibb, GSK, Gilead, and Roche have partnered with PathAI. AI in pathology is not just a technological curiosity, but an opportunity to drastically reduce the costs and timelines of pharmaceutical development. The potential ROI is enormous, and the market has understood this: PathAI is valued at about one billion dollars in its latest funding round.

## The Unanswered Questions

Despite the regulatory success, substantial questions remain that neither the FDA nor the EMA have fully resolved. The first concerns long-term safety: what happens if the algorithm, after years of use in thousands of trials, shows biases or systematic errors that were missed during the initial validation? Who is responsible? PathAI? The sponsors who used the tool? The agencies that qualified it?

The framework of liability in medical AI is still nebulous. If a drug is approved based on data generated with AIM-NASH, and it is later discovered that the algorithm systematically overestimated or underestimated a critical parameter, what are the legal and regulatory implications? There are no clear precedents, and the legal system is still developing the conceptual categories needed to address these scenarios.

A second issue concerns geographical transferability. As mentioned, the model was trained on specific populations. When it is used in trials conducted in sub-Saharan Africa, South America, or South Asia, will it maintain the same performance? And if not, how will the problem be detected before it compromises the integrity of the studies?

PathAI has implemented quality control mechanisms that should flag anomalous samples, but the definition of "anomalous" depends on the distribution of the training set. This is a classic machine learning problem: out-of-distribution detection is difficult, and false negatives can be insidious. A sample that the algorithm evaluates with high confidence might actually belong to a region of the feature space never seen during training.

Finally, there is the issue of economic accessibility. AIM-NASH is a proprietary cloud platform, and PathAI charges per-sample fees to sponsors who use it. For trials conducted by big pharma with multimillion-dollar budgets, the cost is marginal. But for academic trials, small biotechs, or research centers in low- and middle-income countries, it could become prohibitive. There is a risk that AI in pathology will create a gap between those who can afford it and those who cannot, with consequences for the diversity and representativeness of global research.

The qualification of AIM-NASH by the FDA and EMA marks a turning point in the history of regulatory medicine. For the first time, an artificial intelligence algorithm has been recognized not as an experimental gadget, but as a reliable tool for generating data in regulated contexts. It is a recognition that comes after years of skepticism and false starts, and it represents a validation of the potential of computational pathology.

However, it would be naive to ignore the unresolved issues. Dataset biases, liability questions, and global accessibility problems are not technical obstacles that can be overcome with more data or better algorithms. They are systemic challenges that require new conceptual, legal, and ethical frameworks. Major Kusanagi, faced with the biopsy-reading algorithm, would continue to ask: when we entrust such important decisions to machines, what do we lose that is essentially human? And what do we gain that humans alone could not achieve?

The answers are not yet clear, but one thing is certain: the era of AI as a passive support is ending. What is emerging is a hybrid model where humans and algorithms merge into complex decision-making systems, with logics and responsibilities that no longer belong to either one alone. As always, technology runs faster than our ability to understand it. And as always, we are left to chase after it, trying not to lose sight of what really matters: patient health, research integrity, and justice in access to care.
