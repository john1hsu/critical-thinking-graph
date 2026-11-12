---
id: ct:illicit-minor
type: FormalFallacy
title: Illicit minor
aliases: [illicit process of the minor term, illicit process of the minor]
domain: formal-fallacies
summary: >-
  The syllogistic fallacy committed when the minor term (the subject of the
  conclusion) is distributed in the conclusion but undistributed in the minor
  premise, so the conclusion generalizes about a whole class that the premises
  covered only in part.
level: intermediate
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:syllogism, ct:illicit-major, ct:undistributed-middle, ct:rules-of-the-categorical-syllogism, ct:venn-diagram-test, ct:method-of-counterexample, ct:port-royal-logic]
requires: [ct:categorical-syllogism, ct:distribution-of-terms, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:categorical-syllogism, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:distribution-of-terms, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:illicit-major, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:hasty-generalization, source: s1, confidence: medium}
criticalQuestions:
  - Does the conclusion make a claim about every member of its subject class?
  - In the premise where that subject term appears, is it only the predicate of an affirmative statement?
  - Could some members of the conclusion's subject class lie outside the group the premises actually describe?
  - Would a weaker "some" conclusion be all the premises can support?
argumentMap:
  premises:
    - "All members of the incident-response team are certified in first aid."
    - "All members of the incident-response team are full-time staff."
  conclusion: "All full-time staff are certified in first aid."
  verdict: invalid
  scheme: ct:categorical-syllogism
  objections:
    - "The second premise places the team inside the full-time staff; it says nothing about full-time staff who are not on the team."
    - "A full-time accountant who never joined the team could lack the certificate while both premises stay true."
sources:
  - id: s1
    title: "Syllogistic Fallacies: Illicit Major and Illicit Minor"
    publisher: "Philosophy 103: Introduction to Logic, Lander University"
    url: https://philosophy.lander.edu/logic/illicit_fall.html
    type: academic
    accessed: 2026-11-12
  - id: s2
    title: "6.5 Rules for Evaluating Syllogisms"
    publisher: "PHIL 240 lecture notes, Texas A&M University"
    url: https://phil240.tamu.edu/LectureNotes/6.5.pdf
    type: academic
    accessed: 2026-11-12
  - id: s3
    title: "Logic, Deductive and Inductive, Chapter 24: Formal Fallacies"
    publisher: "Carveth Read (1914), Lit2Go, University of South Florida"
    url: https://etc.usf.edu/lit2go/37/logic-deductive-and-inductive/479/chapter-24/
    type: textbook
    accessed: 2026-11-12
  - id: s4
    title: "The Port Royal Logic"
    publisher: "Internet Encyclopedia of Philosophy"
    url: https://iep.utm.edu/portroyl/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
  - id: s5
    title: "Distributive Terms, Truth, and the Port Royal Logic"
    publisher: "History and Philosophy of Logic (Martin, 2012), author's copy"
    url: https://homepages.uc.edu/~martinj/Papers/Distributive%20Terms,%20Truth%20and%20The%20Port%20Royal%20Logic%20-%20HPL%20(web%20version).pdf
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Illicit minor

The illicit minor, also called the illicit process of the minor term, is a formal fallacy of the categorical syllogism. The minor term is the subject of the conclusion, and the fallacy occurs when that term is distributed in the conclusion while it is undistributed in the minor premise, the premise where it appears.[^s1][^s2] Because a distributed term speaks about every member of its class, the conclusion ends up making a claim about a whole group when the evidence concerned only part of it. The reverse case, a term distributed in the premise but not in the conclusion, is harmless and is not this fallacy.[^s1]

## Origin

Carveth Read's 1914 textbook lists the error among the formal fallacies of deduction as distributing in the conclusion a term that the premises left undistributed, and treats it as one case of a single principle: an inference must not outrun its evidence.[^s3] The rule it breaks is older. Its source is the pair of "process rules" about distribution, which appear in sixteenth-century logic texts such as Toletus's 1580 commentary on the *Posterior Analytics*, and were then grouped with four older syllogistic rules by Eustace of St. Paul in 1609.[^s5] The Port-Royal *Logic* of Antoine Arnauld and Pierre Nicole (1662) gave the set its best-known form; its second rule says that the terms of the conclusion may not be taken more universally there than in the premises.[^s4][^s5]

## How it works

Distribution follows the form of each statement. An A statement ("All S are P") distributes only its subject; an E statement ("No S are P") distributes both terms; an I statement ("Some S are P") distributes neither; and an O statement ("Some S are not P") distributes only its predicate.[^s2][^s4] A universal conclusion (A or E) always distributes the minor term, because it is the subject. So the fallacy appears whenever such a conclusion rests on a minor premise in which the minor term is only the predicate of an affirmative statement or the subject of a particular one.[^s1][^s2]

The argument map above is a common workplace version. The second premise tells us that every team member is a full-time employee. It does not tell us that every full-time employee is on the team, so "full-time staff" is undistributed there. The conclusion, however, is about all full-time staff. Nothing in the premises reaches the full-time employees outside the team, and an accountant who never joined it could lack the certificate while both premises remain true.[^s1][^s2] A textbook case has the same structure: all politicians are prevaricators, all politicians are wealthy, so all wealthy people are prevaricators.[^s2]

Read points out why the error can survive scrutiny. In his example (all men are two-handed; all two-handed animals are cooking animals; so all cooking animals are men) the conclusion happens to be true, and a reader who agrees with it may not notice that the form is invalid.[^s3] Validity depends on form, not on whether the conclusion is believable.

## How to spot it

Find the conclusion and take its subject: that is the minor term. If the conclusion begins with "All" or "No", the term is distributed. Then go to the premise that contains it. If it sits as the predicate of an "All" or "Some ... are" statement, or as the subject of a "Some" statement, it is undistributed there, and the syllogism commits the illicit minor.[^s1][^s2] The examples above all have the same shape: the middle term is the subject of both premises (the third figure), so the minor term is the predicate of an affirmative minor premise and cannot be distributed there.[^s1][^s2] A Venn diagram of the premises gives an independent check: it will leave room for a member of the minor class that the conclusion's claim does not cover.[^s1]

## How to counter it

Ask about the members of the conclusion's subject class that the premises do not mention, and produce one. A single case that keeps both premises true and makes the conclusion false shows the form is invalid.[^s1][^s3] Then offer the conclusion the premises can bear. In the example, the most that follows, provided the team has any members, is that some full-time staff are certified, since the evidence covers only the team.[^s1] If the arguer really believes the universal claim, it needs a different premise, one that speaks about every full-time employee.

## Connections

- **Invalid form of the categorical syllogism.** It breaks the rule that a term distributed in the conclusion must also be distributed in its premise, which every valid standard-form syllogism obeys.[^s2]
- **Explained by the distribution of terms.** The fallacy is defined by distribution: the conclusion takes the minor term universally although the minor premise used it only in part. The process rule that forbids this goes back to sixteenth-century logic and the Port-Royal *Logic*.[^s1][^s4][^s5]
- **Contrasts with the illicit major.** Both break the same distribution rule and both reason from part of a class to the whole. The illicit major overextends the conclusion's predicate, while the illicit minor overextends its subject.[^s1]
- **Contrasts with hasty generalization.** The Lander notes liken the illicit minor's move from part of a class to the whole to converse accident, the informal error of generalizing from a few cases. The difference is that the illicit minor is a fault of form, detectable without knowing anything about the subject matter.[^s1][^s3]

## Sources

[^s1]: "Syllogistic Fallacies: Illicit Major and Illicit Minor", Philosophy 103: Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/illicit_fall.html (accessed 2026-11-12)
[^s2]: "6.5 Rules for Evaluating Syllogisms", PHIL 240 lecture notes, Texas A&M University. https://phil240.tamu.edu/LectureNotes/6.5.pdf (accessed 2026-11-12)
[^s3]: Carveth Read, *Logic, Deductive and Inductive* (1914), Chapter 24, Lit2Go, University of South Florida. https://etc.usf.edu/lit2go/37/logic-deductive-and-inductive/479/chapter-24/ (accessed 2026-11-12)
[^s4]: "The Port Royal Logic", Internet Encyclopedia of Philosophy. https://iep.utm.edu/portroyl/ (accessed 2026-11-12)
[^s5]: J. N. Martin, "Distributive Terms, Truth, and the Port Royal Logic", *History and Philosophy of Logic* (2012). https://homepages.uc.edu/~martinj/Papers/Distributive%20Terms,%20Truth%20and%20The%20Port%20Royal%20Logic%20-%20HPL%20(web%20version).pdf (accessed 2026-11-12)
