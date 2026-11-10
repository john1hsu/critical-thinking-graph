---
id: ct:truth-tree
type: Technique
title: Truth tree
aliases: [semantic tableau, semantic tableaux, analytic tableaux, method of analytic tableaux, tree method, tableau method]
domain: formal-logic
summary: >-
  A test of validity that lists an argument's premises together with the
  negation of its conclusion and breaks them down by rule into branches; if
  every branch closes on a contradiction the argument is valid, and a finished
  open branch describes a counterexample.
level: intermediate
evidenceStatus: normative
broader: [ct:predicate-logic]
related: [ct:truth-table, ct:method-of-counterexample, ct:validity, ct:quantifier-scope, ct:propositional-logic, ct:raymond-smullyan]
requires: [ct:validity]
relations:
  - {predicate: detects, object: ct:quantifier-shift-fallacy, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:evert-willem-beth, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:jaakko-hintikka, source: s2, confidence: medium}
  - {predicate: influencedBy, object: ct:gerhard-gentzen, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Chapter 8: Validity Testing"
    publisher: "Logic in Action, open course book (Institute for Logic, Language and Computation, University of Amsterdam)"
    url: https://www.logicinaction.org/docs/ch8.pdf
    type: textbook
    accessed: 2026-11-10
  - id: s2
    title: "First-Order Logic (Raymond M. Smullyan, 1968), preface and ch. II, Analytic Tableaux"
    publisher: "Springer-Verlag, Ergebnisse der Mathematik und ihrer Grenzgebiete 43 (course copy, Cornell CS 4860)"
    url: https://www.cs.cornell.edu/courses/cs4860/2020fa/resources/Smullyan-Book-Full.pdf
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "8.3: Proving Invalidity with Truth Trees"
    publisher: "A Modern Formal Logic Primer, Vol. I (Paul Teller), LibreTexts"
    url: https://human.libretexts.org/Bookshelves/Logic/Map%3A_A_Modern_Formal_Logic_Primer_(Teller)/Volume_I%3A_Sentence_Logic/8%3A_Truth_Trees_for_Sentence_Logic_-_Fundamentals/8.3%3A_Proving_Invalidity_with_Truth_Trees
    type: textbook
    accessed: 2026-11-10
  - id: s4
    title: "3.8.4: Infinite Trees"
    publisher: "A Modern Formal Logic Primer, Vol. II (Paul Teller), LibreTexts"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/A_Modern_Formal_Logic_Primer_(Teller)/03%3A_Volume_II-_Predicate_Logic/3.08%3A_More_on_Truth_Trees_for_Predicate_Logic/3.8.04%3A_Infinite_Trees
    type: textbook
    accessed: 2026-11-10
  - id: s5
    title: "Truth Trees for Predicate Logic"
    publisher: "Computability and Logic course slides, Rensselaer Polytechnic Institute"
    url: https://homepages.hass.rpi.edu/heuveb/Teaching/Logic/CompLogic/Web/Presentations/QTrees.pdf
    type: academic
    accessed: 2026-11-10
  - id: s6
    title: "Quantifiers in tableaux"
    publisher: "The Logic Notes, Australian National University"
    url: https://users.cecs.anu.edu.au/~jks/LogicNotes/quantifiers-in-tableaux.html
    type: academic
    accessed: 2026-11-10
created: 2026-11-10
---

# Truth tree

A truth tree, also called a semantic tableau, is a systematic search for a counterexample. To test an argument, you write down its premises and the denial of its conclusion, then break each complex sentence into simpler parts by fixed rules. Some rules extend a branch and others split it in two. A branch closes when it contains a sentence and its negation. If every branch closes, no counterexample is possible and the argument is valid; if a finished branch stays open, its simple sentences describe a situation where the premises are true and the conclusion false.[^s3][^s2]

## Origin

The Dutch logician Evert Willem Beth introduced the tableau method for propositional and predicate logic in the 1950s.[^s1] Jaakko Hintikka developed a related tableau system, and Raymond Smullyan's 1968 book *First-Order Logic* combined features of both into "analytic tableaux": a single tree of signed formulas in which each step only breaks a formula into its own subformulas. Smullyan traced the underlying idea back to Gerhard Gentzen's proof theory.[^s2] Introductory logic textbooks and courses now teach the method under the name "truth trees", for sentence logic and for predicate logic alike.[^s3][^s5]

## How it works

Take the sentential argument "A or B; therefore A and B". The tree starts with "A or B" and "not (A and B)". The disjunction splits into an A branch and a B branch, and the negated conjunction splits each of those into not-A and not-B. Two paths close on a contradiction; two stay open. One open path has A true and B false, which is a counterexample, so the argument is invalid.[^s3]

With quantifiers the rules add names. A universal sentence may be instantiated with any name on the branch, and again for every new name that turns up. An existential sentence must be instantiated with a fresh name, since the object that satisfies it may be a new one.[^s5][^s6] This is what lets trees expose a quantifier shift. The *Logic in Action* textbook tests whether "everything bears R to something" entails "something is borne R by everything" and finds a finished open branch with two objects, each related to itself and not to the other. In that model each object has its own partner, yet no single object is the partner of all, so the inference fails.[^s1] The argument map on the quantifier-shift page has the same shape: each project has its own budget approver, but nothing shows one approver covers every project.

## How to apply it

1. Write each premise and the negation of the conclusion at the top of the tree.[^s3]
2. Break down each compound sentence by its rule. Instantiate an existential with a name new to the branch, and return to every universal whenever a new name appears.[^s5][^s6]
3. Close any branch that contains a sentence and its denial.[^s3][^s5]
4. A branch is finished when only atomic sentences, their negations, and universals already instantiated for every name on the branch remain.[^s5]
5. If every branch closes, the argument is valid. If a finished branch is open, read the counterexample off it: its named objects form the domain, and its atomic sentences say what is true and false of them.[^s1][^s6]

**Use it** when a natural-language argument mixes "every" and "some", or when you want an explicit counterexample to show someone rather than a bare verdict.[^s1][^s3]

**Pitfalls.** In predicate logic the method no longer decides every case. A sentence such as "everyone loves someone" can produce a tree that never ends, because each fresh name triggers another universal instance and another existential, even though a one-object model would do.[^s4] Some invalid arguments have only infinite countermodels, so no tableau can display them; after the work of Church and Turing in the 1930s, no procedure can detect every invalid predicate-logic argument.[^s1][^s6] Teller adds that spotting such trees in advance can take ingenuity rather than rule-following.[^s4]

## Connections

- **Detects the quantifier shift fallacy.** A finished open branch for "every x has some y" against "some y for every x" gives a concrete two-object countermodel.[^s1]
- **Introduced by Evert Willem Beth and Jaakko Hintikka.** Beth introduced semantic tableaux in the 1950s; Smullyan credits his analytic tableaux to a blend of Beth's and Hintikka's systems.[^s1][^s2]
- **Influenced by Gerhard Gentzen.** Smullyan says the idea ultimately comes from Gentzen's work.[^s2]
- **Related to the truth table and the method of counterexample.** Like a truth table, a tree tests validity mechanically in sentence logic; like the method of counterexample, it shows invalidity by producing a case with true premises and a false conclusion.[^s3][^s1]
- **Broader: predicate logic.** The tree method extends to quantifiers, where it is sound and finds countermodels but is not a full decision procedure.[^s6][^s4]

## Sources

[^s1]: "Chapter 8: Validity Testing", *Logic in Action*, ILLC, University of Amsterdam. https://www.logicinaction.org/docs/ch8.pdf (accessed 2026-11-10)
[^s2]: R. M. Smullyan, *First-Order Logic*, Springer-Verlag, 1968, preface and ch. II. https://www.cs.cornell.edu/courses/cs4860/2020fa/resources/Smullyan-Book-Full.pdf (accessed 2026-11-10)
[^s3]: P. Teller, "Proving Invalidity with Truth Trees", *A Modern Formal Logic Primer*, Vol. I, LibreTexts. https://human.libretexts.org/Bookshelves/Logic/Map%3A_A_Modern_Formal_Logic_Primer_(Teller)/Volume_I%3A_Sentence_Logic/8%3A_Truth_Trees_for_Sentence_Logic_-_Fundamentals/8.3%3A_Proving_Invalidity_with_Truth_Trees (accessed 2026-11-10)
[^s4]: P. Teller, "Infinite Trees", *A Modern Formal Logic Primer*, Vol. II, LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/A_Modern_Formal_Logic_Primer_(Teller)/03%3A_Volume_II-_Predicate_Logic/3.08%3A_More_on_Truth_Trees_for_Predicate_Logic/3.8.04%3A_Infinite_Trees (accessed 2026-11-10)
[^s5]: "Truth Trees for Predicate Logic", Computability and Logic slides, Rensselaer Polytechnic Institute. https://homepages.hass.rpi.edu/heuveb/Teaching/Logic/CompLogic/Web/Presentations/QTrees.pdf (accessed 2026-11-10)
[^s6]: "Quantifiers in tableaux", The Logic Notes, Australian National University. https://users.cecs.anu.edu.au/~jks/LogicNotes/quantifiers-in-tableaux.html (accessed 2026-11-10)
