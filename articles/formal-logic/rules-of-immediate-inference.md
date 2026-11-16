---
id: ct:rules-of-immediate-inference
type: Technique
title: Rules of immediate inference
aliases: [immediate-inference rules, conversion obversion and contraposition rules, table of immediate inferences]
domain: formal-logic
summary: >-
  A checklist for one-premise inferences between categorical statements:
  conversion is valid for E and I, contraposition for A and O, obversion for
  all four forms, and the "by limitation" variants only when the subject class
  is non-empty. Any move outside the table, or one that distributes a term the
  premise left undistributed, is invalid.
level: introductory
evidenceStatus: normative
broader: [ct:immediate-inference]
related: [ct:illicit-contraposition, ct:illicit-conversion, ct:conversion, ct:obversion, ct:contraposition, ct:square-of-opposition, ct:existential-import, ct:venn-diagram-test, ct:rules-of-the-categorical-syllogism, ct:method-of-counterexample, ct:euler-diagram]
requires: [ct:categorical-proposition, ct:distribution-of-terms]
relations:
  - {predicate: detects, object: ct:illicit-contraposition, source: s1, confidence: high}
  - {predicate: detects, object: ct:illicit-conversion, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:distribution-of-terms, source: s2, confidence: high}
  - {predicate: influencedBy, object: ct:aristotle, source: s6, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Lecture notes 5.3: Conversion, obversion and contraposition"
    publisher: "PHIL 240 Introduction to Logic, Texas A&M University"
    url: https://phil240.tamu.edu/LectureNotes/5.3.pdf
    type: academic
    accessed: 2026-11-16
  - id: s2
    title: "Immediate Inference"
    publisher: "Bryan Wiebe, critical thinking course notes (stmcollege.ca)"
    url: https://bryan.stmcollege.ca/Immediate.html
    type: academic
    accessed: 2026-11-16
  - id: s3
    title: "Syllogistic Logic"
    publisher: "C. Byrne, Department of Philosophy, St. Francis Xavier University"
    url: https://people.stfx.ca/cbyrne/Byrne/SyllogisticLogic.pdf
    type: academic
    accessed: 2026-11-16
  - id: s4
    title: "Philosophy 103: Introduction to Logic (immediate inferences)"
    publisher: "PHIL 103 Introduction to Logic, Lander University"
    url: https://philosophy.lander.edu/logic/further.html
    type: academic
    accessed: 2026-11-16
  - id: s5
    title: "Week 3A: Immediate inference (Chapter 5, cont.)"
    publisher: "Logic course handout after Copi and Cohen, DePaul University"
    url: https://condor.depaul.edu/mlarrabe/wk3a.htm
    type: academic
    accessed: 2026-11-16
  - id: s6
    title: "The Traditional Square of Opposition"
    publisher: "Stanford Encyclopedia of Philosophy (Terence Parsons, Spring 2005 archive)"
    url: https://plato.stanford.edu/archives/spr2005/entries/square/
    type: scholarly-encyclopedia
    accessed: 2026-11-16
  - id: s7
    title: "Deductive Logic, Part III, Chapter VI: Of compound forms of immediate inference"
    publisher: "George W. J. Stock (1888), Lit2Go, University of South Florida"
    url: https://etc.usf.edu/lit2go/189/deductive-logic/3910/part-3-chapter-6/
    type: textbook
    accessed: 2026-11-16
created: 2026-11-16
---

# Rules of immediate inference

An immediate inference draws a conclusion from a single categorical premise, with no middle term.[^s1] The rules of immediate inference are the short table that says which of the three standard moves preserves truth for which statement form. Conversion (swap subject and predicate) is valid for universal negatives (E, "No S are P") and particular affirmatives (I, "Some S are P"). Contraposition (swap the terms and replace each with its complement) is valid for universal affirmatives (A, "All S are P") and particular negatives (O, "Some S are not P"). Obversion (flip the quality and replace the predicate with its complement) is valid for all four.[^s1][^s4][^s5] A Texas A&M lecture offers a mnemonic: the vowels inside the names, convErsIon and contrApOsition, mark the forms each rule fits.[^s1]

## Origin

Aristotle's *Prior Analytics* I.2 already holds that E and I statements convert simply, and that claim became part of the traditional doctrine of the square of opposition.[^s6] Terence Parsons' SEP entry reports that contraposition and obversion were worked out later: twelfth- and thirteenth-century logicians, including Peter of Spain, endorsed contraposition for A and O, while Buridan in the fourteenth century showed that these rules break down when terms may be empty.[^s6] Victorian textbooks set out the full scheme, including the compound moves; George Stock's 1888 *Deductive Logic*, for example, contraposes A and O directly, allows E only by limitation and says I cannot be contraposed at all.[^s7] Modern course texts after Copi and Cohen present the same table and separate the moves that yield logical equivalents from the "by limitation" moves that are valid but weaker.[^s5]

## How it works

Each rule follows from the distribution of terms. A distributes only its subject, E both terms, I neither, and O only its predicate. A move is illegitimate when its conclusion says something about every member of a class that the premise left undistributed.[^s2] Converting "All S are P" fails for this reason: P is undistributed in the premise but becomes a distributed subject in "All P are S".[^s2][^s3] Contraposition is obversion, then conversion, then obversion again, so it inherits the limits of conversion. For A and O the middle step converts an E or I statement and is safe; for E and I the middle step would convert an A or O statement and fails.[^s2][^s3][^s4]

Take a workplace rule: "No contractors are on the payroll" (E). The table licenses its converse, "No payroll staff are contractors", and its obverse, "All contractors are non-payroll people".[^s1][^s5] It does not license the contrapositive, "No non-payroll people are non-contractors", because agency temps or visiting auditors can be neither. That is illicit contraposition.[^s1][^s2] What the table does allow from an E premise is contraposition by limitation: "Some non-payroll people are not non-contractors", provided some contractors exist.[^s5][^s7]

## How to apply it

1. Put the premise into standard form and label it A, E, I or O.[^s1]
2. Identify the move: terms swapped (conversion), quality flipped with a complemented predicate (obversion), or both terms swapped and complemented (contraposition). Form complements with "non-" rather than prefixes such as "in-" or "un-", which can mislead ("inflammable" is not the complement of "flammable").[^s4]
3. Check the move against the table. If it falls outside it, the conclusion's truth is undetermined by the premise and the inference is invalid.[^s1][^s4]
4. Confirm with distribution: no term may be distributed in the conclusion unless it was distributed in the premise.[^s2]
5. If a weaker claim will do, use the limited form (A to I by conversion, E to O by contraposition) and state the assumption that the subject class is non-empty.[^s5][^s7]

Wiebe's course notes add a caution: a converse can look true for reasons that have nothing to do with logic, so test a suspect move with a parallel example of the same form whose conclusion is plainly false.[^s2] A Lander University course page likewise advises learning the general rules rather than memorising truth-value tables.[^s4]

## Limitations

The table assumes term complements are well defined and that classes are non-empty. Parsons reports that Buridan's chimera and non-being examples break contraposition and obversion when terms can be empty, that medieval writers patched this with an extra non-emptiness premise, and that nineteenth-century texts combined all the rules consistently only by tacitly excluding empty and universal terms.[^s6] Under the modern Boolean reading, the "by limitation" inferences lapse, so textbooks differ on which entries to include.[^s5][^s6] The table checks single-premise moves only; syllogisms need their own rules or a Venn diagram.[^s3]

## Connections

- **Detects illicit contraposition.** The table marks contraposition of E and I statements as undetermined, so any argument that contraposes them is flagged at step 3.[^s1][^s2]
- **Detects illicit conversion.** Converting A or O statements is not licensed; the distribution check shows why the converse of an A statement overreaches.[^s2][^s3]
- **Explained by distribution of terms.** The pattern of valid and invalid moves follows from which terms each form distributes.[^s2]
- **Influenced by Aristotle.** The simple conversion of E and I statements, the core of the table, comes from *Prior Analytics* I.2.[^s6]

## Sources

[^s1]: "Conversion, obversion and contraposition", PHIL 240 lecture notes 5.3, Texas A&M University. https://phil240.tamu.edu/LectureNotes/5.3.pdf (accessed 2026-11-16)
[^s2]: Bryan Wiebe, "Immediate Inference", critical thinking course notes. https://bryan.stmcollege.ca/Immediate.html (accessed 2026-11-16)
[^s3]: C. Byrne, "Syllogistic Logic", Department of Philosophy, St. Francis Xavier University. https://people.stfx.ca/cbyrne/Byrne/SyllogisticLogic.pdf (accessed 2026-11-16)
[^s4]: "Philosophy 103: Introduction to Logic" course page, Lander University. https://philosophy.lander.edu/logic/further.html (accessed 2026-11-16)
[^s5]: "Week 3A: Immediate inference", logic course handout after Copi and Cohen, DePaul University. https://condor.depaul.edu/mlarrabe/wk3a.htm (accessed 2026-11-16)
[^s6]: Terence Parsons, "The Traditional Square of Opposition", Stanford Encyclopedia of Philosophy (Spring 2005 archive). https://plato.stanford.edu/archives/spr2005/entries/square/ (accessed 2026-11-16)
[^s7]: George W. J. Stock, *Deductive Logic* (1888), Part III, Chapter VI, Lit2Go, University of South Florida. https://etc.usf.edu/lit2go/189/deductive-logic/3910/part-3-chapter-6/ (accessed 2026-11-16)
