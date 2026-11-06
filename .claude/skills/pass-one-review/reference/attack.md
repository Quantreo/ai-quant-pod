# What to attack

A Pass 1 is a promise: if this test is run, its result will mean something. The critic looks for every way the result could mislead, before money is spent writing code.

## Severity

- **blocking**: the test cannot give an honest answer as designed. Look-ahead in the design; a key prediction that cannot be measured or that the rival explanation also passes; data the desk does not have.
- **major**: weakens the conclusion. A kill criterion that kills on absence of evidence (a control's t under 2 with the right sign), against `vault/Toolbox/Kill Policy.md`; a known factor named in "what it could secretly be" with no control (add it as a diagnostic, a label, not a kill); A figure misquoted; a choice with no basis; a free number not in 1.5b; a missing instrument trap; a kill criterion too soft to ever fire; a gate whose power is not stated; a turnover not computed with `budget.py`.
- **minor**: clarity, wording, a small inconsistency. Three at most.

An estimate the sheet itself says will be replaced by a measurement (turnover before the first run) is major only if a choice is missing behind it (a leverage cap), not for the estimate itself.

## Checks

**1. Fidelity**
- Every `[source]` claim says what the note says, at that page. A `[hypothesis]` is not dressed as a source.
- Every figure comes from a note or from `budget.py`; re-run the script with the sheet's inputs.

**2. Mechanism**
- The questions of its type (`.claude/skills/pass-one/reference/mechanisms.md`) are all answered.
- The **strongest rival explanation**: what else could produce the same backtest (beta, short volatility, carry, momentum, liquidity, a trend in the sample)? At least one prediction must come out differently under the rival. A prediction true under both decides nothing; a prediction partly true by construction (more dispersion, more funding collected) decides nothing either.
- Support the rival fairly: cite what the notes say against it too, and do not stretch a figure beyond the asset class or period it comes from.
- A combined condition can hide a redundant part: if "A and B" and B implies A, A tests nothing.

**3. Design**
- Every row of 1.5 has a basis; every number in the sheet is in 1.5b or follows from another choice. Look for the choices nobody wrote: timing against payments or prints, estimators, caps on leverage or inputs, minimum number of names.
- No parameter is both a variant and a stress test. At most 3 variants, one brick each.
- Instrument traps that apply and are missing (check `vault/Toolbox/Instrument Traps.md`; funding timing, delistings, survivorship, rollover, bid/ask at the trade time, look-ahead in a filter or a multiplier). A risk that is measured but never charged to the P&L (a liquidation, a margin call) is still missing.
- Cost budget: turnover computed and explained, cost from `vault/Toolbox/Cost Assumptions.md` or marked to confirm, tail of the universe. The gross book follows from the volatility target and the spread's volatility; a turnover built on an assumed gross (2x) with a vol target that implies 1x is off by half, and with strict gates a pessimistic estimate kills on paper.
- **Controls**: a control must not contain the effect being tested (a momentum book that itself earns funding cannot control a funding strategy: use its price-only returns). Every factor named in "what it could secretly be" has its control, read as a label unless it contradicts.

**4. Test plan and kill criterion**
- Train, validation and test fixed in advance; "Data already seen" honest about what the desk has already used. No criterion computed on a sample that includes the test period before the end.
- At most three kill criteria (Kill Policy), measurable, written before, the key prediction first. A criterion that cannot fire is not a criterion: check it against the archived sheets when one exists. A redundant threshold (0.3 when the luck line is 0.42) is noise. A t-stat or a threshold is given wherever a sign alone is asked.
- **Power of each gate, on the sample where it applies**: compute the chance that a strategy with a plausible true Sharpe passes (standard error of an annual Sharpe about 1/sqrt(years)). If the sheet does not state it, that is major. The fix is to state it, never to lower the bar: the desk keeps strict gates (`.claude/skills/pass-one/reference/method.md`, 1.11).
- **One condition per criterion**: "A and B" is two criteria, each with its own power.
- **Inert checks**: a rule that needs an extreme event to fire in this design (a liquidation threshold at a 90% loss under a 2x gross book) is not a check. A condition true by construction tests nothing.
- **Escape hatches**: any "if X, we will change Y" in the sheet is a future try. It must be counted in the luck line now, or removed.

**5. Feasibility**
- The data exists in `vault/Toolbox/Data Sources.md`, over the period planned, with enough names in the early years.
- Every leg is tradable, the short side included.

## Writing objections

- **One objection, one fix.** If a point needs two fixes, it is two objections.
- A gap caused only by a rule newer than the sheet (a section the template did not have) is one minor line, not a major.
- **Design flaw or spec gap?** An objection says the test could mislead (a missing control, a gate that cannot fire). A spec gap says the Developer will not know what to code (ties in ranks, margin reset inside the band, an estimator for names with a short history). Spec gaps go in their own list: they matter, but they do not weigh on the recommendation.
- **A prediction with no consequence**: every prediction says what its failure does. If none, that is an objection.

## Good and bad objections

- Good: "1.1, P3: 'dispersion of funding' has no definition; the Diagnostic cannot measure it. Define it (e.g. cross-sectional standard deviation of 7-day funding)." major.
- Good: "1.11, criterion 1: a gross Sharpe above 0.98 already implies funding plus price above zero, so the first condition tests nothing, and a P&L made only of price passes. Require the funding component to carry most of the gross P&L." blocking.
- Good: "1.7: 'if turnover is too high, slow the signal' is a future try; count it now (5 tries, luck line rises) or drop it." major.
- Bad: "The mechanism seems weak." No section, no fact, nothing to fix.
- Bad: "Why not test 25 names too?" The universe size is already a stress test: nitpicking.
- Bad: "Lower the gate to 0.6 to raise the power." Against the house rule.

See `example-round-1.md` for a full round with the desk's verdict on each objection.
