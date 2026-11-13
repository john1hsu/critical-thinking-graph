---
id: ct:expected-value
type: Concept
title: Expected value
aliases: [mathematical expectation, expectation, expected monetary value, EMV]
domain: probabilistic-reasoning
summary: >-
  The probability-weighted average of the possible outcomes of an uncertain
  prospect, E[X] = sum of p(x) times x; it is the long-run average payoff per
  trial and the basic yardstick for comparing bets, investments and decisions
  under risk.
level: introductory
evidenceStatus: normative
broader: [ct:probability-theory]
related: [ct:expected-utility-theory, ct:prospect-theory, ct:decision-theory, ct:risk-aversion, ct:gamblers-fallacy, ct:conditional-probability, ct:decision-analysis, ct:abraham-de-moivre]
requires: [ct:probability-theory]
relations:
  - {predicate: introducedBy, object: ct:christiaan-huygens, source: s3, confidence: high}
  - {predicate: challengedBy, object: ct:st-petersburg-paradox, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:expected-utility-theory, source: s5, confidence: high}
  - {predicate: appliedIn, object: ct:decision-analysis, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Discrete Random Variables: Expected Value (Class 4b), 18.05 Introduction to Probability and Statistics"
    publisher: MIT OpenCourseWare (Orloff & Bloom, Spring 2022)
    url: https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_class04-prep-b.pdf
    type: academic
    accessed: 2026-11-13
  - id: s2
    title: "The St. Petersburg Paradox"
    publisher: Stanford Encyclopedia of Philosophy (Martin, rev. 2008; Spring 2013 archive edition)
    url: https://plato.stanford.edu/archives/spr2013/entries/paradox-stpetersburg/
    type: scholarly-encyclopedia
    accessed: 2026-11-13
  - id: s3
    title: "Huygens, Christiaan"
    publisher: Encyclopedia of Mathematics (EMS/Springer; adapted from Schneider)
    url: https://encyclopediaofmath.org/wiki/Huygens,_Christiaan
    type: scholarly-encyclopedia
    accessed: 2026-11-13
  - id: s4
    title: "Prospect Theory: An Analysis of Decision under Risk"
    publisher: Econometrica 47(2), 263-292 (Kahneman & Tversky, 1979), Econometric Society
    url: https://www.econometricsociety.org/publications/econometrica/1979/03/01/prospect-theory-analysis-decision-under-risk
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "Notes 3: Random variables (DECS-430 course notes)"
    publisher: Kellogg School of Management, Northwestern University
    url: https://www.kellogg.northwestern.edu/faculty/weber/DECS-430/Notes_3_Random_variables.pdf
    type: academic
    accessed: 2026-11-13
created: 2026-11-13
---

# Expected value

The expected value of an uncertain quantity is the average of its possible values, each weighted by its probability: multiply every outcome by the chance it occurs and add the products.[^s1] It is also called the mean or the expectation, and it need not be one of the outcomes that can actually happen; a fair die has an expected value of 3.5.[^s1] Two readings make it useful in reasoning. It is the average result you would see per trial if the same gamble were repeated many times, and it is the balance point of the probability distribution.[^s1] Expected value is the first tool for asking whether a bet, an investment or a policy is favourable on average, before asking how risky it is.[^s5]

## Origin

The idea grew out of seventeenth-century problems about games of chance. Christiaan Huygens heard in France in 1655 that Pascal and Fermat had corresponded about gambling problems the year before, but did not learn their methods and worked out his own.[^s3] His 1657 tract *De ratiociniis in ludo aleae*, printed as an appendix to a book by Frans van Schooten, built its whole method on the value of a player's "expectation", understood as a fair share of the stakes.[^s3] Its third proposition gives the rule in modern dress: if there are p ways to gain a and q ways to gain b, the expectation is (pa + qb)/(p + q).[^s3] Huygens used recursive calculations of this kind to solve the problem of points, how to split the pot of an interrupted game.[^s3] Notably, the tract never uses the concept of probability itself; expectation came first, and probability was later read back into it.[^s3]

Within a century the concept was already under strain. Daniel Bernoulli's 1738 paper presented the St. Petersburg game, whose expected payoff is infinite even though almost nobody would pay much to play it, and proposed valuing outcomes by their utility rather than their cash amount.[^s2]

## How it works

Take a firm deciding which of two contracts to bid on, with room for only one bid. Bid A costs 20,000 to prepare and has an estimated 60% chance of winning a contract worth 200,000 in profit. Bid B costs 40,000 and has a 20% chance of a contract worth 800,000. The expected value of A is 0.6 x 200,000 minus 20,000, or 100,000. For B it is 0.2 x 800,000 minus 40,000, or 120,000. On expected value alone B is better, even though it loses money four times out of five. The calculation forces the team to state its probability estimates and to weigh payoffs by them instead of being swayed by the biggest number or the likeliest outcome.[^s1][^s5]

Expected value is linear: the expectation of a sum is the sum of the expectations, and scaling or shifting a quantity scales or shifts its mean the same way.[^s1] That makes portfolio and project totals easy to compute. A trap sits next to it, though: the expectation of a function of X is generally not the function of the expectation, so plugging an average input into a nonlinear model does not give the average output.[^s1]

## How to apply it

1. **List the outcomes and give each a probability** that sums to 1, including the dull and the bad outcomes.[^s1]
2. **Attach a payoff to each outcome**, net of costs, and multiply and add.[^s1]
3. **Compare options on expected value, then on spread.** A diversified shareholder may reasonably want managers to maximise expected profit, but an individual or a small firm that cannot absorb the bad outcome should not stop there.[^s5]
4. **Switch to utility when stakes are large relative to wealth.** A person with square-root utility is indifferent between 250,000 for certain and a 50% chance of 1,000,000, although the gamble's expected value is twice as large.[^s5]

## Limitations

Expected value is a normative benchmark that describes a long run; a one-off decision delivers one outcome, not the average. The St. Petersburg game shows how far it can part company with sensible choice: its expected payoff is infinite, yet the SEP reports Ian Hacking's estimate that few people would pay even 25 dollars to play.[^s2] The proposed repairs (diminishing marginal utility, an upper bound on utility, risk aversion, or the finite bankroll of any real casino) all change the quantity being maximised or the game being played, and the entry's author finds none of them fully satisfying.[^s2]

People also do not choose by expected value, nor even by expected utility. Kahneman and Tversky's 1979 experiments found a certainty effect, in which certain outcomes are overweighted relative to merely probable ones, and decision weights that overweight low probabilities. They proposed this pattern may explain the appeal of both insurance and gambling.[^s4]

## Connections

- **Introduced by Christiaan Huygens**, whose 1657 tract made expectation the basis of the calculus of chance.[^s3]
- **Challenged by the St. Petersburg paradox**, a game with infinite expected value that no reasonable person values highly.[^s2]
- **Contrasts with expected utility theory**, which keeps the weighted-average form but replaces money with the utility of money, capturing risk attitudes that expected monetary value ignores.[^s5]
- **Applied in decision analysis**, where choosing a policy amounts to choosing between random variables and comparing their expectations.[^s5]
- **Related to prospect theory**, whose findings show how actual choices depart from expectation-based rules.[^s4]

## Sources

[^s1]: Orloff & Bloom, "Discrete Random Variables: Expected Value", 18.05 *Introduction to Probability and Statistics*, MIT OpenCourseWare (Spring 2022). https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_class04-prep-b.pdf (accessed 2026-11-13)
[^s2]: Martin, "The St. Petersburg Paradox", Stanford Encyclopedia of Philosophy (Spring 2013 edition). https://plato.stanford.edu/archives/spr2013/entries/paradox-stpetersburg/ (accessed 2026-11-13)
[^s3]: "Huygens, Christiaan", Encyclopedia of Mathematics. https://encyclopediaofmath.org/wiki/Huygens,_Christiaan (accessed 2026-11-13)
[^s4]: Kahneman & Tversky, "Prospect Theory: An Analysis of Decision under Risk", *Econometrica* 47(2), 263-292 (1979). https://www.econometricsociety.org/publications/econometrica/1979/03/01/prospect-theory-analysis-decision-under-risk (accessed 2026-11-13)
[^s5]: Kellogg School of Management, Northwestern University, "Notes 3: Random variables", DECS-430 course notes. https://www.kellogg.northwestern.edu/faculty/weber/DECS-430/Notes_3_Random_variables.pdf (accessed 2026-11-13)
