---
type: reading-note
source: paper
title: Two centuries of trend following
authors: Lempérière, Deremble, Seager, Potters, Bouchaud
affiliations: All five authors at Capital Fund Management (CFM), Paris
year: 2014
venue: arXiv preprint, q-fin.PM
doi: none printed; arXiv:1404.3274
pdf: "[[2014 - Lempérière Deremble Seager et al - Two centuries of trend following.pdf]]"
version: arXiv v1, 12 April 2014 (paper dated 15 April 2014)
tier: 2
read: full
tags: [trend, multi-asset, monthly]
date: 2026-10-23
---

# Two centuries of trend following (Lempérière, Deremble, Seager, Potters, Bouchaud 2014)

## Summary

- **Finding**: a sign-of-trend rule with a 5-month EMA signal earns Sharpe 0.72 since 1800 (t = 10.5, de-biased 9.8) across four sectors, gross. On futures since 1960 the Sharpe is 0.78.
- **Mechanism**: the authors favour extrapolative expectations over under-reaction. They read the signal's saturation as fundamentalists stepping in against strong trends. The support is cited literature and an anecdote, not tested here.
- **Where it works best**: indices since 1800 (Sharpe 0.7, de-biased t 6.3). Futures in 1970-2000 (Sharpe 1.05 to 1.15). Positive in every sector and every 50-year period.
- **Weak spots**: bonds since 1982 have a de-biased t of 1.6. For commodities since 1800 the de-biased t (3.1) is below the long-only t (4.5). Flat since 2011. A 3-day trend has faded since ≈2003.
- **Main caveats**: no costs or financing. Pre-futures data are spot proxies (commodity correlation 0.65). n = 5 chosen without argument. Fig. 1 and Table 1 disagree. The authors work for a fund manager.

Page numbers follow the PDF (the printed page numbers match). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Under-reaction: agents are slow to fold in news such as gradual policy changes (conservatism bias) | Cited literature only | p. 12-13 |
| 2 | Extrapolative expectations: past trends shape expected prices, a positive feedback that reinforces trends. The authors favour this one. | Cited lab experiments, surveys and agent-based models. Anecdote: CFM investors chase performance. | p. 13-14, fn 6 |
| 3 | Saturation: fundamentalist traders step in when trends become strong | Tanh fit of Fig. 5. Called "one plausible interpretation". | p. 14 |

**Caveats raised by the authors**
- If under-reaction drives trends, trends could disappear as policy becomes easier to anticipate (p. 14).
- It is not clear how crowding would hurt trends under extrapolative expectations (p. 13-14).
- No mechanism is offered for the disappearance of fast trends (p. 14).
- They cannot rule out that the recent period is the start of an "end of trends" (p. 2).

**Ruled out**
- Long-only drift as the source: correlation with long-only is +15%, and de-biased t-stats stay high (p. 4, 9).
- Risk premium: asserted with citations only (fn 4, p. 2; p. 14).
- Crowding as the cause of recent weakness: based on Fig. 7 and on CTAs being a few percent of volumes (p. 14).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 7 commodities (crude oil, Henry Hub natural gas, corn, wheat, sugar, live cattle, copper), 7 10-year bonds, 7 stock indexes, 6 currency contracts. Countries: Australia, Canada, Germany, Japan, Switzerland, UK, US. Chosen for long histories; no emerging markets. | p. 4 |
| Period | Futures from 1960 (commodities only until 1973). Full sample from 1800 using spot proxies. | p. 4, 9; Table 2, 8 |
| Signal | Last month's close minus an EMA of past prices, divided by an EMA of absolute monthly price changes, both with decay n months | p. 3, Eq. 1 |
| Entry / exit | Long if the signal is positive, short if negative. No other exit. | p. 3, Eq. 2 |
| Horizon | n = 5 months; grid 2 to 20 months | p. 3; Table 1 |
| Sizing | Quantity ±1/σ_n of each contract | p. 3, Eq. 2 |
| Portfolio | P&L summed across contracts. No sector weighting stated. | p. 4 |
| Rebalancing | Monthly closes | p. 3 |
| Costs | None. P&L excludes interest on capital; called "fictitious". | p. 3, fn 5 |
| Evaluation | Sharpe = annualised mean / annualised volatility; t = Sharpe × √years. De-biased: the residual after removing the beta to long-only. | p. 3-4 |

**Rule** (Eq. 1-2, p. 3)

$$s_n(t) = \frac{p(t-1) - \langle p \rangle_{n,t-1}}{\sigma_n(t-1)}, \qquad Q^\alpha_n(t) = \sum_{t'<t} \text{sign}[s_n(t')] \cdot \frac{p(t'+1) - p(t')}{\sigma_n(t'-1)}$$

- The EMA excludes p(t) itself.
- The EMA decay is "equal to n months"; the exact weights are not given.
- The rule works on price changes, not percentage returns.
- The index alignment is as printed. The paper does not say whether p(t') is the close of month t' or of month t'-1.
- The drift µ is defined as "the average daily return" (p. 3), although the data are monthly.

**Data provenance**
- All data come from Global Financial Data (p. 4).
- Futures start dates: commodities 01/1960, currencies 05/1973, indices 01/1982, bonds 05/1982 (Table 2). How contracts are rolled is not stated.
- Index spot series start between 1693 (UK) and 1914 (Canada, Switzerland, Japan) (Table 5).
- Commodity spot series start between 1784 (sugar) and 1986 (natural gas) (Table 6).
- Bonds come from government rates, from 1918 only. Before that, the debt market is judged not freely traded and liquid (p. 6-7). How rates become prices is not stated.
- FX has no proxy before 1973 (Bretton Woods, gold standard, 1930s managed currencies) (p. 6).
- Excluded: war and post-war Japan and Germany bonds, WWII stock market closures in Germany and Japan, and the fixed-price period of crude (p. 7-8).
- The authors say the series have no gaps and no major outliers (p. 8).
- Proxy check against futures: correlation of trend P&L 91% since 1982 (p. 8); by sector, commodities 0.65, bonds 0.91, indices 0.92 (Table 7). The spot slope is slightly lower (Fig. 3, ≈92 vs ≈103 in arbitrary units by the end).

## 3. Results

All results are on real data, in-sample, gross of costs and financing. No out-of-sample test.

**Aggregate**
- Futures since 1960, n = 5: Fig. 1 gives t = 5.9, Sharpe 0.8, de-biased t 5.0. Table 1 gives Sharpe 0.78, t 5.7, de-biased t 5.0.
- Correlation with long-only: +15% (p. 4).
- Since 1800: Sharpe 0.72, t = 10.5, de-biased 9.8 (Fig. 4). For comparison, the drift t-stat is 4.6 (p. 9).

**By sub-group**
- Futures sectors (Table 2):
	- Sharpe from 0.41 (indices) to 0.8 (commodities).
	- De-biased t from 1.6 (bonds) to 5.0 (commodities).
	- Bond drift t (3.3) exceeds the bond trend de-biased t (1.6).
- Sectors since 1800 (Table 8):
	- Sharpe from 0.28 (commodities) to 0.7 (indices). t ≥ 2.9; de-biased t ≥ 2.7.
	- De-biased t is higher than the long-only t everywhere except commodities (3.1 vs 4.5) (p. 9).
- Futures decades (Table 3):
	- Sharpe from 0.66 (1960s) to 1.15 (1970s).
	- After 2000: Sharpe 0.75, de-biased t 1.9. Lowest de-biased t: 1.8 in the 1960s.
	- The 1980s earn Sharpe 1.05 while the drift Sharpe is -0.03.
- 50-year periods (Table 9): Sharpe from 0.57 (1850-1900) to 0.99 (after 1950). The authors attribute the rise to the growing number of products (p. 9-10).
- No results are given by instrument or by long and short side.

**Horizon and parameters**
- n = 2 to 10 months: Sharpe 0.76 to 0.83. n = 15: 0.65. n = 20: 0.57, de-biased t 3.3 (Table 1).
- Pooled regression of the next price change on s_n, futures only, 240,000 points (Fig. 5):
	- Linear fit: a = 0.018 ± 0.003, b = 0.038 ± 0.002 (p. 10).
	- Cubic fit: very small s² term and a clearly negative s³ term (p. 11).
	- Tanh fit Δ = a + b s* tanh(s/s*): the best fit, s* ≈ 0.89, b ≈ 0.075 (p. 11).
	- How Δ is normalised is not stated.
- A 3-day trend on futures rises to ≈2003, then flattens or slightly falls (Fig. 8). The text says it decayed since 1990 (p. 12). Its rule is not given.

**Over time**
- Flat since 2011 (Fig. 6, ≈508 at 2011 and ≈508 by the end).
- The 10-year rolling P&L was never negative in two centuries (p. 12). It is currently slightly below its average. The 1940s were much worse (lowest ≈3, arbitrary units), with another low ≈1900 (Fig. 7).
- Typical drawdown duration is 1/S² years: 2 years at Sharpe 0.7, and 4 years is not exceptional (p. 11).

**Link to other strategies**
- Long-only: correlation +15% (p. 4).
- "Correlated with long-vol strategies": asserted, no number given (fn 4, p. 2).
- Cross-sectional stock momentum is mentioned but not studied (p. 2).

**Inconsistencies in the source**
- Fig. 1 and p. 4 give t = 5.9 and Sharpe 0.8 for n = 5. Table 1 gives t = 5.7 and Sharpe 0.78.
- p. 4 cites "Table 2" for the dependence on n; it is Table 1.
- p. 7 cites "Fig. 4" for central bank independence; it is Table 4.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Conclusions "extremely robust" to other tests or implementations (cites others) | p. 3 |
| A wider pool would only improve the results | p. 4 |
| Adding the cost of carry can only improve trend on futures | p. 8 |
| Not a risk premium; correlated with long-vol | p. 2, fn 4; p. 14 |
| Cubic coefficients and the fit comparison: no statistic shown | p. 11 |
| a, b and s* hardly change for n from 2.5 to 10 months | p. 11 |
| The recent period is "fully compatible with a statistical fluctuation": no test, only Fig. 7 | p. 2, 12 |
| CTAs manage 325 B$, ≈16% of hedge fund assets (cited) and only a few percent of volumes | p. 2, 14 |
| CTAs neither increased nor reduced long trends | p. 13 |
| Professional investors chase performance (CFM flows, anecdote) | fn 6, p. 13 |
| Drawdown duration 1/S² (cited) | p. 11 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Sign of (price minus EMA of past prices) / EMA of absolute price changes. [[Time-series momentum signal]] | technique | signal | Mimics a constant-risk strategy | p. 3, Eq. 1 |
| 2 | Position ±1/σ_n, with σ_n an EMA of absolute price changes. [[Volatility targeting]] | technique | sizing | Constant risk | p. 3, Eq. 2 |
| 3 | De-biased t-stat: residual after the beta to long-only. [[Always-long benchmark comparison]] | technique | evaluation | Remove the long bias of drifting markets | p. 4 |
| 4 | Keep only free-floating, liquid periods; drop pegged or managed regimes. [[Currency exclusion filter]] | principle | universe | No trend can develop under a peg or without liquidity | p. 6-8 |
| 5 | Pooled regression of the next change on the signal: linear, cubic and tanh fits. [[Signal response curve]] | technique | evaluation | A linear relation is not obvious a priori | p. 10-11, Fig. 5 |
| 6 | Trailing 10-year P&L against its historical average; drawdown duration 1/S². [[Rolling performance against history]] | technique | evaluation | Judge whether recent weakness is exceptional | p. 11-12, Fig. 7 |
| 7 | Spot proxies validated by the correlation of trend P&L with futures on the overlap | technique | universe | Extend the history | p. 8, Table 7 |
| 8 | t = Sharpe × √years, no risk-free rate subtracted for futures | principle | evaluation | Futures are self-financed | p. 3 |
| 9 | Breakdown by sector and by decade | principle | evaluation | Test universality | Tables 2-3, 8-9 |

## 6. Regime observations

- No trend is expected under the Bretton Woods ±1% band or the gold standard (p. 6).
- Trend earned Sharpe 1.05 in the 1980s while the drift was negative (Table 3).
- Plateau since 2011 (Fig. 6). Weakest 10-year stretch in the 1940s (Fig. 7).
- Short-term (3-day) trends faded from ≈1990 and were gone by ≈2003 (p. 12; Fig. 8).

## 7. Acknowledged limits

- Only instruments with long datasets; no emerging markets (p. 4).
- The first 10 years of futures hold only commodities (p. 4).
- No realistic costs (fn 5).
- No FX before 1973 (p. 6, 14).
- Spot proxies miss the cost of carry (p. 8).
- More products in later years raise performance (p. 9-10).
- An end of trends cannot be excluded (p. 2).

## 8. Not addressed

- Transaction costs, slippage, capacity.
- Drawdown depths in numbers.
- Leverage and volatility level of the P&L.
- Futures roll method; how bond yields are converted to prices.
- Exact EMA weights; signal timing alignment.
- Results per instrument; long vs short split.
- Sector weighting; out-of-sample test.
