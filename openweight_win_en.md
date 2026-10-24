---
tags: ["Business", "Generative AI", "Applications"]
date: 2026-11-06
author: "Dario Ferrero"
---

# Open Weights, True Cost
![openweight_win.jpg](openweight_win.jpg)

*A token is a word fragment, the core unit by which a language model's work is measured and billed. In September's tracking data from [Vercel's AI Gateway](https://vercel.com/blog/ai-gateway-production-index-october-2026), over seven out of ten tokens were processed by open-weight models—those downloadable, inspectable, and hostable by anyone with the necessary hardware. Expenditure tells a different story: those same models accounted for just 23% of revenue, slightly less than one in four dollars. That figure stood at one in twenty back in June, so growth is undeniable, but dollars lag far behind token volume.*

This is not an ideological triumph, and that is precisely what interests me. It is a pricing decision, made by people paying for tokens with the cold calculation of the merchant Lawrence in Isuna Hasekura's novel series *Spice and Wolf*, weighing margins and risks before accepting an offer that looks overly generous. When tokens cost so little, one naturally wonders why more organizations don't host them locally. The gateway, however, cannot observe what happens on personal computers, so how many actually run models on-premise remains an open question. What we can do, however, is evaluate the economics when you do.

Here is the trajectory: gateway metrics, three models interpreting openness in distinct ways, local testing on a 16 GB graphics card, and finally the bottom-line accounting, disclosing every flaw and assumption transparently.

## What Vercel Is Truly Measuring

This dataset reflects real production traffic, not a survey. Every month, Vercel writes, tens of trillions of tokens pass through its gateway across production apps and test labs. The count includes input, output, reasoning tokens, cached read tokens, and cached write tokens. Spend is estimated at public list prices, with the caveat that actual negotiated invoices may differ. The classification of open models aligns with the gateway's current index, representing a broader scope than earlier reports, as explained in their [methodology note](https://vercel.com/ai-gateway/leaderboards/about).

Three limitations warrant immediate disclosure. Vercel's user base represents a specific market segment, and how closely it reflects the broader industry remains unverified. Public pricing ignores enterprise discounts and volume contracts. Substantially different workloads are aggregated into the same total. Nonetheless, it remains one of the very few public datasets tracking token volume and dollar spend side-by-side on the exact same perimeter, making it invaluable.

## The Price Hidden in the Numbers
![tabella1.jpg](tabella1.jpg)

Dividing spend share by token share yields an implicit average price. For open models, 0.23 divided by 0.715 equals roughly 0.32. For proprietary models, 0.77 divided by 0.285 equals roughly 2.70. The former represents 12% of the latter. This is my calculation, not Vercel's, blending disparate models and tasks, making it an order of magnitude rather than an exchange rate. Yet it explains the paradox: an open token costs, on average, about one-eighth as much as a closed one.

Growth is asymmetric. Since last December, spend on frontier closed models grew tenfold, while open model spend surged over seventyfold. Proprietary models capture higher revenue, but on an increasingly smaller fraction of each customer's overall token volume.

The data point complicating the simple "open equals cheap" narrative is Kimi K3. According to Vercel, open models priced at least four times above average accounted for two-thirds of the open spend increase, with K3 alone driving nearly half of that surge despite processing far fewer tokens than DeepSeek. Moonshot, the lab behind K3, accounts for 3.6% of tokens and 13.2% of spend. Dividing those figures indicates its tokens cost ~3.7x the gateway average, while DeepSeek—processing 58% of tokens for 6.6% of spend—costs about one-ninth (again, my calculations). K3 has public weights on [Hugging Face](https://huggingface.co/moonshotai/Kimi-K3), featuring 2.8 trillion total parameters with 104 billion active per token, and according to [published pricing](https://benchlm.ai/moonshot/api-pricing), its API costs $3.00 per million input tokens and $15.00 per million output tokens. On a 9:1 input-to-output blend, that equals $4.20 per million tokens, compared to $2.80 for [Claude Sonnet 5.5](https://www.anthropic.com/pricing). An open model priced higher than a frontier closed one: perhaps the key variable isn't weight open-sourcing, but sheer capability.

Geography adds another layer. Nearly 70% of spend on Chinese models flows through US-hosted API providers, and nine out of ten Moonshot tokens are served by American infrastructure providers. The entity training the model and the entity capturing revenue can be completely different—raising the question of who truly wins from open weights: those who release them, or those who host them?

Finally, TypeSafe AI's Jev reached 35.3% of paying teams within two weeks—a gateway record—yet accounted for just 0.27% of spend during that window, and 1% of tokens for 0.15% of spend in September. As Vercel notes, Jev is a specialized System One decision model that consumes a tiny fraction of the tokens required by a full language model request. Adoption does not equal revenue.

## Three Strategies and an Outlier

**DeepSeek V4.1 Flash** features MIT-licensed weights and a Mixture-of-Experts architecture: its [model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) describes a 552-billion parameter backbone with 8 billion active parameters for reads and 16 billion for writes, alongside a 1-million-token context window. The repository lists ~763B total parameters, meaning no 16 GB consumer card will ever host it locally. Official API pricing is $0.15 input / $0.60 output per million tokens ($0.003 for cached inputs). Vercel measured the September version, while API endpoints now serve the 1017 revision. Here, pricing makes bigger headlines than benchmark scores.

**Mercury 3**, by Inception, generates text in parallel rather than token-by-token, claiming speeds exceeding 1,000 tokens per second. Per its [October 19 announcement](https://www.inceptionlabs.ai/blog/introducing-mercury-3), list pricing stands at $0.20 input / $0.70 output (halved during launch). The page leaves the model license unspecified, and comparisons against Luna and Haiku originate from the vendor. It demonstrates that faster generation does not automatically mean lower prices.

**MiniMax M3.1 Flash**, released the same day, is priced at [$0.15 input / $0.60 output](https://www.minimax.io/blog/minimax-m31f), with $0.015 for cached hits. The company states weights will be released later, without specifying a date or license. That represents an open-sourcing commitment with an unanchored timeline—raising the question of whether openness is also being leveraged as a commercial marketing hook.

The outlier consists of decision-first models like Jev. Cloudflare recently unveiled a related model, [Clairic](https://blog.cloudflare.com/clairic-extraction-model)—a single-pass extraction model that generates no tokens, charging exclusively per input. Cloudflare claims a pipeline incorporating Clairic costs 49% less and runs 3x faster than a pipeline built solely on LLMs (internal vendor benchmark). Weights are promised "soon." If workloads shift toward models emitting minimal tokens, how relevant will tracking the market in tokens remain?

Perhaps open weights have won primarily where tasks are structured, repeatable, and verifiable: extraction, classification, routing. That premise remains to be tested.

## The Test Bench

Our test machine consists of an AMD Ryzen 7 7700, 32 GB DDR5 RAM, and a 16 GB Radeon RX 9060 XT. The tested model is Liquid's [LFM2.5-24B-A2B](https://docs.liquid.ai/lfm/models/lfm25-24b-a2b), in the 15.4 GB UD-Q4_K_XL Unsloth quantization, executed via LM Studio. It possesses 24 billion total parameters with ~2.45 billion active per token, generating explicit reasoning before every answer. Across ten test prompts, eight were valid with an average score of 4.3 out of 5. The remaining two required multimodal input (unsupported by this text-only model) and were excluded as non-applicable rather than failures. The score indicates practical usability; it is not factored into cost calculations.

I measured output generation speed directly: 44.7 tokens per second. Three other variables are estimates, disclosed transparently as such.

Prompt processing speed (*prefill*) is vastly faster than generation writing speed, heavily impacting total cost because nine out of ten tokens in production workloads are input tokens. I did not measure prefill directly. Instead, I analyzed three independent reference points to derive a prefill-to-generation ratio. On an RTX 4060 Ti 16 GB with the same model, [llamabench](https://llamabench.ai/?mode=tune&model=lfm2-5-24b-a2b) reports 4,073 tokens/sec prefill vs. 131 tokens/sec generation (October 16), a ratio of ~31:1. For my specific GPU, [a guide](https://bestllmfor.com/guide/llm-radeon-rx-9060-xt/) cites llama.cpp community benchmarks showing 1,420 vs. 68 t/s on a 7B model (~21:1 ratio). A [27B Qwen3.8 model](https://huggingface.co/vmarcelo/Qwen3.8-27B-MIX_GGUF) on an RX 9070 XT with LM Studio achieves ~638 vs. 33 t/s (~19:1 ratio). Applied to my 44.7 t/s generation speed, these yields an estimated prefill speed of 860 to 1,390 tokens/sec. I use 1,100 t/s as the central baseline estimate (range 900–1,400).

Power draw is the second estimate. [AMD](https://www.amd.com/en/products/graphics/desktops/radeon/9000-series/amd-radeon-rx-9060xt.html) lists 160 watts typical board power for the GPU alone. Lacking an inline power meter, I model two scenarios: 160 watts (GPU-only workload) and 250 watts (estimated full system load). Electricity cost is calculated at €0.3163 per kWh, reflecting the [ARERA benchmark rate](https://quifinanza.it/economia/aumento-costi-bollette-luglio-2026/1006324/) for protected Italian residential customers including taxes. Deregulated market contracts vary above or below this figure.

Input/output token ratio is the third estimate. Rather than using prompt-specific test lengths, this reflects real-world production traces. A [study analyzing 6.1 billion requests](https://arxiv.org/html/2608.13573v2) observed a 14.2:1 input-to-output ratio, [Requesty's analysis](https://www.requesty.ai/blog/context-window-new-battleground-input-output-ratio) reports 19:1, and an [OpenRouter data analysis](https://aifoc.us/the-token-salary/) found 93.4% input tokens for coding workloads. These reflect developer and agentic usage. I adopt a conservative 90% input / 10% output split (9:1 ratio), noting that reasoning models emit higher output volume.

## The Line-by-Line Accounting

Consider a processing batch of one million tokens: 900,000 input tokens and 100,000 output tokens. The local setup requires ~818 seconds for prefill and 2,237 seconds for generation—totaling 51 minutes of active execution time. Total energy consumed spans 0.136 to 0.212 kWh, costing between 4.3 and 6.7 euro cents. Accounting for prefill rate, power draw, and utility rate variations, the full cost range spans 4 to 8 cents per million tokens. Cloud prices reflect standard tier list pricing for short contexts, converted at €0.8917 per USD (ECB reference rate as of October 20).
![tabella2.jpg](tabella2.jpg)

API pricing stems from official list prices for [Anthropic](https://www.anthropic.com/pricing), [OpenAI](https://platform.openai.com/docs/pricing), [DeepInfra](https://deepinfra.com/pricing), and [Liquid](https://www.liquid.ai/pricing). Prompts exceeding 100k tokens on Claude Haiku incur higher tier rates, so short context assumptions apply.

The fairest comparison pits local execution against cloud models of similar size: local execution is 2x to 3x cheaper than cloud hosting for equivalent parameters, a margin that narrows at higher system wattage. Comparisons against frontier models (showing 10x to 100x cost differentials) hold true only on paper. Comparing a model with 2.45B active parameters against frontier systems compares entirely different capability classes, and our quality evaluation does not place them on equal footing.
![tabella3.jpg](tabella3.jpg)

*Euros per million tokens, 90:10 input/output split, €0.3163/kWh. At €0.3557/kWh, local costs rise 12%. At a 95:5 split with 1,100 t/s prefill, local costs drop to ~€0.028 and €0.044.*

Calculations invert if all tokens are processed at generation speed without prefill acceleration: execution takes 6.2 hours, costing 31 to 49 cents—higher than hosted DeepSeek. This represents the most instructive insight of the test: prompt prefill acceleration fundamentally alters the cost equation.

Finally, prompt caching alters the balance. All cloud figures above assume zero cache hits, whereas in repetitive agentic workflows, input context can be cached at steep discounts: $0.003 for DeepSeek, $0.10 for Sonnet 5.5. Assuming an 80% prompt cache hit rate (excluding cache write costs), effective cost drops to ~€0.08 for DeepSeek, €1.30 for Sonnet, and €6.20 for Fable. Under those conditions, local self-hosting at 250W and hosted DeepSeek achieve virtual cost parity. How frequently prompt caching applies in real-world workloads remains an open operational question.

## Hidden Costs Beyond Tokens

The accounting above reflects energy alone. The underlying hardware (GPU + system) costs ~€1,300: amortized over three years, capital depreciation equals ~€36 per month. Running continuously at 100% duty cycle, the system can process ~860 million tokens per month, adding €0.04 in hardware depreciation per million tokens. At a 10% duty cycle, depreciation adds €0.42 per million tokens. At a 1% duty cycle, hardware depreciation exceeds €4.00 per million tokens. The true cost of local hosting depends heavily on utilization rates.

Then comes time—not operator labor, but execution wall-clock time: 51 minutes per million tokens means the machine is occupied, individual request latency spans tens of seconds, and human oversight remains necessary. Add maintenance overhead: updating drivers and LM Studio, sourcing new quantizations, and managing model obsolescence.

Open licensing also contains clauses. Liquid grants free commercial use only to entities generating under $10M in annual revenue. Kimi K3's license requires separate commercial agreements for hosting providers generating over $20M, per [published analysis](https://www.unite.ai/?p=441945), with full terms in their repository. DeepSeek operates under MIT. "Open" spans many spectrums; reading the license before checking list prices is essential.

## One Hundred Billion Parameters on a Phone

Cristiano Amon, CEO of Qualcomm, stated in an interview reported by [The Next Web](https://thenextweb.com/news/qualcomm-cristiano-amon-ai-companies-phones-2028) that leading AI companies want 100B+ parameter models running locally on smartphones by 2028. He named no companies, and how strongly industry pushes in that direction remains unverified. A back-of-the-envelope calculation: at 4 bits per parameter, a 100B model requires ~50 GB of storage for weights alone. RAM, memory bandwidth, thermal dissipation, and battery capacity present real hardware bottlenecks, and mobile operating systems consume a significant memory fraction.

Should that materialize, marginal token costs for end users would drop near zero, shifting the bill entirely to silicon—the retail price of the smartphone. What would be lacking then is the economics of the device rather than the model size.

## Open Questions

This single test is illustrative rather than definitive. Vercel's gateway represents a slice of the market, not the entire industry. An extraction token and a reasoning token do not deliver equal value. I evaluated a single model on a single GPU across eight valid test prompts; this is not a comprehensive leaderboard. Public API list prices ignore volume tiers, prompt caching, and custom enterprise contracts. Prefill speeds and system wattage are modeled estimates. Finally, my generation speed of 44.7 t/s fell below the 131 t/s reported elsewhere for similar 16 GB hardware—a variance potentially tied to context length or VRAM allocation overhead.

Key questions remain open. Will price-per-token remain the defining metric, or will price-per-successful-task replace it? Who truly captures value from open weights—those who release them, those who host them, or those who consume them? And if 100B models move to client devices, who will pay for the energy and execution time?

In Ursula K. Le Guin's story of Omelas, a city's prosperity depends on a hidden cost nobody wants to face. With open-weight models, the trade-off is less grim, but the fundamental question endures: who pays the bill, and where is it written down?
