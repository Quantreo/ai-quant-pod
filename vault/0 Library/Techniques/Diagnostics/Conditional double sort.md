---
type: diagnostic
kind: attribution
aliases: [sequential sort, dependent double sort, signal within buckets of another signal, bivariate sort, 3x3 sort, control-then-signal sort, median split on market structure variable]
sources: 7
---

# Conditional double sort

> [!summary]
> Does a signal still work inside groups of assets sorted on another signal?

## How it works

- **How**: each period, split the assets at the median of signal A. Within each half, build a long-short portfolio on signal B. Then swap the roles of A and B. Compare each portfolio across the two halves.
- **Variant**: split on both signals at the 30th and 70th percentiles into a 3x3 grid; compute the long-short spread of each signal in every row and column.
- **Reading**: similar results in both halves mean the two signals capture different returns; a signal that works in one half only depends on the other signal.
- **Data needed**: both signals per asset and date, next-period returns.
- **Variant**: average the signal spread across control deciles.
- **Variant**: split on a market-structure variable (share of speculators) instead of a second signal, and compare the long-short return across halves.

## What the sources say

### Parameters
- **Menkhoff 2016**
	- Median split on carry or value, rank portfolios within each half, quarterly (Table 9, p. 20).
	- 22 currencies vs USD, 1976Q1-2013Q4 (Table 9).
- **Begušić 2019**
	- 14-day return and 14-day Amihud illiquidity, 30/70 breakpoints, equal weight, rebalanced every 14 days (p. 3)
	- Crypto, Jan 2015 to Jan 2019; independent or sequential sort not stated (p. 2-3)
- **Liu 2019**: size halves at the median, then three-week momentum quintiles (Table A.2)
- **Kozlowski 2021**: size halves, then two Amihud illiquidity groups, then return quintiles (Table 3)
- **Ozdamar 2021**: deciles of a control (size, price, momentum, reversal, illiquidity, volatility, skewness), then MAX deciles, averaged across control deciles (p. 12)
- **Menkhoff 2011**
	- Median split on the lagged forward discount (or lagged idiosyncratic volatility, country risk, exchange-rate stability risk), then three portfolios on the lagged return, rebalanced monthly (p. 23, 32-33)
	- Idiosyncratic volatility: absolute residual of a regression on the dollar factor and HML-FX (fn 26, p. 32)
	- Up to 48 currencies vs USD, 1976-2010; risk ratings from 1985 (p. 33)
- **Zaremba 2016**
	- Median split on the non-commercial share of open interest, then median split on the signal (implied yield or past return) inside each half; difference of the two long-short returns (p. 36).
	- 26 commodity futures, monthly, 1987-2013 (p. 34, 36).

### Why
- **Menkhoff 2016**: to understand the link between carry and value (p. 20).
- **Begušić 2019**: to see whether momentum and the illiquidity premium are pervasive across groups (p. 3)
- **Liu 2019**: shows where momentum works (p. 28)
- **Kozlowski 2021**: isolates size and liquidity effects on reversal (p. 6)
- **Ozdamar 2021**: isolates MAX from other characteristics (p. 12)
- **Menkhoff 2011**: to separate momentum from carry (p. 23) and to test whether momentum depends on risky currencies, as a limit to arbitrage (p. 32-33)
- **Zaremba 2016**: median instead of deciles, to avoid small-sample bias in a small universe (p. 36).

### Evidence
- **Menkhoff 2016**: real data, gross.
	- Value Sharpe 0.53 among low-carry currencies, 0.46 among high-carry (Table 9).
	- Carry Sharpe 0.45 among low-value currencies, 0.57 among high-value (Table 9).
	- Authors: differences small, the two capture largely unrelated parts of the premium (p. 20).
- **Begušić 2019**: real data, in-sample, gross
	- Momentum significant in liquid coins only (0.26% a day); illiquidity premium significant among losers only (0.52%) (Table 1)
- **Liu 2019**: real data, in-sample, gross
	- Momentum 0.6% a week in small coins vs 4.2% in large (Table A.2)
- **Kozlowski 2021**: real data, in-sample, gross
	- Daily reversal 18.63% in small illiquid coins vs 0.44% in large liquid (Table 3)
- **Ozdamar 2021**: real data, in-sample, gross
	- MAX spread 1.5% to 2.7% a week value-weighted across controls; 0.9% after IVOL (Tables 7, 10)
- **Menkhoff 2011**: real data, in-sample, gross
	- Momentum 5.06% in low-rate currencies vs 5.36% in high-rate, difference 0.30% (t = 0.17) (Table 6)
	- Idiosyncratic volatility: 3.97% (t = 2.81) low vs 8.09% (t = 4.72) high (Table 11A)
	- Exchange-rate stability risk: 1.98% (t = 1.39) low vs 6.56% (t = 4.06) high (Table 11C)
- **Zaremba 2016**: real data, in-sample, excess return, no costs.
	- Term structure 1-2: 1.43% low share vs 0.41% high share, difference 1.02% (t = 2.18) (Table 2).
	- Momentum 12 months: 0.93% vs 0.66%, difference 0.26% (t = 0.52) (Table 4).

### Limits
- **Menkhoff 2016**
	- No test of the difference between halves is shown (Table 9).
	- Each half holds about 11 currencies (computed from 22).
- **Begušić 2019**
	- Only asterisks at 5%, no t-statistics (Table 1)
	- Printed spreads differ from the differences of cell means (Table 1)
- **Liu 2019**: two size groups only (Table A.2)
- **Kozlowski 2021**: small subsamples reduce power (fn 5)
- **Ozdamar 2021**: full 100-portfolio results not shown (fn 13)
- **Menkhoff 2011**
	- Text says low country risk gives no significant momentum; Table 11B shows 4.50% (t = 3.12) (p. 34)
	- Idiosyncratic volatility is defined on two factors the authors chose (fn 26, p. 32)
- **Zaremba 2016**
	- Each half holds at most about 13 commodities (computed from 26).
	- Only the 1-2 term structure difference is significant; 1-3 and 1-4 are not (Table 2).

## Sources

- [[2016 - Menkhoff Sarno Schmeling et al - Currency Value]] (Menkhoff 2016)
- [[2019 - Begušić Kostanjčar - Momentum and liquidity in cryptocurrencies]] (Begušić 2019)
- [[2019 - Liu Tsyvinski Wu - Common Risk Factors in Cryptocurrency]] (Liu 2019)
- [[2021 - Kozlowski Puleo Zhou - Cryptocurrency return reversals]] (Kozlowski 2021)
- [[2021 - Ozdamar Akdeniz Sensoy - Lottery-like preferences and the MAX effect in the cryptocurrency market]] (Ozdamar 2021)
- [[2011 - Menkhoff Sarno Schmeling Schrimpf - Currency Momentum Strategies]] (Menkhoff 2011)
- [[2016 - Zaremba - Strategies Based on Momentum and Term Structure in Financialized Commodity Markets]] (Zaremba 2016)
