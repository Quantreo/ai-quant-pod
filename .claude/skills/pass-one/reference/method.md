# Method

Pass 1 is written before any code. It decides whether an idea deserves a test, and designs the test so that its result means something. The Developer will fix every exact parameter while coding; the Economist states what is built, why, and what would kill it.

## Verdict

- **Go**: a payer named, even as a `[hypothesis]` the library does not prove; why it persists; at least two predictions, one of which would show the payer wrong; a design within the cost budget. The train gate and the trial count decide the rest.
- **Go with a check**: plausible, but one cheap discriminating test must pass first. Name it at the top.
- **Park**: nobody can be named as the payer, or a line of `Lessons.md` already rules this one out and nothing here answers it. "I do not know where this comes from" is a valid answer: keep the idea, revisit when a new source appears.
- **Kill**: beta or short volatility in disguise, a data artefact, a mechanism known to be dead, or costs larger than any plausible edge.

Put the verdict at the top of `Pass 1.md`, in two or three lines, with its conditions. Pass 1 fits in 1500 words: tables over prose.

## Judge (1.1 to 1.3)

**1.1 Mechanism**: type (see `mechanisms.md`), who pays, why the market, why it is not arbitraged away, what it could secretly be, predictions P1, P2... Each prediction says what its failure does: a kill criterion (give its number), or "read only" (it lowers confidence and is reported, the strategy goes on). A prediction said to separate the mechanism from its rival should not be read only, or it is a gate in disguise that nobody applies. Separate what the sources show from your own construction.

**1.2 Sources and crowding**: the library notes behind the idea, the bricks derived from them, earlier attempts, and how public the idea is.

**1.3 Expected behaviour**: works when, suffers when, payoff profile (skew, how many names or days carry the year).

## Design (1.4 to 1.11)

**1.4 Universe**: where the payer exists, filtered by liquidity. Say what a cut-off justifies: a reason to stop somewhere is not a reason for the exact number. Survivorship: point-in-time membership, measured against a frozen control when it matters.

**1.5 Base version**: one row per choice: brick, choice, why, basis, card. Bases: **mechanism**, **cost**, **source**, **convention** (standard, with its reference), **scale** (does not change the Sharpe), **free** (nothing decides it).

House defaults, each still with its reason: inverse-volatility sizing and a volatility target; point-in-time universe; costs in from the first run; P&L split into price, carry or funding, and costs when the instrument pays or charges a carry; train, validation and test periods fixed in Pass 1.

**1.5b Free parameters**: every number that nothing decides: value, why this value, how it is tested (variant, stress test, or "follows from" another choice). Nobody should find a number in the sheet without its reason. A parameter is a variant or a stress test, never both: otherwise nobody knows whether it counts as a try.

**1.6 Horizon, trades, power**: holding period, trades or turnover a year, number of independent observations, luck line, power when trades are few. The tries passed to `budget.py --tries` are the desk's history on the same data plus this strategy's own: N_eff of the row "family and asset" in `vault/3 Research Log/_desk/Trials summary.md` (0 if there is none), plus the base and the variants. Write both numbers. The Analyst recomputes N_eff once this strategy's runs are in the file.

**Data already seen**: one or two lines, no count. Has the desk already worked on this data (archived sheets, Research Log)? If so, the in-sample and the out-of-sample split are not clean, and the true out-of-sample starts with paper trading. Say it.

**1.7 Cost and capacity budget**: the turnover is an estimate: write how it is obtained (share of the capital traded at each rebalance, rebalancing frequency, band) and compute it with `scripts/budget.py --rotation --rebalances`. Give a central estimate with its reasoning, not a stack of worst cases: the gates are already strict, and a pessimistic cost on top of them kills good strategies on paper. The gross book is not a free number: with a volatility target it follows from the volatility of the long-short spread, so estimate it from that (and cap it if needed). The gates use the measured turnover once the first run gives it. Hand estimates have run 1.2 to 2.8 times below the measured turnover (desk, 2026-10-25): the estimate only sorts ideas, never decides a gate. Yearly cost = turnover x cost per unit traded, with the cost from `vault/Toolbox/Cost Assumptions.md`. Costs must stay under half the expected edge: state the gross Sharpe needed. If no cost assumption exists for the market, write the one used and mark it "to confirm". Capacity in one line.

**1.8 Instrument traps**: from `vault/Toolbox/Instrument Traps.md`, the ones that apply and how the P&L will account for them.

**1.9 Variants**: at most 3, each changing one brick, each tied to a prediction or a known weakness, with the expected effect. A variant answers a question; it is not a candidate in a beauty contest. The validation period is short, so a Sharpe gap between variants is mostly noise: a variant replaces the base only if the prediction it was built for comes out, never on Sharpe alone. Each counts as a try. Stress tests (costs, universe size, window length, controls) are listed apart: not tries, but the result must hold.

**1.10 Test plan**: three periods, fixed now. **Train**: build and adjust freely. **Validation**: read the variants against their predictions and decide revisions; tries count here. **Test**: looked at once, at the very end; any change after seeing it burns it, and only paper trading can judge the strategy then. List the diagnostics that check each prediction.

**1.11 Kill criterion**: follow `vault/Toolbox/Kill Policy.md`: a criterion kills on evidence against, never on absence of evidence. At most three criteria, each of a kind the policy lists, ranked, the key prediction first; then thresholds on the full sample (net Sharpe, luck line, concentration, turnover) and the three-zone rule out of sample. Each extra criterion is one more chance to kill a good strategy by bad luck. One condition per criterion: "A and B" is two criteria. A condition true by construction (a book short the high-funding names collects funding as long as funding persists) tests nothing: leave it out. A criterion must be able to fire: check it against an archived sheet when one exists.

**House rule: a cheap train gate, a strict proof.** The train gate kills cheaply what is clearly dead; it does not prove the edge, and it does not test whether the signal beats a simpler one. On a short train a t-stat of 2 asks for an annual Sharpe of 2 / sqrt(years), 1.15 on 3 years, more than most real premia earn, so such a gate lets through mostly the lucky trains. The gate of 2026-10-25 also showed that stacking low-power controls at t 2 lets a real premium of Sharpe 0.5 through about one time in ten (`vault/3 Research Log/Desk reports/2026-10-25 Gate power diagnostic.md`). So:

- **The level is the gate.** Net Sharpe above the luck line plus cost (measured turnover), with a t-stat bar from the train's length: **1 when the train is shorter than 5 years, 2 otherwise** (`budget.py` gives it). This is the only criterion that kills on train by default.
- **At most one control at the gate**, and only if its power is **50% or more** at a plausible edge (state it with `budget.py`). A sign check that is cheap and clear (the long leg does better than the universe, the effect is not the market's own move) qualifies when its power is stated.
- **Controls are labels, not kills** (`vault/Toolbox/Kill Policy.md`). A control or a prediction kills only if it contradicts the strategy (alpha t at or below -1, the wrong sign at t -1). With a positive sign and a t under 2, it is a label: "premium, alpha not shown", and the strategy goes on to the test.
- **A twin that beats the base becomes the candidate.** When a simpler twin (always-long, the sign of the market, a one-signal version) does better than the base on the gate, the twin goes on in its place, as a new version: one more try in the family. Simpler and better wins.

The proof comes after the test: the net t-stat on train, validation and test together must reach 2, or the strategy stays on paper whatever its test zone (`analyze-backtest`, rules). The bar is set by this rule, never by the sheet: never lower it to raise the power, never raise it to kill an idea. State the power on the sample where each criterion applies: the chance that a strategy with a plausible true Sharpe passes, and the chance that one with a true Sharpe of zero passes. A killed strategy is not retested on the same data: that would be one more try. Reading an existing train run again under a new desk-wide rule is not a try. Section 1.8 of the old template (exit criterion live) belongs to the PM.

## After Pass 1

The strategy folder keeps its history: `Review.md` (the Critic's round, with the Economist's answer to each objection) and `Changelog.md` (every change to Pass 1: date, what, why, what triggered it, which data period it was decided on, whether it counts as a try). `Pass 1.md` always shows the version in force.

The flow: the short Pass 1 (mechanism, base, costs, periods, train gate), the Data check, the train gate on the base. Only after a passed gate: the full Pass 1 (sources, expected behaviour, power, traps, variants, diagnostics, the other kill criteria and the test zones), written before any validation run and with the train result of the base declared as data already seen. Only a strategy that passes gets the Critic round, one revision by the Economist (who checks his own changes), the validation runs and the rest. A change to the base decided after the gate counts as a try, and the gate is run again.

## Checklist

- [ ] Verdict at the top, with its conditions.
- [ ] Mechanism typed; all questions of its type answered.
- [ ] Every claim labelled; every figure from a note page or `budget.py`.
- [ ] At least two predictions, each tied to a diagnostic in 1.10 and saying what its failure does.
- [ ] Every choice in 1.5 has a basis; every free number is in 1.5b.
- [ ] Data already seen stated, with where the true out-of-sample starts.
- [ ] Turnover estimate explained; cost budget stated, with the gross Sharpe needed.
- [ ] At most 3 variants, one brick each, expected effect written. No parameter is both a variant and a stress test.
- [ ] Train, validation and test periods fixed.
- [ ] At most three kill criteria, each a kind the Kill Policy lists (evidence against).
- [ ] Power of each gate stated on the sample where it applies.
- [ ] One condition per kill criterion; none true by construction; each able to fire.
- [ ] Turnover a central estimate, gross book derived from the volatility target.
- [ ] 1500 words at most.
- [ ] No long dash.
