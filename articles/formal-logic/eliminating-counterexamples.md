---
id: ct:eliminating-counterexamples
type: Technique
title: Eliminating counterexamples
aliases: [ECE framework, eliminating-counterexamples framework, counterexample-set reasoning]
domain: formal-logic
summary: >-
  A technique for judging a general conditional claim by describing the whole
  set of its possible counterexamples (cases that meet the condition but not
  the conclusion) and then arguing that those cases cannot exist or exhibiting
  one. Comparing counterexample sets shows that a claim and its contrapositive
  stand or fall together, while a claim and its converse do not.
level: introductory
evidenceStatus: mixed
broader: [ct:deductive-reasoning]
related: [ct:method-of-counterexample, ct:contraposition, ct:commutation-of-conditionals, ct:necessary-and-sufficient-conditions, ct:truth-table, ct:material-conditional]
requires: [ct:necessary-and-sufficient-conditions]
relations:
  - {predicate: detects, object: ct:commutation-of-conditionals, source: s3, confidence: medium}
  - {predicate: counteracts, object: ct:commutation-of-conditionals, source: s1, confidence: low}
  - {predicate: explainedBy, object: ct:mental-model-theory, source: s2, confidence: high}
  - {predicate: introducedBy, object: ct:david-yopp, source: s3, confidence: high}
  - {predicate: appliedIn, object: ct:mathematics-education, source: s2, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Eliminating counterexamples: An intervention for improving adolescents' contrapositive reasoning"
    publisher: "Journal of Mathematical Behavior 59, 100794 (David A. Yopp, 2020), author's copy via CADRE"
    url: https://www.cadrek12.org/sites/default/files/Yopp%202020%20JMB.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Eliminating counterexamples: A case study intervention for improving adolescents' ability to critique direct arguments"
    publisher: "Journal of Mathematical Behavior 57, 100751 (Yopp, Ely, Adams, Nielsen & Corwine, 2020), author's copy via CADRE"
    url: https://cadrek12.org/sites/default/files/Yopp%20et%20al%202020%20JMB.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "Eliminating Counterexamples: A Conception of Contrapositive Proving for Adolescents"
    publisher: "NCTM Research Conference, brief research report (David A. Yopp, San Francisco, 2016)"
    url: https://nctm.confex.com/nctm/2016RP/webprogram/Manuscript/Session42104/NCTM%20eliminate%20CEs%20paper.3.10.16.uploaded.pdf
    type: primary
    accessed: 2026-11-16
  - id: s4
    title: "Partial truth tables (Chapter 15)"
    publisher: "forall x: Calgary. An Introduction to Formal Logic (Magnus, Button et al.; Open Logic Project)"
    url: https://forallx.openlogicproject.org/html/Ch15.html
    type: textbook
    accessed: 2026-11-16
created: 2026-11-16
---

# Eliminating counterexamples

Eliminating counterexamples (ECE) is a way of reasoning about general "if…then" claims. It starts from one fact: a general conditional is true exactly when it has no counterexamples, meaning no case that satisfies the condition but fails the conclusion.[^s2] The reasoner therefore does not reach straight for a proof. First they write down what a counterexample would have to look like, describing the whole set of such cases by their properties. Then they either produce a member of that set, which refutes the claim, or argue that the set must be empty, which proves it.[^s1][^s2] Because the method works with the set of falsifying cases, it also gives a simple test for whether two conditionals say the same thing. If their counterexample sets match, they stand or fall together. If the sets differ, one can be true while the other is false.[^s3]

## Origin

The framework comes from mathematics-education research by David A. Yopp. He presented it in 2016 as a conception of contrapositive proving for adolescents, built on a two-year case study of one Grade 8 student.[^s3] Yopp grounds it in Philip Johnson-Laird's mental-model theory. On that theory a conditional "if p then q" is judged by whether a possibility with p and not-q can exist, so proving a claim means ruling that possibility out.[^s3][^s2] He presents the approach as a meta-level justification that students can build from their own counterexample reasoning, without first learning formal truth tables.[^s3] A 2020 paper by Yopp and colleagues describes ECE as one strand of a year-long Grade 8 argumentation intervention.[^s2] A second 2020 paper turned it into a 17-day, 17-task unit on contrapositive reasoning. That paper builds on Yopp's 2017 learning-trajectory study.[^s1]

## How it works

The method rests on a fact about counterexample sets. The counterexamples to "if p then q" are the cases with p and not-q. The counterexamples to the contrapositive, "if not-q then not-p", are the cases with not-q and p: the same cases, listed in a different order. Ruling out one set therefore rules out the other, which is why a proof of the contrapositive proves the original claim.[^s1][^s3] The converse, "if q then p", has a different set: the cases with q and not-p. That is why reversing a conditional is not a safe step.[^s3] Formal logic gives the same verdict. A single valuation that makes "if p then q" true and "if q then p" false is enough to show that the two sentences are not equivalent.[^s4]

A workplace example shows the difference. A team's rule says: "If a pull request changes the database schema, it gets a review from the database administrator." Its counterexamples are schema-changing pull requests that were merged without that review. The contrapositive, "if a pull request had no administrator review, it did not change the schema", has exactly the same counterexamples, so an audit of either statement is an audit of both. Now suppose someone reads the review log and concludes, "This pull request was reviewed by the administrator, so it must change the schema." That step relies on the converse. The converse's counterexamples are reviewed pull requests that leave the schema alone, such as query-tuning changes sent for a second opinion. Nothing in the original rule rules them out, so the inference commits the commutation of conditionals. Yopp's classroom materials use the same contrast with numbers. "If n is divisible by 3, it is divisible by 6" fails at n = 3. Its converse, "if n is divisible by 6, it is divisible by 3", has no counterexamples.[^s1]

## How to apply it

1. **Name the claim's parts.** Identify the condition and the conclusion of the general claim.[^s2]
2. **Describe every counterexample.** Write the property a case would need: it meets the condition and fails the conclusion. Describe the whole collection, even if you suspect it is empty.[^s1][^s2]
3. **Search or eliminate.** Either find a member of the set, which refutes the claim, or give an argument that no member can exist, which proves it.[^s1][^s2]
4. **Compare sets before swapping statements.** Before treating a reworded claim as equivalent, such as a contrapositive or a converse, describe its counterexample set. Treat the two as interchangeable only if the sets coincide.[^s3]
5. **Critique arguments the same way.** Ask whether an offered argument actually shows that the described counterexamples are impossible. Checking that a few conforming cases work is not enough.[^s1][^s2]

**Pitfalls.** Students in the 2020 case study sometimes overgeneralized their scepticism. Some doubted any argument about infinitely many cases, and others struggled to see that a variable can stand for every case.[^s2] The method can also be misapplied. In the 2016 case, a student first mislabeled a contrapositive argument as a converse and rejected it, before redoing the counterexample description and changing her verdict.[^s3]

## Evidence

The evidence so far comes from small, single-site case studies in one U.S. charter school, without control groups. In the 2020 critique study, 9 of 10 interviewed Grade 8 students used the framework in some way, but students with lower prior achievement more often met obstacles.[^s2] In the 2020 contrapositive unit (15 students), the number of students who made converse errors on a proof item fell from nine to five. More students could also critique indirect arguments. However, the same test was given before and after, the rubrics were the author's own, and gains were concentrated among stronger students.[^s1] The method's logical basis is standard, but its effectiveness as a teaching technique still awaits controlled trials.[^s1][^s2]

## Connections

- **Detects commutation of conditionals.** A conditional and its converse do not share counterexamples, so describing both sets shows that reversing the claim is not a valid step.[^s3]
- **Counteracts commutation of conditionals (weak evidence).** Converse errors fell after the 17-day unit, but the design cannot attribute the drop to the method alone.[^s1]
- **Explained by mental-model theory.** ECE treats a conditional as true when no possibility of p with not-q survives, following Johnson-Laird.[^s2][^s3]
- **Introduced by David Yopp** in his 2016 report on contrapositive proving.[^s3]
- **Applied in mathematics education**, as part of a Grade 8 argumentation curriculum.[^s2]
- **Related techniques.** The method of counterexample refutes an argument *form* by finding a parallel instance. ECE instead describes the counterexample set of a single general claim. A partial truth table can show in one row that two sentences are not equivalent.[^s4]

## Sources

[^s1]: Yopp, "Eliminating counterexamples: An intervention for improving adolescents' contrapositive reasoning", *Journal of Mathematical Behavior* 59, 2020. https://www.cadrek12.org/sites/default/files/Yopp%202020%20JMB.pdf (accessed 2026-11-16)
[^s2]: Yopp, Ely, Adams, Nielsen & Corwine, "Eliminating counterexamples: A case study intervention for improving adolescents' ability to critique direct arguments", *Journal of Mathematical Behavior* 57, 2020. https://cadrek12.org/sites/default/files/Yopp%20et%20al%202020%20JMB.pdf (accessed 2026-11-16)
[^s3]: Yopp, "Eliminating Counterexamples: A Conception of Contrapositive Proving for Adolescents", NCTM Research Conference brief report, 2016. https://nctm.confex.com/nctm/2016RP/webprogram/Manuscript/Session42104/NCTM%20eliminate%20CEs%20paper.3.10.16.uploaded.pdf (accessed 2026-11-16)
[^s4]: Magnus, Button et al., "Partial truth tables", *forall x: Calgary*, ch. 15. https://forallx.openlogicproject.org/html/Ch15.html (accessed 2026-11-16)
