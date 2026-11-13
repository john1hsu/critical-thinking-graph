---
id: ct:no-true-scotsman
type: InformalFallacy
title: No true Scotsman
aliases: [no-true-Scotsman move, no true Scotsman ploy, no-true-Scotsman fallacy]
domain: informal-fallacies
summary: >-
  The fallacy of rescuing a generalization from a counterexample by quietly
  narrowing the category, typically by adding "true", "real" or "genuine",
  so that the counterexample no longer counts as a member.
level: introductory
evidenceStatus: normative
broader: [ct:informal-fallacy]
related: [ct:ad-hoc-hypothesis, ct:stipulative-definition, ct:precising-definition, ct:hasty-generalization, ct:falsifiability, ct:begging-the-question]
requires: [ct:argument]
relations:
  - {predicate: introducedBy, object: ct:antony-flew, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:thinking-about-thinking, source: s1, confidence: high}
  - {predicate: confusedWith, object: ct:fallacy-of-accident, source: s3, confidence: medium}
  - {predicate: explainedBy, object: ct:in-group-bias, source: s3, confidence: low}
  - {predicate: confusedWith, object: ct:ad-hoc-hypothesis, source: s1, confidence: medium}
criticalQuestions:
  - Was the restriction ("true", "real", "genuine") part of the claim before the counterexample appeared, or was it added only after?
  - Is there an independent, agreed criterion for membership in the group, or is membership now defined by having the property in question?
  - Could any possible case count against the revised claim, or has it become true by definition?
  - If the narrowed claim is now safe, what does it still tell us about the actual members of the group?
  - Is the dispute really about how the term should be defined, and if so, has that been argued for openly?
argumentMap:
  premises:
    - "No experienced engineer on our team would ever push code without running the tests."
    - "A colleague with ten years on the team and pushed untested code last week."
    - "A truly experienced engineer would never have done that."
  conclusion: "So that colleague is not really an experienced engineer, and the original claim stands."
  verdict: fallacious
  objections:
    - "Experience was first measured by years on the team; it is now being measured by never skipping tests, which makes the claim true by definition."
    - "The counterexample should lead to revising the generalization (most experienced engineers run tests), not to reclassifying the colleague."
sources:
  - id: s1
    title: "Is Flew's No True Scotsman Fallacy a True Fallacy? A Contextual Analysis"
    publisher: "Anderson, in Modeling and Using Context (CONTEXT 2017), LNAI 10257, Springer, pp. 243-253"
    url: https://link.springer.com/chapter/10.1007/978-3-319-57837-8_19
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s2
    title: "No True Scotsman"
    publisher: "Palomar College philosophy course materials"
    url: https://www.palomar.edu/users/bthompson/No%20True%20Scotsman.html
    type: academic
    accessed: 2026-11-13
  - id: s3
    title: "No True Scotsman"
    publisher: "Chapter in Arp, Barbone & Bruce (eds.), Bad Arguments, Wiley-Blackwell (2018), pp. 374-377; PhilArchive record"
    url: https://dc2.philarchive.org/rec/MANNTS-2
    type: textbook
    accessed: 2026-11-13
  - id: s4
    title: "The No-True-Scotsman Fallacy"
    publisher: "The Fallacy Files (G. N. Curtis)"
    url: https://fallacyfiles.org/scotsman.html
    type: community
    accessed: 2026-11-13
created: 2026-11-13
---

# No true Scotsman

The no true Scotsman fallacy occurs when someone faces a counterexample to a sweeping generalization and, instead of giving up or qualifying the generalization, redefines the group so the counterexample no longer belongs to it.[^s4] The tell-tale step is a new qualifier such as "true", "real" or "genuine" that was not in the original claim.[^s4] The move rules out counterexamples by stipulation rather than by any criterion the group actually has, which leaves the claim immune to refutation.[^s2]

## Origin

The British philosopher Antony Flew named and popularised the move in *Thinking About Thinking* (1975), where he told the story of a patriotic Scot who reads of a crime and insists no Scotsman would do such a thing; when a Scot is later reported to have done something worse, he replies that no *true* Scotsman would.[^s1][^s2] Curtis's Fallacy Files records that Flew returned to the example in later books, including *How to Think Straight* (1998), and that Alan Musgrave calls it a "ploy".[^s4] Flew compared the revised claim to Wittgenstein's point that tautologies say nothing: the speaker is no longer asserting anything about what actually happens in the world.[^s1]

## How it works

The pattern has three steps: a universal claim about a group, a counterexample from within the group, and a restatement of the claim with a narrower meaning that excludes the counterexample.[^s4] In the argument map above, "experienced engineer" first means someone with long service; after a counterexample it silently comes to mean someone who never skips tests. The new claim cannot be false, but only because it no longer says anything about the engineers on the team.[^s4] Curtis puts the trade-off plainly: the arguer buys truth at the cost of informativeness, since "all true swans are white" only reports how the speaker uses the word "swan".[^s4] A Palomar College course page classifies the move as a kind of circularity: membership is fixed by the very property the generalization was supposed to establish.[^s2]

## How to spot it

Watch for "true", "real", "genuine" or "proper" attached to an ordinary group noun right after a counterexample has been raised.[^s4] Ask whether membership criteria for the group exist independently of the disputed property; a political party, a nationality or a profession usually has such criteria, and an invented extra requirement is a warning sign.[^s2] The *Bad Arguments* chapter adds that the arguer sets himself up as the authority on who belongs, which is what makes the claim impossible to disprove.[^s3]

## How to counter it

Point out that the definition has shifted and ask for the criterion of membership that was in use before the counterexample appeared.[^s2] If the speaker accepts that criterion, the counterexample stands and the generalization should be weakened to "most" or "typically".[^s4] The *Bad Arguments* chapter recommends awareness of one's own in-group loyalties and acceptance that members of a group disagree and behave differently.[^s3]

Not every use of "true" is fallacious. Anderson argues that context matters: the speaker's meaning, where "true" sits in the sentence, and whether the conversation is openly about how a category should be defined can all make the move legitimate.[^s1] The Palomar course page likewise notes that excluding cases by a genuine defining principle is not a fallacy.[^s2] A dispute over what "vegetarian" or "fully remote" should mean, argued in the open, is a definitional debate, not a no true Scotsman.

## Connections

- **Named by Antony Flew in *Thinking About Thinking*.** Anderson's analysis takes Flew's 1975 book as the source of the name and the Scotsman story.[^s1]
- **Confused with ad hoc rescue.** Anderson notes that many sources classify the move as an ad hoc rescue or as a form of redefinition, which is why it is often confused with the scientific notion of an ad hoc hypothesis that saves a theory from refutation.[^s1]
- **Confused with the fallacy of accident.** The *Bad Arguments* chapter distinguishes the two, calling the no true Scotsman more subjective, because group membership is decided by the arguer rather than by a general rule misapplied.[^s3]
- **Explained by in-group bias (tentative).** The same chapter traces the move to the tendency to divide people into "us" and "them" and protect the group's image; this is an argued explanation, not a measured effect.[^s3]
- **Related to falsifiability and definition.** Because the revised claim cannot be refuted by any case, it relates to [falsifiability](../scientific-reasoning/falsifiability.md); because it works by quietly changing a definition, it contrasts with openly argued stipulative and precising definitions.[^s1][^s2]

## Sources

[^s1]: Anderson, "Is Flew's No True Scotsman Fallacy a True Fallacy? A Contextual Analysis", in *Modeling and Using Context* (CONTEXT 2017), LNAI 10257, Springer, 243-253. https://link.springer.com/chapter/10.1007/978-3-319-57837-8_19 (accessed 2026-11-13)
[^s2]: "No True Scotsman", Palomar College philosophy course materials. https://www.palomar.edu/users/bthompson/No%20True%20Scotsman.html (accessed 2026-11-13)
[^s3]: "No True Scotsman", in Arp, Barbone & Bruce (eds.), *Bad Arguments*, Wiley-Blackwell (2018), 374-377. https://dc2.philarchive.org/rec/MANNTS-2 (accessed 2026-11-13)
[^s4]: Curtis, "The No-True-Scotsman Fallacy", The Fallacy Files. https://fallacyfiles.org/scotsman.html (accessed 2026-11-13)
