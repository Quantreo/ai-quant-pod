---
type: technique
brick: signal
aliases: [sign of own past return, trend sign, EMA trend signal, price minus moving average, trend following indicator, TS-Mom 1, TS-Mom 12, Moving average crossover, MA crossover, SMA EMA DEMA crossover, Own-return predictive regression, MA(S,L) FX rule, simple trend, average sign of 1, 3 and 12-month returns, n-day momentum rule, Individual currency momentum, SMA(12) momentum, p/SMA13 - 1, 13612W, 13612W momentum, Absolute momentum, Golden cross filter, Absolute momentum, Asset-class trend filter]
sources: 11
tested_on: [multi-asset, fx, crypto, equities]
---

# Time-series momentum signal

> [!summary]
> Goes long an instrument whose own past excess return is positive, short when it is negative.

## How it works

- **Inputs**: the instrument's excess return over a lookback.
- **Formula**: sign of the past k-month excess return.
- **Variant**: price minus an exponential moving average of past prices, divided by an EMA of absolute price changes; the sign gives the position.
- **Variant**: short against long moving average of price; long when the short is above.
- **Variant**: regress the next return on the current one, or sort weekly returns into quintiles of their own history.
- **Variant**: price over the average of the last 13 month-end prices minus 1, negative means bad; or a weighted average of the 1, 3, 6 and 12-month returns, heavier on the short ones.
- **Lookback / holding**: lookback k and holding period h, in months. The position is reset at the end of each holding period.
- **Output**: +1 or -1 per instrument.
- **Variant**: average of the sign of the 1, 3 and 12-month returns, giving a position of -1, -1/3, +1/3 or +1 of notional.
- **Direction**: long and short.
- **Tested on**: futures and forwards in commodities, currencies, equity indexes and government bonds, and spot prices as proxies before futures existed.
- **Variant**: golden cross (short average above long average) used as a long-only eligibility filter on weekly closes.
- **Variant**: trend filter on asset classes, held while the price passes a moving-average or threshold test, else the alternative asset (long-flat).

## What the sources say

### Parameters
- **Moskowitz 2012**
	- Lookback k = 12 months, no month skipped (p. 233, 236).
	- Holding h = 1 month (p. 236).
	- Grid for both: 1, 3, 6, 9, 12, 24, 36, 48 months (Table 2).
	- 58 futures and forwards, results 1985-2009 (p. 230, 236).
- **Lempérière 2014**
	- Signal: last close minus an EMA of past prices, over an EMA of absolute monthly price changes; position is the sign (p. 3, Eq. 1-2).
	- EMA decay n = 5 months; grid 2 to 20 months (p. 3; Table 1).
	- Monthly closes, monthly rebalance (p. 3).
	- 27 contracts in four sectors; futures from 1960, spot proxies from 1800 (p. 4, 8-9).
- **Chernov 2020**
	- TS-Mom 1: sign of last month's return; TS-Mom 12: sign of the last 12 months, weights scaled by inverse conditional volatility (p. 16).
	- As an expected-return input: S(t)/S(t-12), loading from a panel regression (p. 12).
	- Nine G10 currencies vs USD, monthly, 1985-2020 (p. 16-17).
- **Rozario 2020**
	- Short and long windows searched from 1 to 1000 hours (BTCUSD) and 1 to 50 days (S&P 500) (p. 2)
	- SMA, EMA with α = 2/(N+1), DEMA = 2·EMA - EMA(EMA) (p. 3, Eq. 1-2)
	- Windows chosen by best Sharpe each year, used the next year (walk-forward) (p. 3)
	- Bitstamp BTCUSD, hourly, Sept 2011 to Dec 2019 (p. 2)
- **Liu 2018**
	- Next return on current return, 1 to 7 days (daily) and 1 to 4 weeks (weekly) ahead; returns measured from 11:59:59 UTC (p. 20)
	- Quintiles of the weekly return across the whole sample, average return of each quintile over the next 1 to 4 weeks (Table 15)
	- Repeated since 2013 (Table 16) and with quintile cutoffs from the first two years only (Table 17)
	- Bitcoin from 2011, Ripple from 2013, Ethereum from 2015, all to May 2018 (p. 4)
- **Ivanova 2014**
	- Variants: MA(1,5), MA(5,20), MA(1,200) crossovers, and sign of the n-day return, n in {5, 20, 60} (p. 5)
	- 21 USD rates and 19 cross rates, daily, long or short the foreign currency (p. 4-6)
- **Menkhoff 2011**
	- Long a currency if its own last-month return is positive, short if negative; equal-weight portfolio of the individual strategies (p. 20, Table A.3)
	- Benchmark: moving average crossovers (1,20), (5,20), (1,200) days, long when the short average crosses the long one from below, equal-weighted over currencies (p. 19, fn 16)
	- Up to 48 currencies vs USD, monthly for the sign rule, 1976-2010 (p. 9, 20)
- **Keller 2022**
	- SMA(12): p(t)/mean of the last 13 month-end prices - 1; negative when below (p. 3, fn 5)
	- 13612W: 12·RET(1) + 4·RET(3) + 2·RET(6) + 1·RET(12); weight of the 1-month return 40% (p. 4, fn 7)
	- Used as an absolute filter on canary assets and defensive picks, not on offensive picks (p. 4)
	- ETFs, monthly, Dec 1970 to Jun 2022 (p. 3)
- **Unknown 2026**
	- Golden cross: MA50 above MA200 on the Friday close, used as a yes or no eligibility test (C2) (Table 1 A)
	- Same table: price above MA50 (C1), MA50 slope over 10 weeks positive (C3), MA200 slope positive (C4)
	- 3,215 US ETFs, weekly, 2001-2026 (p. 6)
- **Prior-Sanz 2026**
	- Absolute momentum coded for trend rules such as moving-average filters or price above or below a threshold (p. 7).
	- Lookbacks not stated; set by each of 5 published designs (Group 6, about 5 assets each) (Table 1).
	- Monthly, month-end close, 0.2% round trip (p. 6).
- **Hood 2024**
	- Average of the sign of the trailing 1-, 3- and 12-month returns, after Hurst 2013 (p. 6, Exhibit 1A).
	- Position +1, +1/3, -1/3 or -1 of notional, not scaled by volatility (p. 6).
	- 1-day lag; 2 bp cost per unit traded (p. 4, 6).
	- Used as a control for a volatility-managed strategy; alternatives tested are the single 1, 3, 6, 9, 12-month signs and a CTA-style weighted mix (Appendix C).
	- US market factor 1927-2023; 50 futures 2000-2023 (p. 4, 12).

### Why
- **Moskowitz 2012**
	- Convention of the literature (p. 236).
	- Fig. 1 and Table 2 support 12 months (p. 236).
- **Lempérière 2014**
	- Built to mimic a constant-risk strategy without costs (p. 3).
	- Monthly data, because long histories exist only at that frequency (p. 3).
	- n = 5: not argued.
- **Liu 2018**: after Moskowitz 2012; the authors give no mechanism (p. 4, 20)
- **Rozario 2020**: windows chosen by Sharpe; walk-forward done "without great care" for robustness (p. 3)
- **Chernov 2020**: not argued beyond prior work; trend motivated by the literature on moving-average rules in FX (p. 12, 16).
- **Ivanova 2014**: among the most studied FX rules; not argued beyond prior work (p. 4)
- **Menkhoff 2011**: both rules are benchmarks from the earlier FX technical trading literature, not argued further (p. 18-20)
- **Keller 2022**: not argued beyond the earlier PAA, VAA and DAA papers; fast filter for protection, slow for selection (p. 2, 4)
- **Unknown 2026**: golden cross plus 52-week breakout is the canonical combination of the technical literature, in common use in the industry (p. 15)
- **Prior-Sanz 2026**: trend filter on a small set of asset classes, with the alternative asset not stated (p. 7); reason cited: a 10-month moving average on broad asset classes improved risk-adjusted performance and drawdowns against 60/40 (Faber 2007) (p. 3)
- **Hood 2024**: a control chosen for ease of replication, not argued as the best rule (p. 6, fn 6).

### Evidence
- **Moskowitz 2012**: real data, in-sample, gross of costs.
	- Positive profit in 58 of 58 contracts, 52 significant at 5% (p. 236).
	- Best cell 12 / 1, alpha t = 6.61 (Table 2A).
	- Alpha against MSCI World, SMB, HML, UMD: 1.58% a month, t = 7.99 (Table 3A).
	- 1966-1985 Sharpe ratio 1.1, called out-of-sample by the authors (p. 237-238).
- **Lempérière 2014**: real data, in-sample, gross of costs and financing.
	- Futures since 1960, n = 5: Sharpe 0.78, t = 5.7, de-biased t = 5.0 (Table 1).
	- Sharpe 0.76 to 0.83 for n from 2 to 10 months, 0.57 at 20 (Table 1).
	- Since 1800: Sharpe 0.72, t = 10.5, de-biased 9.8 (Fig. 4).
	- Positive in every sector (t ≥ 2.9) and every 50-year period (Tables 8-9).
- **Chernov 2020**: real data, in-sample, gross, G10 1985-2020
	- Sharpe TS-Mom 1 0.440, TS-Mom 12 0.473 (Table 2B); Fig. 1 shows the two bars swapped.
	- Optimal timing alpha 2.66 (t 2.92) and 2.18 (t 2.06) (Table 4A).
	- Adding momentum to carry leaves the mean-variance Sharpe at 0.871 (Table 1D).
- **Rozario 2020**: real data, BTCUSD 2011-2019, gross (no fees, spread or slippage)
	- Best full-period Sharpe: SMA 1.09 (141 / 781 hours), EMA 1.35 (721 / 951), DEMA 1.32 (791 / 981) (Table 1)
	- Walk-forward SMA: 73700% in total, stated as 255% a year (p. 4)
	- Walk-forward yearly Sharpe: ≈ -0.8 for SMA in 2017-18, ≈ 1.6 in 2012-13 (≈ Fig. 3a)
- **Liu 2018**: real data, in-sample, gross, Bitcoin 2011-2018
	- Weekly coefficients 0.19, 0.22, 0.21, 0.09 at 1 to 4 weeks (Table 14)
	- Top quintile 11.22% next week, Sharpe 0.45; bottom quintile 2.60%, Sharpe 0.19 (Table 15)
	- Cutoffs from the first two years: top minus bottom 4.53 at one week (Table 17)
- **Ivanova 2014**: real data, inside a dynamic rule selection
	- Momentum and MA rules gain share in the top portfolio after 1985 (p. 11, Fig. 2)
	- RUB MA(1,5): Sharpe 0.93, mean 7.15% a year, 2000-2012 (Table 2)
	- Monthly returns of cross-sectional momentum rules correlate with the portfolios at a median 0.13 (fn 3)
- **Menkhoff 2011**: real data, in-sample, gross
	- Moving average rules: 5.27%, 5.14%, 5.23% a year, Sharpe 0.88, 0.83, 0.77 (Table 3A)
	- Sign of last month: average Sharpe over currencies 0.45; equal-weight portfolio 4.86%, Sharpe 0.76 (Table A.3)
	- Cross-sectional momentum earns 9.46% (Sharpe 0.95) on the same data (Table A.3)
- **Keller 2022**: real data, in-sample, 0.1% one-way cost listed, ETFs Dec 1970 to Jun 2022
	- SMA10 on SPY switching to IEF: R 11.8%, D 23.3%, Sharpe 0.59 (fn 11, p. 9)
	- Filter grid on K/FS: 13612W protective with SMA(12) selection 11.6% (G12); RET(12) selection 5.0% to 6.7% (Fig 13)
	- G4: protective SMA(9), SMA(12) or RET(12) give K 0.0% in all 18 cells (Fig 14)
- **Unknown 2026**: real data, in-sample, net of 20 bp per side, no SL or TP
	- C1, C2, C3, C4 and C6 alone give identical Sharpe 0.881, drawdown -13.81%, CVaR95 2.80% (Table 2 A)
	- They select the same ETFs in 99% of weeks (p. 14)
	- C2 and C6: Sharpe 0.881 against SPY, difference +0.408 (p = 0.01) (Table 2 C)
- **Prior-Sanz 2026**: real data, vendor-run rules, 1995-April 2025, net of 0.2% round trip
	- Absolute-only group (5 strategies): vol 7.49%, MaxDD -10.2%, Sharpe 0.76, return over MaxDD 0.87, against 8.58%, -23.6%, 0.61 for static allocations (p. 26).
	- Mean return ≈8.03% against 7.41% for static (p. 26-27).
	- Absolute dummy in the 30-year Sharpe regression: +0.06 (0.06), not significant; 2020-23 +0.23*** (Tables 4, 10).
- **Hood 2024**: real data, in-sample, net of 2 bp, US market factor 1927-2023
	- Return 4.9%, volatility 13.2%, Sharpe 0.37, against 0.44 for buy-and-hold (Exhibit 1B).
	- Sharpe 0.40 at 0 bp, 0.24 at 10 bp per unit traded (Exhibit A.1).
	- Used as a regressor, it takes 59% of the alpha of the volatility-managed market factor; single-month signs take 21% to 49% (Exhibit C.1).

### Limits
- **Moskowitz 2012**
	- The 12 / 1 rule was chosen on the same sample as the results (p. 236).
	- Alpha over always-long is significant for 26% of contracts (p. 236).
	- 24 / 36 gives t = -0.09 (Table 2A). Currencies are negative at a 48-month lookback (Table 2E).
	- No costs.
- **Lempérière 2014**
	- No costs, no interest; P&L in price changes over volatility, not returns (p. 3, fn 5).
	- Fig. 1 gives t = 5.9 for the same n = 5 run (p. 5).
	- Bonds since 1982: de-biased t = 1.6 (Table 2).
	- Flat since 2011 (≈ Fig. 6); a 3-day trend faded from ≈2003 (Fig. 8).
- **Chernov 2020**
	- No alpha on the authors' mean-variance factor; R² 0.034 and 0.088 (Table 2B).
	- No transaction costs (whole paper).
- **Rozario 2020**
	- 73700% does not compound to 255% a year over 7 to 8 years (computed) (p. 4)
	- No costs; best Sharpe values are in-sample (p. 2, Table 1)
	- Long-flat or long-short not stated (p. 2)
- **Liu 2018**
	- Bootstrapped t-statistic at one day is 1.22, against 2.96 with regular errors (Table 14)
	- Ethereum is weaker, with a negative coefficient at 5 days (Table 18)
	- No trading rule, no costs (whole paper)
- **Ivanova 2014**
	- No result for these rules alone (p. 11)
	- Net or gross not stated
- **Keller 2022**
	- Best filter pair is in-sample optimal on the authors' K ratio (notes 6, 12)
	- No significance test (whole paper)
- **Menkhoff 2011**
	- Costs of the moving average rules not stated (Table 3)
	- Worst currencies: Finland -7.53% a year, Cyprus -0.57% (Table A.3)
- **Unknown 2026**
	- Used as a long-only filter on a momentum ranking, not as a stand-alone signal; no test of the filter against no filter alone (p. 15)
	- The five trend filters are redundant, so the choice between them says nothing (p. 14-15)
- **Prior-Sanz 2026**
	- Five strategies, no rule or per-strategy result; no significance test for this group (Table 13 omits it).
	- Absolute momentum widens the Sharpe spread without lifting the median (p. 12).
	- 2008-09 absolute strategies had negative median Sharpe (p. 21).
- **Hood 2024**
	- One simple rule on single assets; the authors say a diversified trend fund is the better way to hold trend (p. 16).
	- No result on the rule's own significance in the broad sample (whole paper).
	- Rebalancing frequency not stated (Exhibit 1B notes).

## Sources

- [[2012 - Moskowitz Ooi Pedersen - Time Series Momentum]] (Moskowitz 2012)
- [[2014 - Lempérière Deremble Seager et al - Two centuries of trend following]] (Lempérière 2014)
- [[2022 - Chernov Dahlquist Lochstoer - Pricing Currency Risks]] (Chernov 2020)
- [[2020 - Rozario Holt West et al - A Decade of Evidence of Trend Following Investing in Cryptocurrencies]] (Rozario 2020)
- [[2020 - Liu Tsyvinski - Risks and Returns of Cryptocurrency]] (Liu 2018)
- [[2014 - Ivanova Neely Weller et al - Can risk explain the profitability of technical trading in currency markets]] (Ivanova 2014)
- [[2011 - Menkhoff Sarno Schmeling Schrimpf - Currency Momentum Strategies]] (Menkhoff 2011)
- [[2022 - Keller - Relative and Absolute Momentum in Times of Rising Low Yields Bold Asset Allocation (BAA)]] (Keller 2022)
- [[2026 - Unknown authors - Momentum Strategies in ETFs under Simple Operational Rules]] (Unknown 2026)
- [[2026 - Prior-Sanz Vizuete-Luciano Cruz-Zayash et al - The long-term efficiency of tactical asset allocation Evidence from 86 systematic strategies (1995-2025)]] (Prior-Sanz 2026)
- [[2024 - Hood Raughtigan - Volatility Targeting Is Trendy How Trend Following Explains Alpha in Volatility-Managed Strategies]] (Hood 2024)
