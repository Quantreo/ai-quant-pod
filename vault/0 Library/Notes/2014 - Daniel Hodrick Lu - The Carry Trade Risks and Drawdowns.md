---
type: reading-note
source: paper
title: "The Carry Trade: Risks and Drawdowns"
authors: Daniel, Hodrick, Lu
affiliations: Daniel and Hodrick (Columbia Business School, NBER), Lu (Terry College of Business, University of Georgia)
year: 2014
venue: NBER Working Paper 20433
doi: 10.3386/w20433
pdf: "[[2014 - Daniel Hodrick Lu - The Carry Trade Risks and Drawdowns.pdf]]"
version: working paper, August 2014, not peer-reviewed
tier: 1
read: full
tags: [carry, fx, monthly]
date: 2026-10-22
---

# The carry trade: risks and drawdowns (Daniel, Hodrick, Lu 2014)

## Summary

- **Finding**: G10 dollar-based carry trades, 1976-2013, earn 2.10% to 6.60% a year with Sharpe 0.78 to 1.02, gross. Equity, bond, FX and volatility factors leave significant alphas.
- **Mechanism**: the time-varying dollar exposure drives the "puzzle". The dollar-neutral leg is explained by Fama-French factors; the pure dollar leg (EQ-USD) is explained by nothing tested.
- **Where it works best**: spread-weighted and risk-rebalanced versions (SPD-RR Sharpe 1.02). USD as base currency (Sharpe 0.78 vs 0.36 to 0.71 for other bases).
- **Weak spots**: dollar-neutral EQ0 alpha insignificant; EQ alpha only t = 1.73 after LRV FX factors; 2000-2013 EQ mean insignificant (p = .12); option hedging leaves EQ insignificant.
- **Main caveats**: no transaction costs; drawdowns are slow (94 to 163 days) and occur more often than i.i.d. models imply; option hedge sample only 2000-2013, USD options only.

Page numbers follow those printed on the PDF (PDF page minus one). The paper has no charts; all values come from tables or text.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | The conditional dollar exposure, not the non-dollar "carry", is at the core of the carry puzzle | EQ0 (dollar-neutral) alpha 1.03% [1.54] on FF3, -0.03% [-0.06] on LRV FX factors; EQ-minus and EQ-USD keep significant alphas | p. 16-19, 33; Tables 9-11 |
| 2 | EQ-USD earns a premium no tested risk factor explains, with insignificant skewness, so crash risk cannot explain it | Alpha 4.52% [2.79] with all factors at once; skewness -0.11 (0.17) | p. 18-19, 33; Tables 8, 12 |
| 3 | Downside equity risk (Lettau, Maggiori, Weber; Dobrynskaya) does not explain these carry trades | Downside beta differentials insignificant (largest t 1.43) and not monotonic across interest-rate portfolios | p. 21-23; Tables 13-15 |
| 4 | Monthly negative skewness comes mostly from persistent runs of daily losses (time-varying autocorrelation), not sudden crashes | Worst drawdown of each strategy takes 69 to 353 days; drawdowns and pure drawdowns more frequent than i.i.d. bootstrap allows | p. 27-34; Tables 22-24 |

The authors keep the four classic readings open: falling profitability suggests possible early inefficiency; risk exposures suggest risk aversion; changing risks leave room for learning; a single unrealised peso state is "probably not" the explanation (p. 34).

**Caveats raised by the authors**
- EQ-USD is "not strictly a carry trade"; its down-market return may come from currencies far from the median (p. 21, fn. 15).
- EQ-minus is under-diversified, which could explain its large kurtosis (p. 18).
- Failure to reject a zero beta differential is not enough to reject the downside theory; point estimates are also checked (p. 22).
- USD-only options overstate hedging cost versus a full set of 45 bilateral options (p. 25).
- Normal and i.i.d. bootstrap are simple benchmarks; jump-diffusion and block bootstrap not tried (p. 29, fn. 19, 21).

**Ruled out**
- Fama-French 3 factors, LRV FX factors, US bond level and slope, variance swap as explanations of the dollar-based carry alphas (p. 13-15).
- Downside market beta (LMW) for all six strategies (p. 21-23).
- Jurek DRI for EQ-USD; DRI also loses significance once FF3 are added (p. 24-25; Table 16).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | G10: AUD, GBP, CAD, EUR (spliced with DEM), JPY, NZD, NOK, SEK, CHF, USD. Pre-euro European currencies excluded (convergence trade, peso problem); emerging markets excluded (sovereign risk). | p. 8-9 |
| Period | 1976:02-2013:08, 451 months; AUD, NZD from Oct 1986. Options 2000:09/10-2013:08. | p. 9; Table 1, 17 |
| Signal | Sign (EQ) or size (SPD) of the one-month interest differential vs the base currency | p. 10 |
| Entry / exit | Forward position taken at month start, held one month, rebalanced at month end | p. 5-6, 28 |
| Horizon | One month | p. 28 |
| Sizing | EQ: sign/N each. SPD: differential over sum of absolute differentials. RR: scale EQ or SPD to 5% annual vol from IGARCH covariance. OPT: H^-1 mu scaled to 5% vol | p. 10-11 |
| Portfolio variants | EQ0: dollar-neutral, long (short) the four currencies above (below) the non-USD median. EQ-minus = EQ minus EQ0. EQ-USD: long (short) USD vs all nine when USD rate above (below) the median | p. 15-18 |
| Hedge | Buy 10-delta or 25-delta OTM USD options (equivalent to ITM calls or puts); SEK excluded | p. 7-8, 25 |
| Rebalancing | Monthly | p. 28, fn. 18 |
| Costs | None. Payoffs written "without transaction costs". Results are gross. | p. 4 |

**Rule** (p. 10-11, Eq. 9-10)

$$w^{EQ}_{j,t}=\frac{\text{sign}(i^j_t-i^\$_t)}{N_t},\qquad w^{SPD}_{j,t}=\frac{i^j_t-i^\$_t}{\sum_j|i^j_t-i^\$_t|}$$

$$w^{OPT}_t=\frac{0.05/\sqrt{12}}{(\mu_t'H_t^{-1}\mu_t)^{0.5}}H_t^{-1}\mu_t,\ \mu_t=\text{interest differentials}$$

**Data provenance**
- Spot and forward rates: Datastream and IHS Global Insight. Interest rates: eurocurrency, Datastream; daily analysis infers foreign rates from the USD rate and covered parity (p. 8-9, 28).
- FX options: JP Morgan, 2000:09-2013:08, eight currencies vs USD (p. 9).
- Factors: French's site (FF3), CRSP (bonds), Verdelhan's site (RX, HML-FX, 1983:11-2013:08), S&P 500 and CBOE VIX (variance swap, from 1990), Jurek data to 2012:06 then OptionMetrics (DRI) (p. 13-15, 24; Table 16).

## 3. Results

All results are real data, in-sample, gross. The drawdown p-values come from simulations (normal and i.i.d. bootstrap, 10,000 trials) used as benchmarks for the real series (p. 29).

**Aggregate** (Table 1, p. 38)
- Mean return: OPT 2.10% (0.47) to SPD 6.60% (1.31). Sharpe: EQ 0.78 to SPD-RR 1.02 (p. 11).
- All negatively skewed: OPT worst at -0.89 (0.34); excess kurtosis 0.40 to 3.91 (p. 12).
- Worst month: OPT -4.01% to SPD -7.26%. Positive months: 288 (EQ) to 303 (OPT) of 451 (p. 12).

**Risk-adjusted alphas, full sample**
- FF3: alpha 1.83% [3.72] (OPT) to 5.55% [4.84] (SPD-RR); R2 at most .05 (p. 13; Table 3).
- LRV FX factors: alpha 1.29% (OPT) to 3.60% (SPD-RR); HML-FX t 6.22 to 8.85; R2 .13 to .34 (p. 14; Table 4). EQ alpha 1.47 [1.73].
- Bond factors: alpha 2.15% to 6.71%; 10y beta negative, 10y-2y beta positive, both significant (p. 14; Table 5).
- Variance swap (1990-2013): betas negative, largest |t| 1.76; alphas stay significant (p. 15; Tables 6-7).

**By sub-group**
- Base currency (EQ): mean 2.33% (SEK) to 3.96% (USD); Sharpe 0.36 (JPY) to 0.78 (USD). Worst month beyond -10% for JPY, SEK, NZD, AUD; SEK skewness -3.77, kurtosis 30.24 (p. 12; Table 2).
- Decomposition (Table 8, p. 45): EQ0 1.61%, Sharpe 0.49; EQ-minus 2.35%, Sharpe 0.61; EQ-USD 5.54%, Sharpe 0.68, skewness -0.11.
- EQ0 loads on market (t 5.29) and HML (t 2.83); the market explains about 30% and HML another 15% of its mean, per the authors (p. 16).
- Downside beta test: carry beta differentials 0.00 to 0.10; implied downside premium explains 0% to 5% of EQ, EQ-RR alpha and 20% to 40% of SPD, SPD-RR alpha; EQ-USD -2.12% or -3.28% (p. 21-22; Table 13).
- LRV six portfolios: P6-P1 alpha 6.46% [3.67], beta 0.18; downside explains about a quarter (p. 22; Table 14). LMW five portfolios: P5-P1 alpha 4.52%, downside explains 57% (p. 23; Table 15).
- DRI alone: alphas 1.26% [2.17] (OPT) to 5.37% [2.83] (EQ-USD); EQ0 0.10% [0.13]. With FF3, no DRI beta significant (p. 24-25; Table 16).

**Hedged trades, 2000:10-2013:08** (Table 17, p. 53)
- Unhedged in this sample: EQ 2.22% (p = .12), SPD 5.55%, EQ-USD 4.58% (p. 25-26).
- Cost of hedging: 10-delta cuts 34 to 61 bp, 25-delta 87 to 145 bp (p. 25-26).
- Hedged EQ insignificant (p .132, .198); hedged SPD significant (p .017, .022); EQ-USD p .055, .083 (p. 26).
- Hedging barely cuts EQ and SPD worst months (SPD -7.44% unhedged, -6.30% 10-delta) (p. 26).
- With bond factors, no hedged alpha has t above 1.57 (p. 27; Table 19). DRI alone explains EQ and SPD in this sample, not EQ-USD (p. 27; Table 20).

**Daily distribution and drawdowns** (Tables 21-24, p. 57-60)
- Daily skewness EQ-RR -1.01, SPD-RR -1.62; the worst daily and worst monthly losses fall in different months (p. 29).
- Monthly vs daily skewness ratio, normalised to i.i.d.: EQ 7.1, SPD 2.4, EQ-RR 1.7, SPD-RR 1.3 (p. 29).
- Worst drawdown: EQ 12.0% over 94 days (p-b .13); SPD 21.5% over 163 days (p-b .023). Second EQ drawdown 10.8% (p-b .018) (p. 30).
- Risk rebalancing halves the SPD worst drawdown (10.2%) but EQ-RR worst is 14.1% over 353 days (Table 22).
- Max loss over a horizon: EQ beyond 3 days and SPD beyond 40 days exceed the bootstrap 5% bound; EQ-RR and SPD-RR mostly within (p. 31; Table 23).
- Pure drawdowns (consecutive down days): EQ worst 5.2% over 7 days (p-b .014); runs of 3 to 12 days (p. 31-32; Table 24).

**Over time**
- 1990-2013: EQ 3.83%, Sharpe 0.70; EQ-USD 5.21% (Table 8B). 2000-2013: EQ 2.22%, Sharpe 0.47 (Table 17). Authors state basic carry profitability has decreased (p. 34).
- 2000-2013 FF3: EQ alpha 1.80 [1.55], market beta 0.13 [5.26], R2 .20 (p. 26; Table 18).

**Link to other strategies**
- EQ-USD loads only on the LRV RX factor (0.52, t 4.31) (p. 19; Table 11).

**Inconsistencies in the source**
- Table 17 Sharpe of unhedged EQ-USD is 0.20; text says 0.53 (p. 25). 4.58/8.59 = 0.53 (computed). Hedged USD-25 delta Sharpe 0.93 vs 3.13/7.07 = 0.44 (computed).
- Table 17 EQ-USD max/min printed as 0.09 / -0.07 (and -0.05, -0.04 hedged); text gives losses of 7.15%, 5.30%, 3.68% (p. 26). Units differ between columns.
- Text says minimum daily returns are of similar size to minimum monthly returns "for all four strategies" (p. 29); EQ daily -2.78% vs monthly -6.01% (Table 21).
- Text says the 10 worst SPD drawdowns each took more than 50 days (p. 30); Table 22 rank 7 lasts 38 days.
- Text says LRV FX alphas "remain highly significant" (p. 14); EQ alpha t is 1.73 (Table 4).
- USD-based EQ mean standard error 0.91 in Table 1, 0.88 in Table 2.
- DRI sample: text says to August 2013 (p. 24, fn. 17), Table 16 says 1990:01-2013:07. Table 21 caption says five strategies, shows four.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Alternative downside definitions give similar results "available in an internet appendix" (Table A.2 is in the paper and shows EQ-USD beta differential significantly negative, t -3.56) | p. 20, fn. 13; p. 63 |
| Durations of pure drawdowns within the simulation bounds, "online appendix" | p. 32 |
| Max losses decrease beyond 180 days (table stops at 180) | p. 31 |
| FX traders can adjust daily "with minimal transaction costs" | p. 28, fn. 18 |
| Maximum drawdowns happen "often in highly volatile environments" and could be avoided by daily rebalancing traders | p. 32 |
| Basic carry profitability "has decreased over time" (no formal sub-period test) | p. 34 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Long-short portfolio weighting]]: Spread weighting of carry positions | technique | sizing | Invests more where differentials are larger | p. 10 |
| 2 | [[Volatility targeting]]: IGARCH (RiskMetrics, alpha 0.06) covariance, scale to 5% annual vol | technique | sizing | Mimics trader VaR limits; EQ/SPD take more risk when vol is high | p. 10-11 |
| 3 | [[Mean-variance weighting]]: Mean-variance carry with interest differential as expected return | technique | sizing | Currency moves essentially unforecastable (Meese-Rogoff) | p. 11 |
| 4 | [[Dollar-neutral and dollar leg split]]: Split carry into dollar-neutral and dollar legs | technique | evaluation | Isolate the source of abnormal returns | p. 15-18 |
| 5 | [[Protective option hedge]]: Hedge carry with 10-delta or 25-delta OTM options | technique | risk | Floor on losses from crashes | p. 7-8 |
| 6 | [[Downside beta regression]]: Downside beta test with dummy plus downside market regressor | technique | evaluation | Test beta differential directly | p. 20-21 |
| 7 | [[Drawdown test against i.i.d. bootstrap]]: Drawdown, pure drawdown and max-loss distributions vs normal and i.i.d. bootstrap | technique | evaluation | Separate crashes from persistent losses | p. 29 |
| 8 | [[Currency exclusion filter]]: Exclude currencies carrying sovereign or convergence risk | principle | universe | Carry should bear pure FX risk | p. 9 |

## 6. Regime observations

- Carry trades do worse when equity volatility rises, but the exposure is insignificant and does not explain profits (p. 15).
- 2000-2013: EQ market beta rises to 0.13 and alpha loses significance (Table 18). Bond betas flip sign for SPD versus full sample (p. 27).

## 7. Acknowledged limits

- Hedge sample short and USD options only, overstating hedge cost (p. 25).
- Simulation benchmarks ignore volatility clustering; block bootstrap and jump models left aside (p. 29, 31).
- Daily analysis keeps monthly rebalancing; no forward quotes for arbitrary maturities (p. 28, fn. 18).
- Downside betas small and imprecisely estimated (p. 23).

## 8. Not addressed

- Transaction costs, bid-ask spreads, slippage, capacity.
- Emerging-market and non-G10 currencies.
- Out-of-sample test. Calendar dates of the worst drawdowns.
- Any trading rule using drawdown detection (suggested, not tested, p. 28, 32).
