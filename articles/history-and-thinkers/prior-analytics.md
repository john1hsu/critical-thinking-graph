---
id: ct:prior-analytics
type: Work
title: Prior Analytics
aliases: [Analytica Priora, Aristotle's syllogistic treatise]
domain: history-and-thinkers
summary: >-
  Aristotle's two-book treatise (c. 350 BCE) that founded formal logic: it
  classifies two-premise deductions into three figures, proves the imperfect
  ones by reducing them to a handful of self-evident first-figure moods, shows
  invalidity by counterexample, and extends the system to necessity and
  possibility.
level: intermediate
evidenceStatus: historical
broader: [ct:organon]
related: [ct:syllogism, ct:categorical-syllogism, ct:method-of-counterexample, ct:validity, ct:square-of-opposition, ct:topics, ct:modal-syllogistic, ct:begging-the-question]
requires: [ct:deductive-reasoning]
relations:
  - {predicate: authoredBy, object: ct:aristotle, source: s1, confidence: high}
  - {predicate: partOf, object: ct:organon, source: s3, confidence: high}
  - {predicate: studiedIn, object: ct:formal-logic, source: s6, confidence: high}
  - {predicate: contrastsWith, object: ct:posterior-analytics, source: s3, confidence: medium}
  - {predicate: formalizedBy, object: ct:natural-deduction, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Prior Analytics, Book I (trans. A. J. Jenkinson)"
    publisher: Aristotle, The Internet Classics Archive (MIT)
    url: https://classics.mit.edu/Aristotle/prior.1.i.html
    type: primary
    accessed: 2026-11-04
  - id: s2
    title: "Prior Analytics, Book II (trans. A. J. Jenkinson)"
    publisher: Aristotle, The Internet Classics Archive (MIT)
    url: https://classics.mit.edu/Aristotle/prior.2.ii.html
    type: primary
    accessed: 2026-11-04
  - id: s3
    title: "Aristotle's Logic (substantive revision 2022)"
    publisher: Stanford Encyclopedia of Philosophy (Robin Smith)
    url: https://plato.stanford.edu/entries/aristotle-logic/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
  - id: s4
    title: "The Founding of Logic: Modern Interpretations of Aristotle's Logic"
    publisher: John Corcoran, Ancient Philosophy 14 (1994), author's copy on PhilArchive
    url: https://philarchive.org/archive/CORTFO-2
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s5
    title: "Review of Marko Malink, Aristotle's Modal Syllogistic (Harvard UP, 2013)"
    publisher: Jacob Rosen, Notre Dame Philosophical Reviews 2014.08.33
    url: https://ndpr.nd.edu/reviews/aristotle-s-modal-syllogistic/
    type: academic
    accessed: 2026-11-04
  - id: s6
    title: "Prior Analytics"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/topic/Prior-Analytics
    type: encyclopedia
    accessed: 2026-11-04
created: 2026-11-04
---

# Prior Analytics

The *Prior Analytics* is the treatise in which Aristotle created the first system of formal logic. Britannica calls the syllogistic it sets out the earliest branch of formal logic, and notes that its Latin translation shaped the methods of disputation used by medieval Scholastic thinkers.[^s6] Where its companion, the *Posterior Analytics*, asks when a proof yields knowledge, the *Prior Analytics* asks a more basic question: when does a conclusion follow from premises at all, whatever their content?[^s3] For a critical thinker it is the origin of the idea that validity is a matter of form, and that a claim of "it follows" can be checked mechanically.

## Origin

Aristotle wrote the work in two books, traditionally dated around 350 BCE; the online English translation is A. J. Jenkinson's.[^s1][^s6] Ancient commentators later grouped it with five other treatises under the title *Organon* ("instrument"), a label Aristotle himself never used; they treated the *Prior* and *Posterior Analytics* as halves of one project.[^s3] Book I opens by announcing that its subject is demonstration, then defines its building blocks: a premise affirms or denies one thing of another, a term is what a premise breaks down into, and a deduction (*sullogismos*) is discourse in which, certain things being stated, something else follows of necessity.[^s1] Robin Smith prefers "deduction" to "syllogism" here because Aristotle's definition is not limited to one narrow pattern.[^s3]

## How it works

**Figures and perfect deductions.** Aristotle sorts two-premise arguments by where the shared middle term sits, giving three figures.[^s3] Some first-figure arguments are "perfect": nothing beyond the premises is needed to see that the conclusion follows, as in "A belongs to all B, B to all C, so A to all C".[^s1] Every other valid pattern is "imperfect" and must be shown to follow.[^s1][^s3]

**Proof by reduction.** To complete an imperfect deduction, Aristotle uses three conversion rules (from "no B is A" to "no A is B"; from "some B is A" to "some A is B"; and from "all B is A" to "some A is B") together with proof through the impossible: assume the conclusion's denial and derive a contradiction.[^s1][^s3] For two stubborn moods he also uses ecthesis, picking out a particular instance.[^s3] He then proves results about the system itself, such as that no deduction has two negative premises and that every deduction can be reduced to the two universal first-figure moods later named Barbara and Celarent, a move Smith compares to modern proofs that some axioms are redundant.[^s3]

**Proof of invalidity.** Aristotle does not just list valid forms. He rejects the rest by offering sets of concrete terms that make the premises true and the conclusion false, which is the method of counterexample still taught today.[^s3]

**Modal syllogistic.** Chapters I.3 and I.8–22 extend the system to premises about what holds necessarily or possibly.[^s5] This is the most disputed part. In the "two Barbaras" problem, Aristotle accepts a Barbara with a necessary major premise and a plain minor premise yielding a necessary conclusion, but rejects the version with the modalities swapped; his student Theophrastus instead adopted the simpler rule that a conclusion is only as strong as its weakest premise.[^s3] Jacob Rosen's 2014 review describes the text as messy and finds outright inconsistencies, while crediting Marko Malink's 2013 reconstruction with showing that Aristotle's validity claims can all be made true together.[^s5]

**Arguments in use.** Later chapters turn practical. Book I advises how to find premises by surveying what follows from, and what is excluded by, the subject and predicate in question.[^s1] Book II studies circular and reciprocal proof, refutation, reduction to the impossible, and "begging the question," which Aristotle describes as trying to prove through itself what is not self-evident.[^s2] It also warns that a reductio fails when the absurd result does not actually depend on the assumption being attacked, the original "false cause" objection.[^s2]

**A workplace illustration.** A manager argues: "No contractor has database admin rights; every on-call engineer has admin rights; so no on-call engineer is a contractor." Aristotle would locate the middle term, *has admin rights*, in the predicate of both premises, which puts the argument in the second figure, so it is imperfect. Converting the first premise to "nothing with admin rights is a contractor" turns it into the perfect first-figure Celarent, and the conclusion is secured. If a colleague instead argued "No contractor has admin rights; no on-call engineer is a contractor; so no on-call engineer has admin rights," Aristotle's rule that two negative premises yield nothing would flag it at once.[^s3][^s1]

## Reception and interpretation

Corcoran's 1994 survey distinguishes two modern readings. Jan Łukasiewicz, in a 1951 book, read the syllogistic as an axiomatic theory with the perfect moods as axioms. In the early 1970s Corcoran and Timothy Smiley independently argued instead that it is a natural-deduction system of direct and indirect proofs, concerned with how one knows a conclusion follows, and Corcoran showed it to be semantically complete.[^s4] Corcoran notes that Aristotle never calls a perfect deduction an axiom.[^s4]

## Connections

- **Authored by Aristotle.** The treatise is Aristotle's, from about 350 BCE.[^s1][^s6]
- **Part of the Organon.** It is one of the six logical treatises later collected under that title.[^s3]
- **Studied in formal logic.** It founded syllogistic, the earliest branch of formal logic.[^s6]
- **Contrasts with the Posterior Analytics.** The two were read as one project: the *Prior* covers deduction in general, the *Posterior* adds the conditions for demonstration that yields knowledge.[^s3]
- **Formalized as natural deduction.** Corcoran and Smiley modelled its proof system as natural deduction, rather than as Łukasiewicz's axiom system.[^s4]
- **Source of syllogistic and counterexample methods.** Its figures, moods, reductions and term-based disproofs underlie the categorical syllogism and the method of counterexample.[^s3]
- **Modal syllogistic.** Its treatment of necessity and possibility remains contested among interpreters.[^s5][^s3]

## Sources

[^s1]: Aristotle, *Prior Analytics* Book I, trans. A. J. Jenkinson, The Internet Classics Archive. https://classics.mit.edu/Aristotle/prior.1.i.html (accessed 2026-11-04)
[^s2]: Aristotle, *Prior Analytics* Book II, trans. A. J. Jenkinson, The Internet Classics Archive. https://classics.mit.edu/Aristotle/prior.2.ii.html (accessed 2026-11-04)
[^s3]: Smith, "Aristotle's Logic", Stanford Encyclopedia of Philosophy, sections 2 and 5. https://plato.stanford.edu/entries/aristotle-logic/ (accessed 2026-11-04)
[^s4]: Corcoran, "The Founding of Logic: Modern Interpretations of Aristotle's Logic", *Ancient Philosophy* 14 (1994). https://philarchive.org/archive/CORTFO-2 (accessed 2026-11-04)
[^s5]: Rosen, review of Malink, *Aristotle's Modal Syllogistic*, Notre Dame Philosophical Reviews 2014.08.33. https://ndpr.nd.edu/reviews/aristotle-s-modal-syllogistic/ (accessed 2026-11-04)
[^s6]: "Prior Analytics", Encyclopaedia Britannica. https://britannica.com/topic/Prior-Analytics (accessed 2026-11-04)
