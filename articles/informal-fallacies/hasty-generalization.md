---
id: ct:hasty-generalization
type: InformalFallacy
title: Hasty generalization
aliases: [converse accident, faulty induction, false induction, generalizing from too few cases, overgeneralization, fallacy of insufficient sample]
domain: informal-fallacies
summary: >-
  The fallacy of drawing a general conclusion about a whole class from too few,
  or too unrepresentative, cases, or of treating a rule that holds only usually
  as if it had no exceptions.
level: introductory
evidenceStatus: normative
broader: [ct:informal-fallacy]
related: [ct:insensitivity-to-sample-size, ct:argument-from-analogy, ct:post-hoc-ergo-propter-hoc, ct:suppressed-evidence, ct:representativeness-heuristic, ct:availability-heuristic, ct:selection-bias, ct:defeasible-reasoning]
requires: [ct:inductive-reasoning]
relations:
  - {predicate: instanceOf, object: ct:jumping-to-conclusions, source: s2, confidence: medium}
  - {predicate: confusedWith, object: ct:fallacy-of-accident, source: s3, confidence: high}
  - {predicate: introducedIn, object: ct:port-royal-logic, source: s1, confidence: medium}
  - {predicate: explainedBy, object: ct:law-of-small-numbers, source: s4, confidence: medium}
  - {predicate: explainedBy, object: ct:anecdotal-bias, source: s5, confidence: low}
criticalQuestions:
  - How many cases is the conclusion based on, and is that enough for a claim this broad?
  - How were the cases chosen, and could the way they were found make them unusual?
  - Does the conclusion say "all" or "always" when the evidence supports only "many" or "usually"?
  - Were counterexamples looked for, and what happened to the ones that turned up?
  - How much is at stake if the generalization is wrong, and does that call for a higher standard of proof?
argumentMap:
  premises:
    - "At the trade show, three visitors to our booth said they wanted a dark mode in the app."
    - "Two support tickets last week also asked for a dark mode."
  conclusion: "So most of our customers want dark mode, and it should be next quarter's top priority."
  verdict: fallacious
  objections:
    - "Five requests out of several thousand active customers is a tiny sample."
    - "Trade-show visitors and people who file tickets are self-selected and may not resemble the typical customer."
    - "Nobody checked the feature-request backlog or usage survey for competing priorities."
sources:
  - id: s1
    title: "Fallacies"
    publisher: Stanford Encyclopedia of Philosophy (Hansen, rev. 2024)
    url: https://plato.stanford.edu/entries/fallacies/
    type: scholarly-encyclopedia
    accessed: 2026-11-10
  - id: s2
    title: "Jumping to a Conclusion: Fallacies and Standards of Proof"
    publisher: Informal Logic 29(2) (Walton & Gordon, 2009)
    url: https://doaj.org/article/caa261e5b9f144b6b301b6747f95fb4e
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "Fallacy of Accident (Introduction to Logic)"
    publisher: Lander University, Department of Philosophy (Archie)
    url: https://philosophy.lander.edu/logic/accident.html
    type: academic
    accessed: 2026-11-10
  - id: s4
    title: "Belief in the law of small numbers"
    publisher: Psychological Bulletin 76(2):105-110 (Tversky & Kahneman, 1971)
    url: https://literature.wolkersdorfer.info/literature/Belief%20in%20the%20law%20of%20small%20numbers.pdf
    type: primary
    accessed: 2026-11-10
  - id: s5
    title: "When poignant stories outweigh cold hard facts: A meta-analysis of the anecdotal bias"
    publisher: Organizational Behavior and Human Decision Processes 160:51-67 (Freling, Yang, Saini, Itani & Rashad Abualsamh, 2020)
    url: https://econpapers.repec.org/RePEc:eee:jobhdp:v:160:y:2020:i:c:p:51-67
    type: peer-reviewed
    accessed: 2026-11-10
created: 2026-11-10
---

# Hasty generalization

A hasty generalization concludes something about a whole group from a sample that cannot carry the weight: too few cases, cases that are unusual, or a rule stated as exceptionless when it holds only usually.[^s1][^s3] Generalizing is not the error. Every inductive argument moves from observed cases to unobserved ones, and defeasible generalizations such as "most dogs are friendly" are legitimate tools; the fallacy lies in the haste, in claiming more than the evidence and the context allow.[^s2]

## Origin

Aristotle's list of fallacies did not include an inductive version, though his *secundum quid* (confusing what holds in a certain respect with what holds absolutely) is its close cousin.[^s1] Hans Hansen traces the inductive fallacy to the Port-Royal Logic of Arnauld and Nicole (1662), which added a faulty, incomplete induction to the inherited list, "what we might call hasty generalization."[^s1] Isaac Watts kept it as "false induction", and John Stuart Mill made "fallacies of generalization" a whole branch of inductive error.[^s1] Twentieth-century textbooks such as Copi's sometimes called it *converse accident*, because it runs in the opposite direction to the fallacy of accident.[^s1][^s3] Douglas Walton later argued that ignoring qualifications (*secundum quid*) is best treated as a sub-type of hasty generalization.[^s3]

## How it works

In the argument map above, a product manager hears three trade-show visitors and two support tickets ask for a dark mode and concludes that most customers want it. Every premise is true, yet the conclusion outruns them twice over. Five requests is a tiny fraction of a large customer base, and people who visit a booth or file a ticket are a self-selected group who may not resemble everyone else.[^s3] A third failure is common too: the generalization is used as if it settled the matter, without looking for evidence that would show exceptions.[^s2]

Walton and Gordon (2009) place the fallacy inside a wider pattern they call jumping to a conclusion. One form is resting a claim on evidence too weak for the burden of proof; another is treating a defeasible "usually" as an absolute "always" and ignoring exceptions. Applying a stereotype to an individual without considering contrary evidence is their central example.[^s2] On their account, whether a quick generalization is fallacious depends on the setting: a hunch that is fine for choosing a lunch spot can be reckless when safety is at stake, where a higher standard of proof applies.[^s2]

## How to spot it

Look for sweeping words ("all", "always", "everyone", "never") resting on a handful of cases, a personal story, or one memorable incident.[^s3][^s5] Ask how the cases were gathered: complaints, testimonials, volunteers and the people within earshot are rarely a fair sample.[^s3] Notice when an apparent counterexample is waved away rather than weighed, since ignoring exceptions is one of the ways the reasoning goes wrong.[^s2] And distinguish two related failures: overlooking evidence through a shallow search, which Walton and Gordon treat as the simpler error, and suppressing it, which they judge more culpable.[^s2]

## How to counter it

Ask the critical questions above, starting with sample size and selection. Tversky and Kahneman's advice to researchers carries over to everyday reasoning: estimate how much a small sample could vary by chance, prefer computation to intuition, and be wary of early trends.[^s4] Restate the claim at the strength the evidence supports, for example "some customers want dark mode", and then decide what further data (a survey, the full request log) would justify more.[^s2] Where decisions carry high stakes, raise the bar before acting.[^s2]

## Evidence

As a standard of good reasoning, the fallacy's status is normative, but psychology shows why it is tempting. Tversky and Kahneman (1971) surveyed research psychologists and found that even trained scientists expected small samples to mirror their population closely, a belief they called the "law of small numbers"; the median respondent put the chance that a 10-subject replication would succeed at about .85, against a calculated .48.[^s4] The respondents were attendees at two professional meetings, and the authors did not claim they were representative, so the specific figures are best read as illustrative.[^s4] A 2020 meta-analysis of 61 studies by Freling and colleagues found that anecdotes persuade more than statistics when people are emotionally engaged, as with severe or health-related threats, while statistics win when engagement is low.[^s5] That is one reason a single vivid story so easily becomes a general rule.

## Connections

Hasty generalization is an **instance of jumping to conclusions**, the broader pattern of premature inference that Walton and Gordon analyse.[^s2] It is often **confused with the fallacy of accident**, its mirror image, which misapplies a general rule to an atypical case.[^s3] Its inductive form was **introduced in the Port-Royal Logic**.[^s1] Its pull is **explained by the law of small numbers**, the intuition that small samples are representative,[^s4] and, more tentatively, by the **anecdotal bias** documented in the persuasion literature.[^s5] Related topics include **insensitivity to sample size**, **selection bias**, the **representativeness** and **availability** heuristics, **suppressed evidence**, **post hoc ergo propter hoc** (which Mill also counted as a fallacy of generalization), **argument from analogy**, and **defeasible reasoning**.[^s1][^s2][^s4]

## Sources

[^s1]: Hansen, "Fallacies", Stanford Encyclopedia of Philosophy (substantive revision 2024). https://plato.stanford.edu/entries/fallacies/ (accessed 2026-11-10)
[^s2]: Walton & Gordon, "Jumping to a Conclusion: Fallacies and Standards of Proof", Informal Logic 29(2), 2009, doi:10.22329/il.v29i2.1227. https://doaj.org/article/caa261e5b9f144b6b301b6747f95fb4e (accessed 2026-11-10)
[^s3]: Archie, "Fallacy of Accident", Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/accident.html (accessed 2026-11-10)
[^s4]: Tversky & Kahneman, "Belief in the law of small numbers", Psychological Bulletin 76(2):105-110, 1971. https://literature.wolkersdorfer.info/literature/Belief%20in%20the%20law%20of%20small%20numbers.pdf (accessed 2026-11-10)
[^s5]: Freling, Yang, Saini, Itani & Rashad Abualsamh, "When poignant stories outweigh cold hard facts: A meta-analysis of the anecdotal bias", Organizational Behavior and Human Decision Processes 160:51-67, 2020. https://econpapers.repec.org/RePEc:eee:jobhdp:v:160:y:2020:i:c:p:51-67 (accessed 2026-11-10)
