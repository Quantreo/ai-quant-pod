---
type: reading-note
source: paper
title: The Term Structure of Currency Carry Trade Risk Premia
authors: Lustig, Stathopoulos, Verdelhan
affiliations: Lustig (Stanford Graduate School of Business, NBER), Stathopoulos (University of Washington), Verdelhan (MIT Sloan, NBER)
year: 2013
venue: NBER Working Paper 19623
doi: not printed in the PDF
pdf: "[[2013 - Lustig Stathopoulos Verdelhan - The Term Structure of Currency Carry Trade Risk Premia.pdf]]"
version: working paper, November 2013, revised November 2018, not peer-reviewed
tier: 1
read: full
tags: [carry, fx, monthly]
date: 2026-10-23
---

# The term structure of currency carry trade risk premia (Lustig, Stathopoulos, Verdelhan 2013)

## Summary

- **Finding**: G10 vs USD, 1975-2015, gross: the rate-sorted carry trade earns 2.66% a year with bills (Sharpe 0.36) but -1.12%, not significant, with 10-year bonds.
- **Mechanism (authors)**: local bond term premia offset currency premia. In theory, dollar long-bond premia differ across countries only through the volatility of the permanent component of their pricing kernels.
- **Where it works best**: the currency leg of the slope sort, long flat-curve, short steep-curve currencies: 3.65% a year, Sharpe 0.49. No bond-based version is significant.
- **Weak spots**: dollar return falls with maturity, 2.67% at the short end to -2.18% at 15 years. Even the short-end slope carry has a standard error of 1.50%.
- **Main caveats**: no transaction costs; whole-sample, in-sample, nine countries, log returns. Most robustness checks sit in an Online Appendix not in the PDF. The model failure is shown by simulation only.

Page numbers follow the printed working-paper pagination (page 1 is PDF page 3; title and abstract pages unnumbered). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Currency risk premia and local term premia cancel out for a US investor holding foreign long bonds | High rate differentials predict high currency returns and low local bond returns; steep slopes predict low currency returns and high local bond returns | Table 1; p. 7-8 |
| 2 | Long-term bond rates hedge the transitory part of currency risk: a temporary adverse shock to the foreign pricing kernel appreciates the currency but raises foreign rates, so the bond loses | Derivation, two polar cases | p. 24 |
| 3 | Dollar term premium of an infinite-maturity foreign bond = domestic term premium + difference in entropy of the permanent pricing kernel components (Proposition 1) | Proof built on Backus, Foresi, Telmer (2001) and Alvarez, Jermann (2005) | p. 23; App. B, p. 42-43 |
| 4 | Zero long-bond carry premia require equal entropy of permanent components across countries (Condition 1); stationary exchange rates are sufficient, not necessary | Two worked examples (Alvarez-Jermann, two-country CIR) | p. 26-29 |
| 5 | Leading no-arbitrage models fail to produce the downward term structure in standard calibrations | Lustig, Roussanov, Verdelhan (2014) model gives a flat term structure (Fig. 3, simulation); scorecard of habit, long-run risk and disaster models | p. 21-22, 30; Table 4 |

The authors "pursue a simple interest rate risk interpretation" (p. 18).

**Caveats raised by the authors**
- Results assume complete markets; models with market segmentation are not covered and left open (p. 3).
- Infinite-maturity returns are approximated by 10- and 15-year bonds (Assumption 1, p. 25).
- Level and slope are assumed to hold all relevant forecasting information; other predictors cannot be ruled out (Assumption 2, p. 25).
- Small amounts of dollar-return predictability in models may fall within the confidence intervals (p. 25).
- Long-run UIP tests lack power: few non-overlapping 10-year windows (p. 2).

**Ruled out**
- Inflation risk: high-rate portfolios have higher and more volatile inflation; term premia are higher in low-inflation countries, also 1951-2015 (p. 12, 18; Table 3A).
- Sovereign default risk: countries in the high term premium portfolios have similar or slightly better ratings (p. 12, 18; Table 3A).
- Measurement error in coupon indexes: the zero-coupon results agree (p. 16).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Australia, Canada, Germany, Japan, New Zealand, Norway, Sweden, Switzerland, UK; home country US. "Developed countries with liquid bond markets" | p. 4 |
| Period | Data 1/1951-12/2015; benchmark 1/1975-12/2015 (492 months); zero-coupon 4/1985-12/2015 | p. 4, 6, 15; Table 1 |
| Signal 1 | Short rate minus its own past 10-year rolling mean (conditional carry) | p. 10 |
| Signal 2 | Yield curve slope: 10-year yield minus one-month rate (Tables 2-3) or three-month rate (Fig. 1-2) | Tables 2-3; Fig. 1-2 |
| Portfolio | Three portfolios each month; portfolio return = average of country log excess returns. Long high-rate (flat-slope), short low-rate (steep-slope) | p. 10 |
| Per-country rule | Long foreign bond, short US bond when the foreign rate is higher (or the foreign slope lower); reverse otherwise; equal-weighted across nine countries | p. 8; Table 2 |
| Instruments | Treasury bill and 10-year government bond total return indexes, in USD and local currency; zero-coupon bonds 3 months to 15 years | p. 4; App. A |
| Horizon | Hold one month (indexes); one quarter (zero-coupon) | p. 10, 15 |
| Rebalancing | Monthly, using only information at t | p. 10 |
| Sizing | Equal weights within a portfolio | p. 10 |
| Costs | Not mentioned. Results are gross | whole paper |

Countries per portfolio and the handling of ties are not stated. Whether the slope sort in Table 3 uses levels or deviations is not stated.

**Rule** (Eq. 3, p. 5), dollar excess return of a foreign bond:

$$rx^{(k),\$}_{t+1} = rx^{(k),*}_{t+1} + rx^{FX}_{t+1}, \quad rx^{FX}_{t+1} = r^{f,*}_t - r^f_t - \Delta s_{t+1}$$

The carry trade is long the top portfolio and short the bottom one, on each leg.

**Data provenance** (p. 4; App. A, p. 42)

| Series | Source | Notes |
| --- | --- | --- |
| 10-year bond and T-bill total return indexes | Global Financial Data, monthly, 1/1951-12/2015 | Coupon bonds, 10-year maturity only |
| Zero-coupon curves | Wright (2011) dataset plus Bloomberg sovereign curves estimated from notes, bonds and swaps | Unbalanced. Start: Germany 1/1973, UK 1/1979, Japan 1/1985, Canada 1/1986, Australia 2/1987, Switzerland 1/1988, New Zealand 1/1990 (above 10 years from 12/1994), Sweden 12/1992, Norway 1/1998, US 12/1971 |
| Inflation | GFD CPI | n/a |
| Credit ratings | S&P, 7/1989-12/2015, mapped to numbers (AAA = 1), outlook adjustments | Backfilled before 7/1989 with the first available rating |

## 3. Results

All real data, in-sample, gross, log returns annualised, standard errors bootstrapped (10,000 non-overlapping samples) unless stated. Figure 3 is a simulation.

**Time-series predictability** (Table 1, 1975-2015)
- On rate differentials, the 10-year dollar return differential is predictable only in Japan (beta 2.37, s.e. 0.84) (p. 6).
- Panel: currency leg 1.98 (s.e. 0.44), local bond leg -1.34 (0.30), dollar 0.65 (0.49), adjusted R² -0.05% (p. 7; Table 1A).
- On slope differentials, panel: currency -2.02 (0.73), local 3.96 (0.50), dollar 1.94 (0.84), significant, with the "surprising" sign (p. 7-8; Table 1B).
- Australia, Canada, Sweden: slope predicts dollar long-bond returns with the "wrong" sign (fn. 6, p. 26).

**Per-country dynamic strategies** (Table 2)
- Rate rule, equal-weighted: dollar 0.70% a year (s.e. 1.00), Sharpe 0.11; currency leg 2.59%, Sharpe 0.47; local leg -1.89%, Sharpe -0.51 (Table 2A).
- Slope rule, equal-weighted: dollar -1.03% (1.24), Sharpe -0.13; currency 3.16%, Sharpe 0.47; local -4.19%, Sharpe -0.83 (Table 2B).
- Country dollar returns range from -0.46% (Canada) to 2.19% (Germany) on rates, -3.62% (Sweden) to 1.98% (Germany) on slope; none significant except Sweden on slope (p. 8; Table 2).

**Three-portfolio sorts** (Table 3)

| Sort | Currency leg | Local bond leg | Dollar 10-year bond |
| --- | --- | --- | --- |
| Rate deviation, high minus low | 2.66% (s.e. 1.14), Sharpe 0.36 | -3.78% (0.77), Sharpe -0.77 | -1.12% (1.33), Sharpe -0.13 |
| Slope, flat minus steep | 3.65% (1.18), Sharpe 0.49 | -5.61% (0.74), Sharpe -1.18 | -1.96% (1.38), Sharpe -0.22 |

- High-rate portfolio: currencies depreciate 0.60% a year against a 2.65% rate gap (p. 12).
- Local term premia fall from 3.53% (low-rate) to -0.25% (high-rate); from 4.61% (steep) to -1.01% (flat) (Table 3C).
- The slope spread (-2.76) is about half the local return spread, so the result is "not mechanical" (p. 14).
- Currency carry Sharpe above the S&P 500 over the same period; no figure (p. 12).

**Across maturities** (zero-coupon, slope sort in levels, quarterly hold, 1985-2015; Fig. 2)
- Dollar return 2.67% (s.e. 1.50%) at the short end, falling monotonically to -2.18% (2.28%) at 15 years (p. 15-16).
- Short minus long gap, the local term premium: -4.85% (s.e. 1.82%), significant (p. 16).
- Crosses zero near ≈30 quarters; the 95% band includes zero at every maturity (≈ Fig. 2).
- Rate sort instead: flat, carry 3.71% (1.80%), local -0.21% (1.76%), dollar at 15 years 3.50% (2.32%) (fn. 3, p. 17).

**Over time** (Fig. 1, cumulative log returns, 1975-2015)
- Rate sorts: the offset from local bond premia weakens from the mid-1980s (levels) or 1990s (deviations), as G10 rates converge (p. 15).
- Slope sorts: the offset is larger and does not weaken (p. 15).
- End points: FX ≈1.4 vs bond ≈-1.0 (rate levels); ≈1.1 vs ≈-1.6 (rate deviations); ≈1.5 vs ≈-2.3 (slope levels); ≈1.05 vs ≈-2.4 (slope deviations) (≈ Fig. 1).

**Simulation** (inside a model): the Lustig, Roussanov, Verdelhan (2014) model gives a flat term structure, ≈7% at all maturities to 90 quarters (≈ Fig. 3, p. 22).

**Link to other strategies**
- Level sorts capture conditional and unconditional carry; de-meaned sorts only the conditional part; currency returns are larger with level sorts (p. 14-15).
- Slope predicts currency returns at the short end, confirming Ang and Chen (2010) (p. 14).

**Inconsistencies in the source**
- Fig. 1 caption: full line = currency, dashed = local bond. Text (p. 14) and the chart legend: full = local bond, dashed = FX premium.
- Slope definition: 10-year minus one-month rate (Tables 2-3 notes) vs minus three-month rate (Fig. 1-3 captions), on the same 10-year sample for Table 3 and Fig. 1.
- p. 14: the slope strategy is said to be long bonds of countries with lower inflation and better ratings. Table 3A shows the long leg (portfolio 1, flat) with higher inflation (4.89 vs 2.87) and a worse rating (1.54 vs 1.28, lower is better per App. A). The text fits portfolio 3, the high term premium side.
- p. 10 gives a Sharpe of 0.51 for local bond returns of the rate strategy; Table 2A prints -0.51.
- fn. 3 (p. 17) calls -0.21% the "local 10-year bond premium" in a paragraph on the zero-coupon 15-year maturity.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Time-series results robust to inflation and credit controls, another decomposition, GBP as base currency, windows 10/1983-12/2007, 1/1975-12/2007, 10/1983-12/2015, three-month horizon (Online Appendix A, not in PDF) | p. 18 |
| Portfolio results robust to 3- and 12-month holds, windows, larger country sets, non-demeaned sorts (Online Appendix B) | p. 18 |
| Regressing local log returns (not excess) on rate differentials shows no predictability (Online Appendix) | fn. 1, p. 7 |
| 10- and 15-year bonds approximate infinite maturity, supported by a Joslin, Singleton, Zhu (2011) simulation (Online Appendix H) | p. 25 |
| Term structure model restrictions summarised in Table A18, not in PDF | p. 30 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Carry signal]]: short rate minus its past 10-year rolling mean, three-portfolio sort | technique | signal | Isolates the conditional carry trade | p. 10, 14-15 |
| 2 | [[Carry signal]]: yield curve slope as a currency signal, long flat, short steep | technique | signal | Strongest predictor of currency and term premia, 1985-2015 | p. 14-15 |
| 3 | [[Long-short portfolio weighting]]: three equal-weighted portfolios, long top, short bottom; per-country sign vs US | technique | sizing | Not argued; follows Lustig and Verdelhan (2007) | p. 8, 10 |
| 4 | [[Currency and local return decomposition]]: home-currency return = local excess return + currency excess return, per leg and per maturity | technique | evaluation | Shows why dollar returns are not predictable | p. 5-7, 15 |
| 5 | [[Static and dynamic return decomposition]]: compare level and de-meaned sorts | technique | evaluation | Separates conditional from unconditional carry | p. 14-15 |
| 6 | [[Currency exclusion filter]]: G10 panel with liquid bond markets | principle | universe | Homogeneous, liquid; more countries add illiquid, default-prone markets | p. 4, 18 |
| 7 | Per-country predictability regressions, Newey-West 6 lags; panel with Driscoll-Kraay errors | technique | evaluation | Not argued | p. 6 |
| 8 | Bootstrapped standard errors, 10,000 non-overlapping samples | technique | evaluation | Not argued | Table 2-3 notes |
| 9 | Profile sorted portfolios on inflation and credit ratings | technique | evaluation | Rule out inflation and default risk | p. 12, 14; Table 3A |
| 10 | Numeric rating scale with outlook adjustment | technique | evaluation | Average ratings across countries | App. A, p. 42 |
| 11 | R² to unconditional Sharpe mapping | principle | evaluation | Cochrane (1999) | p. 8 |
| 12 | Condition 1 as a test of asset pricing models | principle | economic intuition | Diagnostic tool for richer models | p. 26, 30 |

## 6. Regime observations

- When G10 rates are similar and low, rates do not predict large term premium differences across countries (p. 15).
- Rate convergence in the second half of the sample weakens the offset in rate sorts, not in slope sorts (p. 15).

## 7. Acknowledged limits

- 10-year data are coupon bonds, while theory concerns zero-coupon bonds; GFD offers no full term structure (p. 4).
- Zero-coupon panel is unbalanced and allows only three-month holds, which "mitigates predictability"; larger standard errors (p. 15).
- Zero-coupon sort uses slope levels only, because of the shorter sample (p. 15).
- Local excess return differential contains the rate differential with a negative sign, so part of its predictability is mechanical; short-rate measurement error could also produce it (fn. 1, p. 7).
- Ratings before 7/1989 are backfilled (App. A, p. 42).

## 8. Not addressed

- Transaction costs, bid-ask spreads, financing of the bond positions, slippage.
- Drawdowns, skewness, worst months.
- Capacity.
- Out-of-sample or ex-ante test; the 10-year rolling window and the three-portfolio split are not argued.
- Emerging or non-G10 currencies in the PDF.
