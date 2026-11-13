---
id: ct:possible-worlds-semantics
type: Technique
title: Possible-worlds semantics
aliases: [Kripke semantics, relational semantics for modal logic, possible-world countermodel method]
domain: formal-logic
summary: >-
  A way of evaluating claims about necessity and possibility by treating
  "necessarily A" as A being true in every accessible possible world and
  "possibly A" as A being true in at least one; used as a test, it builds a
  small model of worlds in which a modal argument's premises hold and its
  conclusion fails.
level: intermediate
evidenceStatus: normative
broader: [ct:modal-logic]
related: [ct:modal-scope-fallacy, ct:method-of-counterexample, ct:de-re-de-dicto-distinction, ct:truth-tree, ct:logical-consequence, ct:validity]
requires: [ct:propositional-logic, ct:validity]
relations:
  - {predicate: detects, object: ct:modal-scope-fallacy, source: s5, confidence: high}
  - {predicate: partOf, object: ct:modal-logic, source: s3, confidence: high}
  - {predicate: introducedBy, object: ct:saul-kripke, source: s2, confidence: high}
  - {predicate: influencedBy, object: ct:rudolf-carnap, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Modal Logic, Summer 2006 edition"
    publisher: Stanford Encyclopedia of Philosophy (James Garson)
    url: https://plato.stanford.edu/archives/sum2006/entries/logic-modal
    type: scholarly-encyclopedia
    accessed: 2026-11-13
  - id: s2
    title: "Modern Origins of Modal Logic, Summer 2025 edition"
    publisher: Stanford Encyclopedia of Philosophy (Roberta Ballarin)
    url: https://plato.stanford.edu/archives/sum2025/entries/logic-modal-origins/
    type: scholarly-encyclopedia
    accessed: 2026-11-13
  - id: s3
    title: "Modal Logic: A Contemporary View"
    publisher: Internet Encyclopedia of Philosophy (Johan van Benthem)
    url: https://iep.utm.edu/modal-lo/
    type: scholarly-encyclopedia
    accessed: 2026-11-13
  - id: s4
    title: "Logic 2: Modal Logic, chapter 3: Accessibility"
    publisher: Wolfgang Schwarz (open online logic textbook)
    url: https://umsu.de/logic2/03-accessibility.html
    type: textbook
    accessed: 2026-11-13
  - id: s5
    title: "Foreknowledge and Free Will"
    publisher: Internet Encyclopedia of Philosophy (Norman Swartz)
    url: https://iep.utm.edu/foreknow/
    type: scholarly-encyclopedia
    accessed: 2026-11-13
created: 2026-11-13
---

# Possible-worlds semantics

Possible-worlds semantics gives precise truth conditions to "must", "might", "necessarily" and "possibly". A model is a set of worlds, an accessibility relation saying which worlds are relevant alternatives to which, and a valuation saying which simple sentences are true at each world. "Necessarily A" is true at a world when A is true at every world accessible from it; "possibly A" is true when A holds at some accessible world.[^s1][^s3] Used as a reasoning technique, it turns a vague question ("does this modal conclusion really follow?") into a concrete one: can I describe a few worlds where the premises are true and the conclusion is false?[^s1][^s4]

## Origin

The informal idea that necessary truths hold in every possible world goes back to Leibniz, and Rudolf Carnap, who spoke of "Leibnizian possible worlds", made it formal in the 1940s: his 1946 paper on modalities and his 1947 *Meaning and Necessity* defined logical truth through state-descriptions, which Roberta Ballarin's Stanford Encyclopedia entry treats as a forerunner of the semantics.[^s2] In the late 1950s and early 1960s several logicians, including Stig Kanger, Richard Montague, Jaakko Hintikka and Arthur Prior, worked with relations between worlds. Saul Kripke's 1959 completeness proof for quantified S5 and his 1963 papers, which treated worlds as simple points of evaluation linked by an accessibility relation and proved completeness for T, S4, S5 and B, are what made the approach standard.[^s2] The basic system K is named after him.[^s1]

## How it works

The accessibility relation lets one semantics serve many kinds of modality. In epistemic logic the accessible worlds are those compatible with what someone knows; in deontic logic, those where the rules are followed; in the logic of historical necessity, those still reachable from the present.[^s4] Conditions on the relation line up with familiar principles: a reflexive relation validates "if necessarily A, then A", a transitive one validates "if necessarily A, then necessarily necessarily A", and S5 results when every world can see every relevant world.[^s1][^s4] An argument is valid in a system when every model of that kind that makes the premises true at a world also makes the conclusion true there.[^s1]

The technique is most useful where English is ambiguous. "If A, then necessarily B" can mean that the conditional is necessary, □(A → B), or that B is necessary whenever A is actually true, A → □B, and the two are not equivalent.[^s1] The worlds picture makes the difference visible. □(A → B) says only that no accessible world makes A true and B false. A → □B says that, given A, B holds in every accessible world, including worlds where A is false.[^s5]

A workplace case: "If the contract has been signed, the client must pay the fee; the contract has been signed; so the client had no choice but to pay." Draw two worlds. In the actual world the contract is signed and the fee is paid. In an alternative world the client declined to sign and pays nothing. Every world satisfies "if signed, then paid", so the necessary conditional is true, and the contract is signed in the actual world, yet "paid" fails in the alternative world, so "necessarily paid" is false. The model shows the conclusion does not follow.[^s5][^s4]

## How to apply it

1. Rewrite each modal sentence with the operator in an explicit position, choosing between □(A → B) and A → □B rather than leaving "must" floating inside a conditional.[^s1]
2. Decide what kind of necessity is meant (logical, physical, legal, what someone knows) and so which worlds count as accessible.[^s4]
3. Try to build a countermodel: start with a world where the premises are true and the conclusion false, then add accessible worlds as each "necessarily" or "possibly" clause demands.[^s4]
4. If the construction succeeds, the argument is invalid for that kind of modality; if every attempt is blocked, look for a proof instead, or use a tree method that searches systematically.[^s4][^s1]

Pitfalls: a countermodel shows invalidity only relative to the frame conditions assumed, so an argument can fail in K and hold in S5.[^s1] And the actual truth of a sentence does not delete the worlds where it is false; Norman Swartz calls this the fixity of modal status.[^s5]

## Evidence and limitations

As a standard of correct reasoning, the method is normative rather than empirical. Its formal credentials are strong: Kripke and others proved that the main modal systems are sound and complete with respect to suitable classes of models.[^s1][^s2] Johan van Benthem notes that worlds need not be read metaphysically. They can be situations, information states or bare points in a graph, and the philosophical debates about what possible worlds are leave the technique intact.[^s3] Its limits show up mainly in quantified modal logic, where there is no agreed account of how one object is identified across worlds and choices about domains change which inferences hold.[^s3][^s1]

## Connections

- **Detects the modal scope fallacy.** Reading □(P → Q) as "no world makes P true and Q false" shows that actual P leaves worlds where Q is false, so "necessarily Q" does not follow.[^s5]
- **Part of modal logic.** It is the standard relational semantics for the field, with frame conditions matching modal axioms.[^s3][^s1]
- **Introduced by Saul Kripke, influenced by Rudolf Carnap.** Kripke's accessibility-relation models built on Carnap's state-description semantics.[^s2]
- **Related to the method of counterexample and truth trees.** A possible-worlds countermodel is the modal version of describing a case with true premises and a false conclusion, and modal trees search for one systematically.[^s4]
- **Related to the de re/de dicto distinction.** Both are tools for scope: Garson's warning that "if A then necessarily B" has two readings is a scope ambiguity of the kind that distinction also sorts out.[^s1]

## Sources

[^s1]: J. Garson, "Modal Logic", Stanford Encyclopedia of Philosophy (Summer 2006 edition). https://plato.stanford.edu/archives/sum2006/entries/logic-modal (accessed 2026-11-13)
[^s2]: R. Ballarin, "Modern Origins of Modal Logic", Stanford Encyclopedia of Philosophy (Summer 2025 edition). https://plato.stanford.edu/archives/sum2025/entries/logic-modal-origins/ (accessed 2026-11-13)
[^s3]: J. van Benthem, "Modal Logic: A Contemporary View", Internet Encyclopedia of Philosophy. https://iep.utm.edu/modal-lo/ (accessed 2026-11-13)
[^s4]: W. Schwarz, *Logic 2: Modal Logic*, ch. 3 "Accessibility". https://umsu.de/logic2/03-accessibility.html (accessed 2026-11-13)
[^s5]: N. Swartz, "Foreknowledge and Free Will", Internet Encyclopedia of Philosophy. https://iep.utm.edu/foreknow/ (accessed 2026-11-13)
