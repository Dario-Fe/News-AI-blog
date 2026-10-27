---
tags: ["Generative AI", "Business", "Training"]
date: 2026-11-04
author: "Dario Ferrero"
---

# Timestral-209M: Forecasting Without Prior Training
![timestral.jpg](timestral.jpg)

*Imagine a warehouse with three thousand product SKUs and a manager who, on Monday morning, must decide how many pallets to order, how many workers to call in for the weekend, and which stock levels should never hit zero. Nobody is asking them to read the future. They are asking for something more humble and more useful, a conditional estimate: given what has happened so far, what range of tomorrows is plausible? A good forecast does not point to a single path; it draws the full fan of possible paths and says which ones are most likely.*

*For decades, the job was done in only one way. Classical models, such as ARIMA, assign one model to each time series and learn solely from it: they are inexpensive, easy to interpret, but start from scratch with every new series. Deep learning, for instance with PatchTST, learns from many series together, but typically must be trained from scratch on each dataset, as [Mistral's own blog explains](https://mistral.ai/news/timestral). Foundation models change the recipe: they are pre-trained on a massive corpus and then applied to unseen data without further training. This is called *zero-shot*—zero training attempts on the specific case.*

*On how big this revolution truly is, opinions are more cautious than press releases. Rob Hyndman, one of the most authoritative names in the field, [writes](https://robjhyndman.com/hyndsight/foundation_models.html) that these models represent a real shift in how forecasts are produced, but not yet a general proof of superior accuracy. This article lies between the two positions: it presents Mistral's Timestral-209M, explains how it works, and reports an in-house test on real sales data, honest but without benchmark pretensions.*

*In a single sentence: Timestral is a serious signal that forecasting is becoming general-purpose, but it does not prove that a foundation model always beats a well-calibrated statistical model tailored to a specific case.*

## Anatomy of Timestral

Timestral is a family of four models with 5, 28, 123, and 209 million parameters, [released by Mistral](https://huggingface.co/mistralai/Timestral-209M) in mid-October 2026. Parameters are the internal knobs the model adjusts during training: 209 million is a lot for a classical statistical model, but very few for a modern language model. The format was chosen to run even on a standard CPU, on-premises or in air-gapped environments.

Four numbers from the [official model card](https://huggingface.co/mistralai/Timestral-209M) help explain what it can do. The *context*, meaning how much history the model reads, reaches 32,768 time steps. The *horizon*, meaning how far ahead it looks, is 1,024 steps in a single pass, beyond which it proceeds in blocks, appending its own median prediction as if it were actual history. The *quantiles* are thresholds describing uncertainty: the 0.95 quantile is the value the model expects to be exceeded only five times out of a hundred, and Timestral outputs 21 of them, from 0.01 to 0.99. Finally, it accepts one or multiple series together, along with *covariates*—ancillary information known in advance, such as calendars, prices, or holidays.

The model is a transformer with 24 layers and an internal hidden dimension of 768, which does not read values one by one, but in *patches*—chunks of 32 steps, each accompanied by an indicator for missing data gaps. It combines two types of attention, that is, the ability to weigh which information matters: temporal attention, which looks at which past moments are relevant, and cross-variable attention, which looks at how series influence each other. According to the [blog](https://mistral.ai/news/timestral), the method called DHF keeps the entire history visible and adds separate prediction tokens, so every observed value serves both as a target and as context. Covariate attention, meanwhile, only allows information flow from covariates toward targets, preventing a series's future from contaminating its own forecast.

The most surprising part is training: most of the data is synthetic—processes with artificial trends, seasonality, and noise, generated in a first phase with an 8,192-step context, followed by a second phase combining real and synthetic data with a context four times longer. It is the opposite of Funes the Memorious, Borges' character who remembers every leaf on every tree and precisely for that reason cannot generalize: here, the shapes of time are taught, not individual events. What exactly is contained in the real-world corpus is not disclosed. The technical report is announced as "coming soon."

Two practical reminders. The status is [public preview](https://docs.mistral.ai/models/timestral-1-0-209m). The [license](https://huggingface.co/mistralai/Timestral-209M/blob/main/LICENSE), a modified MIT license, is not open source in the strict sense: it denies use to any entity or employer with over $20 million in consolidated global monthly revenue in the preceding month, unless a commercial agreement is made with Mistral. It is not a royalty, but an entry threshold, and applies to derivative works as well.

## Promises to Verify

Mistral claims that Timestral-209M ranks first among pre-trained, zero-shot models across three public leaderboards: [GIFT-Eval](https://huggingface.co/spaces/Salesforce/GIFT-Eval), [TIME](https://huggingface.co/spaces/Real-TSF/TIME-leaderboard), and [fev-bench](https://huggingface.co/spaces/autogluon/fev-bench), beating the previous state of the art with two-thirds of the parameters. On the model card, the numbers are: on GIFT-Eval, the MASE error is 0.658 versus t0-gamma's 0.661, and CRPS is 0.446 versus 0.452. MASE measures error relative to a naive baseline, while CRPS evaluates the quality of the entire predicted distribution—for both, lower is better. On fev-bench, the SQL score is 50.39 against t0-gamma's 49.42. The margins are real but small, and these are manufacturer-declared results: Mistral releases the [code](https://github.com/mistralai/timestral) precisely to reproduce them, but an independent replication is not yet available.

On efficiency, the statement is specific. On an 8-thread server CPU, forecasting one day ahead starting from three weeks of 15-minute historical data takes 10 milliseconds with the 5M parameter model and 140 ms with the 209M version. The 28M version is five times faster, while the 123M remains within 0.2% of the top score at three-quarters of the latency. These are measurements taken under precise conditions, different from our test, and should be read as such.

Then there is the underlying issue with leaderboards, where Hyndman is helpful. He references [analyses by Christoph Bergmeir](https://cbergmeir.com/papers/Bergmeir2024LLMs.pdf), which show that comparisons with statistical methods are often conducted using poorly tuned baseline versions. He also cites the study by [Meyer and colleagues](https://arxiv.org/abs/2510.13654v3): out of 401 datasets used by 22 published foundation models, only 6% had never appeared in the training data of any model. Anyone who has watched the cult film *Primer* knows what happens when information travels back in time without anyone noticing. Mistral itself acknowledges the problem: its [Forge](https://mistral.ai/products/forge/) platform promises full control over training data, ensuring that nothing tested on your own historical data has already been seen by the model.
![tabella1.jpg](tabella1.jpg)
*Screenshot of the dashboard showing an overview of our test results.*

## How We Conducted the Test

The test is not a single experiment, but a small chain of steps: starting from original files, preparing data, generating forecasts, comparing them with ground truth, and producing numbers, reports, and charts. Each step saves its result to disk, and the next step picks up from there. This makes the work verifiable and repeatable, allowing it to be interrupted without losing progress. The sequence is as follows.

**1. A closed environment.**

First, we confined the experiment to a single project folder. The launch script creates a local Python environment (.venv), installs dependencies there, and routes cache, temporary files, and credentials inside the project directory, so nothing touches system folders. The M5 dataset is downloaded from Kaggle, and the three required files—sales, calendar, and prices—are copied into data/raw/m5/. The Timestral-209M model is downloaded once from Hugging Face and saved in models/timestral/. If files are already present, they are reused. An automated test checks that directories, caches, and paths remain strictly within the project.

**2. Data preparation.**

With the three local files in place, we built the test dataset. Out of over 30,000 product-store series, we selected 300 using stratified random sampling (seed 42): 120 high-volume, 120 medium-volume, and 60 low-volume or intermittent series. Volume is measured solely on the oldest historical window, so selection does not depend on the future. Series with zero sales in that window were excluded; missing days were filled with zeros, making every series a continuous daily sequence, one row per day. For each series, we added information known in advance: day of the week, month, weekend indicator, events, SNAP days, and price—the latter only if available for all series across the full horizon. The result is saved in Parquet, a fast, compressed format.

**3. Temporal split.**

We then split the timeline into three consecutive 28-day windows, from February 1 to April 24, 2016. For each window, we kept 365 days of history and set aside the 28 days to forecast: those ground-truth values were never fed into the forecasting phase, only into evaluation. The windows are February 1–28, February 29–March 27, and March 28–April 24. The code records window dates in a configuration file and verifies that forecasts cover exactly the expected 28 days. Three windows instead of one ensure results do not depend on a single specific month: if performance holds across all three, it is far more credible.

**4. Zero-shot inference.**

Here the model takes the stage. We load Timestral-209M from local files without further training, processing one series at a time. For each series, we feed 365 days of sales and known covariates for the entire period—365 past days plus 28 future days. The model outputs the 28 days as five quantiles (5%, 25%, 50%, 75%, 95%). Forecasts are computed in batches of eight series on CPU in inference-only mode; negative values are clipped to zero because sales cannot be negative. Every output is saved with series ID, date, window, quantiles, and compute time. If execution stops, the script resumes from missing series.

**5. Evaluation and comparison.**

Once forecasts are fixed, we join them with actual ground-truth values for the 28 days and compute metrics: MAE, RMSE, WAPE, MASE, bias, pinball loss, coverage, and interval width. We do the same with a simple baseline: naive seasonal forecasting, which repeats the value from the same day of the previous week. Metrics are aggregated per series, volume tier, window, and overall; 95% confidence intervals are computed using 1,000 resamplings of the series. Results are saved in six CSV files: series-level, aggregate, baseline, tier-level, confidence intervals, and summary. The point forecast used for MAE, RMSE, WAPE, and bias is the median.

**6. Report and dashboard.**

The final step turns numbers into readable artifacts. A module automatically generates a Markdown report with objectives, dataset, protocol, metrics, baseline comparisons, best/worst cases, and limitations. A Streamlit dashboard reads the same files and displays four tabs: overview, series-by-series, aggregate analysis, and narrative report. Charts are rendered using Plotly, showing history, ground truth, median predictions, and 50% and 90% uncertainty bands. Everything regenerates with a single command: the launch script runs the pipeline and launches the dashboard.

This is the purpose of the pipeline: not merely describing a model, but making an experiment verifiable. The pipeline consists of explicit choices (which series, how much history, which variables, which baseline), and each can be inspected, re-run, or challenged. The numbers that follow are worth as much as the process that produced them: for this reason, the temporal split—decided before seeing any results—is the step that gives meaning to all the rest.
![grafico1.jpg](grafico1.jpg)
*Screenshot of the dashboard; the final section compares ground truth against Timestral's predictions.*

## The Test on M5

An honest disclaimer: this is an in-house test, not a formal benchmark, and it is not independent in the academic sense. [M5](https://www.kaggle.com/competitions/m5-forecasting-accuracy) is a forecasting competition on Walmart unit sales, featuring 30,490 product-store series and 1,941 days between 2011 and 2016. The competition's official metric, WRMSSE, is not calculated here, so results cannot be directly compared to the original leaderboard.

We extracted 300 series via stratified random sampling (seed 42): 120 high-volume, 120 medium-volume, and 60 low-volume or intermittent, with tier thresholds calculated solely on the oldest historical period to prevent sample selection from depending on the target future. Zero-volume series were excluded, missing days set to zero. Three consecutive 28-day windows from February 1 to April 24, 2016, each with 365 days of history. The model operated zero-shot in univariate mode on CPU, with covariates known in advance: day of the week, month, weekend, events, SNAP days (food stamps), and price (assumed known across the entire horizon). No promotions, inventory, or weather data were included. The baseline is naive seasonal forecasting, repeating the same day of the previous week. Ground-truth future values were never passed to the model, and predictions were clipped to zero.

## Examining the Numbers
![tabella2.jpg](tabella2.jpg)

MAE is the mean absolute error in units sold per day per series; RMSE penalizes larger errors more heavily. WAPE is total error divided by total sales: it is important to clarify that 0.6348 does not mean "63% accuracy"—it means an error equal to 63% of total sales volume. MASE compares error against the mean error of a naive method on history: 0.80 versus 1.11 for naive seasonal on the same scale. Relative to the baseline, WAPE improves by 23.45%, MAE by 23.46%, RMSE by 19.54%, and MASE by 27.70%. The improvement direction is consistent across all three windows, with WAPEs of 0.6728, 0.6165, and 0.6154.

It must be interpreted cautiously. The 95% confidence intervals from resampling give a WAPE range of 0.5883–0.6917 versus 0.7610–0.9059 for naive—well separated. For RMSE, ranges are 2.2543–4.9287 versus 2.7815–5.6903, heavily overlapping, and MAE nearly overlaps: on these two metrics, a statistical lead is not proven. Furthermore, confidence intervals reflect variability across series, not across time periods.

Bias deserves attention. It measures signed mean error, and −0.5632 indicates systematic underestimation: on average sales of about two units per day (derived from the MAE/WAPE ratio), this is nearly 28%, compared to −0.025 for naive forecasting. It accounts for about 45% of MAE. For inventory managers, this is the worst kind of defect, as it leads to stockouts. The report does not specify which point forecast was used: if it was the median on series with many zeros, that would be a plausible explanation, but remains a hypothesis to verify.

Prediction intervals are conservative. The 90% interval achieves 93.30% coverage—containing ground truth more often than expected—and the 50% interval hits 62.62%, twelve points above nominal, with an average 90% width of 5.40 units, more than double average sales. On discrete, zero-heavy data, coverage is naturally inflated, and without an equivalent probabilistic baseline, we cannot tell if intervals are good or simply wide.

Breaking results down by volume reveals further nuances. On the 120 high-volume series (~4 units/day), WAPE is 0.5845 versus 0.7518—a 22.25% improvement. On medium volume (~0.8 units/day), it is 0.8708 versus 1.1684 (+25.47%). On the 60 intermittent series (~0.13 units/day), WAPE is 1.0069 versus 1.6956, a 40.62% improvement that is nevertheless misleading: a WAPE above 1 is worse than predicting all zeros, and the naive baseline starts from a terrible benchmark. Here, MASE and pinball loss (quantile error, averaging 0.4066 for Timestral) are more reliable.

Individual cases are more instructive than averages. The best case by WAPE is FOODS\_3\_042\_WI\_1 (0.1975, MASE 0.5069), but another "top" performer, FOODS\_3\_329\_CA\_1, has a MASE of 1.4251, worse than naive: metrics can contradict each other. The worst performer, HOUSEHOLD\_2\_124\_TX\_2, has a WAPE of 26.22 because it sells roughly 0.012 units per day—virtually nothing. In FOODS\_1\_110\_WI\_1, all error stems from overestimation, likely a discontinued product or an out-of-stock item. Zeros in M5 do not always signify absent demand.

Limitations remain as stated: 300 series out of 30,000+, 84 days without structural shifts, no promotional covariates, a single simple baseline, and no comparison against ARIMA, ETS, or other foundation models. Regarding contamination, M5 has been public since 2020, so we cannot rule out its presence in training data. The conclusion is not that "Timestral is the best on M5," but that it consistently beats a naive rule within clear boundaries.

In plain English: in this test, Timestral predicted sales for the final month better than repeating the previous week's values, with about a quarter less error (WAPE 0.63 vs 0.83) and consistent gains across all three windows. However, its lead is solid primarily on overall error and MASE, whereas on MAE and RMSE confidence intervals overlap, leaving its superiority unproven. There remains a systematic underestimation of ~28%—the most hazardous flaw for inventory planning—and forecasts are far more reliable on high-volume products than on intermittent items where zeros blur the line between zero demand and missing stock. In summary: a solid zero-shot result, clearly better than an elementary baseline, but not definitive proof that Timestral is the go-to model for M5-like datasets.

## Who Should Use It, Who Should Not

In its blog, Mistral cites use cases such as industrial sensors, financial flows and volumes, energy, supply chain planning, and system observability metrics. Retail trade is covered here only by our test. In settings with many series, limited statistical resources, and covariate-rich data, the value is obvious: a single pre-trained model avoids building and maintaining a pipeline for every individual series. On the [model card](https://huggingface.co/mistralai/Timestral-209M), Timestral slightly leads Chronos-2, TimesFM-3, Toto-2.0 (2.5B parameter version), and t0-gamma, making it an open race. Furthermore, Mistral reports that its 28M model beats Chronos-2 (roughly four times larger) on GIFT-Eval and TIME.

It is less useful in cases that common sense and Hyndman point out: few series, known causal relationships, mandatory explainability, scarce data, or lack of expertise to maintain a model in production. [His advice](https://robjhyndman.com/hyndsight/foundation_models.html) boils down to three steps: start with a well-built statistical baseline, test on your own data with rolling windows without trusting external leaderboards, and weigh total cost—compute, latency, vendor lock-in, and low interpretability. Added to this is the license, which legal counsel should review before building a commercial product on top of it.

## More Accessible, Not Magical

The bottleneck is shifting: less about model selection, more about data quality, monitoring bias and coverage, and governing covariates and licenses. On-premises deployment with local logs and auditability offers a compelling argument for organizations unable to send data offsite.

Four things to monitor in the coming months: the technical report release, independent result replications, production case studies, and rigorous comparisons against alternatives—including statistical ones. Until then, Timestral is a strong signal, not final proof. In our test, it beats a naive rule by 23% on WAPE, but underpredicts, exhibits wide prediction intervals, and was evaluated on a limited sample.

Forecasting has not become magic. It has become more accessible.
