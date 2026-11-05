---
id: ct:illicit-major
type: FormalFallacy
title: Illicit major
aliases: [illicit process of the major term, illicit process of the major]
domain: formal-fallacies
summary: >-
  The syllogistic fallacy committed when the major term (the predicate of the
  conclusion) is distributed in the conclusion but undistributed in the major
  premise, so the conclusion says something about the whole of a class that
  the premises described only in part.
level: intermediate
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:syllogism, ct:undistributed-middle, ct:illicit-minor, ct:method-of-counterexample, ct:venn-diagram-test]
requires: [ct:categorical-syllogism, ct:distribution-of-terms, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:categorical-syllogism, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:distribution-of-terms, source: s4, confidence: high}
  - {predicate: contrastsWith, object: ct:illicit-minor, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:undistributed-middle, source: s3, confidence: medium}
criticalQuestions:
  - Is the conclusion's predicate about all members of its class while the premise spoke only of some of them?
  - Could something outside the subject class still have the property the conclusion denies?
  - Does a Venn diagram of the premises leave room for the conclusion to be false?
argumentMap:
  premises:
    - "All senior engineers have production access."
    - "No contractors are senior engineers."
  conclusion: "No contractors have production access."
  verdict: invalid
  scheme: ct:categorical-syllogism
  objections:
    - "The first premise says senior engineers are among those with access, not that they are the only ones."
    - "A contractor on the on-call rota could have been granted access through another route."
sources:
  - id: s1
    title: "Syllogistic Fallacies: Illicit Major and Illicit Minor"
    publisher: "Philosophy 103: Introduction to Logic, Lander University"
    url: https://philosophy.lander.edu/logic/illicit_fall.html
    type: academic
    accessed: 2026-11-04
  - id: s2
    title: "6.5 Rules for Evaluating Syllogisms"
    publisher: "PHIL 240 lecture notes, Texas A&M University"
    url: https://phil240.tamu.edu/LectureNotes/6.5.pdf
    type: academic
    accessed: 2026-11-04
  - id: s3
    title: "Deductive Logic, Part III, Chapter XI: Of the General Rules of Syllogism"
    publisher: "G. W. J. Stock (1888), Lit2Go, University of South Florida"
    url: https://etc.usf.edu/lit2go/189/deductive-logic/3917/part-3-chapter-11/
    type: textbook
    accessed: 2026-11-04
  - id: s4
    title: "Distributive Terms, Truth, and the Port Royal Logic"
    publisher: "History and Philosophy of Logic (Martin, 2012), author's copy"
    url: https://homepages.uc.edu/~martinj/Papers/Distributive%20Terms,%20Truth%20and%20The%20Port%20Royal%20Logic%20-%20HPL%20(web%20version).pdf
    type: peer-reviewed
    accessed: 2026-11-04
created: 2026-11-04
modified: 2026-11-05
---

# Illicit major

The illicit major is a formal fallacy of the categorical syllogism. It occurs when the major term, the predicate of the conclusion, is distributed in the conclusion but not in the major premise.[^s1][^s2] A term is distributed when a statement speaks of every member of the class it names, and undistributed when it speaks of only some of them.[^s1] An argument that commits the illicit major therefore concludes something about a whole class from premises that described only part of it, and is invalid whatever its subject matter.[^s1][^s2]

## Origin

The error is defined by the doctrine of distribution, which grew out of medieval supposition theory and its rule of thumb that the subject of a universal statement and the predicate of a negative statement are distributed.[^s4] By the sixteenth century, logic texts added two "process" rules to the older syllogistic rules, and the Port Royal *Logic* of Arnauld and Nicole (1662) gave them an influential statement: the terms of the conclusion may not be taken more universally than in the premises.[^s4] Nineteenth-century textbooks named the violation "illicit process of the major" (or of the minor) and described its fault as arguing from part to whole.[^s3]

## How it works

Most textbook rule sets for syllogisms include one rule that applies here: any term distributed in the conclusion must also be distributed in its premise. The illicit major breaks that rule for the major term, and the illicit minor breaks it for the minor term.[^s2] The usual route into the error is a negative conclusion. A negative statement distributes its predicate, while the predicate of an affirmative statement is undistributed, so a negative conclusion with an affirmative major premise is at risk.[^s3]

The argument map above shows a workplace version. "All senior engineers have production access" places senior engineers among the people with access. It says nothing about everyone who has access. The conclusion, "No contractors have production access", is about the whole class of people with access, since it excludes every contractor from it. The premises are compatible with a contractor having been granted access some other way, so the conclusion does not follow.[^s1][^s3] One nineteenth-century example has the same shape: all learned men go mad; John is not a learned man; therefore John will not go mad.[^s3]

## How to spot it

Find the conclusion's predicate. That is the major term. Then check two things. Is it distributed in the conclusion, which happens whenever the conclusion is an E ("No S are P") or O ("Some S are not P") statement? And is it undistributed in the major premise, which happens when it is the predicate of an affirmative premise or the subject of a particular one? If both are true, the syllogism commits the illicit major.[^s1][^s2] A Venn diagram of the premises gives an independent check: if the diagram leaves room for the conclusion to be false, the form is invalid.[^s1] A classroom example of the O-statement version: some animals are not birds; all robins are birds; so some robins are not animals.[^s2]

## How to counter it

Point to what the premise leaves open. The major premise says only that one group belongs to the predicate class, not that it is the only group there. A single case that satisfies the premises and falsifies the conclusion settles the matter, such as a contractor with access in the example above.[^s1][^s3] If the arguer means the stronger claim ("only senior engineers have production access"), ask for it to be stated. The argument then distributes the major term and may be valid, but it rests on a premise that now has to be defended.[^s3]

## Connections

- **Invalid form of the categorical syllogism.** It breaks one of the rules that every valid standard-form categorical syllogism satisfies.[^s2]
- **Explained by the distribution of terms.** The fallacy is defined by the process rules, which forbid taking a term more universally in the conclusion than in the premises. The rules and their semantics go back to medieval logic and the Port Royal *Logic*.[^s4]
- **Contrasts with the illicit minor.** Both break the same distribution rule. The illicit minor overextends the conclusion's subject, while the illicit major overextends its predicate.[^s1]
- **Contrasts with the undistributed middle.** Both are failures of distribution, but the undistributed middle concerns the term that links the premises, which must be distributed at least once. The illicit process concerns the terms that appear in the conclusion.[^s3]

## Sources

[^s1]: "Syllogistic Fallacies: Illicit Major and Illicit Minor", Philosophy 103: Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/illicit_fall.html (accessed 2026-11-04)
[^s2]: "6.5 Rules for Evaluating Syllogisms", PHIL 240 lecture notes, Texas A&M University. https://phil240.tamu.edu/LectureNotes/6.5.pdf (accessed 2026-11-04)
[^s3]: G. W. J. Stock, *Deductive Logic* (1888), Part III, Chapter XI, Lit2Go, University of South Florida. https://etc.usf.edu/lit2go/189/deductive-logic/3917/part-3-chapter-11/ (accessed 2026-11-04)
[^s4]: J. N. Martin, "Distributive Terms, Truth, and the Port Royal Logic", *History and Philosophy of Logic* (2012). https://homepages.uc.edu/~martinj/Papers/Distributive%20Terms,%20Truth%20and%20The%20Port%20Royal%20Logic%20-%20HPL%20(web%20version).pdf (accessed 2026-11-04)
