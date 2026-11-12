---
id: ct:existential-import
type: Concept
title: Existential import
aliases: [existential presupposition of categorical propositions]
domain: formal-logic
summary: >-
  The property a statement has when its truth requires that something exists,
  typically that its subject class has at least one member; logicians disagree
  about which categorical forms (A, E, I, O) carry it, and the answer decides
  which traditional immediate inferences and syllogisms count as valid.
level: intermediate
evidenceStatus: normative
broader: [ct:categorical-proposition]
related: [ct:square-of-opposition, ct:existential-fallacy, ct:venn-diagram-test, ct:predicate-logic, ct:subalternation, ct:george-boole, ct:aristotle, ct:william-of-ockham, ct:franz-brentano]
requires: [ct:categorical-proposition]
relations:
  - {predicate: studiedIn, object: ct:formal-logic, source: s3, confidence: high}
  - {predicate: formalizedBy, object: ct:free-logic, source: s2, confidence: medium}
  - {predicate: contrastsWith, object: ct:presupposition, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "The Traditional Square of Opposition"
    publisher: Stanford Encyclopedia of Philosophy (Parsons and Ciola, rev. 2025)
    url: https://plato.stanford.edu/ENTRIES/square/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
  - id: s2
    title: "Free Logic"
    publisher: Stanford Encyclopedia of Philosophy (Nolt, rev. 2025)
    url: https://plato.stanford.edu/entries/logic-free/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
  - id: s3
    title: "3.4 Problems with the Square of Opposition (An Introduction to Logic)"
    publisher: Kathy Eldred, Pima Community College Open Press (2024, CC BY-NC 4.0)
    url: https://pimaopen.pressbooks.pub/intrologic/?p=862
    type: textbook
    accessed: 2026-11-12
  - id: s4
    title: "Did Aristotle have a Doctrine of Existential Import?"
    publisher: Open Philosophy 8(1) (Byeong-uk Yi, 2025), De Gruyter Brill
    url: https://www.degruyterbrill.com/document/doi/10.1515/opphil-2025-0066/html
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Existential import

A statement has existential import when its being true requires that something exists.[^s3] "Some auditors are certified" cannot be true unless there is at least one auditor, so particular statements (the I and O forms of categorical logic) carry import on every standard account.[^s3] The live question is whether universal statements do: does "all late invoices are flagged" commit the speaker to there being late invoices? The answer is a choice of interpretation, not a fact to be discovered, and it fixes which inferences on the square of opposition, and which syllogisms, are valid.[^s1][^s3]

## Origin

For most of its history the square of opposition was coherent because of a particular view about import. Late medieval logicians generally held that affirmative propositions have existential import and negative ones do not, and by the end of the fourteenth century this was a common principle; Paul of Venice's *Logica Magna* (c. 1400) gives true particular negatives with empty subjects.[^s1] Aristotle phrased the O form as "not every S is P", which comes out true when S is empty, so the traditional relations hold without contradiction.[^s1] Yi (2025) surveys versions of the doctrine held by al-Fārābī, Abelard and Ockham, and argues against the standard view that Aristotle himself held it, proposing instead that Aristotle gave no categorical, even a particular affirmative, existential import.[^s4]

The modern reading arrived in the late nineteenth century, as Alonzo Church suggested.[^s1] Predicate logic writes "every S is P" as a universal conditional and "some S is not P" as an existential conjunction, so universals become vacuously true of an empty class while particulars still assert existence.[^s1] Introductory texts call this the Boolean standpoint, after George Boole, and contrast it with an Aristotelian standpoint on which all four forms carry import.[^s3] Yi traces the modern objection to subalternation, which rests on universals lacking import, back to Franz Brentano.[^s4]

## How it works

The two standpoints give different squares. On the Aristotelian standpoint, every A, E, I and O statement presupposes members of the subject class, so "all S are P" implies "some S are P" (subalternation), A and E cannot both be true (contraries), and I and O cannot both be false (subcontraries).[^s3] On the Boolean standpoint only I and O have import. If the subject class is empty, A and E are both vacuously true and I and O are both false, so contrariety, subcontrariety and subalternation fail, and only the contradictory diagonals survive.[^s3]

A workplace case shows why the choice matters. A policy says "all employees who miss two safety briefings are suspended." It is meant to keep that class empty, much as "deserters will be shot" is meant to deter desertion; the textbook uses that example to show that universals are often asserted precisely when no instances exist.[^s3] Reading the policy as implying that some employee has been suspended would be a mistake, and drawing that conclusion is the existential fallacy.[^s3]

Import also arises for single names. Classical first-order logic assumes every name refers to an object in the domain, so it licenses moving from a statement about a named thing to "something exists that…". Free logic, a name Karel Lambert coined, drops that assumption and restricts universal instantiation and existential generalisation to terms that refer.[^s2] Its standard example is that "Sleipnir does not exist" should not yield "something exists that does not exist."[^s2]

## How to apply it

- Before drawing a particular conclusion from universal premises, ask whether the subject class is known to be non-empty. If it is, state that as an explicit premise; if not, keep the conclusion universal or conditional.[^s1][^s3]
- When an argument relies on a traditional square relation (subalternation, contrariety), check which standpoint the text assumes; many textbooks adopt the Boolean one and flag Aristotelian-only inferences as conditionally valid.[^s3]
- Treat rules, hypotheses and policies about possible cases (future defects, the largest prime, an unconfirmed particle) as universals that may be true with nothing falling under them.[^s3]

## Limitations

Neither standpoint is cost-free. Adding an existence conjunct to the A form recovers subalternation, but the SEP entry notes this is a notational decision rather than a deep logical discovery.[^s1] Strawson's 1952 proposal treats empty-subject categoricals as neither true nor false, preserving the square but not conversion, contraposition and obversion, and Smiley (1967) showed that chaining such entailments can lead from truth to falsehood.[^s1] Historians also still dispute who held which doctrine.[^s4]

## Connections

- **Studied in formal logic.** Import is taught as a core choice point when categorical logic is reconciled with modern predicate logic.[^s3]
- **Formalised by free logic.** Free logic gives a formal treatment of existence assumptions for singular terms, alongside inclusive logics that allow an empty domain.[^s2]
- **Contrasts with presupposition.** Strawson's alternative treats existence as a presupposition whose failure leaves a statement without truth value, rather than as part of what it asserts.[^s1]
- **Square of opposition and existential fallacy.** Which square relations hold depends on import, and the existential fallacy is the error of assuming import the premises do not supply.[^s1][^s3]

## Sources

[^s1]: Parsons and Ciola, "The Traditional Square of Opposition", Stanford Encyclopedia of Philosophy (rev. 2025). https://plato.stanford.edu/ENTRIES/square/ (accessed 2026-11-12)
[^s2]: Nolt, "Free Logic", Stanford Encyclopedia of Philosophy (rev. 2025). https://plato.stanford.edu/entries/logic-free/ (accessed 2026-11-12)
[^s3]: Eldred, *An Introduction to Logic*, 3.4 "Problems with the Square of Opposition", Pima Community College Open Press (2024). https://pimaopen.pressbooks.pub/intrologic/?p=862 (accessed 2026-11-12)
[^s4]: Yi, "Did Aristotle have a Doctrine of Existential Import?", *Open Philosophy* 8(1), 2025. https://www.degruyterbrill.com/document/doi/10.1515/opphil-2025-0066/html (accessed 2026-11-12)
