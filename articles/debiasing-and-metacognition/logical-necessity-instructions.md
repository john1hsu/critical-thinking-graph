---
id: ct:logical-necessity-instructions
type: Technique
title: Logical necessity instructions
aliases: [necessity instructions, augmented logic instructions, instructional debiasing of belief bias]
domain: debiasing-and-metacognition
summary: >-
  A debiasing technique for deductive judgments in which the reasoner is told,
  or tells themselves, to assume the premises are true and to accept a
  conclusion only if it must follow from them, regardless of whether it is
  believable. It reduces belief bias in some studies but has not eliminated it.
level: intermediate
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:syllogism, ct:method-of-counterexample, ct:venn-diagram-test, ct:undistributed-middle, ct:dual-process-theory]
requires: [ct:validity]
relations:
  - {predicate: counteracts, object: ct:belief-bias, source: s1, confidence: medium}
  - {predicate: supportedBy, object: ct:caravona-2019-pragmatic-instruction-experiments, source: s2, confidence: medium}
  - {predicate: challengedBy, object: ct:evans-1994-debiasing-by-instruction-experiments, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Debiasing by instruction: The case of belief bias"
    publisher: European Journal of Cognitive Psychology 6(3), 263-285 (Evans, Newstead, Allen & Pollard, 1994), Leeds Trinity University research portal
    url: https://research.leedstrinity.ac.uk/en/publications/debiasing-by-instruction-the-case-of-belief-bias/
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s2
    title: "How to Get Rid of the Belief Bias: Boosting Analytical Thinking via Pragmatics"
    publisher: Europe's Journal of Psychology 15(3), 595-613 (Caravona, Macchi, Poli, Vezzoli, Franchella & Bagassi, 2019)
    url: https://ejop.psychopen.eu/index.php/ejop/article/download/1794/1794.html?inline=1
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s3
    title: "Necessity, possibility and belief: A study of syllogistic reasoning"
    publisher: Quarterly Journal of Experimental Psychology A 54(3), 935-958 (Evans, Handley & Harper, 2001), Macquarie University research portal
    url: https://researchers.mq.edu.au/en/publications/necessity-possibility-and-belief-a-study-of-syllogistic-reasoning/
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s4
    title: "Logic, beliefs, and instruction: A test of the default interventionist account of belief bias"
    publisher: Journal of Experimental Psychology - Learning, Memory, and Cognition 37(1), 28-43 (Handley, Newstead & Trippas, 2011), University of Plymouth research portal
    url: https://researchportal.plymouth.ac.uk/en/publications/logic-beliefs-and-instruction-a-test-of-the-default-interventioni/
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s5
    title: "Validity and Soundness"
    publisher: Internet Encyclopedia of Philosophy
    url: https://iep.utm.edu/val-snd
    type: scholarly-encyclopedia
    accessed: 2026-11-06
created: 2026-11-06
---

# Logical necessity instructions

Logical necessity instructions are a way of framing a deductive task so that the only question on the table is whether the conclusion has to be true if the premises are. The reasoner is asked to take the premises as given, to set aside whether the conclusion is plausible, and to accept it only when no way of making the premises true leaves it false.[^s1][^s2] The framing mirrors the logician's definition of validity, under which an argument can be valid even when its premises and conclusion are plainly false, because validity concerns the link between them and not their truth.[^s5] The technique targets belief bias, the habit of judging an argument by how believable its conclusion is.[^s1]

## Origin

The approach grew out of British research on syllogistic reasoning in the late 1980s and early 1990s. According to Caravona and colleagues' review, Newstead and colleagues (1992) gave participants long instructions explaining logic, validity and necessity, and correct rejection of invalid arguments with believable conclusions rose to 83%.[^s2] Those instructions also told people to reject any conclusion they were not absolutely sure of, which may simply have made them more willing to say "invalid".[^s2] Evans, Newstead, Allen and Pollard (1994) then ran three experiments under the title *Debiasing by instruction*. In the first two, including an exact replication of the earlier augmented condition, belief bias persisted even though the instructions stressed logical necessity; in the third, more elaborated instructions that did not explicitly mention necessity reduced it.[^s1] They concluded that instruction can reduce belief bias but not remove it.[^s1]

## How it works

Most people judge an argument by asking whether they agree with its conclusion. Necessity instructions try to swap that question for a different one: could the premises all be true while the conclusion is false?[^s1][^s5] A workplace example: a procurement memo argues, "All vendors that passed our security review hold ISO certification. This supplier holds ISO certification. So this supplier passed our security review." The conclusion sounds right, so it tends to be waved through. Read under a necessity instruction (assume both premises are true; must the conclusion be true?), the gap appears: an ISO-certified supplier might never have been reviewed, or might have failed. The argument commits the undistributed middle, and its believability was doing the work.[^s1][^s5]

Wording seems to matter as much as content. Caravona and colleagues (2019) found that when students were asked only whether a conclusion "follows", just 4% of untrained and 10% of logic-trained students correctly rejected an invalid argument with a believable conclusion.[^s2] When the question asked whether the conclusion necessarily follows, correct rejections rose to 66% and 77%.[^s2] The authors argue that much belief bias reflects a misunderstanding of what the question is asking, not only a lack of logical skill.[^s2]

## How to apply it

1. **Restate the task.** Before judging, say explicitly: "I am assuming every premise is true. I am asking only whether the conclusion must then be true."[^s2][^s5]
2. **Separate truth from validity.** Note your view on whether the conclusion is true in a different column, so it does not leak into the validity judgment.[^s5]
3. **Look for a counter-case.** Try to describe a situation in which every premise holds and the conclusion fails; if you can, the argument is invalid.[^s5]
4. **Use it where stakes and time allow.** It suits written analysis, audits of reasoning in reports, and teaching. It is a framing aid, not a substitute for knowing the valid forms.[^s1]

Pitfalls: stern instructions can make people reject more conclusions across the board, including valid ones, which looks like debiasing but is a shift in caution. In the Newstead study, acceptance of valid arguments with believable conclusions also fell, to 75%.[^s2]

## Evidence and limitations

The record is mixed. Belief effects survived necessity-focused instructions in two of the three Evans et al. (1994) experiments.[^s1] Evans, Handley and Harper (2001) found that people still rejected unbelievable conclusions more often than neutral ones whether they were asked about necessity or about possibility, across three experiments.[^s3] Caravona et al. reported large gains, but their Experiment 2 used one syllogism and borrowed its control group from Experiment 1, and no direct replication is reported.[^s2] Handley, Newstead and Trippas (2011) asked people across five experiments to judge either validity or believability. Logical status disrupted belief judgments more than belief disrupted validity judgments, and belief judgments took longer.[^s4] That suggests some logical information is available quickly, so instructions may work partly by telling people which of two competing answers to report.[^s4]

## Connections

- **Broader: debiasing.** Necessity instructions are a debiasing-by-instruction technique aimed at one specific bias.[^s1]
- **Requires validity.** The instruction is a plain-language restatement of what validity means.[^s5]
- **Counteracts belief bias.** Elaborated instructions reduced, but did not eliminate, the influence of belief on syllogism judgments.[^s1]
- **Supported by Caravona et al. (2019),** whose "necessarily follows" wording sharply raised correct rejections of believable invalid conclusions.[^s2]
- **Challenged by Evans et al. (1994),** where instructions stressing necessity failed to remove belief effects, including in an exact replication.[^s1]
- **Related to the syllogism, the undistributed middle, the method of counterexample, the Venn diagram test and dual-process theory.** Syllogisms are the standard test items, believable undistributed-middle arguments are the classic trap, counterexample search and diagrams are the checks the instruction invites, and dual-process accounts frame the debate over why instruction helps.[^s1][^s4][^s5]

## Sources

[^s1]: J. St. B. T. Evans, S. E. Newstead, J. L. Allen & P. Pollard, "Debiasing by instruction: The case of belief bias", *European Journal of Cognitive Psychology* 6(3), 1994, 263–285. https://research.leedstrinity.ac.uk/en/publications/debiasing-by-instruction-the-case-of-belief-bias/ (accessed 2026-11-06)
[^s2]: L. Caravona, L. Macchi, F. Poli, M. Vezzoli, M. A. G. Franchella & M. Bagassi, "How to Get Rid of the Belief Bias: Boosting Analytical Thinking via Pragmatics", *Europe's Journal of Psychology* 15(3), 2019, 595–613. https://ejop.psychopen.eu/index.php/ejop/article/download/1794/1794.html?inline=1 (accessed 2026-11-06)
[^s3]: J. St. B. T. Evans, S. J. Handley & C. N. J. Harper, "Necessity, possibility and belief: A study of syllogistic reasoning", *Quarterly Journal of Experimental Psychology A* 54(3), 2001, 935–958. https://researchers.mq.edu.au/en/publications/necessity-possibility-and-belief-a-study-of-syllogistic-reasoning/ (accessed 2026-11-06)
[^s4]: S. J. Handley, S. E. Newstead & D. Trippas, "Logic, beliefs, and instruction: A test of the default interventionist account of belief bias", *Journal of Experimental Psychology: Learning, Memory, and Cognition* 37(1), 2011, 28–43. https://researchportal.plymouth.ac.uk/en/publications/logic-beliefs-and-instruction-a-test-of-the-default-interventioni/ (accessed 2026-11-06)
[^s5]: "Validity and Soundness", *Internet Encyclopedia of Philosophy*. https://iep.utm.edu/val-snd (accessed 2026-11-06)
