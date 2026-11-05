---
type: reading-note
source: paper
title: The Risk and Return of Cryptocurrency Carry Trade
authors: Fan, Jiao, Lu, Tong
affiliations: Lang School of Business and Economics, University of Guelph; Dhillon School of Business, University of Lethbridge; Asper School of Business, University of Manitoba
year: 2024
venue: Working paper (SSRN 4666425)
doi: 10.2139/ssrn.4666425
pdf: "[[2024 - Fan Jiao Lu et al - The Risk and Return of Cryptocurrency Carry Trade.pdf]]"
version: working paper, version of 20 November 2024
tier: 1
read: full
tags: [carry, crypto, weekly]
date: 2026-10-24
---

# Crypto carry from lending rates (Fan, Jiao, Lu, Tong 2024)

## Summary

- **Finding**: on 44 coins, Oct 2016 to Nov 2021, long the top third by Bitfinex lending rate, short the bottom third, weekly, equal weight: 43.4% a year, vol 58.9%, Sharpe 0.74, before trading costs (Table 4).
- **Mechanism**: authors attribute part of the premium to equity volatility risk: high-rate coins fall more when VIX and S&P realized volatility rise; proposed channel is forced deleveraging across assets (p. 22-25). Not tested.
- **Where it works best**: price appreciation of high-rate coins drives it: 24.0% of the 43.4% comes from price, 19.4% from the rate differential (Table 4). Carry predicts returns with β ≈ 1.7 (Table 2).
- **Weak spots**: HmL mean is significant only at 10% (43.4, s.e. 24.0). Cong et al. five factors leave no significant alpha (Table 5B). VIX beta loses significance with all C5 controls (p. 26).
- **Main caveats**: no trading costs beyond the 15% lending fee; 268 weeks; Bitfinex-only rates; shorting through borrowing on Bitfinex assumed. Stablecoin carry (USDT 9.28%, Sharpe 3.54) had no depeg in sample.

Page numbers follow the printed pagination of the working paper (1 to 50). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Crypto carry is partly compensation for equity volatility risk | ΔVIX betas fall from Low to High; HmL ΔVIX beta -1.861 (alone), -2.306 with C3 | Table 6; p. 22-23 |
| 2 | The VIX link runs through realized equity volatility, not the variance risk premium | HmL ΔRVOL beta -2.246 to -2.375, VRP not robust | Table 7; p. 24 |
| 3 | Possible channel: institutions with leverage targets unwind both equity and crypto carry positions when equity volatility rises (Capponi and Larsson 2015) | Argument only; testing "falls outside the scope" | p. 4, 25 |
| 4 | UIP fails in crypto: high-rate coins appreciate rather than depreciate | Price component rises from Low (50.7) to High (74.7); β > 1 | Tables 2, 4; p. 13 |
| 5 | Stablecoin-USD carry may compensate depeg risk | DAI has higher tracking error (0.008) and higher carry than USDT (0.001) after July 2020; "anecdotal" | Table 9; p. 28 |

**Caveats raised by the authors**
- Depeg risk is not represented in the sample, so stablecoin carry risk-return may mislead (p. 28).
- Blockchain protocols and wash trading may also matter; not studied (p. 29).

**Ruled out**
- Crypto three factors (Liu, Tsyvinski, Wu): HmL alpha 0.9% a week, R² 0.045 (Table 5A).
- Crypto volatility, downside risk, Amihud illiquidity: HmL loadings insignificant (Table 5C, D, F).
- Platform collapse: HmL CARs insignificant around six collapse events (Table 5E).
- Fiat carry factor: HmL loading 0.428 (s.e. 0.451) (Table 5G).
- Geopolitical risk (fn 2; Table 8).
- Age, size, volume of coins as drivers (Table 4, p. 15).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 46 coins with Bitfinex lending rates (44 excluding DAI and USDT) | p. 6, 11 |
| Period | October 2016 to November 2021 (data before Oct 2016 "unreliable"); 268 weeks | p. 6-7, Table 4 |
| Signal | Carry = coin lending rate minus USD rate (FRED monthly) | Eq. 1, p. 7 |
| Entry | End of each week (last working day), rank by interest rate into three equal groups | p. 11, fn 11 |
| Exit | Hold one week | p. 11 |
| Horizon | Weekly | p. 11 |
| Sizing | Equal weight within each group | p. 11 |
| Portfolio | Long High, short Low (short = borrow the coin on Bitfinex, sell, deposit USD) | p. 11, fn 22 |
| Rebalancing | Weekly | p. 11 |
| Costs | Not included in Table 4; Table A1 applies lender rate = 0.85 x borrower rate (Bitfinex 15% fee) | p. 7, fn 7, Table A1 |
| Data and tools | Bitfinex hourly rates, outliers above 99th pct replaced by prior value, volume-weighted daily, then x7 or x30; CoinMarketCap prices, winsorised, first launch week dropped; Newey-West with 4 lags | p. 7-8 |

**Rule** (Eq. 2, p. 7): r(t+1) = carry(t) + s(t+1) - s(t), s = log USD price. Weekly, long equal-weighted top third of coins by lending rate, short bottom third.

**Data provenance**
- Bitfinex is a peer-to-peer lending book; loans last 2 to 120 days; lenders pay 15% of interest (18% with hidden orders) (Appendix A).
- Lending rates differ from staking rewards (Appendix A).
- Fiat carry factor uses one-month forwards scaled to one week (fn 17).

## 3. Results

All results are real data, in-sample, gross of trading costs.

**Aggregate** (Table 4, annualised)
- Low 50.4%, Mid 56.1%, High 93.9%; HmL 43.4% (s.e. 24.0), vol 58.9%, skew 1.95, kurtosis 21.1, Sharpe 0.74.
- Equal-weight all coins: 63.1%, vol 90.1%, skew -0.09, Sharpe 0.70.
- HmL rate component 19.4%, price component 24.0%.
- Panel regression (Table 2): β = 1.66 (weekly) and 1.69 (monthly) with both fixed effects.
- With the 15% lending fee: HmL 43.3%, Sharpe 0.74 (Table A1).

**By sub-group**
- Most frequent in High: Bitcoin Gold (134 of 203 weeks), Bitcoin (124 of 266), Neo, ETC, ETH. In Low: IOTA (175 of 229), Santiment, LEO (always Low), Zcash, EOS (Table 3).
- Market betas: Low 0.831, High 0.800, HmL -0.031 (Table 5A).
- Five-factor model: HmL loads on value 0.096 and network 0.168; alpha 0.003 (n.s.) (Table 5B).

**Horizon and parameters**
- Monthly and weekly predictive regressions give similar β (Table 2).
- Only terciles tested; no variation of rebalancing or weighting shown.

**Over time** (≈ Fig. 1, carry scaled to EW volatility)
- Carry rises to ≈ 10 (cumulative, real numbers) by mid-2017, falls to ≈ 3 during 2018, reaches ≈ 11 by 2020, peaks ≈ 35 in late 2021, ends ≈ 30.
- EW peaks ≈ 39 in January 2018, drops to ≈ 3 by 2019.
- Authors describe the carry path as a "steady upward trend, albeit with a few slight dips around 2018 and the start of 2021" (p. 14).

**Link to other strategies**
- Stablecoin-USD carry (Table 9): USDT 9.28% a year, vol 2.62%, Sharpe 3.54 (since Dec 2018); 9.98% and Sharpe 6.62 since July 2020. DAI 10.92%, Sharpe 1.54.
- Fiat carry in Koijen et al. (2018): 5.29% return, 7.80% vol, cited (p. 12-13).

**Inconsistencies in the source**
- Table 1, Panel A: Bitcoin rate SD 0.50% with 25th and 75th percentiles 2.05% and 9.47%. A distribution with that interquartile range cannot have that SD (computed); same pattern for other coins.
- p. 23 calls the HmL VIX beta "significantly negative" in both settings; Table 6 marks it at 10% only (-1.861*, -2.306*, -1.674*).
- p. 29 attributes the equity volatility risk factor to Lustig, Roussanov and Verdelhan (2011); the factor used is ΔVIX from CBOE (Section 5.3).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Bitfinex is the largest exchange offering BTC interest rates via an order book (cited) | fn 6 |
| Stablecoin carry compensates depeg risk ("anecdotal evidence") | p. 28 |
| Carry withstood the 2018 and 2021 crashes | p. 2, 14 |
| Institutional deleveraging links equity volatility to crypto carry | p. 25 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Coin lending rate minus USD rate as carry signal | technique | signal | Realistic platform rates instead of illiquid derivatives. Card [[Carry signal]] | p. 5, 7 |
| 2 | Tercile sort, equal weight, weekly | technique | portfolio | Few loanable coins; avoid dominance of majors. Card [[Carry signal]] | p. 1, 11 |
| 3 | Split excess return into rate differential and price change | technique | evaluation | Shows where carry profit comes from. Card [[Spot and roll return decomposition]] | Table 4 |
| 4 | Predictive panel regression of returns on carry (β = 0, 1, >1 reading) | technique | evaluation | Koijen et al. (2018) framework | p. 9-10 |
| 5 | Event study of carry portfolios around exchange collapses | technique | risk | Proxy for platform risk without options | p. 19-20 |
| 6 | VIX split into realized volatility and variance risk premium | technique | evaluation | Bekaert and Hoerova (2014) | p. 23-24 |
| 7 | Stablecoin-USD time-series carry with a no-trade band between deposit and borrow rates | technique | entry | Earn spread without price exposure. Card [[Carry signal]], [[No-trade band]] | p. 27 |

## 6. Regime observations

- High-rate coins lose more when equity volatility rises (Tables 6-7).
- Carry drawdown during 2018 while EW collapsed more (≈ Fig. 1).
- All portfolios have negative CARs around platform collapses; Mid significant at (-1, +1) (Table 5E).

## 7. Acknowledged limits

- Mechanism for the equity-volatility link not tested (p. 25).
- No depeg in the stablecoin sample (p. 28).

## 8. Not addressed

- Spot trading costs, slippage, borrow availability limits on Bitfinex.
- Counterparty risk of Bitfinex itself.
- Value-weighted portfolios.
- Out-of-sample period after November 2021.
- Drawdown statistics.
