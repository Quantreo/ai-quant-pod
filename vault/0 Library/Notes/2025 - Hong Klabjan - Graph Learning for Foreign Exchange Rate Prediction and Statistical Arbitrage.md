---
type: reading-note
source: paper
title: Graph Learning for Foreign Exchange Rate Prediction and Statistical Arbitrage
authors: Hong, Klabjan
affiliations: Northwestern University (both authors)
year: 2025
venue: arXiv 2508.14784v1 [q-fin.TR], manuscript under review
doi:
pdf: "[[2025 - Hong Klabjan - Graph Learning for Foreign Exchange Rate Prediction and Statistical Arbitrage.pdf]]"
version: preprint
tier: 1
read: full
tags: [reversal, fx, daily]
date: 2026-10-25
---

# Graph learning for FX statistical arbitrage (Hong, Klabjan 2025)

## Summary

- **Finding**: a graph neural network sizes daily triangular-arbitrage trades on 10 currencies, 2016-2024 (≈). Against a linear-program benchmark fed the same forecasts: information ratio 43.80 vs 27.06 (%), annual return 4.76% vs 6.17%. Gross.
- **Mechanism**: Not stated by the authors. They cite studies that find triangular arbitrage violations in real FX data, and use interest rate parity as a feature rationale (p. 1-3).
- **Where it works best**: real data, all three home currencies (USD, EUR, JPY) give the same picture: lower volatility (-52.23%), lower max drawdown (-44.77%) than the benchmark (Table 1).
- **Weak spots**: average return is 22.73% lower than the benchmark (Table 1). Rolling information ratio drops in 2020, 2022, 2024 (Fig. 1). Forecast gain is tiny: MSE 2.8635 vs 2.9083 (x10^-5) at best (Table 2).
- **Main caveats**: no transaction costs, no bid-ask, unlimited borrowing assumed, closing rates only, benchmark built by the authors, hyperparameters picked by validation grid (p. 3, 5, 6).

Page numbers follow the PDF (the arXiv preprint has no journal pagination). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

No claim on who pays or why the mispricings persist. Not stated by the authors.

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Triangular arbitrage violations exist in practice, so FX rates are linked across currency triplets | Cited studies only (Aiba 2002, Fenn 2009, Mahmoodzadeh 2020). No own test of the violations. | p. 1-2 |
| 2 | FX rates relate to interest rates through interest rate parity, so rates help predict FX | Theory (covered and uncovered parity). Test: adding interest rates to the GNN lowers MSE from 2.8680 to 2.8635 (x10^-5). | p. 3, Table 2 |
| 3 | The GNN sizing beats the linear program because of better risk management | "In our opinion". Supported by lower volatility, drawdown, holdings and concentration (HHI) in Table 1. | p. 6, Table 1 |

**Caveats raised by the authors**
- The 2020, 2022 and 2024 drops in rolling information ratio "likely" come from shocks absent from training: Covid, Ukraine war, Middle East war (p. 6).
- Realised holdings can deviate from zero although expected holdings are constrained to zero (p. 6).
- Prior arbitrage methods that ignore the observation-execution lag are exposed to look-ahead bias (p. 1-2).

**Ruled out**
- Not addressed.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 10 currencies: USD, EUR, JPY, GBP, AUD, CAD, CHF, HKD, SGD, SEK. Chosen as most traded in 2022 (BIS). CNY excluded for incomplete data. | p. 6 |
| Period | Data 1995-2024, daily closes. Trading starts first trading day of 2015, 40 quarterly refits (to 2024). FXSA model evaluated from refit 5 (≈2016, computed from n_sy = 5). | p. 6 |
| Signal | Step 1: GNN forecasts next-day FX rate of each reciprocal currency pair, from past log changes of FX rates, of interest rates and of a fitted currency value. Step 2: forecasts feed the trade sizing. | p. 3-5 |
| Entry | All trades of the day executed simultaneously at day t, using information up to t-1 close (execution lag modelled). | p. 3 |
| Exit | Holdings converted back to the home currency at t+1. | p. 3 |
| Horizon | One day. | p. 3 |
| Sizing | Total trade size fixed at 1 unit of home currency per day. GNN outputs weights per exchange; projection and ReLU enforce zero expected holdings in other currencies. Loss: squared information ratio when mean P&L is positive, else minus mean P&L. | p. 4-5, Eq. 16-19, 28-29 |
| Portfolio | Three separate runs, home currency USD, EUR or JPY. Long only in exchange flows (w >= 0), no direct two-currency round trips. | p. 4-6 |
| Rebalancing | Daily trade list. Models refit each quarter, expanding window. | p. 3 |
| Costs | None. Unlimited borrowing and lending at the risk-free rate assumed. | p. 4-5 |
| Data and tools | Finaeon database. Python, PyTorch-Geometric, Gurobi. Hyperparameter grid: 9 configurations (parameters 1e4, 5e4, 1e5; layers 2, 3, 4). | p. 6 |

**Rule**
- Triangular arbitrage profit from currencies i, k, j: X_ik X_kj X_ji - 1 (p. 3).
- Benchmark LP (Eq. 3-6): maximise inflow minus outflow in the home currency o, subject to zero net holding in every other currency, total trade 1, weights >= 0, using forecast rates (p. 3).
- Gain per day: G_t = sum over currencies of [(1 + r_i)/(1 + r_o)] X_(t+1,i,o) H_ti, with H_ti the net holding after trades (Eq. 13-14, p. 4).
- Interest rate r estimated as the 1-year government bond rate divided by 365 (p. 6).
- Look-back windows for features: 1, 3, 5, 10, 15, 20 days (p. 6).

**Data provenance**
- Finaeon (GFDatabase): daily closing FX rates among the 10 currencies, plus 1, 2, 5 and 10-year government bond rates (p. 6).
- Cleaning: rescaled JPY and SEK series; removed bad values in SGDAUD, SEKEUR, AUDCHF; removed interest rates above 90% for HKD and SGD in 2022-2023 (p. 6).
- Fills: FX forward-filled up to 7 days (only for the currency value fit); interest rates up to 30 days, then regression on log maturity (p. 6).
- Direct arbitrage removed by redefining each rate as the geometric average of X_ij and 1/X_ji (p. 6).
- Government bond rates stand in for risk-free rates (p. 6).

## 3. Results

All results are real data, in the paper's rolling refit design (parameters chosen on a validation block of each refit), gross of costs.

**Aggregate** (Table 1, average of three home currencies, computed)
- GNN: information ratio 43.80%, Sortino 47.38%, return 4.76%, volatility 0.67%, max drawdown 0.91%.
- LP benchmark: information ratio 27.06%, Sortino 32.56%, return 6.17%, volatility 1.41%, max drawdown 1.64%.
- Paper's headline changes: information ratio +61.89%, Sortino +45.51%, return -22.73%, volatility -52.23%, max drawdown -44.77%, concentration (HHI) -83.12%, average holding -30.09%.
- The unit of "Info. Ratio" (daily or annual) is not stated.

**By sub-group**
- Home currency USD, EUR, JPY: near identical, information ratio 43.86, 43.54, 44.01 (GNN) and 27.21, 27.10, 26.87 (LP) (Table 1).
- Forecast step, MSE (x10^-5), GNN vs MLP: FX only 2.8680 vs 2.9112; FX/CV 2.8648 vs 2.8704; FX/IR 2.8635 vs 2.9083; FX/IR/CV 2.8650 vs 2.8710 (Table 2). Relative gap computed: -1.5% (FX/IR) to -0.2% (FX/IR/CV).
- Test of GNN over MLP (one-sided, valid tests): p-values below 0.05 in all four feature sets (Table 2). GNN with FX only does not beat MLP with FX/CV (p = 0.147) or FX/IR/CV (p = 0.113) (Table 3).

**Horizon and parameters**
- Not addressed beyond the grid of 9 network sizes. No result by look-back window or by trade size.

**Over time**
- Rolling 365-day information ratio: GNN above LP most of the time. Both peak ≈1.5 around 2019-2020 and fall in 2020, 2022, 2024 (Fig. 1).
- Cumulative P&L rises steadily for both. At the end ≈0.43 (GNN) and ≈0.55 (LP), in units of home currency (Fig. 2).
- Average absolute holding after trades: GNN below LP throughout, both rise around 2022 (Fig. 3).

**Link to other strategies**
- Not addressed.

**Inconsistencies in the source**
- None found between text and tables. Table 1 changes match the per-currency values (computed).
- Open point, not an inconsistency: text says trading starts in 2015, but Fig. 1 and 2 start in 2016-2017. The start of the FXSA evaluation is not stated (p. 5-6).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| "Superior risk-adjusted performance" is due to better risk management | p. 6 |
| Drops in 2020, 2022, 2024 come from unseen geopolitical shocks | p. 6 |
| Prior methods are "susceptible to look-ahead bias" | p. 2 |
| Constraint satisfaction "reduces risk" (a proof is given of the constraint, not of the risk) | p. 2, 5-6 |
| Approach is practically applicable despite no costs or spreads | Not argued |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Triangular arbitrage linear program]]: choose trade weights over currency exchanges to maximise home-currency gain, zero net holding elsewhere, unit total trade | technique | signal | Exploit rate inconsistencies among three or more currencies | p. 3, Eq. 3-6 |
| 2 | Currency value by least squares: fit log V_i - log V_j to log X_ij with zero mean; residual is the estimated arbitrage | technique | signal | Maximum-likelihood value of each currency if deviations are normal | p. 4, Eq. 8-9 |
| 3 | GNN on a currency graph, nodes currencies, edges exchanges, interest rates as node features | technique | signal | Capture multi-currency and rate relationships | p. 4, Eq. 10-11 |
| 4 | Observation-execution lag: forecast with data to t-1, execute at t, hold to t+1 | principle | evaluation | Prior work ignores the lag | p. 3-4 |
| 5 | Information ratio loss with projection and ReLU to enforce constraints | technique | sizing | Risk-adjusted sizing, constraints always met | p. 5, Eq. 19, 28-29 |
| 6 | Refit each quarter on an expanding window, validation block for hyperparameters | technique | calibration | Not argued | p. 3, 6 |
| 7 | Geometric average of X_ij and 1/X_ji to remove direct arbitrage | technique | universe | Assumption (1) | p. 6 |

## 6. Regime observations

- Information ratio falls in 2020, 2022 and 2024 for both methods (Fig. 1). Cause: the authors' guess (p. 6).

## 7. Acknowledged limits

- Average return is lower than the benchmark's (p. 6).
- Realised holdings differ from the zero expected value (p. 6).

## 8. Not addressed

- Transaction costs, bid-ask spreads, slippage, funding or borrowing limits, capacity.
- Whether closing-rate signals can be traded the next day at the stated prices (intraday execution data).
- Out-of-sample beyond the paper's own rolling design, other universes, other lags.
- Significance of the trading results (tests are on forecast MSE only).
- Data ids of Finaeon quotes (source and time of the daily close).
