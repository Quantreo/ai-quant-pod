## Review

### Round 1 · 2026-11-09 · Critic: revise

**Strongest rival explanation**: the book is long equities and long duration most of 2009 to 2020, a sample where both rose; the trend sign adds little beyond holding them. Separating prediction: alpha on SPY and TLT excess returns (K2) stays positive; under the rival it is zero or negative.

| # | Section | Objection | Severity | Evidence | Fix asked | Economist's answer | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.11 K2 | "Alpha on SPY plus TLT buy-and-hold" has two readings: two regressors, or one 50/50 basket. They give different alphas, and the reading could be picked after the result | major | Pass 1 v1.1, 1.10 and 1.11 | Fix one regression before validation | Two regressors, SPY and TLT monthly excess, NW 4 lags; the 50/50 basket is read only (1.10, 1.11) | fixed |
| 2 | 1.6, 1.11 | The gate passes on monthly returns (t 2.16) but the daily engine gives t 1.87, under the bar. A gate that passes on one frequency only needs the frequency fixed before the run | major | Build: daily net 0.541, t 1.87 | Show the frequency was fixed before the run; name the gap as a fragility | Monthly was fixed in 1.11 of v1, before the run (Changelog v1). 1.6 names the daily figure as a known fragility; both reported at every phase | fixed |
| 3 | 1.4, 1.8 | The 22 ETFs are survivors picked in 2026. Funds that died, which a trend book would have shorted, are missing; the labels and K2 lean on a list of winners | major | Data check #3 | A point-in-time ETF list, or stresses that bound the effect | No point-in-time ETF list on the machine (Data check #3). stress13 and stress9 read only, and every result is "conditional on the 2026 list" (1.4) | partly fixed |
| 4 | 1.11 K3 | "Best two ETFs" is not defined: price or net P&L, train or pooled | minor | Pass 1 v1.1, 1.11 | Define it | The two ETFs with the largest positive net P&L, pooled (1.11) | fixed |
| 5 | 1.6 | "Data already seen" names the author's earlier work but not its effect: validation 2018-2020 is not fresh to the human who will read it | minor | Pass 1 v1.1, 1.6 | Say what is fresh and what is not | Sentence added: train and validation not fresh to the human; the sealed test is the clean out-of-sample of this sheet (1.6) | fixed |

**Spec gaps** (the Economist settles each in one line, in 1.5b): Newey-West lags on the pooled sample; definition of the delay stress.
