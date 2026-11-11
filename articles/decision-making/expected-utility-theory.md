---
id: ct:expected-utility-theory
type: Framework
title: Expected utility theory
aliases: [EUT, expected utility hypothesis, expected utility maximization, von Neumann-Morgenstern utility theory]
domain: decision-making
summary: >-
  The model of choice under risk that values each option by weighting the
  utility of its possible outcomes by their probabilities and recommends the
  option with the highest total; it is the classical normative standard for
  rational decisions and a much-criticised descriptive model of how people
  actually choose.
level: intermediate
evidenceStatus: contested
broader: [ct:decision-theory, ct:rationality]
related: [ct:bounded-rationality, ct:satisficing, ct:prospect-theory, ct:kenneth-arrow, ct:judgment-and-decision-making, ct:reversible-and-irreversible-decisions, ct:argument-from-consequences, ct:framing-effect, ct:st-petersburg-paradox, ct:risk-aversion]
requires: [ct:probability-theory]
relations:
  - {predicate: introducedBy, object: ct:daniel-bernoulli, source: s2, confidence: high}
  - {predicate: formalizedBy, object: ct:theory-of-games-and-economic-behavior, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:prospect-theory, source: s4, confidence: high}
  - {predicate: challengedBy, object: ct:allais-paradox, source: s5, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Normative Theories of Rational Choice: Expected Utility"
    publisher: Stanford Encyclopedia of Philosophy (Briggs, rev. 2023)
    url: https://plato.stanford.edu/entries/rationality-normative-utility/
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s2
    title: "Exposition of a New Theory on the Measurement of Risk"
    publisher: Econometrica 22(1), 23-36 (Bernoulli, 1738; trans. L. Sommer, 1954), copy hosted on a Czech Technical University course page
    url: https://cw.fel.cvut.cz/b191/_media/courses/xp36vpd/bernoulli-theorymeasurementofrisk.pdf
    type: primary
    accessed: 2026-11-11
  - id: s3
    title: "Theory of Games and Economic Behavior (60th Anniversary Commemorative Edition)"
    publisher: Princeton University Press (von Neumann & Morgenstern, 1944; 2007 edition), Project MUSE
    url: https://muse.jhu.edu/books/9781400829460
    type: primary
    accessed: 2026-11-11
  - id: s4
    title: "Prospect Theory: An Analysis of Decision under Risk"
    publisher: Econometrica 47(2), 263-292 (Kahneman & Tversky, 1979), Econometric Society
    url: https://www.econometricsociety.org/publications/econometrica/1979/03/01/prospect-theory-analysis-decision-under-risk
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "Developments in Non-Expected Utility Theory: The Hunt for a Descriptive Theory of Choice under Risk"
    publisher: Journal of Economic Literature 38(2), 332-382 (Starmer, 2000), copy hosted at Universidad de Montevideo
    url: https://www2.um.edu.uy/marcaffera/marcelo/Papers/Ambiguity/Starmer%20-%20JEL%20-%202000.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s6
    title: "Expected Utility (lecture notes, 14.123 Microeconomic Theory III)"
    publisher: MIT OpenCourseWare (Denti, 2015)
    url: https://ocw.mit.edu/courses/14-123-microeconomic-theory-iii-spring-2015/b2353bc4abf8a109fb75bba0064b331d_MIT14_123S15_expected1.pdf
    type: academic
    accessed: 2026-11-11
created: 2026-11-11
---

# Expected utility theory

Expected utility theory (EUT) says that when outcomes are uncertain, a rational chooser should score each option by multiplying the utility of every possible outcome by its probability, adding the results, and picking the option with the highest sum.[^s1] Utility here is not money: it measures how much an outcome is worth to the person choosing, so the same sum can matter very differently to different people.[^s1][^s2] For critical thinkers, EUT is the benchmark against which "irrational" choices are usually judged, which makes it worth knowing both what it demands and where its authority is disputed.[^s1][^s5]

## Origin

The idea grew out of the 18th-century St Petersburg problem, a coin-toss game whose expected cash payout is infinite even though nobody sensible would pay more than a modest sum to play.[^s2] In a 1738 paper, Daniel Bernoulli proposed that a gamble should be valued by the utility it brings rather than its price, and that each extra ducat adds less utility the richer you already are; with that assumption the game's value becomes small and finite.[^s2] He applied the same reasoning to a merchant deciding whether to insure a cargo, showing that insuring is wise for a poorer merchant and unnecessary for a richer one.[^s2] Two centuries later, Frank Ramsey, John von Neumann and Oskar Morgenstern, and Leonard Savage turned the idea into axiomatic theories: von Neumann and Morgenstern's 1944 *Theory of Games and Economic Behavior* showed that preferences over lotteries satisfying certain axioms can be represented as maximising expected utility, and Savage extended this to personal probabilities derived from preferences over acts.[^s1][^s3]

## How it works

The modern representation theorems say that if your preferences over risky options are complete, transitive, continuous and obey an independence condition (mixing two options with the same third option should not reverse your ranking of them), then there is a utility function such that you prefer one option to another exactly when its expected utility is higher.[^s6][^s1] The axioms do the persuasive work: a person who accepts them is committed to choosing as if maximising expected utility.[^s1]

A workplace example: an operations manager must decide whether to buy a $9,000 service contract on a production machine. Without it, there is roughly a 10% chance of a $60,000 breakdown this year. The expected *monetary* loss without the contract is $6,000, less than the contract price, so a pure expected-value calculation says skip it. EUT asks a further question, following Bernoulli's merchant: how much would a $60,000 hit hurt this particular business? For a small firm where that loss threatens payroll, the utility lost is far more than six times the pain of a $9,000 bill, and buying the contract can maximise expected utility.[^s2][^s1] For a large firm with many machines, the same contract is probably a poor buy.

## How to apply it

1. List the options and the outcomes each could lead to.
2. Estimate a probability for each outcome given each option.
3. Assign utilities that reflect what the outcomes are worth to the decision maker, not just their cash value; concave utility over money expresses risk aversion.[^s2][^s1]
4. Compute each option's probability-weighted sum and compare.
5. Check the ranking against the axioms: if your gut preference flips when an outcome common to both options is changed, you are violating independence and should ask which judgment to trust.[^s5][^s1]

Pitfalls include treating made-up probabilities as precise, forgetting that utility depends on circumstances, and assuming the calculation settles what is rational when the axioms themselves are in question.[^s1]

## Evidence and limitations

As a *descriptive* model, EUT fares poorly. Kahneman and Tversky's 1979 paper presented choice problems in which people systematically violated its assumptions, and proposed prospect theory, which values gains and losses relative to a reference point and replaces probabilities with decision weights.[^s4] Allais's paradox shows two robust patterns, the common consequence and common ratio effects, that break the independence axiom; framing experiments show that equivalent descriptions of the same options shift choices.[^s5] Reviewing two decades of experiments in 2000, Starmer concluded that EUT is likely to mislead descriptively in important contexts and recommended rank-dependent models such as cumulative prospect theory as the default, while noting that EUT fit a substantial minority of individual subjects as well as any rival.[^s5]

As a *normative* standard, its status is debated rather than refuted. Some argue that Allais-type preferences are mistakes; others redescribe outcomes to include regret or disappointment; still others, such as Buchak, defend risk-weighted alternatives under which those preferences are rational.[^s1] Further objections target transitivity and completeness, and the practical impossibility of computing expected utility for every option in real decisions.[^s1]

## Connections

EUT began with Daniel Bernoulli's answer to the St Petersburg paradox, which introduced diminishing marginal utility and a utility-based account of risk aversion.[^s2] It was given its axiomatic form by von Neumann and Morgenstern in *Theory of Games and Economic Behavior*, building on probability theory, and is a central theory within decision theory and the study of rationality.[^s1][^s3] It is challenged by prospect theory, the best-known descriptive alternative and a founding contribution to judgment and decision-making research, and by the Allais paradox, the classic counterexample to its independence axiom.[^s4][^s5] Bounded rationality and satisficing reject its assumption of an all-computing optimiser, and framing effects violate its requirement that choices not depend on description.[^s1][^s5] Arguments from consequences and reasoning about reversible and irreversible decisions draw on it whenever they weigh likely outcomes.[^s1]

## Sources

[^s1]: Briggs, "Normative Theories of Rational Choice: Expected Utility", Stanford Encyclopedia of Philosophy (rev. 2023). https://plato.stanford.edu/entries/rationality-normative-utility/ (accessed 2026-11-11)
[^s2]: Bernoulli, "Exposition of a New Theory on the Measurement of Risk" (1738), trans. Sommer, Econometrica 22(1), 23-36 (1954). https://cw.fel.cvut.cz/b191/_media/courses/xp36vpd/bernoulli-theorymeasurementofrisk.pdf (accessed 2026-11-11)
[^s3]: von Neumann & Morgenstern, *Theory of Games and Economic Behavior* (1944; 60th anniversary edition, Princeton University Press, 2007). https://muse.jhu.edu/books/9781400829460 (accessed 2026-11-11)
[^s4]: Kahneman & Tversky, "Prospect Theory: An Analysis of Decision under Risk", Econometrica 47(2), 263-292 (1979). https://www.econometricsociety.org/publications/econometrica/1979/03/01/prospect-theory-analysis-decision-under-risk (accessed 2026-11-11)
[^s5]: Starmer, "Developments in Non-Expected Utility Theory: The Hunt for a Descriptive Theory of Choice under Risk", Journal of Economic Literature 38(2), 332-382 (2000). https://www2.um.edu.uy/marcaffera/marcelo/Papers/Ambiguity/Starmer%20-%20JEL%20-%202000.pdf (accessed 2026-11-11)
[^s6]: Denti, "Expected Utility", lecture notes for MIT 14.123 Microeconomic Theory III (2015), MIT OpenCourseWare. https://ocw.mit.edu/courses/14-123-microeconomic-theory-iii-spring-2015/b2353bc4abf8a109fb75bba0064b331d_MIT14_123S15_expected1.pdf (accessed 2026-11-11)
