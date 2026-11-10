## Test

**Verdict: keep on paper only, no money (ambiguous zone)** · 2026-10-24 · run read: 20261024-083811-test-base (2025-01-01 to 2026-09-30, 638 days) · control: 20261024-083824-train-base · lab afd371aa0a4a · code c7814558d546 · report [[Crypto Thin Losers - Test report]]

The test does not kill the strategy and does not confirm it. The net mean per day is 0.00025 against 0.00078 on train plus validation: 32% of the earlier mean, below the half that confirms, far above the minus half that kills. The worst news is not in the zone rule: the mechanism did not pay. The long thin leg lost 45.0% of capital in price, and the profit came from the short liquid leg (+96.8%, of which the BTC hedge cost 20.2%). On train it was the other way (long +228.5%, short -88.7%). The sign of the spread still holds (thin falls less than liquid), but "sellers of thin coins are paid by the recovery" is not what the test shows.

### The three zones (1.11 #5)

| Quantity | Train + validation | Test | Ratio |
| --- | --- | --- | --- |
| Net mean per day (after tiered cost, funding) | 0.00078 (NW t 2.29, 1461 days) | 0.00025 as run, 0.00026 with the 1.5b tier rebuilt (NW t 0.46 / 0.50, 638 days) | 0.32 / 0.33 |
| Gross mean per day (price plus funding) | 0.00107 (NW t 3.13) | 0.00055 (NW t 1.04) | 0.51 |
| Net Sharpe | 1.377 train, 0.331 validation | 0.378 (bootstrap 5/50/95%: -0.64 / 0.38 / 1.35) | |

Bars: confirms above 0.00039 (half), contradicts below -0.00039 with t under -1.5. The test sits between: ambiguous, paper only. Pass 1 does not say if "mean" is net or gross. Net is what the book earns, so I apply it (the stricter reading). On gross the ratio is 0.51, a hair above half, which would read as confirms; I do not use it. Either way the t on the test is 0.5 (net) to 1.0 (gross): the test cannot tell this strategy from zero. The earlier mean is dominated by train (3 of 4 years), as Pass 2 warned; the 2024 level alone (0.00021 net) is the same as the test level (0.00025): the test confirms that 2024 was not a bad year but the new level.

### What changed in lab/ (sha fd8ce652344b to afd371aa0a4a) and can it move numbers

The diff of `lab/` is a refactor of `lab/backtest.py` so that the engine accepts hourly and minute bars (a `freq`, a `by_name` P&L per symbol, a `weighted_without_price` note), plus: `stats.py` resamples to days only for intraday bars; `runs.py` saves `by_name.csv`; `attribution.py` reads `by_name.csv`; `data.py` adds two dataset names; `trials.py` reads Pass 1 as well as the index; `report.py`, `tearsheet.py` display only. I did not read this as a proof; I tested it: the train base was rerun on the new lab (20261024-083824-train-base) and its daily price, funding, cost, liquidation and total differ from the old-lab train run (20261023-164156) by exactly 0.0 over 1095 days, with the same 23 liquidations and 13 delisting exits. Daily bars follow the same code path, so the change cannot move numbers on the same inputs. Validation was not rerun on the new lab; its engine path is the one train exercised. One new behaviour: a name weighted but never priced in the window is skipped and listed. On the test it lists BLZUSDT and DARUSDT (never traded, small); on train the list is empty.

### The test run is not the frozen configuration

The summary of the test run shows `cost_bp 12.5` flat, `leverage null` (no isolated-margin check, 0 liquidations) and no tier. The frozen base (1.5b, Build) charges 20 bp on the thin leg and 5 bp on the liquid leg and the hedge, with isolated margin at the gross and liquidations at 12.5 bp. The strategy file on disk cannot run period "test" (its choices stop at train+validation), so the run was made another way; the file hash is the same. I rebuilt the tiered cost from the saved positions (method checked on train: 28.98% rebuilt against 28.82% saved; validation 11.97% against 11.82%). On test: 18.3% tiered against 19.4% flat; net mean 0.00026 against 0.00025. Liquidations are not modelled: on train they cost 0.42% in 3 years, so the omission is of the order of 0.1% a year. The zone does not change under any of these. I did not ask for a rerun: it would not change the verdict, and a run is not mine to make. The Developer should say how the test was run.

### Criteria and predictions, read on the test (the 1.11 gates are train gates; this is information)

| Item | Test | Reading |
| --- | --- | --- |
| #2 net Sharpe vs 0.49 | 0.378 (0.405 tiered) | below the train bar; 1.11 applies #2 to train only, no verdict from it |
| #1 gross intercept on market today + 5 lags | +0.00061/day, NW t 1.20 (no depth control) | same sign, not significant (train 3.01, 2024 0.85) |
| #4 price share of gross | 1.47 (price 51.7, funding -16.5; funding share -0.47) | passes the bar, but funding costs a third of price; the short leg paid 18.7% of funding |
| P2 premium among losers | not rebuilt (winners spread needs a new run) | not measurable |
| Legs | long -45.0%, short +96.8% (2025: -52.6 / +78.2; 2026 to Sept: +7.6 / +18.6) | the P&L is made by another mechanism: liquid losers kept falling and carried a negative funding for shorts, not thin losers recovering |
| Book size | 95 names long, 92 short on average (train 34 / 31); gross 1.68 (1.45) | a different book: the universe tripled, the thin cell is no longer a few names |
| Concentration | top 5 names 74% of P&L (train 41%); no DOGE-type day | the P&L is spread on a few names but none dominates (largest 6.6%) |
| Drawdown | -29.6% (train -20.7%, 2024 -24.3%) | worse than before |
| Weekly skew | +0.25 (train +1.94, 2024 -0.31) | the positive skew of train is gone |

### Luck

No new try: the test is the frozen base run once (trials file: counts no). Tries stay 3 (luck line 0.49 on train). Test gross 0.84 is above 0.49 by 0.35, net 0.38 is below it by 0.11, on 1.75 years where a Sharpe of 0.84 gross has an error of about 0.76. Desk luck line 0.35, N_eff 2.3.

### Decision

**Keep on paper only, no money, half weight not earned.** The rule of 1.11 #5 gives the middle zone. I add what the rule does not say: three readings in a row now (2024 net 0.33, test net 0.38) put the net Sharpe near 0.35, under the 0.49 luck line and at break-even cost 20 to 23 bp, which is the assumed thin cost; on the test the economic story reversed from the long leg to the short leg. Paper trading will say which of these two is true: a smaller edge of the same kind, or an edge that came from other legs than the written payer. I would not size anything on this; a Park would be as defensible as paper, and it is the human gate's call, not a rule in Pass 1.

### Questions for the Economist and the human

1. Pass 1 says "above half, paper at half weight". With the ratio at 0.32 the strategy gets no weight at all; confirm that paper means no capital.
2. Should the thin-leg payer be rewritten, since the test says liquid losers carry the profit? That rewrite would be a new try.
3. Is the mean of 1.11 #5 net or gross? Net applied here.
