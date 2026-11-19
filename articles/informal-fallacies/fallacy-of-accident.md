---
id: ct:fallacy-of-accident
type: InformalFallacy
title: Fallacy of accident
aliases: [accident fallacy, fallacia accidentis, sweeping generalization, a dicto simpliciter ad dictum secundum quid, neglecting qualifications]
domain: informal-fallacies
summary: >-
  The fallacy of applying a generally sound rule or generalization to a
  particular case whose unusual circumstances fall outside the conditions the
  rule was meant to cover, as if the rule held without exception.
level: introductory
evidenceStatus: normative
broader: [ct:informal-fallacy]
related: [ct:hasty-generalization, ct:fallacy-of-composition, ct:fallacy-of-division, ct:no-true-scotsman, ct:equivocation, ct:defeasible-reasoning, ct:straw-man-fallacy, ct:richard-whately, ct:douglas-walton, ct:fallacies-of-relevance]
requires: [ct:argument]
relations:
  - {predicate: introducedIn, object: ct:sophistical-refutations, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:aristotle, source: s2, confidence: high}
  - {predicate: instanceOf, object: ct:fallacies-of-relevance, source: s1, confidence: medium}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s3, confidence: high}
criticalQuestions:
  - Is the general rule stated as an exceptionless universal, or is it really a "usually" or "as a rule" claim?
  - What purpose or typical situation was the rule designed for, and does this case share it?
  - Is there something unusual about this case that the rule's authors did not have in mind?
  - Does a key term mean the same thing in the rule as it does in the conclusion about this case?
  - Would applying the rule here defeat the very goal the rule exists to serve?
argumentMap:
  premises:
    - "Company policy says all expense claims must include an itemised paper receipt."
    - "The engineer's taxi in the foreign city was paid in cash, and the driver issued no receipt."
  conclusion: "So the engineer's taxi fare cannot be reimbursed."
  verdict: fallacious
  objections:
    - "The receipt rule exists to prevent fraud and was written for normal purchases where receipts are available; it did not anticipate cases where no receipt can be obtained."
    - "Policies of this kind usually allow a signed statement or card record in exceptional cases, so treating the rule as absolute ignores its implicit qualifications."
sameAs: []
sources:
  - id: s1
    title: "Fallacies"
    publisher: Stanford Encyclopedia of Philosophy (Hansen, substantive revision 2024)
    url: https://plato.stanford.edu/ENTRIES/fallacies/
    type: scholarly-encyclopedia
    accessed: 2026-11-19
  - id: s2
    title: "The Fallacy of Accident"
    publisher: "Lee C. Archie, Introduction to Logic, Lander University"
    url: https://philosophy.lander.Edu/logic/accident.html
    type: academic
    accessed: 2026-11-19
  - id: s3
    title: "Secundum Quid and the Pragmatics of Arguments. The Challenges of the Dialectical Tradition"
    publisher: "Fabrizio Macagno, Argumentation 36(3), 317-343 (2022), Springer"
    url: https://link.springer.com/article/10.1007/s10503-022-09568-4
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "Applied logic: Nonverbal fallacies"
    publisher: "Jaakko J. Hintikka, Encyclopaedia Britannica"
    url: https://www.britannica.com/topic/applied-logic/Nonverbal-fallacies
    type: encyclopedia
    accessed: 2026-11-19
  - id: s5
    title: "Dicto Simpliciter"
    publisher: "Fallacies tutorial, Palomar College faculty pages"
    url: https://www.palomar.edu/users/bthompson/Dicto%20Simpliciter.html
    type: academic
    accessed: 2026-11-19
created: 2026-11-19
---

# Fallacy of accident

The fallacy of accident is the error of taking a rule or generalization that is sound in the ordinary run of cases and applying it to an atypical case that lies outside the conditions the rule was meant to cover.[^s2] Archie's logic course calls it a fallacy of neglecting qualifications: lions are generally dangerous, but that does not make a well-fed, trained lion dangerous in every situation.[^s2] Palomar College's tutorial describes it as applying a rule to a case outside its scope, and notes that the fallacy trades on how hard it is to tell when differences between cases really matter.[^s5]

## Origin

Aristotle introduced a fallacy of accident in *On Sophistical Refutations*, listing it among the fallacies that do not depend on language.[^s1][^s2] His version is narrower than the modern one. Hansen's SEP entry explains that it treats an accidental attribute as if it were a thing's proper attribute: being equal to two right angles belongs to triangles, but if a triangle happens to be a first principle, it does not follow that every first principle has that property.[^s1] Hintikka reads Aristotle's simplest cases as confusions between senses of "is", identity versus predication, and concludes that this original fallacy has no exact modern counterpart.[^s4]

The modern rule-to-exception sense grew out of the later tradition. Archie traces the Latin name *fallacia accidentis* through the medieval logicians, notes Thomas Blundeville's 1599 description as the first in English, and credits Henry Aldrich and W. Stanley Jevons with the definitions that became textbook standards.[^s2] Many writers equate it with *a dicto simpliciter ad dictum secundum quid*, reasoning from what is said without qualification to a case that needs one.[^s2] Irving Copi's 1961 textbook placed accident and converse accident among the fallacies of relevance, as errors of carelessness about the subject matter.[^s1]

## How it works

The argument has the shape "As a rule, Xs are F; this is an X; so this is F", where "as a rule" has quietly hardened into "always".[^s2] In the argument map above, a receipt policy built to stop fraud in normal purchases is applied to a cash fare where no receipt could be obtained, defeating the rule's purpose rather than serving it.[^s2][^s5] Archie's examples are similar: reading "everyone may vote" as covering children and noncitizens, or treating a moral rule against killing as settling every case without further argument.[^s2]

Some cases also shift a term's meaning. Archie's "Water is liquid; ice is water; so ice is liquid" uses "water" generically in one premise and for a frozen state in the other, which makes the argument a four-term syllogism.[^s2] Macagno's 2022 study in *Argumentation* explains the underlying mechanism as pragmatic: a claim that is implicitly qualified is presented as unqualified, so a default reading replaces the one the context requires.[^s3]

## How to spot it

- Look for a general rule, proverb or policy invoked to settle a case that is unusual in some obvious way.[^s2][^s5]
- Ask whether the premise is a soft generalization (usually, normally, as a rule) being used as if it were exceptionless.[^s2]
- Check whether a key term means something different in the rule and in the case.[^s2]
- Ask whether the difference between this case and the typical one is relevant to the rule's purpose; Palomar's tutorial warns that irrelevant differences (the colour of a car at a red light) do not create exceptions.[^s5]

## How to counter it

State the rule's purpose and the conditions it assumes, then show which of them the present case lacks.[^s2][^s5] Replace the universal reading with the qualified one the rule really supports, and argue for the exception on its merits rather than simply asserting it.[^s3] Archie cautions that there is no reliable test for separating usual from unusual circumstances, so the charge of accident is itself an argument that needs support, as in disputes over whether a moral rule admits exceptions.[^s2]

## Connections

- **Introduced in** Aristotle's *On Sophistical Refutations*, where accident is one of the fallacies outside language.[^s1]
- **Introduced by** Aristotle, whose account the Latin, English and modern textbook traditions reworked.[^s2]
- **Instance of** the fallacies of relevance in Copi's 1961 classification.[^s1]
- **Studied in** argumentation theory, where Macagno analyses the related *secundum quid* as a pragmatic fallacy and links it to the straw man.[^s3]
- **Related** to hasty generalization, often called converse accident because it runs the other way, from atypical cases up to a rule; Walton proposed grouping both as neglect of qualifications, and Whately treated *secundum quid* as accident's counterpart.[^s2][^s3]
- **Related** to equivocation, the fallacies of composition and division, the no true Scotsman and defeasible reasoning, which studies generalizations that hold only by default.[^s2][^s3]

## Sources

[^s1]: H. Hansen, "Fallacies", Stanford Encyclopedia of Philosophy, substantive revision 2024. https://plato.stanford.edu/ENTRIES/fallacies/ (accessed 2026-11-19)
[^s2]: L. C. Archie, "The Fallacy of Accident", Introduction to Logic, Lander University. https://philosophy.lander.Edu/logic/accident.html (accessed 2026-11-19)
[^s3]: F. Macagno, "Secundum Quid and the Pragmatics of Arguments. The Challenges of the Dialectical Tradition", *Argumentation* 36(3), 317-343, 2022. https://link.springer.com/article/10.1007/s10503-022-09568-4 (accessed 2026-11-19)
[^s4]: J. J. Hintikka, "Applied logic: Nonverbal fallacies", Encyclopaedia Britannica. https://www.britannica.com/topic/applied-logic/Nonverbal-fallacies (accessed 2026-11-19)
[^s5]: "Dicto Simpliciter", fallacies tutorial, Palomar College faculty pages. https://www.palomar.edu/users/bthompson/Dicto%20Simpliciter.html (accessed 2026-11-19)
