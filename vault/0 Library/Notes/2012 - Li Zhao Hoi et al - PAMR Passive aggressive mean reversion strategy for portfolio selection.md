---
type: reading-note
source: paper
title: "PAMR: Passive aggressive mean reversion strategy for portfolio selection"
authors: Li, Zhao, Hoi, Gopalkrishnan
affiliations: Li, Zhao and Hoi (Nanyang Technological University), Gopalkrishnan (Deloitte Analytics Institute, Singapore)
year: 2012
venue: Machine Learning 87, 221-258
doi: 10.1007/s10994-012-5281-z
pdf: "[[2012 - Li Zhao Hoi et al - PAMR Passive aggressive mean reversion strategy for portfolio selection.pdf]]"
version: published
tier: 1
read: full
tags: [reversal, equities, daily]
date: 2026-10-21
---

# PAMR mean reversion portfolio (Li, Zhao, Hoi, Gopalkrishnan 2012)

## Summary

- **Finding**: daily long-only rule moving weight from yesterday's winners to losers. Backtests 1962-2010: NYSE (O) wealth 5.14E+15 vs 14.50 market; best on 3 of 6 datasets. Gross.
- **Mechanism**: the authors assume a stock that does worse than others tends to do better the next day, citing cross-autocovariance. Tested only through backtests and a naive check.
- **Where it works best**: TSE 1994-1998: 264.86 vs 1.61 market. MSCI indices 2006-2010: 15.23 vs 0.91. Break-even cost against the market 0.1% to 0.7% on five datasets.
- **Weak spots**: DJIA 2001-2003: 0.68 vs 0.76 market, alpha t = 0.2195. Anticor beats it on NYSE (N) and SP500. Authors admit it needs mean reversion in the pool.
- **Main caveats**: survivor-biased large caps; NYSE (O) result leans on one volatile stock; parameters set after seeing results; costs absent from headline tables; no turnover reported.

Page numbers follow the journal pagination (221-258; PDF page = printed page minus 220). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Worse performers than the rest tend to do better the next day ("sell the winner, buy the loser") | Two-stock example (Tables 1, 2). Cumulative wealth rises as ε falls toward 0 on five datasets (Fig. 5). | p. 227-230, 246 |
| 2 | Effectiveness comes from positive cross-autocovariances across securities | Cited from earlier work; not tested here | p. 227 |
| 3 | Keeping the old portfolio when the return is low avoids "mine" stocks in a crash | Intuition and a noisy-price example | p. 229, 236 |
| 4 | The update trades return against volatility risk | Algebra of the step size | p. 233 |

**Caveats raised by the authors**
- PAMR may lose to the best constant rebalanced portfolio, for example when one stock crashes and another explodes (p. 234).
- The regret bound may be worse than for log-loss methods; universality is an open question (p. 235, 236).
- Needs mean reversion in the asset pool; fails on DJIA (p. 251).
- Survival bias in the NYSE datasets (p. 252-253).
- High wealth would move the market (p. 251).

**Ruled out**
- Luck: t-test on alpha, rejected on all datasets but DJIA (Table 5, p. 243).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Six datasets of stocks or indices, 23 to 88 assets each (Table 3). | p. 237 |
| Period | 1962 to 2010, by dataset: NYSE (O) 1962-1984, NYSE (N) 1985-2010, TSE 1994-1998, SP500 1998-2003, MSCI 2006-2010, DJIA 2001-2003. | Table 3 |
| Signal | Portfolio return on the last price relatives against threshold ε. | p. 230 |
| Entry and exit | Daily rebalance; weight moves from better to worse performers of the last day. | p. 233 |
| Sizing | Long only, fully invested, no short. Start at 1/m each. | p. 223 |
| Calibration | ε = 0.5, C = 500 for all datasets. | p. 238 |
| Rebalancing | Every trading day, at the last close. | p. 224 |
| Costs | None in the model. Proportional cost γ tested separately. | p. 224, 240 |
| Data and tools | Daily price relatives, adjusted for splits and dividends. | p. 237 |

**Rule** (Fig. 2, p. 233): loss $\ell_t = \max(0,\, b_t\cdot x_t - \epsilon)$, then

$$\tau_t = \frac{\ell_t}{\lVert x_t-\bar x_t\mathbf 1\rVert^2}\ \text{(PAMR)},\quad \min\!\Big(C,\frac{\ell_t}{\lVert x_t-\bar x_t\mathbf 1\rVert^2}\Big)\ \text{(PAMR-1)},\quad \frac{\ell_t}{\lVert x_t-\bar x_t\mathbf 1\rVert^2+\frac{1}{2C}}\ \text{(PAMR-2)}$$

$$b_{t+1} = \Pi_{\Delta}\big(b_t - \tau_t(x_t-\bar x_t\mathbf 1)\big)$$

$x_t$ is the price relative vector, $\bar x_t$ its mean, $\Pi_\Delta$ the projection on the simplex. Total cost O(mn) (p. 234).

**Data provenance**
- NYSE (O): 36 stocks, originally collected by another author; selection criteria unknown (p. 237, fn 5).
- NYSE (N): 23 survivors of those, self-collected, Yahoo Finance for 2007-2010 (p. 237, fn 6).
- TSE, SP500, DJIA from Borodin et al. 2004; MSCI: 24 country indices, not all tradable as ETFs (p. 237-238, fn 8).

## 3. Results

Real data, in-sample backtests, gross of costs, unless stated. Initial wealth 1.

**Aggregate** (Table 4, p. 242), cumulative wealth

| Dataset | PAMR | Market | Best competitor |
| --- | --- | --- | --- |
| NYSE (O) | 5.14E+15 | 14.50 | BNN 3.35E+11 |
| NYSE (N) | 1.25E+06 | 18.06 | Anticor 6.21E+06 |
| TSE | 264.86 | 1.61 | Anticor 39.36 |
| SP500 | 5.09 | 1.34 | Anticor 5.89 |
| MSCI | 15.23 | 0.91 | BNN 13.47 |
| DJIA | 0.68 | 0.76 | ONS 1.53 |

- PAMR-1 and PAMR-2 give similar wealth in every dataset (Table 4).
- Alpha vs market (Table 5, p. 244): t from 15.7829 (NYSE (O)) to 2.0020 (SP500); DJIA 0.2195, p = 0.4132. Winning ratio 0.5175 to 0.5925.
- Volatility risk almost the highest; drawdown modest on most; Sharpe highest except DJIA (≈ Fig. 4, p. 245). PAMR drawdown ≈ 80% on DJIA (≈ Fig. 4b).

**By sub-group**
- NYSE (O): without one volatile stock ("Kin Ark"), 5.14E+15 falls to 1.27E+08 (p. 243).
- Volatility (Table 6, p. 246): on 5 low-volatility NYSE stocks 132.25; on 5 high-volatility ones 1.39E+05.
- Reversed datasets (Table 4): PAMR beats the market in all six. It beats BCRP in five of six; on TSE-1 it gets 2.67 vs 58.61 for BCRP.
- Margin buying, 50% down, 6% interest (Table 7): NYSE (O) 5.57E+25, TSE 720.42, MSCI 68.83, DJIA 0.84.
- Mixture MIX with ONS, Anticor, BNN: DJIA 1.35, but 78.58 on TSE (p. 242).

**Horizon and parameters**
- Wealth grows as ε falls from 1.5 toward 0, except on DJIA, where it falls (≈ Fig. 5, p. 246). Above ε = 1 PAMR stays at uniform CRP.
- C from 50 to 5000 changes little (≈ Fig. 6, 7, p. 246-247).
- ε and C were set so wealth "tends to be stable" (p. 238).

**Over time**
- Fig. 3 (≈, log scale): PAMR stays above market and BCRP over the period on most datasets; SP500 curves bunch; DJIA falls.

**Costs and speed**
- Break-even cost against the market: 0.7%, 0.4%, 0.1%, 0.3%, 0% (Fig. 8 caption, p. 248). At 0.2%, PAMR beats BCRP on four datasets (p. 249).
- Authors put a real cost near 0.01% (fn 11, p. 249).
- PAMR 8 s on NYSE (O) vs 2.57E+03 (Anticor), 7.89E+04 (BK), 4.93E+04 (BNN) (Table 8, p. 250).

**Link to other strategies**: compared with 12 benchmarks and methods (Sect. 5.3, p. 241); no factor model.

**Inconsistencies in the source**
- Text: PAMR outperforms Anticor, BK, BNN except on DJIA (p. 241). Table 4: Anticor is higher on NYSE (N), SP500 and DJIA.
- Text: PAMR beats BCRP "in all cases" on reversed data (p. 243). Table 4: BCRP wins on TSE-1.
- Text: parameters "have to be finely tuned" (p. 235) vs "not so parameter sensitive" (p. 247).
- Text: PAMR has the highest H/L ratio (p. 245). Table 6: PAMR 1.05E+03 is below BNN 1.10E+03; PAMR-1 and PAMR-2 are above. Text cites 1.35E+05 on NYSE (H); Table 6 gives 1.39E+05.
- Table 7 "No ML" differs from Table 4: UP on NYSE (O) 27.41 vs 26.68; BNN on MSCI 14.47 vs 13.47.
- Fig. 8 caption gives five break-even values for six datasets.
- Fig. 4c and 4d look identical (≈), which is unlikely for Sharpe and Calmar. To check.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Real transaction costs are low; one broker rate (about 0.01%) is quoted | p. 249, fn 11 |
| PAMR "could be generally applied to any type of financial markets" | p. 238 |
| Bankrupt assets and penny stocks excluded; effect unseen | p. 253 |
| Algorithmic slicing "can significantly decrease" market impact | p. 251 |
| High performance gives "confidence" in unseen markets | p. 251 |
| The naive test identifies mean reversion in a pool (shown on six datasets only) | p. 252 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Cross-sectional mean reversion]]: Loss zero when portfolio return is at or below ε, then linear | technique | signal | Separates passive and aggressive cases | p. 230 |
| 2 | [[Cross-sectional mean reversion]]: Shift weight from last day's winners to losers, step size by return over market variance | technique | entry | Mean reversion, less transfer when risk is high | p. 233 |
| 3 | [[Cross-sectional mean reversion]]: PAMR-1 cap on step size, PAMR-2 added 1/(2C) | technique | calibration | Dampens noisy price relatives | p. 231, 236 |
| 4 | [[Cross-sectional mean reversion]]: Project the update on the simplex | technique | sizing | Keep long-only, fully invested | p. 232 |
| 5 | Mix PAMR with a universal strategy, equal buy-and-hold | technique | risk | Worst-case guarantee for the mix | p. 236 |
| 6 | [[Mean reversion existence test]]: Naive test: weights proportional to gap from last best stock | technique | evaluation | Check that mean reversion exists | p. 252 |
| 7 | Alpha t-test against market excess return | technique | evaluation | Rule out luck | p. 239-240 |
| 8 | Reversed dataset: reverse order, invert price relatives | technique | evaluation | Test on a different market | p. 238 |
| 9 | [[Break-even transaction cost]]: Break-even transaction cost against the market | technique | evaluation | Practical viability | p. 249 |
| 10 | High- vs low-volatility asset subsets, H/L ratio | technique | evaluation | Dataset sensitivity | p. 245 |
| 11 | Margin component asset: price relative 2x - 1 - c | technique | sizing | Test leverage | p. 240 |

## 6. Regime observations

- Dot-com bubble (1995-2000) and subprime crisis (2007-2009) are covered by the datasets; no result split by episode (p. 238).
- DJIA 2001-2003: no mean reversion on the naive test, average daily return 0.999848 (Table 9, p. 252).

## 7. Acknowledged limits

- Universality of PAMR unproven (p. 236, 253).
- Transaction cost not in the formulation (p. 253-254).
- Large caps only, survival bias (p. 252-253).
- Perfect market assumed: no cost, full liquidity, no impact (p. 224, 251).

## 8. Not addressed

- Turnover and number of trades.
- Costs in Table 4 results; net Sharpe ratios.
- Out-of-sample choice of ε and C.
- Drawdown numbers (chart only).
- Data after 2010; assets outside equities.
- How the 36 NYSE stocks were chosen.
