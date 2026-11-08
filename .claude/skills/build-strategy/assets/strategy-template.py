"""
<Strategy name>: built from Pass 1 <version> of vault/2 Strategies/Pipeline/<Strategy name>/<Strategy name>.md.

The file decides the target weights; the lab loads the data (test period sealed), builds the universe,
computes the P&L and saves the run. Every constant names the section of Pass 1 it comes from.

    poetry run python strategies/<file>.py --period train --variant base
    poetry run python strategies/<file>.py --period validation --variant v1
    poetry run python strategies/<file>.py --period train --variant base --cost-bp 20      # stress test
    poetry run python strategies/<file>.py --period train --variant base --check-lookahead # before any run
    poetry run python strategies/<file>.py --period train --variant base --delay 1         # control, not a try
"""
import argparse, sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lab.backtest import backtest            # noqa: E402
from lab.checks import delay_test, truncation_test   # noqa: E402
from lab.data import load                    # noqa: E402
from lab.runs import save_run                # noqa: E402
from lab.universe import crypto_universe     # noqa: E402

NAME = "<Strategy name>"

# 1.10 periods
TRAIN = ("YYYY-MM-DD", "YYYY-MM-DD")
VALIDATION = ("YYYY-MM-DD", "YYYY-MM-DD")
TEST_START = "YYYY-MM-DD"                     # never read here: lab.data.load cuts before it

# 1.4 universe
TOP, VOLUME_WINDOW, MIN_AGE, MIN_NAMES = 30, 30, 90, 20

# 1.5 / 1.5b base version
COST_BP = 10.0                                # 1.7 central case
VOL_TARGET = 0.20                             # 1.5 sizing
BAND = 0.10                                   # 1.5b band width
LEVERAGE = 3                                  # 1.5b / 1.8 isolated margin, leverage per position

VARIANTS = ["base"]                           # 1.9: add v1, v2, v3 exactly as written


def rebalance_days(days):
    """1.5 rebalancing: the trade days (a weight dated d trades at the close of d)."""
    raise NotImplementedError


def build_weights(daily, funding, days, variant="base"):
    """Weights per trade day, in units of capital, using only data up to the close of each day.
    Everything that depends on the data is computed here, the universe included, so that the truncation
    test can recompute it on data cut at any date."""
    universe = crypto_universe(daily, top=TOP, volume_window=VOLUME_WINDOW, min_age_days=MIN_AGE, min_names=MIN_NAMES)
    raise NotImplementedError


PERIODS = {"train": TRAIN, "validation": VALIDATION, "train+validation": (TRAIN[0], VALIDATION[1])}


def run(period, variant="base", cost_bp=COST_BP, delay=0, open_test=False):
    """One run of the frozen configuration. The command line and lab/run_test.py both call this function, so the
    test runs exactly what was validated (costs, leverage, band, every option). period "test" needs open_test=True,
    which only lab/run_test.py passes."""
    if period == "test":
        if not open_test:
            raise SystemExit("The test period is opened only by lab/run_test.py, approved by the user.")
        start, end = TEST_START, None
    else:
        start, end = PERIODS[period]
    daily = load("crypto_daily", test_start=TEST_START, open_test=open_test)
    funding = load("crypto_funding", test_start=TEST_START, open_test=open_test)
    calendar = pd.date_range(daily["date"].min(), daily["date"].max(), freq="D")
    days = [d for d in rebalance_days(calendar) if pd.Timestamp(start) <= d and (end is None or d <= pd.Timestamp(end))]
    w = build_weights(daily, funding, days, variant)
    if delay:
        w = delay_test(w, delay)
    result = backtest(w, daily, funding, cost_bp=cost_bp, band=BAND, leverage=LEVERAGE, end=end)
    name = variant + (f"-delay{delay}" if delay else "")
    return save_run(NAME, period, name, result, params={"cost_bp": cost_bp, "delay": delay}, code_file=__file__)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", choices=list(PERIODS), required=True)
    ap.add_argument("--variant", choices=VARIANTS, default="base")
    ap.add_argument("--cost-bp", type=float, default=COST_BP)
    ap.add_argument("--check-lookahead", action="store_true", help="truncation test only, no run")
    ap.add_argument("--delay", type=int, default=0, help="trade the same weights this many days later (control)")
    a = ap.parse_args()
    if a.check_lookahead:
        start, end = PERIODS[a.period]
        daily = load("crypto_daily", test_start=TEST_START)
        funding = load("crypto_funding", test_start=TEST_START)
        calendar = pd.date_range(daily["date"].min(), daily["date"].max(), freq="D")
        days = [d for d in rebalance_days(calendar) if pd.Timestamp(start) <= d <= pd.Timestamp(end)]
        truncation_test(build_weights, daily, funding, days, variant=a.variant)
        return
    folder, s = run(a.period, a.variant, cost_bp=a.cost_bp, delay=a.delay)
    print(folder)
    for k, v in s.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
