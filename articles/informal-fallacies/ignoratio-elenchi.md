---
id: ct:ignoratio-elenchi
type: InformalFallacy
title: Ignoratio elenchi
aliases: [irrelevant conclusion, missing the point, ignorance of refutation, wrong conclusion fallacy]
domain: informal-fallacies
summary: >-
  The fallacy of offering an argument, often a perfectly good one, for a
  conclusion other than the one actually at issue, so that it misses the point
  it was meant to establish or refute.
level: introductory
evidenceStatus: normative
broader: [ct:informal-fallacy]
related: [ct:straw-man-fallacy, ct:begging-the-question, ct:sophistical-refutations, ct:richard-whately, ct:argument-mapping, ct:fallacies-of-relevance]
requires: [ct:argument]
relations:
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:red-herring, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:non-sequitur, source: s3, confidence: medium}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s2, confidence: medium}
criticalQuestions:
  - What exactly is the conclusion in dispute, stated in one sentence?
  - What conclusion do the premises actually support, and is it the same claim?
  - If the argument succeeds completely, does the disputed claim stand or fall, or is it untouched?
  - Does the argument contradict the opponent's thesis in the same respect, at the same time and about the same thing?
  - Is there a definite alternative conclusion being argued for, or is the argument simply drifting away from the issue?
argumentMap:
  premises:
    - "The question on the table is whether the new expense tool should replace the old one next quarter."
    - "The finance lead shows that the new tool's dashboards are more attractive and that its vendor has won design awards."
  conclusion: "So we should switch to the new expense tool next quarter."
  verdict: fallacious
  objections:
    - "The evidence supports 'the new tool looks better', not 'switching next quarter is worth the cost and disruption'."
    - "Nothing in the argument addresses migration effort, accuracy of reimbursements or staff training, which the decision turns on."
sameAs: []
sources:
  - id: s1
    title: "On Sophistical Refutations (Parts 5-6)"
    publisher: "Aristotle, trans. W. A. Pickard-Cambridge, The Internet Classics Archive (MIT)"
    url: https://classics.mit.edu/Aristotle/sophist_refut.1.1.html
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "Classification of Fallacies of Relevance"
    publisher: "Informal Logic 24(1), 71-103 (Douglas Walton, 2004)"
    url: https://distantreader.org/stacks/journals/il/il-2133.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "Ignoratio Elenchi (Irrelevant Conclusion)"
    publisher: "Philosophy 103: Introduction to Logic, Lander University (Lee C. Archie)"
    url: https://philosophy.lander.edu/logic/ignoratio.html
    type: academic
    accessed: 2026-11-09
created: 2026-11-09
---

# Ignoratio elenchi

*Ignoratio elenchi*, Latin for "ignorance of the refutation" and usually rendered in English as *irrelevant conclusion* or *missing the point*, is the fallacy of arguing for a conclusion other than the one in dispute.[^s3] What makes it distinctive is that the argument itself may be valid and its premises well supported. The fault is that it lands on the wrong target, so even complete success leaves the real question unanswered.[^s2][^s3]

## Origin

The name comes from Aristotle's *On Sophistical Refutations*, the first systematic catalogue of fallacies. Aristotle defines a genuine refutation as proving the contradictory of the opponent's thesis about the same attribute, and in the same respect, relation, manner and time.[^s1] An apparent refutation that drops one of these conditions has only the look of a refutation, and he lists "ignorance of what refutation is" among the fallacies that do not depend on language.[^s1] In Part 6 he goes further, suggesting that every type of apparent refutation can be traced back to some failure of this definition. On that reading, *ignoratio elenchi* is both one fallacy and a diagnosis of all of them.[^s1]

Later logic changed the term's meaning. Lee Archie's Lander University logic notes distinguish three senses. In the narrow Aristotelian sense, a disputant proves something that does not contradict the opponent's thesis. In the traditional sense, the premises are irrelevant to the conclusion. In the catch-all sense, many modern textbooks use the label for any fallacy of relevance that lacks a more specific name.[^s3] Douglas Walton notes that Richard Whately supplied many of the classic nineteenth-century examples, and that textbooks such as Copi and Cohen's equate *ignoratio elenchi* with "irrelevant conclusion".[^s2]

## How it works

Walton reduces the fallacy to three elements: an actual conclusion that the premises support, a proper conclusion that ought to be supported, and a gap between the two.[^s2] The argument map above shows a workplace version. The decision is whether to replace an expense tool next quarter. The finance lead's evidence about attractive dashboards and design awards may be accurate, and it does support a conclusion: the new tool looks better. But that is not the claim at issue. The case for switching turns on cost, migration effort and accuracy, and none of the evidence bears on these.[^s2] The argument therefore borrows the credibility of a sound sub-argument and attaches it to an unproved claim.

The classic textbook illustration has the same shape. Arguing that people untrained in logic often reason well does not show that studying logic is of little use. The premises may be true, but they bear on a different question.[^s3]

## How to spot it

- **Restate the issue.** Write down the disputed claim in one sentence, then the conclusion the premises actually reach. If the two differ, you have found a candidate.[^s2]
- **Apply the refutation test.** In a disagreement, ask whether the reply contradicts the other side's thesis on the same point, in the same respect and at the same time. A reply that only seems to contradict it fails Aristotle's test.[^s1]
- **Map the argument.** Walton analyses examples by diagramming them and tracking where their probative weight lands. If the weight falls on a different conclusion and none falls on the proper one, the argument is a wrong-conclusion fallacy.[^s2]
- **Separate it from neighbours.** A *non sequitur* is simply invalid, whereas an *ignoratio elenchi* can be valid but aimed at the wrong point.[^s3] A straw man misrepresents the opponent's position and attacks the distorted version, and Archie's notes treat it as one specific type of *ignoratio elenchi*.[^s3]

## How to counter it

The simplest reply is to name the gap and tell the arguer they have reached the wrong conclusion. Walton gives this as the standard challenge to a wrong-conclusion argument.[^s2] Grant whatever the argument does establish, then bring the discussion back to the claim at issue and ask what evidence bears on that. In meetings, writing the decision question at the top of the agenda or document makes drift easier to notice. When the problem is a diversion with no definite rival conclusion, Walton's alternative challenge works better: "Where are you going with this line of argument?"[^s2]

## Evidence

The fallacy is defined by a normative standard, not an empirical finding. What remains disputed is classification. Walton shows that textbooks disagree over whether red herring is a subspecies of irrelevant conclusion (Copi and Cohen) or a separate fallacy closely tied to missing the point (Hurley). He also finds that some textbook examples can be read either way.[^s2] He proposes four criteria for the wrong-conclusion fallacy and three for red herring. His heuristic is to classify a case as wrong conclusion when a definite alternative conclusion can be identified, and as red herring when there is doubt about that but clear evidence of a strategic diversion.[^s2] The label's broad modern use as a catch-all for irrelevance is a further source of confusion that critics should keep in mind.[^s3]

## Connections

- **Introduced by Aristotle.** *On Sophistical Refutations* names ignorance of refutation as a fallacy outside language and uses it to unify the whole catalogue.[^s1]
- **Contrasts with red herring.** In Walton's 2004 classification, *ignoratio elenchi* argues to a specific wrong conclusion. Red herring diverts the discussion without reaching any definite conclusion.[^s2]
- **Contrasts with non sequitur.** A *non sequitur*'s conclusion does not follow from its premises. An *ignoratio elenchi* may follow perfectly and still miss the issue.[^s3]
- **Studied in argumentation theory.** Walton's analysis treats relevance in terms of dialogue structure and probative weight, using argument diagramming as the diagnostic tool.[^s2]
- **Related to straw man and begging the question.** The straw man is a species of missing the point, and Aristotle discussed begging the question alongside it in the same catalogue.[^s1][^s3]

## Sources

[^s1]: Aristotle, *On Sophistical Refutations*, Parts 5-6, trans. W. A. Pickard-Cambridge, The Internet Classics Archive. https://classics.mit.edu/Aristotle/sophist_refut.1.1.html (accessed 2026-11-09)
[^s2]: Walton, "Classification of Fallacies of Relevance", *Informal Logic* 24(1), 2004, 71-103. https://distantreader.org/stacks/journals/il/il-2133.pdf (accessed 2026-11-09)
[^s3]: Archie, "Ignoratio Elenchi (Irrelevant Conclusion)", Philosophy 103: Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/ignoratio.html (accessed 2026-11-09)
