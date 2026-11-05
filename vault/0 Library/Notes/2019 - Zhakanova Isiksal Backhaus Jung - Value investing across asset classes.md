---
type: reading-note
source: paper
title: Value investing across asset classes
authors: Zhakanova Isiksal, Backhaus, Jung
affiliations: Zhakanova Isiksal (Near East University, Turkey), Backhaus (LGT Bank AG, Liechtenstein), Jung (Hauck & Aufhäuser, Frankfurt) (p. 1407)
year: 2019
venue: Economic Research-Ekonomska Istraživanja 32(1), 1407-1429
doi: 10.1080/1331677X.2019.1636696
pdf: "[[2019 - Zhakanova Isiksal Backhaus Jung - Value investing across asset classes.pdf]]"
version: published journal article (open access)
tier: 1
read: full
tags: [value, multi-asset, monthly]
date: 2026-10-25
---

# Value investing across asset classes (Zhakanova Isiksal, Backhaus, Jung 2019)

## Summary

- **Finding**: two long-only value strategies on 8 assets, 1995-2015: relative 8.38% a year, absolute 7.54%, against 6.24% for 60/40 and 3.65% for equal weight (Table 2).
- **Mechanism**: the strategies add risky assets in stress phases, when the risk premium is high and sentiment low (p. 1409, 1427). No test of this is shown.
- **Where it works best**: 2002 to 2008, absolute strategy +15% to +30% a year (p. 1420). Both beat the naive mixes on return, not on Sharpe.
- **Weak spots**: Sharpe 0.63 and 0.65 against 0.70 for 60/40 (Table 2). Negative alpha for at least seven years, poor years after the crisis (p. 1420).
- **Main caveats**: no costs stated, z-score band 0 to 1.5 unexplained, eight assets, one 21-year sample, several text statements contradict the tables (section 3).

Page numbers follow the journal pagination (1407 to 1429). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Both strategies raise exposure to risky asset classes in stress phases, when the risk premium is highest and sentiment low | Weights charts (Fig. 5-6), regressions on stress variables (Tables 6-7) | p. 1409, 1427 |
| 2 | Return comes with a lagging risk-reducing character | Average drawdown similar to naive mixes (Table 2); full money market in 2009 (text) | p. 1420-1422 |
| 3 | Returns depend on interest-rate and macro variables: inflation, ISM, oil, EUR/USD | Regressions, R2 0.41 and 0.48 (Table 3) | p. 1423-1424 |
| 4 | Returns depend strongly on stocks and commodities, gold most significant | Regressions, R2 0.68 and 0.88 (Table 4) | p. 1424 |
| 5 | Literature view: value is either compensation for risk (Fama and French; Zhang) or investor errors and discomfort (Lakonishok; Haugen) | Citations only, no own test | p. 1408 |

**Caveats raised by the authors**
- Diversification is not enough to avoid losses in every cycle (p. 1420).
- Performance is poor in the years after the crisis, "a primary indication of distorted signal generation in times of expansive monetary policy" (p. 1420).
- Value strategies should be used as a complement within dynamic asset allocation, because of value phase shifts (p. 1407, 1427).
- The Sharpe ratio of 60/40 is better than both value strategies (p. 1423, 1427).

**Ruled out**: Not stated by the authors.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 8 assets, USD, net total return indices: MSCI World, MSCI Emerging Markets, US Treasury bonds, FTSE NAREIT, Gold, S&P GSCI, JPY/USD, EUR/USD | p. 1409 |
| Period | Data Dec 1992 to Dec 2015; back test Jan 1995 to Dec 2015, 252 monthly returns | p. 1409-1410, Table 1 |
| Value measure | Equities: earnings yield (1 / forward P/E). REITs: dividend yield. Bonds: yield to maturity. Currencies: real exchange rate vs OECD fair value. Commodity index: roll yield. Gold: US Treasury yield | p. 1410-1411 |
| Signal | z-score of the value measure against its own history, expanding window, minimum 24 months. High z = cheap | p. 1411 |
| Absolute entry | Hold an asset if 0.0 < z < 1.5 | p. 1412 |
| Relative entry | Hold the 3 assets with the highest cross-sectional z-score | p. 1412 |
| Sizing | Absolute: equal weight 1/N among selected. Relative: 1/3 each | p. 1412 |
| Exit | Absolute: asset leaves when z is at or below 0, or at or above 1.5. Relative: leaves when out of the top 3. If none selected, 100% money market | p. 1411-1412 |
| Rebalancing | Monthly, start of month, on the signal of the previous month end | p. 1411 |
| Costs | Not stated by the authors | whole paper |
| Benchmarks | Equal weight (12.5% each); strategic 60% MSCI World, 40% US Treasuries | p. 1413 |

**Rule**
- z(i,t) = (X(i,t) minus mean of X(i)) / sd of X(i), mean and sd over all months up to t (Eq. 8, p. 1411).
- Absolute: w = 1/N if 0 < z(t-1) < 1.5, else 0; N is the number of assets selected, cash if N = 0 (Eq. 9, p. 1412).
- Relative: w = 1/3 for the three highest cross-sectional z(t-1), else 0 (Eq. 11, p. 1412).
- Commodity roll yield = return of the excess return index minus return of the spot index (Eq. 7, p. 1411).
- Real effective exchange rate = trade-weighted sum of bilateral real rates, in logs (Eq. 2-3, p. 1410).

**Data provenance**
- P/E, dividend yield and yield to maturity from Bloomberg and DataStream (p. 1410).
- Index P/E uses 12-month forward consensus EPS, a time-weighted mix of fiscal year 1 and 2 forecasts (Eq. 4-5, p. 1410).
- Currency fair value from the OECD (p. 1410).
- Gross and net dividends are assumed equal when only one is reported (note 1, p. 1427).
- The money market rate is not named. Not stated by the authors.

## 3. Results

All results are real data over the same 21 years; the 0 to 1.5 band and the 24-month start are not shown as chosen out of sample. Costs not stated.

**Aggregate** (Table 2)
- Annual return: relative 8.38%, absolute 7.54%, strategic 6.24%, equal 3.65%.
- Volatility: 13.32%, 11.55%, 8.89%, 9.58%.
- Sharpe: 0.63, 0.65, 0.70, 0.38. Information ratio: 0.17, 0.06, -0.07, -0.31.
- Max drawdown: 39.68%, 32.15%, 34.17%, 35.3%. Historical ES 99%: -14.25%, -12.52%, -8.76%, -10.49%.
- Jensen alpha on MSCI World: 3.72%, 4.73%, 2.37%, 0.39%.
- Information ratio matches excess return over MSCI World divided by tracking error against MSCI World (computed, for example 1.54 / 9.45 = 0.16); the paper does not name the benchmark.

**By sub-group**
- Asset weights are charts only (Fig. 5-6). The text says relative holds mainly stocks and gold, REITs after the subprime crisis, and the dollar only when gold was dear (p. 1419-1420).
- No return by asset or asset class is given. Not addressed.

**Horizon and parameters**
- One parameter set. No variant of the band, the window or the number of assets held. Not addressed.

**Over time**
- Best stretch of relative: 2006 to 2008 (p. 1419).
- Absolute: +15% to +30% a year, 2002 to 2008 (p. 1420). 60/40 beat all strategies from 1997 to 2001 (p. 1420).
- Both strategies had negative alpha for at least seven years (p. 1420). Weak years after 2008 (p. 1420).
- Annual bars (Fig. 8-9): 2008 about -23% for relative and ≈-19% for absolute; 2009 ≈+31% and ≈+40%.
- Rolling 3-year volatility rises after 2008, peaks mid-2011, then 5% to 12% in 2015 (p. 1422, Fig. 10).
- Max drawdown dates: 27 Feb 2009 for relative, 31 Oct 2008 for absolute (Table 2).

**Link to other strategies**
- Regressions of strategy returns on factors (Tables 3 to 7). Absolute on financial factors: market 0.4216 (t 4.58), commodities 0.0790 (t 2.56), gold 0.3373 (t 8.82), R2 0.68 (Table 4).
- Relative: market 0.4078, bond -0.2045, gold 0.3116 (t 12.23), REITs 0.1727, EUR/USD 0.0832 (p 10.88%), R2 0.88 (Table 4).
- Macro regressions: ISM positive, oil positive, inflation negative for absolute (-0.5314, t -2.51), R2 0.41 and 0.48 (Table 3).
- Risk factors: VIX loading -0.3262 (absolute) and -0.4218 (relative), R2 0.31 and 0.38 (Tables 6-7).
- Stress regimes: credit spread loading -0.0519 (t -2.90) for absolute in stress only (Table 7).
- Intercepts are large in several tables (for example 1.6260 in Table 3); units are not stated.

**Inconsistencies in the source**
- Text p. 1423 gives R2 of 72% (absolute) and 98% (relative) for the financial factor model without regimes. Table 4 gives 0.68 and 0.88.
- Text p. 1423 says bonds, EUR/USD and REITs are negative determinants for relative. Table 4 shows EUR/USD +0.0832 (not significant) and REITs +0.1727 (significant, positive).
- Text p. 1424 says that when credit conditions worsen in stress, absolute return increases. The loading is negative, -0.0519 (Table 7).
- Text p. 1419 refers to Figure 5 for the relative strategy weights; Figure 5 is the absolute strategy (caption, p. 1420).
- Text p. 1420 says the strategy shown in Figure 6 (relative) was fully in the money market in 2009. Eq. 11 always holds three assets, and Figure 8 shows relative at ≈+31% in 2009.
- Abstract says better risk-reward ratios; Table 2 Sharpe of 60/40 (0.70) is above both strategies (0.63, 0.65). The conclusion says so (p. 1427).
- Cumulative return 542.25% over 21 years (Table 2) is not compatible with 8.38% a year (computed: 1.0838^21 is about 5.4 times, a gain of about 440%). The Figure 7 line ends ≈550 on a scale starting at 100.
- Back test said to span 20 years (p. 1409, 1423) while Table 1 has 252 monthly observations, 21 years.
- Eq. 16 is written as the CAPM expected return, not as alpha.
- Strategies are called out-of-sample, but no estimation step is described (p. 1407).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Back test is out of sample | p. 1407 |
| Better distributed returns, less left tail than naive mixes | p. 1417 |
| Strategies are "robust over time" | p. 1421 |
| Value strategies mitigate drawdown | p. 1407, 1427 |
| Strategies raise risky exposure in stress phases (no regime-split return or weights table) | p. 1409, 1427 |
| Value signal distorted by expansive monetary policy | p. 1420 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Value measure per asset class (earnings yield, dividend yield, yield to maturity, OECD real exchange rate, roll yield, Treasury yield for gold). Card: [[Value z-score signal]] | technique | signal | Common measures in the literature (p. 1409) | p. 1410-1411 |
| 2 | Z-score of the value measure against its own expanding history, hold when 0 < z < 1.5, else cash (absolute value). Card: [[Value z-score signal]] | technique | signal | Picks assets cheap against their own history; z above 1.5 excluded, no reason given | p. 1411-1412 |
| 3 | Top 3 of 8 assets by cross-sectional z-score, 1/3 each (relative value). Card: [[Value z-score signal]] | technique | signal | Picks assets cheapest against the other assets | p. 1412 |
| 4 | Real exchange rate against OECD fair value for currencies. Card: [[Currency value signal]] | technique | signal | Prices converge to PPP (p. 1409) | p. 1410 |
| 5 | Binary market stress indicator: mean of expanding z-scores of MSCI World, Citi Eco Surprise G10, TED spread, Baa credit spread, VIX. Card: [[Market state split]] | technique | signal | Splits regression into stress and stress-free | p. 1414-1415 |
| 6 | Regression of strategy returns on macro, market and risk factors, repeated with factors multiplied by the stress indicator. Card: [[Market state split]] (variant) | technique | diagnostic | Find the drivers of each strategy in each regime | p. 1415-1417 |
| 7 | Equal-weight and 60/40 benchmarks. No card: naive benchmarks | technique | evaluation | Naive comparison | p. 1413 |

## 6. Regime observations

- Longest stress spell in the indicator: mid-2008 to mid-2009; more frequent stress after the crisis (Fig. 12, p. 1423).
- VIX is the most significant risk factor for both strategies, including in stress and stress-free regimes (p. 1427, Table 7).

## 7. Acknowledged limits

- Poor performance after the crisis, with distorted signals in expansive monetary policy (p. 1420).
- Value should be a complement to dynamic asset allocation (p. 1427).

## 8. Not addressed

- Transaction costs, slippage, taxes, capacity.
- Statistical tests of the return difference against the benchmarks.
- Why the band is 0 to 1.5, why 24 months, why three assets.
- Return by asset or asset class; the profit decomposition.
- Sensitivity to the parameters; out-of-sample in the strict sense.
- The money market rate used; which Sharpe risk-free rate.
- Unit of the regression variables (levels or changes).
