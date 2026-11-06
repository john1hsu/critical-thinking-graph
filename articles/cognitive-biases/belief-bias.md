---
id: ct:belief-bias
type: CognitiveBias
title: Belief bias
aliases: [belief-bias effect, belief bias in syllogistic reasoning]
domain: cognitive-biases
summary: >-
  The tendency to judge whether an argument is logically valid by whether its
  conclusion is believable, so that believable conclusions are accepted from
  invalid arguments and unbelievable ones are rejected from valid arguments.
level: intermediate
evidenceStatus: robust
broader: [ct:cognitive-bias]
related: [ct:validity, ct:syllogism, ct:deductive-reasoning, ct:undistributed-middle, ct:dual-process-theory, ct:confirmation-bias, ct:debiasing]
requires: [ct:validity, ct:syllogism]
relations:
  - {predicate: demonstratedBy, object: ct:evans-barston-pollard-1983-belief-bias-experiments, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:dual-process-theory, source: s2, confidence: medium}
  - {predicate: amplifiedBy, object: ct:time-pressure, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:trippas-2018-belief-bias-meta-analysis, source: s4, confidence: high}
  - {predicate: challengedBy, object: ct:dube-rotello-heit-2010-belief-bias-roc-study, source: s3, confidence: medium}
sources:
  - id: s1
    title: "On the conflict between logic and belief in syllogistic reasoning"
    publisher: Memory & Cognition 11(3), 295-306 (Evans, Barston & Pollard, 1983), Springer
    url: https://link.springer.com/content/pdf/10.3758/bf03196976.pdf
    type: primary
    accessed: 2026-11-06
  - id: s2
    title: "Rapid responding increases belief bias: Evidence for the dual-process theory of reasoning"
    publisher: Thinking & Reasoning 11(4), 382-389 (Evans & Curtis-Holmes, 2005)
    url: https://informahealthcare.com/doi/full/10.1080/13546780542000005
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s3
    title: "Assessing the belief bias effect with ROCs: It's a response bias effect"
    publisher: Psychological Review 117(3), 831-863 (Dube, Rotello & Heit, 2010), university library catalogue record
    url: https://vufind-test.katalog.k.utb.cz/SummonRecord/FETCH-LOGICAL-a449t-bd7d2d851ffbda65a5214be8ca550833263bd2cd65d5d0ec6373d455ef9fd1662
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s4
    title: "Characterizing belief bias in syllogistic reasoning: A hierarchical Bayesian meta-analysis of ROC data"
    publisher: Psychonomic Bulletin & Review 25(6), 2141-2174 (Trippas, Kellen, Singmann, Pennycook, Koehler, Fugelsang & Dube, 2018), UCL Discovery
    url: https://discovery.ucl.ac.uk/id/eprint/10107864/
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s5
    title: "Debiasing by instruction: The case of belief bias"
    publisher: European Journal of Cognitive Psychology 6(3), 263-285 (Evans, Newstead, Allen & Pollard, 1994), Leeds Trinity University research portal
    url: https://research.leedstrinity.ac.uk/en/publications/debiasing-by-instruction-the-case-of-belief-bias/
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s6
    title: "How to Get Rid of the Belief Bias: Boosting Analytical Thinking via Pragmatics"
    publisher: Europe's Journal of Psychology 15(3), 595-613 (Caravona, Macchi, Poli, Vezzoli, Franchella & Bagassi, 2019)
    url: https://ejop.psychopen.eu/index.php/ejop/article/view/1794
    type: peer-reviewed
    accessed: 2026-11-06
created: 2026-11-06
---

# Belief bias

Belief bias is the tendency to evaluate an argument by asking "do I agree with the conclusion?" instead of "does the conclusion follow from the premises?" People accept believable conclusions more often than unbelievable ones, regardless of logical validity, even when told to judge only whether the conclusion necessarily follows.[^s1] It matters for critical thinking because validity is a property of an argument's form, and a reader who lets belief stand in for form will wave through weak arguments for congenial conclusions and dismiss sound arguments for surprising ones.[^s1][^s5]

## Origin

The modern study of the effect is anchored in three experiments by Jonathan Evans, Julie Barston and Paul Pollard, published in *Memory & Cognition* in 1983. They crossed logical validity with conclusion believability in categorical syllogisms and controlled for rival explanations such as illicit conversion of premises and response bias toward a particular term order.[^s1] Belief bias appeared in every experiment alongside a genuine effect of validity, and the two factors interacted: belief swayed judgments of invalid syllogisms more than judgments of valid ones.[^s1] The authors concluded that logic and belief conflict throughout the task, and that existing models of syllogistic reasoning had no account of such content effects.[^s1]

## How it works

In the 1983 experiments, acceptance of invalid arguments with believable conclusions ran between 66% and 92%, against 6% to 13% for invalid arguments with unbelievable conclusions.[^s1] When logic and belief pointed the same way, people answered correctly about nine times in ten; when they conflicted, accuracy fell to roughly a quarter to a half.[^s1] Think-aloud protocols helped explain why. People who started from the conclusion and only glanced back at the premises showed the most belief bias, while those who reasoned forward from premises to conclusion showed the least.[^s1]

A workplace example: a manager reads "All successful product launches had a dedicated marketing budget. Our launch had a dedicated marketing budget. So our launch will be successful." The conclusion is welcome, so the argument feels sound, yet it commits the undistributed middle: many failed launches also had marketing budgets. Flip the content to "...so our launch will fail" and the same manager spots the gap at once. Same form, different verdict, driven by belief.[^s1]

## Evidence

Dual-process theorists treat belief bias as a key test case. In a 2005 study, Evans and Curtis-Holmes gave one group unlimited time and forced another to respond within 10 seconds. Time pressure substantially increased belief bias and reduced logically correct answers, which they took as evidence that fast intuitive processing drives belief-based responses while slower analytic processing is needed to override them.[^s2]

What the effect actually is has been disputed. Dube, Rotello and Heit (2010) used confidence ratings and signal detection analysis across three experiments. Their ROC curves were curved, which contradicts the threshold assumptions behind the standard interaction measure and the multinomial model of Klauer, Musch and Naumer (2000).[^s3] They argued belief bias is a response bias, a shift in willingness to say "valid", and that the famous validity-by-belief interaction was probably a Type I error of linear analysis.[^s3] A 2018 hierarchical Bayesian meta-analysis of 22 confidence-rating studies (N = 993) reanalysed the question. It found that believability does not change people's ability to discriminate valid from invalid forms unconditionally, and that individual differences moderate the effect.[^s4] The tendency to endorse believable conclusions is therefore well replicated; whether belief also degrades reasoning accuracy, and for whom, remains contested.[^s3][^s4]

## How to spot it

- You feel confident an argument "works" but cannot say which premise licenses the conclusion.[^s1]
- You judge an argument differently after its topic or conclusion is swapped while the structure stays the same.[^s1]
- You started from the conclusion and searched the premises for support, rather than working forward from the premises.[^s1]
- You are deciding quickly, under deadline pressure, where belief-based answers become more likely.[^s2]

## How to counter it

Simple exhortation is weak. Evans, Newstead, Allen and Pollard (1994) found that belief bias survived instructions that stressed logical necessity in two experiments, though more elaborated instructions in a third experiment reduced it without eliminating it.[^s5] Caravona and colleagues (2019) noted that many debiasing attempts had failed or not replicated, and reported a strong accuracy gain from rewording the task instructions so that the communicative intent of the question was clear, in both logic-trained and untrained participants.[^s6] Practical moves that follow from this work: give yourself time, since speed raises belief bias;[^s2] restate the argument with neutral or nonsense terms and check whether it still follows;[^s1] reason forward from the premises before looking at the conclusion;[^s1] and frame the question explicitly as one about what must follow, not what is true.[^s5][^s6]

## Connections

- **Broader: cognitive bias.** Belief bias is a systematic judgment error in deductive reasoning, where prior beliefs intrude on assessments of logical validity.[^s1]
- **Requires validity and the syllogism.** The effect is defined against the standard of validity and was measured mainly with categorical syllogisms.[^s1]
- **Demonstrated by the Evans, Barston and Pollard (1983) experiments,** which showed belief and validity effects and their interaction under tight controls.[^s1]
- **Explained by dual-process theory** in the account of Evans and Curtis-Holmes, where intuitive processing produces belief-based answers and analytic processing must override them.[^s2]
- **Amplified by time pressure.** Forcing rapid responses increased belief bias and cut logical accuracy.[^s2]
- **Supported by the Trippas et al. (2018) meta-analysis** of 22 studies, which confirms the endorsement effect while qualifying claims about accuracy.[^s4]
- **Challenged by Dube, Rotello and Heit (2010),** whose signal detection analysis recasts the effect as a response bias and questions the accuracy interaction.[^s3]
- **Related to the undistributed middle, deductive reasoning, confirmation bias and debiasing.** Invalid forms with believable conclusions are the classic test items, and instruction-based debiasing has been tried with partial success.[^s1][^s5][^s6]

## Sources

[^s1]: J. St. B. T. Evans, J. L. Barston & P. Pollard, "On the conflict between logic and belief in syllogistic reasoning", *Memory & Cognition* 11(3), 1983, 295–306. https://link.springer.com/content/pdf/10.3758/bf03196976.pdf (accessed 2026-11-06)
[^s2]: J. St. B. T. Evans & J. Curtis-Holmes, "Rapid responding increases belief bias: Evidence for the dual-process theory of reasoning", *Thinking & Reasoning* 11(4), 2005, 382–389. https://informahealthcare.com/doi/full/10.1080/13546780542000005 (accessed 2026-11-06)
[^s3]: C. Dube, C. M. Rotello & E. Heit, "Assessing the belief bias effect with ROCs: It's a response bias effect", *Psychological Review* 117(3), 2010, 831–863. https://vufind-test.katalog.k.utb.cz/SummonRecord/FETCH-LOGICAL-a449t-bd7d2d851ffbda65a5214be8ca550833263bd2cd65d5d0ec6373d455ef9fd1662 (accessed 2026-11-06)
[^s4]: D. Trippas, D. Kellen, H. Singmann, G. Pennycook, D. J. Koehler, J. A. Fugelsang & C. Dube, "Characterizing belief bias in syllogistic reasoning: A hierarchical Bayesian meta-analysis of ROC data", *Psychonomic Bulletin & Review* 25(6), 2018, 2141–2174. https://discovery.ucl.ac.uk/id/eprint/10107864/ (accessed 2026-11-06)
[^s5]: J. St. B. T. Evans, S. E. Newstead, J. L. Allen & P. Pollard, "Debiasing by instruction: The case of belief bias", *European Journal of Cognitive Psychology* 6(3), 1994, 263–285. https://research.leedstrinity.ac.uk/en/publications/debiasing-by-instruction-the-case-of-belief-bias/ (accessed 2026-11-06)
[^s6]: L. Caravona, L. Macchi, F. Poli, M. Vezzoli, M. A. G. Franchella & M. Bagassi, "How to Get Rid of the Belief Bias: Boosting Analytical Thinking via Pragmatics", *Europe's Journal of Psychology* 15(3), 2019, 595–613. https://ejop.psychopen.eu/index.php/ejop/article/view/1794 (accessed 2026-11-06)
