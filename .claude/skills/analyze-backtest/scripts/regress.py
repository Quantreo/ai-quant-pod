"""
Regression of a run's weekly gross returns on factors, with Newey-West t-stats.

    poetry run python .claude/skills/analyze-backtest/scripts/regress.py results/<strategy>/<run id> factors.csv --lags 4

factors.csv: one row per week (column "date", the Sunday ending the week), one column per factor, weekly
returns. The Analyst builds it from the data, point in time, as Pass 1 defines the factors; it lives in
results/<strategy>/analysis/. The intercept is the weekly return not explained by the factors.
"""
import argparse, json
from pathlib import Path

import numpy as np
import pandas as pd


def newey_west(X, e, lags):
    n = len(e)
    Xe = X * e[:, None]
    S = Xe.T @ Xe
    for l in range(1, lags + 1):
        w = 1 - l / (lags + 1)
        G = Xe[l:].T @ Xe[:-l]
        S += w * (G + G.T)
    B = np.linalg.inv(X.T @ X)
    return np.sqrt(np.diag(B @ S @ B))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("factors")
    ap.add_argument("--lags", type=int, default=4)
    a = ap.parse_args()
    run = Path(a.run)
    s = json.loads((run / "summary.json").read_text())
    d = pd.read_parquet(run / "daily.parquet").loc[s["start"]:s["end"]]
    y = (d["price"] + d["funding"]).resample("W-SUN").sum().rename("y")
    f = pd.read_csv(a.factors, parse_dates=["date"]).set_index("date")
    df = pd.concat([y, f], axis=1, join="inner").dropna()
    X = np.column_stack([np.ones(len(df)), df[f.columns].to_numpy()])
    b, *_ = np.linalg.lstsq(X, df["y"].to_numpy(), rcond=None)
    e = df["y"].to_numpy() - X @ b
    se = newey_west(X, e, a.lags)
    r2 = 1 - e.var() / df["y"].var()
    print(f"# {s['strategy']} · {s['period']} · {s['variant']}: {len(df)} weeks, R2 {r2:.2f}, Newey-West lags {a.lags}")
    for name, coef, err in zip(["intercept"] + list(f.columns), b, se):
        print(f"{name:20s} {coef: .5f}  t {coef / err: .2f}")
    print(f"Intercept annualised: {b[0] * 52 * 100:.2f}% of capital a year")


if __name__ == "__main__":
    main()
