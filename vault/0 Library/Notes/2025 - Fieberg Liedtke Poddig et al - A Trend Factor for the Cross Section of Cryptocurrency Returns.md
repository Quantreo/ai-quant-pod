---
type: reading-note
source: paper
title: A Trend Factor for the Cross Section of Cryptocurrency Returns
authors: Fieberg, Liedtke, Poddig, Walker, Zaremba
affiliations: HSB University of Applied Sciences Bremen, Concordia University, University of Luxembourg; University of Bremen; Concordia University, Corvinus University of Budapest; Poznan University of Economics and Business, Monash University
year: 2025
venue: Journal of Financial and Quantitative Analysis 60(7), pp. 3116-3153
doi: 10.1017/S0022109024000747
pdf: "[[2025 - Fieberg Liedtke Poddig et al - A Trend Factor for the Cross Section of Cryptocurrency Returns.pdf]]"
version: published (open access); Supplementary Material read (25 pages, cited as S-page)
supplement: "[[2025 - Fieberg Liedtke Poddig et al - A Trend Factor for the Cross Section of Cryptocurrency Returns Supplementary Material.pdf]]"
tier: 1
read: full
tags: [trend, crypto, weekly]
date: 2026-10-24
---

# CTREND, a crypto trend factor (Fieberg et al. 2025)

## Summary

- **Finding**: an aggregate of 28 technical indicators (CTREND) sorts 3,000+ coins; value-weighted top-minus-bottom quintile earns 3.87% a week (t = 5.19), Sharpe 1.94, Apr 2015 to May 2022, gross (Table 3).
- **Mechanism**: crypto lacks fundamental information, so uninformed investors infer value from past prices and follow trends; retail crypto traders behave momentum-like (Section II, literature). Not tested directly.
- **Where it works best**: survives costs (2.35% to 2.90% a week net, BETC 1.41%) and holds in the 100 largest coins (3.39% gross, 1.90% to 2.45% net) (Tables 8, 9). Stronger in low-volatility weeks (5.46%).
- **Weak spots**: 68% weekly turnover; 2-week rebalancing drops returns to 2.34%; insignificant beyond 4 weeks. Second half 3.26% vs first half 4.47%. 1-day lag lowers median Sharpe (1.46 to 1.24).
- **Main caveats**: baseline Sharpe sits "at the upper edge" of 55,296 design variants (median 1.34, range -1.45 to 10.92). Momentum beta 0.79; CTREND correlates 0.61 with CMOM (Table B.2). Holding beyond 4 weeks gives nothing (Table B.10).

Page numbers follow the journal pagination (3116 to 3153). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Uninformed investors infer fundamentals from past prices and rationally follow trends; scarcer fundamentals mean more reliance on technical signals | Models of Han et al. (2016b), Liu et al. (2024), cited; crypto has no cash-flow information | p. 3120 |
| 2 | Crypto traders are more momentum-prone and biased than stock traders | Kogan et al. (2024), Hackethal et al. (2022), Weber et al. (2023), cited | p. 3121 |
| 3 | Oscillators (rsi, stochK, cci) signal continuation, not reversal, in crypto; herding fuels trends | Positive H-L on oscillators (Table 2) | fn 6, p. 3126 |
| 4 | CTREND carries information beyond momentum | Alpha 2.62% against LTW; CTREND makes most momentum signals insignificant in regressions | Tables 3-4 |

**Caveats raised by the authors**
- Reliance on a preselected set of technical features (p. 3149).
- Volume data may be biased by wash trading; tested by excluding volume indicators (p. 3136).

**Ruled out**
- Momentum, size, beta, illiquidity, idiosyncratic volatility as explanations (bivariate sorts, Table B.3; Table 4).
- Concentration in small or illiquid coins (Table 8).
- Dependence on one market state (Table 5).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | CoinMarketCap coins with close, volume and market cap; market cap at least 1 million USD; drop observations with market cap above Bitcoin; returns truncated at 0.5% and 99.5% | p. 3121-3122 |
| Period | April 2015 to May 2022, 423 weeks | p. 3122 |
| Signal | 28 indicators: oscillators (rsi, stochK, stochD, stochRSI, cci), price SMAs 3 to 200 days scaled by price, macd, macd signal, volume SMAs, volmacd, chaikin, Bollinger bands and width | p. 3122-3124 |
| Indicator settings | Textbook defaults (S-p. 2): rsi, stochRSI, stochK 14 days; stochD 3-day SMA of stochK; cci 20 days, constant 0.015; macd EMA 12 minus EMA 26 over EMA 12, signal EMA 9; chaikin 21 days; Bollinger 20-day SMA, ±2 SD; SMAs and volume SMAs at 3, 5, 10, 20, 50, 100, 200 days, divided by today's price or dollar volume; EMA smoothing stated as 1/(1+L) | S-p. 2-6 |
| Aggregation | Ranks mapped to [-0.5, 0.5]; univariate Fama-MacBeth forecast per indicator (WLS by market cap, coefficients averaged over a 52-week rolling window); elastic net (α = 0.5, λ by corrected AIC) selects forecasts with positive weight; CTREND = average of selected forecasts | Eq. 7-11, p. 3127-3129 |
| Entry | Rank on CTREND at the start of each week, quintiles | p. 3129 |
| Exit | Hold one week | p. 3129 |
| Horizon | Weekly | p. 3129 |
| Sizing | Value-weighted | p. 3129 |
| Portfolio | Long top quintile, short bottom quintile | p. 3129 |
| Rebalancing | Weekly | p. 3129 |
| Costs | Net results with 30 bps long / 40 bps short per trade, plus +10 and +20 bps variants | p. 3146-3147 |
| Data and tools | CoinMarketCap OHLC, volume, market cap; LTW factors from Yukun Liu's dropbox | p. 3121, fn 5 |

**Rule** (p. 3127-3129): for each indicator j, r̂j(i,t+1) = αj + βj·z(i,j,t), with αj, βj averaged from weekly cross-sectional WLS regressions over the past 52 weeks. Keep the forecasts whose elastic-net weight θj is positive; CTREND(i) = their simple average. Long the top quintile of CTREND, short the bottom, value-weighted, weekly.

**Data provenance**
- Market-cap filter above Bitcoin removes ten daily observations (fn 1).
- Coin count from 74 (2015) to 2,213 (2021) (Table 1).

## 3. Results

All results are real data. The CTREND forecast is out-of-sample week by week (rolling 52-week estimation); the design choices are fixed by the authors on the full period. Gross unless noted.

**Aggregate** (Table 3)
- Quintiles L to H: 0.12%, 0.93%, 1.12%, 2.72%, 3.98% a week.
- H-L 3.87% (t = 5.19), SD 14.34%, Sharpe 1.94; CCAPM alpha 3.80%; LTW alpha 2.62% (t = 4.22), βCMOM 0.79.
- Fama-MacBeth WLS (Table 4): CTREND slope 2.36 (t = 5.00) alone, 2.00 to 2.94 with controls.
- Single indicators (Table 2): rsi H-L 3.52%, stochK 3.96%, cci 3.80%; boll_mid -3.50% (low beats high); volume indicators mostly insignificant.

**By sub-group**
- Largest 10% of coins: 2.51% (t = 3.01); top 100: 3.39% (Table 8, Panel A).
- Most liquid 10%: 2.20%; top 100 liquid: 3.30% (Panel B).
- Coins vs tokens (Table B.4): H-L 3.31% (t = 4.31) coins, 3.16% (t = 2.93) tokens; LTW alpha 1.91% and 3.13%.
- Bivariate sorts (Table B.3): H-L 1.42% to 3.10%; with past 1 to 4 week returns as control, 1.90% to 3.10% (t 3.80 to 4.87), LTW alpha 1.28% to 2.39%; Amihud control cuts LTW alpha to 0.62% (t = 1.67).

**Horizon and parameters**
- 55,296 design variants (Table 6, Fig. 2): CS-C-ENet median Sharpe 1.34, range -1.45 to 10.92; significant Sharpe in 79% of variants vs 56% (CSMB) and 49% (CMOM).
- Median Sharpe by choice: value weight 1.17 vs equal weight 1.47; price filter 1 USD 1.13; 1-day lag 1.24 vs 1.46; validation split 1.19 vs 1.47.
- Costs (Table 9): turnover 68.46%; net 2.90% (I), 2.62% (II), 2.35% (III); BETC 1.41%, BETC at 5% significance 0.88%.
- Holding (Table B.10): 1 to 6 weeks gives 3.87, 2.34, 2.35, 1.55 (t = 2.10), 0.03, -0.53% a week.
- Value-weight only grid of 27,648 designs (Table B.6), CS-C-ENet median Sharpe: 1-day lag 1.04 vs 1.28; volume indicators excluded 1.27 vs included 1.08; price filter 1 USD 0.91; 26-week window 1.00, 104-week 1.28.

**Over time** (Table 5)
- First half (Apr 2015 to Nov 2018) 4.47%, second half 3.26%; LTW alphas 2.66% and 2.38%.
- Low volatility 5.46% vs high 2.27%; low uncertainty 4.22% vs high 3.59%; bull 4.49% vs bear 3.25%.

**Link to other strategies**
- Weekly factors (Table B.2): CMKT 1.89% (Sharpe 1.23), CSMB 3.18% (1.79), CMOM 1.98% (1.27); CTREND correlation 0.61 with CMOM, 0.02 with CMKT, -0.01 with CSMB.
- Table B.7 (alternative LTW factor data): H-L βCMOM 0.90 (t = 18.72), LTW alpha 2.61%.
- Indicator alphas against CMKT, CSMB, CTREND: none significant at 5% (Table B.9).
- Frontier test (Table 7): adding CTREND to LTW gives alpha 2.77% (t = 3.80); adding CMOM to CMKT+CSMB+CTREND gives 0.37% (t = 1.02).
- TREND model (CMKT, CSMB, CTREND): average absolute anomaly alpha 0.68% vs 1.44% (LTW); GRS p = 8.02% vs 0.38% (Fig. 3).

**Inconsistencies in the source**
- p. 3122 counts 3,244 unique coins; Table 1 reports 3,245.
- p. 3132 says "despite the earlier evidence from Section IV.B"; the Amihud evidence it refers to is in Section IV.A (bivariate sorts).
- S-p. 2: Eq. A.1 normalises the SMA by 1/(L-1) over l = 0 to L; Eq. A.10 calls a sum the "average absolute deviation" (no 1/L).
- S-p. 3: stochK text says "lowest price", the formula uses lowest low and highest high.
- Figure B.2 is "in percentage terms" with an axis from -2 to 16; 3.87% a week over 423 weeks sums to far more (computed).
- Figure C.4 caption sorts by "the importance ranking shown in Figure C.4"; the ranking is Figure C.3.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Performance stable post-2017 when momentum disappoints (Fig. B.2) | p. 3134 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Cross-sectional combined elastic net (CS-C-ENet) over univariate indicator forecasts | technique | signal | Combines shrinkage and forecast combination; avoids arbitrary indicator choice. Card [[Technical indicator combination signal]] | p. 3127-3129 |
| 2 | Rank-transform indicators to [-0.5, 0.5] | technique | signal | Limits outliers | p. 3129 |
| 3 | Value-weighted WLS in all regressions | principle | evaluation | Reduce weight of micro-caps | p. 3129, 3132 |
| 4 | 52-week rolling estimation, one-week-ahead forecast | technique | calibration | Out-of-sample signal | p. 3129 |
| 5 | Grid of 55,296 design variants (nonstandard errors) | technique | evaluation | Robustness to researcher choices. Card [[Research design variation test]] | p. 3135-3139 |
| 6 | Turnover-based net returns and breakeven cost | technique | evaluation | Novy-Marx and Velikov concern on high-turnover signals. Card [[Break-even transaction cost]] | p. 3146-3147 |
| 7 | Frontier expansion test with out-of-sample tangency portfolios | technique | evaluation | Model comparison without test assets | p. 3140-3141 |
| 8 | Restrict to top 100 by size or liquidity | technique | universe | Tradeable coins. Card [[Minimum price and size filter]] | p. 3145 |

## 6. Regime observations

- CTREND is higher in calm and bullish markets but positive and significant in all states (Table 5).
- Raw returns lower in the second half, alphas almost unchanged (p. 3135).
- Selection is persistent: about 15 indicators a week; macd chosen in ≈ 90.6% of weeks, stochRSI ≈ 81.1%, boll_mid and cci ≈ 78.4%; importance highest for boll_mid, cci, macd (S-p. 21-23, Figs. C.3, C.4).

## 7. Acknowledged limits

- Preselected technical features (p. 3149).
- Extreme Sharpe ratios in some variants come from small, volatile coins (p. 3138-3139).

## 8. Not addressed

- Shorting feasibility and borrow costs for the short quintile.
- Exchange-level execution (CoinMarketCap aggregated prices).
- Drawdowns of the factor.
- Survivorship of delisted coins.
