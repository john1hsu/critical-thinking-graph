---
id: ct:distribution-of-terms
type: Concept
title: Distribution of terms
aliases: [doctrine of distribution, distributed term, undistributed term, distribution (syllogistic)]
domain: formal-logic
summary: >-
  The traditional property of a term in a categorical proposition of being
  "taken universally", so that the statement says something about every member
  of the term's class: universals distribute their subject and negatives their
  predicate, and the syllogistic rules are stated in these terms.
level: intermediate
evidenceStatus: normative
broader: [ct:categorical-proposition]
related: [ct:rules-of-the-categorical-syllogism, ct:undistributed-middle, ct:illicit-major, ct:illicit-minor, ct:venn-diagram-test, ct:square-of-opposition, ct:john-buridan, ct:categorical-syllogism]
requires: [ct:categorical-proposition]
relations:
  - {predicate: challengedBy, object: ct:peter-geach, source: s1, confidence: high}
  - {predicate: formalizedBy, object: ct:port-royal-logic, source: s2, confidence: high}
  - {predicate: influencedBy, object: ct:supposition-theory, source: s3, confidence: medium}
  - {predicate: influencedBy, object: ct:aristotle, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "The doctrine of distribution"
    publisher: "History and Philosophy of Logic 27(1), 59-74 (Terence Parsons, 2006), PhilPapers record"
    url: https://philpapers.org/rec/TERTDO-2
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s2
    title: "Distributive Terms, Truth, and the Port Royal Logic"
    publisher: "History and Philosophy of Logic (John N. Martin, 2012), author's copy, University of Cincinnati"
    url: https://homepages.uc.edu/~martinj/Papers/Distributive%20Terms,%20Truth%20and%20The%20Port%20Royal%20Logic%20-%20HPL%20(web%20version).pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s3
    title: "Medieval Theories: Properties of Terms"
    publisher: "Stanford Encyclopedia of Philosophy (Stephen Read, Spring 2003 archive edition)"
    url: https://plato.stanford.edu/archives/spr2003/entries/medieval-terms/
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s4
    title: "Categorical propositions: distribution (PHIL 1440 handout)"
    publisher: "University of Colorado, philosophy course materials"
    url: https://rintintin.colorado.edu/~vancecd/phil1440/catprop1.pdf
    type: academic
    accessed: 2026-11-08
  - id: s5
    title: "The Irrelevance of Distribution for the Syllogism"
    publisher: "Notre Dame Journal of Formal Logic 35(3), 433-449 (Wallace A. Murphree, 1994), PhilArchive record"
    url: https://dc2.philarchive.org/rec/WALTIO-6
    type: peer-reviewed
    accessed: 2026-11-08
created: 2026-11-08
---

# Distribution of terms

In traditional logic a term is *distributed* in a categorical proposition when the proposition makes a claim about every member of the class the term names, and *undistributed* when it does not.[^s4] The four standard forms settle the matter mechanically: the universal affirmative (A, "all S are P") distributes only its subject; the universal negative (E, "no S are P") distributes both terms; the particular affirmative (I, "some S are P") distributes neither; and the particular negative (O, "some S are not P") distributes only its predicate.[^s4] The handy summary is that universal statements distribute their subject and negative statements distribute their predicate.[^s4]

## Origin

Where the idea comes from is itself disputed. Peter Geach argued that the doctrine was a sixteenth-century misreading of the medieval notion of distributive supposition.[^s1] Terence Parsons replied in 2006 that it appears at least as early as the twelfth century and develops Aristotle's notion of a term being "taken universally", not the later supposition theory.[^s1] The medieval link is real either way: Stephen Read notes that distribution was listed among the properties of terms and that later authors treated it as a mode of supposition, confused-and-distributive supposition, which they explained through "descent" from a general statement to the conjunction of its singular instances.[^s3] On that account the subjects of A and E statements and the predicates of E and O statements have confused-and-distributive supposition, matching the textbook table.[^s3]

The *Port-Royal Logic* of Arnauld and Nicole gave the notion its classic modern shape. John Martin argues that they defined the universal, or distributive, term through identities among referents rather than through entailment or truth, which let them state truth conditions for categorical propositions without circularity and underpinned their rules for valid moods.[^s2] Martin also observes that modern textbooks mostly teach distribution as a syntactic recipe for the syllogistic rules, without a clear semantic account of what it means.[^s2]

## How it works

Take a workplace claim: "All senior engineers are on the on-call rota." It speaks about every senior engineer, so "senior engineers" is distributed; it says nothing about everyone on the rota, so "on the on-call rota" is undistributed, since the rota may include people who are not senior engineers.[^s4] Now negate it: "No contractors are on the on-call rota." This tells us about every contractor and also, in excluding them, about every person on the rota, so both terms are distributed.[^s4] "Some contractors are not on the rota" says that some contractors fall wholly outside the rota class, so it distributes the predicate but not the subject.[^s4]

Distribution earns its place in the rules for testing syllogisms. A middle term that is never distributed cannot link the other two terms, and a term distributed in the conclusion but not in its premise lets the conclusion claim more than the premises gave; these are the fallacies of the undistributed middle and of the illicit major or minor.[^s2][^s4] Suppose a manager reasons, "All approved vendors passed the security review; this new vendor passed the security review; so it is approved." "Passed the security review" is the predicate of two affirmatives and so is undistributed in both premises, which flags the argument as invalid before any facts are checked.[^s4]

## How to apply it

When checking a categorical argument, first rewrite each statement in A, E, I or O form, then mark the subject of every universal and the predicate of every negative as distributed.[^s4] Confirm that the middle term is marked at least once and that nothing marked in the conclusion is unmarked in its premise.[^s4] Treat the marks as a quick screen rather than an explanation of why an inference is valid; if a case is unclear, cross-check with a Venn diagram or a counterexample.

## Evidence and limitations

As a criterion of valid form, distribution is normative, but its coherence has been debated by logicians. Geach defined a distributed term as one that refers to everything it denotes and argued that this idea is incoherent; Parsons reconstructed the Port-Royal version and rejected Geach's arguments.[^s1] Wallace Murphree took a middle line in 1994: he accepted that distribution can be made coherent, as a term's capacity to be swapped in truth-preserving substitution for a narrower or wider term, but argued that what really drives syllogistic validity is whether a term sits as predicate of a negative or of an affirmative statement, so distribution is a dispensable go-between.[^s5] Martin adds that the medieval explanation by descent and ascent ultimately relied on valid entailment, and so on truth, which made it circular as an analysis of truth.[^s2] For everyday use the table works; the debate concerns what, if anything, it explains.

## Connections

- **Broader: categorical proposition; requires it.** Distribution is a property of the subject and predicate terms of A, E, I and O statements, so it presupposes that framework.[^s4]
- **Challenged by Peter Geach.** Geach called the doctrine incoherent and blamed it on a misuse of distributive supposition; Parsons answered him.[^s1]
- **Formalized by the Port-Royal Logic.** Arnauld and Nicole gave a non-circular semantic definition of the distributive term and built the syllogistic rules on it.[^s2]
- **Influenced by supposition theory.** Medieval logicians recast distribution as confused-and-distributive supposition, defined by descent to singulars.[^s3]
- **Influenced by Aristotle.** Parsons traces the doctrine to Aristotle's idea of a term taken universally.[^s1]
- **Related rules and fallacies.** The rules of the categorical syllogism, and the undistributed middle, illicit major and illicit minor that break them, are stated in terms of distribution.[^s2][^s4]

## Sources

[^s1]: Parsons, "The doctrine of distribution", *History and Philosophy of Logic* 27(1), 59-74 (2006), abstract on PhilPapers. https://philpapers.org/rec/TERTDO-2 (accessed 2026-11-08)
[^s2]: Martin, "Distributive Terms, Truth, and the Port Royal Logic", *History and Philosophy of Logic* (2012), author's copy. https://homepages.uc.edu/~martinj/Papers/Distributive%20Terms,%20Truth%20and%20The%20Port%20Royal%20Logic%20-%20HPL%20(web%20version).pdf (accessed 2026-11-08)
[^s3]: Read, "Medieval Theories: Properties of Terms", Stanford Encyclopedia of Philosophy (Spring 2003 archive), sections 1 and 3. https://plato.stanford.edu/archives/spr2003/entries/medieval-terms/ (accessed 2026-11-08)
[^s4]: "Categorical propositions" handout, PHIL 1440, University of Colorado. https://rintintin.colorado.edu/~vancecd/phil1440/catprop1.pdf (accessed 2026-11-08)
[^s5]: Murphree, "The Irrelevance of Distribution for the Syllogism", *Notre Dame Journal of Formal Logic* 35(3), 433-449 (1994), PhilArchive record. https://dc2.philarchive.org/rec/WALTIO-6 (accessed 2026-11-08)
