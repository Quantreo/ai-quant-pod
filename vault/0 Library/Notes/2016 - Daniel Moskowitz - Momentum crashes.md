---
type: reading-note
source: paper
title: Momentum Crashes
authors: Daniel, Moskowitz
affiliations: Daniel (Columbia University, NBER), Moskowitz (Chicago Booth, NBER); Moskowitz discloses an ongoing relationship with AQR Capital (cover page)
year: 2014
venue: NBER Working Paper 20439
doi:
pdf: "[[2016 - Daniel Moskowitz - Momentum crashes.pdf]]"
version: NBER working paper w20439, August 2014 (not the published version)
tier: 1
read: full
tags: [trend, multi-asset, monthly]
date: 2026-10-23
---

# Momentum crashes (Daniel, Moskowitz 2016)

## Summary

- **Finding**: US equity winner-minus-loser momentum (1927-2013) crashes after market declines, in high volatility, when the market rebounds. A dynamic weight on forecast mean over variance roughly doubles Sharpe, gross.
- **Mechanism**: after bear markets losers carry high, convex market beta; WML behaves like a short call on the market. Losers' option-like payoff seems underpriced. Source left open.
- **Where it works best**: dynamic version beats static and constant-volatility momentum in every market tested; all-asset combination Sharpe 1.139 to 1.223 (Table 10).
- **Weak spots**: fixed income momentum fails, even dynamic (Sharpe 0.066). Ex-ante beta hedging does not help. Outside equities and FX, panic-state coefficients mostly insignificant; currency optionality insignificant.
- **Main caveats**: no transaction costs; forecasting regression, GARCH and scaling fitted on each full sample; leverage and turnover of the dynamic strategy not shown.

Page numbers follow the working paper pagination (p. 1 = PDF page 3). The library cites this source as Daniel 2016 (file name); this PDF is dated August 2014. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | After a market fall, losers are high-beta and winners low-beta, so WML has a large negative beta into a rebound | Loser beta ≈3.5 (1930s) and ≈5.5 (2002); text: "as high as 4 or 5". WML beta 1.131 lower in bear markets (t = -13.4) | Fig. 3; p. 2, 13; Table 3 |
| 2 | In bear markets WML is short a call on the market | Up-market beta increment -0.815 (t = -4.5), mostly from losers (+0.600, t = 4.4); absent in bull markets (WML -0.242, t = -1.3) | Tables 3, 4; p. 15-16 |
| 3 | The price of past losers does not reflect this optionality, so momentum's premium is low in panic states | Bear indicator times market variance forecasts low WML returns | p. 19, 40; Table 5 |
| 4 | For equities, levered losers' stock is a call on firm assets (Merton 1974) | Loser firms in March 2009 down 84% from peak, highly levered | p. 4, 10 |
| 5 | Possibly behavioural: fear, focus on losses in extreme states | None; references only | p. 40 |

**Caveats raised by the authors**
- Claim 4 does not fit futures, bonds, currencies, commodities, which show the same optionality (p. 4-5, 34, 36, 40).
- Claim 5 is speculation left to future research (p. 5, 40).
- Crashes are few, and data mining across studies is a risk; hence the out-of-sample markets (p. 4).

**Ruled out**
- Time-varying market beta does not explain low panic-state returns (p. 21; Table 3 col. 2-4).
- Variance risk is only partial: the panic-state premium change is unchanged after controlling for variance swap returns (Table 6, p. 23).
- Fama-French factors with panic-state interactions do not explain it (Table 11, p. 43).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe (US) | CRSP common shares (codes 10, 11), NYSE, AMEX, NASDAQ; valid price and shares; at least 8 monthly returns over the past 11 months | p. 5 |
| Universe (other) | EU, JP, UK, US stocks; 18 equity index futures; 10 developed currencies; 10 government bonds; 27 commodity futures; data of Asness, Moskowitz, Pedersen (2013) | p. 30 |
| Period | US 1927:01-2013:03; others from 1972-1983 to 2013:05 | p. 5, 30 |
| Signal | Cumulative return t-12 to t-2, one month skipped | p. 5-6 |
| Portfolio | US: top decile minus bottom decile, value weighted. International: top third minus bottom third, value weighted | p. 6, 31 |
| Rebalancing | Monthly; membership fixed within the month except delisting | p. 5-6 |
| Panic state | I_B = 1 if past 24-month market return negative; σ²_m = variance of daily market returns over the past 126 days; I_Bσ² = I_B·σ²_m / (full-sample mean of σ²_m in bear months) | p. 15, 20, 22 |
| Sizing, cvol | Weight inverse to strategy volatility from daily returns over the prior 6 months | Table 10 |
| Sizing, dyn | w = (1/2λ)·μ/σ²; μ fitted from Table 5 col. 5; σ from GJR-GARCH plus 126-day realized volatility; λ sets 19% annual volatility in-sample | p. 24-25; App. C, D |
| Costs | None; long-short with margin earning the risk-free rate | p. 6, 41 |

**Rule** (Eq. 5, p. 24): w*_{t-1} = (1/2λ) · μ_{t-1} / σ²_{t-1}. μ is the fitted value of R_WML on I_B, σ²_m and I_B·σ²_m. σ is the fitted future 22-day WML volatility from 0.0010 + 0.6114 σ_GARCH + 0.2640 σ_126 (R² 0.617) (App. D, p. 46).

**Data provenance**
- US: CRSP, close to close; market and T-bill from Ken French's library; daily risk-free from the monthly rate (p. 5-6).
- Other markets: Asness, Moskowitz, Pedersen (2013), updated monthly; details deferred to that paper (p. 30).
- Market index per class: MSCI local (equities), MSCI World (index futures), equal-weight of all country bonds, equal-weight of all currencies, GSCI (p. 30).
- EU, JP, UK daily MSCI only from 1990; before, monthly variance over 6 months (fn 11, p. 32).
- Variance swap returns built from VIX and S&P 500, 1990-2013 (App. A.2).

## 3. Results

All real data, in-sample, gross. Composite weights (GE, GA, GAll) use full-sample volatility (p. 30).

**Aggregate (US, 1927-2013)**
- WML: 17.9% a year, volatility 30.0%, alpha 22.2% (t = 7.3), beta -0.58, Sharpe 0.60, monthly skewness -4.70 (Table 1).
- 14 of the 15 worst WML months follow a negative 2-year market; all 15 come with a rising market. Worst: Aug 1932 -74.36%, Jul 1932 -60.98% (Table 2).
- Crashes are slow, over months; losers "crash up": Jul-Aug 1932 losers +232%, winners +32%; Mar-May 2009 losers +163%, winners +8% (p. 10).
- Sharpe, 1927:07-2013:03: WML 0.59, cvol 1.02, dyn 1.19 (Fig. 5 legend).
- Spanning: dyn alpha on market and WML 23.74% (t = 11.99); on FF3 and cvol, conditional, 6.10% (t = 6.08); cvol on dyn about zero (Table 7).

**By sub-group**
- Subsample Sharpe, WML / cvol / dyn: 1927-49 0.25 / 0.61 / 0.67; 1950-74 1.13 / 1.33 / 1.48; 1975-99 1.18 / 1.36 / 1.48; 2000-13 0.22 / 0.50 / 0.76 (Fig. 5).
- International equities: panic-state coefficient negative and significant in EU, JP, UK, US, GE (-6.5 to -11.4% a year) (Table 8 D). Bear-market optionality significant in EU, JP, UK, GE, not in US 1972-2013 (Table 8 B).
- Japan: static Sharpe 0.067, dyn 0.416 (Table 10).
- Fixed income: static 0.004, dyn 0.066; no bear-state effect (Tables 9, 10).
- Commodities: only class with significant optionality (-1.102, t = -2.5) (Table 9 B).
- Dyn skewness positive in most markets; negative for FX (-0.20) and GA* (-0.19) (Table 10).

**Currencies (10 developed, 1980-2013)**
- Static WML Sharpe 0.296, skewness -0.54; cvol 0.423; dyn 0.653, skewness -0.20 (Table 10).
- Bear-market beta drop -1.092 (t = -8.6), the largest of all classes (Table 9 A).
- Bear indicator lowers returns by 8.2% a year (t = -2.5): the only non-equity class where significant (Table 9 A, p. 34).
- Optionality "weakly" present: -0.405 (t = -1.4) (Table 9 B, p. 34).
- Panic-state coefficient -4.655 (t = -2.1), significant (Table 9 D).
- Alphas on WML: cvol 1.47 (t = 2.8), dyn 3.36 (t = 2.9); dyn on cvol 1.84 (t = 2.0) (Table 10 B).
- "Market" is the equal-weighted average of all currencies (p. 30); base currency not stated.

**Horizon and parameters**
- One lookback (12-2) and one holding period; no grid (p. 5).
- GJR leverage parameter γ negative in every class: WML losses lower its variance (Table 12, p. 46).

**Over time**
- Long drawdowns June 1932-Dec 1939 and March 2009-March 2013 (Fig. 1-2, p. 8).
- Ex-post hedge (future 42-day beta) avoids the 1932 crash; ex-ante hedge (past 42-day beta) does not, and underperforms unhedged 1927-1939 (Fig. 4, p. 19).

**Link to other strategies**
- HML-devil premium rises in panic states, opposite to WML; correlation about -0.50. A 50/50 WML/HML-d mix still loses in panic states (Table 11, p. 44).
- Dyn spans cvol (Barroso, Santa-Clara 2012) in every market; cvol does not span dyn (Table 10 B).

**Inconsistencies in the source**
- p. 7: WML Sharpe 0.71, alpha 22.3% (t = 8.5), market 7.6% and Sharpe 0.40; Table 1: 0.60, 22.2% (t = 7.3), 7.7%, 0.41.
- p. 16: bear up-market WML beta -1.796; Table 3 col. 3 gives -0.032 - 0.661 - 0.815 = -1.508 (computed), and p. 3 gives -1.51.
- p. 4: all-asset dynamic Sharpe 1.18; Table 10 gives 1.139 (GAll) and 1.223 (GAll*).
- Fig. 4 caption: full sample to 2013:03; chart title: 2013:01.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Buying variance swaps in bear markets does not restore momentum; only a regression control is shown, no hedged strategy | p. 3; Table 6 |
| Normalising by 1/v̄_B does not affect significance | p. 22 |
| Behavioural explanation could apply to all asset classes | p. 5, 40 |
| Earnings, time-series and cross-momentum might show the same features | fn 13 |
| 50/50 mix may be dominated by momentum because of dollar rather than risk weights | fn 17 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Cross-sectional momentum]], 12-2 ranking, skip one month | technique | signal | Convention; skip avoids 1-month reversal | p. 5-6 |
| 2 | [[Market state filter]]: bear market times market variance | technique | signal | Forecasts low momentum returns | p. 20-22; Table 5 |
| 3 | Dynamic weight proportional to forecast mean over forecast variance ([[Mean-variance weighting]]) | technique | sizing | Maximises unconditional Sharpe (App. C) | p. 24; App. C |
| 4 | Constant-volatility scaling (cvol), 126-day daily volatility ([[Volatility targeting]]) | technique | sizing | Barroso, Santa-Clara (2012) benchmark | p. 25; Table 10 |
| 5 | GJR-GARCH blended with 126-day realized volatility | technique | calibration | Both components forecast | App. D |
| 6 | Ex-ante vs ex-post [[Market beta hedge]] | technique | risk | Ex-post hedge is biased | p. 13, 19 |
| 7 | Bear-state up/down beta regression (Henriksson-Merton) ([[Downside beta regression]]) | technique | evaluation | Detects option-like payoff | Eq. 3, p. 15 |
| 8 | Regression on variance swap returns in panic states | technique | evaluation | Tests variance risk exposure | Table 6 |
| 9 | Spanning tests with conditional betas | technique | evaluation | Checks dyn is not spanned by cvol or factors | Tables 7, 10 |
| 10 | Rolling beta with 10 daily lags summed | technique | calibration | Lagged market information in losers | fn 2 |
| 11 | Ex-ante volatility-weighted combination of dynamic strategies (GAll*) | technique | sizing | Uses cross-sectional signal strength | p. 38 |

## 6. Regime observations

- Crashes: bear market (negative 2-year return), high volatility, then a sharp market rise (p. 8-10; Table 2).
- 2009: three of the ten worst months, market rising and volatility falling (p. 10).
- Extreme gains are smaller and less clustered than extreme losses (p. 10).

## 7. Acknowledged limits

- Crashes are rare; data-mining risk (p. 4).
- Source of the optionality not understood (p. 5, 40).
- Fixed income: no significant Sharpe even dynamic (p. 36).
- Maximum-Sharpe weights assume the conditional moments known (App. C, p. 44).
- No transaction costs, no margin calls within the month (p. 41).

## 8. Not addressed

- Costs, turnover, leverage range of the dynamic weights.
- True out-of-sample: the forecasting regression, GARCH and λ are estimated on each full sample; the other markets reuse the specification with refitted parameters (p. 24-25; App. D).
- Construction of non-equity momentum portfolios (tercile or decile, weighting) not restated (p. 30-34).
- Currency data details, base currency, forward or spot (deferred to Asness, Moskowitz, Pedersen 2013).
- Capacity, short-selling constraints in losers.
- Data after May 2013.
