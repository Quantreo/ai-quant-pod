---
type: reading-note
source: paper
title: Momentum and liquidity in cryptocurrencies
authors: Begušić, Kostanjčar
affiliations: Laboratory for Financial and Risk Analytics, Faculty of Electrical Engineering and Computing, University of Zagreb
year: 2019
venue: arXiv:1904.00890v1 [q-fin.GN], preprint submitted to Elsevier
doi: none (arXiv:1904.00890)
pdf: "[[2019 - Begušić Kostanjčar - Momentum and liquidity in cryptocurrencies.pdf]]"
version: preprint v1, 31 March 2019
tier: 1
read: full
tags: [trend, crypto, weekly]
date: 2026-11-05
---

# Momentum and liquidity in cryptocurrencies (Begušić, Kostanjčar 2019)

## Summary

- **Finding**: Jan 2015 to Jan 2019, 711 coins, 14-day momentum: significant only among liquid coins (winners minus losers 0.26% daily). Illiquid losers earn 1.07% daily, best of nine cells. Gross.
- **Mechanism (authors)**: investor herding explains momentum in liquid coins; illiquid coins mean-revert. Asserted by citation, not tested in the paper.
- **Where it works best**: long-only illiquid losers, IR 2.49 gross and 2.16 at 100 bps. Long-only liquid winners, IR 1.59 gross and 1.27 at 100 bps. IR is against a cap-weighted portfolio.
- **Weak spots**: momentum not significant in neutral (-0.06%) or illiquid (-0.33%) coins. Authors expect illiquid losers to cost more than assumed, as spreads are wider.
- **Main caveats**: in-sample, four years, no t-statistics, no robustness to window or cutoffs, cost method unstated. IML and UMD cells do not equal the differences of the printed means.

Page numbers follow the PDF, which matches the printed pages (1 to 7). Values marked ≈ are read from a chart. The PDF captions say "Slika" and "Tablica"; this note says Figure and Table.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Momentum may be caused by investor herding. It is strongest in highly liquid coins. | UMD is significant only in the liquid bracket (0.26%). Positive feedback in socio-economic signals is cited from another study [15]. No test of herding. | p. 2, 4 |
| 2 | Illiquid coins mean-revert. | Illiquid losers 1.07% vs illiquid winners 0.53% daily. The authors say this "seems to confirm" Wei [10]. | p. 3-4 |
| 3 | Motivation: momentum is stronger in liquid states in international equities [12]. | Cited, not tested here. | p. 1 |

**Caveats raised by the authors**
- Illiquid losers may do worse in practice: they sit in the least liquid coins, where bid-ask costs may be much higher (p. 5).
- Shorting is limited in crypto, which is why long-only variants are studied (p. 4).
- Figure 2 assumes zero trading costs and zero market impact (p. 5).

**Ruled out**: Not stated by the authors.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Daily market cap, price and volume from coinmarketcap.com. Stablecoins removed. A coin enters if it existed for at least T(c) = 26 weeks and its market cap was never below M(c) = 10^6 USD over that window. 711 coins qualified at least once. | p. 2 |
| Period | Jan 2015 to Jan 2019. Earlier years have few coins and little trading. | p. 2 |
| Signal, momentum | Cumulative return over Tmom = 14 days. Losers: lowest 30%. Neutral: 30% to 70%. Winners: highest 30%. | p. 3 |
| Signal, liquidity | Amihud illiquidity over Tilliq = 14 days, from daily volume in USD. Liquid: lowest 30%. Neutral: middle. Illiquid: highest 30%. | p. 3 |
| Portfolios | 9 cells (3 x 3). Equal weight. Zero-investment UMD (winners minus losers) per liquidity class. Zero-investment IML (illiquid minus liquid) per momentum class. | p. 3 |
| Long-only variants | Illiquid losers and liquid winners. | p. 4 |
| Horizon, rebalancing | Every 14 days. | p. 3 |
| Benchmark | Cap-weighted portfolio of all coins that pass the filter at the rebalance, rebalanced every 14 days. | p. 3 |
| Costs | Table 2 grid: 0, 10, 50, 100 bps. How they are applied (per side, per rebalance, on turnover) is not stated. | p. 5 |

**Rule** (Eq. 1 and 2, p. 3), for coin i at day t:

$$C_i(t) = \frac{P_i(t) - P_i(t - T_{mom})}{P_i(t - T_{mom})} \qquad I_i(t) = \frac{1}{T_{illiq}} \sum_{\tau = t - T_{illiq}}^{t} \frac{|R_i(\tau)|}{V_i(\tau)}$$

Information ratio (Eq. 3): IR = E[Rp - Rb] / sqrt(var[Rp - Rb]), with Rb the cap-weighted portfolio. Table captions call it annualized; the factor is not given.

Not stated: whether the two sorts are independent or sequential, any skipped day between signal and holding, how the portfolio return is measured inside the 14-day holding period.

**Data provenance**: one source, coinmarketcap.com, daily. Coin count grows from ≈15 in 2015-2016 to ≈70 by mid-2017 and ≈540 at the peak near the end of 2018, ≈490 at the end of the sample (Fig. 1). Treatment of delisted coins and of reported volume quality is not stated.

## 3. Results

All results are real data, in-sample, gross unless stated. No out-of-sample split. Returns are mean daily returns in %.

**Aggregate** (Table 1, 9 cells)

| Metric | Value | Where |
| --- | --- | --- |
| Best cell, mean | Illiquid losers 1.07, IR 2.49 | Table 1 |
| Worst cell, mean | Liquid losers 0.31, IR 0.55 | Table 1 |
| Highest standard deviation | Illiquid winners 9.45 | Table 1 |
| Lowest standard deviation | Neutral momentum, liquid 5.18 | Table 1 |
| Significant at 5% (two-tailed t-test) | Only two cells: IML among losers (0.52) and UMD among liquid coins (0.26). No t-statistics printed. | Table 1; p. 3 |

**By sub-group** (Table 1)

| Sort | Values (mean, % daily) | Where |
| --- | --- | --- |
| UMD, liquid / neutral / illiquid | 0.26* / -0.06 / -0.33 | Table 1 |
| IML, losers / neutral / winners | 0.52* / 0.16 / -0.07 | Table 1 |
| Losers, liquid / neutral / illiquid | 0.31 / 0.56 / 1.07 | Table 1 |
| Winners, liquid / neutral / illiquid | 0.71 / 0.42 / 0.53 | Table 1 |
| Neutral, liquid / neutral / illiquid | 0.37 / 0.68 / 0.66 | Table 1 |

- Standard deviations are higher for illiquid coins and generally higher for winners (p. 4).
- IR by cell ranges from -0.55 (IML winners) to 2.49 (illiquid losers). UMD IR: 0.22 liquid, -0.71 neutral, -1.08 illiquid (Table 1). The paper does not say how an IR is defined for a zero-investment portfolio.

**Costs** (Table 2, long-only, mean daily return and IR)

| Costs (bps) | Illiquid losers E[R] / IR | Liquid winners E[R] / IR |
| --- | --- | --- |
| 0 | 1.07 / 2.49 | 0.71 / 1.59 |
| 100 | 0.95 / 2.16 | 0.60 / 1.27 |

Standard deviation: 7.79 for illiquid losers at every cost level; 7.43 for liquid winners, 7.45 at 100 bps. Table 2 gives rows for 10 and 50 bps.

**Horizon and parameters**: one setting only (14-day momentum, 14-day illiquidity, 14-day rebalance, 30% cutoffs, 26 weeks, 1 million USD). Not addressed.

**Over time** (Fig. 2, log scale, ≈ values; y-unit not stated, curves start near 10^0)
- All three curves are flat or below 10^0 until ≈ early 2015.
- All three peak ≈ Jan 2018 and fall through 2018 (no figure given in the text).
- Peak ≈2 x 10^6 (illiquid losers), ≈4 x 10^4 (liquid winners), ≈50 (cap-weighted).
- End ≈4 x 10^5, ≈2 x 10^3 and ≈8. Figure 2 is without costs and market impact.

**Link to other strategies**: only the cap-weighted benchmark. No factor regressions.

**Inconsistencies in the source**
- The text refers to "Table 3" for both the bivariate sorts (p. 3) and the costs (p. 5). The captions are Table 1 and Table 2.
- IML and UMD cells differ from the differences of the printed means (computed from Table 1):

| Cell | Computed difference | Printed |
| --- | --- | --- |
| IML losers | 1.07 - 0.31 = 0.76 | 0.52 |
| IML neutral | 0.66 - 0.37 = 0.29 | 0.16 |
| IML winners | 0.53 - 0.71 = -0.18 | -0.07 |
| UMD liquid | 0.71 - 0.31 = 0.40 | 0.26 |
| UMD neutral | 0.42 - 0.56 = -0.14 | -0.06 |
| UMD illiquid | 0.53 - 1.07 = -0.54 | -0.33 |

  Printed values used. The paper gives no reason.
- Figure 2 starts in Jul 2014; the text restricts the data to Jan 2015 to Jan 2019 (p. 2).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Momentum is "strong" in the most liquid coins (abstract). Only one cell is significant, at 5%. | p. 1, Table 1 |
| Momentum is explained by herding and positive feedback. No herding measure is used. | p. 4 |
| Liquid winners "should be much less exposed" to bid-ask costs. No spread data. | p. 5 |
| Both long-only strategies keep improved risk-adjusted performance "even when transaction costs are included". The benchmark's own statistics are not printed. | p. 6, Table 2 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Cross-sectional momentum]]: 14-day cumulative return, 30 / 40 / 30 split | technique | signal | Not argued | p. 3 |
| 2 | [[Amihud illiquidity]] over 14 days, same window as momentum | technique | signal | Not argued | p. 3 |
| 3 | [[Bivariate portfolio sort]]: 3 x 3 momentum-liquidity | technique | evaluation | To study how momentum interacts with liquidity | p. 1, 3 |
| 4 | [[Minimum age and market cap filter]]: age of at least 26 weeks, market cap never below 1 million USD over that window | technique | universe | Keeps relevant and liquid coins, as a realistic investor would. Small floor avoids a large-cap bias | p. 2 |
| 5 | Stablecoins removed | technique | universe | They are pegged to fiat or commodities | p. 2 |
| 6 | Equal weight, 14-day rebalance | technique | sizing | Not argued | p. 3 |
| 7 | Zero-investment UMD and IML inside each bracket | technique | evaluation | Not argued | p. 3 |
| 8 | Information ratio against a cap-weighted portfolio rebuilt at each rebalance | technique | evaluation | Not argued | p. 3 |
| 9 | Long-only legs of the sort | technique | entry | Limited shorting in crypto | p. 4 |
| 10 | Cost sensitivity grid, 0 to 100 bps | technique | evaluation | Not argued | p. 5 |

## 6. Regime observations

Not discussed by the authors. The chart shows a rise to ≈ Jan 2018 and a fall after it for all three portfolios (Fig. 2). The number of coins grows from ≈15 to ≈540 over the sample (Fig. 1).

## 7. Acknowledged limits

- Shorting is limited in crypto markets (p. 4).
- Illiquid losers may suffer higher indirect costs in practice (p. 5).
- Figure 2 ignores costs and market impact (p. 5).
- Years before 2015 excluded for few coins and little trading (p. 2).

## 8. Not addressed

- Robustness to the 14-day windows, the 30% cutoffs, T(c) and M(c). How they were chosen is not stated.
- Turnover, cost application, bid-ask spreads, capacity, market impact.
- Number of coins per portfolio, especially in 2015-2016 when ≈15 coins qualify (Fig. 1).
- Drawdowns, benchmark statistics, t-statistics, factor regressions.
- Out-of-sample testing, delisted coins, volume data quality.
- Independent or sequential sorting, timing of signal and holding.
