---
id: ct:de-re-de-dicto-distinction
type: Technique
title: De re/de dicto distinction
aliases: [de re and de dicto readings, relational/notional distinction, wide-scope/narrow-scope reading of attitude reports]
domain: formal-logic
summary: >-
  The practice of separating two readings of a belief, knowledge or modal
  claim: de dicto, about how the subject thinks of or describes something
  (the term stays inside the "that"-clause), and de re, about the thing
  itself however it is described (the term takes wide scope). Fixing the
  reading shows when swapping co-referring terms is licensed.
level: intermediate
evidenceStatus: normative
broader: [ct:predicate-logic]
related: [ct:masked-man-fallacy, ct:referential-opacity, ct:ambiguity, ct:quantifier-shift-fallacy, ct:sense-and-reference, ct:willard-van-orman-quine]
requires: [ct:predicate-logic]
relations:
  - {predicate: detects, object: ct:masked-man-fallacy, source: s3, confidence: high}
  - {predicate: explainedBy, object: ct:quantifier-scope, source: s3, confidence: high}
  - {predicate: formalizedBy, object: ct:theory-of-descriptions, source: s4, confidence: medium}
  - {predicate: introducedBy, object: ct:peter-abelard, source: s2, confidence: medium}
sources:
  - id: s1
    title: "The De Re/De Dicto Distinction (supplement to Propositional Attitude Reports), Winter 2012 edition"
    publisher: Stanford Encyclopedia of Philosophy (Thomas McKay and Michael Nelson)
    url: https://plato.stanford.edu/archives/Win2012/entries/prop-attitude-reports/dere.html
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s2
    title: "The De re-De dicto Distinction: A Twelfth-Century Logical Discovery"
    publisher: "Vivarium 60(2-3), 162-191 (Irene Binini, 2022), author's copy via University of Parma repository"
    url: https://air.unipr.it/retrieve/07761e64-c565-44d3-914e-8962219f9449/Binini_De%20Re%20De%20Dicto_Vivarium%202022%2c%2060%2c%202-3.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "Frege's Problem: Referential Opacity"
    publisher: Internet Encyclopedia of Philosophy
    url: https://iep.utm.edu/referential-opacity/
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s4
    title: "24.251 Handout 3 (lecture notes on Russell on denoting)"
    publisher: MIT OpenCourseWare (Richard Holton, Spring 2005)
    url: https://dspace.mit.edu/bitstream/handle/1721.1/152349/24-251-spring-2005/contents/lecture-notes/handout3.pdf
    type: academic
    accessed: 2026-11-11
created: 2026-11-11
---

# De re/de dicto distinction

The de re/de dicto distinction separates two ways of reading a sentence that reports what someone believes, knows or wants, or what is necessary or possible. On the de dicto reading ("about what is said"), the report concerns how the subject thinks of or words the matter. On the de re reading ("about the thing"), it says of a particular object that the subject believes something about it, however that object is described.[^s1] Used as a technique, the distinction is a check: before accepting an inference that swaps one name or description for another inside "believes that", "knows that" or "necessarily", decide which reading each premise carries.[^s3]

## Origin

The distinction began in medieval modal logic. Irene Binini's 2022 study in *Vivarium* reports that it is usually credited to Peter Abelard, who used readings *de sensu* and *de rebus* as the basis of his modal semantics in the early twelfth century, and that only his *Dialectica* treats it systematically; she also shows that earlier masters, possibly including William of Champeaux, were already arguing over the problems behind it.[^s2] Their examples were modal, such as whether "it is possible for Socrates to walk" speaks of a proposition or of Socrates.[^s2]

The modern version comes from philosophy of language. Bertrand Russell's theory of descriptions let a description take wide or narrow scope relative to an attitude verb, as in his example of George IV wanting to know whether Scott was the author of *Waverley*.[^s4] W. V. Quine brought the de re/de dicto contrast for belief to the centre of logic in 1956 with "Ralph believes that someone is a spy": read narrowly it says only that Ralph thinks there are spies; read widely, there is a particular person Ralph suspects, which is what would interest investigators.[^s1]

## How it works

The Internet Encyclopedia of Philosophy treats de re, relational, transparent and wide scope as one side, and de dicto, notional, opaque and narrow scope as the other, and finds the scope labels the most useful because the contrast is visible in the sentence's structure.[^s3] A narrow-scope report, "Lois believes that Superman can fly", resists swapping in "Clark Kent". The exported form, "Superman is such that Lois believes he can fly", allows the swap, because the name now sits outside the belief and simply picks out the man.[^s3] De re reports also support existential generalisation (there is someone of whom Sally believes he is happy), while de dicto reports do not.[^s1]

A workplace example: the facilities team learns that the "anonymous tipster" who reported a safety hazard is the night supervisor. The site manager "believes the tipster acted in good faith". Read de dicto, this is about the manager's view of whoever sent the tip, and it says nothing about what the manager thinks of the night supervisor, whom they may distrust. Read de re, it says of that person that the manager thinks they acted in good faith, and only then may "the night supervisor" be substituted. The SEP notes a related trap: believing that the person at a given place is happy does not yield a de re belief about the individual who happens to be there.[^s1]

Modal sentences divide the same way. The SEP's example, "the shortest spy might not have been a spy", is false read as a claim about the proposition but plausibly true read as a claim about the person who is in fact the shortest spy.[^s1]

## How to apply it

1. **Find the operator.** Mark every attitude verb (believes, knows, suspects, expects) and modal word (must, necessarily, could have).[^s1]
2. **Locate each name or description.** Ask whether it sits inside the "that"-clause or could be moved outside it with "is such that".[^s3]
3. **Paraphrase both readings.** Write the narrow version ("X believes that the tipster…") and the wide version ("The tipster is someone X believes…").[^s3][^s1]
4. **Test the inference on each.** Substitution of co-referring terms and existential generalisation are safe only on the de re reading; if the premise is only true de dicto, the swapped conclusion does not follow.[^s1][^s3]
5. **Say which reading you mean.** Many disputes over what someone "knew" or "thought" dissolve once each side states its reading.[^s3]

**Pitfalls.** Exportation is not always safe: the IEP discusses cases, such as Sosa's shortest-spy example, where the wide reading sounds natural but is arguably literally false.[^s3] Philosophers still disagree about whether "believes" is ambiguous, as Quine suggested, about whether every true de re report has a de dicto counterpart, and about whether the three ways of drawing the line (syntactic, semantic and metaphysical) coincide.[^s1] Russell's own analysis was presented as a rival to Frege's, though the MIT handout notes it may amount to a version of it if senses are given by descriptions.[^s4]

## Connections

- **Detects the masked-man fallacy.** The IEP diagnoses substitution inferences of the Lois/Superman kind as hearing a premise de re but drawing the conclusion de dicto.[^s3]
- **Explained by quantifier scope.** The distinction is a difference in whether a term or quantifier takes wide or narrow scope relative to the attitude or modal operator.[^s3]
- **Formalised by Russell's theory of descriptions.** Russell's primary and secondary occurrences give the wide/narrow contrast a formal treatment.[^s4]
- **Introduced by Peter Abelard.** He gave the first systematic treatment of the distinction for modal propositions.[^s2]
- **Related to referential opacity and sense and reference.** Opaque contexts are where de dicto readings block substitution; Fregean accounts explain the distinction without positing an ambiguous verb.[^s1][^s3]
- **Related to the quantifier shift fallacy and ambiguity.** Both involve readings that differ only in scope, as in Quine's spy sentence.[^s1]

## Sources

[^s1]: T. McKay and M. Nelson, "The De Re/De Dicto Distinction", supplement to "Propositional Attitude Reports", Stanford Encyclopedia of Philosophy (Winter 2012 edition). https://plato.stanford.edu/archives/Win2012/entries/prop-attitude-reports/dere.html (accessed 2026-11-11)
[^s2]: I. Binini, "The De re-De dicto Distinction: A Twelfth-Century Logical Discovery", *Vivarium* 60(2-3), 162-191 (2022). https://air.unipr.it/retrieve/07761e64-c565-44d3-914e-8962219f9449/Binini_De%20Re%20De%20Dicto_Vivarium%202022%2c%2060%2c%202-3.pdf (accessed 2026-11-11)
[^s3]: "Frege's Problem: Referential Opacity", Internet Encyclopedia of Philosophy. https://iep.utm.edu/referential-opacity/ (accessed 2026-11-11)
[^s4]: R. Holton, 24.251 lecture notes, Handout 3, MIT OpenCourseWare (Spring 2005). https://dspace.mit.edu/bitstream/handle/1721.1/152349/24-251-spring-2005/contents/lecture-notes/handout3.pdf (accessed 2026-11-11)
