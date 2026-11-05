---
type: diagnostic
kind: attribution
aliases: [risk or characteristic test, carry factor on momentum portfolios, factor pricing of another sort, Fama-MacBeth cross-sort test]
sources: 1
---

# Cross-sort factor pricing test

> [!summary]
> Does a factor built from one sort of the assets also price portfolios built on a different sort, which would make the premium a risk and not a feature of the first sort?

## How it works

- **How**: build the factor as top minus bottom group of the first sort. Take portfolios from a second sort of the same assets as test assets. Estimate their betas on the factor by time-series regression, then regress average returns on betas across portfolios (Fama-MacBeth without a constant, or GMM). Repeat without the factor of the second sort.
- **Reading**: if the first factor prices the second set about as well without the second factor, the premium is exposure to a common risk. Look at adjusted R², pricing-error RMSE, and whether the risk price equals the factor mean.
- **Data needed**: returns of both sets of portfolios and of the factors, same dates.

## What the sources say

### Parameters
- **Lustig 2008**
	- Test assets: six carry and six momentum currency portfolios, 37 currencies, 11/1983-03/2008 (p. 34).
	- Factors: first three principal components of the 12 portfolios, rescaled to zero-cost: dollar, momentum, carry (third component); then dollar and carry only (p. 34).
	- Fama-MacBeth, no constant in step two; run on 12, on carry-only and on momentum-only test assets (p. 12, 34-35).

### Why
- **Lustig 2008**: a characteristic-based explanation would imply no explanatory power for portfolios not sorted on interest rates (p. 3, 35).

### Evidence
- **Lustig 2008**: real data, in-sample, net of bid-ask.
	- 12 portfolios, three factors: adjusted R² 83.23, RMSE 0.70%; two factors: 68.13, 1.02% (Table 15).
	- Momentum portfolios only, two factors: adjusted R² 50.98 (Table 15).
	- Price of carry risk 9.96% to 10.05% a year across test assets (Table 15).

### Limits
- **Lustig 2008**
	- The carry factor is the third component of the same 12 test portfolios (p. 34).
	- Lowest momentum portfolio not explained (p. 34).
	- The sorts overlap: high-momentum currencies have higher rates (p. 33).

## Sources

- [[2008 - Lustig Roussanov Verdelhan - Common Risk Factors in Currency Markets]] (Lustig 2008)
