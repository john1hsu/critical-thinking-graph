---
id: ct:status-quo-bias
type: CognitiveBias
title: Status quo bias
aliases: [status-quo effect, preference for the status quo]
domain: cognitive-biases
summary: >-
  The tendency to prefer the current state of affairs, such as an existing
  plan, a previous choice or a pre-set default, more often than its merits
  alone would justify.
level: introductory
evidenceStatus: mixed
broader: [ct:cognitive-bias]
related: [ct:endowment-effect, ct:sunk-cost-fallacy, ct:choice-architecture, ct:behavioral-economics, ct:judgment-and-decision-making]
requires: []
relations:
  - {predicate: introducedBy, object: ct:william-samuelson, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:richard-zeckhauser, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:samuelson-zeckhauser-1988-status-quo-experiments, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:loss-aversion, source: s2, confidence: medium}
  - {predicate: supportedBy, object: ct:xiao-2021-status-quo-bias-replication, source: s3, confidence: high}
  - {predicate: supportedBy, object: ct:jachimowicz-2019-default-effects-meta-analysis, source: s4, confidence: medium}
  - {predicate: contrastsWith, object: ct:endowment-effect, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Status Quo Bias in Decision Making"
    publisher: Journal of Risk and Uncertainty 1(1), 7-59 (Samuelson & Zeckhauser, 1988), RePEc/IDEAS record
    url: https://ideas.repec.org/a/kap/jrisku/v1y1988i1p7-59.html
    type: primary
    accessed: 2026-11-12
  - id: s2
    title: "Anomalies: The Endowment Effect, Loss Aversion, and Status Quo Bias"
    publisher: Journal of Economic Perspectives 5(1), 193-206 (Kahneman, Knetsch & Thaler, 1991), copy hosted by Fermat's Library
    url: https://www.fermatslibrary.com/s/the-endowment-effect-loss-aversion-and-status-quo-bias
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "Revisiting status quo bias: Replication of Samuelson and Zeckhauser (1988)"
    publisher: Meta-Psychology 5 (Xiao, Lam, Piara & Feldman, 2021)
    url: https://open.lnu.se/index.php/metapsychology/article/view/2470
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "When and why defaults influence decisions: a meta-analysis of default effects"
    publisher: Behavioural Public Policy 3(2), 159-186 (Jachimowicz, Duncan, Weber & Johnson, 2019), Cambridge University Press
    url: https://core-prod.cambridgecore.org/core/product/67AF6972CFB52698A60B6BD94B70C2C0/core-reader
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Status quo bias

Status quo bias is the tendency to stick with the current state of affairs (doing nothing, keeping an earlier decision, or accepting whatever option is already in place) more often than a neutral comparison of the options would predict.[^s1] Textbook decision models treat every option on equal terms, yet real choices nearly always come with an incumbent option, and that incumbency itself pulls people toward it.[^s1][^s2]

## Origin

Economists William Samuelson and Richard Zeckhauser named and tested the bias in a 1988 paper in the first issue of the *Journal of Risk and Uncertainty*. They combined questionnaire experiments with field data on how university faculty chose health plans and retirement programmes, and argued that the bias also shows up in consequential real decisions.[^s1] In 1991 Daniel Kahneman, Jack Knetsch and Richard Thaler grouped it with the endowment effect as anomalies that loss aversion could explain.[^s2]

## How it works

Samuelson and Zeckhauser gave people the same decision problem in two framings. In a neutral version, all options were simply listed; in a status quo version, one option was described as the one already in place, for example a portfolio a person had inherited. The option labelled as the status quo was chosen noticeably more often than when it appeared in the neutral list, and Kahneman, Knetsch and Thaler noted that its advantage grew as the number of alternatives rose.[^s3][^s2]

Field data point the same way. In a study of California electricity customers summarised by Kahneman, Knetsch and Thaler, about 60% of customers with highly reliable service and about 58% of those with less reliable service ranked their own current arrangement first. Few in either group wanted to switch, even for a 30% change in price.[^s2] When two US states set opposite default car-insurance policies, most drivers in each kept whichever policy came pre-selected.[^s2]

A workplace example: a team renewing a software contract compares its current vendor with two rivals. If the rivals' quotes are run against "what we have now", the incumbent's flaws feel tolerable and the switching risks feel large. The same three products rated fresh, with no incumbent, might rank differently, which is the contrast the original neutral-versus-status-quo design was built to expose.[^s1][^s3]

## Evidence

A 2021 preregistered replication with two online samples of about 310 US adults each re-ran four of the original scenarios. Status quo bias reappeared in the budget-allocation, investment and job-choice problems, at sizes comparable to or larger than the original, but largely vanished in a problem about choosing a car colour.[^s3] The authors noted that the original study had low statistical power, judged that the failure did not overturn the bias, and advised against calling it pervasive.[^s3] They also cautioned that their participants only read a framing: no one had actually made the earlier choice.[^s3]

Defaults are the most studied real-world form. A 2019 meta-analysis of 58 datasets (about 74,000 participants) found a medium-to-large average default effect, around d = 0.68, but extremely high heterogeneity. Effects were larger in consumer decisions, smaller in environmental ones, and larger when a default could be read as a recommendation or as something already owned.[^s4] Because the size of the bias depends so much on domain and framing, this article rates the evidence as mixed rather than robust.[^s3][^s4]

Several explanations compete. Kahneman, Knetsch and Thaler argued that losses weigh roughly twice as much as equal gains, so leaving the reference point makes a change's downsides loom larger than its upsides.[^s2] The replication team also reviewed rational accounts (switching costs, uncertainty), regret and omission bias, mere familiarity, and the urge to justify past choices. They argued that rational costs alone cannot explain the effect, since the original problems removed them.[^s3]

## How to spot it

- The current option wins mainly because it is current, and nobody can say what it would have to lose on to be replaced.[^s1][^s3]
- Alternatives are judged by their risks while the incumbent's known costs go unexamined.[^s2]
- A pre-set default is accepted with no sign that anyone compared it with the other options.[^s4]

## How to counter it

Re-run the choice in neutral form: list every option, including the current one, without labelling which is incumbent, and score them on the same criteria.[^s1][^s3] Ask the reversal question: if we were already on the alternative, would we pay to switch to what we have now? Since default effects are larger when a default reads as an endorsement, say openly why a default was chosen and who set it.[^s4] Keep in mind that sticking with the status quo is sometimes right. Real switching costs and uncertainty are legitimate reasons, so the aim is to count them explicitly rather than let incumbency stand in for them.[^s1][^s3]

## Connections

- **Introduced by** William Samuelson and Richard Zeckhauser, whose 1988 paper named the bias.[^s1]
- **Demonstrated by** their 1988 questionnaire experiments with neutral and status-quo framings, which included field data on faculty health and retirement plans.[^s1]
- **Explained by** loss aversion, the account Kahneman, Knetsch and Thaler gave in 1991.[^s2]
- **Contrasts with** the endowment effect: both rest on loss aversion, but the endowment effect is about valuing objects you own, while status quo bias is about preferring the current option over a change.[^s2]
- **Supported by** Xiao and colleagues' 2021 replication and by Jachimowicz and colleagues' 2019 meta-analysis of default effects, a central case of the bias in choice architecture.[^s3][^s4]
- **Related to** the sunk cost fallacy: the replication's discussion of people defending past choices they regard as their own describes a similar pull toward earlier commitments.[^s3]

## Sources

[^s1]: Samuelson & Zeckhauser, "Status Quo Bias in Decision Making", *Journal of Risk and Uncertainty* 1 (1988). https://ideas.repec.org/a/kap/jrisku/v1y1988i1p7-59.html (accessed 2026-11-12)
[^s2]: Kahneman, Knetsch & Thaler, "Anomalies: The Endowment Effect, Loss Aversion, and Status Quo Bias", *Journal of Economic Perspectives* 5 (1991). https://www.fermatslibrary.com/s/the-endowment-effect-loss-aversion-and-status-quo-bias (accessed 2026-11-12)
[^s3]: Xiao, Lam, Piara & Feldman, "Revisiting status quo bias: Replication of Samuelson and Zeckhauser (1988)", *Meta-Psychology* 5 (2021). https://open.lnu.se/index.php/metapsychology/article/view/2470 (accessed 2026-11-12)
[^s4]: Jachimowicz, Duncan, Weber & Johnson, "When and why defaults influence decisions: a meta-analysis of default effects", *Behavioural Public Policy* 3 (2019). https://core-prod.cambridgecore.org/core/product/67AF6972CFB52698A60B6BD94B70C2C0/core-reader (accessed 2026-11-12)
