---
id: ct:truth-table
type: Technique
title: Truth table
aliases: [truth-table method, truth-table test, truth-table test of validity, truth matrix]
domain: formal-logic
summary: >-
  A mechanical test for arguments in propositional logic: list every
  combination of truth values for the simple sentences, compute each premise
  and the conclusion on every row, and the argument is valid exactly when no
  row makes all the premises true and the conclusion false.
level: introductory
evidenceStatus: normative
broader: [ct:propositional-logic]
related: [ct:method-of-counterexample, ct:validity, ct:venn-diagram-test, ct:disjunctive-syllogism, ct:modus-ponens]
requires: [ct:validity]
relations:
  - {predicate: detects, object: ct:affirming-a-disjunct, source: s1, confidence: medium}
  - {predicate: detects, object: ct:affirming-the-consequent, source: s3, confidence: high}
  - {predicate: introducedBy, object: ct:charles-sanders-peirce, source: s5, confidence: medium}
  - {predicate: introducedBy, object: ct:ludwig-wittgenstein, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Characteristic truth tables (Chapter 9)"
    publisher: "forall x: Calgary. An Introduction to Formal Logic (P. D. Magnus, Tim Button, with Loftis, Trueman, Thomas-Bolduc and Zach; Open Logic Project, University of Calgary)"
    url: https://forallx.openlogicproject.org/html/Ch9.html
    type: textbook
    accessed: 2026-11-06
  - id: s2
    title: "Semantic concepts (Chapter 12)"
    publisher: "forall x: Calgary. An Introduction to Formal Logic (Magnus, Button et al.; Open Logic Project)"
    url: https://forallx.openlogicproject.org/html/Ch12.html
    type: textbook
    accessed: 2026-11-06
  - id: s3
    title: "Partial truth tables (Chapter 15)"
    publisher: "forall x: Calgary. An Introduction to Formal Logic (Magnus, Button et al.; Open Logic Project)"
    url: https://forallx.openlogicproject.org/html/Ch15.html
    type: textbook
    accessed: 2026-11-06
  - id: s4
    title: "Limitations of TFL (Chapter 13)"
    publisher: "forall x: Calgary. An Introduction to Formal Logic (Magnus, Button et al.; Open Logic Project)"
    url: https://forallx.openlogicproject.org/html/Ch13.html
    type: textbook
    accessed: 2026-11-06
  - id: s5
    title: "Peirce's Truth-functional Analysis and the Origin of the Truth Table"
    publisher: "History and Philosophy of Logic 33(1), 87-97 (Irving H. Anellis, 2012), author's copy on arXiv"
    url: https://arxiv.org/pdf/1108.2429
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s6
    title: "Formal logic: The propositional calculus"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/formal-logic/The-propositional-calculus
    type: encyclopedia
    accessed: 2026-11-06
created: 2026-11-06
---

# Truth table

A truth table is a grid that sets out every way the simple sentences in an argument could be true or false, then works out what each complex sentence would be on each of those combinations.[^s6] In propositional logic, connectives such as "and", "or", "not" and "if…then" are truth-functional: the value of the whole sentence depends only on the values of its parts.[^s6] That makes a decisive test of validity possible. An argument is valid exactly when no row of the table makes every premise true and the conclusion false. A single such row shows that the premises fail to guarantee the conclusion.[^s2]

## Origin

Tables of truth values were drawn up independently by several logicians. Irving Anellis, writing in *History and Philosophy of Logic* in 2012, reports that an unpublished 1893 manuscript by Charles Sanders Peirce contains a truth-value matrix for the conditional, and that a 1902 Peirce manuscript sets out a three-variable table.[^s5] In 1997 John Shosky found matrices on the back of a typescript of a 1912 Bertrand Russell lecture. The negation table there is Russell's, and the implication table is in Ludwig Wittgenstein's handwriting.[^s5] Wittgenstein's *Tractatus Logico-Philosophicus* (1921–22) then made the device widely known, and Emil Post and Jan Łukasiewicz extended it to many-valued logics in the early 1920s.[^s5] Anellis argues that Peirce's 1893 matrix is the earliest truth table by an identifiable author, though credit for the device is still debated.[^s5]

## How it works

Each connective has a characteristic table. Logic textbooks read the standard "∨" as inclusive "or": a disjunction is true when at least one disjunct is true, including when both are.[^s1] The material conditional "if A then B" is false only on the row where A is true and B is false.[^s1] With *n* simple sentences, the table needs 2ⁿ rows. Two letters need 4 rows, three need 8, and the count keeps doubling.[^s6] Britannica calls the method the simplest and theoretically most important decision procedure for propositional logic, though not always the quickest to use. Because the table is finite and filled in mechanically, it always delivers a verdict.[^s6]

Consider a workplace post-incident review. "The outage was caused by the configuration change (C) or by the traffic spike (S). It was caused by the configuration change. So the traffic spike was not a cause." The premises are C ∨ S and C, and the conclusion is ¬S. On the row where C and S are both true, inclusive "or" makes the first premise true, the second premise is true, and the conclusion is false.[^s1][^s2] That one row is a counterexample, so the argument commits the fallacy of affirming a disjunct. Compare "C ∨ S; not C; therefore S". The only row where both premises are true is the one where C is false and S is true, and S is true there too, so this disjunctive syllogism is valid.[^s2] If the team really believes the two causes cannot occur together, they can add the premise "not both C and S". That premise is false on the troublesome row, which makes the argument valid. The table also makes the extra assumption visible so it can be checked.[^s1][^s2]

## How to apply it

1. **Symbolize.** Assign a letter to each simple claim and rewrite the premises and conclusion using the connectives. Check that "or" means what the speaker intends. If it is exclusive, state "not both" as a separate premise.[^s1]
2. **List the rows.** Write out all 2ⁿ combinations of T and F for the letters.[^s6]
3. **Compute.** Work out each premise and the conclusion row by row, from the innermost connective outward.[^s6]
4. **Read the verdict.** Look only at rows where every premise is true. If the conclusion is false on any of them, the argument is invalid. If it is true on all of them, or no such row exists, the argument is valid.[^s2]
5. **Take the shortcut when hunting for invalidity.** A partial truth table works backwards. Set the conclusion false, then try to make every premise true. Finding one such row proves invalidity, but showing validity requires ruling out every row.[^s3] The forall x textbook uses this shortcut on "A → B; B; therefore A". Making A false and B true gives true premises and a false conclusion, which exposes affirming the consequent.[^s3]

**Pitfalls.** The test only tracks truth-functional structure. Some arguments that are valid in English come out invalid on a table: "Daisy has four legs, so she has more than two" turns into two unrelated letters, and showing it valid needs first-order logic.[^s4] Tables also misread ordinary conditionals, because the material conditional counts any "if" sentence with a false antecedent as true. Vague predicates can likewise produce results that do not match intuition.[^s4] Because the row count doubles with each new letter, full tables quickly become unwieldy. Partial tables and other methods help here.[^s3][^s6]

## Connections

- **Detects affirming a disjunct.** The inclusive reading of "∨" gives a row where both disjuncts are true. On that row, affirming one disjunct and denying the other turns out to be true premises with a false conclusion.[^s1][^s2]
- **Detects affirming the consequent.** The forall x partial-table example exposes this conditional fallacy with a single row.[^s3]
- **Introduced by Peirce and Wittgenstein.** Anellis traces the earliest known matrix to Peirce in 1893 and records Wittgenstein's 1912 implication table, which later appeared in the *Tractatus*.[^s5]
- **Related techniques.** A truth table systematizes the method of counterexample for propositional forms: each row is a candidate counterexample, checked exhaustively.[^s2][^s3] The Venn diagram test plays the same role for categorical syllogisms, which truth tables cannot represent because they lack quantifiers.[^s4] The table also confirms valid forms such as disjunctive syllogism and modus ponens.[^s2]

## Sources

[^s1]: Magnus, Button et al., "Characteristic truth tables", *forall x: Calgary*, ch. 9. https://forallx.openlogicproject.org/html/Ch9.html (accessed 2026-11-06)
[^s2]: Magnus, Button et al., "Semantic concepts", *forall x: Calgary*, ch. 12. https://forallx.openlogicproject.org/html/Ch12.html (accessed 2026-11-06)
[^s3]: Magnus, Button et al., "Partial truth tables", *forall x: Calgary*, ch. 15. https://forallx.openlogicproject.org/html/Ch15.html (accessed 2026-11-06)
[^s4]: Magnus, Button et al., "Limitations of TFL", *forall x: Calgary*, ch. 13. https://forallx.openlogicproject.org/html/Ch13.html (accessed 2026-11-06)
[^s5]: Anellis, "Peirce's Truth-functional Analysis and the Origin of the Truth Table", *History and Philosophy of Logic* 33(1), 2012. https://arxiv.org/pdf/1108.2429 (accessed 2026-11-06)
[^s6]: "Formal logic: The propositional calculus", *Encyclopaedia Britannica*. https://www.britannica.com/topic/formal-logic/The-propositional-calculus (accessed 2026-11-06)
