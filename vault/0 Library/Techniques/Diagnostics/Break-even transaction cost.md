---
type: diagnostic
kind: performance
aliases: [break-even cost rate, cost scalability test, implied trading cost to zero alpha, cost sensitivity grid, BETC, BETC 5%]
sources: 6
---

# Break-even transaction cost

> [!summary]
> At what proportional cost rate does the strategy stop beating its benchmark?

## How it works

- **How**: re-run the backtest charging a cost rate γ times half the sum of absolute weight changes at each rebalance. Raise γ until the final wealth equals the benchmark's. Variant: charge a cost per unit of absolute weight change and find the rate that sets the alpha on the benchmark to zero. Variant: report the metric at a few fixed cost levels instead of solving for the break-even.
- **Reading**: the higher the break-even rate, the more cost the strategy can bear. Compare it with the cost rate of the real market.
- **Data needed**: daily weights, price relatives, benchmark wealth.
- **Variant**: cost at which the net return stops being significant.

## What the sources say

### Parameters
- **Li 2012**
	- γ from 0 to 1% (p. 248)
	- Benchmarks: market (uniform buy and hold) and best constant rebalanced portfolio (p. 248-249)
- **Moreira 2016**
	- Cost per unit of absolute monthly weight change: 1, 10 and 14 bp (Table 4).
	- Benchmark: buy-and-hold market; break-even is the cost that sets the alpha to zero (Table 4, p. 11).
- **Begušić 2019**
	- Cost levels 0, 10, 50, 100 bps; benchmark cap-weighted portfolio of the eligible coins (Table 2, p. 3)
- **Hudson 2019**: cost per trade that sets the mean return to zero, per rule, in bps (p. 205, Table 6)
- **Fieberg 2025**
	- Turnover following Gu et al. (2020); 30 bps long, 40 bps short, plus +10 and +20 bps (p. 3146-3147)
	- BETC to zero and BETC to 5% significance (p. 3147)
- **Menkhoff 2011**
	- Net return with bid and ask on the forward and spot legs; a currency kept in the portfolio skips the spot leg cost (p. 11-12)
	- Fixed cost levels: 100%, 75% and 50% of the quoted spread (Tables 8, 9)
	- No break-even solved

### Why
- **Li 2012**
	- Shows whether the strategy is usable once costs are charged (p. 249)
- **Moreira 2016**: shows the strategy survives realistic costs, including higher costs in high-volatility episodes (p. 11).
- **Begušić 2019**: shows the long-only strategies stay profitable with costs (p. 5-6)
- **Hudson 2019**: costs differ by exchange and coin (p. 197, 205)
- **Fieberg 2025**: high-turnover signals may not survive costs, following Novy-Marx and Velikov (p. 3146)
- **Menkhoff 2011**: quoted spreads are known to exceed effective spreads, so results are shown at several fractions of the spread (p. 12, 28)

### Evidence
- **Li 2012**: real data, in-sample backtests, long only.
	- Break-even against the market: 0.7%, 0.4%, 0.1%, 0.3%, 0% (five values for six datasets, Fig. 8 caption, p. 248)
	- At γ = 0.2%, beats the best constant rebalanced portfolio on four datasets (p. 249)
	- Underperforms Anticor at high costs, beats it at low or medium costs (p. 249)
- **Moreira 2016**: real data, in-sample, US market 1926-2015
	- Inverse variance rule: mean weight change 0.73, alpha 4.86% gross, 3.63% at 14 bp, break-even 56 bp (Table 4).
	- Inverse vol 84 bp; forecast variance 74 bp (Table 4).
	- Weight capped at 1 or 1.5: mean weight change 0.16, break-even 110 bp and 161 bp (Table 4).
- **Begušić 2019**: real data, in-sample, crypto 2015-2019
	- Illiquid losers: IR 2.49 at 0 bps, 2.16 at 100 bps (Table 2)
	- Liquid winners: IR 1.59 at 0 bps, 1.27 at 100 bps (Table 2)
- **Hudson 2019**: real data, in-sample
	- Mean break-even 7.88 bps (Litecoin support-resistance) to 147.56 bps (Ethereum filter) (Table 6)
	- 0% to 49.52% of rules above 50 bps (Table 6)
- **Fieberg 2025**: real data
	- Net 2.35% to 2.90% a week; BETC 1.41%, 0.88% at 5% significance (Table 9)
- **Menkhoff 2011**: real data, in-sample, currencies 1976-2010
	- f = 1, h = 1: 9.46% gross, 6.64% at 50% of the spread, 5.28% at 75%, 3.92% at 100% (Tables 1, 8, 9)
	- f = 12, h = 12: 1.89% gross, -2.44% at 100% (Tables 1, 8)
	- Since 1992, f = 1, h = 1: 11.69% gross, 7.27% at 100% (Table A.11)

### Limits
- **Li 2012**
	- Costs are charged after the weights are chosen, not inside the update (p. 253-254)
	- Bid-ask spread and market impact are assumed away (p. 251)
- **Moreira 2016**
	- Market only; no cost measure for the other factors or FX carry (p. 11-12).
	- Gross alphas of two variants are swapped between Table 4 and Table 5A (reading note).
- **Begušić 2019**
	- How the cost is charged is not stated; zero market impact assumed (p. 5)
	- Bid-ask costs in illiquid coins may be much higher than the grid (p. 5)
- **Hudson 2019**: break-even only, no net returns at a fixed cost (p. 205)
- **Fieberg 2025**: assumed cost rates may be low for small coins (p. 3146)
- **Menkhoff 2011**
	- Spreads are indicative quotes from BBI and Reuters (p. 12)
	- Market impact not addressed

## Sources

- [[2012 - Li Zhao Hoi et al - PAMR Passive aggressive mean reversion strategy for portfolio selection]] (Li 2012)
- [[2016 - Moreira Muir - Volatility Managed Portfolios]] (Moreira 2016)
- [[2019 - Begušić Kostanjčar - Momentum and liquidity in cryptocurrencies]] (Begušić 2019)
- [[2019 - Hudson Urquhart - Technical trading and cryptocurrencies]] (Hudson 2019)
- [[2025 - Fieberg Liedtke Poddig et al - A Trend Factor for the Cross Section of Cryptocurrency Returns]] (Fieberg 2025)
- [[2011 - Menkhoff Sarno Schmeling Schrimpf - Currency Momentum Strategies]] (Menkhoff 2011)
