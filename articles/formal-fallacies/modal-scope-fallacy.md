---
id: ct:modal-scope-fallacy
type: FormalFallacy
title: Modal scope fallacy
aliases: [the modal fallacy, fallacy of necessity, confusing necessity of the consequence with necessity of the consequent]
domain: formal-fallacies
summary: >-
  The invalid inference from "necessarily, if P then Q" and "P" to
  "necessarily Q", which moves a necessity operator from the whole
  conditional onto its consequent and so turns a conditional, relative
  necessity into an absolute one.
level: intermediate
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:de-re-de-dicto-distinction, ct:quantifier-shift-fallacy, ct:necessary-and-sufficient-conditions, ct:boethius, ct:peter-abelard, ct:aristotle]
requires: [ct:modus-ponens, ct:validity]
relations:
  - {predicate: formalizedBy, object: ct:modal-logic, source: s1, confidence: high}
  - {predicate: invalidFormOf, object: ct:modus-ponens, source: s3, confidence: medium}
  - {predicate: explainedBy, object: ct:amphiboly, source: s4, confidence: medium}
criticalQuestions:
  - Does the "must" or "cannot" govern the whole if-then claim, or only the part after "then"?
  - Read with the modal over the whole conditional, does the conclusion still follow?
  - Read with the modal on the consequent alone, is that premise still true?
  - Is the necessity in the conclusion logical, or only relative to the facts assumed in the premises?
argumentMap:
  premises:
    - "If the release has passed every regression test, it cannot contain a regression."
    - "The release has passed every regression test."
  conclusion: "It is impossible for this release to contain a regression."
  verdict: invalid
  objections:
    - "What is impossible is passing every test that would catch a regression while still containing that regression; the 'cannot' governs the whole conditional."
    - "The valid conclusion is only that the release contains no regression the tests check for, not that it could not have contained one."
sources:
  - id: s1
    title: "Foreknowledge and Free Will"
    publisher: Internet Encyclopedia of Philosophy (Norman Swartz)
    url: https://iep.utm.edu/foreknow/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
  - id: s2
    title: "Medieval Theories of Future Contingents, Spring 2010 edition"
    publisher: Stanford Encyclopedia of Philosophy (Simo Knuuttila)
    url: https://plato.stanford.edu/archives/spr2010/entries/medieval-futcont/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
  - id: s3
    title: "\"The\" Modal Fallacy"
    publisher: Simon Fraser University, Department of Philosophy (Norman Swartz, rev. 2011)
    url: https://sfu.ca/~swartz/modal_fallacy.htm
    type: academic
    accessed: 2026-11-12
  - id: s4
    title: "Modal Scope Fallacy"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://www.fallacyfiles.org/modlscop.html
    type: community
    accessed: 2026-11-12
created: 2026-11-12
modified: 2026-11-12
---

# Modal scope fallacy

The modal scope fallacy is the invalid step from "necessarily, if P then Q" together with "P" to "necessarily Q". In modal-logic notation it treats □(P ⊃ Q) as though it were P ⊃ □Q, the form that would license the stronger conclusion.[^s1][^s3] The first sentence says that one combination of truth values, P true with Q false, is impossible. The second says that Q is a necessary truth whenever P holds. These claims are not equivalent, so an argument that slides from one to the other is invalid whatever its subject matter.[^s1]

## Origin

The underlying distinction is ancient. Medieval logicians inherited it from Boethius, who separated "conditional necessity" from "simple necessity" when answering the worry that God's foreknowledge makes the future necessary: if God knows that p, then p, but p is not thereby simply necessary.[^s2] In the twelfth century Peter Abelard recast the point as a difference between reading a modal statement in the compound sense (de sensu) and in the divided sense (de re), and showed that the foreknowledge argument is invalid on the reading that makes its premise true. Thomas Aquinas later stated it with the Latin terms *necessitas consequentiae* (necessity of the consequence, the whole conditional) and *necessitas consequentis* (necessity of the consequent).[^s2]

The modern labels "the modal fallacy" and "modal scope fallacy" are associated with the philosopher Norman Swartz, who argued that the error drives classic arguments for logical fatalism, including readings of Aristotle's sea-battle puzzle, and for theological fatalism from divine foreknowledge.[^s1][^s3] The Fallacy Files cites Swartz's usage and his 1979 logic textbook with Raymond Bradley as its sources for the fallacy.[^s4]

## How it works

Natural language makes the slip easy. English tends to put "must", "cannot" or "necessarily" inside the "then" clause even when the necessity belongs to the link between the clauses.[^s1][^s3] Swartz's illustration is a man with one daughter and two sons: given those facts, he must have a son. But the "must" holds only relative to the facts assumed. As a matter of logic, nobody has to have a son.[^s3]

The argument map shows the same pattern at work. "If the release has passed every regression test, it cannot contain a regression" is true only when read as "it is impossible to pass every test that would catch a regression and still contain one". With the premise read that way, the valid conclusion from "it passed" is just "it contains no such regression", not that a regression was impossible. Read the premise instead as putting the impossibility on the consequent alone, and the conclusion follows but the premise becomes false, because a release could have had a bug.[^s3][^s4] The Fallacy Files describes the fallacy as exploiting this ambiguity: one reading makes the argument valid, the other makes the premise true, and no single reading does both.[^s4]

The best-known philosophical cases follow the same pattern. "Necessarily, if it is true that I will do X, then I will do X" is a trivial logical truth. Fatalist arguments treat it as "if it is true that I will do X, then necessarily I will do X", and conclude that the future is unavoidable.[^s1] The epistemic version moves from "if you know p, you cannot be mistaken" to the claim that knowledge requires certainty, or that only necessary truths can be known.[^s3][^s4]

## How to spot it

Look for a conditional whose consequent carries a modal word ("must", "cannot", "has to", "necessarily", "is bound to") and an argument that then detaches that modal after affirming the antecedent.[^s3][^s4] Rewrite the premise twice, once with the modal over the whole conditional and once with it on the consequent, and ask which reading the argument needs at each step.[^s4] A conclusion about what is necessary or inevitable, drawn from premises that only describe what is the case, is a strong signal.[^s1]

## How to counter it

Point out that the necessity belongs to the connection, not to the consequent: it is impossible for the antecedent to be true and the consequent false, and that is all.[^s1] Then grant the valid conclusion, which is the plain consequent without the modal, and ask what separate evidence would show it to be necessary.[^s3] A parallel argument also helps. Fallacy Files offers one: if a man is a bachelor he cannot be married, and if he cannot be married he must be a priest, so all bachelors are priests.[^s4] Swartz adds a caution: showing that one formalization is invalid does not prove the English argument fails, because a more charitable rendering may be available.[^s3]

## Connections

- **Formalized by modal logic.** The box notation makes the two readings visibly different, □(P ⊃ Q) versus P ⊃ □Q, and shows they are not equivalent.[^s1]
- **Invalid look-alike of modus ponens.** From □(P ⊃ Q) and P the valid conclusion is Q; the fallacy attaches the necessity to the conclusion as well.[^s3]
- **Explained by amphiboly.** The fallacy trades on a scope ambiguity in how a modal word attaches to a sentence.[^s4]
- **Related to the de re/de dicto distinction and Peter Abelard.** Abelard's compound and divided senses are the medieval tool for the same diagnosis.[^s2]
- **Related to Boethius and Aristotle.** Boethius's conditional versus simple necessity answers foreknowledge arguments, and Aristotle's sea battle is a classic logical-fatalist case.[^s2][^s1]
- **Related to the quantifier shift fallacy.** Both are scope errors, here with a modal operator instead of a quantifier.[^s4]
- **Related to necessary and sufficient conditions.** Swartz describes the error as mistaking a necessary condition for a necessary truth.[^s3]

## Sources

[^s1]: N. Swartz, "Foreknowledge and Free Will", Internet Encyclopedia of Philosophy. https://iep.utm.edu/foreknow/ (accessed 2026-11-12)
[^s2]: S. Knuuttila, "Medieval Theories of Future Contingents", Stanford Encyclopedia of Philosophy (Spring 2010 edition). https://plato.stanford.edu/archives/spr2010/entries/medieval-futcont/ (accessed 2026-11-12)
[^s3]: N. Swartz, "'The' Modal Fallacy", Simon Fraser University (rev. 2011). https://sfu.ca/~swartz/modal_fallacy.htm (accessed 2026-11-12)
[^s4]: G. N. Curtis, "Modal Scope Fallacy", The Fallacy Files. https://www.fallacyfiles.org/modlscop.html (accessed 2026-11-12)
