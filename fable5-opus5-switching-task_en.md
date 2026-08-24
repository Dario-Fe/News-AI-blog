---
tags: ["Business", "Generative AI", "Ethics & Society"]
date: 2026-09-07
author: "Dario Ferrero"
---

# Opus 5 Overtakes Fable 5: The End of the Frontier at All Costs
![fable5-opus5-switching-task.jpg](fable5-opus5-switching-task.jpg)

*Two months after its launch, the most powerful and most expensive model in Anthropic's entire catalog accounts for barely 11.4% of corporate spending on the company's products, and only 6% of tokens actually consumed. The data comes from [Ramp](https://aiweekly.co/alerts/ramp-anthropics-fable-5-plateaus-at-11-as-opus-5-overtakes), the corporate spend management platform that analyzed the behavior of 70,000 U.S. companies and shared it with the Financial Times: Claude Fable 5, introduced in early June as the ultimate generational leap, has plateaued into a niche. Meanwhile, Claude Opus 5, launched on July 24 at half the price of its older sibling, has already surpassed it in enterprise spending.*

Anyone who has followed this sector for a while will recognize the pattern. Back in May, discussing the launch of Opus 4.8, I wrote that [the perceived advantage between one flagship model and the next is narrowing with every generation](https://aitalk.it/it/switching-task.html), while the cost to access them remains high: the question, then theoretical, was whether it still made sense to always chase the latest model or if it was more rational to select the tool based on the task. Ramp's numbers now offer an empirical answer to that question, and the answer seems to be: the majority of teams have already started choosing.

## What These Numbers Really Measure (and What They Don't)

Before drawing hasty conclusions, it is worth understanding what we are talking about. Ramp does not publish a peer-reviewed academic report; it measures what passes through its own corporate expense management infrastructure: the share of dollars spent per model and the share of tokens consumed per model, across a sample that naturally leans toward tech companies and developer tools rather than the end consumer chatting with an app on their phone.

A comparison with direct competitors helps contextualize this. OpenAI's GPT-5.6 Sol accounts for 23% of dollar spend and 25% of tokens on the OpenAI platform, shares significantly higher than Fable 5's. Anthropic, it should be noted, still maintains an advantage in overall adoption: 43.5% of U.S. companies tracked by Ramp use at least one Anthropic product, compared to 39.7% using OpenAI. The issue is not the company as a whole—which reached an annualized revenue of $65 billion in July (up from $47 billion in May)—it is specifically the flagship model that has failed to replicate the success of previous flagships.

Why trust this signal despite its methodological limits? Because it measures real spending, not a score obtained in a laboratory on a benchmark that no one will ever use for actual work. This is real money that companies have decided to direct elsewhere.

## Price, Data Retention, and Adoption Friction

The reasons explaining Fable 5's plateau are not just about the model's intelligence. Fable 5 costs $10 per million input tokens and $50 per million output tokens, according to data reported by [Better Stack](https://betterstack.com/community/guides/ai/claude-opus-5/), exactly double the price of Opus 5, which stands at $5 and $25—the same rate as its predecessor Opus 4.8. Added to this is a detail that carries substantial weight for those handling sensitive data: Fable 5 comes with a 30-day data retention requirement that Opus 5, like previous Opus models, does not require for general access.

Ara Kharazian, chief economist at Ramp, put it in rather direct terms speaking with the Financial Times, [noting that Fable 5 has underwhelmed](https://aiweekly.co/node/10679) both in adoption and practical application due to price and data retention requirements, while OpenAI's GPT-5.6 Sol is increasingly becoming the preferred choice for developers. For a company integrating a model into a production pipeline, with legal teams validating every clause on data management, these factors are not technical details; they are real cost items added to the price per token.

## Benchmarks: Where Opus 5 Ties, and Where It Wins

Here the story becomes more interesting, because Opus 5 is not simply "the cheap version" of Fable 5—in several areas, it matches or surpasses it. On [Frontier-Bench v0.1](https://www.anthropic.com/news/claude-opus-5), the benchmark measuring agentic coding capabilities in a terminal, Opus 5 scores 43.3% against Fable 5's 33.7%, nearly a ten-point margin, more than double the result of Opus 4.8. On ARC-AGI-3, the evaluation testing the ability to solve genuinely novel problems rather than items memorized during training, Opus 5 reaches 30.2%—a figure independently verified by the ARC Prize Foundation—compared to the 7.8% previously held as a record by GPT-5.6 Sol.

Independent indices from Artificial Analysis tell a similar story: on the Coding Index, Opus 5 ranks second, just behind GPT-5.6 Sol and ahead of Fable 5; on the Agentic Index, it is first, outperforming both competitors; on the Intelligence Index, it leads the leaderboard with 61 points versus Fable 5's 60. In practical tests conducted by Better Stack, which asked various models to build a 3D racing game with Three.js and a complete financial dashboard from scratch, Opus 5 produced more polished and better-structured results than Fable 5 in both cases, while GPT-5.6 Sol and Kimi K3 lagged behind on essential elements such as including an actual track in the racing game.

There is, however, an important qualification that Better Stack honestly emphasizes: Opus 5 tends to be more verbose than Fable 5 on complex tasks, meaning the "half price" advantage calculated on single tokens narrows when looking at the cost per completed activity. The advantage remains real on average across the benchmark suite, but on a single specific task, it can shrink significantly. It is a useful reminder: price lists only tell half the story.
![immagine1.jpg](immagine1.jpg)
[Screenshot of the article on aiweekly.co](https://aiweekly.co/alerts/ramp-anthropics-fable-5-plateaus-at-11-as-opus-5-overtakes)

## Where Fable 5 Remains Irreplaceable

It would be inaccurate, and rather lazy, to frame this story as a failure of Fable 5. A model that still accounts for billions of dollars in enterprise spend is not a flop; it is a product that has found a narrower niche than Anthropic likely hoped. In cybersecurity, Anthropic itself admits that Opus 5 lags behind Fable 5 in converting identified vulnerabilities into working exploits, even though the two models are now close in simple vulnerability identification.

The case of biology is even more nuanced. Biological research requests that were previously blocked on Fable 5 are now automatically redirected to Opus 5 rather than the older Opus 4.8—a sign that Anthropic considers Opus 5 sufficiently capable and secure for that domain. Dianne Penn, head of product at Anthropic, summarized the positioning logic in an interview reported by [Implicator](https://www.implicator.ai/anthropic-opus-5-overtakes-fable-5-corporate-spending/): customers should choose Opus 5 for everyday value, reserving Fable 5 for "highly autonomous projects lasting several days." It is, plainly put, the same distinction between a general-purpose tool and a specialized instrument that the open model community has been practicing for a long time with its own hierarchy of local and cloud models.

## From Theory to Practice: Cost per Completed Activity, Not per Token

The most counterintuitive figure in this whole affair lies in the discrepancy between Ramp's two percentages: Fable 5 accounts for 11.4% of spend but only 6% of tokens. This means that when companies do choose Fable 5, they do so for tasks where token cost is less critical than the result achieved, or simply that its double-priced tokens cost proportionally more for the same amount of work done. It is precisely the "cost per completed activity" rather than "cost per token" logic that I tried to outline when discussing [Big Pickle](https://aitalk.it/it/switching-task.html), the free, unpretentious model I used to rebuild several static websites without feeling the need to subscribe to a flagship: a cheaper model wins when additional attempts and revisions still cost less than handing every single task to the top-tier model.

Data gathered by Vercel on its model gateway, cited by Implicator, offers an additional nuance: it places Fable 5 at 13.2% of overall spend—a number slightly different from Ramp's but within the same 11–13% order of magnitude—with the news that nine out of ten teams using Fable 5 are doing so for the first time. It is not, therefore, a model abandoned by legacy clients; rather, it is a model struggling to become the daily default for those who already know it.

## The Broader Economy: Who Wins and Who Loses

Looking beyond individual products, the picture reveals something about the entire industry. Miles Clements, a partner at Accel, told the Financial Times, in [Ramp's coverage](https://aiweekly.co/node/10679), that the era where clients automatically chose the flagship model was unsustainable. This statement comes from someone funding these companies, not an outside critic, and sounds like an admission that the release cycle driven by launch announcements—which I had compared to the high-end smartphone release calendar—is finally hitting a real economic boundary imposed by customers, not by the labs producing the models.

It remains to be seen how specific this pattern is to Anthropic versus reflecting broader market dynamics. The fact that GPT-5.6 Sol dominates OpenAI spend so decisively suggests that not all flagships are treated equally by the market: it depends on price, certainly, but also on how distinct that specific model truly is from the tier immediately below it, and how much contractual constraints like data retention weigh on adoption.

## Concrete Use Cases: Where the Gap Is Visible, and Where It Isn't

In enterprise workflow automation, Opus 5 claimed top spot on Zapier's AutomationBench, completing an entire customer churn prevention process—from identifying at-risk accounts to summarizing insights for the retention team—with a 100% success rate where previous models failed, as detailed in [Anthropic's official announcement](https://www.anthropic.com/news/claude-opus-5). On OSWorld 2.0, the benchmark measuring autonomous computer use, Opus 5 surpasses Fable 5's best result at just over one-third of its cost.

On the scientific front, Opus 5 improves over Opus 4.8 across every internal life science evaluation, with particularly marked gains in organic chemistry—ten percentage points higher in inferring molecular structures from spectroscopic data, an area where technical precision matters far more than rhetorical flair. On the legal front, a client cited in the launch announcement reported that Opus 5 maintains quality comparable to Fable 5 while generating 26% fewer tokens at maximum reasoning threshold: less fluff, same result—roughly the AI equivalent of the principle that good editing shows in what gets cut, not what stays.
![immagine2.jpg](immagine2.jpg)
[Image from ft.com](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245?syn-25a6b1a6=1&ref=aisecret.us)

## Security and Policy as Choice Variables

There is a less discussed but operationally relevant aspect: Opus 5's cybersecurity classifiers trigger, according to Anthropic's estimates, about 85% less often than Fable 5's. This means fewer legitimate security research requests blocked by mistake—a very real issue for authorized penetration testers who found themselves having to bypass overly cautious refusals. A clear line remains, however: Opus 5 blocks binary vulnerability scanning and exploit generation, areas where the top-tier Mythos model maintains an advantage that Anthropic considers intentional rather than a technical limitation to be closed in the next version.

## What to Watch in the Coming Months

Several variables will determine whether this is a temporary adjustment or a structural shift in how enterprises purchase artificial intelligence. Ramp's next report will show whether Fable 5's share stabilizes around 11% or declines further as Opus 5 consolidates as the default on Claude Max. It is also worth observing whether Anthropic decides to adjust Fable 5's price or data retention requirements to boost adoption, or accepts that the model will remain reserved for a narrower audience willing to pay for the ultimate margin of capability. Finally, the growth of low-cost open models—which I wrote about regarding DeepSeek V4 and Salvatore Sanfilippo's local inference engine DS4—will likely continue to exert downward pressure on prices, even for mid-tier models like Opus 5 itself.

## Operational Guidance, Not Judgments

For development team leads, the takeaway emerging from the data is to start with Opus 5 as the default model and reserve Fable 5 for tasks genuinely requiring the ultimate margin of available capability or specific security constraints linked to advanced offensive research. For budget and procurement managers, the lesson is to look at the cost per completed activity rather than simple price per token, incorporating data retention and compliance constraints into calculations—factors that rarely appear on price lists but weigh heavily on total cost. For those building autonomous agents, designing explicit routing between models based on task class from day one—with Opus 5 as the default and automatic escalation to more capable models only when needed—appears to be sound practice rather than an optimization to postpone for later.

More open questions remain than certainties offered by this episode. If task-switching solidifies as the new normal, what will it mean for the economic incentive to build ever larger and more expensive models, when the market rewards those who accomplish more with less spend? And if frontier intelligence increasingly becomes a niche product for a few extreme use cases, who will actually fund the next generational leaps—the very leaps that, generation after generation, end up becoming the baseline everyone takes for granted?

---

*Technical note: the spending and adoption data cited in this article originates from Ramp via Financial Times reporting (reprinted by AI Weekly) and relates to a sample of predominantly U.S. companies with a tech-sector bias; it should therefore be read as directional indicators of a trend rather than a comprehensive census of the global enterprise market.*
