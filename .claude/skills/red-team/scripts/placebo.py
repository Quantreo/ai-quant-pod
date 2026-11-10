"""
Permutation placebo: does the signal matter, or would any book with the same shape have done as well?

    poetry run python .claude/skills/red-team/scripts/placebo.py strategies/<file>.py --period train --n 100 [--mode signs]

At each rebalance, the strategy's non-zero weights are shuffled among the same names: same universe, same exposure,
same leg sizes; only the link between the signal and the name is broken (--mode weights, for a cross-sectional ranking).
For a time-series signal (each name long or short on its own signal), use --mode signs: each name keeps its own size,
the signs are shuffled among the names, so the book keeps its risk structure and only the direction is random.
The real gross Sharpe is compared with the distribution of the shuffled ones. Data before the test start only.

Two kinds of strategy file are supported: a crypto file (crypto_daily + crypto_funding, COST_BP, BAND) and an ETF file
(etf_bars, cash_table, tiered_backtest).
"""
import argparse, importlib.util, sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from lab.backtest import backtest                                     # noqa: E402
from lab.data import load                                             # noqa: E402

sharpe = lambda r: float(r.mean() / r.std() * np.sqrt(365)) if r.std() > 0 else float("nan")


def setup(m, period, variant):
    """Weights of the real book and a function weights -> daily gross P&L (price + funding)."""
    start, end = {"train": m.TRAIN, "validation": m.VALIDATION, "train+validation": (m.TRAIN[0], m.VALIDATION[1])}[period]
    if hasattr(m, "etf_bars"):                                        # ETF file: tiers of cost, cash funding
        bars, cash = m.etf_bars(), m.cash_table()
        price_days = pd.DatetimeIndex(sorted(bars["date"].unique()))
        end_ts = pd.Timestamp(end)
        w = m.build_weights(bars, cash, m.rebalance_days(price_days, start, end_ts), variant).fillna(0.0)
        def pnl(x):
            d = m.tiered_backtest(x, bars, cash, end_ts)[0].daily
            return d["price"] + d["funding"]
        return w, pnl
    daily, funding = load("crypto_daily", test_start=m.TEST_START), load("crypto_funding", test_start=m.TEST_START)
    cal = pd.date_range(daily["date"].min(), daily["date"].max(), freq="D")
    days = [d for d in m.rebalance_days(cal) if pd.Timestamp(start) <= d <= pd.Timestamp(end)]
    w = m.build_weights(daily, funding, days, variant).fillna(0.0)
    kw = dict(cost_bp=m.COST_BP, band=m.BAND, leverage=getattr(m, "LEVERAGE", None), end=end)
    def pnl(x):
        d = backtest(x, daily, funding, **kw).daily
        return d["price"] + d["funding"]
    return w, pnl


def shuffle(w, rng, mode):
    p = w.copy()
    for d in p.index:
        row = p.loc[d].to_numpy().copy()
        nz = np.flatnonzero(row)
        if len(nz) > 1:
            if mode == "signs":
                row[nz] = np.abs(row[nz]) * np.sign(row[nz])[rng.permutation(len(nz))]
            else:
                row[nz] = row[rng.permutation(nz)]
            p.loc[d] = row
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("strategy")
    ap.add_argument("--period", default="train", choices=["train", "validation", "train+validation"])
    ap.add_argument("--variant", default="base")
    ap.add_argument("--mode", default="weights", choices=["weights", "signs"])
    ap.add_argument("--n", type=int, default=100)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    spec = importlib.util.spec_from_file_location("strategy", ROOT / a.strategy)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    w, pnl = setup(m, a.period, a.variant)
    real_s = sharpe(pnl(w))
    rng, out = np.random.default_rng(a.seed), []
    for i in range(a.n):
        out.append(sharpe(pnl(shuffle(w, rng, a.mode))))
        print(f"\r  {i + 1}/{a.n}", end="", flush=True)
    out = np.array(out)
    print(f"\n# Placebo ({a.mode}), {a.period}, {a.variant}: real gross Sharpe {real_s:.2f}; shuffled: median {np.median(out):.2f}, "
          f"95th percentile {np.percentile(out, 95):.2f}; share of shuffles at or above the real one: {(out >= real_s).mean():.1%}")


if __name__ == "__main__":
    main()
