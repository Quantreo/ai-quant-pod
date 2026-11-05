# Triage: which techniques earn a card

The reading note keeps every technique. The library keeps only what the desk will reuse to build or judge a strategy. A library full of minor tricks hides the useful ones.

## Four questions

1. **Does it change a trading decision** (what, when, how much, until when), **or does it judge a strategy?** Neither (data plumbing, a calculation trick): no card.
2. **Does it work outside the paper?** A step that only makes sense inside the authors' model is not a brick.
3. **Does it add a free parameter with no economic reason?** A setting picked by looking at results is calibration, not a technique: no card.
4. **Is it specified enough to code?** A suggestion with no rule and no parameters stays in the reading note, under claims without evidence.

The kind and brick written in the reading note are the reader's hints, not decisions: judge each technique yourself.

A technique that passes goes to a brick folder. A method that judges a strategy is a diagnostic: `performance` (does it beat the right benchmark) or `attribution` (where the return comes from, what it is exposed to).

## Bricks and folders

Signal, Entry, Exit, Risk, Sizing, Rebalancing, Universe, Diagnostics.
- Risk: risk per trade, stops, leverage limits.
- Exit: profit targets, time exits, signal exits.

## Decisions taken with the user (reuse their reasons)

**Card**
| Technique | Brick | Reason |
| --- | --- | --- |
| Sign of own past 12-month return | Signal | Simple, reusable signal |
| Constant ex-ante volatility per position, EWMA estimator, equal risk across instruments | Sizing | Usable in almost any strategy. One card: estimator and aggregation are parameters |
| Direction of the first 5-minute candle, stop at its opposite extreme | Signal | One setup: the stop defines R for this signal, same card |
| Target in multiples of R, else exit at the close | Exit | Reusable exit rule |
| Risk 1% of the account per trade | Risk | Risk management, not sizing |
| Stop as a fraction of the ATR | Risk | Volatility-scaled stop, reusable |
| Regime probability from a filter on returns | Signal | Reusable signal class |
| Two thresholds with a no-trade band between | Rebalancing | Cuts trading inside the band; joins any buffer card |
| Exclude the smallest and cheapest assets (price under $5, bottom NYSE size quintile) | Universe | The idea transfers to any market, e.g. illiquid coins in crypto |
| Condition momentum on comomentum or institutional activity (crowding of the trade) | Signal | A crowding filter for momentum: reusable, and new to the user. Papers often present it as an explanation, not a technique |

**Diagnostic**
| Technique | Kind | Reason |
| --- | --- | --- |
| Compare with the always-long version | performance | The benchmark must fit the strategy: for trend, long-only |
| Regression on squared market return | attribution | Detects a straddle-like profile, useful to build the portfolio |
| Split profit into persistence and mean return | attribution | Says where the profit comes from |
| Split futures return into spot change and roll | attribution | Same, for futures |
| PnL measured in R | performance | Shows payoff asymmetry |

**No card**
| Technique | Reason |
| --- | --- |
| 3x leveraged ETF to bypass a leverage cap | A way to inflate a strategy that works, not a brick of the strategy |
| Regimes defined by 20% moves; parameter update with N = 6 | Free parameters with no economic anchor |
| Thresholds from the model's equation; long and short as two virtual traders; short as the mirror asset 1/S | Only make sense inside the authors' model |
| Average of overlapping portfolios | Statistical device, not a trading rule |
| Net speculator position (CFTC) | No clear use to build or judge a strategy |
| Alpha / beta regression on a benchmark | Standard practice |
| Stop x target grid | A tool to pick the best cell: overfitting |
| "Cut losses, let profits run" | Slogan; its only evidence is an in-sample grid |
| Execute at the open or the close depending on the strategy | Suggested by the authors, not tested, no rule or parameter |
| Cost of a leverage constraint (unconstrained version) | Low value |
| Yearly ex-ante update; real short at 50% margin; log-wealth objective; mean over simulated paths | Standard practice, implementation detail or theory |
