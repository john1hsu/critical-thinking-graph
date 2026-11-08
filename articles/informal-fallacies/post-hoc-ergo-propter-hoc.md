---
id: ct:post-hoc-ergo-propter-hoc
type: InformalFallacy
title: Post hoc ergo propter hoc
aliases: [post hoc fallacy, post hoc reasoning, after this therefore because of this, temporal sequence fallacy]
domain: informal-fallacies
summary: >-
  The fallacy of concluding that one event caused another merely because the
  first came before the second, treating temporal sequence alone as proof of a
  causal connection.
level: introductory
evidenceStatus: normative
broader: [ct:false-cause, ct:informal-fallacy]
related: [ct:correlation-versus-causation, ct:regression-to-the-mean, ct:randomized-controlled-trial, ct:hasty-generalization, ct:slippery-slope, ct:confounding]
requires: [ct:inductive-reasoning]
relations:
  - {predicate: instanceOf, object: ct:false-cause, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:argument-from-correlation-to-cause, source: s2, confidence: medium}
  - {predicate: contrastsWith, object: ct:cum-hoc-ergo-propter-hoc, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:causal-illusion, source: s3, confidence: medium}
criticalQuestions:
  - Apart from the order of events, what independent evidence links the earlier event to the later one?
  - Would the later event probably have happened anyway, for example through seasonal patterns, spontaneous recovery or a return from an unusual extreme?
  - Did anything else change at the same time that could explain the outcome?
  - How often does the outcome occur when the supposed cause is absent?
  - Is there a plausible mechanism, and has the pattern held up across repeated or controlled comparisons?
argumentMap:
  premises:
    - "The office switched to a new IT help-desk ticketing tool in March."
    - "Complaints about slow IT support fell sharply in April."
  conclusion: "So the new ticketing tool reduced complaints."
  verdict: fallacious
  objections:
    - "February had an unusual spike of outages, so complaints may simply have returned to their normal level."
    - "Two extra support staff were hired in March, which could explain the drop on its own."
    - "No comparison with teams still on the old tool, or with previous Aprils, was made."
sources:
  - id: s1
    title: "Fallacies"
    publisher: Internet Encyclopedia of Philosophy (Dowden)
    url: https://iep.utm.edu/fallacy/
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s2
    title: "Correlation and Cause (ch. 9 of Fallacies and Argument Appraisal)"
    publisher: Cambridge University Press (Tindale, 2007)
    url: https://www.cambridge.org/core/books/abs/fallacies-and-argument-appraisal/correlation-and-cause/B86D8252C4E1E1E344F094ADA51254D9
    type: textbook
    accessed: 2026-11-08
  - id: s3
    title: "Illusions of causality: how they bias our everyday thinking and how they could be reduced"
    publisher: Frontiers in Psychology 6:888 (Matute, Blanco, Yarritu, Diaz-Lago, Vadillo & Barberia, 2015)
    url: https://www.frontiersin.org/articles/10.3389/fpsyg.2015.00888/pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s4
    title: "Arguments from Correlation to Causation (ch. 6 of Argument Evaluation and Evidence)"
    publisher: Springer, Law, Governance and Technology Series 23 (Walton, 2016)
    url: https://rd.springer.com/chapter/10.1007/978-3-319-19626-8_6
    type: primary
    accessed: 2026-11-08
  - id: s5
    title: "Fallacy of false cause"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/fallacy-of-false-cause
    type: encyclopedia
    accessed: 2026-11-08
created: 2026-11-08
---

# Post hoc ergo propter hoc

*Post hoc ergo propter hoc* (Latin, roughly "after this, therefore because of this") is the error of noticing that event A was followed by event B and then hastily concluding that A caused B.[^s1] It is the most common form of the fallacy of false cause, which wrongly locates the cause of one thing in another that only seems connected to it; the defect lies in the content of the reasoning rather than in its logical form.[^s5] Bradley Dowden's illustration is a sports fan who buys expensive seats and sees his team win, buys cheap seats and sees it lose, and decides that his ticket choice decides the score.[^s1]

## Origin

The Latin label names a pattern long catalogued under the older heading *non causa pro causa* ("non-cause for cause"), the general family of false-cause errors.[^s5] Modern informal-logic texts keep post hoc as a distinct member of that family. Dowden lists it as one of four principal kinds of false cause, alongside *cum hoc ergo propter hoc*, neglect of regression, and reversing cause and effect.[^s1] Christopher Tindale's 2007 textbook treats it as the first of three problematic causal patterns, together with misidentified cause and slippery slope, and frames all three against a legitimate scheme, the argument from correlation to cause.[^s2]

## How it works

Time order is real evidence: a cause must come before its effect, and close succession is one of the cues people normally and often correctly use to infer causation.[^s3] The fallacy is to let that one cue settle the question. In the argument map above, a manager sees complaints about IT support fall the month after a new ticketing tool arrived and credits the tool. Both premises can be true while the conclusion is unwarranted: complaints may have been unusually high just before, new staff may have been hired in the same month, and nothing was compared with a period or team without the tool.[^s1][^s2] Dowden stresses that the mistake is jumping to the causal conclusion too quickly; a causal claim backed by more than the sequence of events can be perfectly reasonable.[^s1]

## How to spot it

Watch for arguments whose only causal evidence is "before" and "after": a remedy taken and then a recovery, a policy launched and then a better quarter, a ritual performed and then a win.[^s1][^s5] Tindale notes that clear cases are easy to spot, but because there is no agreed analysis of causation, many real cases are contentious and need the conditions of the correlation-to-cause scheme checked one by one.[^s2] Be especially wary where the outcome tends to happen anyway. Matute and colleagues point out that alternative practitioners provide a large share of primary care for back pain, a condition with high spontaneous remission, so improvement after treatment is common whether or not the treatment works.[^s3]

## How to counter it

Ask the critical questions above: what else changed, would the outcome have happened anyway, and how often does it occur without the supposed cause? Douglas Walton argues that argumentation tools built around the correlation-to-cause scheme let a critic judge whether a causal inference is reasonable and settle disputes over whether a conclusion was hasty.[^s4] The decisive move is a comparison: the same outcome measured where the supposed cause was absent, ideally in a controlled test.[^s3] Teaching that move works in at least one study. Barberia and colleagues (2013) had adolescents test a supposed miracle product, then taught them to control for confounding variables; compared with a control group, they tested the product more sparingly and showed a weaker causal illusion.[^s3]

## Evidence

As a normative standard, the fallacy's status rests on logic rather than experiment, but psychology explains why it is so tempting. In contingency-judgment experiments reviewed by Matute and colleagues (2015), participants rate a fictitious drug as effective even when recovery is equally likely without it. The illusion grows when the outcome is frequent and when the supposed cause is often present, because both produce more coincidences.[^s3] The same review reports that providing an alternative cause weakens the illusion and that the error is not confined to people of low intelligence.[^s3] That review summarises one research group's work, so its specific effect sizes should not be generalised without the wider literature.[^s3]

## Connections

Post hoc is an **instance of false cause**, the family that also includes cum hoc and neglect of regression.[^s1][^s5] It **contrasts with cum hoc ergo propter hoc**, which infers causation from any chance co-occurrence rather than from time order specifically.[^s1] It **contrasts with the argument from correlation to cause**, a scheme that Tindale calls reasonable when its conditions are met; post hoc is what that reasoning becomes when they are not.[^s2] The **causal illusion** studied by experimental psychologists, fed by temporal contiguity and frequent coincidences, helps **explain** why the inference feels compelling.[^s3] Related topics include **regression to the mean** (an outcome returning to normal after an extreme), **confounding**, the broader distinction between **correlation and causation**, the **randomized controlled trial** as the standard remedy, **hasty generalization**, and the **slippery slope**, which Tindale groups with post hoc as a causal fallacy.[^s1][^s2][^s3]

## Sources

[^s1]: Dowden, "Fallacies", Internet Encyclopedia of Philosophy. https://iep.utm.edu/fallacy/ (accessed 2026-11-08)
[^s2]: Tindale, "Correlation and Cause", ch. 9 of *Fallacies and Argument Appraisal*, Cambridge University Press, 2007. https://www.cambridge.org/core/books/abs/fallacies-and-argument-appraisal/correlation-and-cause/B86D8252C4E1E1E344F094ADA51254D9 (accessed 2026-11-08)
[^s3]: Matute, Blanco, Yarritu, Diaz-Lago, Vadillo & Barberia, "Illusions of causality: how they bias our everyday thinking and how they could be reduced", Frontiers in Psychology 6:888 (2015). https://www.frontiersin.org/articles/10.3389/fpsyg.2015.00888/pdf (accessed 2026-11-08)
[^s4]: Walton, "Arguments from Correlation to Causation", ch. 6 of *Argument Evaluation and Evidence*, Springer, 2016. https://rd.springer.com/chapter/10.1007/978-3-319-19626-8_6 (accessed 2026-11-08)
[^s5]: "Fallacy of false cause", Encyclopaedia Britannica. https://www.britannica.com/topic/fallacy-of-false-cause (accessed 2026-11-08)
