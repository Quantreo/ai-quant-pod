# SPY Volatility Managed · Pass 1

**Verdict: Go to validation, on the level only.** The train level passes the 1.11 rule of 2026-10-25 (net Sharpe 0.770, t 2.66; [[Gate reread]]), but that rule was written after this result was seen, and the overlay itself is not shown (G1 t 1.38, G2 t -0.66; 1.06 with the 1-month twin). The library predicts it fails: single-asset market management loses out of sample net [source: DeMiguel 2024, Table I C, E].

**Stage: full** (completed after the train gate, before any validation run).

## 1.1 Mechanism

**Type**: behavioural (slow updating of volatility). **Who pays**: the investor who stays fully exposed through high-variance months [hypothesis; source calls it speculative, Moreira Muir 2016, p. 24-25]. **Not arbitraged**: it cuts exposure when risk capital is scarce [hypothesis]. **Could secretly be**: a lower-beta SPY (the alpha regression removes it); one crash avoided, 2008; trend timing: the leverage effect lines the weight up with a trend position [source: Hood Raughtigan 2024, Exhibit 4, p. 10-12]: a 12-month rule absorbs 39% of the market alpha, a 1-month rule 21% (91% and 10% on 2000-2023 equities) [same, Exhibit C.1, C.2]; our book loads 0.39 on the 12-month twin; full-sample c [Moreira Muir, fn 5], with real-time failure reported [literature, not in library: Cederburg O'Doherty Wang Yan 2020].

- **P1** (key): net alpha over SPY, the 12-month and the 1-month SPY trend twins is positive (rival: a short-horizon trend bet in a bull sample). Fails: kill (V1).
- **P2** (one event): the alpha survives without 2008-09 and the 3 best months. Fails: kill (V2).
- **P3** (premise): next-month mean over variance falls from low to high tercile of lagged variance [Moreira Muir, Fig. 1]. Read only; if it fails on pooled data, variant 1 is not run (it would test a premise already refuted).

## 1.2 Sources and crowding

| Note | What it gives here |
| --- | --- |
| Moreira Muir 2016 | rule, c, cap, appraisal 0.33 gross (Table 2A, 5A) |
| Harvey et al. 2018 | US equities Sharpe 0.40 to 0.48-0.51, 1927-2017 (Table 3, p. 8), none in 1957-1987 (Fig. 4, 10); momentum explains 45% to 60% of gains (p. 19-21) |
| Hood Raughtigan 2024 | market alpha 3.07%/yr falls to 1.25% (t 1.3) with their simple trend rule, 59% (Exhibit 4); 12-month rule 39%, 1-month 21% (Exhibit C.1); 2000-2023 equity alpha t 1.0, 0.5 after trend (Exhibit 8); in-sample only |
| DeMiguel 2024 | out of sample the managed market trails the market: 0.408 vs 0.530 gross, 0.433 vs 0.519 net (Table I C, E); single factors fail net |

Very public; vol-target funds run it. Desk lesson 2026-10-25: the trend twin is the right control.

## 1.3 Expected behaviour

Works in calm rising markets (cap 1.5x in 105 of 143 train months) and in a falling spike (2008). Suffers in V-shaped rebounds (2009-03, 2020-04) and in crashes from calm (levered: 2018-02, 2020-02). Payoff: SPY-like; few months carry the gap (G2 dropped 2011-09, 2012-06, 2016-03). Validation holds one event, 2020-03.

## 1.4 Universe

SPY: the source's market factor, the most liquid ETF.

## 1.5 Base version

| Brick | Choice | Basis |
| --- | --- | --- |
| Signal | RV² of daily `adj_close` returns in month m, no demeaning | source, Eq. 2 |
| Sizing | w = min(c / RV², 1.5), rest in T-bills; at the cap 0.5 borrowed | source, Table 5A; Reg T |
| c | train only, managed gross vol = SPY train vol (0.00370) | source, fn 5 |
| Execution | first close of month m+1; each month first close to first close | convention |
| Cash | TB3MS of m-1, rate/1200 a month; borrow on (w-1)+ at T-bill + 50 bp | data lesson; Data check 3 |
| Evaluation | net excess on SPY excess, the SPY 12-month and 1-month sign twins, Newey-West, 4 lags (floor(4(n/100)^(2/9))) | [[Always-long benchmark comparison]], [[Time-series momentum signal]] |

## 1.5b Free parameters

| Parameter | Value | Why | Tested as |
| --- | --- | --- | --- |
| Lookback | 1 month | source | variant 1 |
| Cap | 1.5 | source, Reg T | stress: 1 |
| c | vol-matched | source | stress: 10% target |
| Borrow spread | 50 bp | no source (a margin loan rate; the confirmed 25 bp/yr short borrow is a share-lending fee, another quantity) | stress: 100 and 150 bp |
| Cost | 2 bp | Cost Assumptions, confirmed | stress: 4 bp (2x rule) |
| Twins | sign of SPY excess over 12 and over 1 month, +-1, unscaled, same timing as the base, no cost | Build; [[Time-series momentum signal]]; Critic round 1 | follows from P1 |

Spec gaps (round 1): 143 of 155 months as the 12-month twin needs 12 months, same 143 for the 1-month twin; fixed shares within the month (Build), so 0.770 vs 0.648 is sampling; no RV² floor, the cap bounds w; c fitted with the cap (Build).

## 1.6 Horizon, trades and statistical power

Monthly; 143 train months, 179 pooled (2006-02 to 2020-12). Tries: low-vol · equities history 0 + base + variant 1 = **2**; luck line 0.15 over 11.92 years, 0.13 over 14.92 (budget.py).

| Criterion | Sample | Power at 0.33 / 0.2 appraisal (level: 0.43) | False pass |
| --- | --- | --- | --- |
| Level (passed) | train 11.92 yr | 30% at Sharpe 0.43 | 2.3% |
| V1 (three regressors) | pooled 14.92 yr | 20% at 0.3 (1-month trend takes about 10%, Hood C.2) | 2.3% |
| V2 | pooled 12.67 yr | 18% at 0.3 | 2.3% |
| Final proof, alpha | about 20 yr (test end unknown) | 26% at 0.3 | 2.3% |
| Level, all periods (house) | about 20 yr | 47% at Sharpe 0.43 | 2.3% |
| Zone 3 on alpha | test about 5 yr | fires 6.7% of the time at zero alpha (t < -1.5) | |

**Gate frequency**: the gate figure is the monthly Sharpe (as 1.5 scores months). The engine's daily Sharpe of the same P&L is 0.648 (t 2.33): a known fragility. Both are reported; the less favourable decides by default.

**Data already seen**: SPY 2005-2017 read by three ETF sheets; this base's train run read in full (net Sharpe 0.770 monthly, SPY 0.518, twin 0.459, G1 t 1.38, G2 t -0.66, SPY-only alpha t 1.79; with the 1-month twin, alpha t 1.06, approximate, saved monthly file). The gate failed, then passed on a re-read under a rule changed after these results, whose diagnostic cites this sheet: not clean evidence. The first clean sample is the test, then paper trading.

## 1.7 Cost and capacity budget

Measured turnover 1.98x/yr (Pass 1 estimate 3.96x). SPY 2 bp confirmed: 0.04%/yr; stress 4 bp: 0.08%/yr. Borrow drag 0.20%/yr at 50 bp, unsourced, stresses 100 and 150 bp (train t 1.27 on G1 at 100 bp). Gross Sharpe needed for costs under half the edge: 0.02. Capacity: no limit.

## 1.8 Instrument traps

| Trap | How the P&L handles it |
| --- | --- |
| Dividends | `adj_close` for RV² and returns: total return |
| Leverage | SPY_LEV leg pays T-bill + spread on (w-1)+ |
| 2008-10-13 print | both readings, less favourable decides |

## 1.9 Variants (written before validation)

| # | Brick | Change | Why | Expected effect |
| --- | --- | --- | --- | --- |
| 1 | Signal | RV² over 3 months, c refit on train | P3 premise: if the gain is short-horizon volatility clustering, a slower estimate times worse | lower V1 alpha and higher 12-month twin beta: supports volatility timing. V1 alpha equal or higher: the 1-month window is not what earns, confidence in P3 down |

Variant 1 is a read, never a replacement. Stresses (not tries, read only, reported on the level and V1 for the Analyst and the Red team): cost 4 bp, borrow 100 and 150 bp, cap 1, 10% vol target, one-day delay.

## 1.10 Test plan

Train 2005-2017 (done), validation 2018-2020, test from 2021-01-01 (sealed).

| Diagnostic | Checks | Period |
| --- | --- | --- |
| Alpha on SPY + both twins, NW | P1 (V1); final proof | pooled; all three |
| Same minus 2008-09 and 3 best signed residuals of the pooled fit, refit | P2 (V2) | pooled |
| SPY-only alpha | lower-beta SPY | pooled, read only |
| Next-month mean / variance by tercile of lagged variance | P3 | train, then pooled |
| Months at the cap, w in 2020 | leverage into a crash | validation |
| Correlation with ETF TSMOM 12-Month and the Bold AA twin, monthly | same bet | pooled |

**For the book**: the three are equity timing on one SPY window (one crash on train, one in validation). If correlated, the PM counts them as one risk unit at half weight, and their validations as one observation.

## 1.11 Kill criteria

1. **Level (train, passed)**: net Sharpe above luck line plus cost, t ≥ 2, monthly; daily 0.648 (t 2.33) reported, less favourable decides.
2. **V1 (key, P1)**: pooled alpha over SPY and both twins (one regression), NW t ≥ 2. Power 20% at 0.3. Fails: kill.
3. **V2 (P2)**: V1's regression without 2008-09 and 3 best, t ≥ 2. Power 18%. Fails: kill.
4. **Final proof**: alpha over SPY and both twins, NW t ≥ 2 on train plus validation plus test, or paper only whatever the zone. Power 26% at 0.3. The house net level t ≥ 2 on all three (power 47%) is applied too, as a floor.
5. **Test zones**, on the monthly alpha of criterion 4: test mean against train plus validation mean: above half confirms (paper at half weight); between minus and plus half is ambiguous (paper only); below minus half with test t under -1.5 contradicts: kill (house rule; fires 6.7% at zero alpha: it catches a reversed sign, criterion 4 catches no edge).

Kill 2 rule as on train: residuals of V1's fit, drop 2008 and 2009, 3 largest signed, earlier month on ties, refit.
