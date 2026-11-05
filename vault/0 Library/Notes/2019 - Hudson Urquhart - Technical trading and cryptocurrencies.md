---
type: reading-note
source: paper
title: Technical trading and cryptocurrencies
authors: Hudson, Urquhart
affiliations: Hull University Business School, University of Hull; ICMA Centre, Henley Business School, University of Reading
year: 2019
venue: Annals of Operations Research 297 (2021), pp. 191-220; published online 30 August 2019
doi: 10.1007/s10479-019-03357-1
pdf: "[[2019 - Hudson Urquhart - Technical trading and cryptocurrencies.pdf]]"
version: published (open access)
tier: 1
read: full
tags: [trend, crypto, daily]
date: 2026-10-24
---

# Technical trading rules in crypto (Hudson, Urquhart 2019)

## Summary

- **Finding**: 14,919 daily technical rules on Bitcoin (two price series), Litecoin, Ripple, Ethereum to end-2017. Every rule family earns a significant average return, gross; 20% to 50% of rules survive multiple-testing corrections (Tables 2, 8).
- **Mechanism**: not tested. Authors argue crypto has no fundamentals, so investors rely on past prices, and crypto prices have trended strongly (p. 2-3).
- **Where it works best**: filter and channel breakout rules; Ethereum filter rules 16.45% annualised, breakeven cost 147.56 bps (Tables 2, 6). Ethereum, Ripple, Litecoin stay positive out of sample.
- **Weak spots**: best in-sample Bitcoin rule loses out of sample (H1 2018). Few rules beat buy-and-hold on raw return (4.96% to 15.69%). Support-resistance breakeven only 7.88 to 16.16 bps.
- **Main caveats**: returns gross; out-of-sample is six months, one rule per coin. Sell signals add nothing. Several unit and arithmetic inconsistencies in the tables.

Page numbers follow the journal pagination (191 to 220). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Crypto has no fundamentals, so traders rely on past prices, raising the role of technical analysis | Argument only | p. 192-193 |
| 2 | Crypto prices have followed strong trends, a prior for trend rules | Fig. 1 price paths | p. 192-193 |
| 3 | Bitcoin, the most liquid and most watched coin, is becoming more efficient; less liquid coins keep opportunities | Bitcoin's best rule loses out of sample; others do not | Table 9; p. 213 |
| 4 | Profits come from buy signals, not sell signals | Average sell returns near zero or negative; 15 of 20 class-coin cells have no significant sell rule | Tables 2, 4; p. 200, 205 |

**Caveats raised by the authors**
- Performance of technical rules tends to decline over time and after publication (p. 212).
- Transaction costs differ by exchange and coin, so only breakeven costs are reported (p. 197, 205-210).

**Ruled out**
- Pure data snooping: a share of rules survives Bonferroni, Holm, BH and BY (Table 8).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Bitcoin (CoinDesk index and Bitstamp exchange), Litecoin, Ripple, Ethereum (CoinMarketCap) | p. 195 |
| Period | CoinDesk from 18 Jul 2010, Bitstamp from 1 Dec 2012, Litecoin 28 Apr 2013, Ripple 4 Aug 2013, Ethereum 7 Aug 2015, all to 31 Dec 2017. Out of sample: Jan to Jun 2018 | p. 195-196, 212-213 |
| Signal | Five families: moving average (7,980 rules), filter (963), support-resistance (945), RSI oscillator (810), channel breakout (4,536) | Appendix |
| Entry | Position S(t-1) in {+1, 0, -1} set from prices up to the close of t-1 | Eq. 2, p. 197 |
| Exit | Rule-specific: opposite signal, or neutral after k = 3 or 5 days for the "k-period" variants | Appendix |
| Horizon | Daily bars; holding from days to the next opposite signal | Appendix |
| Sizing | Full position; MA5 uses one third or all of the "risk budget" | Appendix |
| Portfolio | One coin at a time | p. 197 |
| Rebalancing | Daily | p. 197 |
| Costs | Zero in returns; breakeven cost reported; 50 bps cited as the Bitcoin cost (Lintilhac and Tourin 2017) | p. 197, 205, 210 |
| Data and tools | Simple daily returns, seven days a week; neutral earns no risk-free rate; stationary bootstrap (1,000 draws) p-values; Bonferroni, Holm, BH, BY | p. 196-200, fn 8, fn 12 |

**Rule** (Eq. 2, p. 197): R(j,t) = S(j,t-1) x r(t). Example of the best in-sample rules (Table 9): CB2 25/0.05/0.025/5 for Bitcoin and Litecoin (channel breakout, hold k periods); MA1 2/0.001/1 for Ripple; MA4 2/25/0/1/5 for Ethereum. Codes follow the appendix.

**Data provenance**
- CoinDesk is an average across exchanges meeting CoinDesk criteria, not a tradable price (p. 195, 214).
- Bitstamp is an actual exchange price (p. 195).
- Litecoin, Ripple, Ethereum from CoinMarketCap (p. 195).

## 3. Results

Results are real data. Tables 2 to 8 are in-sample to end-2017 and gross. Table 9 is out of sample (H1 2018).

**Aggregate** (Table 2, average over all parameterisations)
- Annualised return by family, lowest to highest: support-resistance 1.96% (Litecoin) to 4.73% (Ripple); filter 7.97% (Bitstamp) to 16.45% (Ethereum); channel breakout 7.89% to 15.99%.
- Average sell-signal returns: -0.06% to 0.01% a day; buy-signal returns all significant.
- Annualised Sharpe 0.0132 (Litecoin SR) to 0.1633 (Ethereum filter); Calmar up to 16.29 (Ethereum filter) (Table 3).

**By sub-group**
- Share of rules with significant returns (Table 4): filter 92.80% to 99.68%; support-resistance 20.95% (Litecoin) to 62.12% (Bitstamp).
- Best single rule (Table 5): 13.42% (CoinDesk channel breakout) to 22.15% (Ethereum filter). Worst: -3.90% (Ethereum MA).
- Survive multiple testing (Table 8): Bonferroni 20.35% (Ripple) to 33.61% (CoinDesk); BH up to 50.41% (CoinDesk).

**Horizon and parameters**
- Breakeven costs (Table 6): 7.88 bps (Litecoin SR) to 147.56 bps (Ethereum filter). CoinDesk 11.42 to 66.41; Bitstamp 11.89 to 57.51.
- Share of rules with breakeven above 50 bps: 0% to 49.52%; support-resistance at most 3.49%.
- Trades per rule: 68 (Ethereum MA) to 294 (CoinDesk filter) over the sample.

**Over time**
- Out of sample, Jan to Jun 2018 (Table 9): CoinDesk -0.0010, Bitstamp -0.0091 annualised return, negative Sharpe; Litecoin 0.0775 (Sharpe 1.36), Ripple 0.0546 (0.74), Ethereum 0.0631 (1.19).
- No in-sample results by subperiod.

**Link to other strategies**
- Buy-and-hold (Table 7): annualised return 0.0928 (Litecoin) to 0.1875 (Ethereum). Only 4.96% to 15.69% of rules beat it on return; 27.99% to 51.26% on Sortino and 28.58% to 57.64% on Calmar.
- Moving average rules correlate above 0.80 with time-series momentum (Marshall et al., cited) (p. 197).

**Inconsistencies in the source**
- p. 200 says filter and channel breakout reach 16.45% "for Ripple". Table 2 gives 16.45% for Ethereum; Ripple's highest is 12.30%.
- Table 2 reports a daily "Ave Return" of 0.40% next to an annualised 7.72% (CoinDesk MA). 0.40% a day cannot annualise to 7.72% (computed); units of one column are unclear. Same issue between Table 1 daily mean 0.0061 and Table 7 buy-and-hold 0.1167.
- Appendix totals: F2 = 7 x 5 x 2 x 9 is 630, printed 648. Final sum uses 630 for support-resistance, whose total is 945; the parts sum to 15,234 (computed), printed 14,919.
- Appendix: SR "#k = 5" with k in {3, 5}; oscillator "#d = 4" with d in {1,...,5} and computed with 5; channel c set lists 0.5 twice.
- Abstract: "two Bitcoin markets and three other" cryptocurrencies; the paper studies Litecoin, Ripple, Ethereum (three) plus two Bitcoin series, called "five cryptocurrency markets" (p. 211) and "four" coins (p. 193).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Other performance metrics for best and worst rules available on request | fn 13 |
| Less liquid coins attract less attention and so keep more opportunities | p. 213 |
| CoinDesk may offer more inefficiencies than Bitstamp because it is an average | p. 214 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Universe of five rule families with full parameter grids (Hsu et al. 2016) | technique | signal | Balance between too few rules (bias) and too many irrelevant ones (power) | p. 193, Appendix |
| 2 | Channel breakout: trade breaks of a c% channel over j days | technique | signal | Breach of drifting support and resistance means sustained move. Card [[Channel breakout]] | Appendix |
| 3 | Filter rule: buy x% above recent low, sell x% below recent high | technique | signal | Simplest trend rule. Card [[Filter rule]] | Appendix |
| 4 | Breakeven transaction cost per rule | technique | evaluation | Costs differ by exchange and coin. Card [[Break-even transaction cost]] | p. 197, 205 |
| 5 | Stationary bootstrap p-values then Bonferroni, Holm, BH, BY | technique | evaluation | Controls data snooping across 14,919 rules. Card [[Multiple testing adjustment]] | p. 199-200 |
| 6 | Pick the best in-sample rule, test it in a later period | technique | evaluation | Pure out-of-sample check. Card [[Chronological holdout test]] | p. 212-213 |
| 7 | Sortino and Calmar next to Sharpe | technique | evaluation | Downside risk and drawdowns matter for momentum-type strategies | p. 198 |

## 6. Regime observations

- The out-of-sample half-year (H1 2018) is a bear market after the late-2017 peak; Bitcoin's best rule loses there (p. 212-213).
- Rules beat buy-and-hold mostly on downside-risk measures, which authors tie to avoiding long, severe drawdowns (p. 211).

## 7. Acknowledged limits

- Transaction costs not modelled, only breakeven (p. 205-210).
- Choice of in- and out-of-sample periods matters (p. 212).

## 8. Not addressed

- Net returns at a fixed cost.
- Slippage and execution on a real exchange for Litecoin, Ripple, Ethereum (CoinMarketCap prices).
- Short-selling feasibility and funding.
- Out-of-sample of more than one rule, or of a rule-selection procedure.
- Subperiod stability in sample.
