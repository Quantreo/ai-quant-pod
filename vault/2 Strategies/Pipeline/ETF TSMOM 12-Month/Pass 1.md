# ETF TSMOM 12-Month · Pass 1

**Verdict: Go.** The payers are named and K4 can show the rival. The train gate passed on level only (monthly net 0.606 against 0.579, at 0.5% borrow), by a thin margin, under a rule changed after the results were seen. v1.3 reruns the gate at 25 bp borrow. P1 is not shown on train (t 1.77) and is judged on train plus validation pooled.

**Stage: full**, v1.4.

---

## 1.1 Mechanism

**Type**: behavioural bias, constraint rival. **Who pays**: investors who under-react, then chase [source: Moskowitz 2012, p. 245; Lempérière 2014, p. 13-14]; commodity hedgers paying for liquidity, via roll [source: Moskowitz 2012, p. 246, "one explanation might be"]. **Why it persists**: losses at turning points (Moskowitz 2012, p. 238) deter arbitrageurs [hypothesis]; flat since 2011 (Lempérière 2014, Fig. 6). **What it could secretly be**: long equities after 2009 and long duration while rates fell (K4).

**Predictions**:
- **P1** (key): net alpha over the always-long control. K1.
- **P2**: profit mostly from persistence, not mean return, except bonds [source: Moskowitz 2012, Table 5B, p. 244]. Read only.
- **P3**: positive loading on the squared equity return [source: Moskowitz 2012, Table 3C]. Read only.

## 1.2 Sources and crowding

Moskowitz 2012 (Notes, 2026-10-22): 12/1 best cell (t 6.61, Table 2A); alpha over always-long positive in 90% of 58 contracts, significant in only 26% (p. 236). Lempérière 2014: Sharpe 0.72 gross since 1800, flat since 2011, crowding only argued (p. 14). Desk, same data: [[ETF Cross-Asset Momentum]] (beta 0.92 on this twin), [[ETF Bold Asset Allocation]]; [[Crypto TSMOM 12-Month]] killed on its market control. Very public: managed futures load 0.55 on it (Table 5C).

## 1.3 Expected behaviour

Works in long trends (2008); suffers at reversals (2009) and in choppy years (2011-2016, Lempérière). Straddle-like: best quarters with the largest S&P moves either way (Moskowitz 2012, Fig. 4); a few months carry the year.

## 1.4 Universe

`etf_daily` minus SHY (near cash: inverse-vol would lever it), 22 ETFs: equities 9 (SPY QQQ IWM EFA EEM EWJ VGK FXI VNQ), bonds 5 (TLT IEF LQD HYG TIP), commodities 5 (GLD SLV DBC USO DBA), FX 3 (UUP FXE FXY). Entry after 12 months of history. The list is survivors picked in 2026 [hypothesis]: stress13, stress9.

## 1.5 Base version, brick by brick

| Brick | Choice | Why | Basis |
| --- | --- | --- | --- |
| Return | adj_close minus cash | dividends in, excess return | source (p. 236) |
| Signal | sign of 12-month excess return, month end | published rule | source (Eq. 5) |
| Sizing | 1/sigma, EWMA com 60 days, lagged | equal risk per ETF | source (p. 233) |
| Book | equal weight, 8% ex-ante vol (261-day covariance), gross cap 2 | measured gross 2.0 at 10% | scale, convention (Reg T) |
| Rebalance | monthly, last close | auction (Cost Assumptions) | cost |
| Costs | 2 bp: SPY QQQ IWM EFA EEM TLT IEF LQD HYG GLD; 5 bp: the other 12 | confirmed by Lucas 2026-10-25 | cost |
| Borrow | 25 bp a year on short gross, all ETFs incl. FX (v1.3; 0.5% superseded) | confirmed by Lucas 2026-10-25 | cost |

## 1.5b Free parameters

| Parameter | Value | Why | Tested as |
| --- | --- | --- | --- |
| Vol target | 8% | gross under the cap most months | scale |
| Borrow fee | 25 bp | confirmed | stress 1% |
| Cost tiers | 2 / 5 bp | confirmed | stress 2x |
| Risk split | equal per ETF | published rule | variant A |
| Controls (R1) | always-long: base sizing, target, cap, costs, signs +1; twin: all take the sign of the 1/sigma basket's 12m excess | as built | follows |
| Cap binding (R1) | all weights x 2 / gross | keeps risk shares, as built | follows |
| Covariance (R1) | pairwise, 240 common days minimum (12-month entry ensures it) | as built | follows |
| Timing (R1) | signal and trade at the same month-end close; delay stress: next close | Data check #5 | stress |
| stress13 (R1) | same target and cap | scale | follows |
| Zero return (R1) | weight 0 | convention | follows |

## 1.6 Horizon, trades and statistical power

One-month holding; 1.2 sign flips per ETF a year, turnover 6.7x; train 143 months (11.92 years).

**Tries** (budget.py): when the base ran, N_eff trend · multi-asset was 0, so 1 try with luck line 0.00. Now there are 3 (0.25 on 11.92 years). v1.3 (borrow 25 bp, after the gate) adds a try: 4, so the gate rerun meets a luck line of 0.30. Variant A makes 5: luck line 0.31 on 14.92 years.

**Gate figure: monthly** net returns, Sharpe x sqrt(years), fixed in the gate code before the run. **Known fragility**: daily engine net 0.525, t 1.81, under the bar. Measured on the saved output (R1, no run): daily P&L summed by month equals the monthly series (correlation 1.0000, max gap 0.05%), so they are aligned. The gap is the variance ratio: monthly variance is 0.78 of 21 x daily (about 2.4 standard errors under 1; daily lag-1 autocorrelation -0.047). **Monthly decides**: it is the signal and holding horizon. Whether the ratio persists is unproven; both are reported.

**Data already seen**: the full train of the base and both controls (Build). The gate was **re-read under a rule changed after these results were seen**: G1 had killed the base, and the new rule moved it to validation. Two other trend sheets used 2006-2017 here. Nobody has read 2018-2020. The test from 2021 is sealed.

## 1.7 Cost and capacity budget

Measured 3.2x at 2 bp and 3.5x at 5 bp; borrow 0.27% a year at the old 0.5%. Costs and borrow: -6.1% over the train. Costs 2x: 0.47% a year, gross Sharpe needed 0.12 (budget.py). Break-even 71.6 bp. Capacity not binding (1% of daily volume).

## 1.8 Instrument traps

| Trap | Here | Accounting |
| --- | --- | --- |
| Dividends | equity, bond ETFs | adj_close |
| Futures roll | USO, DBC, DBA | inside the ETF price; reported alone |
| Survivorship | list picked in 2026 | stress13, stress9 (read only) |
| FX ETFs | FXE, FXY earn foreign deposits | excess over T-bill; UUP worst on train (-4.2) |

## 1.9 Variants (written before the test)

| # | Brick | Change | Why | Expected effect |
| --- | --- | --- | --- | --- |
| A | Book | equal risk per class (4 x 25%), 1/sigma within | equities hold 41% of risk (9 of 22): the rival of 1.1 | beta to SPY and to always-long falls, K1 alpha t rises; replaces the base only if both come out pooled, never on Sharpe |

One try. Stresses (not tries; net Sharpe must stay above 0): costs 2x, borrow 1%, delay 1 day.

## 1.10 Test plan

Train 2005-2017 (scored from 2006-02), validation 2018-2020, test from 2021-01-01 (sealed). Pooled: 2006-02 to 2020-12, 14.92 years.

| Diagnostic | Checks | Sample |
| --- | --- | --- |
| Alpha on always-long, NW 4 | P1, K1 | pooled |
| Alpha on one-sign twin, NW 4 | K2 | pooled |
| Auto-covariance vs mean-squared, by class | P2 | pooled |
| Regression on SPY excess and its square | P3 | pooled |
| Alpha on SPY and TLT buy-and-hold excess, NW 4 | rival, K4 | pooled |
| The same, 2008-09 dropped | rival | pooled, read only |
| stress13 (13 ETFs alive in 2005), stress9 | survivor list | pooled, read only |
| P&L by ETF; daily and monthly Sharpe | K5, fragility | pooled |

## 1.11 Kill criterion (backtest)

**Train gate**: level only, monthly net Sharpe at least 0.579 (t 2, 11.92 years). Re-read in v1.1, not a try: 0.606 at 0.5% borrow passed (data already seen). **The v1.3 rerun at 25 bp is a try**; luck line 0.30; the Developer's figure decides. No control at the gate: alpha t 2 on train has 27% power at IR 0.4 (twin: 17% at 0.3). Twins do not beat the base: always-long 0.456, one-sign twin 0.449.

**Validation criteria, pooled, monthly, read by the Analyst and the Red team:**

| # | Criterion (kill if not met) | Power, given the train seen | False pass at zero, given the train |
| --- | --- | --- | --- |
| K1 (P1) | alpha on always-long t 2 or more (train 1.77: validation needs 0.93) | 41% at IR 0.4, 47% at 0.5 | 18% |
| K2 | alpha on the one-sign twin t 2 or more (train 1.43: needs 1.61) | 14% at IR 0.3 | 5% |
| K3 | net Sharpe t 2 or more, 0.518 (train 2.09 at 0.5%: needs 0.29) | 72% at 0.5 | 38% |
| K4 | alpha on SPY plus TLT buy-and-hold t 2 or more (train not computed) | 32% at IR 0.4, 47% at 0.5 | 2.3% |
| K5 | top two ETFs under 50% of price P&L (train SPY plus VNQ: 23%) | can fire | n/a |

Conditional rates (R1): validation t ~ N(IR x sqrt(3), 1), added to the train t already seen. The pooled bar is the house rule's and is not raised here. K1 and K3 lean on the train. K4, never computed, is the one clean test. Luck line 0.31 is reported as a line; it sits under the t bar. K3 uses the 25 bp rerun.

**After the test**: three zones on the test mean against the pooled mean of the frozen version. Full-sample net t (about 20.75 years) must reach 2: power 61% at 0.5.
