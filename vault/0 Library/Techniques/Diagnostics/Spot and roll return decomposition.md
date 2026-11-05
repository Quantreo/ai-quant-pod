---
type: diagnostic
kind: attribution
aliases: [spot change and roll return split, Carry and price change split, Interest differential and price split, Spot and forward premium split]
sources: 4
---

# Spot and roll return decomposition

> [!summary]
> Does a futures return come from information spreading slowly (spot change) or from hedging pressure (roll return)?

## How it works

- **How**: split the futures return into the spot price change and the roll return. Follow the response of each component to a return shock over time.
- **Reading**: compare how long each component keeps responding and whether it reverses.
- **Data needed**: futures prices, spot prices, roll returns.
- **Variant**: carry trade: split the excess return into the interest rate differential and the price change of the asset. Variant: currency excess return = spot change minus the forward premium.

## What the sources say

### Parameters
- **Moskowitz 2012**
	- VAR, said to be robust to lag lengths 12 to 24, not shown (p. 246).
- **Fan 2024**: r = carry + change in log price, per coin and per portfolio (Eq. 2, p. 7)
- **Colacito 2019**
	- RX = (Spot(t+1) - Fwd(t)) / Spot(t) = spot return minus forward premium, per portfolio and for the long-short (Eq. 1-2, p. 8; Table 1).
- **Grewal 2015**
	- Run the same momentum portfolio on spot returns and on excess returns (forward-based); the gap is the interest differential (p. 37, 45-46; Tables 3.3-3.6)
	- Excess return R = forward minus next spot; spot return r = spot minus next spot, in log foreign currency per USD (p. 37)

### Why
- **Moskowitz 2012**
	- Separates information from hedging pressure (p. 247).
	- Conjecture: hedging pressure acts on roll return, information diffusion on the spot price (p. 247).
- **Fan 2024**: shows whether carry profits come from rates or prices, a test of uncovered interest parity (p. 13)
- **Colacito 2019**: shows the output gap sort is not a carry trade, whose return is the forward premium (p. 12)
- **Grewal 2015**: shows how much of a momentum return is carry

### Evidence
- **Moskowitz 2012**: real data, in-sample, gross of costs.
	- The spot component reverses after about 12 months (p. 245, 248-249).
	- Roll return keeps rising, ≈2.6% at month 36, with no reversal (≈ Fig. 7C).
	- Cumulative response ≈3.9% near month 12, ≈3.7% at month 36 (≈ Fig. 7A-B).
- **Fan 2024**: real data, in-sample, gross
	- High minus Low 43.4% = 19.4% rate differential + 24.0% price change (Table 4)
	- Price component rises from Low (50.7%) to High (74.7%) (Table 4)
- **Colacito 2019**: real data, real time, gross
	- Output gap long-short 4.92% = 4.21 spot + 0.71 interest (Table 4A).
	- Carry long-short, full sample: 7.80% = -4.63 spot + 12.43 interest (Table A2).
- **Grewal 2015**: real data, in-sample, gross, master's thesis
	- Daily, one pair, 1-day formation and holding: 5.58% excess against 6.95% spot (Tables 3.1-3.2)
	- Weekly and monthly, before 2008: excess positive in almost every cell, spot mostly negative (p. 46, Tables 3.4, 3.6)

### Limits
- **Moskowitz 2012**
	- Roll return and positions are imperfect proxies of hedging pressure (p. 248).
- **Fan 2024**: price component of High minus Low has a standard error of 24.1 (Table 4)
- **Colacito 2019**
	- After the crisis the forward discount holds interest differentials and CIP deviations together (p. 8).
- **Grewal 2015**
	- Only a comparison of two tables, no formal split and no standard errors (p. 45-46)

## Sources

- [[2012 - Moskowitz Ooi Pedersen - Time Series Momentum]] (Moskowitz 2012)
- [[2024 - Fan Jiao Lu et al - The Risk and Return of Cryptocurrency Carry Trade]] (Fan 2024)
- [[2019 - Colacito Riddiough Sarno - Business Cycles and Currency Returns]] (Colacito 2019)
- [[2015 - Grewal - Momentum in the Foreign Exchange Market]] (Grewal 2015)
