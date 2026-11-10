# ETF TSMOM 12-Month · Pass 1

**Verdict: Go.** A payer is named in two sources and K2 can show the rival. The train gate passed on level (monthly net Sharpe 0.626, t 2.16, bar 0.579). The alpha over the always-long book is not shown on train (t 1.83): a label, not a kill. The base is unchanged since the gate.

**Stage: full**, v2.

---

## 1.1 Mechanism

**Type**: behavioural bias, with a liquidity premium on commodities.

**Who pays.** Investors who under-react to news, then chase it once the move is visible [source: Moskowitz 2012, p. 245, 248-249; Lempérière 2014, p. 13-14]. In commodities, hedgers who pay speculators for liquidity, through the roll [source: Moskowitz 2012, p. 246, "one explanation might be"].

**What the sources show.** On 58 futures, the sign of the past 12-month excess return predicts the next month in every contract, 1985-2009, gross (Moskowitz 2012, p. 236). Trend has earned a Sharpe of 0.72 since 1800 across four sectors, gross (Lempérière 2014, Fig. 4). Same rule on 22 ETFs instead of futures [own construction].

**Why it is not arbitraged away.** Losses at turning points (Moskowitz 2012, p. 238) and drawdowns of years (Lempérière 2014, p. 11) deter capital [hypothesis].

**What it could secretly be.** A long equity and long duration book in a sample where both rose (2009 to 2020). K2 tests it.

**Predictions, to be checked by the Diagnostic.**
- **P1** (key): net alpha over the always-long control with the same sizing. Label if t under 2 with a positive sign; kill only if K1 or K2 fires.
- **P2**: the profit comes mostly from persistence, not from the mean return, except in bonds [source: Moskowitz 2012, Table 5B]. Read only.
- **P3**: positive loading on the squared SPY excess return (straddle shape) [source: Moskowitz 2012, Table 3C]. Read only.

## 1.2 Sources and crowding

[[2012 - Moskowitz Ooi Pedersen - Time Series Momentum]]: 12/1 is the best cell (t 6.61, Table 2A), chosen on the same sample (p. 236); alpha over always-long is positive in 90% of contracts but significant in only 26% (p. 236). [[2014 - Lempérière Deremble Seager et al - Two centuries of trend following]]: flat since 2011 (Fig. 6), crowding only argued (p. 14). Crowded: managed futures load 0.55 on it (Moskowitz 2012, Table 5C).

## 1.3 Expected behaviour

Works in long trends (2008); loses at reversals (2009) and in choppy years (Lempérière 2014). Best quarters with the largest S&P moves either way (Moskowitz 2012, Fig. 4).

## 1.4 Universe

The 23 core ETFs of `etf_daily` minus SHY (near cash: 1/sigma would lever it), 22 ETFs: equities 9 (SPY QQQ IWM EFA EEM EWJ VGK FXI VNQ), bonds 5 (TLT IEF LQD HYG TIP), commodities 5 (GLD SLV DBC USO DBA), FX 3 (UUP FXE FXY). An ETF enters after 12 months of history. The list is 22 survivors picked in 2026 [hypothesis: tilted]; read-only stresses on the 13 alive in 2005 (stress13) and the 9 launched later (stress9). Results are "conditional on the 2026 list".

## 1.5 Base version, brick by brick

| Brick | Choice | Why | Basis | Card |
| --- | --- | --- | --- | --- |
| Return | adj_close minus T-bill | dividends in, excess return | source (p. 236) | [[ETF daily]], [[T-bill rate]] |
| Signal | sign of the 12-month excess return, month end, no skip | published rule | source (Eq. 5) | [[Time-series momentum signal]] |
| Sizing | 1/sigma, EWMA com 60 days | equal risk per ETF | source (p. 233) | |
| Book | 8% ex-ante vol (261-day covariance), gross cap 2 | a book under the cap most months | scale, convention (Reg T) | |
| Rebalance | monthly, last close | source horizon; closing auction | source (p. 233), cost | |
| Costs | 2 bp: SPY QQQ IWM EFA EEM TLT IEF LQD HYG GLD; 5 bp: the other 12 | Cost Assumptions | cost | |
| Borrow | 25 bp a year on short gross, all ETFs | Cost Assumptions | cost | |

## 1.5b Free parameters

| Parameter | Value | Why this value | Tested as |
| --- | --- | --- | --- |
| Vol target | 8% | gross under the cap most months | scale |
| Risk split | equal per ETF | published rule | variant A |
| Costs | 2 / 5 bp | Cost Assumptions | stress 2x |
| Borrow | 25 bp | Cost Assumptions | stress 1% |
| Controls | always-long: base sizing, target, cap, costs, signs +1; twin: every ETF takes the sign of the 1/sigma basket's 12-month excess return; both on the names alive at each month end | Data check #2 | labels |
| Newey-West lags (R1) | 4 on the pooled 179 months (floor of 4 x (n/100)^(2/9)) | standard rule | follows |
| Delay stress (R1) | signal at close d, trade at close d+1 | Data check #5 | stress |

## 1.6 Horizon, trades and statistical power

One-month holding. Train 143 scored months (11.92 years); pooled 179 months (14.92 years).

**Tries** (budget.py): family trend · multi-asset had no try before; the base is 1 try (luck line 0.00 over 11.92 years). Variant A makes 2: luck line 0.13 over 14.92 years.

**Gate figure: monthly**, fixed in 1.11 before the run (v1). **Known fragility (R1)**: the daily engine gives net Sharpe 0.541, t 1.87, under the bar. Both are reported at every phase; monthly decides, it is the signal and holding horizon.

**Data already seen**: the train result of the base and of both controls (Build). The author ran a version of this idea on the same ETFs on another desk, over 2006-2020 (R1): train and validation are not fresh to the human. The sealed test from 2021 is fresh to the pod and is the clean out-of-sample of this sheet; paper trading is the next one.

## 1.7 Cost and capacity budget

Estimate in v1: 5.4x a year at 3.6 bp, 0.19% a year. Measured: 6.7x; costs and borrow 0.37% a year. Gross Sharpe needed to keep costs under half the edge: 0.06 (budget.py), measured gross 0.588. Break-even 71.6 bp. Capacity not binding: thinnest median dollar volume FXY 18m a day.

## 1.8 Instrument traps

| Trap | Here | Accounting |
| --- | --- | --- |
| Dividends | equity, bond ETFs | adj_close |
| Futures roll | USO, DBC, DBA | inside the ETF price; reported alone |
| Survivorship | list picked in 2026 | stress13, stress9 (read only) |
| FX ETFs | FXE, FXY earn foreign deposits | excess over T-bill |

## 1.9 Variants (written before validation)

| # | Brick | Change | Why | Expected effect |
| --- | --- | --- | --- | --- |
| A | Book | equal risk per class (4 x 25%), 1/sigma within | equities hold 9 of 22 slots: the rival of 1.1 | beta to SPY falls, K2 alpha rises; replaces the base only if its pooled net Sharpe and K2 alpha are both higher |

One try. Stresses (not tries; net Sharpe must stay above 0): costs 2x, borrow 1%, delay 1 day.

## 1.10 Test plan

Train 2006-01 to 2017-12 (scored from 2006-02), validation 2018-2020, test from 2021-01-01 (sealed). Pooled: 2006-02 to 2020-12, 14.92 years, monthly, NW 4 lags.

| Diagnostic | Checks | Sample |
| --- | --- | --- |
| Validation net mean t; pooled net Sharpe | K1 | validation, pooled |
| Alpha on SPY and TLT monthly excess, two regressors (R1); 50/50 basket and 2008-09 dropped read only | K2, rival | pooled |
| Net P&L by ETF | K3 | pooled |
| Alpha on always-long, on the twin | P1, labels | pooled |
| Auto-covariance vs mean squared; SPY excess and its square | P2, P3 | pooled |
| stress13, stress9, costs 2x, borrow 1%, delay 1 day | stresses | pooled |
| Daily and monthly Sharpe | fragility | pooled |

## 1.11 Kill criterion (backtest)

**Train gate (v1)**: level only. Monthly net Sharpe at least 0.579 (t 2 over 11.92 years) and above the luck line 0.00 plus cost. No control at the gate: alpha t 2 on train has under 50% power at a plausible edge, so the two controls are labels. **Result: pass** (0.626, t 2.16).

**Validation criteria (Kill Policy), ranked:**

| # | Kind | Criterion: kill if | Power, false kill |
| --- | --- | --- | --- |
| K1 | level | validation net mean t at or below -1, or pooled net Sharpe under the luck line 0.13 | false kill at Sharpe 0.5: 3% |
| K2 | control contradicts | alpha on SPY and TLT excess (two regressors, NW 4) at t at or below -1, pooled (R1) | false kill at IR 0.3: 1.5%; fires 16% at zero alpha |
| K3 | construction | pooled net P&L negative without the two ETFs with the largest positive net P&L (R1) | train: SPY plus DBC 12.8 of 52.6 |

**Labels, never kills**: alpha over always-long (train t 1.83), over the twin (1.48), P2, P3, stresses, stress13 and stress9.

**After the test**: three zones on the test mean against the pooled mean of the frozen version. Money needs the net t of train, validation and test together at 2 or more; otherwise paper only.
