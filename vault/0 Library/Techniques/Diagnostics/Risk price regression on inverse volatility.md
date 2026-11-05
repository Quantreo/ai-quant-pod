---
type: diagnostic
kind: attribution
aliases: [price of risk and market volatility, conditional risk-return trade-off regression, factor risk price regression]
sources: 1
---

# Risk price regression on inverse volatility

> [!summary]
> Does the price of risk of a return series fall when market volatility is high?

## How it works

- **How**: regress next-month return divided by this month's realized variance on the demeaned inverse of realized market volatility. The intercept is the average price of risk, the slope says how it moves with volatility.
- **Reading**: a positive slope means the price of risk falls in high-volatility months, the case where scaling exposure down by variance is favoured. A zero slope means no timing gain from volatility.
- **Data needed**: daily returns of the series and of the market, to build monthly realized variance and volatility.

## What the sources say

### Parameters
- **DeMiguel 2024**
	- Regression r(t+1) / variance(t) = alpha + beta x demeaned (1 / market volatility(t)) + error, one per factor (Eq. 17, p. 29).
	- Variance: sample variance of the factor's daily returns in month t; volatility: sample volatility of daily market returns (p. 8, 29).
	- Newey-West t-statistics; nine US equity factors, January 1977 to December 2020 (Table V).

### Why
- **DeMiguel 2024**: with uncorrelated factors the ratio of expected return to variance equals the price of risk of the pricing kernel (Eq. 15-16, p. 28).

### Evidence
- **DeMiguel 2024**: real data, in-sample, gross
	- Intercept positive for all nine factors, significant for seven (Table V).
	- Slope positive for all nine; significant for MKT (t 2.36), HML (2.27), RMW (2.24), UMD (3.84), ROE (2.62), IA (1.98), BAB (7.20) (Table V).
	- Not significant for SMB (0.42) and CMA (0.75) (Table V).

### Limits
- **DeMiguel 2024**
	- Ignores correlations between factors; a shrinkage version only in the Internet Appendix (p. 28).
	- Fitted price of risk is negative in some months: about 30% of months for HML, under 15% for MKT (fn 40, p. 30).

## Sources

- [[2024 - DeMiguel Martin-Utrera Uppal - A Multifactor Perspective on Volatility-Managed Portfolios]] (DeMiguel 2024)
