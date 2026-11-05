---
type: diagnostic
kind: attribution
aliases: [downside market beta test, beta differential test, Henriksson-Merton regression, bear-market optionality test, up and down market beta, recession beta, recession interaction regression, state-dependent beta, call-payoff beta, short call test, DR-CAPM]
sources: 5
---

# Downside beta regression

> [!summary]
> Is the strategy more exposed to the market when the market is down than when it is up?

## How it works

- **How**: regress the strategy return on a constant, a down-market dummy, the market return, and the market return kept only in down-market periods (zero otherwise). The last coefficient is the extra beta in the down state. Variant: recession state. Variant: Henriksson-Merton form, strategy on market return and max(market return, 0), run within groups of periods sorted on a state variable; compare the skewness of returns and of residuals.
- **Reading**: a positive, significant extra beta means the strategy loses more with the market in bad states than its plain beta says. Multiplying the beta gap by a price of downside risk gives the share of the mean return it could explain. Variant: bear-state up-market beta; negative is a short call.
- **Data needed**: strategy and market excess returns, same dates.

## What the sources say

### Parameters
- **Daniel 2014**
	- R_t = a1 + a2 I- + b1 R_m + b2 R_m- ; b2 = downside beta minus b1 (Eq. 12, p. 20).
	- Down state: market return one standard deviation below its mean, following Lettau, Maggiori, Weber (p. 20).
	- Newey-West standard errors, 3 lags (p. 21).
	- Price of downside risk taken from Lettau, Maggiori, Weber: 16.92% or 26.2% a year (p. 21).
- **Daniel 2016**
	- Variant: R = [α0 + αB·I_B] + [β0 + I_B(βB + I_U·βB,U)]·R_m, with I_B a bear-market dummy (past 24-month market return negative) and I_U = 1 if the same-month market excess return is positive (Eq. 3, p. 15)
	- βB,U < 0: short a call on the market in bear markets (p. 15-16)
	- Run on each decile and on the long-short portfolio; mirror test with a bull dummy (Table 4)
- **Moreira 2016**
	- Managed factor on constant, NBER recession dummy, original factor, and original factor times the dummy (Table 3, p. 32).
	- Heteroscedasticity-robust standard errors (Table 3).
	- Downside beta as in Lettau, Maggiori, Weber, unreported (p. 43).
- **Daniel 2012**
	- R_p = α + β0·R_m + β+·max(R_m, 0) + ε (Eq. 1, p. 10)
	- Groups: top and bottom 20% of a state variable, middle 60% (p. 10)
	- White standard errors (Table 3)
- **Ivanova 2014**
	- Downside risk CAPM: strategy beta in months when the market is at least one standard deviation below its mean, compared with the plain beta (Eq. 17, p. 18)
	- Price of risk set to the average market excess return; 12 FX portfolios, June 1977 to December 2012 (Table 4)
### Why
- **Daniel 2014**: tests the beta differential directly, to see whether downside market risk explains carry returns (p. 20).
- **Daniel 2016**: after market falls the losers of a momentum sort carry high beta; the test shows whether the payoff is option-like (p. 15-16)
- **Moreira 2016**: a strategy that takes less risk in recessions is hard to explain by business cycle risk (p. 10-11).
- **Daniel 2012**: β+ is the exposure to a one-month market call payoff, a measure of convexity (p. 10)
- **Ivanova 2014**: following Lettau, Maggiori and Weber, who explain carry with it (p. 17-18)
### Evidence
- **Daniel 2014**: real data, in-sample, gross of costs.
	- Carry b2 positive but insignificant, largest t 1.43; EQ-USD b2 negative (p. 21; Table 13).
	- Downside exposure explains 0% to 5% of EQ and EQ-RR alpha, 20% to 40% of SPD and SPD-RR alpha (p. 21-22; Table 13).
	- Six interest-rate portfolios: downside explains about a quarter of P6-P1 alpha (p. 22; Table 14).
- **Daniel 2016**: real data, in-sample, gross, monthly 1927-2013
	- US WML: βB,U = -0.815 (t = -4.5); no significant asymmetry in bull markets (-0.242, t = -1.3) (Table 4)
	- Loser decile βB,U = 0.600 (t = 4.4), winner decile -0.215 (t = -2.5) (Table 4)
	- 1972-2013: significant in EU, JP, UK equities and commodities; currencies -0.405 (t = -1.4) (Tables 8 B, 9 B)
- **Moreira 2016**: real data, in-sample, gross
	- Market: beta 0.83 outside recessions, interaction -0.51 (SE 0.10), so 0.32 in recessions (Table 3, p. 11).
	- FX carry 1983-2015: beta 0.73, interaction -0.26 (SE 0.15) (Table 3).
	- RMW: interaction -0.08 (SE 0.13), not significant (Table 3).
	- Downside beta of the managed market 0.11, not significant, numbers not shown (p. 43).
- **Daniel 2012**: real data, in-sample, gross, US 1929-2013
	- After low 36-month market returns: momentum β+ -1.01 (t = -3.17), losers 0.72 (t = 3.60); not significant elsewhere (Table 3A)
	- Momentum skewness -2.33 falls to -0.48 on residuals in that group (Table 3D)
	- 2000-2002: β+ -1.35 (t = -1.26), 36 months (Table 4)
- **Ivanova 2014**: real data, in-sample, FX technical portfolios
	- Downside betas significant but wrong-signed, like the plain betas (p. 19, Table 4)
	- Price of downside risk -3.35, t = -0.86; R2 -0.16 without a constant (Table 4)
### Limits
- **Daniel 2014**
	- Downside betas are small and imprecisely estimated (p. 23).
	- The downside market return is not a traded return, so the intercept is not an abnormal return (p. 21).
- **Daniel 2016**
	- Up-market dummy is contemporaneous: a description, not a forecast (p. 15)
	- Not significant for US 1972-2013 (Table 8 B)
- **Moreira 2016**
	- Recession dates known only ex post; a description of exposure, not a rule (Table 3).
	- The downside beta result is unreported (p. 43).
- **Daniel 2012**
	- The intercept is not an abnormal return: max(R_m, 0) is not an excess return (p. 10)
	- Group cut-offs are full-sample percentiles (p. 10)
- **Ivanova 2014**
	- Negative betas mean the strategy hedges downside risk, so risk cannot explain its mean return (p. 18-19)

## Sources

- [[2014 - Daniel Hodrick Lu - The Carry Trade Risks and Drawdowns]] (Daniel 2014)
- [[2016 - Daniel Moskowitz - Momentum crashes]] (Daniel 2016)
- [[2016 - Moreira Muir - Volatility Managed Portfolios]] (Moreira 2016)
- [[2012 - Daniel Jagannathan Kim - Tail Risk in Momentum Strategy Returns]] (Daniel 2012)
- [[2014 - Ivanova Neely Weller et al - Can risk explain the profitability of technical trading in currency markets]] (Ivanova 2014)
