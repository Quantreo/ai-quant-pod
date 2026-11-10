"""
Standard read of one or more saved runs (results/<strategy>/<run id>/), the same for every strategy.

    poetry run python .claude/skills/analyze-backtest/scripts/run_report.py results/crypto_funding_carry/<run id> \
        --test-start 2025-01-01

Prints: the summary; P&L by year and by leg; weekly skew and worst weeks; drawdown; a block bootstrap of the
Sharpe; contribution by name (price plus funding, from the saved positions and the data) with the share of
the top 5. With two runs or more, a side-by-side table (base against delay, survivorship control...).
The test period is read only for a run whose period is "test".
"""
import argparse, json, sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from lab.attribution import by_name, read_run                          # noqa: E402

PPY = 365


def sharpe(r):
    return float(r.mean() / r.std() * np.sqrt(PPY)) if r.std() > 0 else float("nan")


def bootstrap(r, block=63, n=2000, seed=0):
    a, rng, out = r.to_numpy(), np.random.default_rng(seed), []
    for _ in range(n):
        st = rng.integers(0, len(a) - block, len(a) // block + 1)
        s = np.concatenate([a[i:i + block] for i in st])[:len(a)]
        out.append(s.mean() / s.std() * np.sqrt(PPY))
    return np.percentile(out, [5, 50, 95])


def contributions(folder, s, test_start):
    return by_name(folder, test_start)


def report(folder, test_start):
    folder = Path(folder)
    s, d = read_run(folder)
    gross, net = d["price"] + d["funding"], d["total"]
    print(f"\n# {s['strategy']} · {s['period']} · {s['variant']} · {folder.name} · lab {s.get('lab_sha')} · code {s.get('code_sha')}")
    print("Summary: " + ", ".join(f"{k} {s[k]}" for k in ["gross_sharpe", "net_sharpe", "net_t_stat", "net_vol_pct", "max_drawdown_pct",
                                                           "turnover_per_year", "funding_share_of_gross", "breakeven_cost_bp", "liquidations"]))
    y = d.groupby(d.index.year)
    by_year = pd.DataFrame({"gross_sharpe": y.apply(lambda x: sharpe(x["price"] + x["funding"])), "net_sharpe": y.apply(lambda x: sharpe(x["total"])),
                            "price_%": y["price"].sum() * 100, "funding_%": y["funding"].sum() * 100,
                            "cost_%": y["cost"].sum() * 100, "liq_%": y["liquidation"].sum() * 100})
    print("By year:\n" + by_year.round(2).to_string())
    legs = d[["price_long", "price_short", "funding_long", "funding_short"]].sum() * 100
    print("By leg (% of capital): " + ", ".join(f"{k} {v:.2f}" for k, v in legs.items()))
    w = gross.resample("W-SUN").sum()
    print(f"Weekly gross: skew {w.skew():.2f}, worst 10 weeks: " + ", ".join(f"{i:%Y-%m-%d} {v*100:.1f}%" for i, v in w.nsmallest(10).items()))
    lo, mid, hi = bootstrap(net)
    print(f"Net Sharpe, block bootstrap 5/50/95 %: {lo:.2f} / {mid:.2f} / {hi:.2f}")
    c = contributions(folder, s, test_start)
    tot = c["total"].sum()
    print(f"Names: {len(c)}; top 5 share of P&L: {c['total'].head(5).sum() / tot:.0%}" if tot > 0 else f"Names: {len(c)}; total P&L not positive")
    print("Top 5: " + ", ".join(f"{i} {r.total*100:.1f}% (price {r.price*100:.1f}, funding {r.funding*100:.1f})" for i, r in c.head(5).iterrows()))
    print("Bottom 5: " + ", ".join(f"{i} {r.total*100:.1f}%" for i, r in c.tail(5).iterrows()))
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("runs", nargs="+")
    ap.add_argument("--test-start", required=True)
    a = ap.parse_args()
    rows = [report(r, a.test_start) for r in a.runs]
    if len(rows) > 1:
        keys = ["period", "variant", "gross_sharpe", "net_sharpe", "funding_share_of_gross", "turnover_per_year", "pnl_price_pct", "pnl_funding_pct", "liquidations", "lab_sha"]
        print("\nSide by side:\n" + pd.DataFrame([{k: r.get(k) for k in keys} for r in rows]).to_string(index=False))


if __name__ == "__main__":
    main()
