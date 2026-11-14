---
id: ct:risk-aversion
type: Concept
title: Risk aversion
aliases: [risk-averse preference, aversion to risk]
domain: decision-making
summary: >-
  A preference for a certain outcome over a gamble whose expected value is
  equal or higher; in expected utility theory it is modelled by a concave
  utility function, and its size is measured by the risk premium a person
  would pay to avoid the gamble.
level: intermediate
evidenceStatus: robust
broader: [ct:decision-theory, ct:expected-utility-theory]
related: [ct:loss-aversion, ct:prospect-theory, ct:expected-value, ct:broad-bracketing, ct:framing-effect, ct:allais-paradox, ct:richard-thaler, ct:risk-communication]
requires: [ct:expected-value]
relations:
  - {predicate: introducedBy, object: ct:daniel-bernoulli, source: s6, confidence: medium}
  - {predicate: formalizedBy, object: ct:expected-utility-theory, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:holt-laury-2002-lottery-choice-experiment, source: s3, confidence: high}
  - {predicate: supportedBy, object: ct:holt-laury-2005-order-effects-replication, source: s4, confidence: medium}
  - {predicate: explainedBy, object: ct:prospect-theory, source: s5, confidence: medium}
  - {predicate: explainedBy, object: ct:loss-aversion, source: s2, confidence: medium}
  - {predicate: studiedIn, object: ct:behavioral-economics, source: s2, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Risk Aversion in the Small and in the Large"
    publisher: Econometrica 32(1), 122-136 (Pratt, 1964), Econometric Society
    url: https://www.econometricsociety.org/publications/econometrica/1964/01/01/risk-aversion-small-and-large
    type: primary
    accessed: 2026-11-14
  - id: s2
    title: "Anomalies: Risk Aversion"
    publisher: Journal of Economic Perspectives 15(1), 219-232 (Rabin & Thaler, 2001), via IDEAS/RePEc
    url: https://ideas.repec.org:443/a/aea/jecper/v15y2001i1p219-232.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "Risk Aversion and Incentive Effects"
    publisher: American Economic Review 92(5), 1644-1655 (Holt & Laury, 2002), copy hosted at Universidad de Montevideo
    url: https://www2.um.edu.uy/marcaffera/marcelo/Papers/Trust%20Nestor/Holt%20and%20Laury%202002%20AER%20Risk%20Aversion%20and%20Incentives%20Effects.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "Risk Aversion and Incentive Effects: New Data without Order Effects"
    publisher: American Economic Review 95(3), 902-904 (Holt & Laury, 2005), copy hosted on a UC San Diego course page
    url: https://econweb.ucsd.edu/~jandreon/Econ264/papers/Holt%20Laury%20AER%202005.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "Prospect Theory: An Analysis of Decision under Risk"
    publisher: Econometrica 47(2), 263-292 (Kahneman & Tversky, 1979), Econometric Society
    url: https://www.econometricsociety.org/publications/econometrica/1979/03/01/prospect-theory-analysis-decision-under-risk
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s6
    title: "Normative Theories of Rational Choice: Expected Utility"
    publisher: Stanford Encyclopedia of Philosophy (Briggs, rev. 2023)
    url: https://plato.stanford.edu/entries/rationality-normative-utility/
    type: scholarly-encyclopedia
    accessed: 2026-11-14
created: 2026-11-14
---

# Risk aversion

Risk aversion is the tendency to prefer a sure thing to a gamble that offers the same, or even a somewhat higher, expected value. Someone who takes a guaranteed bonus rather than a fair coin flip for twice the amount, or who buys insurance whose premium exceeds the expected loss, is behaving in a risk-averse way. Within expected utility theory the attitude is captured by the shape of the utility function for money, and its strength is expressed as a risk premium: the amount a person would give up to swap a risky prospect for a certain one.[^s1] Unlike most entries in this domain, risk aversion is not an error in itself; it becomes a reasoning problem only when its size or its triggers make choices inconsistent.[^s2][^s6]

## Origin

The idea goes back to Daniel Bernoulli's 1738 answer to puzzles about gambling. Bernoulli argued that money has diminishing marginal utility, so the same sum matters less to a rich person than to a poor one; his example was that a rich man, but not a pauper, can sensibly pay a large price for a lottery ticket that a poor man should sell.[^s6] Two centuries later, after von Neumann and Morgenstern had put expected utility on an axiomatic footing, John Pratt's 1964 paper in *Econometrica* gave the concept its modern measurement: a local measure of risk aversion derived from the curvature of the utility function, a definition of the risk premium, and a precise sense in which risk aversion can decrease as wealth grows.[^s1]

## How it works

Take a team lead choosing between two supplier contracts. Contract A guarantees savings of 40,000. Contract B saves 100,000 with probability one half and nothing otherwise, so its expected value is 50,000. A risk-neutral chooser takes B. A risk-averse chooser may take A, and the 10,000 of expected value she forgoes is a rough upper bound on her risk premium for this decision.[^s1] Under expected utility theory, that choice is fully rational if her utility for savings is concave: the second 50,000 adds less utility than the first, so the sure 40,000 can beat the gamble.[^s6]

Prospect theory describes the same territory differently. Kahneman and Tversky found that people overweight outcomes that are certain relative to those that are merely probable, which pushes them toward risk aversion when choosing between a sure gain and a gamble, and toward risk seeking when choosing between a sure loss and a gamble. Their value function is concave for gains and convex for losses, measured from a reference point rather than total wealth.[^s5] On this account, the team lead who plays safe with savings might gamble to avoid a certain cost overrun.

## Evidence

Laboratory measurement is now standard. In Holt and Laury's 2002 lottery-choice experiment, participants made ten paired choices between a safer and a riskier option as the chance of the high prize rose. At low stakes about two-thirds chose more safe options than a risk-neutral person would, and when real payoffs were scaled up twenty, fifty and ninety times, the average number of safe choices climbed steadily. Scaling up hypothetical payoffs changed little, and hypothetical choices were more risk-seeking, a warning that stated preferences understate real caution.[^s3] After critics argued that the result reflected the order in which conditions were run, Holt and Laury's 2005 follow-up gave each group only one payoff level and still found significantly more risk aversion at twenty-times real stakes, though the size of any order effect remained unclear.[^s4]

## Limitations and debates

The textbook link between risk aversion and concave utility has been attacked from two directions. Rabin and Thaler argued in 2001 that the modest risk aversion people show over small and moderate stakes cannot come from the curvature of utility over total wealth, because any utility function concave enough to produce it would imply absurdly extreme caution over large stakes; they proposed loss aversion and mental accounting as a better explanation.[^s2] Philosophers have also asked whether some risk aversion is a separate attitude toward how outcomes are spread rather than a fact about the value of money. Preferences in the Allais paradox, for example, cannot be fitted by any utility curvature within expected utility; defenders of the theory call them irrational, while Buchak argues they can be rationally permissible.[^s6]

## How to apply it

- **Name the attitude.** Ask whether a preference for the safe option reflects real diminishing value (losing 100,000 would hurt the business far more than gaining it would help) or reluctance about uncertainty for its own sake.[^s6]
- **Price it.** Compute the expected value of each option and state how much you are paying for certainty; if that premium is large, check that it is deliberate.[^s1]
- **Check the frame.** If the same choice described as avoiding losses produces the opposite preference, the decision is being driven by the reference point, not a stable risk attitude.[^s5]
- **Use real stakes.** When measuring a group's risk tolerance, questions about hypothetical money can be misleading guides to how people will act when the money is real.[^s3]

## Connections

- **Broader:** `ct:decision-theory` and `ct:expected-utility-theory`, the framework in which the concept is defined and measured.[^s1]
- **Introduced by:** `ct:daniel-bernoulli`, whose diminishing-marginal-utility account first explained why prudent people avoid fair gambles.[^s6]
- **Formalized by:** `ct:expected-utility-theory`, within which Pratt defined the local measure and the risk premium.[^s1]
- **Demonstrated by:** `ct:holt-laury-2002-lottery-choice-experiment`,[^s3] and **supported by** `ct:holt-laury-2005-order-effects-replication`, which reproduced the stake effect without order effects.[^s4]
- **Explained by:** `ct:prospect-theory`, whose certainty effect and concave gain function generate risk aversion for gains,[^s5] and `ct:loss-aversion`, which Rabin and Thaler proposed as the better explanation of small-stakes caution.[^s2]
- **Studied in:** `ct:behavioral-economics`, where the calibration critique of concave utility was developed.[^s2]
- **Related:** `ct:expected-value` (a prerequisite), `ct:broad-bracketing` and `ct:framing-effect`, which shape how risky options are grouped and described, and `ct:allais-paradox`, the classic case where risk attitudes escape expected utility.[^s6]

## Sources

[^s1]: Pratt, "Risk Aversion in the Small and in the Large", Econometrica 32(1), 1964. https://www.econometricsociety.org/publications/econometrica/1964/01/01/risk-aversion-small-and-large (accessed 2026-11-14)
[^s2]: Rabin & Thaler, "Anomalies: Risk Aversion", Journal of Economic Perspectives 15(1), 2001. https://ideas.repec.org:443/a/aea/jecper/v15y2001i1p219-232.html (accessed 2026-11-14)
[^s3]: Holt & Laury, "Risk Aversion and Incentive Effects", American Economic Review 92(5), 2002. https://www2.um.edu.uy/marcaffera/marcelo/Papers/Trust%20Nestor/Holt%20and%20Laury%202002%20AER%20Risk%20Aversion%20and%20Incentives%20Effects.pdf (accessed 2026-11-14)
[^s4]: Holt & Laury, "Risk Aversion and Incentive Effects: New Data without Order Effects", American Economic Review 95(3), 2005. https://econweb.ucsd.edu/~jandreon/Econ264/papers/Holt%20Laury%20AER%202005.pdf (accessed 2026-11-14)
[^s5]: Kahneman & Tversky, "Prospect Theory: An Analysis of Decision under Risk", Econometrica 47(2), 1979. https://www.econometricsociety.org/publications/econometrica/1979/03/01/prospect-theory-analysis-decision-under-risk (accessed 2026-11-14)
[^s6]: Briggs, "Normative Theories of Rational Choice: Expected Utility", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/rationality-normative-utility/ (accessed 2026-11-14)
