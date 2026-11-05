---
type: technique
brick: signal
aliases: [carry, carry trade, currency carry, interest rate differential, forward premium, basis, roll yield, term structure slope, roll-down, carry1-12, carry timing, conditional carry, de-meaned interest rate sort, slope carry, yield curve slope currency signal, dollar carry, forward discount, TS-Carry, CS-Carry, Crypto carry, Lending rate carry, Stablecoin carry, average forward discount, forward discount sort, HML_FX, implied yield]
sources: 9
tested_on: [multi-asset, fx, commodities, crypto]
---

# Carry signal

> [!summary]
> Measures what a position earns if prices stay unchanged, then goes long the assets with the highest carry and short the lowest.

## How it works

- **Inputs**: futures or forward and spot prices, short rates, or yield curves.
- **Formula**: carry = return if prices do not move. Futures: (spot - futures) / futures. Currencies: foreign minus home short rate. Commodities: slope between the two nearest contracts. Bonds: yield slope plus roll-down. 12-month average possible.
- **Lookback / holding**: current carry at the rebalance date; hold one period (week to quarter).
- **Output**: a cross-sectional rank (long top, short bottom), or per asset the sign of carry or its gap to its own mean.
- **Direction**: long-short.
- **Tested on**: currencies, commodities, equity indexes, bonds, credit, index options.
- **Variant**: yield-curve slope as a currency signal: long flat-curve, short steep-curve currencies.
- **Variant**: dollar carry: long or short all currencies together against the base currency by the sign of their average carry.
- **Variant**: crypto: platform lending rate minus USD rate.
- **Variant**: stablecoin vs USD, time series, flat inside a rate band.

## What the sources say

### Parameters
- **Koijen 2013**
	- C = (S - F) / F at month end, one-month hold (Eq. 5, p. 6-7, 18-19).
	- Commodities: two nearest contracts, per month (p. 11). Bonds: synthetic 1-month future on a 10Y zero (p. 13-14).
	- Carry1-12: 12-month average, window stated two ways (p. 19; App. C, p. 42).
	- Timing: sign of carry, or carry vs its mean (p. 29; Table VII).
- **Brunnermeier 2008**
	- Rank 8 currencies vs USD by 3-month interbank rate; long top k, short bottom k, k = 1, 2, 3 (p. 7, 11).
	- Rebalance weekly or quarterly, 1986-2006 (p. 11; Table 2).
- **Clarida 2009**
	- G10, rank by interest rate; long N highest, short N lowest, N = 1 to 5 (p. 6).
	- Run on all currencies, ex JPY, ex JPY and USD (p. 6-7).
- **Gorton 2007**
	- Basis = (F1 / F2 - 1) x 365 / (D2 - D1), F1 nearest, F2 next contract, D days to last trading date (fn. 6, p. 10).
	- 31 commodities ranked at month end; long the top half, short the bottom half, monthly (p. 16, 19).
- **Lustig 2013**
	- Nine G10 currencies vs USD, three portfolios monthly on the short rate minus its past 10-year rolling mean; long top, short bottom (p. 10).
	- Slope: 10-year yield minus one-month (Table 3) or three-month rate (Fig. 1-2); long flattest, short steepest (p. 14).
	- Per country: long foreign, short US when the foreign rate is higher or its slope lower (Table 2).
	- Run with bills and 10-year bonds, one-month hold (Table 3).
- **Chernov 2020**
	- Forward discount S/F - 1, month-end one-month forwards, nine G10 currencies vs USD, 1985-2020 (p. 10, 15-17).
	- CS-Carry: rank weights; TS-Carry: sign per currency (p. 15-16).
	- Dollar Carry: long or short all currencies together by the sign of the average forward discount (p. 15).
- **Fan 2024**
	- Bitfinex hourly lending rates, volume-weighted daily; 44 coins, Oct 2016 to Nov 2021 (p. 6-7)
	- Weekly terciles, equal weight, long High, short Low (p. 11)
	- Cost check: lender rate = 0.85 x borrower rate (Table A1)
	- Stablecoin carry: USDT and DAI, one-month hold, formed daily (p. 27)
- **Lustig 2008**
	- Forward discount f - s at month end, 37 currencies vs USD, six portfolios, equal weight, long the highest, short the lowest, monthly (p. 8).
	- Net version: forward bid on entry, spot ask on exit, on every leg (p. 7-8).
	- Variant: average forward discount across the six portfolios as one forecaster of each portfolio's excess return, 1 to 12 months (p. 22-25).
- **Zaremba 2016**
	- Implied yield = [ln(P nearest) - ln(P distant)] x 365 / (days to distant expiry - days to nearest expiry), nearest vs second nearest contract (Eq. 1, p. 35).
	- Checks with the first vs third and first vs fourth contract (p. 35).
	- 26 commodity futures, long the top half, short the bottom half, equal weight, monthly, 1987-2013 (p. 34, 36).

### Why
- **Koijen 2013**
	- Model-free, observable ex ante, same in every class (p. 6-7).
	- Commodity spot illiquid; few liquid bond futures (p. 11, 13-14).
	- Carry1-12 smooths seasonality (p. 19).
- **Brunnermeier 2008**: a portfolio shows how carry relates to returns beyond single currencies (p. 11).
- **Clarida 2009**: more currencies per leg lower volatility (p. 6, 8).
- **Gorton 2007**
	- The shape of the futures curve reflects inventories; low inventories mean a higher risk premium (p. 8, 10).
	- Halves sort is nonparametric and controls cross-sectional dependence (p. 16, 19).
- **Lustig 2013**
	- De-meaning isolates conditional carry; a level sort adds the unconditional premium (p. 10, 14-15).
	- Slope is the strongest predictor of currency and term premia, 1985-2015 (p. 15).
- **Chernov 2020**: with a random-walk spot rate the forward discount is the expected excess return, a robust forecaster (p. 10).
- **Fan 2024**
	- Realistic platform rates rather than illiquid derivatives (p. 5)
	- Equal weight so that major coins do not drive the result (p. 11)
- **Lustig 2008**
	- Forward discount equals the interest differential under covered parity; forwards are easy to trade, with spreads available and little counterparty risk (p. 2, 6).
	- The average discount drops country-specific inflation information (p. 24).
- **Zaremba 2016**: the curve shape reflects hedging pressure. Short hedgers push futures down, long speculators earn the premium (p. 32).

### Evidence
- **Koijen 2013**: real data, in-sample, gross.
	- Sharpe positive in all nine classes, 0.37 to 1.80 (Table II A).
	- Return on carry coefficient positive everywhere, not significant for commodities and calls (Table VI).
	- Sign timing: Sharpe 0.23 to 1.01 (Table VII).
	- Carry1-12 Sharpe lower in 7 of 9 classes (App. C).
- **Brunnermeier 2008**: real data, in-sample, gross.
	- Carry portfolios Sharpe 0.592 (2x2 weekly) to 0.784 (3x3 quarterly) (Table 2).
	- Rate differential on next-quarter FX excess return: 2.17 (SE 0.78), fading to -0.04 at t+10 (Table 3).
- **Clarida 2009**: real data, in-sample; gross or net not stated.
	- 1990-2009 baskets: mean 2.38% to 5.66% a year, mean over vol 0.25 to 0.66 (Table 1).
	- Volatility and mean both fall as N rises, 1v1 4.98% to 5v5 3.28% (p. 8).
- **Gorton 2007**: real data, in-sample, gross.
	- High minus low basis 1969-2006: 10.23% a year, t = 3.73 (Table 6).
	- 1990-2006: 11.57%, t = 4.08 (Table 6).
	- High-basis half holds lower inventories, t = -17.08 (Table 6).
- **Lustig 2013**: real data, in-sample, gross, G10 1975-2015.
	- Rate deviation sort, bills: 2.66% a year, Sharpe 0.36 (Table 3B).
	- Slope sort, bills: 3.65%, Sharpe 0.49 (Table 3B).
	- Same sorts with 10-year bonds in USD: -1.12% and -1.96%, not significant (Table 3D).
	- Zero-coupon slope sort: 2.67% at the short end, -2.18% at 15 years (p. 16).
- **Chernov 2020**: real data, in-sample, gross, G10 1985-2020
	- Sharpe: TS-Carry 0.685, Dollar Carry 0.576, CS-Carry 0.469 (Table 2B).
	- No alpha on the authors' mean-variance factor; R² 0.151 (CS) and 0.163 (TS) (Table 2B).
	- A mean-variance portfolio on carry alone: Sharpe 0.871, vs 1.075 with value and trend added (Table 1D).
- **Fan 2024**: real data, in-sample, gross of trading costs, crypto
	- High minus Low 43.4% a year, vol 58.9%, Sharpe 0.74 (Table 4)
	- Price change 24.0% of the return, rate differential 19.4% (Table 4)
	- Panel β of returns on carry 1.66 to 1.69 (Table 2)
	- Stablecoin carry USDT 9.28% a year, Sharpe 3.54 (Table 9)
- **Lustig 2008**: real data, in-sample, net of bid-ask, 37 currencies, 11/1983-03/2008.
	- High minus low 4.83% a year, Sharpe 0.54; gross 8.83%, 0.99 (Table 1).
	- Developed currencies: 3.46%, Sharpe 0.40 (Table 1).
	- Average forward discount R² 2.68% to 7.85% at one month, 17.54% to 32.57% at 12 months (Tables 7-8).
	- Price of carry risk 5.46% a year, adjusted R² 69.28 (Table 3).
- **Zaremba 2016**: real data, in-sample, excess return, no costs.
	- 1-2 spread 0.92% a month, t = 4.14, Sharpe 0.80 (Table 2).
	- 1-3 spread 0.97% (t = 4.46), 1-4 spread 0.68% (t = 3.07) (Table 2).
	- Alpha 0.66% to 0.90% a month on three factor models, 1-2 spread (Table 3).

### Limits
- **Koijen 2013**
	- No costs; higher costs than passive, per the authors (p. 22).
	- Bond level carry Sharpe 0.52 vs 0.74 passive (Table II A).
	- Commodity carry hit by seasonality (p. 28).
	- Timing: no t-statistics shown (p. 29).
- **Brunnermeier 2008**
	- Skewness -0.54 to -0.98; adding currencies does not reduce it (Table 2, p. 11).
	- With signed VIX added, rate differential coefficient 1.35 (SE 1.36), not significant (Table 8).
	- No costs; eight currencies vs USD only.
- **Clarida 2009**
	- In the top quartile of FX volatility, all-currency 1v1 loses 9.75% a year (Table 2).
	- Rebalancing frequency and costs not stated.
- **Gorton 2007**
	- No costs; one lookback and one holding period only.
	- Basis and 12-month momentum portfolios correlate at 0.87 (p. 21).
	- Part of the basis return is orthogonal to inventories, left unexplained (p. 25).
- **Lustig 2013**
	- Local term premia offset the currency premium: -3.78% (rates), -5.61% (slope) (Table 3C).
	- Offset in rate sorts weakens from the mid-1980s or 1990s (p. 15).
	- No transaction costs.
- **Chernov 2020**
	- Carry-only expected returns rejected on long-horizon returns of the carry strategies, p = 0.023 (Table 3).
	- Optimal timing adds nothing to CS-Carry, t 0.46 (Table 4A).
	- No transaction costs (whole paper).
- **Fan 2024**
	- High minus Low significant at 10% only (Table 4)
	- No significant alpha under the Cong et al. five-factor model (Table 5B)
	- No stablecoin depeg in the sample (p. 28)
- **Lustig 2008**
	- Single sample, no out-of-sample test.
	- Market beta of the carry factor up to 1.22 in crisis windows, alpha -3.82% over six months (Table 11).
	- A currency enters only with spot and forward in the current and next period (p. 8).
	- Sort date stated as t in the text and t-1 in the Table 1 note (p. 8).
- **Zaremba 2016**
	- No transaction costs (not addressed).
	- 26 contracts, start dates differ by commodity (Table 1, p. 43).

## Sources

- [[2013 - Koijen Moskowitz Pedersen et al - Carry]] (Koijen 2013)
- [[2008 - Brunnermeier Nagel Pedersen - Carry Trades and Currency Crashes]] (Brunnermeier 2008)
- [[2009 - Clarida Davis Pedersen - Currency Carry Trade Regimes Beyond the Fama Regression]] (Clarida 2009)
- [[2007 - Gorton Hayashi Rouwenhorst - The Fundamentals of Commodity Futures Returns]] (Gorton 2007)
- [[2013 - Lustig Stathopoulos Verdelhan - The Term Structure of Currency Carry Trade Risk Premia]] (Lustig 2013)
- [[2022 - Chernov Dahlquist Lochstoer - Pricing Currency Risks]] (Chernov 2020)
- [[2024 - Fan Jiao Lu et al - The Risk and Return of Cryptocurrency Carry Trade]] (Fan 2024)
- [[2008 - Lustig Roussanov Verdelhan - Common Risk Factors in Currency Markets]] (Lustig 2008)
- [[2016 - Zaremba - Strategies Based on Momentum and Term Structure in Financialized Commodity Markets]] (Zaremba 2016)
