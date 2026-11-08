---
id: ct:hindsight-bias
type: CognitiveBias
title: Hindsight bias
aliases: [knew-it-all-along effect, creeping determinism]
domain: cognitive-biases
summary: >-
  The tendency, once an outcome is known, to judge it as having been more
  predictable, more inevitable and more obvious beforehand than it actually
  was, and to misremember one's earlier predictions as closer to the outcome.
level: introductory
evidenceStatus: robust
broader: [ct:cognitive-bias]
related: [ct:premortem, ct:overconfidence-effect, ct:calibration, ct:debiasing, ct:bias-blind-spot]
requires: []
relations:
  - {predicate: introducedBy, object: ct:baruch-fischhoff, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:fischhoff-1975-hindsight-experiments, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:raft-model, source: s3, confidence: medium}
  - {predicate: explainedBy, object: ct:processing-fluency, source: s2, confidence: medium}
  - {predicate: amplifies, object: ct:overconfidence-effect, source: s2, confidence: medium}
  - {predicate: supportedBy, object: ct:chen-2021-hindsight-bias-replications, source: s5, confidence: medium}
  - {predicate: challengedBy, object: ct:seda-2025-hindsight-bias-replication, source: s4, confidence: low}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s2, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Hindsight Bias: On Being Wise After the Event"
    publisher: "Social Cognition 25(1), 1-9 (Blank, Musch & Pohl, 2007), copy hosted by Jagiellonian University"
    url: https://iphils.uj.edu.pl/~a.trybus/classes/logic/cs/20.Pohl.Hindsight.Bias.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s2
    title: "Hindsight Bias"
    publisher: "Perspectives on Psychological Science 7(5), 411-426 (Roese & Vohs, 2012), doi:10.1177/1745691612454303, copy hosted by the University of Minnesota"
    url: https://carlsonschool.umn.edu/sites/carlsonschool.umn.edu/files/2026-01/vohs-et-al-2012-hindsight-bias.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s3
    title: "Hindsight bias: How knowledge and heuristics affect our reconstruction of the past"
    publisher: "Memory 11(4/5), 357-377 (Hertwig, Fanselow & Hoffrage, 2003), Max Planck Society repository"
    url: https://pure.mpg.de/pubman/item/item_2101638_6/component/file_2101637/RH_Hindsight_2003.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s4
    title: "Hindsight is not equal to foresight (Fischhoff, 1975): replication record"
    publisher: FORRT Replication Atlas
    url: https://forrt.org/flora-replication-atlas/doi/10.1037/0096-1523.1.3.288/
    type: community
    accessed: 2026-11-08
  - id: s5
    title: "Considering Alternative Outcomes of Research: Does Knowing the Actual Outcome Create Bias?"
    publisher: "Proceedings of the Annual Meeting of the Cognitive Science Society 45, 3187-3193 (Munnich et al., 2023), eScholarship, University of California"
    url: https://escholarship.org/content/qt4w1069qh/qt4w1069qh.pdf?t=rxyb4b
    type: peer-reviewed
    accessed: 2026-11-08
created: 2026-11-08
---

# Hindsight bias

Hindsight bias is the "I knew it all along" effect: after learning how something turned out, people judge that outcome as having been more predictable than it really was, and they recall their own earlier forecasts as closer to the result than they were.[^s2][^s1] Roese and Vohs, reviewing a literature of more than 800 papers, describe it as operating at three partly separable levels: memory distortion (misremembering what you predicted), inevitability (feeling the outcome had to happen) and foreseeability (feeling you personally could have seen it coming).[^s2]

## Origin

Baruch Fischhoff introduced the experimental study of the bias in 1975 with "Hindsight ≠ foresight" in the *Journal of Experimental Psychology: Human Perception and Performance*.[^s1][^s4] He gave people short accounts of historical, political and clinical cases. Those told that a particular outcome had occurred rated it as more likely than people who read the same account without an outcome, and the effect persisted when participants were told to ignore what they knew or to answer as someone who did not know it. Fischhoff called this "creeping determinism".[^s1] In the same year Fischhoff and Beyth showed the memory version: people asked to recall their earlier predictions about President Nixon's 1972 visits to China and the USSR remembered them as closer to what actually happened.[^s1]

## How it works

Several processes contribute and no single theory covers every finding.[^s1] On the cognitive side, outcome knowledge is folded into what we know, so when we try to reconstruct an earlier judgment we rebuild it from knowledge that already contains the answer. Hertwig, Fanselow and Hoffrage modelled this as RAFT (Reconstruction After Feedback with Take The Best): feedback fills in missing facts, which then tilt the reconstructed judgment toward the outcome.[^s3] People also build a tidy causal story around the outcome, and the ease with which that story comes to mind, its processing fluency, is mistaken for evidence that the outcome was obvious.[^s2] Motivation adds to this: the need for a predictable, controllable world, and the wish to look and feel competent.[^s2][^s1]

A workplace example: a team launches a product and it fails because a competitor cut prices. In the retrospective, the price cut seems to have been obvious. People remember having been more doubtful than they were, early warning signs that were one item among dozens now look decisive, and the project lead is blamed for missing what "everyone could see". Roese and Vohs give the same pattern for a manager blamed for a bad hire because of warning signs that only stood out after the fact.[^s2]

## Evidence

The basic effect is among the most often reproduced in judgment research and appears in memory designs (recalling one's own earlier estimate) and hypothetical designs (estimating what an uninformed person would have predicted).[^s1][^s2] It has been studied in medical diagnosis, jury and liability decisions, auditing, investing, elections and sport.[^s1][^s2] A 1991 meta-analysis of 128 studies by Christensen-Szalanski and Willham found that people more familiar with a task showed less bias (corrected r = 0.42 for the expertise effect), but a later 2004 meta-analysis by Guilbault and colleagues found no such relation, so the role of expertise is unsettled.[^s3][^s2]

Direct replications of the founding experiment are mostly but not entirely positive. Chen and colleagues (2021, *Journal of Experimental Social Psychology*) replicated Fischhoff's Experiment 2 with 890 participants and found retrospective hindsight bias with a mean effect of about d = 0.60, and also replicated Slovic and Fischhoff's (1977) related study.[^s4][^s5] Two smaller Brazilian projects, a 2024 thesis and a 2025 preregistered preprint by Seda and colleagues, did not reproduce the original difference.[^s4] Hertwig and colleagues add a caution about framing: the bias may be a by-product of a memory system that efficiently updates knowledge, since most updated information in their simulations was correct.[^s3]

## How to spot it

- You or others say an outcome was "obvious" or "inevitable" but nobody wrote that prediction down beforehand.[^s2]
- A review settles quickly on one cause, often one person to blame, and stops considering others.[^s2]
- Your memory of what you expected matches the result unusually well.[^s1]
- Decisions are graded by how they turned out rather than by what was knowable when they were made.[^s2]

## How to counter it

Warnings and instructions to ignore the outcome do little.[^s1] What works better is asking people to explain how other outcomes could have happened. Roese and Vohs report that this consider-the-opposite strategy reduces but does not remove the bias, and that two or three alternatives are best, since struggling to list many can backfire by making the alternatives feel implausible.[^s2] Write predictions and their reasons down before outcomes are known, so later reviews compare against a record instead of memory.[^s2] In post-incident reviews, judge decisions against the information available at the time.[^s2] Reducing the bias substantially usually takes considerable effort.[^s1]

## Connections

- **Introduced by** Baruch Fischhoff and **demonstrated by** his 1975 outcome-knowledge experiments.[^s1]
- **Explained by** the RAFT model of knowledge updating and reconstruction.[^s3]
- **Explained by** processing fluency, the ease of making sense of the known outcome.[^s2]
- **Amplifies** the overconfidence effect: believing you saw the past coming makes you overconfident about predicting the future and less inclined to learn from it.[^s2][^s1]
- **Supported by** Chen and colleagues' 2021 replications and **challenged by** the 2025 Seda preregistered replication.[^s4][^s5]
- **Studied in** judgment and decision making, where Roese and Vohs place it among the best-known decision biases.[^s2]
- **Related to** debiasing and calibration, since the bias distorts the feedback people use to judge how good their forecasts were, and to the premortem, which asks a team to explain a failure before it happens.[^s2][^s1]

## Sources

[^s1]: Blank, Musch & Pohl, "Hindsight Bias: On Being Wise After the Event", *Social Cognition* 25 (2007). https://iphils.uj.edu.pl/~a.trybus/classes/logic/cs/20.Pohl.Hindsight.Bias.pdf (accessed 2026-11-08)
[^s2]: Roese & Vohs, "Hindsight Bias", *Perspectives on Psychological Science* 7 (2012). https://carlsonschool.umn.edu/sites/carlsonschool.umn.edu/files/2026-01/vohs-et-al-2012-hindsight-bias.pdf (accessed 2026-11-08)
[^s3]: Hertwig, Fanselow & Hoffrage, "Hindsight bias: How knowledge and heuristics affect our reconstruction of the past", *Memory* 11 (2003). https://pure.mpg.de/pubman/item/item_2101638_6/component/file_2101637/RH_Hindsight_2003.pdf (accessed 2026-11-08)
[^s4]: FORRT Replication Atlas, record for Fischhoff (1975). https://forrt.org/flora-replication-atlas/doi/10.1037/0096-1523.1.3.288/ (accessed 2026-11-08)
[^s5]: Munnich et al., "Considering Alternative Outcomes of Research: Does Knowing the Actual Outcome Create Bias?", *Proceedings of the Cognitive Science Society* 45 (2023). https://escholarship.org/content/qt4w1069qh/qt4w1069qh.pdf?t=rxyb4b (accessed 2026-11-08)
