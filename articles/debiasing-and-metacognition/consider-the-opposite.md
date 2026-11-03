---
id: ct:consider-the-opposite
type: Technique
title: Consider the opposite
aliases: [considering the opposite, consider-the-opposite strategy, consider-an-alternative strategy]
domain: debiasing-and-metacognition
summary: >-
  A debiasing technique in which a person deliberately generates reasons why
  their current judgment, hypothesis or reference value might be wrong, so
  that evidence pointing the other way becomes as available as the evidence
  that supports it.
level: introductory
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:devils-advocacy, ct:premortem, ct:anchoring-effect, ct:selective-accessibility-model]
requires: []
relations:
  - {predicate: introducedBy, object: ct:charles-lord, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:mark-lepper, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:biased-assimilation, source: s1, confidence: medium}
  - {predicate: counteracts, object: ct:anchoring-effect, source: s2, confidence: high}
  - {predicate: counteracts, object: ct:hindsight-bias, source: s4, confidence: medium}
  - {predicate: counteracts, object: ct:overconfidence-effect, source: s4, confidence: medium}
  - {predicate: explainedBy, object: ct:selective-accessibility-model, source: s2, confidence: medium}
  - {predicate: demonstratedBy, object: ct:nagtegaal-2020-public-managers-anchoring-study, source: s3, confidence: medium}
  - {predicate: contrastsWith, object: ct:ease-of-retrieval-effect, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Considering the opposite: A corrective strategy for social judgment"
    publisher: Journal of Personality and Social Psychology 47(6), 1231-1243 (Lord, Lepper & Preston, 1984), CAUSE record
    url: https://causeweb.org/cause/node/7638
    type: primary
    accessed: 2026-11-03
  - id: s2
    title: "Overcoming the inevitable anchoring effect: Considering the opposite compensates for selective accessibility"
    publisher: Personality and Social Psychology Bulletin (Mussweiler, Strack & Pfeiffer, 2000), Synapse record
    url: https://synapsesocial.com/papers/W1992970544
    type: primary
    accessed: 2026-11-03
  - id: s3
    title: "Designing to Debias: Measuring and Reducing Public Managers' Anchoring Bias"
    publisher: Public Administration Review, 565-576 (Nagtegaal, Tummers, Noordegraaf & Bekkers, 2020), Erasmus University research portal
    url: https://pure.eur.nl/en/publications/designing-to-debias-measuring-and-reducing-public-managers-anchor/
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s4
    title: "Metacognitive experiences and the intricacies of setting people straight: Implications for debiasing and public information campaigns"
    publisher: Advances in Experimental Social Psychology 39, 127-161 (Schwarz, Sanna, Skurnik & Yoon, 2007), author's copy, University of Southern California
    url: https://dornsife.usc.edu/norbert-schwarz/wp-content/uploads/sites/231/2023/11/07_aep_schwarz_et_al_setting-people-straight.pdf
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s5
    title: "Overcoming the inevitable anchoring effect (faculty publication record)"
    publisher: London Business School
    url: https://www.london.edu/faculty-and-research/academic-research/o/overcoming-the-inevitable-anchoring-effect--considering-the-opposi
    type: academic
    accessed: 2026-11-03
created: 2026-11-03
---

# Consider the opposite

Consider the opposite is a debiasing technique: before settling on a judgment, you deliberately ask yourself why it might be wrong and generate concrete reasons or evidence for the alternative. Its rationale is that many judgment errors are not caused by a lack of effort or goodwill but by a lopsided search of memory, in which the possibilities that fit the current view come to mind and the ones that contradict it do not.[^s1] Making the other side explicitly available is meant to rebalance that search.[^s2]

## Origin

The technique was named and first tested by Charles Lord, Mark Lepper and E. Preston in a 1984 paper in the *Journal of Personality and Social Psychology*. They traced the underlying problem back to an observation by Francis Bacon: people tend not to consider possibilities that run against what they already believe.[^s1] In two parallel experiments, one on how people assimilate mixed evidence about a social issue and one on how they test hypotheses about another person's personality, they prompted participants to consider the opposite, either by instructing them to do so or by using materials that made the opposite possibility salient. In both, the prompt reduced bias more than an instruction simply to be as fair and unbiased as possible.[^s1] The authors linked their results to earlier findings on belief perseverance and hindsight and proposed the strategy as a way to retrain social judgment.[^s1]

Thomas Mussweiler, Fritz Strack and Tim Pfeiffer later gave the technique a mechanism for numerical judgment. Their selective-accessibility account of anchoring holds that thinking about an anchor makes anchor-consistent knowledge easier to recall, so the remedy should be to make anchor-inconsistent knowledge equally accessible.[^s2][^s5]

## How it works

A team lead is drafting next year's budget for a software project, and the first number on the table is last year's figure of 400 person-days. Left alone, the new estimate tends to land near that figure. Using consider the opposite, the lead writes down three specific reasons why 400 could be badly wrong for this year: the scope has doubled, two senior engineers have left, and a dependency is being rewritten. Those reasons now sit alongside the familiar ones that made 400 feel right, and the final estimate is built from both.[^s2][^s3]

This is the pattern Mussweiler and colleagues tested. In their first study, experts who listed arguments against a supplied anchor showed a smaller anchoring effect than experts who did not; in the second, the influence of the anchor and the influence of considering the opposite added together, consistent with two opposing pulls on what comes to mind.[^s2]

## How to apply it

1. **Fix the judgment first.** Write down your current estimate, hypothesis or conclusion so you know what you are testing.[^s1]
2. **Ask a specific question.** Not "am I biased?" but "what would have to be true for the answer to be very different, and what evidence points that way?" Lord and colleagues found that this targeted instruction beat a general appeal to fairness.[^s1]
3. **Generate only a few reasons.** Two or three concrete counter-reasons are enough. Schwarz and colleagues review studies in which listing a small number of alternatives reduced bias, while being asked for many (such as twelve) did not help and sometimes made things worse.[^s4]
4. **Revise, then record.** Adjust the judgment in light of the reasons you found and note what you considered, so the check can be reviewed later.[^s3]

**When to use it:** whenever a starting value, prior hypothesis or known outcome is likely to dominate your thinking, for example estimates, performance ratings, negotiations, forecasts, and post-mortems where the outcome is already known.[^s3][^s4]

**Pitfalls:** if generating counter-reasons feels hard, people can read that difficulty as a sign that the original view must be right, and the technique backfires.[^s4] A prompt that feels like a box-ticking exercise is also unlikely to change the search of memory it is meant to correct.[^s1]

## Evidence

The core finding has been reproduced in several settings, but with variation. A 2020 survey experiment with 1,221 public managers and employees in the United Kingdom replicated two anchoring experiments and found that a brief, low-cost consider-the-opposite prompt reduced anchoring; an exploratory subgroup analysis suggested the size of the benefit depends on context, and the authors called for field tests.[^s3]

The main limitation comes from research on metacognitive experience. Reviewing work by Sanna, Schwarz and colleagues, Schwarz and co-authors (2007) report that listing three reasons for an alternative outcome eliminated hindsight bias and reduced students' overconfidence before an exam, but listing twelve did not, and in one study generating many alternatives pushed hindsight bias above the no-intervention baseline.[^s4] They conclude that the technique works when thinking of the opposite feels easy and can fail when it feels difficult, so trying harder to be unbiased is not always better.[^s4] On current evidence the technique is best described as useful but sensitive to how it is delivered, which is why its evidence status here is mixed.[^s3][^s4]

## Connections

- **Introduced by** Charles Lord and Mark Lepper, with E. Preston, in their 1984 experiments.[^s1]
- **Counteracts** biased assimilation of evidence, the first target of the original studies.[^s1]
- **Counteracts** the anchoring effect, as shown by Mussweiler, Strack and Pfeiffer.[^s2]
- **Explained by** the selective-accessibility model, which says anchoring works by making anchor-consistent knowledge easier to retrieve.[^s2]
- **Demonstrated by** Nagtegaal and colleagues' 2020 survey experiment on anchoring among UK public managers.[^s3]
- **Counteracts** hindsight bias and overconfidence when only a few alternatives are generated.[^s4]
- **Contrasts with** the ease-of-retrieval effect, the metacognitive mechanism that can make the technique backfire when counter-reasons are hard to produce.[^s4]
- **Related to** devil's advocacy and the premortem, structured techniques that likewise make an opposing case explicit before a decision is taken.[^s1]

## Sources

[^s1]: Lord, Lepper & Preston, "Considering the opposite: A corrective strategy for social judgment", *Journal of Personality and Social Psychology* 47 (1984). https://causeweb.org/cause/node/7638 (accessed 2026-11-03)
[^s2]: Mussweiler, Strack & Pfeiffer, "Overcoming the inevitable anchoring effect: Considering the opposite compensates for selective accessibility", *Personality and Social Psychology Bulletin* (2000). https://synapsesocial.com/papers/W1992970544 (accessed 2026-11-03)
[^s3]: Nagtegaal, Tummers, Noordegraaf & Bekkers, "Designing to Debias: Measuring and Reducing Public Managers' Anchoring Bias", *Public Administration Review* (2020). https://pure.eur.nl/en/publications/designing-to-debias-measuring-and-reducing-public-managers-anchor/ (accessed 2026-11-03)
[^s4]: Schwarz, Sanna, Skurnik & Yoon, "Metacognitive experiences and the intricacies of setting people straight", *Advances in Experimental Social Psychology* 39 (2007). https://dornsife.usc.edu/norbert-schwarz/wp-content/uploads/sites/231/2023/11/07_aep_schwarz_et_al_setting-people-straight.pdf (accessed 2026-11-03)
[^s5]: London Business School, faculty publication record for Mussweiler, Strack & Pfeiffer (2000). https://www.london.edu/faculty-and-research/academic-research/o/overcoming-the-inevitable-anchoring-effect--considering-the-opposi (accessed 2026-11-03)
