---
type: technique
brick: universe
aliases: [Penny stock and micro-cap exclusion, Price under $5 and small-cap screen, Minimum age and market cap screen, Stablecoin exclusion, Top volume filter, Balanced panel, Minimum average daily volume, Seasoning period, Minimum turnover filter, Top 100 coins, ETF viability filter]
sources: 9
tested_on: [equities, crypto]
---

# Minimum price and size filter

> [!summary]
> Drops the cheapest and smallest assets from the universe before ranking, to avoid microstructure problems.

## How it works

- **Selection rule**: remove assets under a minimum price and in the smallest size bucket, using the breakpoints of a large reference exchange.
- **Liquidity filter**: price and size act as the liquidity proxy. No volume or spread test.
- **Point-in-time**: not stated by the authors.
- **Variant**: keep an asset only if it has been listed for a minimum time and its market cap stayed above a floor over that whole window.
- **Variant**: keep only assets traded over the whole sample, then the top share by trading volume.
- **Variant**: minimum turnover, seasoning period, or top N by size or liquidity.
- **Variant**: ETF universe: minimum history, minimum median dollar volume, minimum data coverage, and no leveraged or inverse funds.

## What the sources say

### Parameters
- **Lou 2019**
	- Price below $5 excluded (p. 195).
	- Bottom NYSE size quintile excluded (p. 195).
	- Universe: US CRSP-Compustat stocks (p. 194-195).
- **Begušić 2019**
	- Listed at least 26 weeks; market cap never below $1 million over those 26 weeks (p. 2)
	- Stablecoins removed; coinmarketcap.com data, Jan 2015 to Jan 2019 (p. 2)
- **Fil 2020**
	- Coins traded from Jan 2018 to Sept 2019 only, so no listing or delisting in the window (p. 172646)
	- Then the top 30% by volume; 181 coins reduced to 26 (p. 172646)
- **Kosch 2026**
	- Keep a futures contract only if its monthly average daily volume was at least 1,000 contracts in every month of 2006-2015 (p. 4)
	- Universe fixed before the first out-of-sample month, Jan 2016; 15 commodities kept, palladium and platinum dropped (p. 4)
- **Liu 2019**: market cap at least 1 million USD; non-return variables winsorised at 1% and 99% each week (p. 4)
- **Kozlowski 2021**: drop coin-periods with monthly turnover below 1% (fn 2)
- **Ozdamar 2021**: market cap at least 5 million USD; a coin enters six months after launch (p. 5, fn 8)
- **Fieberg 2025**
	- Market cap at least 1 million USD; drop observations above Bitcoin's market cap (p. 3121-3122)
	- Top 100 by size or by Amihud liquidity, or top 50% to 10% (p. 3145)
- **Unknown 2026**
	- At least 52 weeks of continuous history (fn 2, p. 6)
	- 13-week rolling median of daily volume above USD 100,000; at least 90% non-null closes in the 252-day window (fn 2)
	- Leveraged and inverse ETFs excluded, 77 funds in seven Refinitiv categories (fn 2)
	- 3,215 US ETFs kept (Table 5)

### Why
- **Lou 2019**: microstructure issues (p. 195).
- **Fil 2020**: a balanced panel and the volume filter mitigate liquidity-related issues (p. 172646)
- **Begušić 2019**: keeps the relevant, liquid coins a realistic investor would hold; $1 million is meant to avoid a large-cap bias (p. 2)
- **Kosch 2026**: tradability must be shown before the out-of-sample period, so the universe uses no future liquidity information (p. 4)
- **Liu 2019**: limits outliers (p. 4)
- **Kozlowski 2021**: limits microstructure effects (fn 2)
- **Ozdamar 2021**: low caps are too illiquid to trade; new coins behave oddly until adopted (fn 8)
- **Fieberg 2025**: checks the effect does not come from hard-to-trade coins (p. 3144)
- **Unknown 2026**: leveraged and inverse funds suffer volatility decay beyond one day and do not fit a holding period longer than a few days (fn 2, p. 6)

### Evidence
- **Lou 2019**: no test of the filter itself
	- All results use this universe, US 1993-2013 (p. 194-195).
	- Robustness to excluding small caps is claimed "available upon request" and not shown (fn 2, 8).
- **Begušić 2019**: no test of the filter itself
	- 711 coins qualify at least once; ≈ under 20 eligible before 2017, peak ≈ 540 in late 2018 (p. 2, ≈ Fig. 1)
- **Fil 2020**: no test of the filter itself
	- All results use the 26-coin set (p. 172646)
- **Kosch 2026**: no test of the filter itself
	- Raising the cutoff from 500 to 1,000 contracts removed no ticker (p. 4)
	- Minimum monthly volumes in 2001-2024 run from 1,007 (copper) to 48,893 (WTI crude) (Table 8)
- **Liu 2019**: filter not tested (p. 4)
- **Kozlowski 2021**: results robust to no filter or higher filters, not shown (fn 2)
- **Ozdamar 2021**: all 2,000 coins without the floor give similar results, not shown (fn 6)
- **Fieberg 2025**: real data, gross
	- Top 100 coins: CTREND 3.39% a week; 10% largest 2.51% (Table 8)
	- Median Sharpe 1.13 with a 1 USD price floor vs 1.64 without (Table 6)
- **Unknown 2026**: no test of the filter itself
	- All results use the 3,215-ETF universe (p. 6)

### Limits
- **Lou 2019**
	- The effect of the filter on the results is not shown (fn 2, 8).
- **Begušić 2019**
	- Effect of the filter on results not shown; survivorship of delisted coins not discussed (p. 2)
- **Fil 2020**
	- Dropping every coin listed or delisted in the window creates survivorship bias; not discussed (p. 172646)
	- Effect of the filter on results not shown (p. 172646)
- **Kosch 2026**
	- Effect on results not shown; one fixed threshold (p. 4)
- **Liu 2019**: effect of the floor not shown (p. 4)
- **Kozlowski 2021**: robustness not shown (fn 2)
- **Ozdamar 2021**: coin list not published (fn 7)
- **Fieberg 2025**: the price floor shrinks the cross section sharply (p. 3139)
- **Unknown 2026**
	- Effect of the filter on results not shown (p. 6)
	- Closed or delisted funds and survivorship not discussed (p. 6)

## Sources

- [[2019 - Lou Polk Skouras - A Tug of War Overnight vs Intraday Returns]] (Lou 2019)
- [[2019 - Begušić Kostanjčar - Momentum and liquidity in cryptocurrencies]] (Begušić 2019)
- [[2020 - Fil Kristoufek - Pairs Trading in Cryptocurrency Markets]] (Fil 2020)
- [[2026 - Kosch Forsberg - Seasonal Trading in Commodity Futures Evidence from Regression and Singular Spectrum]] (Kosch 2026)
- [[2019 - Liu Tsyvinski Wu - Common Risk Factors in Cryptocurrency]] (Liu 2019)
- [[2021 - Kozlowski Puleo Zhou - Cryptocurrency return reversals]] (Kozlowski 2021)
- [[2021 - Ozdamar Akdeniz Sensoy - Lottery-like preferences and the MAX effect in the cryptocurrency market]] (Ozdamar 2021)
- [[2025 - Fieberg Liedtke Poddig et al - A Trend Factor for the Cross Section of Cryptocurrency Returns]] (Fieberg 2025)
- [[2026 - Unknown authors - Momentum Strategies in ETFs under Simple Operational Rules]] (Unknown 2026)
