---
type: reading-note
source: paper
title: Time series momentum
authors: Moskowitz, Ooi, Pedersen
affiliations: Moskowitz (Chicago Booth), Ooi and Pedersen (AQR Capital Management)
year: 2012
venue: JFE 104, 228-250
doi: 10.1016/j.jfineco.2011.11.003
pdf: "[[2012 - Moskowitz Ooi Pedersen - Time Series Momentum.pdf]]"
version: published
tier: 1
read: full
tags: [trend, multi-asset, monthly]
date: 2026-10-21
---

# Time series momentum (Moskowitz, Ooi, Pedersen 2012)

## Summary

- **Finding**: the sign of an instrument's own past 12-month excess return predicts its next-month return in all 58 futures tested, 1985-2009. Diversified Sharpe ratio above 1, gross of costs. Continuation lasts about a year, then partially reverses.
- **Mechanism (authors)**: under-reaction then delayed over-reaction to information, and/or hedgers paying speculators for liquidity. Both left open. Who pays: hedgers.
- **Where it works best**: 12-month lookback, 1-month holding (best cell of the grid, t = 6.61). Significant in all four asset classes.
- **Weak spots**: bond profits come mostly from the mean return, not persistence; currencies negative at long lookbacks; several contracts with Sharpe below 0.1; sharp losses at trend reversals (March-May 2009).
- **Main caveats**: no costs; specification chosen in-sample; pre-futures history uses cash indexes.

Page numbers follow the journal pagination (228-250). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

Two explanations, both left open.

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Under-reaction to information, then delayed over-reaction | Returns continue for about 12 months, then partially reverse. Only the spot-price component reverses. Impulse response of futures returns: peak ≈3.9% near month 12, ≈3.7% at month 36. | Fig. 1, 6A, 7A-B; p. 245, 248 |
| 2 | Premium paid by hedgers to speculators for liquidity | Speculators are positioned with the trend in every CFTC contract except the S&P 500, and cut positions as it fades. The roll-return component keeps rising (≈2.6% at month 36) without reversal. | Fig. 5, 6B, 7C; p. 244-248 |

Claim 2 is put as a possibility: "one explanation might be" (p. 246).

**Caveats raised by the authors**
- TSMOM is more correlated across asset classes than the assets themselves; behavioural models do not explain this (p. 229).
- Different investor bases produce the same pattern at the same time (p. 229).
- No link with sentiment measures (p. 229, Table 3C).
- A rational explanation cannot be ruled out (p. 230).
- Causality between positions and returns is indeterminate (p. 245-246).
- Speculators do not chase the trend; any over-reaction from trading would come from hedgers (p. 245).

**Ruled out**
- Crash-risk compensation: returns are highest in extreme markets, up and down (p. 230, Table 3C).
- Funding liquidity, volatility, sentiment as drivers: no significant relation (Table 3C).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 58 futures and forwards: 24 commodities, 12 currency pairs (from 9 currencies), 9 equity indexes, 13 government bonds. Most liquid contracts, to avoid illiquidity and stale prices. | p. 230, App. A |
| Period | Data 1965-2009. Results 1985-2009, for breadth and liquidity. | p. 230, 236 |
| Signal | Sign of the past 12-month excess return, no month skipped. Long if positive, short if negative. | p. 233, 236 |
| Horizon | Hold 1 month. Grid tested: lookback and holding in {1, 3, 6, 9, 12, 24, 36, 48} months. | Table 2 |
| Sizing | 40% / sigma per position. Sigma: EWMA of squared daily returns, centre of mass 60 days, annualised with 261, estimated at t-1. | p. 233, 236 |
| Portfolio | Equal weight across the S(t) instruments available at t. About 12% annual volatility. | p. 236 |
| Rebalancing | Monthly. Holding above 1 month: average of the overlapping portfolios. | p. 233-234 |
| Costs | None. Results are gross. | Fig. 2 |

**Rule** (Eq. 5, p. 236), per instrument s, then averaged over the S(t) available instruments:

$$r^{TSMOM,s}_{t,t+1} = \text{sign}(r^s_{t-12,t}) \cdot \frac{40\%}{\sigma^s_t} \cdot r^s_{t,t+1}$$

**Data provenance** (p. 231, App. A)

| Class | Source | Before futures existed |
| --- | --- | --- |
| Equity indexes | Datastream futures | MSCI country index returns |
| Bonds | Datastream futures, scaled to constant duration (2, 4, 7, 20 years) | JP Morgan country bond index returns |
| Currencies | Citigroup spot and forward rates from 1989 (CAD from 1992, NZD from 1996) | Datastream spot rates and Bloomberg IBOR short rates |
| Commodities | LME, ICE, CME, CBOT, NYMEX, COMEX, TOCOM | n/a |
| Positions | CFTC Commitments of Traders, 1986-2009 | n/a |
| Liquidity | Reuters and broker feeds, one snapshot (June 2010) | n/a |

Return series: daily excess return of the most liquid contract (nearest or next-nearest), compounded.

## 3. Results

1985-2009 unless stated.

**Aggregate**

| Metric | Value | Where |
| --- | --- | --- |
| Diversified Sharpe ratio | "greater than one", about 2.5x the equity market. No exact figure. | p. 230 |
| Positive contracts | 58 of 58; 52 significant at 5% | p. 236 |
| Alpha over always-long, per contract | positive in 90%; 26% of those significant | p. 236 |
| Alpha vs MSCI World, SMB, HML, UMD | 1.58% per month (t = 7.99); 4.75% per quarter (t = 7.73) | Table 3A |
| Loading on UMD | 0.28 (t = 6.78) | Table 3A |
| Alpha vs value and momentum "everywhere" | 1.09% per month (t = 5.40) | p. 237 |
| Portfolio volatility | about 12% | p. 236 |
| Margin used | about 5-20% | footnote 8 |
| Squared market return coefficient (quarterly) | 1.99 (t = 3.88) | Table 3C |
| Sharpe vs illiquidity, across contracts | correlation -0.16 | p. 239 |
| Across-class correlation of TSMOM | 0.05 to 0.21 | Table 4B |

**By asset class**

| Class | Alpha t-stat, 12m / 1m | Sharpe per contract (gross, ≈) | Profit source per month: auto-covariance / mean squared / total | Within-class correlation, TSMOM / passive long |
| --- | --- | --- | --- | --- |
| Commodities | 4.66 | 0.02 (corn) to 0.78 (zinc) | 0.43% / 0.17% / 0.59% | 0.07 / 0.19 |
| Equity indexes | 3.77 | 0.34 (ASX, FTSE 100) to 0.83 (FTSE/MIB) | 0.83% / 0.17% / 1.00% | 0.37 / 0.60 |
| Bonds | 3.53 | 0.13 (3Y Australia) to 1.05 (2Y US) | 0.35% / 0.70% / 1.05% | 0.38 / 0.63 |
| Currencies | 3.41 | 0.06 (EUR-SEK) to 0.53 (USD-JPY) | 0.80% / 0.17% / 0.96% | 0.10 / -0.04 |
| Where | Table 2B-E | Fig. 2 | Table 5B | Table 4A |

- Bonds are the exception: most of the profit comes from the mean return of bonds over the sample ("mean squared"), not from trend persistence (p. 244).
- Weakest contracts (≈ Fig. 2): corn 0.02, natural gas 0.06, EUR-SEK 0.06, AUD-NZD 0.09, soybean complex about 0.1.

**Horizon** (lookback x holding)
- Best cell of the whole grid, all assets: 12-month lookback, 1-month holding, t = 6.61 (Table 2A).
- Significance fades beyond 12 months: 24 / 24 gives t = 0.20; 24 / 36 and 24 / 48 turn negative (Table 2A).
- Currencies: negative for every holding period at a 48-month lookback (-0.55 to -2.34); lowest cell -2.42 at 36 / 48 (Table 2E).
- Pooled regressions: all 12 most recent monthly lags positive, 9 significant; weaker reversals over the next 4 years (p. 233, Fig. 1B).
- Bonds: only lag 1 above t = 2 among the first 12 (≈ Fig. 1C). Currencies: most lags beyond 12 negative (≈ Fig. 1C).

**Over time and in extreme markets**
- 1966-1985 Sharpe ratio: 1.1, asked by the referee as an out-of-sample check (p. 238).
- Quarterly returns range from about -11% to about +25%; the highest come with the largest S&P 500 moves, up and down (≈ Fig. 4).
- Cumulative return ends well above a passive long portfolio with the same ex-ante volatility (Fig. 3, log scale, no figure given).

**Link to other strategies**

| Regression | Result | Where |
| --- | --- | --- |
| TSMOM on cross-sectional momentum (XSMOM), same assets | beta 0.66 (t = 15.17), R² 44%, alpha 0.76% per month (t = 5.90) | Table 5A |
| XSMOM of each class on TSMOM | alphas not significant; equity indexes marginal (0.29%, t = 1.86) | Table 5C |
| UMD (US stocks) on TSMOM | loading 0.49 (t = 6.56), alpha -0.28% (t = -0.93) | Table 5C |
| Managed futures index (1994-2009) on TSMOM | loading 0.55 (t = 9.60), alpha -0.30% (t = -1.37), R² 33% | Table 5C |
| Global macro index (1994-2009) on TSMOM | loading 0.32 (t = 5.64), alpha 0.52% (t = 2.38), R² 14% | Table 5C |

Inconsistency: p. 240 gives 0.10 for commodities and 0.07 for currencies; Table 4A gives the reverse. Table values used.

## 4. Claims without evidence shown

Stated by the authors, results not in the paper.

| Claim | Where |
| --- | --- |
| Robust among more illiquid instruments: illiquid commodities (feeder cattle, Kansas wheat, lumber, orange juice, rubber, tin), emerging market currencies and equities, illiquid fixed income futures. "(not reported)" | footnote 4 |
| Next-to-most-liquid contract: slightly stronger for commodities, almost unchanged for financials | p. 231 |
| Results robust to more sophisticated volatility models | p. 233 |
| Regressions qualitatively similar with OLS and no volatility scaling | footnote 7 |
| Pre-1985 data gives "similar (and generally more significant)" results; only the 1966-1985 Sharpe ratio is shown | p. 236, 238 |
| Equity results "almost identical" with cash indexes | p. 236 |
| XSMOM results do not depend on skipping the most recent month | footnote 10 |
| VAR results robust to lag lengths between 12 and 24 | p. 246 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Sign of own past 12-month return | technique | signal | Simplest form of the effect; 12-month lookback follows convention and Fig. 1, Table 2 | p. 233, 236 |
| 2 | Constant ex-ante volatility per position | technique | sizing | Aggregates instruments with very different volatilities; not dominated by a few volatile periods | p. 233 |
| 3 | EWMA volatility, centre of mass 60 days, lagged | technique | sizing | Simple, no look-ahead; results robust to richer models | p. 233 |
| 4 | Equal weight across available instruments | technique | sizing | Not argued | p. 236 |
| 5 | Average of overlapping portfolios when holding above 1 month | technique | rebalancing | One monthly series without overlapping observations | p. 233-234 |
| 6 | Continuous index from the most liquid contract | technique | universe | Not argued; next contract gives similar results | p. 231 |
| 7 | Bond futures at constant duration | technique | universe | Not argued | App. A.2 |
| 8 | Regression on squared market return | technique | evaluation | Detects straddle-like payoffs | Table 3C |
| 9 | Strategy vs always-long on the same instrument | technique | evaluation | Isolates the timing return | p. 236 |
| 10 | Quarterly non-overlapping returns next to monthly | technique | evaluation | Controls for non-synchronous trading across markets | p. 236 |
| 11 | Split profits into auto-covariance and mean-return components | technique | evaluation | Shows whether profits come from persistence or from the average drift | Table 5B |
| 12 | Split futures return into spot change and roll return | technique | economic intuition | Separates information diffusion from hedging pressure | p. 247-248 |
| 13 | Net speculator position: (long - short) / open interest | technique | economic intuition | Identifies who sits on each side of the trend | p. 231 |
| 14 | Both time series and cross-sectional momentum come from return auto-covariance | principle | signal | Lo-MacKinlay / Lewellen decomposition | Table 5B |

No turnover-reduction technique. #5 is statistical, not a trading rule.

## 6. Regime observations

- Q3 2008: losses, the strategy turns short. Q4 2008: large gains as markets keep falling (p. 238).
- March-May 2009: sharp losses at the end of the crisis, a trend reversal (p. 238).
- Best quarters coincide with the largest S&P 500 moves, up and down (Fig. 4).
- No relation with TED spread, VIX or sentiment, extremes included (Table 3C).

## 7. Acknowledged limits

- Results shown from 1985 only; earlier data thinner (p. 236).
- CFTC classification is noisy; positions cover only US stock and bond futures (p. 231, footnote 6).
- Liquidity measured on one volume snapshot, June 2010 (p. 239).
- Causality between positions and returns indeterminate (p. 245-246).

## 8. Not addressed

- Costs, turnover, slippage.
- Drawdowns and the exact portfolio Sharpe ratio.
- Capacity.
- Out-of-sample choice of the 12-month / 1-month specification: it is the best cell of the 1985-2009 grid; 1966-1985 is the only other check.
- Data after 2009.
- Execution timing within the month and roll schedule.
- Equity and bond histories before futures are cash index returns, not futures; the paper does not show results split by data type.
