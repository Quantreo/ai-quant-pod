# What to check

Generic checks catch broken files. They do not catch data that is clean and wrong: a delisted contract with flat zero-volume bars has no missing value, no duplicate and consistent bars, and would still sit in a backtest as a live name earning nothing. That is why there are market checks, and why each WARN is judged against the strategy.

## Generic checks (`scripts/check_panel.py`)

| Line | What it means | Usually |
| --- | --- | --- |
| missing values | NaN in a column | funding_rate is NaN on days with no print: an issue only if the strategy holds the name that day |
| infinite values | division by zero upstream | always an issue |
| duplicated keys | two rows for one name and time | always an issue |
| time going backwards | file not sorted inside a name | the Developer sorts before any rolling window |
| zero or negative prices | broken bars | always an issue |
| inconsistent bars | high below open or close, low above | an issue if the strategy uses high or low (liquidation, stops) |
| one-bar moves | jumps above 80% (crypto daily), 5% (FX daily) | real pumps or a new token under an old ticker: look at the names the strategy can hold |
| price unchanged 5+ bars | dead or frozen name | an issue if the name can enter the universe |
| zero volume | no trade that day | a day with no trade is not a tradable day |
| missing bars inside a span | archive holes | returns over a hole span several days: the Developer must not annualise them as one day |
| funding prints and intervals | funding feed | see crypto checks |
| stale series | a rate series that stopped | an issue for any period after it stops |

## Crypto perpetuals (Binance USDT-M)

- **Not only coins**: since late 2025 Binance lists perps on stocks, metals, indices and pre-IPO names (AAPLUSDT, XAUUSDT, NVDAUSDT...), with large volumes. `perps_meta.csv` gives `underlying_type`; `lab.universe.crypto_universe` keeps coins only by default. Check the Pass 1 says which types it trades, and count the `unknown` types in the period.
- **Zombie bars**: the archive keeps flat zero-volume bars after a delisting, sometimes for years. The build drops zero-volume days; check that no name in the universe has a long unchanged price.
- **Relisted tickers**: a ticker silent for more than 30 days that comes back is a new listing (often a new token under an old name) and is split as `SYMBOL.2`. Never join it with the old one; check none enters the universe before its own listing age.
- **Archive holes**: about 50 names miss 2022-02-26 to 28, 2022-04-01 to 02 and 2025-03-28 to 30 in the monthly files; the build fills what the daily files have. A hole left inside a held name means a multi-day return.
- **Funding interval**: 8, 4, 2 or 1 hour, and it changes for many names. Annualise per actual print, never 3 a day.
- **Funding timing**: a print belongs to whoever holds the position at its time; `perps_daily.funding_rate` sums the prints of the UTC day. Check that Pass 1's rebalance time and the print times give an unambiguous rule, and say it in the instruction.
- **Funding absent for a whole listing**: some names have prices and no print for months (ICPUSDT 2021-05 to 2022-06, BNXUSDT 2022-04 to 2023-01). A name with a price and no print is not a zero-funding name: it is out of any funding ranking that week.
- **Liquidation price**: Binance liquidates on the mark price; the archive bars are last price. A last-price wick (2021-05-19: ETH low 1,400 against an open of 3,377) can liquidate in a backtest a position the exchange kept. The build has the mark price OHLC: the desk backtests on it (signals, volatility, risk, liquidation, P&L), with the cost assumption covering the real fill. The last price is kept for diagnostics and as a fallback on days with no mark price. Check the instructions say so.
- **Daily funding sum**: `perps_daily.funding_rate` adds the prints of the UTC day, so on a rebalance day it mixes the old and the new position. A strategy that rebalances inside the day works at print level (`crypto_funding`).
- **Missing funding**: days with a price and no print. An issue if the strategy holds the name that day (the P&L would miss funding silently).
- **Multipliers**: 1000SHIB, 1MBABYDOGE: price per 1000 or per million units, from `perps_meta.csv`.
- **Thin early years**: 2020 has few perps; check the minimum number of names Pass 1 asks for, week by week.
- **Universe at a 00:00 rebalance**: the `crypto_universe` row of day t uses day t's volume, known at its close; a rebalance at 00:00 UTC of t uses the row of t-1.
- **Market-wide mark-price holes**: some days have no mark price for most names (2021-07-24 to 27, 2022-10-02, 2023-02-24); count them on the held names and fall back to the last price on those days only.
- **High and low**: needed for liquidation in isolated margin (`vault/Toolbox/Instrument Traps.md`); daily bars only, so the worst intraday path inside a day is unknown.

## Crypto intraday (hourly, one-minute)

- **Only the names asked for**: `perps_1h` / `perps_1m` hold the names the build was run for (`--top N`, `--strategy`, `--symbols`). Check every name the strategy can hold is there, over the whole period.
- **Bars with no trade are dropped**: a missing bar is a bar with no volume, not an error; a return over a gap spans several bars.
- **Funding is sparse**: one print every 8, 4, 2 or 1 hours; most bars have none. The engine pays it on the bar the print falls in.
- **Mark price at intraday size**: the mark files may miss whole hours on some days, as the daily ones do; count the bars with no mark.

## FX (FRED H.10, daily)

- **One price a day, at noon New York**: not the 17:00 close of the FX market. A signal computed on day t trades at the noon rate of day t+1 at the earliest; check the Pass 1 timing matches.
- **No bid, ask, high or low**: costs come from `vault/Toolbox/Cost Assumptions.md`; no intraday stop, no liquidation path.
- **US holidays**: about 10 weekdays a year have no rate; a return across a holiday spans two days.
- **Quote direction**: USDJPY, USDCHF, USDCAD, USDNOK, USDSEK are units per dollar; a return in USD terms needs the inversion.
- **Carry**: price returns miss the interest differential; it comes from the rates dataset.

## Rates (FRED, OECD 3-month interbank, monthly)

- **Known only after the month**: a monthly average is published after the month ends. Lag it one month before using it in a signal.
- **Stale series**: EUR and GBP stop in 2026-01. Any period after that has no rate for them.
- **Approximation**: an interbank rate is not the forward points a position really earns. Say so in any instruction about carry.

## Look-ahead in the data itself

- A universe or filter uses only data known at the close of the date (`lab.universe` does).
- No field computed over the full sample (a listing date from the future, a full-sample volatility).
- The test period is cut by `lab.data.load(test_start=...)`.
