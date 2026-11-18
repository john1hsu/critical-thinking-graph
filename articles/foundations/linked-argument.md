---
id: ct:linked-argument
type: Concept
title: Linked argument
aliases: [linked premises, linked support, dependent premises, dependent reasons, coordinate argumentation, linked argumentation]
domain: foundations
summary: >-
  An argument structure in which two or more premises support the conclusion
  only in combination, each filling a gap the others leave, so that a single
  unacceptable premise can defeat the whole inference.
level: introductory
evidenceStatus: normative
broader: [ct:argument]
related: [ct:convergent-argument, ct:argument-mapping, ct:argument-reconstruction, ct:argument-evaluation, ct:syllogism, ct:enthymeme, ct:toulmin-model, ct:douglas-walton]
requires: [ct:argument]
relations:
  - {predicate: introducedBy, object: ct:stephen-thomas, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:convergent-argument, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:informal-logic, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:argument-mapping, source: s2, confidence: high}
sources:
  - id: s1
    title: "Freeman's Syntactic Criterion for Linkage"
    publisher: "Informal Logic 35(1), 1-31 (David Hitchcock, 2015)"
    url: https://distantreader.org/stacks/journals/il/il-4234.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "Dependent and Independent Reasons"
    publisher: "Informal Logic 13(3) (Robert J. Yanal, 1991)"
    url: https://distantreader.org/stacks/journals/il/il-2563.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "The TRUE Test of Linkage"
    publisher: "Informal Logic 16(3) (Mark Vorobej, 1994)"
    url: https://distantreader.org/stacks/journals/il/il-2454.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Argument Structure: A Pragmatic Theory"
    publisher: "University of Toronto Press (Douglas Walton, 1996), Project MUSE book page"
    url: https://muse.jhu.edu/book/108197
    type: primary
    accessed: 2026-11-18
  - id: s5
    title: "Linked Argumentation"
    publisher: "Dictionary of Argumentation, ICAR laboratory, CNRS / Université Lyon 2 (Christian Plantin, 2021)"
    url: https://icar.cnrs.fr/dicoplantin/linked-argumentation-e/
    type: academic
    accessed: 2026-11-18
created: 2026-11-18
---

# Linked argument

A linked argument is one whose premises give support to the conclusion only as a group. Each premise is relevant because of the others: on its own it leaves a gap that another premise closes.[^s1][^s2] Robert Yanal calls such premises "dependent reasons" and argues that together they form a single argument, whereas independent reasons amount to several arguments for the same point.[^s2] Christian Plantin's dictionary of argumentation adds "coordinate argumentation" as a synonym and offers a simple case: the claim that it rained and that the temperature is below freezing is a complete reason to expect black ice, but either half alone needs something more.[^s5]

## Origin

Stephen Thomas introduced the linked/convergent pair in his 1977 textbook on practical reasoning, defining linked premises as relevant to the conclusion only in combination.[^s1] The contrast became a standard part of critical thinking textbooks, and argument diagrams adopted a convention for it: jointly working premises are bundled under a single arrow, while independent premises each get their own.[^s1][^s2] During the 1990s it turned into a running research question in the journal *Informal Logic*, with Yanal, Mark Vorobej, James Freeman and Douglas Walton each proposing criteria for detecting linkage.[^s1][^s2][^s3] Walton devoted two chapters of his 1996 book *Argument Structure* to the distinction, observing that rival textbook tests often classify the same argument differently.[^s4]

## How it works

Consider a workplace example. A facilities manager reasons: the server-room alarm logs a badge entry at 2 a.m.; only staff on the night roster hold badges that open that door after hours; so someone on the night roster entered the room. Neither premise does any work alone. The log entry says nothing about who could have opened the door, and the badge policy says nothing about whether anyone did. Together they make the conclusion follow.[^s2][^s5] A colleague who wants to resist the conclusion needs to defeat only one premise, for example by showing that a contractor's badge was wrongly given after-hours access. Vorobej sums up this vulnerability with the image of a chain that is only as strong as its weakest link.[^s3]

Many familiar forms are linked by nature. The premises of a categorical syllogism or a disjunctive syllogism work as a team, and in Toulmin's model the data supports a claim only together with a warrant.[^s2][^s5] Linkage is not confined to valid deduction. Yanal argues that the observations in an inductive generalisation can be dependent, because the accumulated evidence counts for more than the separate observations would, and he notes that even a fallacious form such as affirming the consequent has premises that give their slight support only jointly.[^s2]

## How to apply it

When reconstructing or mapping an argument, ask of each premise whether it would still show any relevance to the conclusion if the others were set aside.[^s1][^s5]

1. **Removal test.** Delete one premise. If what remains is still an argument for the conclusion, the support is convergent; if not, it is linked.[^s5]
2. **Weakening test.** Vorobej's TRUE test (type reduction upon elimination) asks whether removing a premise drops the support from conclusive to partial, or from partial to none; any such drop marks linkage.[^s3]
3. **Mediating-term test.** Freeman's syntactic criterion looks at the inference rule: if a term appears in two or more premises but not in the conclusion, those premises are linked. In the badge example, the night roster's badges are such a mediating term.[^s1]
4. **Evaluate together.** Linked premises must be judged as a set. Walton points out that a linked argument can be refuted by showing one premise false or unacceptable, whereas a convergent case needs each line tested separately.[^s5]

A practical payoff is in spotting missing premises: if a stated reason supports the conclusion only with an unstated partner, the reconstructed argument is linked, and the hidden premise is often the place to probe.[^s5]

## Limitations

No test of linkage commands agreement. Yanal rejects the tests of Copi, Thomas and Govier with counterexamples and offers his own probabilistic criterion only as a guide.[^s2] Vorobej shows that relevance-based tests misclassify fallacies of irrelevance, and he concludes that one definitive account is unlikely.[^s3] Hitchcock finds that Freeman's criterion avoids some of these problems but misses many intuitively linked cases, such as conjunction introduction, and that applying any test already requires some evaluation of the argument.[^s1] Vorobej also reports that convergent structures appeared in fewer than one in twelve diagrams in one logic textbook, a reminder that linkage is the common case in practice.[^s3]

## Connections

- **Broader: argument.** Linkage describes how the premises of one argument jointly bear on its conclusion.[^s2]
- **Introduced by Stephen Thomas.** Hitchcock credits Thomas's 1977 textbook with the linked/convergent distinction.[^s1]
- **Contrasts with convergent argument.** Thomas defined the two by whether premises are relevant only in combination or each on its own.[^s1]
- **Studied in informal logic.** The criteria debate ran largely in *Informal Logic*, including Yanal's paper on dependent reasons.[^s2]
- **Applied in argument mapping.** Diagrams draw linked premises under one arrow and independent ones under separate arrows.[^s2]
- **Related to syllogism, enthymeme and the Toulmin model.** Syllogistic premises and Toulmin's data-plus-warrant are standard linked cases, and a premise that needs an unstated partner yields a linked reconstruction.[^s5]
- **Related to Douglas Walton.** His 1996 book surveys the conflicting tests and proposes new criteria.[^s4]

## Sources

[^s1]: Hitchcock, "Freeman's Syntactic Criterion for Linkage", Informal Logic 35(1), 2015. https://distantreader.org/stacks/journals/il/il-4234.pdf (accessed 2026-11-18)
[^s2]: Yanal, "Dependent and Independent Reasons", Informal Logic 13(3), 1991. https://distantreader.org/stacks/journals/il/il-2563.pdf (accessed 2026-11-18)
[^s3]: Vorobej, "The TRUE Test of Linkage", Informal Logic 16(3), 1994. https://distantreader.org/stacks/journals/il/il-2454.pdf (accessed 2026-11-18)
[^s4]: Walton, Argument Structure: A Pragmatic Theory, University of Toronto Press, 1996. https://muse.jhu.edu/book/108197 (accessed 2026-11-18)
[^s5]: Plantin, "Linked Argumentation", Dictionary of Argumentation, ICAR/CNRS, 2021. https://icar.cnrs.fr/dicoplantin/linked-argumentation-e/ (accessed 2026-11-18)
