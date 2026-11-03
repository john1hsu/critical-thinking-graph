---
id: ct:chrysippus
type: Person
title: Chrysippus
aliases: [Chrysippus of Soli]
domain: history-and-thinkers
summary: >-
  Greek Stoic philosopher (c. 280-207 BCE) and third head of the Stoa, the
  main architect of Stoic logic, whose system of five indemonstrable
  arguments, starting with "if p then q; p; therefore q", made him one of the
  first to organise propositional logic as a discipline.
level: intermediate
evidenceStatus: historical
broader: []
related: [ct:stoic-logic, ct:modus-ponens, ct:deductive-reasoning, ct:liar-paradox, ct:sorites-paradox]
requires: []
relations:
  - {predicate: influencedBy, object: ct:cleanthes, source: s4, confidence: high}
  - {predicate: studiedIn, object: ct:propositional-logic, source: s5, confidence: high}
  - {predicate: contrastsWith, object: ct:aristotle, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Chrysippus (c. 280-207 B.C.E.)"
    publisher: Internet Encyclopedia of Philosophy (Kirby)
    url: https://iep.utm.edu/chrysippus/
    type: scholarly-encyclopedia
    accessed: 2026-11-03
  - id: s2
    title: "Ancient Logic"
    publisher: Stanford Encyclopedia of Philosophy (Bobzien, rev. 2020)
    url: https://plato.stanford.edu/entries/logic-ancient/
    type: scholarly-encyclopedia
    accessed: 2026-11-03
  - id: s3
    title: "Crísipo de Solos y los indemostrables (Chrysippus of Soli and the Indemonstrables)"
    publisher: Revista de Filosofía 74, 193-214, Universidad de Chile (Ramírez Figueroa, 2018)
    url: https://revistaschilenas.uchile.cl/handle/2250/15306?show=full
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s4
    title: "Chrysippus of Soli"
    publisher: MacTutor History of Mathematics Archive, University of St Andrews
    url: https://mathshistory.st-andrews.ac.uk/Biographies/Chrysippus/
    type: academic
    accessed: 2026-11-03
  - id: s5
    title: "Chrysippus"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/biography/Chrysippus
    type: encyclopedia
    accessed: 2026-11-03
  - id: s6
    title: "Stoicism: Inferential logic"
    publisher: Routledge Encyclopedia of Philosophy (Sedley, 1998)
    url: https://www.rep.routledge.com/articles/thematic/stoicism/v-1/sections/inferential-logic
    type: scholarly-encyclopedia
    accessed: 2026-11-03
created: 2026-11-03
---

# Chrysippus

Chrysippus of Soli (c. 280-207 BCE) was the Stoic philosopher who turned the school's scattered doctrines into a system, and above all the logician behind Stoic logic.[^s1][^s5] Where Aristotle built a logic of terms such as "all" and "some", Chrysippus built one of whole statements joined by "if", "or", "and" and "not", which is why he is counted among the first to organise propositional logic as a discipline.[^s1][^s4][^s5] Bobzien's survey of ancient logic calls him the second great logician in the history of the subject, after Aristotle.[^s2]

## Origin

Chrysippus was born at Soli in Cilicia, on the south coast of present-day Turkey, and came to Athens, where he studied in Plato's Academy under the sceptic Arcesilaus before joining the Stoa under Cleanthes.[^s1][^s4] He succeeded Cleanthes as head of the school around 230 BCE and led it until his death.[^s1][^s4] Ancient reports credit him with more than 700 books, over 300 of them on logic, including a multi-volume treatment of the Liar paradox; none survives whole, so his views reach us through fragments and later reports, many of which simply say "the Stoics".[^s1][^s2][^s4] A later Stoic saying held that without Chrysippus there would have been no Stoa.[^s1][^s4]

## How it works

Chrysippus's central idea was that arguments can be checked by their connective structure alone. A small set of basic forms, the five *indemonstrables*, need no proof; every other valid argument is shown valid by reducing it to them with four rules called *themata*.[^s2][^s6] The five are: from "if p then q" and p, infer q (later named modus ponens); from "if p then q" and not-q, infer not-p (modus tollens); from "not both p and q" and p, infer not-q; from "either p or q" (exclusive) and p, infer not-q; and from "either p or q" and not-p, infer q.[^s2][^s1] Ramírez Figueroa argues that Chrysippus's work on these five forms is the main foundation of the Stoic deductive system and still bears on the modern question of how deduction is justified.[^s3]

A workplace example shows the forms in use. A release checklist says: "Either the build passed or the deployment is blocked." An engineer learns the build did not pass and concludes the deployment is blocked, which is the fifth indemonstrable. If she instead reasons "the build passed, so the deployment is not blocked", she relies on the fourth form, and that step is safe only if the "or" is exclusive, which Chrysippus required of disjunctions.[^s1][^s2] Spotting which basic form an argument uses tells you exactly which premise to test.

Chrysippus also took a demanding view of "if". For Philo, a conditional was false only when its antecedent was true and its consequent false, much like today's material conditional. Chrysippus required instead that the contradictory of the consequent conflict with the antecedent, a connection test that is not truth-functional and that later scholars compare to relevance logic.[^s2][^s1] He also worked on the sorites and the Liar, puzzles that still test theories of vagueness and truth.[^s4][^s6]

## Legacy and limitations

Our picture of Chrysippus's logic is reconstructed from fragments and later reports, and only two badly damaged papyri survive.[^s2] Because so many testimonies name no particular Stoic, it is often unclear how much of the system is his own and how much belongs to other members of the school; Bobzien's survey accordingly credits the indemonstrables to "the Stoics" in general, while specialist studies tie them to his work.[^s2][^s3] What is not in doubt is the lasting idea: an argument's validity can be judged from its connective form, separately from whether its premises are true, which is the same check a careful reader runs on any chain of "if" and "or" claims today.[^s1][^s3]

## Connections

- **Introduced modus ponens** as the first of the five indemonstrables; the reasoner records this from the modus ponens article.[^s3][^s2]
- **Influenced by Cleanthes**, his teacher and predecessor as head of the Stoa.[^s4]
- **Studied in propositional logic**, the discipline Britannica credits him with being among the first to organise.[^s5]
- **Contrasts with Aristotle**: his logic of connectives between whole statements differs from Aristotle's logic of terms and quantifiers.[^s1][^s2]
- **Related: Stoic logic**, the system he did most to build, and **deductive reasoning**, which his indemonstrables formalise for the propositional case.[^s2][^s6]
- **Related: the Liar and sorites paradoxes**, on which he wrote extensively.[^s4][^s6]

## Sources

[^s1]: Kirby, "Chrysippus (c. 280-207 B.C.E.)", Internet Encyclopedia of Philosophy. https://iep.utm.edu/chrysippus/ (accessed 2026-11-03)
[^s2]: Bobzien, "Ancient Logic", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/logic-ancient/ (accessed 2026-11-03)
[^s3]: Ramírez Figueroa, "Crísipo de Solos y los indemostrables", *Revista de Filosofía* 74 (2018), 193-214. https://revistaschilenas.uchile.cl/handle/2250/15306?show=full (accessed 2026-11-03)
[^s4]: MacTutor History of Mathematics Archive, "Chrysippus of Soli", University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Chrysippus/ (accessed 2026-11-03)
[^s5]: Encyclopaedia Britannica, "Chrysippus". https://www.britannica.com/biography/Chrysippus (accessed 2026-11-03)
[^s6]: Sedley, "Stoicism: Inferential logic", Routledge Encyclopedia of Philosophy. https://www.rep.routledge.com/articles/thematic/stoicism/v-1/sections/inferential-logic (accessed 2026-11-03)
