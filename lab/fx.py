"""
FX daily for the engine: prices in dollars per unit of each currency, and the carry as daily prints.

    from lab.fx import fx_bars, fx_carry
    fx = load("fx_daily", test_start=...); rates = load("rates", test_start=...)
    bars, carry = fx_bars(fx), fx_carry(fx, rates)
    result = backtest(weights, bars, carry, cost_bp=...)

fx_bars: every pair is turned into one currency against the dollar (EUR, GBP, AUD, NZD, JPY, CHF, CAD, NOK, SEK), price
in dollars per unit, so a long position is long that currency and every P&L is in dollars. USDJPY becomes JPY =
1 / USDJPY. One price a day (noon New York, FRED H.10): high and low are the close, so no intraday path.

fx_carry: a long position in a currency earns its interest rate and pays the dollar rate. The engine's sign is the
funding one (a long pays a positive rate), so the print is -(r_ccy - r_usd) / 365 per calendar day, weekends
included: holding over a weekend earns three days, as the FX rollover does. Rates are monthly averages, known only
after the month ends: the rate used in a month is the previous month's. A rate older than three months is not used
(EUR and GBP stop in 2026-01): no carry is better than a stale one.

Weights: index on business days that have a price; a weight dated on a day with no price is set to zero by the engine.
"""
import pandas as pd

QUOTED_PER_USD = {"USDJPY": "JPY", "USDCHF": "CHF", "USDCAD": "CAD", "USDNOK": "NOK", "USDSEK": "SEK"}
USD_PER_UNIT = {"EURUSD": "EUR", "GBPUSD": "GBP", "AUDUSD": "AUD", "NZDUSD": "NZD"}


def fx_bars(fx):
    out = []
    for pair, g in fx.groupby("pair"):
        if pair in USD_PER_UNIT:
            ccy, px = USD_PER_UNIT[pair], g["close"]
        elif pair in QUOTED_PER_USD:
            ccy, px = QUOTED_PER_USD[pair], 1 / g["close"]
        else:
            continue
        out.append(pd.DataFrame({"date": g["date"].to_numpy(), "symbol": ccy, "close": px.to_numpy()}))
    b = pd.concat(out, ignore_index=True)
    b["high"] = b["close"]; b["low"] = b["close"]
    return b.sort_values(["symbol", "date"]).reset_index(drop=True)


def fx_carry(fx, rates):
    days = pd.date_range(fx["date"].min(), fx["date"].max(), freq="D")
    r = rates.pivot(index="date", columns="currency", values="rate").sort_index() / 100
    r.index = r.index + pd.offsets.MonthBegin(1)                        # known from the first day of the next month
    r = r.reindex(r.index.union(days)).ffill(limit=None)
    last = rates.groupby("currency")["date"].max() + pd.offsets.MonthBegin(1)
    rows = []
    for ccy in set(USD_PER_UNIT.values()) | set(QUOTED_PER_USD.values()):
        if ccy not in r or "USD" not in r:
            continue
        diff = (r[ccy] - r["USD"]).reindex(days)
        stale = days > last.get(ccy, days.max()) + pd.DateOffset(months=3)
        diff[stale] = float("nan")
        rows.append(pd.DataFrame({"symbol": ccy, "time": days + pd.Timedelta(days=1), "rate": -(diff / 365).to_numpy()}))
    c = pd.concat(rows, ignore_index=True).dropna()
    return c.sort_values(["symbol", "time"]).reset_index(drop=True)
