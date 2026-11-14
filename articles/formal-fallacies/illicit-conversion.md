---
id: ct:illicit-conversion
type: FormalFallacy
title: Illicit conversion
aliases: [fallacy of illicit conversion, simple conversion of A or O, invalid conversion]
domain: formal-fallacies
summary: >-
  The formal fallacy of swapping the subject and predicate of a universal
  affirmative (A) or particular negative (O) categorical proposition and
  treating the converse as following, as in inferring "all P are S" from
  "all S are P".
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:categorical-proposition, ct:square-of-opposition, ct:existential-import, ct:contraposition, ct:illicit-minor, ct:illicit-major, ct:method-of-counterexample, ct:prior-analytics, ct:aristotle]
requires: [ct:categorical-proposition, ct:distribution-of-terms, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:conversion, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:distribution-of-terms, source: s4, confidence: high}
  - {predicate: contrastsWith, object: ct:affirming-the-consequent, source: s4, confidence: high}
  - {predicate: studiedIn, object: ct:psychology-of-reasoning, source: s6, confidence: high}
criticalQuestions:
  - Is the original statement an "All" statement or a "Some ... are not" statement? If so, does the swapped version actually follow?
  - Does the predicate class contain members that lie outside the subject class?
  - Can you name one case where the original statement is true and the swapped one is false?
  - If only a weaker claim follows, is "some P are S" enough for the argument's purpose?
argumentMap:
  premises:
    - "All of our certified suppliers passed the safety audit."
  conclusion: "So every supplier that passed the safety audit is one of our certified suppliers."
  verdict: invalid
  scheme: ct:conversion
  objections:
    - "The premise puts certified suppliers inside the group that passed; it says nothing about suppliers that passed but never applied for certification."
    - "An uncertified local supplier could pass the same audit while the premise stays true and the conclusion is false."
sources:
  - id: s1
    title: "4.4 Conversion, Obversion, & Contraposition"
    publisher: "PHIL 1440 course notes, University of Colorado Boulder"
    url: https://rintintin.colorado.edu/~vancecd/phil1440/conversion.pdf
    type: academic
    accessed: 2026-11-14
  - id: s2
    title: "Further Immediate Inferences"
    publisher: "Philosophy 103: Introduction to Logic, Lander University"
    url: https://philosophy.lander.edu/logic/further.html
    type: academic
    accessed: 2026-11-14
  - id: s3
    title: "Aristotle's Logic"
    publisher: "Stanford Encyclopedia of Philosophy (Smith, Winter 2001 archive)"
    url: https://plato.stanford.edu/archives/win2001/entries/aristotle-logic/
    type: scholarly-encyclopedia
    accessed: 2026-11-14
  - id: s4
    title: "Logic, Deductive and Inductive, Chapter 24: Formal Fallacies"
    publisher: "Carveth Read (1914), Lit2Go, University of South Florida"
    url: https://etc.usf.edu/lit2go/37/logic-deductive-and-inductive/479/chapter-24/
    type: textbook
    accessed: 2026-11-14
  - id: s5
    title: "On Sophistical Refutations (trans. W. A. Pickard-Cambridge)"
    publisher: "Aristotle, The Internet Classics Archive, MIT"
    url: https://classics.mit.edu/Aristotle/sophist_refut.1.1.html
    type: primary
    accessed: 2026-11-14
  - id: s6
    title: "Theories of the Syllogism: A Meta-Analysis"
    publisher: "Psychological Bulletin 138(3), 427-457 (Khemlani & Johnson-Laird, 2012), authors' copy"
    url: https://modeltheory.org/papers/ssk/ssk2012syllogisms-meta-analysis.pdf
    type: peer-reviewed
    accessed: 2026-11-14
created: 2026-11-14
---

# Illicit conversion

Illicit conversion is the formal fallacy of swapping the subject and predicate of a categorical proposition when the swap does not preserve truth. Conversion means interchanging the two terms, so that "All S are P" becomes "All P are S".[^s1][^s2] For E statements ("No S are P") and I statements ("Some S are P") the converse always has the same truth value as the original. For A statements ("All S are P") and O statements ("Some S are not P") it does not, and treating the converse as guaranteed is the fallacy of illicit conversion.[^s1][^s2] "All dogs are mammals" is true; "all mammals are dogs" is not.[^s1]

## Origin

Aristotle set out the rules in *Prior Analytics* I.2: universal negatives and particular affirmatives convert, and a universal affirmative yields only the particular "some B are A". He used these conversions as steps when reducing syllogisms in the second and third figures to the first.[^s3] In *On Sophistical Refutations* he diagnosed a closely related error: people assume that because one thing follows from another, the relation runs both ways. His examples are mistaking yellow bile for honey because honey is yellow, and inferring rain from wet ground.[^s5] Carveth Read's 1914 textbook lists simple conversion of A and O among the formal fallacies of deduction, with the examples "All money is wealth, so all wealth is money" and "Some wealth is not money, so some money is not wealth".[^s4]

## How it works

The diagnosis rests on distribution. E and I statements have a symmetrical distribution status: both terms are distributed in an E statement and neither in an I statement, so swapping them changes nothing.[^s2] An A statement distributes its subject but not its predicate, and an O statement distributes its predicate but not its subject. Converting either one moves an undistributed term into a position where it is distributed, so the converse claims something about a whole class that the original spoke about only in part.[^s4] Read frames this, like the other formal fallacies, as going beyond the evidence.[^s4]

The argument map above shows a workplace version. Knowing that every certified supplier passed the audit places the certified suppliers inside the group that passed. It does not exclude suppliers that passed without being certified, so the conclusion that every passing supplier is certified does not follow.[^s1][^s2] The O case is similar: from "some applicants are not engineers" it does not follow that some engineers are not applicants, since every engineer might have applied.[^s1][^s2]

Aristotle's valid alternative for the A form, now called conversion by limitation, is to conclude only "some P are S". On the modern Boolean reading, which does not assume the subject class has members, even that step is suspect, and the SEP entry notes that modern readers often regard it with suspicion for this reason.[^s3]

## How to spot it

Look for an inference that keeps the quantity and quality of a statement but reverses its terms. If the starting point is an "All" statement or a "Some ... are not" statement, the swap is unsupported.[^s1][^s2] Everyday signals include "all X are Y, so anything that's Y is X" and "being X means being Y, so if it's Y it must be X". The conditional version, from "if trade is free it prospers" to "if trade prospers it is free", is the same move on a hypothetical statement, and Read classes it alongside A conversion.[^s4]

## How to counter it

Ask whether the predicate class has members outside the subject class, and name one. A single uncertified supplier that passed the audit keeps the premise true and the conclusion false, which shows the inference is invalid.[^s1][^s2] Then state what does follow. From an A statement, on the traditional reading, the most that follows is the particular converse; from an O statement, no converse follows at all.[^s2][^s3] If the arguer really needs the reversed claim, it requires its own evidence.

## Evidence on how often people commit it

Psychologists have studied illicit conversion as a source of errors in syllogistic reasoning since Chapman and Chapman's 1959 proposal that reasoners take a premise and its converse to be equivalent. A 2012 meta-analysis by Khemlani and Johnson-Laird reports that people do make illicit conversions on single-premise inferences, especially with abstract terms: about a third of participants accepted "All A are B, therefore all B are A", and more accepted the O version.[^s6] Across six syllogism data sets, a conversion-based theory correctly predicted 83% of responses overall, second of seven theories tested, but only 44% of the responses that people actually gave.[^s6] The authors note that widespread conversion would erase the figural effect, a robust bias toward conclusions that keep the order of terms in the premises, so conversion explains part of syllogistic error rather than all of it.[^s6]

## Connections

- **Invalid form of conversion.** Conversion is a valid immediate inference for E and I statements; illicit conversion applies the same swap to A and O statements, where it no longer preserves truth.[^s1][^s2]
- **Explained by the distribution of terms.** The converse of an A or O statement distributes a term that the original left undistributed, which is why it outruns the evidence.[^s2][^s4]
- **Contrasts with affirming the consequent.** Both reverse a one-way relation. Read treats converting "if A then B" to "if B then A" as the hypothetical analogue of A conversion, and Aristotle's examples of the consequent fallacy rest on the same assumption that consequence runs both ways. Illicit conversion concerns categorical statements, while affirming the consequent concerns conditionals.[^s4][^s5]
- **Studied in the psychology of reasoning.** Conversion of premises is one of the standard hypotheses for why people endorse invalid syllogisms, tested against other theories in the 2012 meta-analysis.[^s6]

## Sources

[^s1]: "4.4 Conversion, Obversion, & Contraposition", PHIL 1440 course notes, University of Colorado Boulder. https://rintintin.colorado.edu/~vancecd/phil1440/conversion.pdf (accessed 2026-11-14)
[^s2]: "Further Immediate Inferences", Philosophy 103: Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/further.html (accessed 2026-11-14)
[^s3]: Robin Smith, "Aristotle's Logic", Stanford Encyclopedia of Philosophy (Winter 2001 archive). https://plato.stanford.edu/archives/win2001/entries/aristotle-logic/ (accessed 2026-11-14)
[^s4]: Carveth Read, *Logic, Deductive and Inductive* (1914), Chapter 24, Lit2Go, University of South Florida. https://etc.usf.edu/lit2go/37/logic-deductive-and-inductive/479/chapter-24/ (accessed 2026-11-14)
[^s5]: Aristotle, *On Sophistical Refutations*, trans. W. A. Pickard-Cambridge, The Internet Classics Archive, MIT. https://classics.mit.edu/Aristotle/sophist_refut.1.1.html (accessed 2026-11-14)
[^s6]: S. Khemlani and P. N. Johnson-Laird, "Theories of the Syllogism: A Meta-Analysis", *Psychological Bulletin* 138(3), 427-457 (2012). https://modeltheory.org/papers/ssk/ssk2012syllogisms-meta-analysis.pdf (accessed 2026-11-14)
