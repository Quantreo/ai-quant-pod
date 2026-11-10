## Pass 2

**Verdict: candidate for the test** · 2026-11-09 · runs read: 20261109-103847, 103855, 103857, 103858, 103900, 103902, 103904, 103905, 103907, 103939 · lab 70e86da018e5

No kill criterion fires, but the edge is thin and not shown. The last three years lost money (validation monthly net Sharpe -0.35, t -0.60). Pooled monthly net Sharpe is 0.467 (t 1.80, daily 0.409, t 1.58), under t 2. The shorts lose: price short -25.9%, long +85.6% (offset by +11.6% short funding). Labels: alpha over always-long not shown (t 1.69); alpha over the twin not shown (t 1.67); full report [[ETF TSMOM 12-Month - Backtest report]].

### Kill criteria (1.11)

| # | Criterion | Threshold | Measured | Pass |
| --- | --- | --- | --- | --- |
| K1a | validation net mean t | at or below -1 kills | -0.60 (35 months) | pass |
| K1b | pooled net Sharpe (monthly) | under luck line 0.13 kills | 0.467 | pass |
| K2 | alpha on SPY and TLT excess, NW 4, pooled | t at or below -1 kills | alpha 2.9%/yr, t +1.51; betas SPY -0.01 (t -0.16), TLT 0.08 (t 1.27) | pass |
| K3 | pooled net P&L without top 2 ETFs | negative kills | total 0.494, without SPY and QQQ 0.365 | pass |

K2 read-only: train alone t 1.93; dropping 2008-09 to 2009-12 alpha t 0.78 (1.4%/yr). The alpha leans on the 2008 crisis.

### Predictions (1.1)

| P | Prediction | Separates from the rival? | Measured | Confirmed |
| --- | --- | --- | --- | --- |
| P1 | net alpha over always-long | yes (key) | t 1.69 (3.2%/yr); beta on long 0.04. Over the twin t 1.67, twin beta 0.31 (t 3.2) | right sign, t under 2: label, not shown |
| P2 | persistence, not mean return | no | not computed (no auto-covariance table built) | not measurable |
| P3 | positive loading on SPY excess squared | no | +0.13, t 0.24; SPY beta -0.03 | right sign, not significant |

The rival (a long equity and duration book) is not supported: SPY beta is about 0. But always-long alone has monthly Sharpe 0.379, and base minus A pooled difference t is 0.45.

### Luck

Tries 2 (base, A; N_eff 1.0 on the desk file, rho 0.94), years 14.92, luck line 0.13 (desk file: -0.16 for trend multi-asset). Pooled gross daily Sharpe 0.457; monthly net 0.467 minus 0.13 = +0.34. Above the line, but the t is 1.80.

### Controls

| Control | Base | Control | Reading |
| --- | --- | --- | --- |
| One-day delay (103939) | monthly 0.467, daily 0.409 | monthly 0.397, daily 0.349 | keeps 85%: no collapse, no leak sign |
| Survivorship stress13 | 0.467 | 0.508 | same sign, not worse |
| Survivorship stress9 (168 m) | 0.467 | 0.216 (daily t 0.79) | halves, sign kept; top 5 names 116% of P&L (DBC, FXY, HYG) |
| Costs 2x / borrow 1% | 0.467 | 0.433 / 0.403 | stay above 0 |
| Always-long / twin | 0.467 | 0.379 / 0.137 | base beats both; twin is weak |
| Variant A (try 2) | 0.467 | 0.415 | lower: does not replace the base |

### P&L by period and by leg

Price 59.7%, funding -4.5%, costs -5.8%, borrow in costs. Years negative: 2009, 2011, 2016, 2018, 2020 (-0.06). Worst: 2016 -1.42 Sharpe. Legs: long price +85.6, short price -25.9. Top 5 names 50% of P&L (SPY, QQQ, IEF, GLD, DBC); UUP -3.8%. The P&L is price, as the mechanism says, but the short side does not pay.

### For the next seat

- Red team: (1) the code sha: Build says 56ac41f76375, but runs 103847 to 107 carry ed3a686172a3 (only 103939 carries 56ac); confirm the base weights are identical. (2) Why shorts lose, and whether the long-only part is only the equity and gold drift of 2006-2020. (3) Reliance on 2008. (4) The 2018-2020 decay.
- Lab owner: `lab.checks.delay_test` shifts calendar days (weekend weights).
- Method: the train t of 2.16 became 1.80 pooled; the full-sample t after the test decides money (t 2 needed).
