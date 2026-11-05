---
type: reading-note
source: paper
title: Hidden Markov Models Applied To Intraday Momentum Trading With Side Information
authors: Christensen, Turner, Godsill
affiliations: Cambridge University Engineering Department (Signal Processing and Communications Laboratory; Machine Learning Group)
year: 2020
venue: arXiv:2006.08307v1 [q-fin.TR], 15 Jun 2020
doi:
pdf: "[[2020 - Christensen - Hidden Markov Models Applied To Intraday Momentum Trading With Side Information.pdf]]"
version: preprint (v1)
tier: 1
read: full
tags: [trend, equities, intraday]
date: 2026-10-24
---

# HMM intraday momentum (Christensen, Turner, Godsill 2020)

## Summary

- **Finding**: on one year of 1-minute e-mini S&P 500 futures (2011), a two-input HMM momentum model reaches a pre-cost Sharpe ratio of about 2.0 to 2.5. The plain Baum-Welch HMM reaches about 1.0, long-only 0.4 (≈ Fig. 8, p. 18).
- **Mechanism**: the trend is a hidden state inferred from returns, so the signal can flip at trend changes without filter lag. Why trends exist: the authors cite herding and delayed over-reaction, not tested.
- **Where it works best**: the IOHMM versions, which add a volatility ratio or time of day to the transition matrix. Both predictors alone also score Sharpe ≈1.85 to ≈2.5 (≈ Fig. 6).
- **Weak spots**: the default HMM loses (Sharpe ≈ -4.5) and MCMC learning does not beat long-only (≈0.2). The authors do not know why. Costs lower Sharpe by about 15% (p. 18).
- **Main caveats**: one year, one contract. Spline knots and volatility windows chosen with the results in view. Position rule left unspecified. No test statistics printed.

Page numbers follow the printed pagination of the preprint, which matches the PDF pages. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Returns are a noisy trend: a hidden state sets the mean return, the observed return adds Gaussian noise | Model assumption (Eq. 1-2). Estimated K is 2 or 3 states: down, up, and possibly flat. | p. 4, 10 |
| 2 | Filter-based momentum signals lag; the HMM does not, so it flips sign at change points | Argued in the text. No comparison with a filter (MACD) is run. | Abstract, p. 4, 19 |
| 3 | Trend causes: herding, supply and demand, delayed over-reaction | Literature cited, none tested. | p. 2 |
| 4 | High short-term volatility lowers the probability of a positive next return | Gaussian argument, then a spline fit. | p. 11-12, 13 |
| 5 | Intraday returns depend on time of day | Spline fit on the time-of-day index. | p. 12, Fig. 5 |

**Caveats raised by the authors**
- Estimating K by a mixture likelihood "may be a fragile process" and depends on the chosen distribution (p. 10).
- The Gaussian model "suffers from overfitting and unobservability" of states (p. 10).
- Splines are "as much an art as a science"; knots and end-points are judgment calls (p. 11).
- The splines are empirical shapes and need a stronger belief in the economic story behind them (p. 13).
- Bridge sampling becomes inaccurate above about six states (p. 9).

**Ruled out**
- Not stated by the authors.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | E-mini S&P 500 future (ES), CME Globex electronic trades, front month, rolled 12 days before expiry | p. 17 |
| Period | Test: 1 Jan to 31 Dec 2011, 258 days. Learning: second half of 2010. | p. 17 |
| Signal | Hidden state m_t in K states, emission Gaussian with its own mean and variance. Forecast of the next return = sum over states of predicted state probability times state mean. | p. 4-6, 16 |
| Entry | Position from the lagged signal: strategy return = return times lagged signal. Long when the signal is positive, short when negative (stated for classical signals). | p. 10, 17 |
| Exit | Not stated by the authors. | |
| Horizon | 1-minute grid, 856 observations a day, 01:00 to 15:15 Chicago time | p. 17 |
| Sizing | The final "transfer function" TF applied to the forecast is not defined. | Alg. 4, p. 16 |
| Portfolio | One contract. | p. 17 |
| Rebalancing | Every minute. | p. 17 |
| Costs | Headline results pre-cost. Post-cost Sharpe about 15% lower; no cost model given. | p. 13, 18 |
| Data and tools | Tick data aggregated to 1-minute bars. MATLAB with PMTK and Bayesf toolboxes. | p. 17, 20 |

**Rule** (p. 16, Alg. 4): predict state weights ω(t|t-1,k) = sum over k' of a(k,k') · ω(t-1|t-1,k'), then Δŷ_t = sum over k of ω(t|t-1,k) · µ_k. Update ω(t|t,k) ∝ ω(t|t-1,k) · Normal(Δy_t; µ_k, σ_k²). Signal = TF(Δŷ_t).

**Learning of the parameters** (p. 5-10): piecewise linear regression with K = 2 chosen by cross validation (the "default" HMM); Baum-Welch with K = 3 from AIC and BIC over 1 to 50 states; MCMC with K = 3 from bridge sampling over 1 to 10 states. Means are estimated on a rolling window of 23 trading days (p. 5).

**IOHMM** (p. 13-15): the transition matrix depends on a side input X. The spline of X is cut at its roots into R buckets (R = 5 for the volatility ratio, R = 2 for seasonality). Baum-Welch is run on each bucket.

**Side predictors** (p. 11-13): normalised return (EWMA mean and volatility) regressed on X with a B-spline, zero mean, refit on the previous 66 days; evaluated at X.
- Volatility ratio: EWMA volatility with λ = 0.79 on 1-minute data, ψfast = 50 over ψslow = 100, 6 knots.
- Seasonality: minute-of-day index (T = 856), 10 knots.

**Data provenance**: no cleaning beyond the provider's (p. 17).

## 3. Results

Real data, one year, pre-cost, signal lagged one period. The authors call the 2011 simulation "truly out-of-sample" (p. 13), with the in-sample choices listed under Horizon and parameters. No test statistics are printed.

**Aggregate** (annualised Sharpe from daily returns, N = 258, risk-free 0; p. 13)

| Strategy | Sharpe | Where |
| --- | --- | --- |
| Long-only ES | 0.4 | p. 18 |
| Default HMM (PLR, K = 2) | ≈ -4.5 | ≈ Fig. 8 |
| Baum-Welch HMM (K = 3) | ≈1.0 | ≈ Fig. 8 |
| MCMC HMM (K = 3) | ≈0.2 | ≈ Fig. 8 |
| Volatility-ratio IOHMM | ≈2.5 | ≈ Fig. 8 |
| Seasonality IOHMM | ≈2.0 | ≈ Fig. 8 |
| Volatility-ratio spline alone | ≈2.5 | ≈ Fig. 6 |
| Seasonality spline alone | ≈1.85 | ≈ Fig. 6 |

**By sub-group**: Not addressed (one contract, no long and short split).

**Horizon and parameters**
- Number of states: 2 (cross validation), 3 (AIC and BIC), 3 (bridge sampling) (p. 7, 9-10).
- Knots on the volatility spline: 40 instead of 6 doubles the in-sample performance, "probably just fitting to noise" (p. 13).
- In-sample choices: ψfast = 50 and ψslow = 100 picked by a parameter sweep on "stability and predictive performance" (p. 12); knot counts picked by intuition (p. 13); λ = 0.79 set to suit 1-minute data (p. 12). The data used for the sweep are not stated.
- Learned means: Baum-Welch µ = [-0.0198, -0.00573, 0.0183], MCMC µ = [-0.122, -0.0117, 0.121] (p. 17).

**Over time**
- ES return over 2011 gives a Sharpe of about 0.4 (p. 18). Cumulative-return chart (≈ Fig. 8): volatility-ratio IOHMM ends near +50%, default HMM near -75%.

**Link to other strategies**
- Correlation with long-only (≈ Fig. 6): volatility ratio 0.17, seasonality -0.48. Between the two predictors -0.15.
- Baum-Welch and MCMC returns correlate 0.41 (p. 18).

**Inconsistencies in the source**
- The abstract says "the models have a Sharpe ratio in excess of 2.0". Fig. 8 shows this for the two IOHMMs only; Baum-Welch ≈1.0, MCMC ≈0.2, default negative.
- p. 18 says the IOHMM Sharpe is smaller than that of the individual predictors. The bars read ≈2.5 and ≈2.0 in Fig. 8 against ≈2.5 and ≈1.85 in Fig. 6, so not smaller.
- p. 5 says means are estimated on a rolling 23-day window. p. 17 says learning is done on the second half of 2010.
- p. 2 says the experiments include transaction costs and slippage. Section 7 gives pre-cost results and a 15% figure with no cost model.
- The abstract speaks of "statistically significant relationships" for the splines. No test statistic or p-value is shown.
- Cumulative return of the volatility predictor ends near +9% in Fig. 6 and near +50% in Fig. 8, with a similar Sharpe. Position scaling is not given.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| The HMM "does not suffer from lagging" and flips at change points | Abstract, p. 19; no filter comparison |
| In MACD experiments only the signal sign has traction, not its size | p. 10; results not shown |
| Post-cost results reduce the Sharpe by about 15% | p. 18; no cost model |
| The momentum effect "is viable at higher trading frequencies" | p. 19; one year, one contract |
| An HMM "would outperform" the Rao-Blackwellised particle filter | p. 4; not tested |
| The IOHMM solves the signal combination problem | Abstract, p. 19; no comparison with a weighted mean (listed as future work, p. 20) |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Hidden Markov model of a latent trend, forecast = state-probability-weighted state means | technique | signal | No filter lag. Card [[Regime probability filter]] | p. 4-6, 16 |
| 2 | IOHMM: transition matrix conditioned on side information, one matrix per spline bucket | technique | signal | Signal combination problem. Card [[Regime probability filter]] | p. 13-15 |
| 3 | Ratio of fast to slow EWMA volatility mapped to the next return by a spline | technique | signal | Rising volatility lowers the odds of a positive return. Card [[Volatility regime filter]] | p. 11-13 |
| 4 | Time-of-day spline on the 1-minute return, refit on a rolling 66-day window | technique | signal | Intraday seasonality is documented. Card [[Intraday seasonality signal]] | p. 12-13 |
| 5 | Compare with long-only ES, Sharpe 0.4 | technique | evaluation | Benchmark. Card [[Always-long benchmark comparison]] | p. 13, 18 |
| 6 | Number of states by cross validation, AIC and BIC, bridge sampling | technique | calibration | Not argued beyond the literature. No card: tied to this model | p. 6-10 |
| 7 | Baum-Welch versus MCMC learning | technique | calibration | Simplicity and speed (p. 10). No card: tied to this model | p. 7-10 |
| 8 | Daily aggregation of intraday returns for the Sharpe ratio | technique | evaluation | More stable than scaling by the square root of N (p. 13). No card: standard practice | p. 13 |

## 6. Regime observations

- The volatility spline reads: a ratio near 0.6 (risk falling) suggests buying, near 0.8 (risk rising) suggests selling (p. 13, ≈ Fig. 5).
- The seasonality spline is positive early in the day and negative later (≈ Fig. 5).
- Strategy performance by sub-period: Not addressed.

## 7. Acknowledged limits

- MCMC learning underperforms and the cause is unclear: prior, proposal density, point estimate, or local maxima (p. 17-18).
- Fully Bayesian inference and model averaging are left as future work (p. 19).
- Asynchronous data and non-parametric emission are only sketched (p. 16-17, 19).

## 8. Not addressed

- Position size, the transfer function, holding time, number of trades.
- Transaction cost level, slippage, capacity.
- More than one year, more than one contract, any other period.
- Statistical significance of the Sharpe ratios.
- The choice of the volatility windows and knot counts on data outside the test year.
