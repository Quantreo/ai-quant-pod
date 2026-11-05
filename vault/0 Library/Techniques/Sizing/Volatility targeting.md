---
type: technique
brick: sizing
aliases: [constant ex-ante volatility, inverse volatility sizing, risk rebalancing, RR, IGARCH volatility scaling, volatility-weighted portfolio, inverse volatility weighting, constant risk position, constant volatility momentum, cvol, volatility managed portfolio, volatility timing, inverse variance scaling, closed-loop volatility targeting, feedback volatility control, open-loop volatility targeting, conditional multifactor portfolio, mix of managed and unmanaged factor, diversified risk parity, inverse risk weighting, DRP, DMV, volatility scaling, volatility-scaled returns, constant volatility exposure]
sources: 12
tested_on: [multi-asset, fx, equities, commodities, rates]
---

# Volatility targeting

> [!summary]
> Sizes each position, or the whole portfolio, inversely to its estimated volatility, so it carries a set ex-ante risk.

## How it works

- **Rule**: size = target volatility / estimated volatility, applied per position or to the whole portfolio. Variant: constant / estimated variance. Variant: no target, weights proportional to 1 / risk and normalised to sum to 1.
- **Risk estimate**: EWMA of squared returns, lagged one period, or an EWMA covariance matrix when the target is set on the portfolio. Variant: EMA of absolute price changes. Variant: full-sample volatility, known only ex post. Variant: trailing realized volatility. Variant: last month's realized variance, or its forecast.
- **Other risk measures**: variant: VaR, CVaR or maximum drawdown over a trailing window in place of volatility.
- **Intraday estimate**: variant: daily realized variance from 5-minute returns over the liquid hours, exponentially averaged, then square-rooted.
- **Mixing**: variant: hold a fixed-weight mix of the unscaled and the scaled factor, or let each factor's weight be a + b / market volatility, with a and b at least 0.
- **Feedback**: variant: scale the target by exp(kappa), kappa from the smoothed, clipped log gap between the portfolio's own realized volatility and the target.
- **Aggregation**: equal risk across the instruments available, or across sub-portfolios such as asset classes. Variant: scale each asset, then scale the portfolio again on its own volatility.
- **Implied leverage**: set by the target and the estimated volatilities, optionally capped (a cap of L means weight min(rule, L)).

## What the sources say

### Parameters
- **Moskowitz 2012**
	- 40% annual target per position (p. 233, 236).
	- EWMA centre of mass 60 days, annualised with 261 (p. 233, 236).
	- Portfolio volatility about 12% a year (p. 236).
	- Margin use about 5-20% (fn 8).
- **Daniel 2014**
	- Target set on the whole carry portfolio: 5% annual volatility (p. 10-11).
	- Covariance from IGARCH (RiskMetrics), alpha 0.06 (p. 10-11).
	- Applied to equal-weight (EQ-RR) and spread-weight (SPD-RR) carry portfolios, rebalanced monthly (p. 10-11, 28).
- **Koijen 2013**
	- Applied across asset classes: each of nine class carry portfolios weighted by inverse full-sample volatility to form the global carry factor (p. 21; Table II).
- **Lempérière 2014**
	- Quantity ±1/σ_n per contract; σ_n an EMA of absolute monthly price changes, decay n = 5 months, taken one month back (p. 3, Eq. 2).
	- No target level; P&L summed across contracts (p. 3-4).
- **Daniel 2016**
	- Whole long-short momentum strategy scaled by inverse forecast volatility, after Barroso and Santa-Clara (2012) (p. 25)
	- Volatility from daily strategy returns over the prior six months (Table 10)
	- Scaled to 19% annual volatility, in-sample (p. 25)
- **Moreira 2016**
	- Weight c / RV², RV² from the previous month's 22 daily returns, monthly (Eq. 1-2, p. 5-6).
	- c from the full sample: the scaled factor keeps the original's volatility (fn 5).
	- Single factors, including FX carry, and static MVE mixes (p. 5, 9).
	- Variants: 1/RV, AR log-variance forecast, caps at 1 or 1.5, common volatility factor (Tables 4-5, 7-8).
- **Chernov 2020**
	- Volatility timing: each strategy scaled by its conditional variance alone, mean held constant, from the model's currency covariance (Table 4B; p. 24-25).
	- TS-Mom 12 weights scaled by inverse conditional volatility (p. 16).
	- Nine G10 currencies vs USD, monthly, 1985-2020 (p. 17).
- **Devanathan 2026**
	- One risky asset and cash, daily close, weight min(exp(kappa) x target / EWMA volatility, L) (Eq. 5, p. 5).
	- Target 15% a year, L = 1.5, no short; EWMA halflife 126 days for asset and index (p. 7).
	- Feedback: kappa = (1 - theta) x clip(-g x e, [-1, 1]) + theta x previous kappa; e = log(index EWMA volatility / target); g = 55, theta = 0.6 (Eq. 3, 6; p. 7).
	- Open-loop version, same without kappa, used as benchmark (Eq. 4, p. 5).
- **Choi 2021**
	- Weights 1/ρ_i over the sum of 1/ρ_j, no volatility target, long-only; ρ = std, variance, VaR, CVaR (90/95/99%) or maximum drawdown (Eq. 2-3, 11; p. 4, 7, 12).
	- Variant 1 − ρ_i, same normalisation (Eq. 12, p. 12).
	- Window: last 6 months of daily data; ARMA-GARCH-CTS conditional estimates or raw history (p. 12).
	- 6/6 monthly: hold 6 months, a sixth of the book re-set each month (p. 12).
	- Dow Jones constituents, 1999-2020 (p. 11).

- **DeMiguel 2024**
	- Single factor: weight c / variance of the previous month's daily returns, mixed with the unmanaged factor, gamma = 5, expanding window from 120 months (Eq. 1, p. 7, 14).
	- Multifactor: factor k weighted a_k + b_k / market volatility, a_k and b_k at least 0, set by mean-variance utility net of costs (Eq. 3, 6, p. 8-9).
	- Nine US equity factors, monthly, 1977-2020 (p. 6).
- **Harvey 2018**
	- Excess return times 10% target / EWMA volatility lagged to t-2, daily, zero-mean squares (p. 4).
	- Half-lives 10, 20, 40, 60, 90 days; 270 days of warm-up (p. 4, fn 9).
	- Constant k set so the full-sample volatility equals the target, for scaled and unscaled alike (p. 4).
	- Intraday variant: 5-minute returns, 9:15 to 14:00 Chicago (p. 5).
	- Two-level variant: asset scaling to 10%, then portfolio scaling, 20-day half-life, daily rebalancing (p. 16).
- **Hood 2024**
	- Weight = target / trailing 3-month volatility, applied to the asset's own excess return, uncapped in the main version (Exhibit 1A, p. 5-6).
	- Target: full-period volatility of the unscaled asset, 17.2% on the US market factor (p. 4-5, fn 4, 7).
	- Caps of 1x, 1.5x, 2.5x tested (Exhibit 3A, p. 8).
	- 1-day lag between estimate and position; 2 bp cost per unit of notional traded (p. 4).
	- US market factor 1927-2023; 50 futures, 2000-2023, front month rolled 7 days before expiry (p. 4, 12; fn 17).

### Why
- **Moskowitz 2012**
	- Aggregates unlike contracts, with stable volatility (p. 233).
	- EWMA is simple and has no look-ahead (p. 233).
	- Equal weight: not argued.
- **Daniel 2014**
	- Mimics the VaR limits traders face (p. 10-11).
	- Unscaled equal and spread portfolios take more risk when volatility is high (p. 10-11).
- **Koijen 2013**
	- With equal weights, options and commodities would dominate the factor (p. 21, fn 18).
- **Lempérière 2014**
	- A "constant risk trading strategy" (p. 3).
	- Equal weight across contracts: not argued.
- **Daniel 2016**: benchmark for the dynamic strategy; optimal only if the strategy's Sharpe ratio were constant over time (p. 25)
- **Moreira 2016**: the mean-variance weight is proportional to mean over variance; volatility is forecastable, barely predicts returns (p. 6).
- **Chernov 2020**: volatility timing isolates the part of timing gains that comes from the conditional mean (p. 24-25).
- **Choi 2021**: penalise risky assets, the investor is risk averse; the authors tie it to the low volatility anomaly (p. 5, 16-19).
- **Devanathan 2026**
	- Volatility is latent and lagged; an open-loop forecast keeps a persistent tracking error, and feedback on the index's own volatility corrects it (p. 2, 5).
	- Log space because volatility moves multiplicatively (p. 5).

- **DeMiguel 2024**: the pricing kernel is a multifactor portfolio, so volatility management should be tested on one, not factor by factor (p. 2).
- **Harvey 2018**
	- Volatility clusters and expected return does not rise with it, so scaling can raise the Sharpe ratio (p. 2, 7).
	- Portfolio level scaling adjusts for time-varying correlation between assets (p. 17).
	- Gain comes from added momentum where a leverage effect exists (p. 19-21).
- **Hood 2024**: practitioner version, simple and easy to replicate; scaling by volatility, not variance, is what is "much more common in practical applications" (p. 4-5, fn 5).

### Evidence
- **Moskowitz 2012**: none isolated. No comparison with other sizing.
- **Daniel 2014**: real data, in-sample, gross, G10 currencies 1976-2013
	- SPD-RR has the highest Sharpe of the six strategies, 1.02 (Table 1, p. 11).
	- Worst drawdown: SPD 21.5% vs SPD-RR 10.2%; but EQ 12.0% over 94 days vs EQ-RR 14.1% over 353 days (Table 22, p. 30).
	- Monthly over daily skewness ratio, normalised to i.i.d.: EQ 7.1 vs EQ-RR 1.7; SPD 2.4 vs SPD-RR 1.3 (p. 29).
	- Max loss over a horizon: EQ and SPD exceed the bootstrap 5% bound, EQ-RR and SPD-RR mostly within (p. 31; Table 23).
- **Koijen 2013**: real data, in-sample, gross
	- Global carry factor: Sharpe 1.10, volatility 6.12%, skewness -0.02 (Table II A).
	- No comparison with an equal-weight factor.
- **Lempérière 2014**: none isolated. No comparison with other sizing.
- **Daniel 2016**: real data, in-sample, gross, cross-sectional momentum
	- US 1927-2013 Sharpe: static 0.59, constant volatility 1.02, mean-variance dynamic 1.19 (Fig. 5)
	- Higher Sharpe than static in every market and asset class 1972-2013; currencies 0.296 to 0.423 (Table 10)
	- Alpha on static WML positive in all markets, not significant in Japan and bonds (Table 10 B)
	- Spanned by the dynamic strategy everywhere: alphas about zero (Tables 7, 10 B)
- **Moreira 2016**: real data, in-sample, gross unless stated
	- Market 1926-2015: alpha 4.86% (SE 1.56), Sharpe 0.42 to 0.52; 3.63% net of 14 bp (Tables 1, 4, 5A).
	- FX carry 1983-2015: alpha 2.78% (SE 1.49); 1.77% (SE 0.90) with forecast variance (Tables 1, 8).
	- FX carry on the common volatility factor: -1.28% (SE 1.21) (Table 7).
	- Inverse vol and caps: market Sharpe 0.51 to 0.53, lower alpha (Table 5A).
- **Chernov 2020**: real data, expanding-window estimates, gross, 1985-2020
	- Alpha of the volatility-timed strategy on the original: -1.31 (Dollar, t -2.13) to 1.14 (TS-Carry, t 1.29); none significantly positive (Table 4B).
	- Timing on mean and variance does better: five or six significant alphas (Table 4A; p. 25).
	- Volatility-timed returns stay close to the originals, R² 0.571 to 0.890 (Table 4B).
- **Devanathan 2026**: real data, parameters tuned in-sample on IVV 2000-2009, net of a 5 bp spread and Fed Funds on cash
	- IVV 2000-2024, open-loop vs feedback: tracking error 2.3% vs 0.4%, Sharpe 0.33 vs 0.42, max drawdown 38.6% vs 37.1%, turnover 93% vs 1105% (Table 1, p. 9).
	- Buy-and-hold IVV: Sharpe 0.31, volatility 19.1%, max drawdown 55.3% (Table 1).
	- 44 ETFs, 2010-2024, parameters fixed from IVV: feedback tracking error below 0.6%, turnover 800% to 1800%; open-loop 70% to 100% (Fig. 4-5, p. 10-11).
- **Choi 2021**: real data, in-sample, gross, Dow Jones 1999-2020, against equal weight (Table 4)
	- Inverse variance: Sharpe 0.5402 vs 0.4967, std 17.44% vs 19.82%, max drawdown 46.41% vs 57.81%, mean 9.42% vs 9.84%, turnover 12.87% vs 6.75%.
	- Inverse max drawdown: Sharpe 0.5141, max drawdown 50.38%, turnover 12.29%.
	- 1 − ρ rules: almost equal weight (std 19.77%, Sharpe 0.4971 for std).
	- Carhart monthly alpha 0.2263 to 0.2838 vs 0.2129 for equal weight, market beta 0.81 to 0.88 (Table 5).

- **DeMiguel 2024**: real data, 1977-2020, out of sample (expanding window) unless stated
	- Market, Sharpe unmanaged then managed mix: in-sample gross 0.530 then 0.585 (p 0.242); out-of-sample gross 0.408; out-of-sample net with netting 0.433 against 0.519 (Table I A, C, E).
	- Single factors, out-of-sample net: only UMD (p 0.097), IA (0.029), BAB (0.064) beat unmanaged (Table I E).
	- Multifactor, out-of-sample net: Sharpe 1.062 against 0.940, alpha t 3.64 (Table II).
- **Harvey 2018**: real data, in-sample, gross and net of 0.5 to 3.5 bp per notional traded, 10% full-sample volatility, 20-day half-life unless stated
	- US equities 1927-2017: Sharpe 0.40 to 0.48-0.51, 1% left tail -11.4% to -8.3 / -10.1% (Table 3).
	- US bonds 1963-2017: Sharpe 0.25 to 0.05-0.09; Treasury futures 1988-2017: 0.64 to 0.63 (Tables 5-6).
	- Credit 1988-2017: 0.30 to 0.49 at 10-day half-life, 0.18 at 90-day (Table 7).
	- Balanced 60-40: 0.80 to 0.87 (assets), 0.91 (assets and portfolio); risk parity 0.80 to 0.89 to 0.91 (Tables 8-9).
	- Vol of vol and tail kurtosis fall in every asset class; currencies and commodities show no Sharpe gain (Fig. 10, A2).
- **Hood 2024**: real data, in-sample, net of 2 bp, US market factor 1927-2023 unless stated
	- Sharpe 0.54 against 0.44 buy-and-hold; skewness -0.9 against -0.2; rolling 3-month volatility error from target 4.5% against 9.3% (Exhibit 1B).
	- Alpha over buy-and-hold 3.07% (t 2.9); 1.25% (t 1.3) once a simple trend strategy is added to the regression (Exhibit 4).
	- Caps: Sharpe 0.50 (1x), 0.53 (1.5x), 0.55 (2.5x); mean leverage uncapped 1.49x, max 5.18x (Exhibit 2, 3A).
	- 2000-2023 panels: equity alpha 1.57% falls to 0.65% with trend; commodities, bonds, currencies show no trend loading (Exhibit 8).

### Limits
- **Moskowitz 2012**
	- Results said to be robust to richer volatility models (p. 233).
	- Similar with OLS and no scaling (fn 7). No numbers shown for either.
- **Daniel 2014**
	- No transaction costs (p. 4).
	- Daily analysis keeps monthly rebalancing (p. 28, fn 18).
	- Scaling did not shorten the worst EQ drawdown (Table 22).
- **Koijen 2013**
	- Weights use full-sample volatility, not an ex-ante estimate (p. 21; Table II).
	- No transaction costs.
- **Lempérière 2014**
	- Scales price changes, not percentage returns (p. 3, Eq. 2).
	- No costs, no interest on capital (p. 3, fn 5).
- **Daniel 2016**
	- Ignores that momentum's mean return falls when its volatility is high (p. 25)
	- Currency skewness stays negative, -0.47 (Table 10)
	- No costs (p. 41)
- **Moreira 2016**
	- Market weight P99 6.39 (Table 5A).
	- Costs tested on the market only (p. 11-12).
	- Market alpha 0.18% (SE 1.87) against six factors (Table 11).
	- Carry: no cost, leverage or subsample test (Tables 2-11).
- **Chernov 2020**
	- Exact weight formula of the volatility-only case not written out (p. 24-25).
	- No transaction costs (whole paper).
- **Devanathan 2026**
	- Turnover about 12 times the open-loop rule; authors say open-loop may suit illiquid assets (p. 9, 11).
	- ETF cohort kept only funds with annualized return above 5% over the test period (p. 10).
	- No significance test, no borrowing spread beyond the cash rate, no time-at-cap shown (p. 7).
	- Feedback variant adds two tuned parameters, g and theta, picked on IVV (p. 9).
- **Choi 2021**
	- No transaction costs; inverse rules turn over 9.0% to 18.7% against 6.75% (Table 4).
	- No significance test of the gap to equal weight; only the Dow Jones table is shown.
	- Lower mean return than equal weight for the 1/ρ rules (9.36% to 9.54% vs 9.84%) (Table 4).
	- Weights not scaled to a risk level, so portfolio volatility floats.

- **DeMiguel 2024**
	- Single-factor gains fail out of sample and net of costs; for the market, SMB and CMA the managed mix is below unmanaged even gross out of sample (Table I C, E; p. 17).
	- Multifactor gain depends on netting stock-level trades across factors: Sharpe 0.739 without netting against 1.062 (Table IV).
	- Nonnegativity constraints and one-month volatility chosen to match the literature (p. 9, fn 28).
- **Harvey 2018**
	- Sharpe gain only for risk assets (equities, credit); none for bonds, currencies, commodities (abstract; Tables 5-6, Fig. 10).
	- Costs are post-2008 estimates applied to all years; k fixed on the full sample (fn 13, p. 4).
	- Credit gain disappears with slow estimates; mean notional reaches 510% (Table 7).
	- Turnover 4.66 round trips a year at 10-day half-life, 0.56 at 90-day (Table 3).
	- US bond data only; bond volatility regimes before the mid-1980s (p. 11, 22).
- **Hood 2024**
	- Most of the equity alpha is trend exposure, through the leverage effect; no such link outside equities (p. 9-16).
	- Leverage averages 1.49x with peaks above 5x, and caps change the result (p. 6-8; fn 7).
	- Broad-sample alphas not significant; costs of leverage outside the futures section not charged (p. 16; fn 15).
	- Target needs the full-period volatility of the asset (fn 4).

## Sources

- [[2012 - Moskowitz Ooi Pedersen - Time Series Momentum]] (Moskowitz 2012)
- [[2014 - Daniel Hodrick Lu - The Carry Trade Risks and Drawdowns]] (Daniel 2014)
- [[2013 - Koijen Moskowitz Pedersen et al - Carry]] (Koijen 2013)
- [[2014 - Lempérière Deremble Seager et al - Two centuries of trend following]] (Lempérière 2014)
- [[2016 - Daniel Moskowitz - Momentum crashes]] (Daniel 2016)
- [[2016 - Moreira Muir - Volatility Managed Portfolios]] (Moreira 2016)
- [[2022 - Chernov Dahlquist Lochstoer - Pricing Currency Risks]] (Chernov 2020)
- [[2026 - Devanathan Rueter Boyd et al - Single-Asset Adaptive Leveraged Volatility Control]] (Devanathan 2026)
- [[2021 - Choi Kim Kim - Diversified reward-risk parity in portfolio construction]] (Choi 2021)
- [[2024 - DeMiguel Martin-Utrera Uppal - A Multifactor Perspective on Volatility-Managed Portfolios]] (DeMiguel 2024)
- [[2018 - Harvey Hoyle Korgaonkar et al - The Impact of Volatility Targeting]] (Harvey 2018)
- [[2024 - Hood Raughtigan - Volatility Targeting Is Trendy How Trend Following Explains Alpha in Volatility-Managed Strategies]] (Hood 2024)
