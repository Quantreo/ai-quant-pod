# Example: Crypto Thin Losers (text.md behind "Crypto Thin Losers - Report.pdf")

The bar to meet: every number from numbers.md, the worst news in bold in the abstract, short paragraphs that read the tables and figures.

## abstract
Crypto Thin Losers buys the least liquid coins among recent losers on Binance USDT perpetuals and sells the most liquid ones, with a BTC hedge. Over January 2021 to September 2026 it earns a net Sharpe ratio of 0.92 (90% bootstrap range 0.25 to 1.52), with no exposure to BTC. On the sealed test, January 2025 to September 2026, the net Sharpe falls to 0.38 (range -0.88 to 1.51). **Three findings weigh against it: in the test the profit came from the short leg, not from the recovery the hypothesis predicts; the gains sit in very few days and names; and the book was under water for 884 days.** It stays in the library on paper only.

## hypothesis
When a thin coin falls, its sellers meet few buyers and push the price below value; whoever absorbs the flow is paid by the recovery. The pattern comes from Begušić and Kostanjčar (2019), measured in-sample on spot coins from 2015 to 2019, before costs.

## method
The universe is the Binance USDT perpetuals listed for at least 180 days, point in time, with delisted names kept to their last price. Each week the losers are sorted on illiquidity; the book is long the thin losers, short the liquid losers, and hedged on BTC. Costs are charged by tier (20 bp on the thin leg, 5 bp on the liquid leg and the hedge), with funding and liquidations. The train runs from 2021 to 2023, the validation over 2024, and the test from January 2025; the test was opened once, on 24 October 2026.

## performance
The full sample includes the train, on which the strategy was designed; the test is the honest estimate. Over the test the strategy returned 9.0% a year for 23.8% volatility, and on 21 months a Sharpe ratio of 0.38 can be told apart neither from zero nor from the 0.92 of the full sample. The strategy made 38%, 37% and 32% in 2021, 2022 and 2023, then about 8% a year. The maximum drawdown, -38.4%, runs from April 2024 to April 2025, and the peak was only recovered in September 2026.

## exposure
The strategy is not a bet on the crypto market: its beta to BTC is 0.02 over the full sample and -0.02 over the test, and its correlation to BTC stays under 0.05 in absolute value. The alpha over BTC is significant on the full sample (21.9% a year, t 2.16), carried by the train, and not on the test (9.1%, t 0.47).

## sources
The hypothesis says the long leg earns the money. It did on the train: the thin losers made 228% of capital in price while the short leg lost 89%. In the test the legs swapped: the long leg lost 45% and the short leg, liquid losers that kept falling, made 97%. Funding cost 17% over the test against 4% over the three years of train. The payer named in the hypothesis did not pay.

## concentration
The best 21 days of the full sample, 1% of the days, make 97% of its net P&L: without them the Sharpe ratio falls from 0.92 to 0.04. In the test, the best 7 days make more than twice the net P&L, and the best five names more than all of it. The same cut on BTC takes its Sharpe from 0.61 to -0.11: thick right tails are the nature of the market, but the result rests on rare events. The big days are regular, though: each month its two best days carry it, and the slowdown after 2023 came from the other days losing twice as much, not from fewer big days.

## implementation
The book holds about 30 names on each side in the train and about 95 in the test, at a gross exposure of 1.5 to 1.8, and keeps a position about four weeks. Costs take 10 to 12% of capital a year. The break-even cost fell from 57 bp in the train to 20 bp in the validation and 23 bp in the test, against the 20 bp assumed on the thin leg.

## robustness
The result holds a one-day delay and the choice of price, but not higher costs: with costs doubled or trades three days late, the validation Sharpe turns negative. Several sorting choices tried in the validation (independent sort, shorter beta window, equal-weight hedge, thinner cut) also turn it negative. The edge is thin compared with what it costs to trade.

## luck
Three versions of this strategy were run, and seven reversal strategies on crypto in all. On three years of train, the best of 5.3 independent tries with no skill would reach a Sharpe ratio of 0.71. The train net Sharpe of 1.38 clears that line by 0.67, and the probability that its true value exceeds it is 91%. The line applies to the train, where the choices were made.

## risks
The test book is not the train book: the universe tripled, and the strategy held about 95 names long on average against 34. The test run charged a flat 12.5 bp instead of the tiers. The daily returns of the train are very skewed (skewness 5.4), so the full-sample figures depend on a handful of days in 2021.

## decision
Kept in the library, on paper only. The full-sample t of 2.19 is carried by the train, and the test does not show the mechanism at work. To revisit after twelve months of paper trading: if the long leg keeps losing, the hypothesis is dead and what remains is a short on liquid losers, to be judged as such.
