## abstract
The desk has three strategies that passed their sealed test: Crypto Thin Losers (reversal on crypto perpetuals), ETF TSMOM 12-Month (trend on multi-asset ETFs) and SPY Volatility Managed (equities timed by their own volatility). Put together with equal risk, the book earns a net Sharpe ratio of 1.02 at 10.7% volatility from January 2021 to September 2026, against 0.49 to 0.76 for each strategy alone at the same volatility. It is far from three independent bets, though: its diversification multiplier is 1.56, and it is mostly long US equities, with a beta of 0.38 to SPY and a correlation to SPY above 0.3 in 83% of weeks. TSMOM does not earn its place: the book without it has a higher Sharpe ratio and a smaller drawdown. **Proposed: a book of Crypto Thin Losers and SPY Volatility Managed, on paper; TSMOM stays in the library.** The book's real need is a second source of return that does not depend on equities.

## strategies
Each strategy is scaled to 15% volatility with its trailing 60-day volatility, known the day before; the three families (reversal, trend, low-vol) share the risk equally, a third each, and the book is brought to its 10% target by the diversification multiplier, here 1.56. SPY Volatility Managed has the best Sharpe ratio alone (0.76) and the strongest evidence (t of 3.33). Thin Losers loses almost all of its Sharpe ratio to the luck haircut of its family (0.71, leaving -0.01), because the desk tried several reversal ideas on crypto before keeping it.

## performance
The book does what a book should: its Sharpe ratio of 1.02 is above every strategy alone, and in the bootstrap it beats each of them in 78% to 96% of histories. Its 90% range is still wide, 0.30 to 1.63, but its Sharpe ratio is above zero in 99.7% of histories. Its maximum drawdown, -17.2%, is not smaller than the strategies', and its worst month, -5.1%, is no better than SPY Volatility Managed's alone: the book smooths the ordinary days more than it protects the bad ones.

From January 2025, when every strategy is in its sealed test, the book earns a Sharpe ratio of 0.96 over 638 days, against 1.05 before: the result holds where nothing was fitted.

## place
Thin Losers earns its place: without it the Sharpe ratio falls to 0.75, and dropping it hurts in 90% of histories, because it is uncorrelated with the other two. SPY Volatility Managed does too (0.87 without it, 76%). TSMOM does not: without it the book's Sharpe ratio is 1.04, its drawdown -13.6% instead of -17.2%, and removing it hurts in only 46% of histories. Over these years TSMOM and SPY Volatility Managed are correlated (+0.41), so TSMOM adds a second equity-like bet rather than a new one; what it still brings is the 2022 bear market, and one episode is not a place in the book.

## diversification
Thin Losers is independent of both others (-0.05 and -0.02), while TSMOM and SPY Volatility Managed move together at +0.41. The rolling view shows how unstable that pair is: TSMOM's correlation with the rest of the book runs from -0.58 in November 2022 to +0.68 in February 2022, and the average pairwise correlation peaks at +0.33 in May 2025, just after the tariff shock. The risk is shared about evenly on average, but Thin Losers carried up to 71% of it at times. One day stands out in the data: on 6 August 2023 Thin Losers gains 8.2%, beyond eight standard deviations; it should be checked in the runs.

## exposures
The regression shows what the book really is. SPY Volatility Managed is US equities: a beta of 0.54 with a t of 7.7, 85% of its variance explained, no alpha left, which is its design. TSMOM was short long Treasuries and long gold over these years, with no alpha left either. Only Thin Losers has an alpha of its own, 8.4% a year with a t of 2.5, and no market beta. The book as a whole has a beta of 0.38 to SPY (t of 3.7) and an alpha of 2.6% a year that is not significant (t of 0.8).

The rolling view makes it plain: the book's correlation to SPY is +0.58 over the window, above 0.3 in 83% of weeks, reached +0.90 in January 2026 and reads +0.79 at the end. Most of the time this is an equity book with a crypto sleeve.

## stress
The book made money in the slow crises, the 2022 bear market in equities and bonds (+12.3%, carried by TSMOM and Thin Losers while SPY Volatility Managed lost) and the crypto crashes of 2021 and 2022. It lost in the fast ones, where all three strategies fell together: the yen carry unwind of August 2024 (-4.1%) and the tariff shock of April 2025 (-6.0%). In a crash of a few days, the diversification of this book disappears.

## decision
A strategy earns its place if dropping it hurts the book in 60% of histories or more, and can carry money with a full-sample t of 2 or more and a Sharpe ratio after luck above zero. SPY Volatility Managed passes both. Thin Losers earns its place most clearly, but nothing of its Sharpe ratio survives the luck haircut, so it stays on paper. TSMOM stays in the library, passed. The proposed book, Thin Losers and SPY Volatility Managed with half the risk each, earns 1.04 with a maximum drawdown of -13.6%; since one of its two members is paper only, the book goes on paper, tracked month by month before any money.

## needs
The book needs a second engine that does not depend on equities: beyond Thin Losers, its return is the US equity premium, timed. The next research should aim at premia on other markets, carry or value on currencies or rates, and at strategies that hold up in fast crashes, where this book loses all its diversification at once.

## limits
Five years and eight months is short, and it is a single equity cycle. The weights are equal risk by family on purpose: with three strategies, optimised weights would fit noise. The leave-one-out comparison is on the same years as everything else, so it can say that TSMOM adds little here, not that it never will. Thin Losers' first four years are in-sample, and its suspect day of 6 August 2023 is still in the data.
