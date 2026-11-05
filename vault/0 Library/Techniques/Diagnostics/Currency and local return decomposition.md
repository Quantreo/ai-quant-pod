---
type: diagnostic
kind: attribution
aliases: [currency and local leg split, FX attribution of foreign returns, term structure of carry premia, carry by instrument maturity]
sources: 1
---

# Currency and local return decomposition

> [!summary]
> Does a foreign asset's return in home currency come from the currency or from the asset itself, and does a carry premium survive when it is held in longer instruments?

## How it works

- **How**: express the return of a foreign asset in home currency, in excess of the home short rate, as the asset's local excess return (over the foreign short rate) plus the currency excess return (foreign minus home short rate, minus depreciation). Run the same signal or sort on each leg, and on instruments of different maturity.
- **Reading**: legs moving in opposite directions across portfolios cancel in home currency. A premium found with bills that fades with bond maturity is offset by local term premia, not earned by the signal.
- **Data needed**: local-currency total returns, short rates in both currencies, spot exchange rates; zero-coupon curves for the maturity profile.

## What the sources say

### Parameters
- **Lustig 2013**
	- rx$ = rx* + rxFX, in logs (Eq. 3, p. 5).
	- Each leg regressed on rate or slope differentials; leg slopes sum to the total slope (p. 6).
	- Three-portfolio sorts, 10-year indexes, one-month hold (Table 3).
	- Zero-coupon maturities 3 months to 15 years, one-quarter hold (p. 15; Fig. 2).

### Why
- **Lustig 2013**: shows that the lack of dollar-return predictability comes from local bond returns offsetting currency returns (p. 7).

### Evidence
- **Lustig 2013**: real data, in-sample, gross, G10 1975-2015.
	- Panel on rate differentials: currency 1.98, local -1.34, dollar 0.65, not significant (Table 1A).
	- Rate deviation sort: currency 2.66%, local -3.78%, dollar -1.12% a year (Table 3).
	- Slope sort: currency 3.65%, local -5.61%, dollar -1.96% (Table 3).
	- Zero-coupon slope sort: 2.67% short end, -2.18% at 15 years; gap -4.85% (s.e. 1.82%) (p. 16).

### Limits
- **Lustig 2013**
	- 10-year indexes are coupon bonds (p. 4).
	- Zero-coupon panel unbalanced, 1985-2015, quarterly hold only (p. 15).
	- The local excess return contains the rate differential with a negative sign, so part of its predictability is mechanical (fn. 1, p. 7).
	- No transaction costs.

## Sources

- [[2013 - Lustig Stathopoulos Verdelhan - The Term Structure of Currency Carry Trade Risk Premia]] (Lustig 2013)
