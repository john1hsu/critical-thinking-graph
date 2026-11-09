---
id: ct:fast-and-frugal-heuristics
type: Framework
title: Fast-and-frugal heuristics
aliases: [simple heuristics program, adaptive toolbox, fast and frugal heuristics program]
domain: heuristics-and-dual-process
summary: >-
  The research program, launched by Gerd Gigerenzer and colleagues in the
  mid-1990s, that models judgment as the use of simple, precisely specified
  rules which search little information, stop early and decide on one or a few
  cues, and that judges such rules by how well they fit the structure of the
  environment rather than by logical or statistical norms.
level: intermediate
evidenceStatus: contested
broader: [ct:bounded-rationality]
related: [ct:recognition-heuristic, ct:satisficing, ct:ecological-rationality, ct:heuristics-and-biases-program, ct:dual-process-theory, ct:gerd-gigerenzer, ct:overfitting, ct:herbert-simon]
requires: [ct:bounded-rationality]
relations:
  - {predicate: introducedBy, object: ct:gerd-gigerenzer, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:reasoning-the-fast-and-frugal-way, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:herbert-simon, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:ecological-rationality, source: s2, confidence: medium}
  - {predicate: contrastsWith, object: ct:heuristics-and-biases-program, source: s2, confidence: medium}
  - {predicate: appliedIn, object: ct:medicine, source: s5, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:phillips-2017-fftrees-benchmark, source: s4, confidence: medium}
  - {predicate: challengedBy, object: ct:pohl-2011-recognition-heuristic-debate-review, source: s3, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Reasoning the fast and frugal way: Models of bounded rationality"
    publisher: Psychological Review 103(4), 650-669 (Gigerenzer & Goldstein, 1996), author's copy
    url: https://www.dangoldstein.com/papers/FastFrugalPsychReview.pdf
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "Heuristic decision making"
    publisher: Annual Review of Psychology 62, 451-482 (Gigerenzer & Gaissmaier, 2011), University of Konstanz repository record
    url: https://kops.uni-konstanz.de/entities/publication/641996fe-73e8-4d82-b940-1e49598102ac
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "On the use of recognition in inferential decision making: An overview of the debate"
    publisher: Judgment and Decision Making 6(5), 423-438 (Pohl, 2011)
    url: https://core-prod.cambridgecore.org/core/services/aop-cambridge-core/content/view/740657BB9CD07AC20033402527379F85/S1930297500001388a.pdf/on-the-use-of-recognition-in-inferential-decision-making-an-overview-of-the-debate.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "FFTrees: A toolbox to create, visualize, and evaluate fast-and-frugal decision trees"
    publisher: Judgment and Decision Making 12(4), 344-368 (Phillips, Neth, Woike & Gaissmaier, 2017)
    url: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EBA944267A2D0EE5970471B38BC1CA84/S1930297500006239a.pdf/fftrees-a-toolbox-to-create-visualize-and-evaluate-fast-and-frugal-decision-trees.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s5
    title: "Heuristic decision making in medicine"
    publisher: Dialogues in Clinical Neuroscience 14(1) (Marewski & Gigerenzer, 2012)
    url: https://informahealthcare.com/doi/full/10.31887/DCNS.2012.14.1/jmarewski
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s6
    title: "Towards competitive instead of biased testing of heuristics: A reply to Hilbig and Richter (2011)"
    publisher: Topics in Cognitive Science 3, 197-205 (Brighton & Gigerenzer, 2011), Max Planck Society repository
    url: https://pure.mpg.de/pubman/item/item_2098985_1/component/file_2098984/HB_Towards_2011.pdf
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# Fast-and-frugal heuristics

Fast-and-frugal heuristics are simple decision rules that deliberately ignore part of the available information: they look up few cues, stop searching as soon as one cue settles the matter, and decide without weighing and adding everything.[^s1][^s2] The research program built around them, often called the *adaptive toolbox* or simple heuristics program, treats the question of whether such a rule is good as empirical. A heuristic is rational to the extent that it fits the structure of the environment it is used in, which the program calls *ecological rationality*.[^s2]

## Origin

Gerd Gigerenzer and Daniel Goldstein introduced the approach in a 1996 *Psychological Review* paper. They argued that classical models of rational inference assume unlimited time, knowledge and computation, and proposed instead a family of satisficing algorithms based on one-reason decision making, explicitly extending Herbert Simon's idea that people stop searching once an option meets their aspiration.[^s1] They also stressed that bounded rationality has an ecological side as well as a cognitive one: a rule's success depends on how cue validities and redundancies are distributed in the world.[^s1] Gigerenzer and Wolfgang Gaissmaier's 2011 *Annual Review of Psychology* survey summarised the program's later development in business, legal and medical decision making, and named a systematic theory of heuristic building blocks as its main open challenge.[^s2]

## How it works

Each heuristic is specified precisely enough to simulate, using three building blocks: a **search rule** (which cues to look up, in what order), a **stopping rule** (when to stop), and a **decision rule** (how to choose).[^s5] The flagship example is *Take The Best*. To judge which of two German cities is larger, first apply the recognition principle: if you recognise only one, pick it. Otherwise check cues in order of validity (is it a state capital? does it have a top-league football team?) and stop at the first cue on which the two cities differ.[^s1] In simulations on all 3,403 pairs of the 83 German cities above 100,000 inhabitants, Take The Best matched multiple regression in accuracy (about 69% at full knowledge) while looking up on average 5.9 of 20 cue values.[^s1] The same simulations produced a *less-is-more effect*: because recognition carries information, simulated people who knew fewer cities could sometimes infer more accurately than people who knew more.[^s1]

A workplace version is the *fast-and-frugal tree*, a yes/no checklist in which every question can end the decision. A hospital tree for chest-pain patients asks first about one ECG anomaly (yes sends the patient to coronary care), then whether chest pain is the chief complaint, then about a short list of further signs. In the reported comparison it caught more heart attacks with fewer false alarms than a regression-based instrument, while using a fraction of the information.[^s5]

## How to apply it

Use a simple rule when data are scarce, the future is uncertain, or the decision must be transparent and fast; build it from the few best cues, order them, and test it on *new* cases rather than on how well it fits the past.[^s5][^s2] The rationale is overfitting: a model that weights many cues can fit past noise and then predict worse.[^s5] Prefer a weighted model when many weak cues jointly carry the signal, since one-reason rules can miss it.[^s4]

## Evidence

Out-of-sample comparisons are encouraging but not uniform. In a 2017 benchmark over 10 public datasets, fast-and-frugal trees reached a mean balanced accuracy of 0.83, the same as random forests and regularised logistic regression and slightly ahead of plain logistic regression (0.82), while using about 1.8 cues per case; they did much worse than other methods on one dataset.[^s4] The descriptive claim that people actually use these rules is more disputed. A 2011 review of the recognition-heuristic debate found that high rates of choosing the recognised option do not prove the rule was used, that less-is-more effects in people are scarce and small, that reaction-time data mostly favour evidence-accumulation accounts, and that individuals differ widely.[^s3] Defenders reply that heuristics should be tested competitively against other process models rather than against near-perfect consistency thresholds, and that people select strategies adaptively, so use should track how valid recognition is in a given environment.[^s6] The evidence status is therefore *contested*: the normative "less can be more" result is well supported, while the descriptive account of strategy selection remains open.[^s3][^s6]

## Connections

- Its parent idea is **bounded rationality**, and it was **influenced by** Herbert Simon's satisficing, which the 1996 paper explicitly extends.[^s1]
- It was **introduced by** Gerd Gigerenzer, with Daniel Goldstein, **in** *Reasoning the fast and frugal way*.[^s1]
- It is **explained by** ecological rationality, the fit between a rule and its environment.[^s2]
- It **contrasts with** the heuristics-and-biases program, which measures heuristics against logical and statistical norms and stresses their errors; it is **studied in** judgment and decision making.[^s2]
- It is **applied in** medicine through fast-and-frugal trees for triage and diagnosis.[^s5]
- It is **supported by** the 2017 FFTrees benchmark and **challenged by** Pohl's 2011 review of the recognition-heuristic debate.[^s4][^s3]
- It is related to the recognition heuristic, satisficing, overfitting and dual-process theory, and to Gigerenzer's work more broadly.[^s1][^s5]

## Sources

[^s1]: Gigerenzer & Goldstein, "Reasoning the fast and frugal way: Models of bounded rationality", *Psychological Review* 103(4), 1996. https://www.dangoldstein.com/papers/FastFrugalPsychReview.pdf (accessed 2026-11-09)
[^s2]: Gigerenzer & Gaissmaier, "Heuristic decision making", *Annual Review of Psychology* 62, 2011. https://kops.uni-konstanz.de/entities/publication/641996fe-73e8-4d82-b940-1e49598102ac (accessed 2026-11-09)
[^s3]: Pohl, "On the use of recognition in inferential decision making: An overview of the debate", *Judgment and Decision Making* 6(5), 2011. https://core-prod.cambridgecore.org/core/services/aop-cambridge-core/content/view/740657BB9CD07AC20033402527379F85/S1930297500001388a.pdf/on-the-use-of-recognition-in-inferential-decision-making-an-overview-of-the-debate.pdf (accessed 2026-11-09)
[^s4]: Phillips, Neth, Woike & Gaissmaier, "FFTrees: A toolbox to create, visualize, and evaluate fast-and-frugal decision trees", *Judgment and Decision Making* 12(4), 2017. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EBA944267A2D0EE5970471B38BC1CA84/S1930297500006239a.pdf/fftrees-a-toolbox-to-create-visualize-and-evaluate-fast-and-frugal-decision-trees.pdf (accessed 2026-11-09)
[^s5]: Marewski & Gigerenzer, "Heuristic decision making in medicine", *Dialogues in Clinical Neuroscience* 14(1), 2012. https://informahealthcare.com/doi/full/10.31887/DCNS.2012.14.1/jmarewski (accessed 2026-11-09)
[^s6]: Brighton & Gigerenzer, "Towards competitive instead of biased testing of heuristics: A reply to Hilbig and Richter (2011)", *Topics in Cognitive Science* 3, 2011. https://pure.mpg.de/pubman/item/item_2098985_1/component/file_2098984/HB_Towards_2011.pdf (accessed 2026-11-09)
