---
id: ct:conditional-reasoning-training
type: Technique
title: Conditional reasoning training
aliases: [logic training for conditionals, conditional logic instruction, training propositional reasoning]
domain: debiasing-and-metacognition
summary: >-
  Instruction that teaches what an "if p, then q" statement does and does not
  license (modus ponens and the contrapositive follow; the converse and the
  inverse do not), aimed at reducing fallacious conditional inferences. Bare
  rule teaching transfers poorly; rules tied to truth conditions or worked
  examples do better, and the gains are partial.
level: intermediate
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:statistical-reasoning-training, ct:logical-necessity-instructions, ct:eliminating-counterexamples, ct:truth-table, ct:material-conditional, ct:wason-selection-task, ct:contraposition, ct:affirming-the-consequent]
requires: [ct:material-conditional, ct:validity]
relations:
  - {predicate: counteracts, object: ct:denying-the-antecedent, source: s3, confidence: medium}
  - {predicate: counteracts, object: ct:improper-transposition, source: s6, confidence: low}
  - {predicate: supportedBy, object: ct:klauer-2000-propositional-reasoning-training-study, source: s2, confidence: medium}
  - {predicate: challengedBy, object: ct:cheng-1986-deductive-reasoning-training-study, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:mental-model-theory, source: s2, confidence: medium}
  - {predicate: appliedIn, object: ct:mathematics-education, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Pragmatic versus syntactic approaches to training deductive reasoning"
    publisher: "Cognitive Psychology 18(3), 293-328 (Cheng, Holyoak, Nisbett & Oliver, 1986), University of Michigan Deep Blue"
    url: https://deepblue.lib.umich.edu/items/249f6d6c-c52f-4b50-9db5-3ecd3096160a/full
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "Training propositional reasoning"
    publisher: "Quarterly Journal of Experimental Psychology 53A(3), 868-895 (Klauer and colleagues, 2000), Taylor & Francis abstract"
    url: https://informahealthcare.com/doi/abs/10.1080/713755911
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "Advanced Mathematics and Deductive Reasoning Skills: Testing the Theory of Formal Discipline"
    publisher: "Nina Attridge, PhD thesis, Loughborough University (2013), CORE repository copy"
    url: https://core.ac.uk/download/288381715.pdf
    type: academic
    accessed: 2026-11-17
  - id: s4
    title: "Conditional inference and advanced mathematical study"
    publisher: "Educational Studies in Mathematics 67(3), 187-204 (Inglis & Simpson, 2008), Loughborough repository preprint via CORE"
    url: https://core.ac.uk/download/288388639.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "Advanced mathematical study and the development of conditional reasoning skills"
    publisher: "PLOS ONE 8(7) (Attridge & Inglis, 2013), Loughborough University repository"
    url: https://repository.lboro.ac.uk/articles/journal_contribution/Advanced_mathematical_study_and_the_development_of_conditional_reasoning_skills/9369845
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s6
    title: "Implication (CS205 Discrete Structures lecture slides)"
    publisher: "A. Elgammal, Department of Computer Science, Rutgers University"
    url: https://people.cs.rutgers.edu/~elgammal/classes/cs205/implication.pdf
    type: academic
    accessed: 2026-11-17
created: 2026-11-17
---

# Conditional reasoning training

Conditional reasoning training is instruction designed to make people draw only the inferences an "if p, then q" statement supports. Standard teaching material sets out four related statements: the conditional itself, its converse ("if q, then p"), its inverse ("if not p, then not q") and its contrapositive ("if not q, then not p"). Only the contrapositive is equivalent to the original; the inverse and the converse are equivalent to each other but not to the conditional.[^s6] Training aims to make that table usable in practice, so that a learner who hears "if p, then q" does not slide into the inverse (improper transposition), into denying the antecedent, or into affirming the consequent.[^s6][^s3] It is a debiasing technique in the same family as statistical reasoning training: teach an abstract rule, then help people see where it applies.[^s1]

## Origin

The modern research programme starts with Patricia Cheng, Keith Holyoak, Richard Nisbett and Lindsay Oliver at the University of Michigan, who published "Pragmatic versus syntactic approaches to training deductive reasoning" in *Cognitive Psychology* in 1986.[^s1] They tested, in the laboratory and in a classroom, whether teaching abstract logical rules improves performance on Wason's selection task. Teaching abstract principles on their own did little; the principles worked only when paired with worked examples of selection problems.[^s1] Attridge's 2013 review of that work describes the classroom arm: a semester-long standard logic course of about 40 hours, covering modus ponens, modus tollens, the two conditional fallacies and the difference between the material conditional and the biconditional, reduced selection-task errors by only about 3 percent, which was not significant.[^s3] In 2000, Klauer and colleagues compared ways of training propositional reasoning directly and found that semantic training, which explains connectives through their truth conditions, outperformed syntactic training in formal derivations.[^s2]

## How it works

The technique replaces a pattern-matching habit with a check on what the conditional rules out. A conditional is false only in the case where p is true and q is false, so a conclusion follows only if every case that leaves the premises true also makes the conclusion true.[^s6][^s2] Klauer and colleagues' semantic condition taught exactly this, by explaining the truth-table definitions of the connectives, and a second semantic condition used thematic, everyday contexts for the premises. Both beat syntactic instruction and an unrelated control task, and the two did not differ from each other; the pattern replicated in a second experiment.[^s2]

A workplace example: a team lead is told, "If a pull request touches the billing module, it needs a security review." A trainee who has only memorised the rule may conclude, "This one doesn't touch billing, so it needs no review." Trained reasoners ask which case the rule forbids (a billing change without a review), notice that a non-billing change is not that case, and recognise that the rule is silent about it. The rule supports only the contrapositive: a change that legitimately skipped review did not touch billing.[^s6]

## How to apply it

1. **Teach the four statements together.** Present the conditional, converse, inverse and contrapositive side by side and show by truth table which pairs agree.[^s6]
2. **Explain meaning, not just moves.** Ground the rule in the one case a conditional rules out, rather than in derivation rules alone; this semantic route is the one with experimental support.[^s2]
3. **Pair every rule with worked examples.** Abstract principles transferred only when coupled with concrete problems that show how they map onto cases.[^s1]
4. **Practise rejecting tempting inferences.** Give items where denying the antecedent or the inverse feels natural, and require a counterexample case before accepting any conclusion.[^s3][^s4]
5. **Check transfer.** Test on unfamiliar content, since a one-semester logic course showed almost no gain on the selection task.[^s3]

**Pitfalls.** Training can overshoot. Learners may start rejecting valid modus tollens along with the fallacies, which is what happened to mathematics students in Attridge and Inglis's longitudinal study.[^s5][^s3]

## Evidence

The evidence is real but uneven, so the status here is *mixed*. Direct, short training works better when it is semantic: Klauer and colleagues' truth-condition and thematic trainings significantly improved propositional reasoning compared with syntactic and control training.[^s2] Classroom logic, taught as rules, transfers poorly.[^s1][^s3] Correlational and quasi-experimental studies of mathematics students point the same way but complicate it. Inglis and Simpson (2008) found that mathematics undergraduates endorsed far fewer invalid conditional inferences than arts undergraduates, with denial-of-the-antecedent endorsements averaging about 1 versus about 4, though their cross-sectional design could not show that study caused the gap.[^s4] Following A-level students for a year, Attridge found that mathematics students' denial-of-the-antecedent endorsements fell from about 5.0 to 3.9 while literature students' did not fall. The mathematics students also endorsed fewer valid modus tollens inferences.[^s3] Attridge and Inglis (2013) read this as a shift toward a "defective" reading of the conditional, not toward the textbook material conditional.[^s5] No large multi-lab replication of a conditional-logic training effect was found for this article.

## Connections

- **Counteracts denying the antecedent.** A year of mathematics study, in effect sustained practice with conditionals, cut endorsement of this fallacy in a controlled comparison.[^s3]
- **Counteracts improper transposition (low confidence).** The core teaching content is that the inverse is not equivalent to the conditional; direct trials measuring the inverse inference after training are scarce.[^s6]
- **Supported by Klauer and colleagues' 2000 training study.** Semantic training beat syntactic and control training in two experiments.[^s2]
- **Challenged by Cheng and colleagues' 1986 study.** Abstract rule teaching and a full logic course produced little transfer without worked examples.[^s1][^s3]
- **Explained by mental model theory.** Klauer and colleagues present the advantage of semantic training as support for the mental models account of reasoning.[^s2]
- **Applied in mathematics education.** Advanced mathematics is the main natural setting where conditional reasoning is practised and its development has been tracked.[^s5][^s4]
- **Related to statistical reasoning training, logical necessity instructions and eliminating counterexamples.** These are sibling instructional fixes: rule teaching for statistics, instructions against belief bias, and a counterexample-set method for conditionals.[^s1][^s6]

## Sources

[^s1]: Cheng, Holyoak, Nisbett & Oliver, "Pragmatic versus syntactic approaches to training deductive reasoning", *Cognitive Psychology* 18(3), 1986. https://deepblue.lib.umich.edu/items/249f6d6c-c52f-4b50-9db5-3ecd3096160a/full (accessed 2026-11-17)
[^s2]: Klauer and colleagues, "Training propositional reasoning", *Quarterly Journal of Experimental Psychology* 53A(3), 2000. https://informahealthcare.com/doi/abs/10.1080/713755911 (accessed 2026-11-17)
[^s3]: Attridge, *Advanced Mathematics and Deductive Reasoning Skills: Testing the Theory of Formal Discipline*, PhD thesis, Loughborough University, 2013. https://core.ac.uk/download/288381715.pdf (accessed 2026-11-17)
[^s4]: Inglis & Simpson, "Conditional inference and advanced mathematical study", *Educational Studies in Mathematics* 67(3), 2008. https://core.ac.uk/download/288388639.pdf (accessed 2026-11-17)
[^s5]: Attridge & Inglis, "Advanced mathematical study and the development of conditional reasoning skills", *PLOS ONE* 8(7), 2013. https://repository.lboro.ac.uk/articles/journal_contribution/Advanced_mathematical_study_and_the_development_of_conditional_reasoning_skills/9369845 (accessed 2026-11-17)
[^s6]: Elgammal, "Implication", CS205 lecture slides, Rutgers University. https://people.cs.rutgers.edu/~elgammal/classes/cs205/implication.pdf (accessed 2026-11-17)
