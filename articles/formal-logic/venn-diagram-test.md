---
id: ct:venn-diagram-test
type: Technique
title: Venn diagram test
aliases: [Venn diagram method, Venn validity test, three-circle test for syllogisms]
domain: formal-logic
summary: >-
  A visual decision procedure for categorical syllogisms: draw three overlapping
  circles for the three terms, record only what the premises say (shading for
  empty regions, an X for "at least one"), and the argument is valid exactly
  when the conclusion can be read off the finished diagram.
level: introductory
evidenceStatus: normative
broader: [ct:diagrammatic-reasoning, ct:categorical-syllogism]
related: [ct:syllogism, ct:method-of-counterexample, ct:distribution-of-terms, ct:validity]
requires: [ct:categorical-syllogism, ct:validity]
relations:
  - {predicate: detects, object: ct:illicit-major, source: s2, confidence: high}
  - {predicate: detects, object: ct:illicit-minor, source: s2, confidence: high}
  - {predicate: detects, object: ct:undistributed-middle, source: s3, confidence: high}
  - {predicate: introducedBy, object: ct:john-venn, source: s5, confidence: high}
  - {predicate: contrastsWith, object: ct:euler-diagram, source: s4, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Categorical Syllogisms: Venn Diagrams"
    publisher: "Introduction to Logic, Philosophy Department, Lander University"
    url: https://philosophy.lander.edu/logic/syll_venn.html
    type: academic
    accessed: 2026-11-05
  - id: s2
    title: "Syllogistic Fallacies: Illicit Major and Illicit Minor"
    publisher: "Introduction to Logic, Philosophy Department, Lander University"
    url: https://philosophy.lander.edu/logic/illicit_fall.html
    type: academic
    accessed: 2026-11-05
  - id: s3
    title: "Syllogistic Fallacy 2: Undistributed Middle"
    publisher: "Introduction to Logic, Philosophy Department, Lander University"
    url: https://philosophy.lander.Edu/logic/middle_fall.html
    type: academic
    accessed: 2026-11-05
  - id: s4
    title: "Diagrams and Diagrammatical Reasoning"
    publisher: Stanford Encyclopedia of Philosophy (rev. 2025)
    url: https://plato.stanford.edu/entries/diagrams/
    type: scholarly-encyclopedia
    accessed: 2026-11-05
  - id: s5
    title: "A Survey of Venn Diagrams: John Venn"
    publisher: "The Electronic Journal of Combinatorics, Dynamic Survey DS5 (Ruskey & Weston)"
    url: https://www.combinatorics.org/files/Surveys/ds5/VennJohnEJC.html
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s6
    title: "How Diagrams Can Support Syllogistic Reasoning: An Experimental Study"
    publisher: "Journal of Logic, Language and Information 24(4), 409-455 (Sato & Mineshima, 2015)"
    url: https://research.brighton.ac.uk/en/publications/how-diagrams-can-support-syllogistic-reasoning-an-experimental-st/
    type: peer-reviewed
    accessed: 2026-11-05
created: 2026-11-05
---

# Venn diagram test

The Venn diagram test is a mechanical way to decide whether a categorical syllogism is valid. Each of the three terms (minor, major and middle) gets its own circle, the circles overlap so that every possible combination of membership has a region, and only the premises are drawn. If the finished drawing already shows what the conclusion claims, the argument is valid; if the conclusion still has to be added, it is invalid.[^s1] Because the test looks at the diagram rather than at the subject matter, it gives a quick, content-neutral check on syllogisms whose conclusions merely sound right.[^s1][^s2]

## Origin

Circle diagrams for syllogisms are older than Venn. Euler used closed curves in the eighteenth century, with containment for "all" and separation for "no", but his scheme struggled with "some" statements: one diagram could be read several ways, and some premise pairs needed several alternative drawings.[^s4] John Venn (1834-1923), a Cambridge logician, introduced his version in "On the Diagrammatic and Mechanical Representation of Propositions and Reasonings" in the *Philosophical Magazine* in July 1880 and developed it in *Symbolic Logic* (1881).[^s5] Ruskey and Weston note that he is credited less for inventing overlapping circles than for surveying their use systematically and first generalising them.[^s5] Venn's key move was the "primary diagram", which draws every possible combination of classes without committing to whether any region has members, and then marks empty regions by shading. Charles S. Peirce later added a mark for existence, the X that textbooks now use for "some". In 1994 Sun-Joo Shin gave the extended system a formal syntax and semantics and proved it sound and complete, showing that diagrams can be a rigorous proof method and not only an illustration.[^s4]

## How it works

The notation has three marks. Shading means a region is known to be empty. An X means at least one thing is in the region. Blank space means nothing is known about it.[^s1] An A statement ("All S are P") shades the part of S outside P; an E statement ("No S are P") shades the overlap; I and O statements put an X in the overlap or in the part of S outside P.[^s1]

A workplace example shows how the test catches an undistributed middle. "All approved vendors have passed the security review. Some cloud providers have passed the security review. So some cloud providers are approved vendors." Draw circles for cloud providers (S), approved vendors (P) and passed the review (M). The first premise shades the part of P outside M. The second premise needs an X in the overlap of S and M, but that overlap is split by the P circle, and neither part is shaded, so the X goes on the line. Its position is undetermined, so the diagram does not show that any cloud provider is an approved vendor, and the form (AII-2) is invalid.[^s1][^s3] Lander University's notes use the same reading for an AAA-2 argument: a blank region in which the minor term can sit outside the major term shows that the conclusion has not been proved.[^s3]

## How to apply it

1. Put the argument in standard form and label the minor term (subject of the conclusion), major term (predicate of the conclusion) and middle term.[^s1]
2. Draw three overlapping circles and diagram the universal premises first, then the particular ones. If an X goes in first, a later universal premise may shade the region it occupies.[^s1]
3. Place an X inside a single region only when the premises force it there. Otherwise put it on the line between the candidate regions.[^s1]
4. Never draw the conclusion. Inspect the diagram instead: valid means the region the conclusion calls empty is already shaded, or the region it says is occupied already holds an X entirely inside it.[^s1]
5. Watch existential import. A syllogism with two universal premises and a particular conclusion (for example EAO-4) fails the test unless an extra premise that the relevant class has members is added.[^s1]

When a diagram shows an argument is invalid, the same picture shows why. For the illicit major and illicit minor, Lander University's notes pair each example with a diagram on which the conclusion fails to appear.[^s2] The blank or uncertain region is where a counterexample would sit.[^s1][^s2]

## Evidence and limitations

The test is a logical procedure, so its correctness does not rest on experiments. Shin's soundness and completeness results show that the diagram system matches monadic predicate logic, which covers the categorical syllogism.[^s4] Whether diagrams help untrained reasoners is a separate, empirical question. In a 2015 study in the *Journal of Logic, Language and Information*, Sato and Mineshima compared syllogistic reasoning with Euler-style diagrams and with Venn diagrams. They concluded that the benefit depends on how a diagram represents the relations in each sentence, and their results favoured their Euler-style system.[^s6] The Stanford Encyclopedia notes a general trade-off: from Euler through Venn to Peirce, the diagrams gained expressive power and lost visual clarity.[^s4] Venn's test is also limited to categorical (one-place, class) statements. Arguments with relations, conditionals or quantities need other methods.[^s4]

## Connections

- **Detects the illicit major and illicit minor.** Diagramming the premises shows that the conclusion's universal claim about the major or minor class is not drawn in.[^s2]
- **Detects the undistributed middle.** An X that must sit on a line, or a blank area that lets the minor term fall outside the major, shows that the premises never link the two end terms.[^s1][^s3]
- **Introduced by John Venn** in his 1880 *Philosophical Magazine* paper.[^s5]
- **Contrasts with Euler diagrams,** which represent known relations directly but cannot show partial information about existence as cleanly as Venn's primary diagrams.[^s4]
- **Related to the method of counterexample:** the region the diagram leaves open is where a case with true premises and a false conclusion would sit.[^s1]

## Sources

[^s1]: "Categorical Syllogisms: Venn Diagrams", Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/syll_venn.html (accessed 2026-11-05)
[^s2]: "Syllogistic Fallacies: Illicit Major and Illicit Minor", Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/illicit_fall.html (accessed 2026-11-05)
[^s3]: "Syllogistic Fallacy 2: Undistributed Middle", Introduction to Logic, Lander University. https://philosophy.lander.Edu/logic/middle_fall.html (accessed 2026-11-05)
[^s4]: "Diagrams and Diagrammatical Reasoning", Stanford Encyclopedia of Philosophy (rev. 2025). https://plato.stanford.edu/entries/diagrams/ (accessed 2026-11-05)
[^s5]: Ruskey & Weston, "A Survey of Venn Diagrams: John Venn", The Electronic Journal of Combinatorics, DS5. https://www.combinatorics.org/files/Surveys/ds5/VennJohnEJC.html (accessed 2026-11-05)
[^s6]: Sato & Mineshima (2015), "How Diagrams Can Support Syllogistic Reasoning: An Experimental Study", Journal of Logic, Language and Information 24(4). https://research.brighton.ac.uk/en/publications/how-diagrams-can-support-syllogistic-reasoning-an-experimental-st/ (accessed 2026-11-05)
