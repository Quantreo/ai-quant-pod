---
type: reading-note
source: paper
title: Seasonality in the Cross-Section of Cryptocurrency Returns
authors: Long, Zaremba, Demir, Szczygielski, Vasenin
affiliations: Zhejiang University; Poznan University of Economics and Business; University of Dubai; Istanbul Medeniyet University; Northumbria University; University of Pretoria; University of Social Sciences, Lodz
year: 2020
venue: Finance Research Letters 35, 101566
doi: 10.1016/j.frl.2020.101566
pdf: "[[2020 - Long Zaremba Demir et al - Seasonality in the Cross-Section of Cryptocurrency Returns.pdf]]"
version: published (open access)
tier: 1
read: full
tags: [seasonality-flows, crypto, daily]
date: 2026-10-24
---

# Cross-sectional seasonality in crypto (Long et al. 2020)

## Summary

- **Finding**: coins with the highest average same-weekday return over the past 20 weeks beat those with the lowest by 0.31% a day equal-weighted, 0.43% value-weighted, gross (Table 2).
- **Mechanism**: borrowed from equities: behavioural mispricing, recurring demand by weekday (sentiment, flows, trading patterns). Not tested; the authors list the mechanism as an open question (p. 2, 7).
- **Where it works best**: value-weighted long-short, three-factor alpha 0.45% a day (t = 2.26). Low-SEAS quintile carries a negative alpha (-0.40%) (Table 2).
- **Weak spots**: t-stats only around 2.0 to 2.3 for the long-short. No middle quintile is significant. Robustness tests are not reported (Table A2 online, "available upon request").
- **Main caveats**: universe picked by market cap on 16 Dec 2019, the end of the sample. No costs. Short sample (Aug 2016 to Dec 2019), admitted by the authors.

Page numbers follow the journal pagination (1 to 8 of article 101566). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Seasonal shifts in demand for risky assets push prices away from fundamentals on given weekdays | Literature only (Keloharju et al. 2019; Hirshleifer et al.; Heston et al.; Bogousslavsky) | p. 2 |
| 2 | Same biases exist in every asset class, so the pattern should appear in crypto | Argument, then the test of the paper | p. 2 |
| 3 | SEAS works through the same weekday, not general past returns | SEAS stays significant with MOM in the regression; MOM coefficient is negative | Table 3; p. 5 |

**Caveats raised by the authors**
- "The exact mechanism" in crypto is an unanswered question (p. 7).
- How practitioners can exploit it is also left open (p. 7).

**Ruled out**
- SEAS as another anomaly "in disguise": significant with BETA, MV, MOM, TURN, IVOL, ILLIQ controls, alone or together (Table 3, p. 5).
- Exposure to MKT, SMB, UMD: long-short loadings small or insignificant (Table 2).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Bitcoin plus the next 150 coins by market cap on 16 Dec 2019. Requires at least 20 coins on a day. Drops non-positive market value or turnover and prices at or below 0.005 USD. Average 68 coins a day. | p. 2-3, Table 1 note |
| Period | 5 Aug 2016 to 16 Dec 2019, daily | p. 2-3 |
| Signal | SEAS = mean log return on the same weekday over the last 20 weeks (days t-7, t-14, ..., t-140) | Eq. 1, p. 3 |
| Entry | Rank every day, quintiles | p. 3 |
| Exit | Hold one day | p. 3 |
| Horizon | Daily | p. 3 |
| Sizing | Equal weight and value weight | p. 3 |
| Portfolio | Long top quintile, short bottom quintile | p. 3 |
| Rebalancing | Daily | p. 3 |
| Costs | Not stated by the authors | |
| Data and tools | CoinMarketCap daily USD closes; factor models with 1, 3 and 7 factors built as value-weighted quintile long-shorts; Fama-MacBeth with Newey-West t-stats | p. 2-4 |

**Rule** (Eq. 1, p. 3): SEAS(i,t) = (1/20) x (R(i,t-7) + R(i,t-14) + ... + R(i,t-140)). Each day, long the quintile with the highest SEAS, short the lowest, hold one day.

**Data provenance**
- Coin list fixed by size at the end of the sample (16 Dec 2019) and applied back to 2016 (p. 2).
- Coin count grows from ≈ 20 in Aug 2016 to ≈ 115 in late 2019 (Fig. 1, Panel A).
- Control variables: MOM is mean daily return t-140 to t-2; BETA and IVOL from a 20-week one-factor regression; TURN over 20 weeks; ILLIQ (Amihud) over weeks t-10 to t-1 (p. 3).

## 3. Results

All results are real data, in-sample, gross of costs.

**Aggregate** (Table 2)
- Equal-weighted H-L: 0.31% a day (t = 2.05), vol 5.03%. Alphas 0.31%, 0.30%, 0.30% for the 1, 3, 7-factor models.
- Value-weighted H-L: 0.43% a day (t = 2.06), vol 7.18%. Alphas 0.45%, 0.45%, 0.43%.
- Regressions (Table 3): SEAS slope 0.060 (t = 2.32) alone on raw returns, 0.053 (t = 2.04) on risk-adjusted. R² 3.55%.

**By sub-group**
- Short leg: Low quintile alpha F3 -0.27% (EW, t = -2.82) and -0.40% (VW, t = -2.75). High quintile alphas not significant (0.03% and 0.06%) (Table 2).
- Long-short loadings: VW has βMKT -0.14 (t = -2.11) and βTURN 0.11 (t = 2.00). EW loadings all insignificant (Table 2).
- By coin, by weekday: not shown (only "Table A2" online).

**Horizon and parameters**
- Robustness listed but not shown: decile and tercile sorts, top 20 or 30 coins only, trimming 10% largest and smallest, excluding Bitcoin, minimum price 0.1 to 0.4 USD, 10-week window, half samples, excluding each weekday (p. 5-6). Results "do not contradict" the baseline (p. 6).
- UMD formation of 5, 10, 25, 52 weeks does not change the findings qualitatively (fn 6).

**Over time**
- Not shown in the article. Subperiod split is in the online appendix only (p. 6).
- Market value of the sample peaks ≈ 700 bn USD around January 2018 (Fig. 1, Panel B).

**Link to other strategies**
- MOM negatively predicts returns once SEAS is in the regression: -0.354 (t = -3.79) (Table 3, spec 4).
- Pearson correlation of SEAS with MOM 0.240 (Table 1, Panel B).

**Inconsistencies in the source**
- Table 3, Panel A: SEAS in spec (8) is 0.094 with one star but t = 3.30; spec (7) is 0.068 with one star and t = 2.60. Stars and t-stats disagree with the stated levels.
- Table 3, Panel B, spec (7): SEAS coefficient 0.006 with t = 2.34, an order of magnitude below the other columns (0.049 to 0.079).
- p. 5 says SEAS in spec (8) has "a t-value exceeding 2.77". Table 3 gives 3.30 (Panel A) and 2.72 (Panel B).
- p. 3 defines MV as the natural log of market value; Table 1 reports MV in USD million (average 2,510).
- The robustness list (p. 5-6) names the minimum price test twice (third and seventh check).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Robustness checks "do not contradict" the baseline, all in an online Table A2 | p. 6, fn 9 |
| Quantile regressions give consistent signs, significance depends on τ | fn 7 |
| Adding an explicit other-weekday return keeps SEAS significant | fn 8 |
| Results hold for UMD windows of 5 to 52 weeks | fn 6 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Same-weekday average return over 20 weeks as a cross-sectional signal | technique | signal | Follows Keloharju et al. (2016); aggregates all daily seasonalities into one signal. Card [[Calendar seasonality signal]] | Eq. 1, p. 2-3 |
| 2 | Momentum window matched to the seasonality window | principle | evaluation | Ensures SEAS is not driven by other-weekday returns | p. 3 |
| 3 | Factors built with one-way sorts, same as test portfolios | principle | evaluation | Any alpha then comes from the signal, not the construction | fn 6 |
| 4 | Risk-adjusted returns from a rolling 140-day three-factor regression as dependent variable | technique | evaluation | Follows Brennan et al.; Avramov et al. | p. 4 |
| 5 | Exclude each weekday in turn | technique | evaluation | Checks no single day drives the result | p. 6 |

## 6. Regime observations

- Not addressed in the article (subperiods in the online appendix only).

## 7. Acknowledged limits

- Short sample, to be checked on longer and fresher data (p. 6-7).
- Mechanism and practical exploitation not studied (p. 7).

## 8. Not addressed

- Transaction costs and turnover of a daily rebalanced strategy.
- Shorting feasibility.
- Effect of choosing the coin list on 16 Dec 2019, the last day of the sample.
- Drawdowns, Sharpe ratio, cumulative performance.
- Which weekday contributes most.
- Out-of-sample test.
