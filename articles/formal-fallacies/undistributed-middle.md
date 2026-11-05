---
id: ct:undistributed-middle
type: FormalFallacy
title: Undistributed middle
aliases: [fallacy of the undistributed middle, undistributed middle term]
domain: formal-fallacies
summary: >-
  The syllogistic fallacy committed when the middle term, the term shared by
  both premises, is not distributed in either premise, so each premise may be
  about a different part of its class and nothing links the conclusion's two
  terms.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:syllogism, ct:illicit-major, ct:illicit-minor, ct:venn-diagram-test, ct:method-of-counterexample, ct:affirming-the-consequent]
requires: [ct:categorical-syllogism, ct:distribution-of-terms, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:categorical-syllogism, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:distribution-of-terms, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:illicit-major, source: s2, confidence: high}
  - {predicate: exploits, object: ct:belief-bias, source: s4, confidence: medium}
criticalQuestions:
  - Is the shared term ever used to speak about every member of its class, in either premise?
  - Could the two groups in the conclusion each overlap a different part of the shared class?
  - Would I still accept this form if the conclusion were something I believed to be false?
argumentMap:
  premises:
    - "All of our certified suppliers use encrypted file transfer."
    - "The new printing vendor uses encrypted file transfer."
  conclusion: "The new printing vendor is one of our certified suppliers."
  verdict: invalid
  scheme: ct:categorical-syllogism
  objections:
    - "Neither premise is about everyone who uses encrypted file transfer, so the vendor may belong to a part of that group that contains no certified supplier."
    - "Plenty of uncertified firms use encrypted transfer; the shared trait does not establish membership."
sources:
  - id: s1
    title: "Syllogistic Fallacy 2: Fallacy of the Undistributed Middle Term"
    publisher: "Philosophy 103: Introduction to Logic, Lander University"
    url: https://philosophy.lander.Edu/logic/middle_fall.html
    type: academic
    accessed: 2026-11-05
  - id: s2
    title: "Rules of the Categorical Syllogism"
    publisher: "Philosophy 3304: Introduction to Logic, Dallas Baptist University (Naugle)"
    url: https://www3.dbu.edu/Naugle/pdf/2302_handouts/categorical_syllogisms.pdf
    type: academic
    accessed: 2026-11-05
  - id: s3
    title: "Medieval Theories of the Syllogism"
    publisher: Stanford Encyclopedia of Philosophy (Lagerlund, rev. 2026)
    url: https://plato.stanford.edu/entries/medieval-syllogism/
    type: scholarly-encyclopedia
    accessed: 2026-11-05
  - id: s4
    title: "Characterizing belief bias in syllogistic reasoning: A hierarchical Bayesian meta-analysis of ROC data"
    publisher: "Psychonomic Bulletin & Review 25, 2141–2174 (Trippas et al., 2018)"
    url: https://link.springer.com/10.3758/s13423-018-1460-7
    type: peer-reviewed
    accessed: 2026-11-05
created: 2026-11-05
---

# Undistributed middle

The undistributed middle is a formal fallacy of the categorical syllogism. It occurs when the middle term, the term that appears in both premises but not in the conclusion, is undistributed in both premises.[^s1][^s2] A term is distributed when a statement refers to every member of the class it names.[^s1] The rule it breaks is one of the standard rules of syllogism: the middle term must be distributed in at least one premise. An argument that breaks it is invalid whatever its content, even when all of its statements happen to be true.[^s1][^s2]

## Origin

The rule that the middle term must be distributed came out of medieval logic. The fourteenth-century logician John Buridan restated the traditional theory of the syllogism in terms of supposition, a theory of how terms refer, and held that a syllogism is formally acceptable only if its middle term is distributed.[^s3] Buridan also gave the working test still taught today: universal statements distribute their subjects, negative statements distribute their predicates, and no other terms are distributed.[^s3] On that basis he rejected premise pairs such as two particular affirmatives, where the middle is never distributed.[^s3] Later textbook rule sets list the requirement as a basic rule and call its violation the fallacy of the undistributed middle.[^s2]

## How it works

The middle term is the bridge between the two outer terms. Each premise ties one outer term to the middle, and the conclusion claims a link between the outer terms. If neither premise speaks of the whole middle class, the minor term may sit in one part of it and the major term in another, so the premises establish no relation between them.[^s1][^s2] The commonest version puts the middle term in the predicate of two affirmative premises, since the predicate of an affirmative statement is undistributed.[^s2]

The argument map above shows a workplace case. "All of our certified suppliers use encrypted file transfer" says certified suppliers are among the firms that use it, not that every such firm is certified. "The new printing vendor uses encrypted file transfer" places the vendor somewhere in the same large group. Nothing puts the vendor in the certified part, so the conclusion does not follow.[^s2] A logic handout makes the same point with a person who has long hair: knowing that all radicals have long hair and that Ed has long hair tells you nothing about whether Ed is a radical.[^s2] Lander University's notes list several invalid moods that commit the fallacy, including AAA-2, AII-4 and III-1.[^s1]

## How to spot it

Find the term that appears in both premises. Then check each premise: the middle is distributed only where it is the subject of a universal ("All M…", "No M…") or the predicate of a negative ("…are not M").[^s3] If neither premise meets that test, the syllogism commits the fallacy.[^s1][^s2] A quick warning sign in everyday talk is "X has trait T, Y has trait T, so X is Y", where two things are linked only because they share a feature.[^s2] A Venn diagram gives an independent check: if the premises leave a blank region where the minor term can sit outside the major term, the conclusion has not been proved.[^s1]

## How to counter it

Name what the premises leave open. Sharing a trait with a group does not make something a member of that group, and one counterexample, such as an uncertified firm that also uses encrypted transfer, shows that the form can lead from true premises to a false conclusion.[^s1][^s2] If the arguer really means the converse ("only certified suppliers use encrypted transfer"), ask for it to be stated. That premise distributes the middle and can make the argument valid, but it is usually false and now has to be defended.[^s1]

## Evidence

The rule is a matter of logic, not psychology, but the error is easy to miss when the conclusion is believable. Psychologists studying belief bias often open with an undistributed-middle example: all flowers have petals, roses have petals, therefore roses are flowers. Many people judge it valid because the conclusion matches what they know.[^s4] A 2018 hierarchical Bayesian meta-analysis of 22 confidence-rating studies (N = 993) confirmed that believable conclusions are endorsed more often. It also found that believability did not reliably change people's ability to tell valid from invalid forms. The authors read this as mostly a shift in willingness to say "valid", not worse reasoning.[^s4]

## Connections

- **Invalid form of the categorical syllogism.** It breaks one of the rules that every valid standard-form categorical syllogism satisfies.[^s2]
- **Explained by the distribution of terms.** Buridan's account of when a term is distributed, and his requirement that the middle be distributed, define the fallacy.[^s3]
- **Contrasts with the illicit major.** Both are distribution errors, but the illicit major concerns a conclusion term taken more widely than in its premise, while the undistributed middle concerns the term that links the premises.[^s2]
- **Exploits belief bias.** Undistributed-middle syllogisms with plausible conclusions are a standard way to show people accepting invalid arguments because they believe the conclusion.[^s4]

## Sources

[^s1]: "Syllogistic Fallacy 2: Fallacy of the Undistributed Middle Term", Philosophy 103: Introduction to Logic, Lander University. https://philosophy.lander.Edu/logic/middle_fall.html (accessed 2026-11-05)
[^s2]: D. Naugle, "Rules of the Categorical Syllogism", Philosophy 3304 handout, Dallas Baptist University. https://www3.dbu.edu/Naugle/pdf/2302_handouts/categorical_syllogisms.pdf (accessed 2026-11-05)
[^s3]: H. Lagerlund, "Medieval Theories of the Syllogism", Stanford Encyclopedia of Philosophy (rev. 2026). https://plato.stanford.edu/entries/medieval-syllogism/ (accessed 2026-11-05)
[^s4]: D. Trippas et al., "Characterizing belief bias in syllogistic reasoning: A hierarchical Bayesian meta-analysis of ROC data", *Psychonomic Bulletin & Review* 25 (2018), 2141–2174. https://link.springer.com/10.3758/s13423-018-1460-7 (accessed 2026-11-05)
