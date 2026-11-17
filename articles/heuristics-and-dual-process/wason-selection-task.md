---
id: ct:wason-selection-task
type: Study
title: Wason selection task
aliases: [four-card selection task, Wason four-card problem, Wason card task]
domain: heuristics-and-dual-process
summary: >-
  Peter Wason's four-card experiment (1966, 1968) in which people choose which
  cards to turn over to test a rule of the form "if p then q". Most choose p and
  q, or p alone, rather than the logically required p and not-q, although some
  rule contents, such as permissions and social exchanges, sharply improve performance.
level: intermediate
evidenceStatus: robust
broader: [ct:psychology-of-reasoning]
related: [ct:peter-wason, ct:modus-tollens, ct:material-conditional, ct:contraposition, ct:confirmation-bias, ct:matching-bias, ct:dual-process-theory, ct:jonathan-st-b-t-evans, ct:conditional-reasoning-training, ct:logical-necessity-instructions, ct:wason-1960-rule-discovery-study, ct:argumentative-theory-of-reasoning, ct:falsifiability]
requires: [ct:material-conditional, ct:modus-tollens]
relations:
  - {predicate: introducedBy, object: ct:peter-wason, source: s5, confidence: high}
  - {predicate: studiedIn, object: ct:psychology-of-reasoning, source: s4, confidence: high}
  - {predicate: explainedBy, object: ct:mental-model-theory, source: s4, confidence: medium}
  - {predicate: explainedBy, object: ct:social-contract-theory, source: s3, confidence: low}
  - {predicate: challengedBy, object: ct:optimal-data-selection-model, source: s2, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Evoking the permission schema: The impact of explicit negation and a violation-checking context"
    publisher: Quarterly Journal of Experimental Psychology 46A(4), 615-635 (Kroger, Cheng & Holyoak, 1993), copy hosted by the UCLA Reasoning Lab
    url: https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/kroger_cheng_holyoak_1993.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "A rational analysis of the selection task as optimal data selection"
    publisher: Psychological Review 101(4), 608-631 (Oaksford & Chater, 1994), copy hosted by UC San Diego
    url: https://pages.ucsd.edu/~mckenzie/OaksfordChaterPsychReview1994.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "The logic of social exchange: Has natural selection shaped how humans reason? Studies with the Wason selection task"
    publisher: Cognition 31, 187-276 (Cosmides, 1989), copy hosted by the UCSB Center for Evolutionary Psychology
    url: https://cep.ucsb.edu/wp-content/uploads/2023/05/socexcog89.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "The Wason selection task: A meta-analysis"
    publisher: Proceedings of the 39th Annual Meeting of the Cognitive Science Society (Ragni, Kola & Johnson-Laird, 2017), eScholarship, University of California
    url: https://escholarship.org/uc/item/3rv0k45d
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "Explanation or modeling: A reply to Kellen and Klauer"
    publisher: Computational Brain & Behavior 3, 354-361 (Ragni & Johnson-Laird, 2020)
    url: https://link.springer.com/article/10.1007/s42113-020-00077-9
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# Wason selection task

The Wason selection task is a short reasoning experiment in which a person sees four cards and a conditional rule, "if p then q", and must say which cards need to be turned over to find out whether the rule is true.[^s1] Each card shows one of four cases, p, not-p, q or not-q, and only the p card and the not-q card could hide a case that breaks the rule.[^s1] Most people instead pick p and q, or p alone, so the task has become a much-studied demonstration that intelligent adults often fail to look for the evidence that could refute a claim.[^s4][^s5]

## Origin

The British psychologist Peter Wason introduced the task at University College London in papers published in 1966 and 1968.[^s5] In its classic abstract form the cards showed letters on one side and numbers on the other, and the rule said that a card with a vowel on one side has an even number on the other.[^s1] In Wason's first four studies only about 4% of participants chose the correct pair.[^s5] Later analyses describe the same core tendency: people check instances that fit the rule and overlook the card that could falsify it.[^s4]

## How it works

The logic is the logic of modus tollens. A rule "if p then q" is broken only by a case with p and not-q, so the p card must be checked for not-q on its back, and the not-q card must be checked for p.[^s1] The q card cannot break the rule whatever is on its back, and neither can the not-p card, because the rule says nothing about cases where p is absent.[^s2]

A workplace version shows why the error matters. An auditor is told: "if an invoice is over $10,000, it carries a second signature." Four files are on the desk: an invoice for $12,000, one for $3,000, one with a second signature and one without. The files that must be opened are the $12,000 invoice and the one without a second signature, the p and not-q cases.[^s1] Opening the signed file is the intuitive choice, but it can only confirm, never refute, the policy; framing such a check as a hunt for violations is what makes people more likely to get it right.[^s1]

## Evidence

The basic pattern is very stable. Oaksford and Chater's 1994 meta-analysis of 34 abstract tasks with 845 participants found the p card chosen by 89% of people, q by 62%, not-q by 25% and not-p by 16%.[^s2] A larger meta-analysis of 228 experiments by Ragni, Kola and Johnson-Laird (2017 conference paper, 2018 *Psychological Bulletin* article) confirmed that people tend to overlook a potentially falsifying card and that card choices are not made independently of one another.[^s4][^s5]

Content changes the picture. Rules about permissions and obligations, such as "if a person is drinking beer, they must be over 18", produce far more correct choices. In one series an abstract permission rule framed as checking for violations yielded 47% correct against 5% for a matched arbitrary rule.[^s1] Leda Cosmides found that unfamiliar rules framed as social exchanges drew the logically correct choice from 71-75% of participants against 21-25% for the same content framed as a description, and argued that people have evolved a mechanism for detecting cheaters.[^s3] Cheng and Holyoak's school explains the same facilitation through learned pragmatic schemas for permission, which a violation-checking context helps to evoke.[^s1]

## Limitations and rival explanations

What the robust result means is disputed. Oaksford and Chater argued that typical choices are a rational strategy for gaining information when p and q are rare, so the q card is genuinely informative and the p-and-q pattern is not simply an error.[^s2] Ragni and colleagues tested 15 later theories and report that most were eliminated; the survivors were their own model-theory account, in which intuition picks instances of the rule and deliberation looks for counterexamples, and the inference-guessing theory of Klauer and colleagues, which fitted less well.[^s4][^s5] Rival modellers dispute that comparison, and the same authors note that online samples give noisier, less informative selections than face-to-face studies.[^s5]

## Connections

The task was **introduced by Peter Wason**, whose early studies set the 4% baseline.[^s5] It is **studied in the psychology of reasoning**, where it is a central paradigm for how people select evidence to test hypotheses.[^s4] Its results are **explained by mental model theory** in the account of Ragni, Kola and Johnson-Laird,[^s4] and, for social-exchange content, **by social contract theory** according to Cosmides, a reading others contest.[^s3][^s1] Its standard reading as a failure of logic is **challenged by the optimal data selection model**.[^s2] It is related to **modus tollens**, **contraposition** and the **material conditional**, which define the correct answer; to **confirmation bias** and **matching bias**, offered as causes of the error; and to **conditional reasoning training** and **logical necessity instructions**, which try to improve performance.[^s1][^s4]

## Sources

[^s1]: Kroger, J. K., Cheng, P. W. & Holyoak, K. J. (1993). "Evoking the permission schema: The impact of explicit negation and a violation-checking context", Quarterly Journal of Experimental Psychology 46A(4), 615-635. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/kroger_cheng_holyoak_1993.pdf (accessed 2026-11-17)
[^s2]: Oaksford, M. & Chater, N. (1994). "A rational analysis of the selection task as optimal data selection", Psychological Review 101(4), 608-631. https://pages.ucsd.edu/~mckenzie/OaksfordChaterPsychReview1994.pdf (accessed 2026-11-17)
[^s3]: Cosmides, L. (1989). "The logic of social exchange: Has natural selection shaped how humans reason? Studies with the Wason selection task", Cognition 31, 187-276. https://cep.ucsb.edu/wp-content/uploads/2023/05/socexcog89.pdf (accessed 2026-11-17)
[^s4]: Ragni, M., Kola, I. & Johnson-Laird, P. N. (2017). "The Wason selection task: A meta-analysis", Proceedings of the 39th Annual Meeting of the Cognitive Science Society. https://escholarship.org/uc/item/3rv0k45d (accessed 2026-11-17)
[^s5]: Ragni, M. & Johnson-Laird, P. N. (2020). "Explanation or modeling: A reply to Kellen and Klauer", Computational Brain & Behavior 3, 354-361. https://link.springer.com/article/10.1007/s42113-020-00077-9 (accessed 2026-11-17)
