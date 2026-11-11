---
id: ct:prospect-theory
type: Framework
title: Prospect theory
aliases: [cumulative prospect theory, CPT, Kahneman-Tversky value function]
domain: decision-making
summary: >-
  A descriptive model of choice under risk, introduced by Kahneman and Tversky
  in 1979, in which people value gains and losses relative to a reference point,
  feel losses more than equal gains, and weight probabilities non-linearly
  instead of maximising expected utility.
level: intermediate
evidenceStatus: contested
broader: [ct:decision-theory, ct:judgment-and-decision-making]
related: [ct:expected-utility-theory, ct:loss-aversion, ct:framing-effect, ct:sunk-cost-fallacy, ct:risk-aversion, ct:bounded-rationality, ct:behavioral-economics]
requires: [ct:expected-utility-theory]
relations:
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:expected-utility-theory, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:ruggeri-2020-prospect-theory-replication, source: s3, confidence: high}
  - {predicate: challengedBy, object: ct:gal-rucker-2018-loss-of-loss-aversion, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Prospect Theory: An Analysis of Decision under Risk"
    publisher: Econometrica 47(2), 263-291 (Kahneman & Tversky, 1979), SSRN record
    url: https://papers.ssrn.com/abstract=1505880
    type: primary
    accessed: 2026-11-11
  - id: s2
    title: "Advances in Prospect Theory: Cumulative Representation of Uncertainty"
    publisher: Journal of Risk and Uncertainty 5, 297-323 (Tversky & Kahneman, 1992), copy hosted by California State University, Fullerton
    url: https://psych.fullerton.edu/mbirnbaum/psych466/articles/Tversky_Kahneman_JRU_92.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "Replicating patterns of prospect theory for decision under risk"
    publisher: Nature Human Behaviour 4(6) (Ruggeri et al., 2020), Vrije Universiteit Amsterdam research portal
    url: https://research.vu.nl/en/publications/replicating-patterns-of-prospect-theory-for-decision-under-risk/
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "The Loss of Loss Aversion: Will It Loom Larger Than Its Gain?"
    publisher: Journal of Consumer Psychology (Gal & Rucker, 2018), SSRN record
    url: https://papers.ssrn.com/abstract=3049660
    type: peer-reviewed
    accessed: 2026-11-11
created: 2026-11-11
---

# Prospect theory

Prospect theory is a model of how people actually choose between risky options. Instead of weighing final wealth by probabilities, as expected utility theory prescribes, people judge outcomes as gains or losses from a reference point, treat losses as weightier than gains of the same size, and give probabilities decision weights that are not proportional to the probabilities themselves.[^s1][^s2] For critical thinkers it is the standard explanation of why the same decision can feel different depending on how it is described, and a reminder that a choice can be predictable without being optimal.[^s1]

## Origin

Daniel Kahneman and Amos Tversky published the theory in *Econometrica* in 1979. They presented hypothetical choice problems to students and faculty and reported systematic patterns that expected utility theory could not accommodate, then proposed prospect theory as a descriptive alternative.[^s1] In 1992 they revised it as cumulative prospect theory, which weights cumulative rather than individual probabilities (a rank-dependent method), extends the model to uncertain prospects with any number of outcomes, and, unlike the original, always respects stochastic dominance.[^s2]

## How it works

The 1979 paper describes two phases. In an editing phase, people simplify the options, for example by coding outcomes as gains or losses and setting aside components the options share. In an evaluation phase, each edited option gets a value from a value function and decision weights, and the highest-valued option is chosen.[^s1] Three empirical patterns motivated the design: the certainty effect (sure outcomes are overweighted relative to merely probable ones), the reflection effect (risk preferences flip when gains become losses), and the isolation effect (shared components are ignored, so the way a choice is broken down changes the decision).[^s1]

The 1992 version gave the shape numbers. The value function is concave for gains and convex for losses, with a median curvature of about 0.88, and steeper for losses: the median loss-aversion coefficient was about 2.25, and a coin-flip gamble was acceptable to most participants only when the possible gain was roughly twice the possible loss.[^s2] The weighting function is inverse-S-shaped, overweighting small probabilities and underweighting moderate and large ones. Together these produce a fourfold pattern: risk aversion for likely gains and unlikely losses, risk seeking for likely losses and unlikely gains.[^s2]

A workplace example: a project is $200,000 over budget. Leadership can stop now and book the loss, or spend another $150,000 on a fix that has a 50% chance of recovering the overrun and a 50% chance of failing. Framed against the original budget, both options sit in the loss domain, where the convex value function makes the gamble attractive, so teams tend to keep spending. Reframe the same choice against today's position (a new $150,000 bet with a coin-flip payoff) and it becomes a gain-domain decision where most people turn cautious. The numbers are identical; only the reference point moved, which is exactly the dependence prospect theory predicts.[^s1][^s2]

## How to apply it

1. Name the reference point each stakeholder is using; status quo, budget, target and last year's result all give different ones.[^s1]
2. Re-express the options against at least two reference points and check whether the preferred option changes; if it does, the choice is being driven by framing.[^s1][^s2]
3. Watch for risk seeking when everything is coded as a loss, and for premium-paying caution around small, vivid probabilities, as the fourfold pattern predicts.[^s2]
4. Combine gambles that are separated only by presentation, so the isolation effect cannot hide what they share.[^s1]

Pitfalls include treating the 1992 parameter estimates as universal constants and assuming that every observed asymmetry between gains and losses is loss aversion.[^s2][^s4]

## Evidence and limitations

The core choice patterns replicate well. In 2020 Ruggeri and colleagues re-ran the original 1979 problems with 4,098 participants in 19 countries and 13 languages; 94% of the items replicated, though with some weakening of the effects.[^s3] The 1992 parameters, however, came from 25 graduate students, and the fourfold pattern held fully for 22 of them, so the precise numbers should be read as illustrative.[^s2]

Loss aversion, the model's most widely cited component, is disputed. In a 2018 review, Gal and Rucker argued that the evidence does not show losses to be generally more impactful than equivalent gains, and that the idea's popularity owes partly to the persistence of established beliefs in science; they call for a more contextual account of when losses do loom larger.[^s4] The theory is also descriptive: it explains departures from expected utility without claiming they are rational.[^s1]

## Connections

Prospect theory was introduced by Daniel Kahneman and Amos Tversky and is a cornerstone of judgment and decision making and of behavioral economics.[^s1] It contrasts with expected utility theory, the normative benchmark it was built to replace as a description, and it requires that theory to be understood first.[^s1] It is supported by the 2020 multinational replication of its original problems and challenged by Gal and Rucker's critique of loss aversion.[^s3][^s4] It is the usual explanation for framing effects and is invoked for the sunk cost fallacy, since sunk costs place decision makers in the loss domain; its fourfold pattern refines the simple picture of risk aversion.[^s1][^s2] Like bounded rationality, it describes choice as it is rather than as an ideal optimiser would make it.[^s1]

## Sources

[^s1]: Kahneman & Tversky, "Prospect Theory: An Analysis of Decision under Risk", Econometrica 47(2), 263-291 (1979). https://papers.ssrn.com/abstract=1505880 (accessed 2026-11-11)
[^s2]: Tversky & Kahneman, "Advances in Prospect Theory: Cumulative Representation of Uncertainty", Journal of Risk and Uncertainty 5, 297-323 (1992). https://psych.fullerton.edu/mbirnbaum/psych466/articles/Tversky_Kahneman_JRU_92.pdf (accessed 2026-11-11)
[^s3]: Ruggeri et al., "Replicating patterns of prospect theory for decision under risk", Nature Human Behaviour 4(6) (2020). https://research.vu.nl/en/publications/replicating-patterns-of-prospect-theory-for-decision-under-risk/ (accessed 2026-11-11)
[^s4]: Gal & Rucker, "The Loss of Loss Aversion: Will It Loom Larger Than Its Gain?", Journal of Consumer Psychology (2018). https://papers.ssrn.com/abstract=3049660 (accessed 2026-11-11)
