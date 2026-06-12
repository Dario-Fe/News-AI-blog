---
tags: ["Research", "Generative AI", "Training"]
date: 2026-06-12
author: "Dario Ferrero"
---

# ChartNet: chart analysis is no longer just for big budgets
![chartnet.jpg](chartnet.jpg)

*For the first time, a small open-source AI model interprets charts better than commercial giants, thanks to ChartNet, the revolutionary MIT dataset of 1.5 million synthetic samples that combines plotting code, rendered images, data tables, natural language summaries, and reasoning Q&A pairs. The result? Anyone who needs to analyze a 200-page financial report can now use a free 3-billion parameter model on HuggingFace to extract data, reconstruct charts, and get reasoning-based answers, democratizing visual data analysis for SMEs, researchers, and professionals with limited budgets.*

Imagine having a financial analyst who perfectly understands English and knows all the fundamentals of a balance sheet, but when you show them a bar chart with quarterly revenues, they respond by describing the colors of the bars instead of reading the numbers. It's a paradoxical situation, yet it's exactly what happens to many of the visual artificial intelligence models on the market today, including some of the most famous and expensive.

The problem is not new, but it has long remained in the shadows, obscured by the clamor surrounding AI's linguistic capabilities. So-called vision-language models—those that process both text and images—have made spectacular progress in describing photographs, recognizing objects, and transcribing documents. But when they encounter a chart, their reasoning stalls in a subtle and dangerous way: they see a figure, but they don't understand the data that figure represents.

Interpreting a chart is not simply "looking at an image." It requires merging three distinct skills: the visual perception of geometric shapes (where the bars are, where the trend line passes), the structural understanding of numerical data (axis scale, proportions, absolute values), and the linguistic understanding of labels, titles, and legends. It is a cognitive triangulation that the human brain performs almost automatically, but for an artificial model, it remains an open challenge—a territory where even systems with billions of parameters stumble over seemingly trivial details.

Dhiraj Joshi, senior scientist at IBM Research, clearly described the problem in the [MIT announcement](https://news.mit.edu/2026/mit-researchers-teach-ai-models-to-interpret-charts-0603): the financial industry lives on charts, and if vision-language models can reliably extract information, trend descriptions, variations over time, and comparisons between categories, dozens of downstream workflows that currently require human analysts or expensive tools open up automatically. But the keyword is "reliably." A model that responds with confidence but gets the numbers wrong is worse than no model at all.

The bottleneck, as often happens in this field, was not in the models. It was in the data.

## How a dataset of 1.5 million charts is born

Anyone who follows the AI world knows that the quality of training data is almost always more important than the model architecture. A simple but well-nourished idea almost always beats a brilliant idea starved of examples. The problem with charts is that collecting, labeling, and rendering them in a way that is truly useful for training is extraordinarily difficult.

The datasets existing before ChartNet were, looking back, almost naive in their partiality. FigureQA, one of the best known, contained 100,000 images but covered only three types of charts and used a single rendering library, accepting only binary yes/no answers. DVQA was built around only one type of chart. ChartQA, more ambitious, included real images and complex questions but stopped at 14,000 examples—not nearly enough to train a robust model. The common gap was structural: none of these datasets linked the chart image to the code that generated it, the underlying data, a natural language description, and, above all, to explicit reasoning chains.

Jovana Kondic, an MIT doctoral student in electrical engineering and computer science and lead author of the [paper](https://arxiv.org/pdf/2603.27064), framed the problem with an analogy worth repeating: a model, unlike the human brain, might need to see thousands of examples during training to reliably recognize something like a line chart. Data scarcity is not an inconvenience; it's a structural barrier.

The solution conceived by the MIT-IBM team is elegant precisely because it reverses conventional logic. Instead of collecting charts from the internet and then attempting to annotate them, the researchers built a pipeline that generates charts starting from code. The underlying idea, so-called code-guided synthesis, works like this: you take an initial set of existing chart images, use a visual model to approximately reconstruct the code that might have generated them, and then use that code as a seed to produce hundreds of variants. Change the chart type, modify the values, alter the colors, change the theme, the title, the data density—each code modification produces a new authentic sample, with all its metadata already available by construction.

The result is a pipeline capable of expanding almost geometrically. Starting from a relatively small number of seed charts, the system produced over 1.5 million diversified samples, covering 24 chart types (histograms, line charts, pie charts, scatter plots, box plots, heatmaps, and many others) across six different plotting libraries, including Matplotlib, Seaborn, Plotly, and Vega-Altair. An automatic quality control system verifies that each generated sample is executable, rendered correctly, and semantically coherent: they don't just want diversity, but meaningful diversity.

## Five languages for a single chart

The true innovation of ChartNet, however, is not in the quantity; it's in the structure. Each sample in the dataset is not a simple image-label pair: it is a tuple of five elements perfectly aligned with each other—a representation of the same chart in five different "languages."

The first element is the executable plotting code, the source of truth from which everything else derives. The second is the rendered image of the chart, which the model will see during training. The third is the data table with the underlying numerical values, expressed in a structured format. The fourth is a natural language summary describing the patterns, trends, and anomalies visible in the chart. The fifth, available for 632,000 of the core samples (and expanding), is a Q&A pair with an explicit chain-of-thought reasoning chain, showing not only the correct answer but the logical path to get there.

This five-level multimodal structure is not aesthetically pleasing; it is functionally necessary. When a model is trained on this data, it learns not just to "look" at a chart but to relate its visual structure to the numbers it represents, the words that describe it, and the questions that can be asked about it. The cross-alignment between the five components is what researchers call granular cross-modal alignment: the model develops an integrated, not fragmented, understanding.

In addition to the synthetic core, ChartNet includes specialized subsets addressing dimensions often ignored by previous datasets. A subset of 94,643 synthetic charts was verified by human expert annotators, also producing a test set of 2,000 samples with certified quality guarantees: it is the statistical safety net of the entire system. A second subset collects 30,000 real charts extracted from authoritative media and data visualization sources—what's needed to test generalization from the synthetic world to the real world. A third subset includes grounding annotations—Q&A pairs associated with precise bounding boxes on the visual regions of the chart—teaching the model not just what to answer, but where to look. Finally, a subset dedicated to safety addresses the problem of potentially misleading or manipulated charts, a dimension that previous academic datasets almost completely ignored.
![tabella1.jpg](tabella1.jpg)
[Image taken from the official paper on arxiv.org](https://arxiv.org/pdf/2603.27064)

## A 3B beats GPT-4o

The experimental results are the part that raised some eyebrows in the community, and for good reason. The team evaluated the models trained on ChartNet on four main tasks: chart reconstruction (recreating the plotting code from the image), data extraction (recovering the underlying numerical table), summary generation, and Q&A with chain-of-thought reasoning.

The 3-billion parameter Granite 4.0 Vision model, trained with ChartNet, achieved 86.4% accuracy in summary generation (Chart2Summary) on ChartNet's verified human test set, with evaluation conducted via LLM-as-a-judge. This score is the highest among all evaluated models, including significantly larger ones. On the same benchmark, Granite ranked second in data extraction (Chart2CSV) with 62.1%, surpassed only by Qwen3.5-9B with 63.4%, a model more than double its size.

But the data that most struck observers was in the direct comparison with commercial systems. Open-source models trained on ChartNet outperformed models of orders of magnitude larger, including OpenAI's GPT-4o, on all chart interpretation tasks. The concept of "orders of magnitude" here is not rhetorical emphasis: GPT-4o is a model estimated to have hundreds of billions of parameters, while Granite 4.0 Vision has three billion. The ratio is in the order of 100:1 for parameters, with the smaller model winning. This is exactly what Kondic meant when she stated that the project's goal is to demonstrate that state-of-the-art results can be achieved with smaller models that do not require infinite amounts of computation.

The result is not magic; it is consequential: GPT-4o is a generalist model trained on huge amounts of heterogeneous data. Granite, trained on a dataset surgically built for the specific task, can outperform it in that precise niche. It's the difference between a general surgeon and a specialist: in the operating room for that specific procedure, the specialist almost always wins.

ChartNet also improved performance on standard industry public benchmarks, such as ChartQA, FigureQA, and PlotQA, demonstrating that the gains are not limited to the proprietary test set but generalize to independent evaluations.

## Open source, but with reservations

Up to this point, the story seems almost too good to be true. A free dataset, built with scientific rigor, allowing small and inexpensive models to beat commercial giants in chart analysis tasks. For those managing an SME, conducting research without Big Tech funding, or simply not wanting to pay premium provider API fees, ChartNet and the resulting Granite models represent concrete access to capabilities that were effectively locked away.

The [dataset is available on HuggingFace](https://huggingface.co/datasets/ibm-granite/ChartNet), the Granite models are released under an Apache 2.0 license, and the paper is published on arXiv with a CC BY 4.0 license. There are no barriers to access. A professional wishing to integrate Granite Vision today to automatically analyze their company's PDF reports, extract charts, and get summaries and answers to questions can do so on consumer hardware with marginal costs close to zero.

That said, an honest account cannot ignore the project's structural limits.

The most obvious critical point is the synthetic nature of most of the data. Charts generated by automatic pipelines, however diversified and controlled, tend to be visually cleaner, more regular, and more "correct" than charts encountered in reality. A multinational's annual report, a slide from an academic presentation, or a newspaper infographic often has idiosyncratic graphic styles, non-standard fonts, anomalous scales, manual annotations, overlaps, and variable rendering quality. The subset of 30.000 real charts in ChartNet is an attempt to bridge this gap, but it remains a minor fraction of the total dataset. The risk of so-called "distribution shift"—the difference between the distribution of training data and real-world data—is real and recognized by the authors themselves, who have indicated expansion with data of greater complexity as a priority for future versions.

Then there is a question of ecosystem dependence. ChartNet was developed within the MIT-IBM Computing Research Lab, a structured collaboration between MIT and IBM Research, and its most visible results are the models of IBM's Granite family. This is not a flaw, but it is a context to keep in mind: the dataset is open-source, but its development trajectory is influenced by the goals of a large tech company with specific commercial interests in enterprise AI. The independent research community is explicitly invited to contribute, but the balance between community governance and corporate direction remains to be observed over time.

It should also be noted that the most flattering evaluation metrics, such as the 86.4% on Chart2Summary, use an LLM-as-a-judge approach where one language model evaluates the quality of another model's responses. It is an increasingly common methodology but not free from criticism: automatic judges can have systematic preferences, can be less sensitive than human experts to certain types of numerical errors, and absolute scores depend in part on the evaluator's prompt choices. The test set of 2,000 human-verified samples is a partial guarantee, but not a complete validation under real conditions.

The paper will be presented at IEEE CVPR 2026, Computer Vision and Pattern Recognition, one of the world's most important academic conferences in the field of artificial vision. It is the project's seal of scientific legitimacy and brings with it the tradition of peer review that distinguishes academic research from a simple commercial announcement.
![tabella2.jpg](tabella2.jpg)
[Image taken from the official paper on arxiv.org](https://arxiv.org/pdf/2603.27064)

## What changes, concretely

For those reading this article from a practical perspective, the question is: what changes today in my activity thanks to ChartNet?

If you work in a large organization with access to premium commercial models and a dedicated AI team, it's mainly interesting news about research progress. If, however, you are a freelance financial analyst processing dozens of PDF reports monthly, a researcher with a limited budget, or an SME wanting to automate data extraction from presentations and dashboards, then ChartNet opens a concrete door.

A 3-billion parameter model like Granite 4.0 Vision runs on cloud servers with hourly costs of a few cents. The difference compared to GPT-4o via API is not just economic: it's also about latency, data control, and the possibility of fine-tuning on proprietary data. The human-annotated subset in ChartNet is designed precisely for this: to allow anyone to adapt performance to their specific domain, from stock market charts to company performance metrics.

ChartNet demonstrates that in AI, the competitive advantage doesn't necessarily belong to those with more parameters and more computing power, but to those with the right data built in the right way. On specific and well-defined tasks, a small but well-trained model can turn the tables. Sometimes what matters is not being bigger, but being more precise.
