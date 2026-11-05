---
id: ct:debiasing
type: Technique
title: Debiasing
aliases: [bias mitigation, cognitive bias mitigation, debiasing strategies]
domain: debiasing-and-metacognition
summary: >-
  The family of interventions that remove or reduce systematic errors in
  judgment and decision making, either by changing the decision maker
  (education, cognitive strategies, decision models) or by changing the
  task and environment (incentives, accountability, choice architecture,
  organisational routines).
level: introductory
evidenceStatus: mixed
broader: [ct:judgment-and-decision-making]
related: [ct:cognitive-bias, ct:bias-blind-spot, ct:metacognition, ct:choice-architecture]
requires: [ct:cognitive-bias]
relations:
  - {predicate: introducedBy, object: ct:baruch-fischhoff, source: s1, confidence: medium}
  - {predicate: introducedIn, object: ct:judgment-under-uncertainty, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:confirmation-bias, source: s3, confidence: medium}
  - {predicate: counteracts, object: ct:overconfidence-effect, source: s2, confidence: medium}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:swaryandini-2025-debiasing-education-meta-analysis, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Debiasing"
    publisher: "Fischhoff, B. (1982), chapter 31 in Kahneman, Slovic & Tversky (eds.), Judgment under Uncertainty: Heuristics and Biases, pp. 422-444, Cambridge University Press"
    url: https://www.cambridge.org/core/books/abs/judgment-under-uncertainty/debiasing/5DBEFB9D23BCC41E7A78BBBD895F9699
    type: primary
    accessed: 2026-11-05
  - id: s2
    title: "A User's Guide to Debiasing"
    publisher: "Soll, Milkman & Payne (2015), chapter 33 in Keren & Wu (eds.), The Wiley Blackwell Handbook of Judgment and Decision Making (author copy)"
    url: https://static1.squarespace.com/static/5353b838e4b0e68461b517cf/t/59b966cd4c0dbf23b6b997b2/1505322703896/39-2016_Handbook_of_JDM.pdf
    type: textbook
    accessed: 2026-11-05
  - id: s3
    title: "Giving Debiasing Away: Can Psychological Research on Correcting Cognitive Errors Promote Human Welfare?"
    publisher: "Perspectives on Psychological Science 4(4), 390-398 (Lilienfeld, Ammirati & Landfield, 2009), University of Notre Dame copy"
    url: https://www3.nd.edu/~ghaeffel/Lilienfeld2009%20Perspectives%20on%20Psychological%20Science.pdf
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s4
    title: "Systematic review and meta-analysis of educational approaches to reduce cognitive biases among students"
    publisher: "Nature Human Behaviour (Swaryandini, Graham, Griffith et al., 2025), University of Leicester repository"
    url: https://figshare.le.ac.uk/articles/journal_contribution/Systematic_review_and_meta-analysis_of_educational_approaches_to_reduce_cognitive_biases_among_students/30208108
    type: peer-reviewed
    accessed: 2026-11-05
created: 2026-11-05
---

# Debiasing

Debiasing is the umbrella term for anything that removes a systematic judgment error or makes it smaller or less frequent. Researchers use the word broadly: an intervention counts even if it only weakens a bias rather than eliminating it.[^s3] The benchmark is a normative standard, such as logical coherence, probability theory or accuracy against outcomes, and debiasing also covers improving the process that produces a judgment, not only the final answer.[^s2]

## Origin

The term was set out by Baruch Fischhoff in a 1982 chapter titled "Debiasing" in *Judgment under Uncertainty*, the volume edited by Daniel Kahneman, Paul Slovic and Amos Tversky that collected the early heuristics-and-biases research.[^s1] Fischhoff borrowed the engineering idea of destructive testing: once a bias has been found, researchers should probe the conditions under which it appears and disappears, and the psychological processes that must be evoked or controlled to remove it.[^s1] Later reviewers credit him with a lasting distinction between blaming a bias on the judge and blaming it on the task, which still organises the field.[^s2]

## How it works

Soll, Milkman and Payne sort debiasing tools into two broad strategies.[^s2]

- **Modify the decision maker.** Teach normative rules (most effective when the training is domain-specific, timely and repeated); give people cognitive strategies such as considering the opposite, imagining a future failure, or averaging two of their own independent estimates; or replace intuition with simple linear models, which often beat expert judgment.[^s2]
- **Modify the environment.** Add incentives or accountability, redesign how choices are presented (defaults, planning prompts, precommitment, clearer formats for numbers), or build organisational "cognitive repairs" such as checklists that catch errors individuals would miss.[^s2]

A workplace example: a hiring panel keeps favouring candidates who resemble its first strong interviewee. Training the panel on confirmation bias is the person-side fix. Changing the task, by scoring every candidate on the same structured questions before anyone discusses them and averaging the independent scores, is the environment-side fix. Lilienfeld and colleagues single out confirmation bias as a priority target because it fuels entrenched disagreement.[^s3]

## How to apply it

1. **Name the error and its cause.** Ask whether the problem is lack of effort, lack of knowledge, or a quirk of how the task is framed, because the remedy differs: incentives help with effort-driven errors but do little when the bias comes from missing knowledge.[^s2]
2. **Prefer changing the task when you can.** Defaults, structured formats and checklists work without asking people to notice their own bias, which they often cannot.[^s2][^s3]
3. **If you train people, make it specific and repeated.** Transfer to new domains is weak, so practise on the decisions people actually make and add booster sessions.[^s2][^s3]
4. **Test the fix.** Effects vary by context, so pilot an intervention and measure whether judgments improve.[^s2]

**Pitfalls:** some remedies backfire. Asking people to generate many alternative outcomes can increase hindsight certainty, and weak counterarguments can inoculate people against stronger ones.[^s3] Incentives can make people think harder without thinking better, and defaults treat everyone alike even when preferences differ.[^s2]

## Evidence

The evidence is real but modest. A 2025 meta-analysis in *Nature Human Behaviour* pooled 160 effects from 41 randomised trials of educational debiasing and found a small average benefit (Hedges' g of about 0.26) over control conditions.[^s4] The same review rated every included study at unclear or high risk of bias, flagged possible publication bias, found some biases (such as those from the representativeness heuristic) hard to shift, and could not establish that gains last or carry over to real decisions.[^s4] Earlier, Lilienfeld and colleagues described the literature as sparse, fragmented and mixed, while still warranting cautious optimism.[^s3] The bias blind spot is a recurring obstacle: people see bias in others more readily than in themselves, which weakens their motivation to accept correction.[^s2][^s3]

## Connections

- **Broader:** debiasing is a central applied question within judgment and decision making, the field that studies how heuristics produce biases and how to repair them.[^s2]
- **introducedBy / introducedIn:** Baruch Fischhoff framed debiasing as a research programme in his 1982 chapter in *Judgment under Uncertainty*.[^s1]
- **counteracts:** confirmation bias is the target Lilienfeld and colleagues argue matters most,[^s3] and cognitive strategies such as considering the opposite and averaging one's own estimates are aimed at overconfidence.[^s2]
- **supportedBy:** the 2025 meta-analysis of educational interventions provides the main quantitative support, with the caveats above.[^s4]
- **Related:** the bias blind spot limits self-debiasing,[^s3] choice architecture is the environment-side toolkit,[^s2] and narrower techniques such as consider the opposite, premortem and debiasing training games sit beneath this node.

## Sources

[^s1]: Fischhoff, "Debiasing", in *Judgment under Uncertainty: Heuristics and Biases*, Cambridge University Press, 1982. https://www.cambridge.org/core/books/abs/judgment-under-uncertainty/debiasing/5DBEFB9D23BCC41E7A78BBBD895F9699 (accessed 2026-11-05)
[^s2]: Soll, Milkman & Payne, "A User's Guide to Debiasing", *Wiley Blackwell Handbook of Judgment and Decision Making*, 2015. https://static1.squarespace.com/static/5353b838e4b0e68461b517cf/t/59b966cd4c0dbf23b6b997b2/1505322703896/39-2016_Handbook_of_JDM.pdf (accessed 2026-11-05)
[^s3]: Lilienfeld, Ammirati & Landfield, "Giving Debiasing Away", *Perspectives on Psychological Science*, 2009. https://www3.nd.edu/~ghaeffel/Lilienfeld2009%20Perspectives%20on%20Psychological%20Science.pdf (accessed 2026-11-05)
[^s4]: Swaryandini et al., "Systematic review and meta-analysis of educational approaches to reduce cognitive biases among students", *Nature Human Behaviour*, 2025. https://figshare.le.ac.uk/articles/journal_contribution/Systematic_review_and_meta-analysis_of_educational_approaches_to_reduce_cognitive_biases_among_students/30208108 (accessed 2026-11-05)
