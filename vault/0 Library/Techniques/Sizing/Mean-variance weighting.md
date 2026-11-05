---
type: technique
brick: sizing
aliases: [maximum mean-CVaR portfolio, mean-CVaR optimisation, mean-variance optimal weights, OPT carry, inverse covariance times signal, dynamic momentum, maximum Sharpe ratio timing, mu over sigma squared scaling, unconditional MVE portfolio, UMVE, conditional mean-variance efficient portfolio, CMVE, SDF projection portfolio, optimal factor timing, Pure anomaly timing, Factor timing portfolio, Regime-forecast mean-variance, Minimum variance among bull assets]
sources: 6
tested_on: [fx, equities, commodities, rates, multi-asset]
---

# Mean-variance weighting

> [!summary]
> Sets weights to the inverse covariance matrix times the signal used as expected return, scaled to a volatility target.

## How it works

- **Rule**: weights proportional to H^-1 mu, with mu the expected returns taken from the signal and H the covariance matrix. Variant: one strategy timed over time, weight proportional to its forecast mean over its forecast variance.
- **Risk estimate**: an estimated covariance matrix of the assets.
- **Aggregation**: the optimiser sets relative weights; one scalar scales the book to the target volatility.
- **Implied leverage**: set by the target and the estimated covariance.
- **Variant**: expected returns from several signals combined by a rolling or expanding panel regression; covariance from shrunk realized daily covariance.
- **Variant**: constrained optimiser (long-only, weight cap, leverage at most 1, rest in the risk-free asset) with a risk term and a trading cost term. Expected return from a regime forecast per asset; equal inputs for all bull assets give a minimum-variance portfolio among them.
- **Variant**: variance replaced by conditional value-at-risk computed on simulated return scenarios; maximise expected return over CVaR, long only, weights sum to 1.

## What the sources say

### Parameters
- **Daniel 2014**
	- mu = one-month interest differentials vs USD (Eq. 10, p. 11).
	- H from IGARCH (RiskMetrics), alpha 0.06 (p. 10-11).
	- Scaled to 5% annual volatility, rebalanced monthly (Eq. 10, p. 11, 28).
- **Daniel 2016**
	- Time-series variant on one strategy: w = (1/2λ)·μ/σ², reset monthly (Eq. 5, p. 24)
	- μ: fitted value of a regression of momentum returns on a bear-market indicator, market variance and their product (Table 5 col. 5, p. 24)
	- σ: fitted future 22-day volatility from GJR-GARCH and 126-day realized volatility (App. D, p. 46)
	- λ set so the in-sample annual volatility is 19% (p. 25)
- **Chernov 2020**
	- Weights (1 + θ)^-1 E' V^-1, θ the maximal conditional squared Sharpe (Eq. 8-9, p. 13).
	- E = forward discount (loading fixed at 1) + δ value + φ S(t)/S(t-12); δ, φ from monthly panel regressions, expanding window (p. 12, 18).
	- V: monthly realized covariance of daily changes, Ledoit-Wolf shrinkage, EWMA λ = 0.94 (App. A.1).
	- Timing variant: the same formula on one strategy's return, using its known weights (p. 24).
	- Nine G10 currencies vs USD, monthly, 1985-2020 (p. 17).
- **Haddad 2020**
	- Weights Σ_Z^{-1} E_t[Z] on the market and five PCs of 50 anomalies; Σ_Z homoskedastic, from the forecast residuals (Eq. 10-11, p. 15, 35-36)
	- Variants: factor investing (unconditional means), market timing, anomaly timing, and pure anomaly timing with zero average weights, using E_t[Z] - E[Z] (Eq. 12-15, p. 37)
	- Monthly, 1974-2017; parameters from the first half for out-of-sample (p. 21, 36)
- **Shu 2024**
	- Maximise w'mu minus gamma_risk w'Sigma w minus gamma_trade times 5 bp times the L1 distance to previous weights; long-only, cap 40%, leverage at most 1 (Eq. 2-4, p. 17)
	- MinVar variant: mu = 10 bp for assets forecast bull, 0 for bear (p. 18-19)
	- MV variant: mu = average past return of periods in the forecast regime, bear capped at -10 bp (p. 19)
	- Sigma: EWM covariance, half-life 252 days; gamma_risk 10, gamma_trade 1; cash if three or fewer assets are bull (p. 19)
	- Daily, 12 USD asset indexes, test 2007-2023 (p. 4, 21)
- **Luo 2013**
	- Max Sharpe and max mean-CVaR (expected return over CVaR), long only, fully invested (p. 34-36)
	- Expected returns: trailing one-year average, long-term average (look-ahead), or a VRP and regime regression (p. 31)
	- Scenarios from a GARCH-DCC-copula model; 20 runs averaged for the factor case (p. 59, 64)
	- 11 asset classes (2000-2013), 5 equity factors (2004-2013), monthly (p. 22, 56, 64)

### Why
- **Daniel 2014**: currency moves are essentially unforecastable (Meese-Rogoff), so the differential stands for the expected return (p. 11).
- **Daniel 2016**: maximises the unconditional Sharpe ratio when the strategy's mean and variance vary over time (App. C, p. 44-45)
- **Chernov 2020**
	- A small cross-section makes the covariance precise; a few signals give the conditional mean (p. 1, 9).
	- Timing: conditional premiums vary about as much as their level, 3.4% vs 3.2% (p. 4).
- **Haddad 2020**: the maximum Sharpe ratio factor timing portfolio is the SDF; gain from timing = sum of R²/(1 - R²) over components (Eq. 7, p. 13)
- **Shu 2024**: return forecasts move the optimiser more than covariance forecasts, so regimes enter through the return input (p. 19)
- **Luo 2013**: CVaR suits non-normal returns, which mean and variance cannot capture (p. 35)

### Evidence
- **Daniel 2014**: real data, in-sample, gross, G10 1976-2013
	- Mean 2.10%, the lowest of six strategies (Table 1).
	- Skewness -0.89, the most negative (p. 12).
	- Worst month -4.01%, the smallest; 303 positive months of 451, the most (p. 12).
	- FF3 alpha 1.83% (t 3.72), the lowest (Table 3).
- **Daniel 2016**: real data, in-sample parameters, gross, cross-sectional momentum
	- US 1927-2013 Sharpe 1.19 vs 0.59 static and 1.02 constant volatility (Fig. 5)
	- Higher Sharpe than constant volatility in every market 1972-2013; Japan 0.067 to 0.416, currencies 0.296 to 0.653 (Table 10)
	- Alpha over constant volatility, US conditional FF3: 6.10% a year (t = 6.08) (Table 7)
	- Bonds still fail: Sharpe 0.066 (Table 10)
- **Chernov 2020**: real data, expanding-window estimates, gross, 1985-2020
	- Sharpe 1.075; with carry-only expected returns 0.871 (Table 1D).
	- Mean only (identity covariance) 0.565; covariance only (constant mean) 0.165 (Table 3).
	- Timing alpha on the original strategy significant for Dollar (3.75, t 2.72) and the four momentum strategies (t 2.06 to 2.92) (Table 4A).
- **Haddad 2020**: real data, 1974-2017, gross
	- Sharpe in / out of sample: factor investing 1.27 / 0.76; factor timing 1.19 / 0.87; pure anomaly timing 0.71 / 0.77 (Table 6)
	- Information ratio against factor investing: 0.36 in sample, 0.42 out of sample (Table 6)
	- Expected utility 1.66 (investing) to 2.96 (timing) (Table 6)
- **Shu 2024**: real data, walk-forward 2007-2023, net of 5 bp one-way
	- MinVar Sharpe 0.70 to 1.12 with regime inputs; MDD -19.3% to -7.1% (Table 6, p. 24)
	- MV Sharpe 0.37 to 1.02; MDD -25.6% to -13.5% (Table 6)
	- Gamma_risk 5, 10, 20: Sharpe 1.01, 1.02, 0.96 (Table 9, p. 28)
- **Luo 2013**: real data, monthly refits, gross or net not stated
	- 11 assets, alpha-based rules, average Sharpe ≈0.83 rolling, ≈1.15 expanding, ≈1.18 copula risk model (≈ Fig. 77)
	- Factor rotation, max mean-CVaR: Sharpe 0.91 vs 0.54 (risk parity) and 0.63 (max diversification); max drawdown -9.2% vs -5.4% and -3.1% (Fig. 106-107)
	- Max Sharpe on one-year average returns: Sharpe ≈0.33 with rolling risk (≈ Fig. 77)

### Limits
- **Daniel 2014**
	- No transaction costs (p. 4).
	- LRV FX factor alpha 1.29%, the lowest of the six (Table 4).
- **Daniel 2016**
	- Forecast regression, GARCH and λ fitted on each full sample (p. 24-25; App. D)
	- Leverage and turnover of the weights not reported
	- No costs (p. 41)
- **Chernov 2020**
	- Timing adds nothing to CS-Carry (t 0.46) or CS-Value (t -0.62) (Table 4A).
	- Leverage k(t) left free; portfolio volatility and drawdowns not reported (p. 8).
	- No sensitivity to λ or signal windows; no transaction costs (whole paper).
- **Haddad 2020**
	- No transaction costs; monthly turnover 41% (A13)
	- Leverage scale of the weights not stated (p. 35)
	- Text gives the out-of-sample Sharpe range as 0.63 to 0.87, Table 6 shows 0.96 for anomaly timing (p. 37)
- **Shu 2024**
	- Turnover 2.06 (MinVar) and 9.12 (MV) with regime inputs; unit not defined (Table 6, p. 24)
	- Sensitivity covers gamma_risk and gamma_trade only, on the test period (Tables 8-9)
	- Baseline MV uses a 5-year EWMA mean, which the authors call simplistic (p. 19)
- **Luo 2013**
	- The long-term alpha uses the whole history, a look-ahead (p. 31)
	- A good alpha model does not always give a better portfolio (fn 24, p. 48)
	- Factor-rotation baselines use rolling risk, not the same risk model (Fig. 106)

## Sources

- [[2014 - Daniel Hodrick Lu - The Carry Trade Risks and Drawdowns]] (Daniel 2014)
- [[2016 - Daniel Moskowitz - Momentum crashes]] (Daniel 2016)
- [[2022 - Chernov Dahlquist Lochstoer - Pricing Currency Risks]] (Chernov 2020)
- [[2020 - Haddad Kozak Santosh - Factor Timing]] (Haddad 2020)
- [[2024 - Shu Yu Mulvey - Dynamic Asset Allocation with Asset-Specific Regime Forecasts]] (Shu 2024)
- [[2025 - Luo Wang Jussa - Dynamic allocation extremes, tail dependence, and regime Shifts]] (Luo 2013)
