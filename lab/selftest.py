"""
Self-test of the lab: checks the engine on cases whose answer is known in advance.

    poetry run python lab/selftest.py

Run it once after installing, and again after any change to lab/. Every line must say OK.
Synthetic prices only, except the last check, which loads your crypto data if it is there.
"""
import contextlib, io, sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lab.backtest import backtest            # noqa: E402
from lab.checks import truncation_test       # noqa: E402

FAILED = []


def check(name, ok, detail=""):
    print(f"{'OK  ' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILED.append(name)


def bars(prices, symbol="AAA", start="2024-01-01"):
    """A daily panel with one symbol: date, symbol, close, high, low."""
    dates = pd.date_range(start, periods=len(prices), freq="D")
    p = np.asarray(prices, float)
    return pd.DataFrame({"date": dates, "symbol": symbol, "close": p, "high": p, "low": p})


# 1. Buy and hold, no cost: the P&L is the price return
prices = [100, 110, 99, 120, 130]
b = bars(prices)
w = pd.DataFrame({"AAA": [1.0]}, index=[b["date"].iloc[0]])
r = backtest(w, b, cost_bp=0)
pnl, expected = r.daily["total"].sum(), prices[-1] / prices[0] - 1
check("buy and hold earns the price return", abs(pnl - expected) < 1e-12, f"P&L {pnl:.4f}, price return {expected:.4f}")

# 2. Timing: a weight dated d earns nothing on day d, only after
check("a weight dated d earns nothing on day d", r.daily["total"].iloc[0] == 0.0,
      f"day d P&L {r.daily['total'].iloc[0]:.4f}, day d+1 P&L {r.daily['total'].iloc[1]:.4f}")

# 3. Costs: a round trip at 10 bp on flat prices costs exactly 20 bp
b = bars([100] * 5)
w = pd.DataFrame({"AAA": [1.0, 0.0]}, index=[b["date"].iloc[0], b["date"].iloc[2]])
r = backtest(w, b, cost_bp=10)
cost = r.daily["cost"].sum()
check("a round trip at 10 bp costs 20 bp", abs(cost + 0.0020) < 1e-12, f"cost {cost * 1e4:.1f} bp")

# 4. Funding: a long pays a positive funding print
f = pd.DataFrame({"symbol": ["AAA"], "time": [b["date"].iloc[1] + pd.Timedelta(hours=8)], "rate": [0.0001]})
r = backtest(pd.DataFrame({"AAA": [1.0]}, index=[b["date"].iloc[0]]), b, funding=f, cost_bp=0)
fund = r.daily["funding"].sum()
check("a long pays positive funding", abs(fund + 0.0001) < 1e-12, f"funding {fund * 1e4:.1f} bp")

# 5. Look-ahead: the truncation test passes an honest signal and catches a cheating one
rng = np.random.default_rng(0)
dates = pd.date_range("2024-01-01", periods=80, freq="D")
panel = pd.concat([pd.DataFrame({"date": dates, "symbol": s, "close": 100 * np.exp(np.cumsum(rng.normal(0, 0.02, 80)))})
                   for s in ["AAA", "BBB", "CCC"]], ignore_index=True)
no_funding = pd.DataFrame({"symbol": [], "time": pd.to_datetime([]), "rate": []})
days = list(dates[10:])


def honest(daily, funding, days):
    c = daily.pivot(index="date", columns="symbol", values="close")
    return np.sign(c.pct_change(5)).reindex(days).dropna(how="all")         # past 5 days only


def cheating(daily, funding, days):
    c = daily.pivot(index="date", columns="symbol", values="close")
    return np.sign(c.pct_change().shift(-1)).reindex(days).dropna(how="all")  # tomorrow's return


with contextlib.redirect_stdout(io.StringIO()):
    ok_honest = truncation_test(honest, panel, no_funding, days)["ok"].all()
    ok_cheat = truncation_test(cheating, panel, no_funding, days)["ok"].all()
check("the truncation test passes an honest signal", bool(ok_honest))
check("the truncation test catches a signal that reads tomorrow", not ok_cheat)

# 6. Sealed test: loaded data stops before the test start
try:
    from lab.data import load
    d = load("crypto_daily", test_start="2025-01-01")
    check("loaded data stops before the test start", d["date"].max() < pd.Timestamp("2025-01-01"),
          f"last date {d['date'].max():%Y-%m-%d}, test start 2025-01-01")
except FileNotFoundError:
    print("SKIP  loaded data stops before the test start  (no crypto data yet: run data/get_crypto_daily.py)")

print()
print("All checks passed." if not FAILED else f"{len(FAILED)} check(s) failed: {', '.join(FAILED)}")
sys.exit(1 if FAILED else 0)
