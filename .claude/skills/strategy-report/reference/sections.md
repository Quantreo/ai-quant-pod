# What each section says

Every section is three to six sentences, numbers from numbers.md. The script builds the tables and figures; the text tells the reader what to take from them.

## abstract
Four to six sentences: what the strategy trades and how (one sentence); the full-sample net Sharpe with its 90% range; the test net Sharpe with its range, or "the test is still sealed"; then one sentence in bold with the findings that weigh most against it (two or three at most); then its status in a few words.

## hypothesis
Who pays and why, from 1.1 of Pass 1. Then the source: who showed it, on what market and years, and how (in-sample, before costs, gross). Mark a payer the authors did not name as the desk's hypothesis.

## method
Universe (point in time, delisted names), signal and book (long, short, hedge, rebalancing), costs (the tiers, funding for perpetuals, financing for leverage or shorts), periods (train, validation, test, and the date the test was opened). No result here.

## performance
The test is the honest estimate; the full sample includes the train, on which the strategy was designed. Give the test return and volatility, what the bootstrap range says about the Sharpe, the returns by year when they change regime, and the maximum drawdown with its dates and the time under water.

## exposure
Beta, correlation and alpha to the benchmark (BTC for crypto, SPY for ETFs and equities), full sample and test. Say plainly whether the strategy is a bet on the market. When the strategy is long the market by design (a volatility-managed or trend book on equities), the beta is the point: the question is whether the alpha over the benchmark is shown, and on which period.

## sources
Compare the P&L by source with what the hypothesis says should pay, period by period.
- Long and short legs (numbers.md says "long and short legs"): which leg earned the money, and did that change in the test?
- One price leg (a directional book): how much is price, and how much is financing or costs.
- Funding (crypto perpetuals) or financing at the T-bill rate (ETFs and other funded assets): its size against the price P&L. On ETFs the P&L is in excess of cash: a long position pays the T-bill rate, a short one earns it, and a spread is added above 1x leverage when the strategy has one. The fee to borrow a short ETF is in the costs, not in the financing line. Read the strategy file's header to say which applies.
End with one sentence: did the payer named in the hypothesis pay?

## concentration
The share of net P&L from the best 1% of days and the Sharpe without them, full sample and test; the same cut on the benchmark, so the reader sees what is the market's nature and what is the strategy's. Then the regularity line: do the big days come every month, and did the slowdown, if any, come from fewer big days or from the other days losing more? Names: only when the table exists (a single-asset strategy has none); say how much the best five names carry.

## implementation
Names held, gross exposure, holding period, turnover, cost drag, and the break-even cost against the cost assumed in Pass 1. A break-even close to the assumed cost is the most important line of this section.

## robustness
The table lists every run saved before the test: variants, diagnostics, controls and stress tests, under the names the desk gave them. Comment only what matters: costs doubled, delayed trades, price choice, and the variants that flip the sign. Say whether the result survives higher costs.

## luck
Tries for this strategy and for its family and asset, the luck line, the train net Sharpe minus the line, the probability that the true train Sharpe exceeds the line. Say that the line applies to the train, where the choices were made.

## risks
What the backtest does not show: a regime that changed, a universe that changed between periods, a cost model that differs between runs, data issues named in the Data check, capacity, a skew that makes the result rest on a few days.

## decision
The status from the index and Test.md, in one sentence, with its reason. The money rule of the desk (vault/Toolbox/Kill Policy.md): money needs a full-sample t of 2 or more and a test that does not contradict; otherwise paper only. Then the condition to revisit it (what would change the decision, after how long).
