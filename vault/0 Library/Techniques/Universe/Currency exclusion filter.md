---
type: technique
brick: universe
aliases: [G10 currency universe, exclude sovereign or convergence risk, ex JPY and USD universe, pure FX risk universe, G10 liquid bond market panel, free-floating filter, exclude pegged regimes, euro legacy currency removal]
sources: 5
tested_on: [fx]
---

# Currency exclusion filter

> [!summary]
> Removes from a currency universe the currencies whose returns carry another risk than floating FX risk, or that play a special funding role.

## How it works

- **Selection rule**: drop currencies exposed to convergence toward a peg or union, or to sovereign risk, and optionally safe-haven or funding currencies, before ranking.
- **Variant**: exclude by period. Drop the years when a currency is pegged or managed (fixed band, gold convertibility) and keep only free-floating periods.
- **Liquidity filter**: none explicit; what remains is a developed-market set.
- **Point-in-time**: a currency can leave the universe on the date it joins a currency union, with one member kept as its successor.

## What the sources say

### Parameters
- **Daniel 2014**
	- G10 only: AUD, GBP, CAD, EUR (spliced with DEM), JPY, NZD, NOK, SEK, CHF, USD (p. 8-9).
	- Pre-euro European currencies and emerging markets excluded (p. 9).
- **Clarida 2009**
	- Three G10 universes: all, ex JPY, ex JPY and USD (p. 6-7; Table 1).
- **Lustig 2013**
	- Nine countries vs USD: Australia, Canada, Germany, Japan, New Zealand, Norway, Sweden, Switzerland, UK (p. 4).
- **Lempérière 2014**
	- FX starts in 1973. Excluded: Bretton Woods 1944-1971 (±1% band to USD), the gold standard and the managed currencies of the 1930s (p. 6).
	- 6 currency contracts across 7 countries (p. 4).
- **Menkhoff 2016**
	- France, Italy and Spain dropped in 1999 at euro adoption, Germany kept (fn. 21, p. 44).
	- 22 currencies vs USD, developed and emerging (p. 43-44).

### Why
- **Daniel 2014**
	- Pre-euro currencies: convergence trade, peso problem (p. 9).
	- Emerging markets: sovereign risk. Carry should bear pure FX risk (p. 9).
- **Clarida 2009**: the literature is dominated by the yen and the dollar; USD is a safe haven (p. 7).
- **Lustig 2013**
	- A small homogeneous panel of developed countries with liquid bond markets (p. 4).
	- More countries add power but bring less liquid, more default-prone bond markets (p. 18).
- **Lempérière 2014**: no trend can develop when a price is held in a band or fixed to gold; trends need freely traded, liquid instruments (p. 6).
- **Menkhoff 2016**: not argued (fn. 21).

### Evidence
- **Daniel 2014**: no test of the exclusion; all results use the G10 set (p. 8-9).
- **Clarida 2009**: real data, in-sample, 1990-2009, gross or net not stated
	- Ex JPY/USD baskets: higher mean and lower volatility than all-currency, 1v1 to 3v3 (p. 8-9; Table 1).
	- Top volatility quartile: all-currency 1v1 to 3v3 lose (-9.75% to -1.89%); ex JPY/USD earn 1.14% to 4.72% (Table 2).
	- Ex JPY/USD 4v4 still loses in that quartile, -0.67% (Table 2).
- **Lustig 2013**: no test of the exclusion in the PDF; results on larger country sets are said to hold, shown only in an Online Appendix (p. 18).
- **Lempérière 2014**: no test of the exclusion; pegged periods are never simulated (p. 6).
- **Menkhoff 2016**: no test of the exclusion.

### Limits
- **Daniel 2014**
	- Emerging and non-G10 currencies not tested (whole paper).
- **Clarida 2009**
	- Robustness to excluding the yen holds only "to a point" (p. 3).
	- Volatility quartiles are full-sample, so no tradable rule is tested (p. 11).
- **Lustig 2013**
	- The larger country sets are not listed in the PDF (p. 18).
- **Lempérière 2014**
	- The same rule is applied to bonds before 1918, to wartime Japan and Germany, and to fixed-price crude, all outside FX (p. 7-8).
	- No FX history at all before 1973 (p. 14).
- **Menkhoff 2016**
	- Only the euro rule is applied; emerging currencies stay in (p. 43-44).

## Sources

- [[2014 - Daniel Hodrick Lu - The Carry Trade Risks and Drawdowns]] (Daniel 2014)
- [[2009 - Clarida Davis Pedersen - Currency Carry Trade Regimes Beyond the Fama Regression]] (Clarida 2009)
- [[2013 - Lustig Stathopoulos Verdelhan - The Term Structure of Currency Carry Trade Risk Premia]] (Lustig 2013)
- [[2014 - Lempérière Deremble Seager et al - Two centuries of trend following]] (Lempérière 2014)
- [[2016 - Menkhoff Sarno Schmeling et al - Currency Value]] (Menkhoff 2016)
