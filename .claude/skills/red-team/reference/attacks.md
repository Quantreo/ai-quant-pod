# Attacks

## Look-ahead patterns in code

- `shift(-k)`, `.diff(-k)`, `pct_change(-k)`, `center=True`, `bfill`, `fillna(method="bfill")`.
- A normalisation over the whole sample (`.mean()`, `.std()`, `.rank()` or a z-score on all dates at once, `quantile` on the full series).
- `resample(..., label="right")` or a weekly sum that ends after the trade day; a `merge_asof(direction="forward")`.
- The universe, the volatility or the funding read on the row of the day after the trade day (a Monday 00:00 trade uses Sunday's row).
- Funding prints with time after 00:00 of the day after the trade day in the signal.
- Anything using `last_day`, `perps_meta` end dates or the knowledge that a name will be delisted.
- A parameter computed from the backtest period (a threshold set to "the median of the sample").

## Tests

- **Truncation** (`lab.checks.truncation_test`): weights recomputed on data cut at the close of a trade day equal the full-data weights. Wider than the Developer's: 40 days, another seed.
- **Placebo** (`scripts/placebo.py`): weights shuffled among the same names at each rebalance (`--mode weights`, for a cross-sectional ranking), or signs shuffled among the names, each keeping its size (`--mode signs`, for a time-series signal). If the real Sharpe is not above the 95th percentile of the shuffled ones, the signal adds nothing the structure of the book does not give.
- **Delay**: the Developer's one-day delay control. A collapse with no leak found means a very fast effect: the weekly mechanism is not what pays.
- **Fill price**: the engine fills at the mark close. The mark is an index price with a smoothed premium; on names whose last price runs far from the index (high funding), a fill at the mark may be a price nobody could trade. Re-price the trades at the last close (or the next open) and compare, above all when the P&L sits in the first day after the trade.
- **Costs**: twice the central cost. A strategy that dies at twice the cost lives on the cost assumption.

## Data

- The days and names that carry the result: a last-price wick the mark did not see, a relisted ticker, a hole of several days, a funding print far out of line, a delisting exit at a price nobody got.
- Survivorship: the Developer's control with today's universe.
