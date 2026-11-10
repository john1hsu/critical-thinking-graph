---
id: ct:cost-benefit-reasoning-training
type: Technique
title: Cost-benefit reasoning training
aliases: [economic reasoning training, sunk cost principle training, cost-benefit rule training, training in economic choice rules]
domain: debiasing-and-metacognition
summary: >-
  A debiasing technique that explicitly teaches the cost-benefit rules of
  microeconomics, chiefly that unrecoverable past costs should be ignored and
  that forgone alternatives count as costs, with varied worked examples, so that
  people apply them to everyday choices. Targeted rule training reduces sunk cost
  reasoning in experiments, while general economics coursework shows little effect.
level: intermediate
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:statistical-reasoning-training, ct:transfer-of-learning, ct:escalation-of-commitment, ct:debiasing-training-games, ct:behavioral-economics]
requires: [ct:sunk-cost-fallacy]
relations:
  - {predicate: counteracts, object: ct:sunk-cost-fallacy, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:opportunity-cost-neglect, source: s3, confidence: medium}
  - {predicate: demonstratedBy, object: ct:larrick-morgan-nisbett-1990-cost-benefit-training-study, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:bishop-feltz-conway-critical-thinking-class-field-experiment, source: s3, confidence: medium}
  - {predicate: challengedBy, object: ct:arkes-blumer-1985-sunk-cost-experiments, source: s2, confidence: medium}
  - {predicate: challengedBy, object: ct:roth-2015-sunk-cost-meta-analysis, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Teaching the use of cost-benefit reasoning in everyday life"
    publisher: Psychological Science 1(6), 362-370 (Larrick, Morgan & Nisbett, 1990), copy hosted by Gwern.net
    url: https://Www.Gwern.net/doc/psychology/cognitive-bias/sunk-cost/1990-larrick.pdf
    type: primary
    accessed: 2026-11-10
  - id: s2
    title: "The psychology of sunk cost"
    publisher: Organizational Behavior and Human Decision Processes 35(1), 124-140 (Arkes & Blumer, 1985), copy hosted by University of Klagenfurt
    url: https://cognition.aau.at/bg/BA/Arkes%20%26%20Blumer%201985.pdf
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "Critical thinking classes can reduce common biases: results from a field experiment"
    publisher: Journal of Applied Psychology (Bishop, Feltz & Conway, 2026), accepted manuscript at University of Southampton ePrints
    url: https://eprints.soton.ac.uk/510148/1/Bishop_et_al_2026_Critical_Thinking_Classes_Can_Debias_Reasoning_JAP_Preprint.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s4
    title: "On the sunk-cost effect in economic decision-making: a meta-analytic review"
    publisher: Business Research 8, 99-138 (Roth, Robbert & Straus, 2015), Springer
    url: https://link.springer.com/article/10.1007/s40685-014-0014-8
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s5
    title: "Does learning economics make you less susceptible to the sunk cost fallacy?"
    publisher: IZA Discussion Paper No. 17639 (Milovanska-Farrington & Mateer, 2025)
    url: https://docs.iza.org/dp17639.pdf
    type: preprint
    accessed: 2026-11-10
  - id: s6
    title: "Teaching the use of cost-benefit reasoning in everyday life (record and abstract)"
    publisher: Duke University Scholars@Duke
    url: https://scholars.duke.edu/individual/pub893241
    type: academic
    accessed: 2026-11-10
created: 2026-11-10
---

# Cost-benefit reasoning training

Cost-benefit reasoning training is a debiasing technique that teaches people the choice rules of microeconomics as explicit, abstract principles and then drills them on varied examples. The core rules are the sunk cost principle (ignore costs that cannot be recovered, since they are the same whichever option you pick), its mirror the extra cost principle, and the opportunity cost principle (the value of the best alternative you give up is a real cost).[^s1] The aim is not to turn people into economists but to make these rules available when an everyday decision is framed around money, time or effort already spent.[^s1][^s6]

## Origin

The technique grew out of Richard Nisbett's research programme at the University of Michigan on whether abstract reasoning rules can be taught. Richard Larrick, James Morgan and Nisbett reported the founding studies in *Psychological Science* in 1990.[^s1] A survey of 126 Michigan professors found that economists endorsed cost-benefit answers to policy questions more often than biologists or humanists and reported more normative everyday behaviour, such as walking out of a bad film or abandoning an unrewarding project. Because that comparison could reflect who chooses economics, the authors ran training experiments with randomly assigned students.[^s1] They concluded that ordinary people can learn and use these rules and that brief instruction improves both reasoning and self-reported behaviour.[^s6]

## How it works

In the second study, 79 undergraduates received about half an hour of instruction on the sunk cost and extra cost principles, using either only financial or only non-financial examples, or no training. Both trained groups chose and reasoned more normatively than controls, and training with money examples transferred fully to problems about time and effort, and vice versa.[^s1] In a third study, trained students picked the normative answer to sunk cost problems 44% of the time versus about 29% for untrained students. About a month later, in an unannounced telephone survey, trained students gave more normative answers on university policy questions; a measure of abandoning purchased activities moved in the expected direction but only marginally.[^s1]

The studies also exposed a lay theory: untrained students mostly believed an economist would endorse "waste not, want not", picking that trap answer more often than the correct rule.[^s1] Training works partly by correcting that belief.

A workplace example: a team has spent eight months and most of a budget on an in-house reporting tool, and a vendor product now does the job better for less than the remaining build cost. A trained reviewer sets the eight months aside as identical under both options, prices what each path still costs and delivers, and adds the opportunity cost of the engineers' time, as the rules prescribe.[^s1]

## How to apply it

1. **State the rules abstractly.** Teach the sunk cost, extra cost and opportunity cost principles as general rules, not as tips for one domain.[^s1]
2. **Vary the examples.** Mix money, time, effort and emotional investments so the rule is not tied to a surface feature.[^s1]
3. **Pair sunk cost and extra cost problems.** Including cases where continuing is correct stops learners from adopting a blanket "always quit" rule.[^s1]
4. **Name the lay theory.** Point out that "waste not, want not" feels like economic prudence but is not the normative rule.[^s1]
5. **Ask the fresh-choice question.** Before a continue-or-stop decision, ask what you would choose today if offered each option at its remaining cost.[^s1][^s2]

Pitfall: completing an economics course is not the same as this training. Generic coursework that never practises recognising sunk costs in disguise may leave the bias intact.[^s2][^s4]

## Evidence and limitations

The evidence that targeted training helps is encouraging but limited. Arkes and Blumer's 1985 tenth experiment found students currently taking economics, and psychology students who had taken it, chose the sunk cost option about as often as students with no economics background.[^s2] A 2015 meta-analysis of about 100 effect sizes from 45 studies likewise found no reliable protective effect of familiarity with economic decision making, though it had very few expert samples.[^s4] Together these suggest it is explicit, transferable rule practice, not exposure to economics, that matters.[^s1][^s2][^s4]

Newer classroom studies point the same way. A field experiment published in the *Journal of Applied Psychology* compared a philosophy critical thinking class that taught such rules with other introductory philosophy classes (N = 397) and reported large reductions in sunk cost and opportunity cost errors, still present at a 16-month follow-up; students self-selected into classes, each bias was measured with one item, follow-up attrition was heavy, and one author taught the course.[^s3] A 2025 working paper found a short lesson in an introductory economics course reduced scores on an eight-item sunk cost scale by about 15%, but not for time-based sunk costs, and it had no control group.[^s5] Because the founding experiments used small student samples and hypothetical problems, and behavioural effects were weak, the evidence is rated mixed.[^s1][^s3][^s5]

## Connections

- **Counteracts** the sunk cost fallacy: randomly assigned training made choices and reasoning about sunk costs more normative.[^s1]
- **Counteracts** opportunity cost neglect: the 2026 field experiment found large reductions in errors on its opportunity cost item.[^s3]
- **Demonstrated by** Larrick, Morgan and Nisbett's 1990 studies, including domain-general transfer and a one-month follow-up.[^s1]
- **Supported by** the Bishop, Feltz and Conway field experiment, which reported durable gains from a critical thinking class.[^s3]
- **Challenged by** Arkes and Blumer's finding that economics instruction did not lessen the effect, and by the 2015 meta-analysis that found no protective effect of economic familiarity.[^s2][^s4]
- **Related to** statistical reasoning training, its sister programme from the same research group, and to transfer of learning, since its value depends on rules carrying over to new domains.[^s1]

## Sources

[^s1]: Larrick, Morgan & Nisbett, "Teaching the use of cost-benefit reasoning in everyday life", *Psychological Science* 1 (1990). https://Www.Gwern.net/doc/psychology/cognitive-bias/sunk-cost/1990-larrick.pdf (accessed 2026-11-10)
[^s2]: Arkes & Blumer, "The psychology of sunk cost", *Organizational Behavior and Human Decision Processes* 35 (1985). https://cognition.aau.at/bg/BA/Arkes%20%26%20Blumer%201985.pdf (accessed 2026-11-10)
[^s3]: Bishop, Feltz & Conway, "Critical thinking classes can reduce common biases: results from a field experiment", *Journal of Applied Psychology* (2026), accepted manuscript. https://eprints.soton.ac.uk/510148/1/Bishop_et_al_2026_Critical_Thinking_Classes_Can_Debias_Reasoning_JAP_Preprint.pdf (accessed 2026-11-10)
[^s4]: Roth, Robbert & Straus, "On the sunk-cost effect in economic decision-making: a meta-analytic review", *Business Research* 8 (2015). https://link.springer.com/article/10.1007/s40685-014-0014-8 (accessed 2026-11-10)
[^s5]: Milovanska-Farrington & Mateer, "Does learning economics make you less susceptible to the sunk cost fallacy?", IZA Discussion Paper 17639 (2025). https://docs.iza.org/dp17639.pdf (accessed 2026-11-10)
[^s6]: Duke University Scholars@Duke, record for Larrick, Morgan & Nisbett (1990). https://scholars.duke.edu/individual/pub893241 (accessed 2026-11-10)
