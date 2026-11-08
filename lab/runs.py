"""
Save every backtest run, so that nothing is run and forgotten.

    folder, s = save_run("Crypto Funding Carry", "train", "base", result, params={"cost_bp": 10})

Writes results/<strategy>/<run id>/ (never committed): daily.parquet (one row per bar), positions.parquet (held
weights, once a day for intraday bars), trades.parquet, liquidations.csv, by_name.csv (P&L per symbol), summary.json. The summary carries the parameters, the engine notes and the hash of the
strategy file, so a run can always be traced to the exact code that made it.
"""
import hashlib, json, sys
from datetime import datetime
from pathlib import Path

from lab.stats import summary

ROOT = Path(__file__).resolve().parent.parent


def lab_sha():
    """One hash for the files that compute a result (data loading, universe, engine): two runs with different
    lab hashes were not computed by the same engine."""
    h = hashlib.sha256()
    for name in ["data.py", "universe.py", "backtest.py"]:
        h.update((ROOT / "lab" / name).read_bytes())
    return h.hexdigest()[:12]


def slug(name):
    return name.lower().replace(" ", "_")


def save_run(strategy, period, variant, result, params=None, code_file=None):
    code = Path(code_file or sys.argv[0]).resolve()
    run_id = f"{datetime.now():%Y%m%d-%H%M%S}-{period}-{variant}"
    folder = ROOT / "results" / slug(strategy) / run_id
    folder.mkdir(parents=True, exist_ok=True)
    result.daily.to_parquet(folder / "daily.parquet")
    result.positions.to_parquet(folder / "positions.parquet")
    result.trades.to_parquet(folder / "trades.parquet")
    result.liquidations.to_csv(folder / "liquidations.csv", index=False)
    result.by_name.to_csv(folder / "by_name.csv")
    s = summary(result)
    s.update({"run_id": run_id, "strategy": strategy, "period": period, "variant": variant, "params": params or {},
              "engine": {k: v for k, v in result.notes.items() if k not in ("price_fallback_days", "delisting_exits")},
              "code": str(code.relative_to(ROOT)) if code.is_relative_to(ROOT) else str(code),
              "code_sha": hashlib.sha256(code.read_bytes()).hexdigest()[:12] if code.exists() else None,
              "lab_sha": lab_sha()})
    (folder / "summary.json").write_text(json.dumps(s, indent=2))
    return folder, s
