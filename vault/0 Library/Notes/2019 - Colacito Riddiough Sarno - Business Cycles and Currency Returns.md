---
type: reading-note
source: paper
title: Business Cycles and Currency Returns
authors: Riccardo Colacito, Steven J. Riddiough, Lucio Sarno
affiliations: University of North Carolina at Chapel Hill (Kenan-Flagler) and NBER; University of Melbourne; Cass Business School
year: 2019
venue: NBER Working Paper 26299
doi: not stated in the PDF
pdf: "[[2019 - Colacito Riddiough Sarno - Business Cycles and Currency Returns.pdf]]"
version: September 2019
tier: 1
read: full
tags: [value, fx, monthly]
date: 2026-10-25
---

# Business cycles and currency returns (Colacito 2019)

## Summary

- **Finding**: Buying currencies of countries with a high output gap versus the US and selling low ones earned a real-time Sharpe of 0.72 gross, 0.50 net (1999-2016, cross-section).
- **Mechanism**: Compensation for business cycle risk in a long-run risk model; the authors call it one possible framework, not tested against rivals.
- **Where it works best**: Spot return carries about 86% of the cross-sectional return (computed, Table 4). Correlation with carry is 0.06. Adding it lifts carry Sharpe from 0.58 to 0.85.
- **Weak spots**: The cross-section is flat after about 2010 (≈ Fig. 2). Time-series version loses 3.99% in US recessions and is insignificant for a Swiss investor.
- **Main caveats**: Real-time sample is 17 years, on a changing number of currencies. Costs use 50% of quoted spreads. The priced GAP factor is built from the portfolios it prices.

Page numbers follow the working paper pagination (main text; "IA" is the Internet Appendix, own numbering). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Currencies of strong economies earn higher excess returns than those of weak economies. | Quintile sorts, all four gap measures, spread 4.56% to 6.66% a year, 1% significance. | p. 12, Table 1 |
| 2 | The return comes from spot changes, not interest differentials. | fx 5.06 vs ir 1.60 in the HP cross-section. Carry has negative fx. | p. 12, Tables 1, A2 |
| 3 | The return is compensation for risk, a "GAP premium". | Standard factors (DOL, HMLFX, VOL, IMB) do not price the sorted portfolios; the GAP factor does. | p. 19-24, Tables 7-9 |
| 4 | Model: investors of the base country dislike low output-gap shocks. A country whose output gap correlates less with the base country's is a worse hedge, so its currency is riskier. | Proposition 1, with an assumed correlation falling in the country's gap (Eq. 16). | p. 27-30 |
| 5 | Output-gap sorting differs from interest-rate sorting because output gap and volatility shocks are imperfectly correlated. | IA regression: coefficient 0.25, rejected equal to 1. | p. 27, IA p. 15 |

**Caveats raised by the authors**
- The model leaves out trade in goods; a full general equilibrium analysis is left to future work (p. 5, 27).
- The model is "only one of potentially several frameworks" (p. 31).
- Quoted spreads overstate effective spreads (p. 17).
- Post-crisis covered interest parity deviations mean the forward discount holds more than rates (p. 8).

**Ruled out**
- Carry: correlation with HMLFX 0.06 (Table 5).
- Taylor-rule sorting: all its predictability is in the forward premium (p. 14).
- Conventional risk factors (p. 22).
- Trend in the dollar (cross-section only): dollar neutral by construction (p. 11).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 27 countries, USD base, euro replaces DEM from Jan 1999, euro members drop out, Turkey hyperinflation removed. | p. 7-8, Table A1 |
| Period | Full: Oct 1983 to Jan 2016. Real time: Dec 1999 to Jan 2016. | p. 7, 10 |
| Signal | Output gap of country minus US output gap. | p. 10 |
| Entry | Long top quintile (P5), short bottom (P1). | p. 10 |
| Exit | Replaced at the next monthly sort. | p. 10-11 |
| Horizon | One month. | p. 10 |
| Sizing | P5 and P1 equal weight (at most 5 currencies, weights ±20%); variants linear and rank weights, one dollar long and short. | p. 10-11, fn. 9 |
| Portfolio | GAPCS (cross-section), GAPTS (time series), 50-50 combinations COM. | p. 11-12, Table 4 |
| Rebalancing | Month end. | p. 11 |
| Costs | Bid-ask at 50% of quoted spread, spot and forward. | p. 16-17 |
| Data | Spot and 1M forward bid, mid, ask; OECD industrial production vintages. | p. 7, 9 |

**Rule**
- RX(t+1) = (Spot(t+1) − Fwd(t)) / Spot(t) (Eq. 1, p. 8).
- Output gap: log industrial production minus its trend (p. 9). Real time: regress y(t) on 12 lags starting 24 months earlier; gap = residual (Eq. 3, p. 10).
- GAPCS: long P5, short P1, equal weights inside quintiles (p. 10).
- Linear: w = c(x_j − mean x), c scales absolute weights to 1 (Eq. 4, p. 11). Rank: same with ranks (Eq. 5).
- GAPTS: 1/N, long if country gap is above the US gap, short if below. Not dollar neutral (p. 11-12).
- In-sample gap filters: HP (λ = 14400 monthly), Baxter-King (K = 36, 8 to 96 months), quadratic trend (IA p. 1-2).

**Data provenance**
- FX: Barclays and Reuters via Datastream, end of month; start dates differ by currency (Table A1).
- Industrial production: OECD Original Release Data and Revisions Database. Full sample uses the April 2016 vintage (p. 9).
- Real-time vintages from Dec 1999. The Dec 1999 vintage shows US data to Oct 1999 (p. 10).
- Quarterly industrial production uses four lags from eight quarters earlier (p. 10).

## 3. Results

**Aggregate**
- Real data, in-sample, full sample, gross, 1983-2016: cross-section spread 4.56% to 6.66%, Sharpe 0.60 to 0.82; time series mean 2.14% to 3.83%, Sharpe 0.41 to 0.74 (Table 1).
- Real data, real time, gross, 1999-2016: GAPCS 4.92%, Sharpe 0.72; linear 0.74; rank 0.72; GAPTS 0.65; combinations 0.82 (Table 4A).
- Net of 50% quoted spread: GAPCS 3.46%, Sharpe 0.50; GAPTS 0.50; combinations 0.57 to 0.60 (Table 4B).
- Turnover (Table 1) has no stated unit.

**By sub-group**
- Gap measure: P5 − P1 and Sharpe similar across HP, BK, linear projection, quadratic trend. Portfolio means rise from P1 to P5 (Table 1).
- Return split: fx is 4.21 of 4.92 for GAPCS; ir 0.71 (Table 4A). Carry: fx −4.63, ir 12.43 (Table A2).
- Home investor, GAPCS Sharpe: German 0.79, Japanese 0.66, British 0.72, Swiss 0.91 (Table A8). GAPTS: 0.50, 0.61, 0.40, 0.14.
- Taylor-rule sort: cross-section Sharpe 0.90, correlation with HMLFX 0.84, with GAP 0.25 (Table 3).

**Horizon and parameters**
- One monthly horizon only; no other holding period or quantile count is shown.
- Gap correlation across the four measures 0.41 to 0.65; first principal component 86% (p. 13, Table A3).

**Over time**
- Fig. 2, GAPCS out of sample (normalised to 6% volatility): rises to ≈0.8 around 2010, ≈0.7 at the end, flat in between.
- GAPTS drops during the 2008 crisis and takes years to recover (p. 15-16, Fig. 2).
- US booms vs recessions, mean: GAPCS 4.75% vs 5.94%; GAPTS 3.90% vs −3.99%; GAPTS dollar exposure 0.26 vs −0.27 (Table A6).
- Max drawdown, full sample, cross-section: 9.0% (HP) to 35.3% (linear projection) (Table 1). Real time: 6.88% (Table 4A).

**Link to other strategies**
- GAPCS correlation: HMLFX 0.06, dollar 0.24, value 0.15, momentum 0.07, US equity 0.00; with GAPTS 0.36 (Table 5).
- Carry Sharpe 0.58, with GAPCS 0.85; equal weight of carry, dollar carry, momentum, value 0.74, with GAPCS 0.87 (Table 6, 1999-2016).
- Pricing: DOL plus GAP adjusted R2 44% on the five portfolios; three-factor model 59% to 62% on larger sets (p. 21-23).

**Inconsistencies in the source**
- Text says the sorts give a "monotonic increase" (p. 2). Table 1 is not monotonic: linear projection P2 2.85 vs P3 2.23; Baxter-King P2 2.45 vs P3 2.39.
- Text says the forward discount plays "a negligible role" (p. 8). Table 1 HP cross-section ir is 1.60 of 6.66 (computed 24%).
- Table 6 reports drawdowns of 0.16 and 0.07 labelled "%", while Table 4 reports 6.88 in the same unit.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| VOL and IMB as second factor give "qualitatively identical" results, "available upon request". | p. 27, fn. 17 |
| The IA tests of model assumptions: the "empirical support" is two pooled regressions, no robustness. | p. 29, IA p. 15 |
| Gap is "highly correlated" with the model's z. | p. 28 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Sort currencies on output gap minus US output gap: quintile long-short, linear or rank weights, or time-series long-short against the US gap. Card: [[Output gap signal]]. | technique | signal | Business cycle risk is priced (p. 3). Rank and linear weights trade all currencies (p. 11). | p. 10-12 |
| 2 | Real-time output gap by linear projection on 12 lags from 24 months earlier, on data vintages. Same card: [[Output gap signal]]. | technique | signal | No revisions or forward-looking filter (p. 10). | p. 9-10 |
| 3 | Split excess return into spot change and forward premium. Card: [[Spot and roll return decomposition]]. | principle | evaluation | Shows the return is not carry (p. 12). | p. 8, 12 |
| 4 | No card (recession dating is ex post). Net dollar exposure and performance in US booms and recessions. | principle | evaluation | GAPTS is not dollar neutral (p. 12, fn. 10). | p. 15, Table A6 |
| 5 | No card (the desk's portfolio rule). Add the strategy to canonical currency strategies at equal weight; compare Sharpe. | principle | evaluation | Diversification (p. 18). | p. 18-19, Table 6 |
| 6 | No card (asset pricing test). Price the sorted portfolios with a GAP factor (GMM, conditional IV alpha). | technique | evaluation | Tests risk compensation (p. 19). | p. 19-27 |
| 7 | No card (data practice). Compare real-time vintage results with full-sample revised data. | principle | evaluation | Revised, two-sided filters may not be exploitable (p. 3). | p. 3, 9 |
| 8 | No card (cost convention). Net returns with 50% of the quoted bid-ask spread. | principle | evaluation | Quoted spreads exceed effective ones (p. 17). | p. 16-17 |

## 6. Regime observations

- GAPCS earns similar returns in US booms and recessions (p. 15, Table A6).
- GAPTS is long the dollar in US expansions and short in recessions; it lost when the dollar rose in the global financial crisis (p. 15-16).

## 7. Acknowledged limits

- Model abstracts from goods trade (p. 27).
- The full-sample gap uses two-sided filters and revised data (p. 3).
- Quoted, not effective, spreads (p. 17).
- Asset pricing tests have low power in small cross-sections (p. 22).

## 8. Not addressed

- Capacity, market impact, margin or leverage.
- Performance after 2016, or a test on the full-sample period in real time (vintages start in 1999).
- Holding periods other than one month, or other quantile counts.
- Release lag of industrial production beyond the Dec 1999 example.
- Drawdown duration of GAPCS.
- Rival explanations for the flat stretch after about 2010.
