---
name: build-strategy
description: Act as the desk's Developer: turn a reviewed and data-checked strategy sheet into code, exactly as Pass 1 says, with the desk's lab (load, universe, backtest, runs), then run the train gate and, if it passes, the validation runs Pass 1 lists, saving and logging every run. Use whenever the user asks to code, build, implement, backtest or run a strategy sheet, or a sheet has a Data check and is waiting for code.
---

# Build a strategy

1. Read `Pass 1.md` and `Data check.md` (its instructions are mandatory) in the strategy folder; in phase validation, also `Build.md`, `Changelog.md` and the answers in `Review.md`. Stop and say why if there is no Data check, if it says blocked, if a review round is open, or, in phase validation, if the status is not `reviewed`.
2. Read `reference/conventions.md` and the docstrings only (`head -40`) of `lab/data.py`, `lab/universe.py`, `lab/backtest.py`, `lab/runs.py`.
3. Write the spec table, one row per choice: what Pass 1 says (section), what the code does, which Data check instruction applies. A choice Pass 1 and the Data check do not settle is a **spec gap**. In phase gate, do not stop: take the simplest reading that uses no result, write it in `Build.md` under **Assumptions** (the gap, the reading, why), and run; the Economist reads the assumptions only if the gate passes. In phase validation, a gap that can change a result stops that strategy: write a Developer round in `Review.md` from `assets/developer-round.md` and reply that it waits for the Economist. A gap that cannot change a result (a variable name, the order of two columns) is not a gap.
4. Write `strategies/<strategy_slug>.py` from `assets/strategy-template.py`. Every constant carries the section of Pass 1 it comes from. The file computes signals and target weights; the lab does loading, universe, P&L and saving.
5. Check the file against the Data check instructions one by one, and against the timing convention (a weight dated d trades at the close of d and uses nothing after it). Then run the truncation test (`--check-lookahead`): it recomputes the weights on data cut at a sample of trade days and must PASS before any run. A FAIL is a bug to fix, never a result. Write both checks in the build section.
6. **Phase gate**: exactly one run: train period, base version, central cost. No diagnostic, no control, no variant: they belong to the validation phase. Save it (the template does), compute the gate as Pass 1 writes it, with the measured turnover. Stop there, pass or fail. On a fail, add one lesson line to your reply if the failure teaches something beyond this strategy.
7. **Phase validation** (after the review, on a passed gate; if the base changed since the gate, run the gate again first): run what Pass 1 lists for validation, and nothing else: the base on the periods Pass 1 names, each variant, each stress test. Add one control: the base traded one day late (`--delay 1`), logged as a control and not a try; the Analyst reads it. Every run is saved.
8. Write `Build.md` in the strategy folder from `assets/build-section.md` (phase validation: add the new runs to it): the code and its hash, the spec table, the Data check instructions applied, the runs table, the measured turnover against the estimate, the gate result. Append one Research Log line per run under the strategy in `vault/3 Research Log/_desk/Research Log.md`. Add your row to the index.
9. Reply in at most 6 lines: the gate (bar, measured, pass or fail), the run folders, the lesson if any.

## Rules

- Several folders in one prompt (a batch of gates): read the conventions and the lab once, then build and gate the strategies one after the other in this context. A spec gap on one does not stop the others.
- The same error stops a run twice: stop trying. Write in `Build.md` what fails and where, and reply; never a third fix in a row.

- Pass 1 is the spec. Never choose a number it does not give (except an Assumption of the gate, written before the run); never change one after seeing a result. A change is a question for the Economist, through a Developer round.
- Never open the test period: no `open_test=True`, no date at or after the test start. The test is run once, by the user, after the Red team and the human gate.
- Every run is saved with `lab.runs.save_run` and gets its Research Log line, the bad ones first of all.
- Never judge the strategy beyond the gate Pass 1 asks you to compute: the verdict on predictions, luck and regimes belongs to the Analyst.
- Do not rewrite the lab. If it lacks something, say what, and code it in the strategy file only if it is specific to this strategy.
- Code and reports in English. Never use a long dash.
