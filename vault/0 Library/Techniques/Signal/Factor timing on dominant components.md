---
type: technique
brick: signal
aliases: [Factor timing, Anomaly timing, Valuation spread timing, Principal component factor timing, Book-to-market timing of factors, Characteristic-based factor timing, PLS and LASSO factor timing]
sources: 2
tested_on: [equities]
---

# Factor timing on dominant components

> [!summary]
> Predicts the returns of many stock factors at once by forecasting only their few largest principal components with each component's own valuation spread.

## How it works

- **Inputs**: returns of many long-short factors and a predictor for each, such as the book-to-market spread between its legs.
- **Formula**: rescale the factors, take principal components, keep the largest few. Regress each component's next return on its predictor. Map the forecasts back to each factor.
- **Lookback / holding**: components and coefficients from an initial or expanding window; monthly forecasts.
- **Output**: an expected return for each component and for each factor.
- **Direction**: long and short factors, timed over time.
- **Tested on**: US stock anomaly portfolios.
- **Choice of k**: from a prior on predictability and a Sharpe cap, or fixed.
- **Variant**: predictors are all factor characteristics, weighted by the loadings, compressed by PCA or PLS; LASSO picks components.

## What the sources say

### Parameters
- **Haddad 2020**
	- 50 anomaly portfolios, decile 10 minus decile 1, value-weighted, monthly, 1974-2017 (p. 17)
	- bm = log book-to-market of decile 10 minus that of decile 1 (p. 17)
	- Market-adjusted, rescaled to equal variance; betas, variances, eigenvectors from the first half only (p. 17-18)
	- Five PCs plus the market, from a 75 bp total R² prior and a monthly squared Sharpe cap of 8.3% (p. 18-19)
- **Kagkadis 2023**
	- 72 anomalies of Green 2017, decile 10 minus decile 1, value-weighted, monthly, 1970-2019; price under $5 removed, NYSE breakpoints (p. 20)
	- Forecasts out of sample 1990-2019; expanding window of at least 240 months, components re-estimated each month (p. 13, 23)
	- 5 PCs by PCA or by Risk Premium PCA (gamma 10), about 67% of variance (p. 2, 14)
	- Characteristics standardised across factors each month; PC characteristics = loadings times characteristics (p. 11, 14)
	- OLS on the first component, or LASSO on all, penalty chosen on a rolling 60-month validation (p. 15)

### Why
- **Haddad 2020**
	- With no near-arbitrage, small components cannot be predictable (p. 12-14)
	- Book-to-market is a discounted sum of future expected returns (p. 19-20)
	- Own-bm forecast of each anomaly gives about half the predictability (p. 4-5)
- **Kagkadis 2023**
	- Stocks sit in several legs, so characteristics of other portfolios can matter (p. 1-2)
	- PLS keeps only the return-relevant variation of the characteristics (p. 3)
	- LASSO lets the number of components change over time (p. 31-32)

### Evidence
- **Haddad 2020**: real data, split sample, gross
	- Out-of-sample monthly R²: PC1 4.82%, PC4 3.52%, market 1.00% (Table 2)
	- Total out-of-sample R² 0.93% over the 50 anomalies; about half have R² above 1% (p. 25)
	- Pure anomaly timing Sharpe 0.71 in sample and 0.77 out of sample (Table 6)
- **Kagkadis 2023**: real data, out of sample, gross, 1990-2019
	- Total out-of-sample R²: one component -1.55% to -0.38%; LASSO 0.52% to 1.53% (Table 1)
	- Long-short of factor forecasts 1.47% a month, t 3.40, against 1.06% for 1-month factor momentum (Table 4)
	- Book-to-market on the 5 PCs: Total R² 0.43%, long-short 0.79% (Tables 1, 4)
	- Own characteristic only, per anomaly: long-short 0.46% (Table 6)

### Limits
- **Haddad 2020**
	- PC5 is not predictable; PC2 and PC3 turn negative in expanding and rolling windows (Table 2, A.1)
	- Gross profitability has out-of-sample R² of -4.7% (Table 3)
	- No transaction costs; one predictor only (p. 20, 39)
- **Kagkadis 2023**
	- One component, no LASSO: no skill in exact terms; PCA long-short -0.10% (Table 4)
	- Anomalies with small PC loadings are not predicted (p. 25)
	- Gain over the book-to-market model is not significant (Table 2)
	- No costs, no turnover; number of PCs, gamma and windows fixed by the authors (whole paper)

## Sources

- [[2020 - Haddad Kozak Santosh - Factor Timing]] (Haddad 2020)
- [[2023 - Kagkadis Nolte Nolte et al - Factor Timing with Portfolio Characteristics]] (Kagkadis 2023)
