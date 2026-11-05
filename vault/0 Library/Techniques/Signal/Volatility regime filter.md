---
type: technique
brick: signal
aliases: [Volatility regime conditioning, VIX filter, High and low volatility states, lagged volatility sort, volatility-sorted months, Volatility ratio, Fast to slow volatility ratio, risk-return trade-off by market volatility tercile]
sources: 6
tested_on: [fx, equities]
---

# Volatility regime filter

> [!summary]
> Classifies each period by the level or change of volatility and reads, or holds, a strategy differently in high and low volatility states.

## How it works

- **Inputs**: a volatility measure: realized volatility of the strategy's own returns, implied volatility of the traded asset, or a market gauge such as the VIX.
- **Formula**: estimate volatility (for example an EWMA of squared deviations), then compare it with percentiles of its own history, or use its level or change directly.
- **Lookback / holding**: set by the estimator's decay and by the horizon at which returns are read.
- **Output**: a regime label (high, middle, low) or a continuous volatility score.
- **Direction**: depends on the strategy and the horizon; see the sources.
- **Tested on**: currency carry baskets and single currencies against the USD, and the US equity market.
- **Variant**: ratio of a fast to a slow EWMA volatility of the traded asset, mapped to the next return by a spline; a falling ratio is read as falling risk.

## What the sources say

### Parameters
- **Clarida 2009**
	- EWMA of squared deviations of daily carry returns, λ = 0.95, half-life 14 days (p. 10)
	- High volatility above the full-sample 75th percentile, low below the 25th (p. 11)
	- Variant: regimes from 1-month at-the-money implied volatility (p. 15, 21)
- **Brunnermeier 2008**
	- Signed VIX: VIX times the sign of the currency's rate differential, so the measure follows the trade direction (p. 23)
	- Weekly changes for the same-week test; quarterly level for horizons t+1 to t+10 (Tables 5, 8)
- **Moreira 2016**
	- Five buckets of the previous month's realized volatility of the US market, 1926-2015 (Fig. 1, p. 36).
	- Read per bucket: next-month mean, standard deviation, mean over variance, recession probability (Fig. 1).
- **Christensen 2020**
	- EWMA volatility with λ = 0.79 on 1-minute data; fast window 50, slow window 100 (p. 12)
	- Ratio mapped to the normalised next return by a B-spline with 6 knots, zero mean, refit on the previous 66 days (p. 11-13)
	- Windows chosen by a parameter sweep on "stability and predictive performance" (p. 12)
	- E-mini S&P 500, 1-minute bars, 2011 (p. 17)

- **DeMiguel 2024**
	- Months sorted into terciles of realized market volatility (sample variance of daily market returns), 1977-2020 (Fig. 1, p. 4).
	- Read for each of nine factors: next-month return over this month's realized factor variance, averaged per tercile (p. 4).
- **Harvey 2018**
	- Quintiles of the previous month's volatility; read next-month mean excess return and volatility, both annualised (Fig. 2, 6, p. 7, 12).
	- US equities 1926-2017 and US bonds 1962-2017.

### Why
- **Clarida 2009**
	- Carry returns depend strongly on volatility (p. 11)
	- Carry returns move inversely with realized and implied FX volatility (p. 10-11)
- **Brunnermeier 2008**
	- Rising VIX proxies funding constraints that force speculators to unwind carry trades (p. 2-3, 22-24)
	- Losses when VIX rises reflect a higher risk premium, earned back later (Table 8, p. 25)
- **Moreira 2016**: shows that the risk-return trade-off weakens when volatility is high, the motive for scaling by inverse variance (p. 1).
- **Christensen 2020**: the probability of a positive return falls as conditional volatility rises, under a Gaussian return model (p. 11-12)

- **DeMiguel 2024**: the trade-off falls with market volatility; the authors find this puzzling and state no cause (p. 4, 27).
- **Harvey 2018**: the sort shows whether scaling can help; flat mean return across quintiles points to a Sharpe gain (p. 7, 12).

### Evidence
- **Clarida 2009**: real data, in-sample, G10 carry baskets 1990-2009, gross or net not stated
	- High volatility state: all-currency 1v1 -9.75%, 2v2 -5.01%, 3v3 -1.89% a year (Table 2)
	- Low volatility state: all 14 baskets positive, 2.87% to 13.61%, mean over vol 0.38 to 1.34 (Table 2)
	- Ex JPY and USD baskets 1v1 to 3v3 stay positive in high volatility, 1.14% to 4.72% (Table 2)
- **Brunnermeier 2008**: real data, in-sample regressions, gross, no traded rule
	- Signed weekly VIX change on currency excess return, same week: -0.43 (SE 0.11) (Table 5)
	- Weekly VIX change on the 3x3 carry portfolio: -0.94 (SE 0.25) same week, -0.07 (SE 0.23) next week (Table 7)
	- Signed VIX level predicts higher carry returns from t+2 to about t+8 quarters, not at t+1 (Table 8, p. 25)
- **Moreira 2016**: real data, in-sample, gross, market only
	- Next-month mean ≈8% in the lowest bucket, ≈10% in the highest, no clear trend (≈ Fig. 1).
	- Next-month standard deviation ≈11% to ≈30%; mean over variance ≈7 to ≈1 (≈ Fig. 1).
	- Recession probability ≈0.10 in the lowest bucket, ≈0.42 in the highest (≈ Fig. 1).
- **Christensen 2020**: real data, one year, pre-cost
	- Sharpe ≈2.5 against long-only ≈0.45 (≈ Fig. 6, p. 14)
	- Correlation with long-only ≈0.17 (≈ Fig. 6)

- **DeMiguel 2024**: real data, in-sample, gross, nine US equity factors
	- Low tercile above high tercile for every factor (Fig. 1).
	- Market ≈15 low, ≈3 high; UMD ≈56 and ≈5; BAB ≈69 and ≈-2; CMA ≈14 and ≈12 (≈ Fig. 1).
- **Harvey 2018**: real data, in-sample, gross, no traded rule
	- Equities: next-month volatility rises with the quintile, mean return shows no clear pattern (Fig. 2, p. 7).
	- Bonds: mean return much higher in the high-volatility quintile (Fig. 6, p. 12).

### Limits
- **Clarida 2009**
	- Thresholds are full-sample percentiles: no ex-ante rule is tested (p. 11)
	- Volatility at t includes the return at t; regime returns may be contemporaneous, not predictive (p. 10-12, open question in the note)
	- Robustness to other thresholds claimed, not shown (p. 12)
- **Brunnermeier 2008**
	- The same-week loss is not tradable; next-week effect is not significant (Table 7)
	- The TED spread, the other funding gauge, is mostly insignificant (Table 6, p. 24)
	- Eight currencies against the USD, sample ends 2006 (p. 7)
- **Moreira 2016**
	- Chart only: no table, no standard errors (Fig. 1).
	- Market only; no sort shown for FX carry (whole paper).
- **Christensen 2020**
	- 40 knots instead of 6 double the in-sample result, "probably just fitting to noise" (p. 13)
	- One contract, one year; window choice data not stated (p. 12, 17)

- **DeMiguel 2024**
	- Chart only; no standard errors for the tercile means (Fig. 1).
	- Market's high tercile ≈3 sits above its medium one ≈2 (≈ Fig. 1).
- **Harvey 2018**
	- Chart only; captions say "previous month's return" while the text says volatility (Fig. 2, 6).

## Sources

- [[2009 - Clarida Davis Pedersen - Currency Carry Trade Regimes Beyond the Fama Regression]] (Clarida 2009)
- [[2008 - Brunnermeier Nagel Pedersen - Carry Trades and Currency Crashes]] (Brunnermeier 2008)
- [[2016 - Moreira Muir - Volatility Managed Portfolios]] (Moreira 2016)
- [[2020 - Christensen - Hidden Markov Models Applied To Intraday Momentum Trading With Side Information]] (Christensen 2020)
- [[2024 - DeMiguel Martin-Utrera Uppal - A Multifactor Perspective on Volatility-Managed Portfolios]] (DeMiguel 2024)
- [[2018 - Harvey Hoyle Korgaonkar et al - The Impact of Volatility Targeting]] (Harvey 2018)
