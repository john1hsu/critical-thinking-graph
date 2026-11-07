---
id: ct:statistical-reasoning-training
type: Technique
title: Statistical reasoning training
aliases: [statistical rule training, formal rule training, training in statistical rules, set-inclusion training]
domain: debiasing-and-metacognition
summary: >-
  A debiasing technique that teaches abstract statistical and probability rules,
  such as the law of large numbers and the rule that a conjunction can be no
  more likely than its parts, with worked examples, so that people apply them
  to everyday judgments. Short training reduces errors such as the conjunction
  fallacy and sample-size neglect, but rarely eliminates them.
level: intermediate
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:natural-frequencies, ct:logical-necessity-instructions, ct:debiasing-training-games, ct:base-rate-neglect, ct:dual-process-theory]
requires: [ct:conjunction-fallacy]
relations:
  - {predicate: counteracts, object: ct:conjunction-fallacy, source: s2, confidence: high}
  - {predicate: counteracts, object: ct:representativeness-heuristic, source: s3, confidence: medium}
  - {predicate: counteracts, object: ct:insensitivity-to-sample-size, source: s1, confidence: medium}
  - {predicate: demonstratedBy, object: ct:fong-krantz-nisbett-1986-statistical-training-study, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:agnoli-krantz-1989-conjunction-training-study, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:truong-2022-conjunction-training-replication, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "The effects of statistical training on thinking about everyday problems"
    publisher: Cognitive Psychology 18(3), 253-292 (Fong, Krantz & Nisbett, 1986), University of Michigan Deep Blue copy
    url: https://deepblue.lib.umich.edu/bitstream/handle/2027.42/26118/0000194.pdf;sequence=1
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s2
    title: "Suppressing natural heuristics by formal instruction: The case of the conjunction fallacy"
    publisher: Cognitive Psychology 21(4), 515-550 (Agnoli & Krantz, 1989), CAUSEweb literature record
    url: https://causeweb.org/cause/node/5355
    type: primary
    accessed: 2026-11-07
  - id: s3
    title: "The conjunction fallacy: The case for the existence of competing heuristic strategies"
    publisher: British Journal of Psychology 88(1), 1-27 (Fisk & Pidgeon, 1997), Cardiff University ORCA
    url: https://orca.cardiff.ac.uk/id/eprint/34385/
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s4
    title: "Transfer Success on the Linda Problem: A Re-Examination Using Dual Process Theory, Learning Material Characteristics, and Individual Differences"
    publisher: York University master's thesis (Truong, 2022), YorkSpace repository
    url: https://yorkspace.library.yorku.ca/xmlui/bitstream/10315/40957/2/Truong_Michael_S_2022_Masters.pdf
    type: academic
    accessed: 2026-11-07
created: 2026-11-07
---

# Statistical reasoning training

Statistical reasoning training is the deliberate teaching of abstract inferential rules (the law of large numbers, regression, and the inclusion rule that "A and B" can never be likelier than "A") together with worked examples, so that people recognise when those rules apply to ordinary judgments. It rests on the claim that people already hold rough intuitive versions of these rules and that instruction can sharpen them, rather than having to build domain-specific habits one setting at a time.[^s1] It is one of the few debiasing approaches with direct experimental evidence against the conjunction fallacy.[^s2]

## Origin

The approach grew out of Richard Nisbett's group at the University of Michigan in the 1980s. Fong, Krantz and Nisbett (1986) defended a "formalist" view: people reason partly with content-free rules, so changing the rule should change reasoning across many topics.[^s1] David Krantz then extended the idea from sample size to probability. Agnoli and Krantz (1989) asked whether "intensional" heuristics, judging by resemblance, could be suppressed when an alternative, extensional strategy based on set inclusion was taught, using the Linda problem and similar items.[^s2][^s4]

## How it works

Training pairs a short statement of the rule with concrete demonstrations. In Fong et al.'s 25-minute version, participants read four pages on sampling and watched samples of 1, 4 and 25 drawn from an urn of coloured gumballs, worked through three example problems, or did both.[^s1] For the conjunction rule, trainees learn to treat each description as a set of cases and to notice that "bank teller who is active in the feminist movement" is a subset of "bank teller".[^s2][^s4]

A workplace example: a project lead is asked which is likelier, "the vendor misses the deadline" or "the vendor misses the deadline because its key engineer leaves". The second story is vivid, but a trained reasoner pictures 100 similar projects, counts every late delivery, and sees that the engineer-departure cases are only some of them. The detailed story cannot be the likelier one.[^s2][^s4] The same trainee, told that a new hire's first week of sales beat the team average, recalls the law of large numbers: one week is a small sample and next week will probably regress.[^s1]

## How to apply it

1. **Name the rule and the structure.** Teach the rule abstractly and show the problem shapes it governs (small samples, nested categories).[^s1]
2. **Add varied examples.** Rule plus examples outperformed either alone, and examples from one domain helped others.[^s1]
3. **Prompt use at the point of decision.** Effects are much larger when people are told to apply what they learned; a reminder or checklist ("is one option a subset of the other?") does this job.[^s4]
4. **Revisit it.** Gains measured soon after training may fade, so revisit the rule rather than relying on one session.[^s1][^s4]

Pitfalls: training improves the frequency and quality of statistical answers but leaves many errors in place, and rule recitation without structure recognition does little.[^s3][^s4]

## Evidence and limitations

In Fong et al.'s first experiment (347 adults and high-school students), statistical answers rose from 42% in controls to 64% with full training; a demand-only control that merely named the law changed little (44%).[^s1] Their fourth study phoned students in an introductory statistics course under the guise of a sports poll: on a regression question, statistical answers rose from 16% at the start of term to 37% at the end, though two other questions showed no change.[^s1] For the conjunction fallacy, Agnoli and Krantz's trainees erred on roughly 44% of problems versus about 73% for controls.[^s4] Fisk and Pidgeon (1997) found that teaching the extension rule cut errors while teaching similarity-based judgment raised them, yet judgments still tracked the less likely component event, suggesting training shifts a compromise rather than replacing the heuristic.[^s3] A 2022 online conceptual replication with 453 analysed participants found error rates of 84% for controls, 59–65% after training with no prompt, and 41–44% when told to apply it; diagrams did not clearly help.[^s4] The record is consistent on direction but shows large residual error, strong dependence on prompts and short test delays, and few long-term follow-ups, so the evidence is rated mixed.[^s1][^s4]

## Connections

- **Broader: debiasing.** It is a form of debiasing by instruction that targets probabilistic errors.[^s2]
- **Requires the conjunction fallacy.** The training is defined against that error, so understanding the error comes first.[^s2]
- **Counteracts the conjunction fallacy.** Set-inclusion instruction reduced conjunction errors on Linda-type problems.[^s2][^s4]
- **Counteracts the representativeness heuristic.** Extension-rule training reduced similarity-driven errors, while similarity training increased them.[^s3]
- **Counteracts insensitivity to sample size.** Law-of-large-numbers training increased attention to sample size in everyday problems.[^s1]
- **Demonstrated by Fong, Krantz and Nisbett (1986) and Agnoli and Krantz (1989),** the founding experiments for sample-size and conjunction training respectively.[^s1][^s2]
- **Supported by Truong (2022),** a conceptual replication that found transfer even without an explicit prompt, though smaller.[^s4]
- **Related to natural frequencies, logical necessity instructions, debiasing training games, base-rate neglect and dual-process theory.** Frequency framing is the companion representational fix, necessity instructions are the deductive analogue, games are a newer training format, base rates are another rule-governed error, and dual-process accounts frame why instruction must override an intuitive answer.[^s4][^s1]

## Sources

[^s1]: G. T. Fong, D. H. Krantz & R. E. Nisbett, "The effects of statistical training on thinking about everyday problems", *Cognitive Psychology* 18(3), 1986, 253–292. https://deepblue.lib.umich.edu/bitstream/handle/2027.42/26118/0000194.pdf;sequence=1 (accessed 2026-11-07)
[^s2]: F. Agnoli & D. H. Krantz, "Suppressing natural heuristics by formal instruction: The case of the conjunction fallacy", *Cognitive Psychology* 21(4), 1989, 515–550. https://causeweb.org/cause/node/5355 (accessed 2026-11-07)
[^s3]: J. E. Fisk & N. F. Pidgeon, "The conjunction fallacy: The case for the existence of competing heuristic strategies", *British Journal of Psychology* 88(1), 1997, 1–27. https://orca.cardiff.ac.uk/id/eprint/34385/ (accessed 2026-11-07)
[^s4]: M. S. Truong, "Transfer Success on the Linda Problem: A Re-Examination Using Dual Process Theory, Learning Material Characteristics, and Individual Differences", master's thesis, York University, 2022. https://yorkspace.library.yorku.ca/xmlui/bitstream/10315/40957/2/Truong_Michael_S_2022_Masters.pdf (accessed 2026-11-07)
