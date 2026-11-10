"""
Open the test period of one or several strategies, once each. The desk calls it at the end of a run, in one batch;
Claude Code asks the user before it runs (rule "ask" in .claude/settings.json): that click is the human gate.

    poetry run python lab/run_test.py --batch strategies/etf_tsmom_12m.py:base strategies/crypto_thin_losers.py:twin
    poetry run python lab/run_test.py strategies/crypto_funding_carry.py --variant base      # one strategy

Each strategy runs its own run("test", variant, open_test=True): the same function as every train and validation
run, so the test runs the frozen configuration (costs, leverage, band, options) and nothing rebuilt here. A strategy
file without run() is refused. Then it writes results/<strategy>/TEST_DONE (the run, the variant, the code and lab
hashes): a second opening is refused. After this, the strategy file and Pass 1 do not change: the Analyst reads the
test with the three-zone rule. Nothing else in the repository opens a test (hook .claude/hooks/test_guard.py).
"""
import argparse, hashlib, importlib.util, json, sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from lab.runs import lab_sha, slug                                     # noqa: E402


def open_one(file, variant):
    path = ROOT / file
    if not path.exists():
        return {"strategy": file, "error": "no such file"}
    spec = importlib.util.spec_from_file_location("strategy", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    lock = ROOT / "results" / slug(m.NAME) / "TEST_DONE"
    if not hasattr(m, "run"):
        return {"strategy": m.NAME, "error": "no run(period, variant, open_test) function: the test could differ from the "
                                             "configuration validated (ask the Developer to add it, see the strategy template)"}
    if lock.exists():
        return {"strategy": m.NAME, "error": f"test already opened: {lock.read_text()}"}
    code = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
    print(f"{m.NAME}: test from {m.TEST_START}, variant {variant}, code {code}, lab {lab_sha()}", flush=True)
    out = m.run("test", variant, open_test=True)
    folder, s = out[0], out[1]                                         # some run() return more than (folder, summary)
    lock.parent.mkdir(parents=True, exist_ok=True)
    lock.write_text(json.dumps({"opened": f"{datetime.now():%Y-%m-%d %H:%M}", "run": folder.name, "variant": variant,
                                "code_sha": s["code_sha"], "lab_sha": s["lab_sha"]}))
    return {"strategy": m.NAME, "run": str(folder.relative_to(ROOT)), "start": s.get("start"), "end": s.get("end"),
            "net_sharpe": s.get("net_sharpe"), "gross_sharpe": s.get("gross_sharpe"), "max_dd_pct": s.get("max_drawdown_pct"),
            "turnover": s.get("turnover_per_year")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("strategy", nargs="?", help="path of one strategy file, from the repository root")
    ap.add_argument("--variant", default="base", help="the version frozen for the test, as Pass 2 names it")
    ap.add_argument("--batch", nargs="+", metavar="FILE:VARIANT", help="several strategies in one call, each FILE:VARIANT")
    a = ap.parse_args()
    jobs = [(b.rsplit(":", 1)[0], b.rsplit(":", 1)[1] if ":" in b else "base") for b in (a.batch or [])]
    if a.strategy:
        jobs.append((a.strategy, a.variant))
    if not jobs:
        ap.error("give a strategy file or --batch FILE:VARIANT ...")
    results = []
    for file, variant in jobs:
        try:
            results.append(open_one(file, variant))
        except Exception as e:                                         # one failure does not stop the batch
            results.append({"strategy": file, "error": f"{type(e).__name__}: {e}"})
    print("\n| Strategy | Test | Net Sharpe | Gross Sharpe | Max DD % | Turnover / yr | Run |\n| --- | --- | --- | --- | --- | --- | --- |")
    for r in results:
        if "error" in r:
            print(f"| {r['strategy']} | not opened: {r['error']} | | | | | |")
        else:
            print(f"| {r['strategy']} | {r['start']} to {r['end']} | {r['net_sharpe']} | {r['gross_sharpe']} | {r['max_dd_pct']} | {r['turnover']} | {r['run']} |")
    print("\nOpened tests are final. Next: the Analyst reads each one with the three-zone rule.")
    sys.exit(1 if any("error" in r for r in results) else 0)


if __name__ == "__main__":
    main()
