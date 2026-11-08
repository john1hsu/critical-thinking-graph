---
id: ct:square-of-opposition
type: Concept
title: Square of opposition
aliases: [traditional square of opposition, Aristotelian square, logical square]
domain: formal-logic
summary: >-
  A diagram that arranges the four categorical statement forms (A, E, I, O) at
  the corners of a square and labels the logical relations between them:
  contradictories, contraries, subcontraries and subalterns, which together
  license immediate inferences from the truth or falsity of one statement to
  the others.
level: introductory
evidenceStatus: normative
broader: [ct:categorical-proposition]
related: [ct:existential-import, ct:existential-fallacy, ct:distribution-of-terms, ct:venn-diagram-test, ct:categorical-syllogism, ct:aristotle, ct:boethius, ct:john-buridan, ct:prior-analytics]
requires: [ct:categorical-proposition]
relations:
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:de-interpretatione, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:formal-logic, source: s3, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "The Traditional Square of Opposition"
    publisher: Stanford Encyclopedia of Philosophy (Ciola and Parsons, rev. 2025; Fall 2026 archive edition)
    url: https://plato.stanford.edu/archives/fall2026/entries/square/
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s2
    title: "Square of Opposition"
    publisher: Internet Encyclopedia of Philosophy
    url: https://iep.utm.edu/sqr-opp/
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s3
    title: "3.2 The Square of Opposition (An Introduction to Logic)"
    publisher: Kathy Eldred, Pima Community College Open Press (2024, CC BY-NC 4.0)
    url: https://pimaopen.pressbooks.pub/intrologic/?p=818
    type: textbook
    accessed: 2026-11-08
  - id: s4
    title: "The Traditional Square (Logic Primer, chapter 8)"
    publisher: Saul Traiger, Occidental College
    url: https://sites.oxy.edu/traiger/logic/primer/chapter8/traditional-square.html
    type: academic
    accessed: 2026-11-08
  - id: s5
    title: "The Revised Square (Logic Primer, chapter 8)"
    publisher: Saul Traiger, Occidental College
    url: https://sites.oxy.edu/traiger/logic/primer/chapter8/revised-square.html
    type: academic
    accessed: 2026-11-08
created: 2026-11-08
---

# Square of opposition

The square of opposition is a classic teaching diagram for categorical statements. Its four corners hold the universal affirmative (A: "every S is P"), the universal negative (E: "no S is P"), the particular affirmative (I: "some S is P") and the particular negative (O: "some S is not P"), and its sides and diagonals name how the truth of one corner constrains the others.[^s1][^s3] Because it lets a reader move from one statement to a conclusion about another without a second premise, it is the standard map of the so-called immediate inferences in traditional logic.[^s2][^s3]

## Origin

Aristotle set out the core of the doctrine in chapters 6 and 7 of *De Interpretatione*, pairing A with O and E with I as contradictories and A with E as contraries; the subcontrary and subaltern relations follow from what he says, and *Prior Analytics* I.2 adds the conversion rules.[^s1] The diagram itself was circulating by the second century CE, and Boethius's Latin translations and commentaries, written shortly after 500 CE, made it a fixture of medieval logic teaching.[^s1] Medieval logicians such as John Buridan and Paul of Venice later tested the doctrine and its companion inferences against empty terms such as "chimera".[^s1]

## How it works

The square encodes four relations.[^s1][^s2][^s3][^s4]

- **Contradictories** (the diagonals, A–O and E–I) always take opposite truth values: exactly one is true.[^s1][^s2]
- **Contraries** (the top side, A–E) cannot both be true, but both can be false.[^s2][^s4]
- **Subcontraries** (the bottom side, I–O) cannot both be false, but both can be true.[^s2][^s4]
- **Subalterns** (the vertical sides, A→I and E→O): truth flows down from the universal to the particular, and falsity flows up from the particular to the universal, but not the other way round.[^s1][^s3]

A workplace example: a release manager is told "every test in the suite passed" (A). If that is true, the square says "some test failed" (O) is false, "no test passed" (E) is false, and "some test passed" (I) is true. If instead the manager only knows "some test passed" (I), the square settles very little: E is false, while A and O stay open.[^s3] An everyday slip the textbook flags is reading "some passed" as quietly implying "some failed"; in logic "some" means only "at least one", so I does not entail O.[^s3]

## How to apply it

To use the square, translate each claim into one of the four standard forms with the same subject and predicate, place it on its corner, and read off what is fixed and what is undetermined.[^s3] It is useful for checking whether two claims in a report or debate are true opposites (contradictories, so one must be right) or merely contraries (both could be wrong, which leaves room for a middle position).[^s1][^s2]

## Limitations: existential import

The traditional relations assume that the subject term picks out at least one thing. When a term is empty, most of them break down.[^s2] Modern logic writes "every S is P" as a universally quantified conditional, which is vacuously true when nothing is S, and on that reading only the diagonal contradictions survive; the result is often called the modern square.[^s1][^s2] Traiger's primer illustrates this with unicorns: "all unicorns are horned" comes out true while "some unicorns are horned" is false, so subalternation fails, and a Venn diagram with the subject region shaded empty shows the same thing.[^s5] Medieval logicians had their own fix: by the late fourteenth century it was widely held that affirmatives carry existential import and negatives do not, and Aristotle's original O-form, "not every S is P", is true when S is empty, which keeps the square intact.[^s1] The traditional square is therefore valid relative to its assumptions: its side relations hold only when the subject term is known to be non-empty, which is why the traditional square presents them as putative claims to be checked rather than free inferences.[^s4][^s5]

## Connections

- **Broader: categorical proposition; requires it.** The square is a set of relations among the four categorical forms, so a reader needs those forms first.[^s3]
- **Introduced by Aristotle in *De Interpretatione*.** The contradictory and contrary pairings come from that work.[^s1]
- **Studied in formal logic.** It remains a standard chapter of introductory logic courses.[^s3][^s4]
- **Related to existential import and the existential fallacy.** Empty terms are where the traditional and modern squares diverge; inferring a particular from a universal when the subject might be empty is the step that breaks.[^s1][^s5]
- **Related to the Venn diagram test, distribution of terms and the categorical syllogism.** These are companion tools for the same statement forms; Venn diagrams show which relations hold once empty terms are allowed.[^s5]
- **Related to Boethius and John Buridan.** Boethius spread the diagram in the Latin West, and Buridan used empty-term examples to test its rules.[^s1]

## Sources

[^s1]: Ciola and Parsons, "The Traditional Square of Opposition", Stanford Encyclopedia of Philosophy (rev. 2025). https://plato.stanford.edu/archives/fall2026/entries/square/ (accessed 2026-11-08)
[^s2]: "Square of Opposition", Internet Encyclopedia of Philosophy. https://iep.utm.edu/sqr-opp/ (accessed 2026-11-08)
[^s3]: Eldred, "3.2 The Square of Opposition", An Introduction to Logic, Pima Community College Open Press (2024). https://pimaopen.pressbooks.pub/intrologic/?p=818 (accessed 2026-11-08)
[^s4]: Traiger, "The Traditional Square", Logic Primer, Occidental College. https://sites.oxy.edu/traiger/logic/primer/chapter8/traditional-square.html (accessed 2026-11-08)
[^s5]: Traiger, "The Revised Square", Logic Primer, Occidental College. https://sites.oxy.edu/traiger/logic/primer/chapter8/revised-square.html (accessed 2026-11-08)
