# Rules of the verdict

## Kill

Any kill criterion of 1.11 that fails, on the period and the version 1.11 names, kills, if it is evidence against (`vault/Toolbox/Kill Policy.md`). No exception, no "almost". A criterion that fails only for lack of evidence (a control or prediction with the right sign and a t under 2) does not kill: write it as a label at the top of Pass 2 ("premium, alpha over <control> not shown, t 1.7"). A criterion computed with an input Pass 1 says to replace (the measured turnover) uses the measured value.

## Candidate for the test

All kill criteria pass. Then the verdict is still qualified by the predictions and the controls, in this order of weight:

1. **A prediction said to separate the mechanism from its rival is contradicted** (wrong sign, t at or below -1): **inconclusive**, with the question for the Economist (a rewrite of the mechanism counts as a try). Not shown (right sign, t under 2): a label, candidate for the test.
2. **A control collapses**: the one-day delay takes away most of the P&L, or the survivorship control changes the sign. Say what it means: a very fast effect (then the weekly mechanism of Pass 1 is not what pays), a leak (then the Red team must find it before any test), or a universe effect.
3. **The P&L is not what the mechanism says**: the split of P&L (price, carry or funding, costs) by period. A carry strategy whose P&L is price in one period is two strategies, and only one was written.
4. **Read-only predictions** that fail lower confidence; they are reported, they do not block.

## Controls

Controls are labels unless they contradict (Kill Policy). A twin that beats the base by a difference t of 1 or more: verdict **inconclusive**, the twin goes to the Economist as the new candidate (one try).

## Luck

- Tries: base plus the variants Pass 1 counted, plus every change decided on a result (changelog, Research Log). Stress tests and controls are not tries.
- Luck line: `budget.py --tries N --years T` on the period of the gate. Report Sharpe minus luck line.
- With correlated tries, the luck line with the effective number N_eff = N / (1 + (N - 1) x rho), rho from the variants' return correlation; give both.

## After the test: three zones (from the strategy sheet template)

With the test mean against the train-plus-validation mean of the version frozen for the test:
- **confirms**: test mean above half the earlier mean → keep, paper trading at half weight;
- **ambiguous**: between minus half and plus half → keep on paper only, no money, wait for data;
- **contradicts**: below minus half, with a test t-stat under -1.5 → kill.

Losing half the edge out of sample is normal; a reversed sign with a significant t is not.

## After the test: the full-sample t-stat

The train gate of a short train only asks for a t of 1; the proof is here. Compute the net t-stat (Newey-West) of the frozen version on train, validation and test stitched together:
- **2 or more**: the edge is shown on the whole sample; the zone above decides paper at half weight or paper only.
- **under 2**: not shown; paper only, no money, whatever the zone. Say it in one line with the t.
The kill of the "contradicts" zone stays.
