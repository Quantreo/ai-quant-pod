---
name: data-check
description: Act as the desk's Data seat and check that a strategy sheet can be tested honestly with the desk's data, before any code: list what Pass 1 needs, check presence, run the generic and market-specific checks, build the point-in-time universe with the Pass 1 parameters, and write a Data check verdict (ready, ready with reserves, blocked). Use whenever the user asks to check, prepare or validate data for a strategy, or a sheet has passed its review and is heading to the Developer.
---

# Data check

1. Read `Pass 1.md` in the strategy folder: 1.4 universe, 1.5 and 1.5b, 1.10 periods, and 1.6 and 1.8 when they exist (a short Pass 1, before the gate, has only the base: check what the base needs, nothing more). Note the test start: you never read data from it. If `Review.md` has a round with rows the Economist has not answered, Pass 1 can still change: say so and stop. If a `Data check.md` already exists, check only what the last changelog row changed.
2. Read `reference/checks.md` and the data cards in `vault/Toolbox/Data/` for the markets involved.
3. List the needs: one row per field Pass 1 uses (prices, high and low, volume, funding, spread, rates...), with the dataset that holds it and the period needed.
4. Presence: run `scripts/check_panel.py <dataset> --coverage-only` for each dataset. If a dataset is missing, too short, or its card lists an open problem that hits this sheet, the verdict is **blocked**: give the user the download command from `data/README.md` and stop.
5. Generic checks: `scripts/check_panel.py <dataset> --until <test start>` for each dataset. For the test period, only `--since <test start> --coverage-only`.
6. Strategy checks: for a crypto universe, `scripts/universe_report.py` with the Pass 1 parameters (the same `lab.universe` function the Developer will call). Then the market checks of `reference/checks.md` that apply to this sheet.
7. Look at the data yourself, like a researcher who has never seen it, in at most five short queries with outputs under 30 lines. Scripts only find what someone already thought of: the zombie contracts and the stock perps were found by looking. With short pandas queries (`lab.data.load`, before the test start), look at the fields Pass 1 uses, on the names and period it will trade: their ranges over time, the names that dominate the universe, how the funding or the spread is distributed, anything that does not match what you know of this market (a price that never moves, a volume far out of line, a name that is not what its ticker says). Prices, volumes and funding of single names are fine to look at; the strategy's returns are not. A new kind of trap goes in the result as an issue, plus a proposed line for `reference/checks.md`.
8. Decide, for each WARN, market check and finding: harmless here (say why in one line: zombie bars cannot reach a top-30 universe by volume), or an issue. An issue has evidence (counts, names, dates), what it does to the test, and an instruction for the Developer. Then the verdict: **ready**, **ready with reserves** (issues with instructions) or **blocked** (the test cannot be honest until data or a script is fixed).
9. Write `Data check.md` in the strategy folder from `assets/data-check.md`, and your row in the index. A "ready with reserves" goes straight to the Developer; a "blocked" goes back to the desk with the command to run.
10. Reply in at most 6 lines: the verdict, the issues in one line each, a proposed line for `reference/checks.md` if you found a new trap.

## Rules

- Never change data, never edit a download script, never download a full dataset. A fix is a proposal for the user, with the line of the script it changes.
- Never compute a return, a Sharpe or anything that tells how the strategy did. You check data, not results.
- Never read the test period beyond coverage counts.
- Every issue is checkable: a count, a name, a date. "Data looks noisy" is not an issue.
- Use `lab.data.load` and `lab.universe`, never your own version: the Developer must trade exactly what you checked.
- Write in English. Never use a long dash.
