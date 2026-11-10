# Book construction: what each section of text.md says

There is no book yet. The reader wants to know whether these strategies make a book, which ones belong in it, and what that book really is. Each section is one or two paragraphs of 3 to 6 lines, reading the tables and figures in order with the numbers that matter. Refer to tables and figures by what they are ("the leave-one-out table"): the PDF numbers them.

## abstract (6 to 9 lines)
The strategies in one sentence each (what they trade). The book in one sentence: its Sharpe and volatility on the window against the range of the strategies alone, and whether it is positive every year. What the book really is (its market exposure, its IDM), and which strategy does not earn its place, if any. One sentence in bold: the proposal as the script wrote it. Then the book's main need.

## strategies
How the book is sized (15% per strategy, equal risk by family, IDM, 10% target, the IDM's value). Each strategy alone: its Sharpe, its Sharpe after the luck haircut (say why a haircut is large: many tries in that family), its t, its drawdown.

## performance
The book against each strategy alone: is its Sharpe above all of them, in what share of histories does it beat each, how wide is its range, its probability of a Sharpe above zero. Drawdown and worst month: does the book protect the bad days, or only smooth the ordinary ones? Then the out-of-sample window, if there is one: the book's Sharpe from the day every strategy is in its sealed test, against before.

## place
Read the leave-one-out table strategy by strategy: the book's Sharpe without it, how often dropping it hurts, and why (usually its correlation to the others). A strategy whose removal raises the Sharpe or lowers the drawdown does not earn its place: say what it still brings (often one episode), and why that is not enough.

## diversification
The correlations between strategies (appendix matrix), then the rolling view: the ranges with dates, when the average pairwise correlation peaked. The IDM: how far the book is from as many independent bets as it has strategies. Risk share (mean and max) and return share of each. Any suspect day: its date, what moved, and that it must be checked in the runs.

## exposures
The regression: which strategies are a market in disguise (high R2, significant beta, no alpha) and which have an alpha of their own. The book's alpha, its t, its betas, its R2. Then the rolling correlations to equities and bitcoin: full-window value, range with dates, share of weeks above 0.3, latest reading. Say plainly what the book is most of the time (for example "an equity book with a crypto sleeve").

## stress
How the book did across the episodes, which strategies carried it and which cost, and the pattern (slow crises against crashes of a few days).

## decision
The two rules (earning a place, carrying money), each strategy's outcome, the proposed book's numbers, and the decision as the script wrote it. What paper means (tracked month by month without money). What would change the proposal.

## needs
What the book lacks, in 2 to 4 lines the Ideator can use: the markets or premia missing, the conditions in which it loses.

## limits
Short window or a single market cycle; equal risk weights on purpose (optimised weights would fit noise); the leave-one-out comparison is on the same years; the in-sample part of each strategy; suspect days; imported returns.
