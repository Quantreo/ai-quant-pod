---
type: diagnostic
kind: performance
aliases: [Cross-sectional correlation of forecasts, Out-of-sample R2 versus ranking, Sign hit rate of forecasts, Total OOS R2]
sources: 1
---

# Forecast ranking accuracy

> [!summary]
> Does a return forecast rank assets correctly, even when its exact level is wrong?

## How it works

- **How**: each month, correlate the forecasts with the realised returns across assets, then average over months. Add the share of correct signs. Put them next to the out-of-sample R² against the expanding historical mean, pooled across assets and months.
- **Reading**: a model can have a very negative R² and still rank well, because only the order matters for a long-short portfolio. Compare the months where the model beats the mean error with the others.
- **Data needed**: forecasts and realised returns per asset and month, and a historical mean forecast as benchmark.

## What the sources say

### Parameters
- **Kagkadis 2023**
	- OOS R² = 1 - sum of squared errors over sum of squared errors of the expanding mean; Total OOS R² pools factors and months, from month 240 (Eq. 6-7, p. 23)
	- Sign rate: share of correct signs of factor returns (p. 28)
	- Average cross-sectional correlation between forecasts and realised returns (p. 28)

### Why
- **Kagkadis 2023**
	- Total OOS R² is a distance measure and does not say whether strong performers are told from weak ones (p. 28)
	- Example: realised 3%, 2%, 1%, means 0%, 1%, 2%, forecasts 6%, 5%, 4% give R² of -145.45% with a perfect ranking (p. 28)

### Evidence
- **Kagkadis 2023**: real data, out of sample, gross, 72 factors, 1990-2019
	- PCA-PLS one component: Total R² -1.55%, cross-sectional correlation 9.12%. Beats the mean error in 54% of months (R² 12.24%, correlation 41%); in the other 46%, R² -17.17%, correlation -28% (Tables 1, 3; p. 29)
	- PCA one component: R² -0.55%, correlation 0.70%, long-short -0.10% a month (Tables 1, 3, 4)
	- 1-month factor momentum: R² -88.98%, correlation 5.98%, long-short 1.06% (Tables 1, 3, 4)

### Limits
- **Kagkadis 2023**
	- Sign rate stays between 49.90% and 52.75% for every model, so it separates little (Table 3)
	- No significance test for the correlations (whole paper)
	- The link to portfolio profit is shown by tables, not tested; the authors point to Kelly 2022 for the disconnect (p. 28)

## Sources

- [[2023 - Kagkadis Nolte Nolte et al - Factor Timing with Portfolio Characteristics]] (Kagkadis 2023)
