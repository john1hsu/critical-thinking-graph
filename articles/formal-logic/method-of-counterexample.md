---
id: ct:method-of-counterexample
type: Technique
title: Method of counterexample
aliases: [counterexample method, refutation by counterexample, refutation by logical analogy]
domain: formal-logic
summary: >-
  A test for invalidity: to show that an argument form does not guarantee its
  conclusion, describe a case or substitution instance of the same form in
  which every premise is true and the conclusion is false.
level: introductory
evidenceStatus: normative
broader: [ct:deductive-reasoning]
related: [ct:validity, ct:truth-table, ct:modus-ponens, ct:consider-the-opposite]
requires: [ct:validity]
relations:
  - {predicate: detects, object: ct:affirming-the-consequent, source: s3, confidence: high}
  - {predicate: detects, object: ct:denying-the-antecedent, source: s3, confidence: high}
  - {predicate: counteracts, object: ct:affirming-the-consequent, source: s4, confidence: medium}
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: medium}
  - {predicate: introducedIn, object: ct:prior-analytics, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Aristotle's Logic"
    publisher: Stanford Encyclopedia of Philosophy (Robin Smith, rev. 2022)
    url: https://plato.stanford.edu/entries/aristotle-logic/
    type: scholarly-encyclopedia
    accessed: 2026-11-03
  - id: s2
    title: "2.4.02: Invalidity and Counter Examples"
    publisher: "A Modern Formal Logic Primer (Teller), LibreTexts"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/A_Modern_Formal_Logic_Primer_(Teller)/02%3A_Volume_I-_Sentence_Logic/2.04%3A_Validity_and_Conditionals/2.4.02%3A_Invalidity_and_Counter_Examples
    type: textbook
    accessed: 2026-11-03
  - id: s3
    title: "1.3 Counterexamples and Invalidity (lecture notes)"
    publisher: Texas A&M University, PHIL 240 Introduction to Logic
    url: https://phil240.tamu.edu/LectureNotes/1.3.pdf
    type: academic
    accessed: 2026-11-03
  - id: s4
    title: "Inference suppression and semantic memory retrieval: Every counterexample counts"
    publisher: Memory & Cognition 31, 581-595 (De Neys, Schaeken & d'Ydewalle, 2003)
    url: https://link.springer.com/article/10.3758/BF03196099
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s5
    title: "Conditional reasoning and causation"
    publisher: Memory & Cognition 19(3), 274-282 (Cummins, Lubart, Alksnis & Rist, 1991), MEDLINE record
    url: https://busqueda.bvsalud.org/portal/resource/es/mdl-1861613
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s6
    title: "The Asymmetry Thesis and the Diversity of 'Invalid' Argument-Forms"
    publisher: Informal Logic 19(1), 67-76 (George Bowles, 1999)
    url: https://distantreader.org/stacks/journals/il/il-2316.pdf
    type: peer-reviewed
    accessed: 2026-11-03
created: 2026-11-03
---

# Method of counterexample

The method of counterexample is the standard way to show that an argument is not deductively valid. A valid argument is one with no counterexample: there is no possible case in which all its premises are true and its conclusion false. So producing a single such case is enough to prove invalidity.[^s2] In formal logic a counterexample is an assignment of truth values that makes the premises true and the conclusion false; in everyday reasoning it is usually a parallel argument of the same form whose premises are obviously true and whose conclusion is obviously false.[^s2][^s3]

## Origin

The technique is as old as formal logic. In the *Prior Analytics*, Aristotle showed that certain pairs of premises yield no syllogism by supplying concrete terms that make the premises true while the rival conclusions come out false, which is the same logic behind modern invalidity proofs.[^s1] He often did this economically with two triplets of terms, one making a universal affirmative conclusion true and the other a universal negative one, which together rule out every candidate conclusion.[^s1] Modern sentence logic restates the idea precisely: a truth table lists every case, and any row with true premises and a false conclusion is a counterexample.[^s2]

## How it works

Take a workplace argument: "If the vendor is reliable, the delivery arrives on time. The delivery arrived on time. So the vendor is reliable." Its form is "If A then B; B; so A." To test the form, keep it fixed and swap in content where the conclusion is plainly false and the premises plainly true: "If Paris is in Germany, Paris is in Europe. Paris is in Europe. So Paris is in Germany." The premises are true and the conclusion false, so the form is invalid, and the vendor argument cannot rely on its form alone.[^s3] This is how the method exposes affirming the consequent and denying the antecedent, the invalid look-alikes of modus ponens and modus tollens.[^s3]

## How to apply it

Course notes on the method give a five-step routine:[^s3]

1. Lay out the argument as numbered premises and a conclusion, then write its most logically sensitive form, using capital letters for statements or terms.[^s3]
2. Substitute content into the conclusion so that it becomes a well-known falsehood.[^s3]
3. Apply the same substitutions everywhere the letters occur.[^s3]
4. Fill any remaining letters so that each premise is a well-known truth.[^s3]
5. Check the result. If it works, the original argument is formally invalid.[^s3]

In sentence logic the search can be made systematic by checking every row of a truth table for a case with true premises and a false conclusion.[^s2] Outside formal settings, the informal version is to ask whether the premises could all hold while the conclusion fails, and to describe that situation concretely.[^s3]

**Pitfalls.** Failing to find a counterexample does not prove validity; the reasoner may just not have found one.[^s3] Counterexamples only persuade when the truth values of the substituted premises and conclusion are obvious to the audience.[^s3] And because an argument can instantiate an invalid form while being valid in virtue of a finer-grained form, showing a form invalid does not by itself show every instance invalid. Massey's asymmetry thesis made this point, though Bowles argued in 1999 that many forms do make their standard instances invalid.[^s6]

## Evidence

Psychologists have tested whether ordinary reasoners use something like this method when judging conditionals. Cummins and colleagues (1991) found that people accept conditional conclusions less often when the causal conditional has many alternative causes or disabling conditions.[^s5] De Neys, Schaeken and d'Ydewalle (2003) measured how many counterexamples each participant could retrieve and found that acceptance of affirming the consequent fell steadily as the number of retrieved alternative causes rose, with each extra counterexample adding to the effect. Results for denying the antecedent and modus tollens were less clear.[^s4] These studies use everyday causal content, so they show that bringing counterexamples to mind suppresses the fallacy, not that formal training in the method does.[^s4][^s5]

## Connections

- **Detects affirming the consequent and denying the antecedent.** A substitution instance with true premises and a false conclusion shows each of these forms invalid.[^s3]
- **Counteracts affirming the consequent.** Retrieving alternative causes, which are counterexamples to the conditional's converse, lowers acceptance of the fallacious inference.[^s4]
- **Introduced by Aristotle in the *Prior Analytics*.** He disproved inconclusive premise pairs with counterexample terms.[^s1]
- **Related to truth tables and validity.** Validity is defined as the absence of counterexamples, and a truth table is an exhaustive search for one.[^s2]

## Sources

[^s1]: Smith, "Aristotle's Logic", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/aristotle-logic/ (accessed 2026-11-03)
[^s2]: Teller, "Invalidity and Counter Examples", *A Modern Formal Logic Primer*, LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/A_Modern_Formal_Logic_Primer_(Teller)/02%3A_Volume_I-_Sentence_Logic/2.04%3A_Validity_and_Conditionals/2.4.02%3A_Invalidity_and_Counter_Examples (accessed 2026-11-03)
[^s3]: "1.3 Counterexamples and Invalidity", PHIL 240 lecture notes, Texas A&M University. https://phil240.tamu.edu/LectureNotes/1.3.pdf (accessed 2026-11-03)
[^s4]: De Neys, Schaeken & d'Ydewalle, "Inference suppression and semantic memory retrieval: Every counterexample counts", *Memory & Cognition* 31, 2003. https://link.springer.com/article/10.3758/BF03196099 (accessed 2026-11-03)
[^s5]: Cummins, Lubart, Alksnis & Rist, "Conditional reasoning and causation", *Memory & Cognition* 19(3), 1991. https://busqueda.bvsalud.org/portal/resource/es/mdl-1861613 (accessed 2026-11-03)
[^s6]: Bowles, "The Asymmetry Thesis and the Diversity of 'Invalid' Argument-Forms", *Informal Logic* 19(1), 1999. https://distantreader.org/stacks/journals/il/il-2316.pdf (accessed 2026-11-03)
