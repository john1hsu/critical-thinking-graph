---
id: ct:rsa-criteria
type: Framework
title: RSA criteria
aliases: [RSA triangle, ARS criteria, RAS criteria, relevance sufficiency acceptability, acceptability relevance and sufficiency]
domain: argumentation
summary: >-
  Johnson and Blair's three standards for a good argument, introduced in
  Logical Self-Defense (1977): each premise must be acceptable, each must be
  relevant to the conclusion, and together the premises must be sufficient to
  support it. A failure of any one marks a flawed or fallacious argument.
level: introductory
evidenceStatus: normative
broader: [ct:argument-evaluation]
related: [ct:cogency, ct:informal-logic, ct:non-sequitur, ct:hasty-generalization, ct:toulmin-model, ct:conductive-argument, ct:validity, ct:ignoratio-elenchi]
requires: [ct:argument]
relations:
  - {predicate: introducedBy, object: ct:ralph-h-johnson, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:j-anthony-blair, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:logical-self-defense, source: s4, confidence: high}
  - {predicate: detects, object: ct:non-sequitur, source: s1, confidence: medium}
  - {predicate: detects, object: ct:hasty-generalization, source: s1, confidence: medium}
  - {predicate: studiedIn, object: ct:informal-logic, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:validity, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Review of Groundwork in the Theory of Argumentation: Selected Papers of J. Anthony Blair"
    publisher: "David Hitchcock, Informal Logic 34(1), 2014, pp. 94-123"
    url: https://distantreader.org/stacks/journals/il/il-4120.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "The Significance of Informal Logic for Philosophy"
    publisher: "David Hitchcock, Informal Logic 20(2), 2000, pp. 129-138"
    url: https://distantreader.org/stacks/journals/il/il-2265.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "A probabilistic analysis of argument cogency"
    publisher: "David Godden and Frank Zenker, Synthese (2016), author's copy on PhilArchive"
    url: https://philarchive.org/archive/GODAPA-5
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Logically Defending for Publication: An Analysis of the Review Process of Logical Self-Defense"
    publisher: "Takuzo Konishi, ISSA Proceedings 2010 (Rozenberg Quarterly)"
    url: https://rozenbergquarterly.com/?p=7190
    type: academic
    accessed: 2026-11-18
  - id: s5
    title: "The Irrelevance of Relevance"
    publisher: "David Botting, Informal Logic 33(1), 2013, pp. 1-21"
    url: https://distantreader.org/stacks/journals/il/il-3493.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s6
    title: "Informal Logic (chapter 7 of the Handbook of Argumentation Theory)"
    publisher: "van Eemeren, Garssen, Krabbe, Snoeck Henkemans, Verheij and Wagemans, Springer, 2014"
    url: https://rd.springer.com/referenceworkentry/10.1007/978-90-481-9473-5_7
    type: textbook
    accessed: 2026-11-18
created: 2026-11-18
---

# RSA criteria

The RSA criteria are a three-part test for whether an argument is any good. Each premise should be **acceptable** (reasonable for the audience or evaluator to accept), each should be **relevant** to the conclusion, and the premises taken together should be **sufficient** to support it.[^s2] The order of the letters varies: textbooks speak of RSA, RAS or ARS criteria, and Trudy Govier's closely related "ARG" conditions rename sufficiency as "good grounds."[^s1][^s3] The point of the scheme is to judge everyday arguments without asking only whether they are deductively valid.[^s5]

## Origin

Ralph H. Johnson and J. Anthony Blair worked out the criteria in the mid-1970s, while building a classification of fallacies around three kinds of flaw: the problematic premise, the irrelevant reason and the hasty conclusion. Hitchcock describes the three standards as the contraries of those three flaws.[^s1] They became the organising framework of the pair's textbook *Logical Self-Defense*. A history of its review process reports that the manuscript was first turned down in 1975, then supported by second-round reviewers including Govier, and published in 1977.[^s4] That account calls the book one of the most influential introductory texts on argument appraisal and credits the triad with shaping both informal logic teaching and theory.[^s4] The criteria grew out of informal logicians' rejection of the idea that a good argument is simply a valid one, which they argued gives false positives (valid but useless arguments) and false negatives (strong arguments that are not deductively valid).[^s5]

## How it works

Take a workplace case. A team lead argues: "We should move the release to Friday. Two of our five testers are on leave this week, the last release that skipped regression testing produced a week of hot-fixes, and Friday is the quietest support day." Applying the criteria in the order Hitchcock lists them:[^s2]

1. **Acceptability.** Is it reasonable to accept each premise? The leave calendar and the hot-fix history can be checked, so both pass. Hitchcock notes that a premise can be acceptable without being true, if the evaluator has good reason to accept it.[^s2]
2. **Relevance.** Does each premise bear on the conclusion? Fewer testers and a past failure without testing both bear on whether to delay. Whether Friday is quiet bears on *which* day, not on *whether* to delay.
3. **Sufficiency.** Do the premises together give enough support? Hitchcock calls this criterion true but schematic, and suggests Toulmin's warrants as one way to make it concrete: a firm conclusion needs a nearly exceptionless warrant, while a tentative one can rest on a warrant that only usually holds.[^s2] Here the case is reasonable but would be stronger with an estimate of what the delay costs.

A probabilistic reading by Godden and Zenker makes the three standards precise. A reason is relevant if it raises the probability of the claim, sufficient if it lifts the claim above a threshold of acceptance, and acceptable if the reason itself clears a threshold.[^s3] On their analysis the three are not independent: sufficiency, properly stated, already implies positive relevance.[^s3]

## How to apply it

- **Diagnose fallacies by which criterion fails.** Johnson and Blair treated a fallacy as a violation of one or more of the three standards.[^s3] An argument whose premises have no bearing on its conclusion fails relevance; one that leaps from thin evidence fails sufficiency; one that rests on a doubtful claim fails acceptability.[^s1] This gives a way to classify faulty arguments without first deciding whether the argument was meant to be deductive or inductive.[^s4]
- **Judge sufficiency on the whole set.** Johnson stressed that sufficiency applies to all the premises together, not one at a time.[^s3] Godden and Zenker show why this matters: four reasons that are each too weak can jointly raise a claim's probability from about 0.17 to about 0.61, so rejecting each in isolation would be a mistake.[^s3]
- **Fix the standard to the context.** Blair later held that the bar for acceptability and sufficiency depends on purpose: a justificatory argument is judged by the standards of its field, a persuasive one by those of its intended audience.[^s1]

## Limitations

Critics find the criteria easier to state than to apply. The *Handbook of Argumentation Theory* reports the complaint that relevance is too vague and lacks a satisfactory account, and notes the tension that a premise may be false yet acceptable, or true yet unacceptable.[^s6] Botting goes further, arguing that a general theory of relevance is neither possible nor needed, and that intuitive relevance judgments can do their work unanalysed.[^s5] Blair himself came to call acceptability and sufficiency largely placeholders and, persuaded by Christopher Tindale, accepted that the triad is an unstable basis for a full theory of fallacy. He still judged the criteria useful for organising thought about what makes an argument good.[^s1] Derek Allen has objected that the scheme mixes an epistemic standard for premises with an ontic standard for the premise-conclusion link.[^s1]

## Connections

- **Broader: argument evaluation.** The criteria are one of the main informal-logic answers to how arguments should be appraised, and the field's handbook treats them as Johnson and Blair's core evaluative contribution.[^s6][^s2]
- **Introduced by Ralph H. Johnson and J. Anthony Blair, in *Logical Self-Defense*.** Hitchcock traces the criteria to the pair's mid-1970s fallacy work, and Konishi to the 1977 book.[^s1][^s4]
- **Detects non sequitur and hasty generalization.** The irrelevant reason and the hasty conclusion are two of the three flaws the criteria were built to name. A conclusion that does not follow from its reasons fails relevance or sufficiency, and a sweeping conclusion from too little evidence fails sufficiency.[^s1][^s3]
- **Studied in informal logic.** Hitchcock presents the triad as a popular set of informal-logic criteria and discusses which of them are really necessary.[^s2]
- **Contrasts with validity.** The RSA model arose to replace validity as the sole test of a good argument, since validity alone misclassifies arguments in both directions.[^s5]

## Sources

[^s1]: Hitchcock, review of *Groundwork in the Theory of Argumentation: Selected Papers of J. Anthony Blair*, *Informal Logic* 34(1), 2014. https://distantreader.org/stacks/journals/il/il-4120.pdf (accessed 2026-11-18)
[^s2]: Hitchcock, "The Significance of Informal Logic for Philosophy", *Informal Logic* 20(2), 2000. https://distantreader.org/stacks/journals/il/il-2265.pdf (accessed 2026-11-18)
[^s3]: Godden and Zenker, "A probabilistic analysis of argument cogency", *Synthese*, 2016. https://philarchive.org/archive/GODAPA-5 (accessed 2026-11-18)
[^s4]: Konishi, "Logically Defending for Publication: An Analysis of the Review Process of Logical Self-Defense", ISSA Proceedings 2010. https://rozenbergquarterly.com/?p=7190 (accessed 2026-11-18)
[^s5]: Botting, "The Irrelevance of Relevance", *Informal Logic* 33(1), 2013. https://distantreader.org/stacks/journals/il/il-3493.pdf (accessed 2026-11-18)
[^s6]: van Eemeren et al., "Informal Logic", *Handbook of Argumentation Theory*, Springer, 2014. https://rd.springer.com/referenceworkentry/10.1007/978-90-481-9473-5_7 (accessed 2026-11-18)
