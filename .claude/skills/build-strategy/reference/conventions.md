# Conventions

## Files

- `strategies/<strategy_slug>.py`: one file per strategy, from `assets/strategy-template.py`. Run from the repository root with `poetry run python strategies/<file>.py --period train --variant base`.
- `results/<strategy_slug>/<run id>/`: one folder per run, written by `lab.runs.save_run` (daily P&L, positions, trades, liquidations, summary with the code hash). Never committed.
- The strategy file does not change once the test is run: the test runs the same file, by the user.
- Every run records `code_sha` (the strategy file) and `lab_sha` (the whole lab). All the runs reported together must share the same `lab_sha`; if the lab changed during a build, rerun what ran before the change.

## Data and periods

- Always `lab.data.load(name, test_start=<test start of 1.10>)`. The test start is a constant of the file.
- Train and validation are cut inside the backtest by its `end` and by the dates of the weights; the warm-up of a signal may read data before the train start, never after the period's end.

## Bar size

`lab.backtest` runs at any bar size: daily bars (`crypto_daily`), hourly or one-minute bars (`crypto_1h`, `crypto_1m`, built by `data/get_crypto_intraday.py` for a chosen set of names). For intraday bars, the weights are indexed by the open time of the bar they trade at the close of; the universe can still come from `lab.universe` on the daily file (the row of the previous day). Most bars have no funding print: the engine pays funding only on the bar a print falls in. A one-minute backtest is about 60 times slower than an hourly one: keep it to the names and years Pass 1 needs.

## FX

`lab.fx.fx_bars` and `lab.fx.fx_carry` turn `fx_daily` and `rates` into the engine's bars (nine currencies in dollars per unit) and carry prints (the rate differential, daily). Rebalance on business days with a price. No high or low: no stop and no liquidation path in FX daily.

## Timing (lab.backtest)

- A weight dated d is traded at the close of d (00:00 UTC of d+1). It may use any data up to and including day d: prices, volumes, the universe row of d, funding prints up to 00:00 of d+1.
- A rebalance "Monday 00:00" is a weight dated Sunday.
- Funding: the engine works at print level; a print at exactly 00:00 belongs to the old position.

## Prices, costs, margin

- Mark price for signals, volatility, risk, P&L and liquidation; the engine falls back to the last price where the mark is missing and counts it.
- `cost_bp` one way per unit of notional traded; stress tests change it, never the central case.
- Isolated margin: `leverage` is the leverage per position Pass 1 gives (1.5b); the margin is reset at each rebalance.

## Look-ahead guards

- The engine: a weight earns only returns and prints after the close it is traded at. It cannot see a signal that read the future while being computed.
- The truncation test (`lab.checks.truncation_test`, `--check-lookahead`): weights recomputed on data cut at the close of sampled trade days must equal the full-data weights. It catches a wrong shift, a centred window, the universe row of the trade day, a print after 00:00. Mandatory before the gate.
- The one-day delay control (`--delay 1`): same weights, traded a day later. A collapse means a very fast signal or a leak; the Analyst reads it.
- The Red team attacks the rest later.

## The gate

Pass 1 writes it. For a gate "gross Sharpe at least luck line plus cost / volatility": cost = measured turnover per year x cost_bp / 10,000; volatility = the volatility target of Pass 1. Report the inputs, the bar and the measured value.

## Research Log line

In `vault/3 Research Log/_desk/Research Log.md`.

`YYYY-MM-DD · <period>, <variant>, <what differs from the base> → gross Sharpe x, net Sharpe y, turnover z/yr, funding share w · <verdict>`

Verdicts: baseline · step · insight · dropped · retained · control · logged. The gate run is the baseline; a stress test is logged; a run that fails the gate is dropped.

## The test run

Every run goes through the file's `run(period, variant, cost_bp, delay, open_test)` (template). `lab/run_test.py` calls `run("test", variant, open_test=True)` and refuses a file without it: an option that lives outside `run()` (a cost tier, a leverage rule, a stress switch) would be missing from the test. Put every frozen choice inside `run()` or the functions it calls.
