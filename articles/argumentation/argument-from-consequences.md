---
id: ct:argument-from-consequences
type: ArgumentScheme
title: Argument from consequences
aliases: [argument from positive consequences, argument from negative consequences, consequentialist argument, pragmatic argument]
domain: argumentation
summary: >-
  The presumptive argument pattern "if A is brought about, good (or bad)
  consequences will plausibly follow; so A should (or should not) be brought
  about". It is a reasonable but defeasible basis for decisions about action,
  and it becomes the fallacy of appeal to consequences when it is used to
  settle what is true rather than what to do.
level: introductory
evidenceStatus: normative
broader: [ct:argumentation-schemes]
related: [ct:slippery-slope, ct:ignoratio-elenchi, ct:burden-of-proof, ct:defeasible-reasoning, ct:argument-from-expert-opinion, ct:cost-benefit-reasoning-training, ct:informal-fallacy, ct:ad-baculum]
requires: [ct:argumentation-schemes]
relations:
  - {predicate: contrastsWith, object: ct:appeal-to-consequences, source: s3, confidence: high}
  - {predicate: instanceOf, object: ct:value-based-practical-reasoning, source: s2, confidence: medium}
  - {predicate: influencedBy, object: ct:aristotle, source: s1, confidence: medium}
  - {predicate: explainedBy, object: ct:expected-utility-theory, source: s5, confidence: medium}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s1, confidence: high}
criticalQuestions:
  - How likely is it that the cited consequences will actually follow if the action is taken?
  - What evidence supports the claim that those consequences will occur?
  - Are there consequences of the opposite value, such as benefits of acting or costs of not acting, that should also be weighed?
  - Is the question really a decision about what to do, or a question of fact on which good or bad consequences have no bearing?
  - Is the speaker the one who would bring about the bad outcome, turning a warning into a threat?
argumentMap:
  premises:
    - "If we cut over to the new billing system on the holiday weekend and the cutover fails, customers may be unable to pay for up to three days."
    - "Three days of failed payments would cost us more than waiting two weeks would."
  conclusion: "We should not cut over to the new billing system on the holiday weekend."
  verdict: strong
  scheme: ct:argument-from-consequences
  objections:
    - "A tested rollback plan makes a three-day outage unlikely, so the bad consequence is less probable than claimed."
    - "Waiting also has a cost: the old system's support contract lapses at month end."
sameAs: []
sources:
  - id: s1
    title: "Dialectical Shifts Underlying Arguments from Consequences"
    publisher: "Informal Logic 29(1), 54-83 (Douglas Walton, 2009), journal archive copy"
    url: https://distantreader.org/stacks/journals/il/il-684.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "A classification system for argumentation schemes"
    publisher: "Argument & Computation 6(3), 219-245 (Walton & Macagno, 2015), PhilArchive copy"
    url: https://philarchive.org/archive/WALACS-7
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "Fallacies"
    publisher: Internet Encyclopedia of Philosophy (Bradley Dowden)
    url: https://iep.utm.edu/fallacy/
    type: scholarly-encyclopedia
    accessed: 2026-11-10
  - id: s4
    title: "Utility conditionals as consequential arguments: A random sampling experiment"
    publisher: "Thinking & Reasoning 18(3), 379-393 (Jean-François Bonnefon, 2012), author copy"
    url: https://jfbonnefon.github.io/publication/tar12/tar12.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s5
    title: "The Slippery Slope Argument: Probability, Utility & Category Reappraisal"
    publisher: "Proceedings of the 28th Annual Meeting of the Cognitive Science Society (Corner, Hahn & Oaksford, 2006), eScholarship"
    url: https://escholarship.org/content/qt4m59x3cq/qt4m59x3cq.pdf?t=op2kje
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s6
    title: "Commentary on Feteris"
    publisher: "OSSA Conference Archive, OSSA 5, University of Windsor (Douglas Walton, 2003), CORE copy"
    url: https://core.ac.uk/download/72794604.pdf
    type: academic
    accessed: 2026-11-10
created: 2026-11-10
---

# Argument from consequences

The argument from consequences supports or opposes an action by pointing to what would happen if it were taken. In its positive form, bringing about A would plausibly have good consequences, so A should be brought about; in its negative form, bad consequences would plausibly follow, so A should not be brought about.[^s1][^s2] It is one of the most common argumentation schemes in everyday deliberation, law and policy. Like other schemes it is presumptive: it gives a reason that holds until critical questions about likelihood, evidence and side effects are raised and left unanswered.[^s1]

## Origin

Weighing outcomes is an old part of rhetoric. Walton points to Aristotle's *Rhetoric*, which treats consequences as a topic for both urging and dissuading an audience, and elsewhere traces the pattern to the *Topics* and to later rhetorical work by Windes and Hastings and by Perelman and Olbrechts-Tyteca.[^s1][^s6] Logic textbooks long treated it as a fallacy of relevance; Nicholas Rescher (1964) held that the undesirable results of rejecting a thesis say nothing about whether it is true.[^s1]

The modern scheme, with paired positive and negative forms and critical questions, comes from Douglas Walton's work from the 1990s onward, restated with Reed and Macagno in *Argumentation Schemes* (2008).[^s1][^s2] In Walton and Macagno's 2015 classification it sits under value-based practical reasoning, with argument from threat, from waste and from sunk costs listed beneath it.[^s2]

## How it works

The scheme has one premise linking an action to outcomes and a conclusion about whether to act. Whether an outcome counts as good or bad is fixed by the goals and values the parties share; if the listener accepts that the consequences are bad, the argument gives a real reason against the action.[^s6] Walton gives three critical questions for the negative form: how probable the consequences are, what evidence supports them, and whether there are consequences of the opposite value to set against them.[^s1]

In the argument map above, an operations team argues against a holiday-weekend billing cutover because a failure could block payments for days. That is a strong presumptive argument for a decision. The objections show where the questions bite: a tested rollback plan lowers the probability of the bad outcome, and a lapsing support contract is a consequence of the opposite value that waiting would bring.[^s1]

Subtypes add premises. A slippery slope adds a chain of steps ending in a bad outcome, and an argument from threat adds the speaker's own commitment to bring about the harm unless the listener complies; a mere warning lacks that commitment.[^s1][^s2]

## When it goes wrong

Walton's central claim is that the argument is usually reasonable and becomes fallacious only in context, most often through a dialectical shift: a discussion about whether a claim is true is quietly turned into a deliberation about what would be convenient to do.[^s1] His examples include arguing that a defendant must be convicted because an acquittal would cause riots, which is irrelevant to whether the defendant is guilty, and a professor threatening a poor grade if a student keeps defending a philosophical view.[^s1] By contrast, warning someone that heavy drinking may lead to early death is a legitimate prudential argument, even if a weak one.[^s1]

The Internet Encyclopedia of Philosophy files the fallacious version as appeal to consequence (*argumentum ad consequentiam*): rejecting a belief as false because it implies something one would rather not believe.[^s3] The test is the question at issue. Consequences are relevant to whether to adopt a policy and irrelevant to whether a factual report is accurate.[^s1][^s3]

## Evidence

The scheme is a normative standard, but psychologists have studied how people weigh such arguments. In a Cardiff experiment with 60 students, slippery slope arguments, a species of negative-consequence argument, were rated more convincing when the feared outcome was more probable and when it was worse, consistent with expected-utility reasoning.[^s5] Bonnefon's 2012 study of 39 students used randomly generated utility conditionals and found that people drew predictable conclusions about what an agent would do from statements of who gains or loses, though the study used only four arguments and was framed as a method demonstration.[^s4] Both are small, single-site studies; they show that people respond to probability and value in sensible directions, not that everyday use of the scheme is well calibrated.[^s4][^s5]

## Connections

- **Contrasts with appeal to consequences.** The fallacy uses the same pattern to decide what is true rather than what to do.[^s3][^s1]
- **Instance of value-based practical reasoning.** Walton and Macagno place it under practical reasoning that turns on values.[^s2]
- **Influenced by Aristotle,** whose rhetoric treats consequences as grounds for exhortation and dissuasion.[^s1]
- **Explained by expected-utility theory.** Corner, Hahn and Oaksford tie the strength of negative-consequence arguments to outcome probability and disutility.[^s5]
- **Studied in argumentation theory,** where Walton's account of dialectical shifts is the standard treatment.[^s1]
- **Related:** the slippery slope and threat (ad baculum) are subtypes; ignoratio elenchi names the wrong-conclusion failure; the burden of proof governs who must answer the critical questions; and argument from expert opinion is a sibling scheme.[^s1][^s2]

## Sources

[^s1]: Walton, "Dialectical Shifts Underlying Arguments from Consequences", *Informal Logic* 29(1), 2009, 54-83. https://distantreader.org/stacks/journals/il/il-684.pdf (accessed 2026-11-10)
[^s2]: Walton & Macagno, "A classification system for argumentation schemes", *Argument & Computation* 6(3), 2015, 219-245. https://philarchive.org/archive/WALACS-7 (accessed 2026-11-10)
[^s3]: Dowden, "Fallacies", *Internet Encyclopedia of Philosophy*. https://iep.utm.edu/fallacy/ (accessed 2026-11-10)
[^s4]: Bonnefon, "Utility conditionals as consequential arguments: A random sampling experiment", *Thinking & Reasoning* 18(3), 2012, 379-393. https://jfbonnefon.github.io/publication/tar12/tar12.pdf (accessed 2026-11-10)
[^s5]: Corner, Hahn & Oaksford, "The Slippery Slope Argument: Probability, Utility & Category Reappraisal", *Proceedings of the 28th Annual Conference of the Cognitive Science Society*, 2006. https://escholarship.org/content/qt4m59x3cq/qt4m59x3cq.pdf?t=op2kje (accessed 2026-11-10)
[^s6]: Walton, "Commentary on Feteris", OSSA Conference Archive (OSSA 5), University of Windsor, 2003. https://core.ac.uk/download/72794604.pdf (accessed 2026-11-10)
