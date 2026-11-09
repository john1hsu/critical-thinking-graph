---
id: ct:fallacy-of-four-terms
type: FormalFallacy
title: Fallacy of four terms
aliases: [quaternio terminorum, four-term fallacy, fallacy of more than three terms]
domain: formal-fallacies
summary: >-
  The syllogistic fallacy of an argument that looks like a categorical
  syllogism but uses four terms instead of three, usually because one word
  carries two meanings, so the middle term never actually links the subject
  and predicate of the conclusion.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:syllogism, ct:undistributed-middle, ct:illicit-major, ct:venn-diagram-test, ct:rules-of-the-categorical-syllogism, ct:ambiguous-middle-term, ct:equivocation]
requires: [ct:categorical-syllogism, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:categorical-syllogism, source: s3, confidence: high}
  - {predicate: explainedBy, object: ct:equivocation, source: s1, confidence: medium}
  - {predicate: contrastsWith, object: ct:undistributed-middle, source: s4, confidence: medium}
criticalQuestions:
  - Does each key word or phrase mean exactly the same thing in both places it appears?
  - If the shared term were replaced by a precise definition, would the two premises still talk about the same class?
  - Does the argument look valid even though its premises are true and its conclusion is plainly false?
  - Once the terms are counted by meaning rather than by wording, are there still only three?
argumentMap:
  premises:
    - "All tools that have passed the security review are approved for production use."
    - "All of the vendor's plugins have passed a security review."
  conclusion: "All of the vendor's plugins are approved for production use."
  verdict: invalid
  scheme: ct:categorical-syllogism
  objections:
    - "The first premise means the company's own formal review; the second may mean the vendor's internal check."
    - "With two different reviews in play, the argument has four terms, and nothing links the plugins to approval."
sameAs: []
sources:
  - id: s1
    title: "The Four Term Fallacy"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://fallacyfiles.org/fourterm.html
    type: community
    accessed: 2026-11-09
  - id: s2
    title: "Syllogistic Fallacies: Four Term Fallacy"
    publisher: "Philosophy 103: Introduction to Logic, Lander University"
    url: https://philosophy.lander.edu/logic/four_fall.html
    type: academic
    accessed: 2026-11-09
  - id: s3
    title: "6.5 Rules for Evaluating Syllogisms"
    publisher: "PHIL 240 lecture notes, Texas A&M University"
    url: https://phil240.tamu.edu/LectureNotes/6.5.pdf
    type: academic
    accessed: 2026-11-09
  - id: s4
    title: "Deductive Logic, Part III, Chapter XXX: Of Fallacies"
    publisher: "G. W. J. Stock (1888), Lit2Go, University of South Florida"
    url: https://etc.usf.edu/lit2go/189/deductive-logic/3940/part-3-chapter-30/
    type: textbook
    accessed: 2026-11-09
  - id: s5
    title: "Medieval Theories of the Syllogism"
    publisher: "Stanford Encyclopedia of Philosophy (Henrik Lagerlund, rev. 2022; Summer 2025 edition)"
    url: https://plato.stanford.edu/archives/sum2025/entries/medieval-syllogism/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
created: 2026-11-09
---

# Fallacy of four terms

The fallacy of four terms, known by its Latin name *quaternio terminorum*, is committed by an argument that has the shape of a categorical syllogism but contains four terms rather than three.[^s1] A standard-form syllogism needs exactly three terms (the subject and predicate of the conclusion and a middle term that links them), each used in one sense throughout.[^s3] A term here is a meaning, not a word. Two words with one meaning count as one term, and one word used in two senses counts as two.[^s1] Because the extra term is almost always smuggled in by a word that shifts its sense, the argument can look perfectly valid on paper while proving nothing.[^s1][^s2]

## Origin

The requirement it violates is as old as the syllogism itself. Aristotle's syllogism has three sentences built from three terms, major, minor and middle, and medieval logicians inherited that picture, although some, such as John Buridan, also studied arguments with more than three terms.[^s5] Victorian logic textbooks listed four terms among the formal fallacies of the syllogism, alongside the undistributed middle, illicit process and negative premises. G. W. J. Stock's 1888 *Deductive Logic* added that "more than three terms" would be the more exact name, since a syllogism-like argument could in principle contain up to six.[^s4] Modern catalogues keep the Latin label and file the fallacy under syllogistic fallacies.[^s1]

## How it works

Take the argument map above. On the surface it is a valid mood: all M are P, all S are M, so all S are P. But "the security review" in the first premise means the company's own formal review, while "a security review" in the second could mean the vendor's internal check. Those are two different classes. The argument therefore has four terms: the vendor's plugins, tools approved for production, tools that passed the company's review, and tools that passed the vendor's review. With two middle terms instead of one, nothing connects the plugins to approval, and the conclusion does not follow.[^s2][^s3] Stock's classic case has the same structure: people who write books are authors; all educated people could write books; so all educated people are authors. Actually writing books and being able to write them are different things.[^s4]

Logicians disagree slightly about how to describe the fault. One view holds that a four-term argument is not a syllogism at all, because the three-term rule partly defines what a syllogism is, while the other rules decide whether a genuine syllogism is valid.[^s1] Introductory courses simply treat it as the first rule of validity, often under the informal-logic name of equivocation.[^s2][^s3]

## How to spot it

The tell-tale sign is an argument that seems formally valid yet has true premises and an obviously false conclusion. A valid form cannot do that, so look for a term that changed meaning.[^s2] Rewrite each premise with its terms spelled out precisely, then count meanings rather than words.[^s1] Check the middle term first: an equivocal middle is the most common case and has its own name, the fallacy of ambiguous middle.[^s4] A Venn diagram drawn from the wording alone will look valid, so diagram only after the terms are pinned down; once the fourth term is shown, no valid diagram can be drawn.[^s2]

## How to counter it

Ask the arguer to define the shared word in each premise. If the definitions differ, the argument falls apart; if they are forced to match, one premise usually becomes false or doubtful.[^s2][^s3] In the workplace example, the fix is to ask which review the vendor's plugins passed. If it was the company's formal review, the argument is valid and sound. If it was only the vendor's own check, the premise that would matter, that the plugins passed the company review, is simply unsupported.[^s3]

## Connections

- **Invalid form of the categorical syllogism.** It breaks the first rule of the standard-form syllogism, that there be exactly three terms used in the same sense.[^s3]
- **Explained by equivocation.** Real cases are usually equivocations, in which one word hides two meanings and so conceals the extra term.[^s1]
- **Related to the ambiguous middle, its most common variety.** When the shifting term is the middle term, textbooks call the result the fallacy of ambiguous middle.[^s4]
- **Contrasts with the undistributed middle.** Both stop the middle term from linking the other two, but the undistributed middle has one middle term that never covers its whole class, while four terms has two middle terms that never meet. Stock lists them as separate formal fallacies.[^s4]
- **Related to the rules of the categorical syllogism and the Venn diagram test,** the two standard ways of checking a syllogism, each of which must count terms by meaning to catch this error.[^s2][^s3]

## Sources

[^s1]: Gary N. Curtis, "The Four Term Fallacy", The Fallacy Files. https://fallacyfiles.org/fourterm.html (accessed 2026-11-09)
[^s2]: "Syllogistic Fallacies: Four Term Fallacy", Philosophy 103: Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/four_fall.html (accessed 2026-11-09)
[^s3]: "6.5 Rules for Evaluating Syllogisms", PHIL 240 lecture notes, Texas A&M University. https://phil240.tamu.edu/LectureNotes/6.5.pdf (accessed 2026-11-09)
[^s4]: G. W. J. Stock, *Deductive Logic* (1888), Part III, Chapter XXX, "Of Fallacies", Lit2Go, University of South Florida. https://etc.usf.edu/lit2go/189/deductive-logic/3940/part-3-chapter-30/ (accessed 2026-11-09)
[^s5]: Henrik Lagerlund, "Medieval Theories of the Syllogism", Stanford Encyclopedia of Philosophy (Summer 2025 edition). https://plato.stanford.edu/archives/sum2025/entries/medieval-syllogism/ (accessed 2026-11-09)
