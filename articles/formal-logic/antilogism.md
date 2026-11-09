---
id: ct:antilogism
type: Technique
title: Antilogism
aliases: [inconsistent triad, Ladd-Franklin's antilogism, antilogism test, inconsistent triad test]
domain: formal-logic
summary: >-
  A single-rule test for categorical syllogisms devised by Christine Ladd(-Franklin):
  pair the two premises with the contradictory of the conclusion, and the syllogism
  is valid exactly when that trio has the shape of an inconsistent triad (two
  universal exclusions, one particular, with the right pattern of positive and
  negated terms).
level: intermediate
evidenceStatus: normative
broader: [ct:categorical-syllogism]
related: [ct:venn-diagram-test, ct:rules-of-the-categorical-syllogism, ct:distribution-of-terms, ct:existential-import, ct:square-of-opposition, ct:method-of-counterexample, ct:syllogism, ct:george-boole, ct:undistributed-middle, ct:illicit-major]
requires: [ct:categorical-syllogism, ct:categorical-proposition, ct:validity]
relations:
  - {predicate: detects, object: ct:exclusive-premises, source: s4, confidence: medium}
  - {predicate: introducedBy, object: ct:christine-ladd-franklin, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:on-the-algebra-of-logic, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:charles-sanders-peirce, source: s6, confidence: medium}
  - {predicate: contrastsWith, object: ct:rules-of-the-categorical-syllogism, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "The Syllogism's Final Solution"
    publisher: "Bulletin of Symbolic Logic 5(4), 451-469 (I. Susan Russinoff, 1999), Cambridge Core"
    url: https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/syllogisms-final-solution/64B927F7328426E5D5FD35185FA1022B
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s2
    title: "What Problem Did Ladd-Franklin (Think She) Solve(d)?"
    publisher: "Sara L. Uckelman, Durham University; talk slides, ASL 2023 Annual Meeting, UC Irvine"
    url: https://sites.uci.edu/asl2023/files/2023/03/asl-2023.pdf
    type: academic
    accessed: 2026-11-09
  - id: s3
    title: "An Introduction to Logic and Scientific Method: the antilogism or inconsistent triad (excerpt)"
    publisher: "Morris R. Cohen & Ernest Nagel, Harcourt, Brace and Company (textbook excerpt)"
    url: https://www.hist-analytic.com/NagelInconsistentriad.pdf
    type: textbook
    accessed: 2026-11-09
  - id: s4
    title: "Diagramas para o Antilogismo de Ladd"
    publisher: "Dissertatio 47, 84-94 (Frank Thomas Sautter, 2018), Universidade Federal de Pelotas"
    url: https://periodicos.ufpel.edu.br/index.php/dissertatio/article/view/13731/8800
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s5
    title: "Christine Ladd-Franklin's 'On the Algebra of Logic': On Elimination (annotated by Julia M. Parker)"
    publisher: "Convergence, Mathematical Association of America (2019)"
    url: https://old.maa.org/node/2019045
    type: institutional
    accessed: 2026-11-09
  - id: s6
    title: "Christine Ladd-Franklin"
    publisher: "Women in Philosophy and Mathematics, Universität Siegen"
    url: https://www.uni-siegen.de/fb6/phima/women/ladd_franklin.html
    type: academic
    accessed: 2026-11-09
created: 2026-11-09
---

# Antilogism

An antilogism, or inconsistent triad, is a set of three categorical propositions that cannot all be true together, so that any two of them entail the contradictory of the third.[^s3] Christine Ladd (later Ladd-Franklin) turned this observation into a validity test: a syllogism is valid exactly when its two premises plus the denial of its conclusion form an antilogism of a fixed shape.[^s1][^s3] One rule thereby does the work that traditional logic spread across a list of valid moods and several separate rules.[^s2][^s4]

## Origin

Ladd introduced the antilogism in "On the Algebra of Logic", published in 1883 while she was a graduate student of Charles S. Peirce at Johns Hopkins; the university withheld her doctorate until 1926.[^s1][^s6] Her algebra took exclusion rather than inclusion as its basic relation, which is why every universal statement in her system reads as "these two things never occur together".[^s6][^s5] She framed the work as part of the nineteenth-century algebra-of-logic programme, describing elimination of a middle term from a triad of mutually inconsistent propositions.[^s5] Later admirers called it the decisive solution to Aristotle's syllogistic problem, a framing the historian Sara Uckelman argues Ladd-Franklin herself did not adopt.[^s1][^s2] In a 1928 note she added a clause that closes gaps in the 1883 wording.[^s4]

## How it works

Write each universal proposition as an exclusion that says a combination is empty, and each particular as a claim that a combination has members. "No C is B" becomes "CB is empty"; "All V are B" becomes "V-and-not-B is empty"; "Some V is not C" becomes "V-and-not-C has members". Then the trio of premises plus denied conclusion is a valid antilogism when:[^s3][^s4]

1. two propositions are universal and one is particular;[^s3]
2. the term shared by the two universals appears positive in one and negated in the other;[^s3] and
3. (the 1928 clause) each universal shares its remaining term with the particular, with the same sign in both.[^s4]

Workplace example. A facilities memo argues: "No contractors have badge access. Some visitors are not contractors. So some visitors lack badge access." Both premises are negative. Denying the conclusion gives "All visitors have badge access" (V-not-B empty). The universals are "CB empty" and "V-not-B empty": B is positive in one and negated in the other, so the 1883 condition passes. But the particular, "V-not-C has members", carries C negated while the universal carries C positive, so the 1928 clause fails and the argument is invalid.[^s4] Change the second premise to "Some visitors are contractors" (VC has members) and every condition holds, so that version is valid. Sautter shows that without the later clause the original rule lets through four invalid patterns, which is exactly the kind of case above.[^s4]

## How to apply it

- Translate every proposition into "is empty" or "has members" form before checking anything; most mistakes come from mistranslating "All" and "Some ... not".[^s3]
- Always negate the conclusion, not the premises; the test is a disguised reductio.[^s2][^s3]
- Check the three conditions in order; a failure names the problem (wrong quantity mix, a middle term not pinned down, or mismatched signs in the particular).
- Pitfall: the method reads universals as making no claim that their classes have members, so moods that rely on existential import, including the weakened moods, come out invalid.[^s3] If your context assumes non-empty classes, add that assumption as an explicit premise.

## Connections

The antilogism detects the fallacy of exclusive premises: two negative premises can never meet the sign conditions together, and Sautter's analysis of the refined rule classes the patterns it rejects as fallacies.[^s4] It contrasts with the rules of the categorical syllogism, since Ladd's single condition collapses the separate traditional rules into one.[^s4] It was introduced by Christine Ladd-Franklin in "On the Algebra of Logic".[^s1] Peirce, her teacher and collaborator, shaped the algebraic setting she worked in.[^s6] The test is a symbolic cousin of the Venn diagram test, which reads the same empty and non-empty regions off a picture; both treat universals without existential import.[^s3]

## Sources

[^s1]: Russinoff, "The Syllogism's Final Solution", Bulletin of Symbolic Logic 5(4), 1999. https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/syllogisms-final-solution/64B927F7328426E5D5FD35185FA1022B (accessed 2026-11-09)
[^s2]: Uckelman, "What Problem Did Ladd-Franklin (Think She) Solve(d)?", ASL 2023 talk slides. https://sites.uci.edu/asl2023/files/2023/03/asl-2023.pdf (accessed 2026-11-09)
[^s3]: Cohen & Nagel, An Introduction to Logic and Scientific Method, antilogism excerpt. https://www.hist-analytic.com/NagelInconsistentriad.pdf (accessed 2026-11-09)
[^s4]: Sautter, "Diagramas para o Antilogismo de Ladd", Dissertatio 47, 2018. https://periodicos.ufpel.edu.br/index.php/dissertatio/article/view/13731/8800 (accessed 2026-11-09)
[^s5]: Parker (annotator), Ladd-Franklin's "On the Algebra of Logic": On Elimination, MAA Convergence, 2019. https://old.maa.org/node/2019045 (accessed 2026-11-09)
[^s6]: "Christine Ladd-Franklin", Women in Philosophy and Mathematics, Universität Siegen. https://www.uni-siegen.de/fb6/phima/women/ladd_franklin.html (accessed 2026-11-09)
