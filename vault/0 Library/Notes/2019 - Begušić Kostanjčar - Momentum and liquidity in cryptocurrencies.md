---
type: reading-note
source: paper
title: "Momentum and liquidity in cryptocurrencies"
authors: Begušić, Kostanjčar
affiliations: Begušić and Kostanjčar (Laboratory for Financial and Risk Analytics, Faculty of Electrical Engineering and Computing, University of Zagreb)
year: 2019
venue: arXiv preprint 1904.00890v1 (q-fin.GN), marked as submitted to Elsevier, dated 31 March 2019
doi: none given; arXiv:1904.00890
pdf: "[[2019 - Begušić Kostanjčar - Momentum and liquidity in cryptocurrencies.pdf]]"
version: preprint v1, not peer-reviewed
tier: 1
read: full
tags: [trend, crypto, weekly]
date: 2026-10-23
---

# Momentum and liquidity in cryptocurrencies (Begušić, Kostanjčar 2019)

## Summary

- **Finding**: in 3x3 sorts on 14-day return and Amihud illiquidity, winners minus losers earns 0.26% a day in liquid coins; illiquid minus liquid 0.52% among losers. Gross, 2015-2019.
- **Mechanism (authors)**: investor herding and social-signal feedback explain momentum in liquid coins. Illiquid losers echo earlier evidence of mean reversion in illiquid coins. Not tested.
- **Where it works best**: long-only illiquid losers (1.07% a day, IR 2.49) and liquid winners (0.71%, IR 1.59), against a cap-weighted benchmark, gross.
- **Weak spots**: momentum negative, not significant, in neutral and illiquid coins. Authors admit illiquid losers may deteriorate through bid-ask costs. All portfolios fall sharply through 2018.
- **Main caveats**: one in-sample specification, no t-stats printed, cost method unstated, coins per portfolio unreported, ≈ 20 to ≈ 540 coins over time, survivorship not discussed.

Page numbers are the printed page numbers, which match the PDF (7 pages). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Momentum may be caused by investor herding; with positive feedback found in socio-economic signals around crypto, this explains why momentum is strongest in liquid coins | The pattern itself: UMD significant only in the liquid group. Herding and feedback are cited from other papers (refs 13, 15), not tested here | p. 2, 4, 6 |
| 2 | Illiquid coins show a mean reversion effect, in line with Wei (2018) | Illiquid losers 1.07% vs illiquid winners 0.53% a day; UMD in illiquid coins -0.33%, not significant | p. 3-4, Table 1 |
| 3 | An illiquidity premium exists within last period's losers | IML among losers 0.52% a day, significant at 5% | p. 2-3, Table 1 |

Motivation: stronger momentum in liquid market states in international equities (ref. 12, p. 1).

**Caveats raised by the authors**
- The illiquid losers portfolio sits in the most illiquid coins, where indirect costs from the bid-ask spread may be much higher (p. 5).

**Ruled out**
- Nothing is ruled out.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Coins listed on coinmarketcap.com, stablecoins removed. At each date: listed for at least T(c) = 26 weeks, and market cap never below M(c) = $1 million over those 26 weeks. 711 coins qualify at least once | p. 2 |
| Period | January 2015 to January 2019; earlier years have few coins and little trading | p. 2 |
| Signal | Momentum: cumulative price return over Tmom = 14 days, no skip. Illiquidity: Amihud measure over Tilliq = 14 days | Eq. 1-2, p. 3 |
| Groups | Each measure split at the 30th and 70th percentiles: losers / neutral / winners; liquid / neutral / illiquid. 9 portfolios. Whether the two sorts are independent or sequential is not stated | p. 3 |
| Spreads | UMD = winners minus losers within each illiquidity group; IML = illiquid minus liquid within each momentum group. Zero-investment | p. 3 |
| Long-only strategies | Illiquid losers; liquid winners | p. 4-5 |
| Horizon | Hold 14 days | p. 3 |
| Sizing | Equal weight within each portfolio | p. 3 |
| Rebalancing | Every 14 days. Drift between rebalances not stated | p. 3 |
| Benchmark | Cap-weighted portfolio of all eligible coins, rebalanced every 14 days | p. 3 |
| Metric | Mean daily return, daily standard deviation, information ratio vs benchmark, annualised (factor not stated) | Eq. 3, Table 1 |
| Costs | Gross in Table 1 and Fig. 2. Table 2 charges 10, 50, 100 bps; how the charge is applied (per trade, per turnover, per rebalance) is not stated. Zero market impact assumed | p. 5 |

**Rule** (Eq. 1-2, p. 3)

$$C_i(t) = \frac{P_i(t) - P_i(t - T_{mom})}{P_i(t - T_{mom})}, \qquad I_i(t) = \frac{1}{T_{illiq}} \sum_{\tau = t - T_{illiq}}^{t} \frac{|R_i(\tau)|}{V_i(\tau)}$$

V is daily traded volume in USD. As printed, the sum runs over Tilliq + 1 days and divides by Tilliq. Liquid winners: top 30% on C and bottom 30% on I, equal weight, held 14 days. Illiquid losers: bottom 30% on C and top 30% on I.

**Data provenance** (p. 2)
- Daily market cap, price and volume from coinmarketcap.com. Exchange coverage, price definition and treatment of delisted coins not stated.
- Number of eligible coins: ≈ under 20 through 2016, ≈ 100 by early 2018, peak ≈ 540 in late 2018, ≈ 490 at the end (≈ Fig. 1).

## 3. Results

All real data, in-sample, one specification, Jan 2015 to Jan 2019. Daily figures in %.

**Aggregate** (Table 1, gross)
- UMD among liquid coins: 0.26% a day, significant at 5% (two-tailed t-test); sd 5.10%; IR 0.22.
- IML among losers: 0.52% a day, significant; sd 5.05%; IR 1.05.
- No t-statistic or p-value is printed, only asterisks (Table 1).

**By sub-group** (Table 1, gross)
- Cell means range from 0.31% (liquid losers) to 1.07% (illiquid losers). IRs range from 0.55 (liquid losers) to 2.49 (illiquid losers).
- Standard deviation is highest among illiquid coins (7.36% to 9.45%) and among winners (p. 4).
- UMD by illiquidity group: liquid 0.26%*, neutral -0.06%, illiquid -0.33%.
- IML by momentum group: losers 0.52%*, neutral 0.16%, winners -0.07%.
- Where it does not work: momentum is negative in neutral and illiquid coins; illiquidity premium is negative among winners. Both not significant.

**Long-only strategies, with costs** (Table 2)

| Cost (bps) | Illiquid losers: mean / sd / IR | Liquid winners: mean / sd / IR |
| --- | --- | --- |
| 0 | 1.07 / 7.79 / 2.49 | 0.71 / 7.43 / 1.59 |
| 100 | 0.95 / 7.79 / 2.16 | 0.60 / 7.45 / 1.27 |

10 and 50 bps lie between (Table 2).

**Over time** (Fig. 2, log scale, gross, no costs)
- All three portfolios stay ≈ near their start until ≈ mid 2015.
- Illiquid losers peak ≈ 10^6 around Jan 2018; liquid winners ≈ 10^4.5; cap-weighted ≈ 10^1.5.
- All three fall from ≈ Jan 2018 to the end. Peak to end, ≈ -80% (illiquid losers), ≈ -95% (liquid winners), ≈ -83% (cap-weighted) (computed from chart readings, rough).
- No drawdown, Sharpe ratio or yearly figure is given in a table.

**Horizon and parameters**
- Not addressed. Only Tmom = Tilliq = 14 days, 30/70 breakpoints, T(c) = 26 weeks and M(c) = $1 million are shown. No other value is tested.

**Link to other strategies**
- None beyond the cap-weighted benchmark.

**Inconsistencies in the source**
- The text cites "Table 3" for the 3x3 sorts (p. 3) and for the cost table (p. 5). The tables are numbered 1 and 2; there is no Table 3.
- Printed spreads differ from the difference of printed cell means (computed): IML losers 0.52 vs 1.07 - 0.31 = 0.76; UMD liquid 0.26 vs 0.71 - 0.31 = 0.40; UMD illiquid -0.33 vs -0.54. All six spreads are smaller in size than the computed differences. The paper does not say whether spreads use a different sample of days.
- Fig. 2 starts in Jul 2014 and Fig. 1 before Jan 2015, while the text restricts the data to Jan 2015 - Jan 2019 (p. 2).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| The inclusion rules keep the most relevant and liquid coins, as a realistic investor would | p. 2 |
| $1 million is small enough to avoid any large-cap bias | p. 2 |
| Liquid winners should be much less exposed to bid-ask costs in practice | p. 5 |
| Herding explains momentum in liquid coins | p. 4, 6 |
| Shorting opportunities in crypto are limited | p. 4 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Rank on 14-day return, top 30% vs bottom 30%, held 14 days. Card: [[Cross-sectional momentum]] | technique | signal | Not argued | Eq. 1, p. 3 |
| 2 | Amihud illiquidity over 14 days as a second sort; momentum and reversal read within liquidity groups; long-only liquid winners and illiquid losers. Card: [[Liquidity-conditioned momentum]] | technique | signal | Momentum may be stronger in liquid states; shorting is limited | p. 1, 3-4 |
| 3 | 3x3 bivariate sort with spreads per row and column. Card: [[Conditional double sort]] | technique | evaluation | Tests whether momentum and illiquidity are pervasive | p. 3 |
| 4 | Minimum age 26 weeks and minimum market cap $1 million over that window, stablecoins removed. Card: [[Minimum price and size filter]] | technique | universe | Keeps relevant, liquid coins; avoids large-cap bias | p. 2 |
| 5 | Results at 0, 10, 50, 100 bps of cost. Card: [[Break-even transaction cost]] | technique | evaluation | Shows the strategies remain profitable with costs | p. 5 |
| 6 | Information ratio against a cap-weighted portfolio of the same eligible universe, same rebalancing | technique | evaluation | Risk-adjusted performance vs the market | Eq. 3, p. 3 |
| 7 | Equal weight, rebalanced every 14 days | technique | sizing | Not argued | p. 3 |

## 6. Regime observations

- Eligible coins grow from ≈ under 20 to ≈ 540; most of the growth comes from late 2017 (≈ Fig. 1).
- All portfolios peak ≈ Jan 2018 and decline through 2018 (≈ Fig. 2).
- No split of results by sub-period.

## 7. Acknowledged limits

- Illiquid losers performance "may additionally deteriorate in practice" through bid-ask costs (p. 5).
- Fig. 2 assumes no trading costs and zero market impact (p. 5).

## 8. Not addressed

- Number of coins per portfolio and per period, turnover.
- How costs are charged; bid-ask spreads and slippage measured on real data.
- Survivorship: whether dead or delisted coins remain in the coinmarketcap data.
- Any parameter other than the one set shown; any out-of-sample period.
- t-statistics, Sharpe ratios, drawdowns, results by sub-period.
- Exposure to the market or to other factors; capacity.
- Shorting or perpetual futures; which exchanges the prices come from.
- Execution price and timing at each rebalance.
