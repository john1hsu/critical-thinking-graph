---
id: ct:cognitive-bias
type: Concept
title: Cognitive bias
aliases: [judgmental bias, bias in judgment, systematic judgment error]
domain: cognitive-biases
summary: >-
  A systematic and predictable tendency for human judgment to depart from a
  chosen normative standard (logic, probability theory, or accurate perception),
  so that errors lean in a consistent direction rather than scattering at random.
level: introductory
evidenceStatus: mixed
broader: [ct:judgment-and-decision-making]
related: [ct:heuristics-and-biases-program, ct:debiasing, ct:confirmation-bias, ct:anchoring-effect, ct:belief-bias, ct:overconfidence-effect, ct:bias-blind-spot, ct:representativeness-heuristic, ct:availability-heuristic, ct:informal-fallacy, ct:dual-process-theory]
requires: []
relations:
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: medium}
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: medium}
  - {predicate: explainedBy, object: ct:heuristics-and-biases-program, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:error-management-theory, source: s2, confidence: high}
  - {predicate: challengedBy, object: ct:gerd-gigerenzer, source: s3, confidence: high}
  - {predicate: supportedBy, object: ct:many-labs-1-replication-project, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Judgment under Uncertainty: Heuristics and Biases"
    publisher: "Science 185(4157), 1124-1131 (Amos Tversky & Daniel Kahneman, 1974), PubMed record"
    url: https://pubmed.ncbi.nlm.nih.gov/17835457/
    type: primary
    accessed: 2026-11-06
  - id: s2
    title: "The Paranoid Optimist: An Integrative Evolutionary Model of Cognitive Biases"
    publisher: "Personality and Social Psychology Review 10(1), 47-66 (Martie G. Haselton & Daniel Nettle, 2006), author's copy"
    url: https://www.danielnettle.org.uk/wp-content/uploads/2024/06/034.pdf
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s3
    title: "On Narrow Norms and Vague Heuristics: A Reply to Kahneman and Tversky (1996)"
    publisher: "Psychological Review 103(3), 592-596 (Gerd Gigerenzer, 1996), CORE copy"
    url: https://core.ac.uk/download/193648205.pdf
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s4
    title: "Investigating variation in replicability: A 'many labs' replication project"
    publisher: "Social Psychology 45(3), 142-152 (Richard A. Klein et al., 2014), Penn State research portal"
    url: https://pure.psu.edu/en/publications/investigating-variation-in-replicability-a-many-labs-replication-/
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s5
    title: "Data from Investigating Variation in Replicability: A 'Many Labs' Replication Project"
    publisher: "Journal of Open Psychology Data (Richard A. Klein et al., 2014), CORE copy"
    url: https://core.ac.uk/download/420823721.pdf
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s6
    title: "Many Labs 2: Investigating Variation in Replicability Across Samples and Settings"
    publisher: "Advances in Methods and Practices in Psychological Science (Richard A. Klein et al., 2018), University of Salford repository copy"
    url: https://salford-repository.worktribe.com/OutputFile/1490505
    type: peer-reviewed
    accessed: 2026-11-06
created: 2026-11-06
---

# Cognitive bias

A cognitive bias is a systematic, predictable tendency for judgment to depart from a normative standard such as logic, probability theory or an accurate reading of the world. What makes it a bias rather than mere error is direction: people do not just make mistakes, they make the same kind of mistake in the same direction across situations.[^s1] Haselton and Nettle give a compact working definition: a bias is a tendency to accept one belief on weaker evidence than would be needed to accept its alternative.[^s2] Individual biases such as anchoring, confirmation bias and overconfidence are all instances of this general idea, and critical thinking is largely the practice of noticing and correcting for them.

## Origin

The modern concept comes from Amos Tversky and Daniel Kahneman's 1974 *Science* article, "Judgment under Uncertainty: Heuristics and Biases".[^s1] They argued that people judging uncertain matters rely on a few shortcuts (representativeness, availability, and adjustment from an anchor) that are economical and usually effective but produce systematic and predictable errors; those predictable errors are the biases.[^s1] The paper framed biases as by-products of heuristics, not of motivation or ignorance, and suggested that understanding the shortcuts could improve judgments and decisions.[^s1]

## How it works

A bias always has three ingredients: a judgment, a standard it is measured against, and a consistent gap between them.[^s1] Consider a workplace example. A manager reviewing a project estimate sees the vendor's opening figure of 400 hours before forming a view. Her own estimate lands at 360 hours; a colleague who saw an opening figure of 150 hours lands at 190. Each adjusted away from the number they saw, but not far enough, so both estimates lean toward an arbitrary starting point. No single estimate proves a bias; the bias shows up in the pattern across people and occasions, which is why the concept is defined statistically.[^s1]

Explanations differ about *why* the gap is systematic. In the heuristics-and-biases tradition, biases are side effects of simple rules that work well in many settings but misfire in others.[^s2] Error management theory, proposed by Haselton and colleagues, adds that when the costs of false alarms and misses were unequal over evolutionary history, selection should favour leaning toward the cheaper error.[^s2] On that view some biases are design features, not defects: like a smoke detector tuned to sound too often rather than miss a fire, people hear rising sounds as closer than equivalent falling sounds, since bracing too early costs less than bracing too late.[^s2]

## How to spot it

Ask what standard the judgment is being measured against and whether the deviation is consistent. Useful signals are a judgment that shifts with irrelevant features of how the question was posed, errors that all lean one way across a team or over time, and confidence that stays high when feedback says otherwise.[^s1] Because the definition depends on the norm, also ask whether that norm fits the situation; a response that breaks a probability rule may be sensible given how ordinary language uses words such as "probable" and "and".[^s3]

## Evidence and limitations

Large replication projects show that many classic judgment effects are real. Many Labs 1 (2014) tested 13 effects across 36 samples and 6,344 participants; ten replicated consistently, and the two clear failures were priming effects, not judgment biases.[^s4] The tested set included sunk costs, gain-versus-loss framing, anchoring and the retrospective gambler's fallacy.[^s5] The broader picture is less tidy. Many Labs 2 (2018) found that only about half of 28 effects replicated, with median effect sizes shrinking from d = 0.60 in the originals to d = 0.15, and a Tversky and Kahneman framing effect that replicated at less than half its original size.[^s6] Effect sizes for individual biases therefore need checking one by one.

The concept also faces a theoretical challenge. Gerd Gigerenzer argued in 1996 that the norms used to declare errors are narrow and content-blind, and that one-word heuristics explain too little and too much because they can be fitted to almost any result after the fact.[^s3] He called for precise process models that predict when an apparent bias appears and when it disappears.[^s3] Haselton and Nettle likewise note concern that the field's focus on error can make human judgment look worse than it is.[^s2]

## Connections

- **Broader: judgment and decision making.** Biases are the central object of study in research on how people judge under uncertainty, which grew from Tversky and Kahneman's work.[^s1]
- **Introduced by Amos Tversky and Daniel Kahneman,** whose 1974 article named heuristics and the systematic errors they produce.[^s1]
- **Explained by the heuristics-and-biases program,** which treats biases as by-products of efficient mental shortcuts such as representativeness and availability.[^s1]
- **Explained by error management theory,** which accounts for some biases as adaptive responses to asymmetric error costs.[^s2]
- **Challenged by Gerd Gigerenzer,** whose critique targets the narrow norms and vague heuristics behind many bias claims.[^s3]
- **Supported by the Many Labs 1 replication project,** in which most classic judgment effects replicated across dozens of samples, though later projects show shrinking effect sizes.[^s4][^s6]
- **Related to debiasing, the bias blind spot and specific biases** such as anchoring, confirmation bias, belief bias and overconfidence, all of which are instances of the general pattern or remedies for it.[^s1][^s2]

## Sources

[^s1]: A. Tversky & D. Kahneman, "Judgment under Uncertainty: Heuristics and Biases", *Science* 185(4157), 1974, 1124–1131. https://pubmed.ncbi.nlm.nih.gov/17835457/ (accessed 2026-11-06)
[^s2]: M. G. Haselton & D. Nettle, "The Paranoid Optimist: An Integrative Evolutionary Model of Cognitive Biases", *Personality and Social Psychology Review* 10(1), 2006, 47–66. https://www.danielnettle.org.uk/wp-content/uploads/2024/06/034.pdf (accessed 2026-11-06)
[^s3]: G. Gigerenzer, "On Narrow Norms and Vague Heuristics: A Reply to Kahneman and Tversky (1996)", *Psychological Review* 103(3), 1996, 592–596. https://core.ac.uk/download/193648205.pdf (accessed 2026-11-06)
[^s4]: R. A. Klein et al., "Investigating variation in replicability: A 'many labs' replication project", *Social Psychology* 45(3), 2014, 142–152. https://pure.psu.edu/en/publications/investigating-variation-in-replicability-a-many-labs-replication-/ (accessed 2026-11-06)
[^s5]: R. A. Klein et al., "Data from Investigating Variation in Replicability: A 'Many Labs' Replication Project", *Journal of Open Psychology Data*, 2014. https://core.ac.uk/download/420823721.pdf (accessed 2026-11-06)
[^s6]: R. A. Klein et al., "Many Labs 2: Investigating Variation in Replicability Across Samples and Settings", *Advances in Methods and Practices in Psychological Science*, 2018. https://salford-repository.worktribe.com/OutputFile/1490505 (accessed 2026-11-06)
