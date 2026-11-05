---
type: reading-note
source: paper
title: Understanding the profitability of currency-trading strategies
authors: Craig Burnside, Martin Eichenbaum, Sergio Rebelo
affiliations: NBER Program on Economic Fluctuations and Growth (Research Associates)
year: 2012
venue: NBER Reporter, 2012 Number 3, pp. 10-14
doi: none (handle https://hdl.handle.net/10419/103224)
pdf: "[[2012 - Burnside Eichenbaum Rebelo - Understanding the profitability of currency-trading strategies.pdf]]"
version: 6-page research summary, not the full paper
tier: 1
read: full
tags: [carry, fx, monthly]
date: 2026-10-25
---

# Currency carry and momentum payoffs (Burnside, Eichenbaum, Rebelo 2012)

> This is a 6-page summary of the authors' own earlier papers, not a full paper. It gives a few headline numbers, one figure and no tables. Everything below is what this summary states. Details (exact rules, tables, tests) sit in the papers it cites and were not read.

## Summary

- **Finding**: Equal-weighted monthly carry and momentum on 20 currencies, 1976-2012: carry 4.5% a year, Sharpe 0.86; momentum 4.4%, Sharpe 0.60; US stocks Sharpe 0.41 (p. 10).
- **Mechanism**: Both profits come from the failure of uncovered interest parity; the authors reject conventional risk compensation and point to peso-type states, microstructure frictions and overconfidence (pp. 11-13).
- **Where it works best**: Diversification across currencies cuts carry volatility by over 50% (Sharpe doubles); carry and momentum are roughly uncorrelated with each other and with stocks (p. 11).
- **Weak spots**: Worst calendar year: carry -5.6% (2008), momentum -10.9% (2012). Single-currency carry in 2008 was about -20% (NOK, NZD) (p. 11).
- **Main caveats**: Payoffs appear to be gross of transaction costs (costs not mentioned). No tables, no standard errors in this text. Hedged carry and peso results rest on cited papers.

Page numbers follow the journal pagination (NBER Reporter pp. 10-14; PDF pages 2-6). Values marked ≈ are read from a chart. None are used here.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Both strategies profit because uncovered interest parity (UIP) fails. | Stated; UIP failure called "extensively documented" (Fama 1984, Eichenbaum and Evans 1995). | p. 11 |
| 2 | Profits are not compensation for conventional risk. | Covariance with conventional risk factors is not statistically significant; large, significant pricing errors ("high alphas"). | p. 11 |
| 3 | Carry-factor models do not explain momentum. | Models of Lustig et al. (2011) and Menkhoff et al. (2012) leave momentum with a large, significant alpha (BER 2011). | p. 11 |
| 4 | Negative skewness does not explain the payoffs. | Carry skewness statistically insignificant, and smaller than US stocks if taken at face value; momentum positively skewed, not significantly. | p. 11 |
| 5 | A peso event is consistent with the carry payoff, but the event is a high discount factor with moderate losses, not huge losses. | Currency-option data: hedged carry pays less than unhedged; hedged and unhedged non-peso payoffs are similar (BEKR 2011). Same result for a carry plus momentum portfolio (BER 2011). | p. 12 |
| 6 | Price pressure (price depends on quantity traded) keeps average payoffs positive while the marginal trade earns nothing. | Model argument (BER 2011). | p. 12 |
| 7 | Adverse selection for market makers (worse when the currency is expected to appreciate) produces the forward premium puzzle. | Model (BER 2009). | p. 12 |
| 8 | Investor overconfidence makes spot and forward rates overshoot, giving the forward premium puzzle and profitable carry. | Model (Burnside, Han, Hirshleifer, Wang 2011). | p. 13 |

**Caveats raised by the authors**
- Payoffs are fat-tailed: excess kurtosis, especially for carry (p. 11).
- Small observed fat tails partly reflect diversification across currencies (p. 11).
- Option counterparty default in the hedged carry is possible, judged small because exchange-traded options are marked to market daily (fn. 9, p. 13).
- The question "who is on the other side and why" is open; the authors suspect heterogeneous expectations and persistent disagreement (p. 13).

**Ruled out**
- Conventional risk factors, and carry-specific factors for momentum (claims 2 and 3).
- Negative skewness (claim 4).
- The 2008 crisis as the rare disaster that justifies the profits: momentum made money in it (p. 12).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 20 currencies: Australia, Austria, Belgium, Canada, Denmark, France, Germany, Ireland, Italy, Japan, Netherlands, New Zealand, Norway, Portugal, South Africa, Spain, Sweden, Switzerland, UK, US (domestic is USD) | p. 10, fn. 1 p. 13 |
| Period | March 1976 to January 2012 | p. 10 |
| Carry signal | Borrow low-interest currencies, lend high-interest currencies. Exact signal not given here | p. 10 |
| Momentum signal | Long (short) currencies whose past returns were positive (negative). Past return is the previous month | p. 10, fn. 2 p. 13 |
| Sizing | No parameters to estimate. Variants such as optimal weights or volatility triggers are mentioned, not tested | p. 10 |
| Portfolio | Equal-weighted combination of the single-currency strategies | p. 10 |
| Rebalancing / horizon | Monthly | p. 10 |
| Costs | Not stated | |
| Cumulative payoff | Zero net investment: 1 USD in an account earning the T-bill rate, balance bet each period on the strategy, payoff deposited | fn. 3 p. 13 |

**Rule**: Not given as a formula in this summary. Carry: long high-rate, short low-rate currency, equal weights. Momentum: sign of previous month's return, equal weights. The exact definitions are in BER (2011) (NBER WP 16942), not read.

**Data provenance**: Not stated here. Option data used for the hedged carry are from BEKR (2011), not described.

## 3. Results

All results are real data, in-sample, full period. No out-of-sample split is given.

**Aggregate** (annualised; text does not say gross or net, no costs mentioned; p. 10)

| Strategy | Mean payoff | Std dev | Sharpe |
| --- | --- | --- | --- |
| Carry | 4.5% | 5.2% | 0.86 |
| Momentum | 4.4% | 7.3% | 0.60 |
| US stocks (excess return) | 6.5% | 15.8% | 0.41 |

Sharpe is the mean excess return over its standard deviation (p. 10).

**By sub-group**
- Individual currencies: diversification cuts payoff volatility by more than 50% with the same average payoff, so the portfolio Sharpe doubles relative to the average single carry trade (p. 11). Similar gains for momentum (p. 11).
- Carry in 2008: USD vs NOK and USD vs NZD about -20%; USD vs EUR and DKK about +14% (p. 11).
- Emerging-market currencies: similar diversification gain for carry, in a cited paper (fn. 5, p. 13). Not shown.

**Horizon and parameters**
- Only the monthly version is reported (fn. 2 p. 13). Not addressed otherwise.

**Over time**
- Figure 1 (p. 10): cumulative returns of carry, momentum, US stocks and T-bills, March 1976 to January 2012, on a log scale. The text says both currency strategies end almost as high as stocks and are much less volatile. Chart not read for values.
- Worst annual payoff: carry -5.6% in 2008, momentum -10.9% in 2012; US stocks -40% in 2008 (p. 11).
- Momentum made money during the 2008 crisis (p. 12).

**Link to other strategies**
- Carry and momentum payoffs are "roughly uncorrelated" (no figure given). Both are uncorrelated with US stock returns (p. 11).
- Carry-factor models leave momentum with a significant alpha (p. 11).
- Utility illustration (BEKR 2006): an investor with relative risk aversion of 5 would put 187% of the portfolio in carry, 68% in stocks and borrow 157% at the risk-free rate (p. 11). This is a model calculation on in-sample moments.

**Inconsistencies in the source**
- None found. One point to note: the 2012 annual loss of momentum (-10.9%) is for a year that ends in the sample at January 2012 (p. 11 vs p. 10), so it covers at most one month of 2012. The text does not explain this.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Hedged carry (with options) earns less than unhedged carry | p. 12 |
| Risk factors leave economically large, significant pricing errors | p. 11 |
| Carry and momentum skewness not significant | p. 11 |
| Carry and momentum payoffs roughly uncorrelated with each other and with stocks | p. 11 |
| Carry strategies that use the interest differential as a forecast have lower Sharpe ratios than the carry trade | fn. 6 p. 13 |
| Similar diversification gains for emerging-market carry | fn. 5 p. 13 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Carry: long high-rate, short low-rate currencies, equal-weighted across currencies | technique | signal | Needs no parameter estimate | p. 10 |
| 2 | Momentum: sign of previous month's return per currency, equal-weighted | technique | signal | Needs no parameter estimate | p. 10, fn. 2 |
| 3 | Equal-weighted portfolio of single-currency strategies | principle | sizing | Diversification halves volatility, doubles Sharpe | p. 11 |
| 4 | Hedged carry: buy a call (put) on the currency borrowed (lent) | technique | risk | Bounds losses to test the peso explanation | p. 12 |
| 5 | Cumulative payoff of a zero-net-investment strategy: bet the T-bill account balance each period | technique | evaluation | Not argued | fn. 3 p. 13 |

The rules in 1 to 3 are already in the library cards of carry, momentum and weighting. No new card from this summary alone.

## 6. Regime observations

- 2008: carry lost 5.6% in the year, individual carry trades diverged widely; momentum gained (pp. 11-12).
- No other regime split in this summary.

## 7. Acknowledged limits

- Excess kurtosis in payoffs, especially carry (p. 11).
- The authors suspect the real answer involves heterogeneous expectations and disagreement, which mainstream macro models do not yet contain (p. 13).

## 8. Not addressed

Transaction costs and bid-ask spreads, capacity, leverage, drawdown depth and duration, out-of-sample tests, sub-period results, results by currency, the exact carry signal and data sources, t-statistics, momentum lookbacks other than one month, and the correlation values.
