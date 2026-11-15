---
id: ct:decision-theory
type: Field
title: Decision theory
aliases: [normative decision theory, theory of rational choice, rational choice under uncertainty]
domain: decision-making
summary: >-
  The interdisciplinary study of how an agent's beliefs and desires should
  combine into choices, especially under uncertainty; its orthodox normative
  core is expected utility theory, built on axioms about coherent preference,
  and it is contrasted with descriptive research on how people actually choose.
level: intermediate
evidenceStatus: normative
broader: [ct:philosophy]
related: [ct:expected-utility-theory, ct:decision-analysis, ct:judgment-and-decision-making, ct:prospect-theory, ct:risk-aversion, ct:bayesian-reasoning, ct:bounded-rationality, ct:expected-value]
requires: [ct:probability-theory, ct:expected-value]
relations:
  - {predicate: formalizedBy, object: ct:theory-of-games-and-economic-behavior, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:probability-theory, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:allais-paradox, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:judgment-and-decision-making, source: s3, confidence: medium}
  - {predicate: appliedIn, object: ct:economics, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Decision Theory"
    publisher: Stanford Encyclopedia of Philosophy (Stefánsson; first published 2015 with Steele; substantive revision 2025)
    url: https://plato.stanford.edu/ENTRiES/decision-theory/
    type: scholarly-encyclopedia
    accessed: 2026-11-15
  - id: s2
    title: "An Introduction to Decision Theory, 2nd ed., chapter 3: Decisions under Ignorance"
    publisher: Cambridge University Press (Martin Peterson, 2017)
    url: https://www.cambridge.org/highereducation/books/an-introduction-to-decision-theory/93E043CC210347D7F3FE39665FD26C9F/decisions-under-ignorance/8D2AA3F1E63A72EE182D6AB527513732
    type: textbook
    accessed: 2026-11-15
  - id: s3
    title: "Descriptive, Normative, and Prescriptive Interactions in Decision Making"
    publisher: "Bell, Raiffa & Tversky, in Bell, Raiffa & Tversky (eds.), Decision Making: Descriptive, Normative, and Prescriptive Interactions, Cambridge University Press, 1988"
    url: https://cambridge.org/core/books/decision-making/descriptive-normative-and-prescriptive-interactions-in-decision-making/E9C320AB14791B3F586A583AA4989DD0
    type: textbook
    accessed: 2026-11-15
  - id: s4
    title: "Risk, Ambiguity, and the Savage Axioms"
    publisher: Quarterly Journal of Economics 75(4), 643-669 (Ellsberg, 1961), EconPapers record
    url: https://econpapers.repec.org/RePEc:oup:qjecon:v:75:y:1961:i:4:p:643-669.
    type: primary
    accessed: 2026-11-15
created: 2026-11-15
---

# Decision theory

Decision theory studies the reasoning behind an agent's choices. In the philosophical tradition it is as much a theory of beliefs, desires and preferences as a theory of action: it asks what constraints those attitudes must meet to count as rational, and how they should combine into a choice.[^s1] Its orthodox normative answer is expected utility theory. Under uncertainty, a rational agent should prefer the option with the highest expected value of desirability, judged by the agent's own probabilities and utilities.[^s1] Economists often read preference as nothing more than observed choice (revealed preference), while most philosophers treat a preference as a judgment that explains why someone chooses as they do.[^s1]

## Origin

The field grew from a few twentieth-century representation theorems. Frank Ramsey sketched, in 1926, how degrees of belief and cardinal utilities could be recovered from preferences over gambles, though without a complete proof.[^s1] John von Neumann and Oskar Morgenstern proved in 1944 that preferences over lotteries obeying completeness, transitivity, continuity and independence can be represented by an expected utility function.[^s1] Leonard Savage's *The Foundations of Statistics* (1954) went further: from preferences over acts, treated as functions from states of the world to outcomes, it derives both a probability function and a utility function, using axioms that include the sure-thing principle.[^s1] Richard Jeffrey's 1965 theory made propositions the objects of both belief and desire, which avoids Savage's assumption that acts and states are probabilistically independent.[^s1]

## How it works

A decision problem is modelled as a table: the options available, the possible states of the world, and the outcome each option produces in each state.[^s1] Theorists then distinguish decisions *under risk*, where probabilities can be assigned to the states, from decisions *under ignorance*, where the decision maker cannot assign any; textbooks sometimes call the latter decision under uncertainty.[^s2] Under risk, expected utility theory weights each outcome's utility by its probability and sums. Under ignorance, a family of rival rules competes for the job, and an introductory textbook surveys the most influential of them in a chapter of its own.[^s2]

*Workplace example.* A team lead must choose between a fixed-price and a usage-based software contract. The states are next year's usage (low, medium, high). If the team can estimate how likely each level is, decision theory says to assign utilities to the costs in each cell and choose the contract with the higher expected utility. If they cannot, the problem is one of ignorance, and the choice of decision rule itself becomes the question.[^s1][^s2] The axioms also act as consistency checks: a manager who prefers vendor A to B, B to C and C to A could be led through a series of trades that loses money for certain, which is the money-pump argument for transitivity.[^s1]

## Normative, descriptive and prescriptive

Bell, Raiffa and Tversky (1988) separated three questions. Normative theory says how decisions ought to be made; descriptive theory reports how people actually make them; prescriptive work asks how real people, with limited time and attention, can choose better.[^s3] Decision theory in the narrow sense is the normative member of that trio. Judgment and decision-making research supplies the descriptive side, and decision analysis supplies the prescriptive tools.[^s3]

## Evidence and limitations

The normative core is contested on several fronts. Maurice Allais (1953) found common preferences that violate the independence axiom, and later regret-based accounts try to explain them.[^s1] Daniel Ellsberg (1961) asked whether some uncertainties are not risks at all, opening a literature on ambiguity.[^s4] One response is imprecise probabilism, which represents beliefs as a set of probability functions and offers rules such as maximin expected utility, which picks the option whose worst expected utility is highest.[^s1] Further open problems include how to reason about states one has not even thought of (unawareness), whether catastrophic risks call for a precautionary rule rather than expected utility, and how to choose across a sequence of decisions when one's preferences may change, as in the story of Ulysses and the sirens.[^s1] Critics also argue the theory can be too permissive, since an apparent violation can often be redescribed as consistent by redefining the outcomes.[^s1]

## Connections

Decision theory is **formalized by** von Neumann and Morgenstern's *Theory of Games and Economic Behavior*, whose theorem gave expected utility its axiomatic footing.[^s1] It is **influenced by** probability theory: Bayesian decision theory ties rational preference to probabilism.[^s1] It is **challenged by** the Allais paradox, the best-known counterexample to the independence axiom.[^s1] It **contrasts with** judgment and decision making, the descriptive study of actual choice.[^s3] It is **applied in** economics and policy analysis, where expected utility models are used even for catastrophic risks such as climate change, a practice its critics question.[^s1] Expected utility theory, risk aversion and decision analysis sit beneath it as theory, concept and applied method.[^s1][^s3]

## Sources

[^s1]: Stefánsson (earlier versions with Steele), "Decision Theory", Stanford Encyclopedia of Philosophy (rev. 2025). https://plato.stanford.edu/ENTRiES/decision-theory/ (accessed 2026-11-15)
[^s2]: Peterson, An Introduction to Decision Theory, 2nd ed., ch. 3 "Decisions under Ignorance", Cambridge University Press, 2017. https://www.cambridge.org/highereducation/books/an-introduction-to-decision-theory/93E043CC210347D7F3FE39665FD26C9F/decisions-under-ignorance/8D2AA3F1E63A72EE182D6AB527513732 (accessed 2026-11-15)
[^s3]: Bell, Raiffa & Tversky, "Descriptive, Normative, and Prescriptive Interactions in Decision Making", Cambridge University Press, 1988. https://cambridge.org/core/books/decision-making/descriptive-normative-and-prescriptive-interactions-in-decision-making/E9C320AB14791B3F586A583AA4989DD0 (accessed 2026-11-15)
[^s4]: Ellsberg, "Risk, Ambiguity, and the Savage Axioms", Quarterly Journal of Economics 75(4), 1961. https://econpapers.repec.org/RePEc:oup:qjecon:v:75:y:1961:i:4:p:643-669. (accessed 2026-11-15)
