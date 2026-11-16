---
id: ct:conductive-argument
type: ReasoningMode
title: Conductive argument
aliases: [conduction, conductive reasoning, pro and con argument, balance-of-considerations argument]
domain: foundations
summary: >-
  An argument in which several separately relevant reasons about a single case,
  often weighed against acknowledged counter-considerations, converge to support
  a conclusion non-conclusively; proposed by Carl Wellman as a third type
  alongside deduction and induction.
level: intermediate
evidenceStatus: contested
broader: [ct:defeasible-reasoning]
related: [ct:argument, ct:argument-evaluation, ct:convergent-argument, ct:pragma-dialectics, ct:weighted-additive-rule, ct:value-based-practical-reasoning, ct:toulmin-model]
requires: [ct:argument]
relations:
  - {predicate: introducedBy, object: ct:carl-wellman, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:deductive-reasoning, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:inductive-reasoning, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:informal-logic, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:applied-ethics, source: s3, confidence: medium}
  - {predicate: challengedBy, object: ct:possin-2016-conductive-arguments-critique, source: s4, confidence: high}
argumentMap:
  premises:
    - "Vendor A's quote is about 20% cheaper than Vendor B's over three years."
    - "Vendor A's tool already integrates with the ticketing system the team uses."
    - "Counter-consideration: Vendor A's onboarding takes about six weeks longer than Vendor B's."
    - "On balance, the lower cost and ready integration outweigh the slower start for a three-year contract."
  conclusion: "The team should choose Vendor A."
  verdict: strong
  objections:
    - "If the project has a hard deadline inside the next two months, the slower onboarding could outweigh the savings."
sources:
  - id: s1
    title: "Two Unreceived Views about Reasoning and Argument (ch. 4 of Problems in Argument Analysis and Evaluation)"
    publisher: Trudy Govier, Windsor Studies in Argumentation (2018)
    url: https://ecampusontario.pressbooks.pub/wsia062018/chapter/4/
    type: academic
    accessed: 2026-11-16
  - id: s2
    title: "A Dialectical View on Conduction: Reasons, Warrants, and Normal Suasory Inclinations"
    publisher: Shiyang Yu and Frank Zenker, Informal Logic 39(1), 32-69 (2019)
    url: https://assets.erudit.tech/fr/revues/informallogic/2019-v39-n1-informallogic04661/1060809ar.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "Conductive Argument"
    publisher: Christian Plantin, Dictionnaire de l'argumentation, ICAR / CNRS (2021)
    url: https://icar.cnrs.fr/dicoplantin/conductive-argument-e/
    type: academic
    accessed: 2026-11-16
  - id: s4
    title: "Conductive Arguments: Why is This Still a Thing?"
    publisher: Kevin Possin, Informal Logic 36(4), 563-593 (2016), PhilArchive record
    url: https://dc2.philarchive.org/rec/POSCAW-4
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "Arguing Conductively or Arguing Strategically?"
    publisher: Yun Xie, OSSA 11 Conference Proceedings, University of Windsor (2016)
    url: https://core.ac.uk/download/84725212.pdf
    type: academic
    accessed: 2026-11-16
created: 2026-11-16
---

# Conductive argument

A conductive argument draws a conclusion about one particular case from several considerations about that same case, each relevant on its own, without appealing to other cases and without claiming that the premises guarantee the conclusion.[^s1] Its best-known form is the "pro and con" or balance-of-considerations argument, in which reasons against the conclusion are stated openly and judged to be outweighed by the reasons for it.[^s2] Everyday deliberation (which job offer to take, which vendor to hire, whether a policy is fair) is full of reasoning of this shape.

## Origin

The ethicist Carl Wellman introduced the term "conduction" in 1971, presenting it as a kind of ethical justification distinct from both deduction and induction, though he did not restrict it to ethics.[^s2] He described three patterns: a conclusion supported by a single reason, by several independent reasons, or by reasons for it together with reasons against it.[^s3] Trudy Govier took up the idea in her teaching and theoretical work from the late 1970s, and argues that it was long neglected because it fell between the deductive and inductive categories that dominated logic at the time.[^s1][^s5] Interest revived after a 2010 symposium at the University of Windsor's Centre for Research in Reasoning, Argumentation and Rhetoric.[^s4]

## How it works

The premises in a conductive argument converge: each counts in favour of the conclusion independently, and together they count for more.[^s1] Nothing links them into a single chain, and no general rule or set of past cases is invoked. In the argument map above, cost and integration are separate reasons, the slower onboarding is a counter-consideration, and an "on balance" premise records the judgment that the pros outweigh the cons. Yu and Zenker propose making that outweighing premise explicit when the argument is diagrammed, since it carries the real weight and is where disagreement usually lies.[^s2]

Because the weighing depends on how much each arguer values each factor, two people can accept every stated reason and still reach opposite verdicts; Plantin illustrates this with a piece of music judged beautiful despite some dissonance by one listener and spoiled by it for another.[^s3] Such arguments typically concern moral or aesthetic values, and their central difficulty is how to rank or balance those values.[^s3]

## How to apply it

To evaluate a conductive argument, you do not test it for deductive validity. Instead, ask whether each premise is acceptable and relevant, how much support each gives, and whether factors the arguer has not mentioned would tip the balance the other way.[^s1] Relevance claims can be checked by imagining other cases in which the factor is present or absent.[^s1] When writing one yourself, state the strongest counter-considerations honestly and say why they are outweighed. Treat the conclusion as defeasible, since new considerations can arrive mid-decision and overturn the balance.[^s2]

## Evidence and limitations

Whether conduction is a genuine third type of argument is disputed. Kevin Possin argues it is not a useful separate category: some supposed examples are really inductive, and others are better read as components of an ordinary position paper.[^s4] Jonathan Adler went further and argued that conductive arguments are not possible at all, while J. Anthony Blair has defended the category against both objections.[^s5] A further puzzle is the logical role of counter-considerations, since a premise that counts against the conclusion does not fit the usual idea of a premise.[^s2] Yun Xie suggests they often serve a rhetorical purpose, such as building the arguer's credibility, and that the moves can be judged by pragma-dialectical rules rather than a separate logic.[^s5] Wellman himself doubted that the considerations could be scored on a common scale, so the weighing is not mechanical.[^s2]

## Connections

Conductive argument is a form of defeasible reasoning; Yu and Zenker treat it as practical, non-monotonic reasoning about what to do.[^s2] Wellman introduced it and defined it in contrast with induction, and Plantin presents it as a third type beside deduction and induction.[^s1][^s3] It is studied mainly in informal logic, where the journal *Informal Logic* has hosted much of the debate.[^s2] Its most common setting is moral and aesthetic evaluation.[^s3] It relies on convergent rather than linked support,[^s1] and Possin's critique challenges its status as a separate type.[^s4] Xie's analysis connects it to pragma-dialectics.[^s5] The weighing step resembles a weighted-additive decision rule, though Wellman denied that the weights can be calculated.[^s2]

## Sources

[^s1]: Govier, "Two Unreceived Views about Reasoning and Argument", *Problems in Argument Analysis and Evaluation*, Windsor Studies in Argumentation, 2018. https://ecampusontario.pressbooks.pub/wsia062018/chapter/4/ (accessed 2026-11-16)
[^s2]: Yu and Zenker, "A Dialectical View on Conduction: Reasons, Warrants, and Normal Suasory Inclinations", *Informal Logic* 39(1), 2019. https://assets.erudit.tech/fr/revues/informallogic/2019-v39-n1-informallogic04661/1060809ar.pdf (accessed 2026-11-16)
[^s3]: Plantin, "Conductive Argument", *Dictionnaire de l'argumentation*, ICAR/CNRS, 2021. https://icar.cnrs.fr/dicoplantin/conductive-argument-e/ (accessed 2026-11-16)
[^s4]: Possin, "Conductive Arguments: Why is This Still a Thing?", *Informal Logic* 36(4), 2016. https://dc2.philarchive.org/rec/POSCAW-4 (accessed 2026-11-16)
[^s5]: Xie, "Arguing Conductively or Arguing Strategically?", OSSA 11 Proceedings, 2016. https://core.ac.uk/download/84725212.pdf (accessed 2026-11-16)
