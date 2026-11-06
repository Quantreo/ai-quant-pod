# Operators

An idea is not a random mix of bricks. Each one comes from one operator, and the operator's question must be answered in the entry.

| Operator | What it does | Question to answer | Example from the library |
| --- | --- | --- | --- |
| **transpose** | Move a mechanism to another market or instrument | Does the same payer exist there, for the same reason? | Pre-FOMC drift to the ECB and the BoE |
| **swap** | Replace one brick of a strategy with a card from another source | Which known weakness of the strategy does the new brick fix? | Add the No-trade band to time-series momentum, to cut trading on small signal changes |
| **condition** | Trade a strategy only in a state another source identifies | Does the condition rest on a mechanism, or on a fitted threshold? | Stand aside from crypto momentum when the trade is crowded (Momentum crowding filter) |
| **test a claim** | Test a claim a paper states without showing evidence | Do we have the data to test it? | Moskowitz 2012 says the effect holds on emerging market currencies, "not reported" |
| **fix a weakness** | Build the version that removes a weakness a paper documents | What is left of the edge once the weakness is removed? | Bond trend profit is mostly the mean return (Moskowitz 2012, Table 5B): trend on demeaned bond returns |
| **combine** | Pair strategies with opposite payoff profiles | Is the low correlation explained by the mechanisms, not only by the sample? | Trend (straddle-like) with carry (negative skew) |

One brick changes at a time. An idea that needs two operators is two ideas.

**Transpose** means a market the source did not test.

**replicate**: run a paper's own strategy, on the market it tested, often on later data. At most one per run, and only when the reading note shows all of these:
- real-data results that hold across several markets or sub-groups;
- in the desk's scope, with data the desk has;
- something the paper lacks that a replication would add: costs, an out-of-sample period. A paper that already tested everything teaches nothing when replicated.
Say in "What's new" that it is a replication, and why this paper deserves one.
