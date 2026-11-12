---
id: ct:reversal-test
type: Technique
title: Reversal test
aliases: [Bostrom-Ord reversal test, double reversal test]
domain: debiasing-and-metacognition
summary: >-
  A check for status quo bias: when a change to some quantity seems bad,
  ask whether the opposite change would also be bad. If both directions
  seem worse, you owe a reason why the current value happens to be the
  best one; lacking it, suspect the preference comes from bias.
level: intermediate
evidenceStatus: contested
broader: [ct:debiasing]
related: [ct:status-quo-bias, ct:consider-the-opposite, ct:burden-of-proof, ct:loss-aversion, ct:omission-bias, ct:endowment-effect]
requires: [ct:status-quo-bias]
relations:
  - {predicate: introducedBy, object: ct:nick-bostrom, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:toby-ord, source: s1, confidence: high}
  - {predicate: detects, object: ct:status-quo-bias, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:status-quo-bias, source: s1, confidence: medium}
  - {predicate: appliedIn, object: ct:applied-ethics, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:clarke-2016-reversal-test-critique, source: s3, confidence: high}
  - {predicate: challengedBy, object: ct:nebel-2015-status-quo-conservatism-about-value, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "The Reversal Test: Eliminating Status Quo Bias in Applied Ethics"
    publisher: Ethics 116(4), 656-679 (Bostrom & Ord, 2006), author's copy
    url: https://www.nickbostrom.com/ethics/statusquo.pdf
    type: primary
    accessed: 2026-11-12
  - id: s2
    title: "Status Quo Bias, Rationality, and Conservatism about Value"
    publisher: Ethics 125(2), 449-476 (Nebel, 2015), PhilArchive copy
    url: https://philarchive.org/archive/NEBSQB
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "The Reversal Test, Status Quo Bias, and Opposition to Human Cognitive Enhancement"
    publisher: Canadian Journal of Philosophy 46(3), 369-386 (Clarke, 2016), Cambridge University Press
    url: https://www.cambridge.org/core/journals/canadian-journal-of-philosophy/article/reversal-test-status-quo-bias-and-opposition-to-human-cognitive-enhancement/7F2FF188835015750D9C1EF5CDB7E904
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Reversal test

The reversal test is a thinking check for status quo bias, the tendency to favour an option simply because it keeps things as they are. When a proposed change to some continuous parameter strikes you as bad, you imagine changing the same parameter by a similar amount in the opposite direction. If that change also strikes you as bad, you take on a burden: explain why the present value is the best one. If no good explanation is available, the double rejection is a sign that the preference is coming from bias rather than from reasons.[^s1]

## Origin

Philosophers Nick Bostrom and Toby Ord, both at the University of Oxford, introduced the test in a 2006 paper in *Ethics*.[^s1] Their target was applied ethics, where judgments about long-run consequences rest heavily on intuition. They drew on the behavioural-economics literature on status quo bias, including Samuelson and Zeckhauser's choice experiments, the endowment-effect "mug" studies, and framing effects attributed to loss aversion. They argued that such a bias could quietly shape intuitions about novel interventions.[^s1] Their running example was a hypothetical safe and affordable way to raise human intelligence. In the same paper they added a *double reversal test* for cases where the opposite change is hard to picture.[^s1]

## How it works

The logic turns on the shape of the option space. A continuous parameter, such as a budget, a speed limit, a review cycle or a staffing level, can take many values. Only a few of them can be local optima, where any small move in either direction makes things worse. Someone who rejects both an increase and a decrease is implicitly claiming that the current value is one of those rare optima. Bostrom and Ord argue that this claim needs support, so the burden of proof shifts to whoever makes it.[^s1]

A workplace example: a team lead objects to a proposal to move the weekly status meeting to every two weeks, saying people will lose touch. The reversal question is whether the meeting should then happen twice a week. If the lead objects to that as well ("too much time in meetings"), they should be able to say why weekly is the sweet spot, for example because project milestones fall weekly. If the only reason is "that's how we've always done it", the objection to the original proposal deserves less weight, which is the inference the test licenses.[^s1]

The **double reversal test** handles changes that are hard to imagine in reverse. Suppose some outside factor is about to push the parameter away from its current value, and we would judge it good to offset that push. Now suppose the factor later disappears. If we would judge it bad to undo our offsetting move, we are in effect endorsing the new value for its own sake. That makes it awkward to oppose reaching that value directly.[^s1]

## How to apply it

1. Name the parameter that the proposal changes, and check that it can vary in both directions.
2. State your verdict on the proposed change, then judge an equal change the other way.
3. If you reject both, write down the reason the current value is optimal.
4. Test that reason against the legitimate grounds Bostrom and Ord list: the current value may reflect long adaptation to stable conditions, switching may carry transition costs, or change may bring risks that outweigh the expected gains.[^s1]
5. If none of these grounds holds, treat your initial objection as possibly biased and re-examine the proposal on its merits.

The authors themselves stress the limits. The test diagnoses a possible bias but does not replace judgment. It gives clearer verdicts for small changes than for large ones, and it cannot settle disputes that turn on side constraints rather than consequences.[^s1]

## Evidence

The reversal test is a normative heuristic, not an experimentally validated intervention. It borrows its rationale from empirical work on status quo bias, but the test itself has not been trialled as a debiasing method. Its scope is philosophically disputed, so its status is best called contested.[^s1][^s2][^s3] Nebel argues that a preference for the status quo is sometimes rational, because there is reason to preserve existing things of value even when replacements would be just as good. On that view, a person can reject change in both directions without being biased. Nebel still accepts the test as a fallible guide rather than a definition of bias.[^s2] Clarke argues that the standard statement of the test needs revising and that its burden of proof is unclear. He also argues that the burden can be met in a way the originators overlooked, and that the test applies usefully in fewer situations than they claimed.[^s3]

## Connections

- **Detects and counteracts** `ct:status-quo-bias`: the test was designed to reveal and correct an irrational preference for the current state.[^s1]
- **Broader:** `ct:debiasing`; it is a self-check strategy in the same family as `ct:consider-the-opposite`, in that both force attention to the neglected alternative.[^s1]
- **Introduced by** `ct:nick-bostrom` and `ct:toby-ord` (2006), and **applied in** `ct:applied-ethics`, notably debates on human enhancement.[^s1]
- **Related:** `ct:loss-aversion`, `ct:omission-bias` and `ct:endowment-effect`, the mechanisms and effects the originators cite as sources of the bias; and `ct:burden-of-proof`, which the test reallocates.[^s1]
- **Challenged by** Nebel's conservatism-about-value argument (2015) and Clarke's critique (2016).[^s2][^s3]

## Sources

[^s1]: Bostrom & Ord, "The Reversal Test: Eliminating Status Quo Bias in Applied Ethics", *Ethics* 116 (2006). https://www.nickbostrom.com/ethics/statusquo.pdf (accessed 2026-11-12)
[^s2]: Nebel, "Status Quo Bias, Rationality, and Conservatism about Value", *Ethics* 125 (2015). https://philarchive.org/archive/NEBSQB (accessed 2026-11-12)
[^s3]: Clarke, "The Reversal Test, Status Quo Bias, and Opposition to Human Cognitive Enhancement", *Canadian Journal of Philosophy* 46 (2016). https://www.cambridge.org/core/journals/canadian-journal-of-philosophy/article/reversal-test-status-quo-bias-and-opposition-to-human-cognitive-enhancement/7F2FF188835015750D9C1EF5CDB7E904 (accessed 2026-11-12)
