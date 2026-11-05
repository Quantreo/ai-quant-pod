---
type: technique
brick: signal
aliases: [Three-state volatility HMM, Volatility regime HMM, Bull probability filter, Wonham filter, Hidden Markov model state probability, HMM turbulent state, Turbulent state probability, Latent momentum HMM, IOHMM, Statistical jump model, Cluster-then-classify regime forecast, 0/1 regime-switching strategy, Macro regime clustering, Modified k-means regime probabilities, Markov-switching risk regime, Dynamic regime switching on CVaR]
sources: 7
tested_on: [equities, multi-asset]
---

# Regime probability filter

> [!summary]
> Turns daily returns into the probability that the market is in an uptrend state, and uses that probability as the trading signal.

## How it works

- **Inputs**: price series; assumed drift of the up state and of the down state; volatility; switching rates between the two states.
- **Formula**: each day, the new probability is the old one, plus a drift correction, plus the day's log return scaled by the gap between the two drifts. It is clipped to [0, 1].
- **Lookback / holding**: recursive, no fixed window. It starts from a prior probability.
- **Output**: a probability between 0 and 1.
- **Direction**: rises after price rises, falls after price falls.
- **Tested on**: equity indexes.
- **Variant**: a two-state hidden Markov model fitted by maximum likelihood on the strategy's and the market's returns jointly; the output is the probability of a risky state, used to forecast crashes or to switch a hedge, not to pick direction.
- **Variant**: hidden Markov trend model with two or three states; the forecast is the state probabilities times the state means. A side input can condition the transitions.
- **Variant**: three-state Gaussian hidden Markov model on a volatility series; the predicted state is a regime label that selects an allocation.
- **Variant**: two steps per asset. A two-state jump model (temporal clustering with a fixed cost per state change) labels past periods bull or bear from return features; a classifier trained on those labels, with return and macro features, gives the bull probability for the next period. The flag holds the asset or the risk-free asset.
- **Variant**: regimes from a vector of monthly macro series, not from returns: standardize, PCA, split outlier months by clustering, cluster the rest, and turn centroid distances into regime probabilities.
- **Variant**: two-state Markov-switching model on a risk gauge (the predicted CVaR of a fixed asset mix), with serially correlated errors; a side variable moves the state means and the transition probabilities; the high-risk state is the one with probability of 50% or more.

## What the sources say

### Parameters
- **Dai 2011**
	- Daily update, dt = 1/252 (p. 10)
	- Drifts, switching rates and volatility estimated from past bull and bear markets, moves of at least 20% (p. 12)
	- Re-estimated every January, with trends confirmed before that date (p. 12)
- **Daniel 2012**
	- States calm and turbulent; momentum return on market return and max(market return, 0), state-dependent coefficients and volatility; market mean and volatility by state (Eq. 2-3, p. 13-14)
	- 14 parameters by maximum likelihood; probability updated by Bayes' rule, started at the steady state (Eq. 5-10, p. 14-17)
	- Residuals: momentum Normal, market Student-t with 5 d.f., chosen by simulated moment matching (p. 18-19; Table 6)
	- Out-of-sample variant: expanding window from 1937, monthly (Fig. 2B)
- **Christensen 2020**
	- K = 2 (cross validation) or 3 (AIC, BIC, bridge sampling); Gaussian emission per state (p. 7, 9-10)
	- Baum-Welch learning; means on a rolling 23-day window (p. 5, 7)
	- Forecast = predicted state probability times state mean (Alg. 4, p. 16)
	- IOHMM: side-input spline cut at its roots into R buckets, one transition matrix each; R = 5, 2 (p. 15)
	- E-mini S&P 500, 1-minute bars, test year 2011 (p. 17)
- **Verma 2026**
	- Three-state Gaussian HMM, EM estimation, forward filter, 2 and 3 states compared by AIC and BIC (p. 2-3; Table 1)
	- Input series not stated; Table 2 means and sds are on the scale of a VIX change (p. 3)
	- Daily, one-day execution lag, 70% train, 30% test (p. 5)
- **Oliveira 2025**
	- 127 FRED-MD series (interest and exchange rate group removed), t-code transform, standardize, PCA to 95% of variance, 61 components (p. 7)
	- K-means L2 with k = 2: the smaller cluster is Regime 0, outlier months. Cosine k-means on the rest, k = 5 by the elbow heuristic (p. 5, 7)
	- P(Ci) from centroid distances di: (1 - di/Σdj), renormalized (Eq. 1, p. 6); Regime 0 weight -Pmax·log2(1 - P(Regime 0)) (Eq. 4, p. 6)
	- Dec 1959 to Jan 2023, monthly (p. 7)
- **Shu 2024**
	- One model per asset; 2-state jump model on 8 EWM features of the excess return: downside deviation (log; half-lives 5, 21), average return and Sortino ratio (half-lives 5, 10, 21) (Table 2, p. 10-11)
	- Bull is the state with the higher cumulative excess return; jump penalty on a log grid from 0 to 100 (p. 10, 13)
	- Labels shifted one day; XGBoost, default settings, 8 features plus 5 macro-features (2-year yield, curve slope, VIX, stock-bond correlation); threshold 0.5; probability EWMA-smoothed, half-life 0 to 8 days by asset (Table 3, p. 11-12, fn 14)
	- Refit every 6 months on 11 years; penalty re-chosen every 6 months by the Sharpe ratio of the 0/1 strategy over the previous 5 years (p. 13-14)
	- 12 USD total return indexes, daily, 1991-2023, test 2007-2023 (p. 4, 14)
- **Luo 2013**
	- Gauge: CVaR of a 50/40/10 equity, bond, commodity mix, from 10,000 simulated 21-day paths (p. 5, 19)
	- CVaR_t = mu(s_t) + phi(CVaR_{t-1} - mu(s_{t-1})) + sigma(s_t) eps_t; mu(s_t) and the transition probabilities depend on VRP lagged one month (p. 38)
	- True out-of-sample version: refit every month on data to that date, use the last predicted probability (p. 40-41)
	- High risk if probability is 50% or more; the same model on predicted correlation (p. 41, fn 18)

### Why
- **Dai 2011**
	- Only the price is observable, so a filter infers the state (p. 5-6, 10)
	- The probability moves with the price, so the rule buys only into rises (Eq. 13, p. 9)
- **Daniel 2012**: losers' effective leverage cannot be measured and state-variable windows are arbitrary, so a hidden state summarises market conditions (p. 12-13)
- **Christensen 2020**
	- No lag at trend changes, unlike a digital filter (p. 4, 19)
	- Side information added because momentum does not explain all variance (p. 13)
- **Verma 2026**: volatility clusters and breaks, so regimes are persistent and asset payoffs differ by regime (p. 1-3)
- **Oliveira 2025**
	- Macro data is steadier than returns, so regimes are less noisy (p. 2)
	- Distance-based probabilities give smooth transitions, unlike the near-binary GMM probabilities (p. 8)
- **Shu 2024**
	- Regimes are a smoothed version of returns, so a better signal-to-noise ratio than raw return forecasts (p. 8)
	- A separate forecaster has its own features and is tuned on the money result, not on label accuracy (p. 7, 14)
- **Luo 2013**
	- Risk is easier to predict than returns; the same model on returns fails to converge for treasuries and high yield (p. 54-55)

### Evidence
- **Dai 2011**: real data, ex-ante, filter plus two thresholds, long or flat. Gross or net not stated.
	- S&P 500 1972-2011: 11.03% a year, quarterly Sharpe 0.217, vs 9.8% and 0.128 buy and hold (Table 4, p. 14)
	- SSE index 2001-2011: 14.0%, Sharpe 0.263, vs 2.58% and 0.083 buy and hold (Table 4, p. 14)
- **Daniel 2012**: real data, US momentum 1927-2013, full-sample parameters unless stated, gross
	- All 13 losses below -20% come with probability above 80% (155 of 1044 months); mean momentum return there -1.01% a month (Table 7, p. 37-38)
	- 114 false positives at the -20% threshold, vs 150 without the call term and 147 to 256 for volatility measures (Table 8)
	- Out-of-sample 1980-2013: losses below -20% at probability ≈0.85 or above (≈ Fig. 2B)
- **Christensen 2020**: real data, one year, pre-cost, signal lagged one period
	- Baum-Welch HMM Sharpe ≈1.0, long-only 0.4 (≈ Fig. 8, p. 18)
	- IOHMM with volatility ratio ≈2.5, with seasonality ≈2.0 (≈ Fig. 8)
	- MCMC HMM ≈0.2, default HMM ≈ -4.5 (≈ Fig. 8)
- **Verma 2026**: real data, SPY, TLT, GLD daily, 30% test window of about 6.3 years (computed), gross, costs zero (p. 6)
	- Regime-driven rotation test Sharpe 0.79 (Top-1), 0.82 (60/40), against SPY 0.65 and equal-weight 0.83 (Table 7)
	- Crisis state is 6.18% of days (Table 3)
- **Oliveira 2025**: real data, in-sample classification; used in walk-forward allocation, gross
	- Regimes line up with NBER recessions, shown as a chart only (Fig. 2, p. 9)
	- Regime 0 has the lowest income, sentiment and fed funds rate and the highest unemployment (Fig. 4, p. 9)
	- With regime conditioning, ridge Sharpe beats random regimes, p = 0.004 (Fig. 9, p. 17)
- **Shu 2024**: real data, walk-forward 2007-2023, 0/1 strategy per asset, net of 5 bp one-way
	- Sharpe against buy and hold: LargeCap 0.79/0.50, EM 0.85/0.20, HighYield 1.88/0.67 (Table 4, p. 22)
	- Max drawdown lower for all 12 assets; LargeCap -55.25% to -17.69% (Table 4)
	- Jump model alone: Sharpe below buy and hold for SmallCap, AggBond, Treasury, Gold (Table 4)
- **Luo 2013**: real data, true out-of-sample refits, 1998-2013, gross or net not stated
	- Portfolio CVaR about 47% higher in high-risk regimes (p. 42)
	- Equities and REITs earn less in high-risk regimes, bonds and commodities more (Fig. 65)
	- With the regime dummy, forecast IC/sd 2.31 vs 1.53 without (Fig. 73-74, p. 48)
	- Correlation of the true out-of-sample probability with the one-step prediction: 68% (Fig. 63)

### Limits
- **Dai 2011**
	- Sensitivity to parameters is expected; apply test results with caution (p. 14)
	- The regime model may be a crude approximation of real markets (p. 17)
- **Daniel 2012**
	- 8 of 12 gains above 20% also fall above 80% (Table 7)
	- At the -10% threshold more false positives (902) than market RV 12m (796) (Table 8)
	- Out-of-sample shown as a chart only (Fig. 2B)
- **Christensen 2020**
	- One contract, one year; position rule not defined (Alg. 4, p. 16)
	- MCMC learning underperforms, cause unknown (p. 17-18)
	- Post-cost Sharpe about 15% lower, no cost model (p. 18)
- **Verma 2026**
	- Filtered or smoothed regime in the test window not stated; Figures 7-8 use the Viterbi path and smoothed probabilities (p. 3)
	- Number of crisis episodes in the test not reported (Table 3 gives time share only)
	- No costs; gaussian emissions miss heavy tails (p. 6-7)
- **Oliveira 2025**
	- k-means "crisis" probability stays ≈0.45 to 0.49 all along (≈ Fig. 3, p. 10)
	- k, PCA size and probability formula fixed on the full sample; whether they run inside the 48-month window is not stated (p. 7, 16)
	- No costs (whole paper)
- **Shu 2024**
	- Gold Sharpe 0.31 against 0.43 buy and hold; out of the market over 60% of the time (Table 4, p. 23)
	- Forecasts lag turning points, for example 2015-2016 (p. 15)
	- Features, windows and thresholds: no account of how they were picked (not addressed)
- **Luo 2013**
	- Model fit rests on one point, Nov 2008 (p. 38-39)
	- Correlation regime only flags two episodes since 1998 (p. 43)
	- No costs, no test of the IC gain (whole paper)

## Sources

- [[2011 - Dai Zhang Zhu - Optimal Trend Following Trading Rules]] (Dai 2011)
- [[2012 - Daniel Jagannathan Kim - Tail Risk in Momentum Strategy Returns]] (Daniel 2012)
- [[2020 - Christensen - Hidden Markov Models Applied To Intraday Momentum Trading With Side Information]] (Christensen 2020)
- [[2026 - Verma Putri Lesupi - Regime-Based Portfolio Allocation Using Hidden Markov Models and Reinforcement Learning]] (Verma 2026)
- [[2025 - Oliveira Sandfelder Fujita et al - Tactical Asset Allocation with Macroeconomic Regime Detection]] (Oliveira 2025)
- [[2024 - Shu Yu Mulvey - Dynamic Asset Allocation with Asset-Specific Regime Forecasts]] (Shu 2024)
- [[2025 - Luo Wang Jussa - Dynamic allocation extremes, tail dependence, and regime Shifts]] (Luo 2013)
