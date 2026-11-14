---
id: ct:liar-paradox
type: Concept
title: Liar paradox
aliases: [the Liar, paradox of the liar, Epimenides paradox, strengthened liar]
domain: philosophy-of-reasoning
summary: >-
  The family of paradoxes built from a sentence that says of itself that it is
  false or not true ("This sentence is not true"): if it is true it is not, and
  if it is not, it is, so seemingly obvious principles about truth plus ordinary
  logic yield a contradiction.
level: intermediate
evidenceStatus: normative
broader: [ct:paradox]
related: [ct:sorites-paradox, ct:alfred-tarski, ct:saul-kripke, ct:chrysippus, ct:stoic-logic, ct:john-buridan, ct:principle-of-explosion, ct:reductio-ad-absurdum]
requires: [ct:propositional-logic]
relations:
  - {predicate: introducedBy, object: ct:eubulides, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:logic, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:philosophy-of-language, source: s1, confidence: medium}
  - {predicate: formalizedBy, object: ct:paraconsistent-logic, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Liar Paradox"
    publisher: Stanford Encyclopedia of Philosophy (Rossi, rev. 2026)
    url: https://plato.stanford.edu/ENTRiES/liar-paradox/
    type: scholarly-encyclopedia
    accessed: 2026-11-14
  - id: s2
    title: "Liar Paradox"
    publisher: Internet Encyclopedia of Philosophy (Dowden)
    url: https://iep.utm.edu/liar-par/
    type: scholarly-encyclopedia
    accessed: 2026-11-14
  - id: s3
    title: "Outline of a Theory of Truth"
    publisher: Kripke, The Journal of Philosophy 72(19), 690-716 (1975), copy hosted by IMPAN truth seminar
    url: https://www.impan.pl/~kz/truthseminar/Kripke_Outline.pdf
    type: primary
    accessed: 2026-11-14
created: 2026-11-14
---

# Liar paradox

The liar paradox is a family of puzzles in which a sentence says of itself that it is false or not true.[^s1] Take "This sentence is not true." If it is true, then what it says holds, so it is not true; if it is not true, then that is exactly what it says, so it is true.[^s1][^s2] Using only basic logic and principles about truth that seem beyond doubt, we reach a contradiction, and in classical logic a contradiction lets anything at all be derived.[^s1][^s2] For critical thinkers the Liar is the standard warning that self-reference and an unrestricted notion of "true" can break an otherwise sound reasoning system.

## Origin

The Liar is usually traced to Eubulides of Miletus, a contemporary of Socrates whose list of seven puzzles included it; his own discussion is lost.[^s2] A related tradition attributes a version to Epimenides of Crete, a Cretan said to have called all Cretans liars, though the Stanford entry treats that attribution with caution.[^s1] Ancient logicians took it seriously: Chrysippus wrote six works on it and Theophrastus three, none of which survive.[^s2] Medieval logicians studied it among the *insolubilia*, and Jean Buridan built a two-sentence variant into an argument for God's existence.[^s2][^s1] The modern debate begins with Alfred Tarski, who in the 1930s set out the truth schema and proved that a classical formal language cannot define its own truth predicate.[^s1][^s2]

## How it works

The paradox needs three ingredients.[^s1] First, **self-reference**: a sentence that can talk about itself, either directly ("this sentence") or by a name or description; Kripke stresses that such reference is often perfectly harmless, as in naming a sentence and then calling it short.[^s3] Second, the **truth schema**: a sentence *A* is true if and only if *A*. Third, **classical logic**, including the rule that every sentence is either true or not true.[^s1] Feed the Liar into the schema and the two sides of the biconditional collide.

A simple-falsity version, "This sentence is false", can be escaped by denying that every sentence is true or false. The **strengthened Liar**, "This sentence is not true", blocks that exit, because a sentence that is neither true nor false is still *not true*, which is what it claims.[^s1][^s2] Each repair tends to invite a new Liar phrased in the repair's own terms, such as "This sentence is false or meaningless"; philosophers call this the **revenge** problem.[^s1][^s2]

Kripke showed that Liars need not be deliberately constructed.[^s3] A workplace version: in a project review, the finance lead says "Every claim the engineering lead makes in this meeting is false," and the engineering lead, as it happens, makes just one claim: "Something the finance lead says in this meeting is true." Each remark is ordinary, and with other claims in play either could have a stable value; given only these two, no consistent assignment exists. Whether a statement about truth is paradoxical can depend on unlucky empirical facts, so no test of grammar or meaning alone can screen out the dangerous ones.[^s3]

## How to apply it

- **Separate levels of talk.** When a document, policy or argument evaluates its own claims ("all statements in this report are unreliable"), state which statements the evaluation covers; Tarski's object-language and metalanguage split is the formal model of this habit.[^s1][^s2]
- **Watch for self-sealing claims.** A claim that certifies or condemns itself cannot be checked by appeal to itself; look for independent grounding.[^s3]
- **Treat a contradiction as a signal, not a licence.** In classical logic a contradiction implies everything, so when reasoning produces one, locate the faulty premise rather than accepting whatever follows.[^s2]

## Evidence and limitations

As a logical puzzle the Liar is normative, and there is no agreed solution.[^s1] The main families are:

- **Hierarchies.** Tarski indexes truth predicates by level so no sentence can call itself true or untrue. Critics reply that ordinary speakers use one word "true", and Kripke argued that levels cannot be fixed in advance when the facts decide whether a claim is paradoxical.[^s2][^s3]
- **Truth-value gaps.** Kripke's 1975 fixed-point construction, developed at about the same time by Martin and Woodruff, lets "true" be partially defined: grounded sentences get values and the Liar falls into a gap.[^s3][^s2] Kripke admitted that the claim that the Liar is not true cannot be stated inside the language, so "the ghost of the Tarski hierarchy" remains.[^s3]
- **Gluts (dialetheism).** Graham Priest holds that the Liar is both true and not true, using a paraconsistent logic in which a contradiction does not entail everything; critics cite Curry's paradox and the intuition that nothing is both true and false.[^s1][^s2]
- **Contextualism.** Parsons, Burge and Glanzberg explain the apparent shift in the Liar's status by a change in context partway through the reasoning.[^s1]

## Connections

- **Introduced by** Eubulides of Miletus, the earliest named source of the puzzle.[^s2]
- **Studied in** logic and the philosophy of language, where theories of truth and self-reference are tested against it.[^s1]
- **Formalized by** paraconsistent logic, in which Priest models the Liar as a true contradiction without triviality.[^s1]
- **Broader:** paradox. **Related to** the sorites paradox, another ancient puzzle about classical logic and our concepts; Tarski and Kripke, whose theories of truth were shaped by it; Chrysippus, Stoic logic and Buridan, who studied it; the principle of explosion, which makes it dangerous; and reductio ad absurdum, the pattern of reasoning that turns it into a contradiction.[^s1][^s2][^s3]

## Sources

[^s1]: L. Rossi, "Liar Paradox", Stanford Encyclopedia of Philosophy (rev. 2026). https://plato.stanford.edu/ENTRiES/liar-paradox/ (accessed 2026-11-14)
[^s2]: B. Dowden, "Liar Paradox", Internet Encyclopedia of Philosophy. https://iep.utm.edu/liar-par/ (accessed 2026-11-14)
[^s3]: S. Kripke, "Outline of a Theory of Truth", *The Journal of Philosophy* 72(19), 690-716 (1975). https://www.impan.pl/~kz/truthseminar/Kripke_Outline.pdf (accessed 2026-11-14)
