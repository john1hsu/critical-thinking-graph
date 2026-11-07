---
id: ct:inference-to-the-best-explanation
type: ReasoningForm
title: Inference to the best explanation
aliases: [IBE, abduction, abductive reasoning, abductive inference]
domain: foundations
summary: >-
  The non-deductive inference that accepts a hypothesis because, among the
  available rivals, it would best explain the evidence; in its modern sense
  it is the standard meaning of "abduction".
level: introductory
evidenceStatus: normative
broader: [ct:reasoning]
related: [ct:occams-razor, ct:hypothesis-testing, ct:affirming-the-consequent, ct:bayesian-reasoning, ct:explanatory-virtues]
requires: [ct:argument]
relations:
  - {predicate: contrastsWith, object: ct:inductive-reasoning, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:deductive-reasoning, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:gilbert-harman, source: s3, confidence: medium}
  - {predicate: influencedBy, object: ct:charles-sanders-peirce, source: s2, confidence: medium}
  - {predicate: challengedBy, object: ct:bad-lot-objection, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:medical-diagnosis, source: s1, confidence: medium}
  - {predicate: studiedIn, object: ct:cognitive-psychology, source: s4, confidence: high}
argumentMap:
  premises:
    - "Since Tuesday's deploy, the checkout service has been timing out, but only for requests that hit the new discount code path."
    - "A bad database index added in that deploy would explain both the timing and why only the discount path is slow."
    - "The rival explanations (a network fault, a traffic spike, a third-party outage) would slow every path, and monitoring shows normal traffic and healthy vendors."
    - "The index explanation is a good explanation in its own right: it is specific and testable."
  conclusion: "The new index is probably causing the timeouts, so it is the hypothesis to act on and test first."
  verdict: strong
  objections:
    - "The rival list may be a bad lot: an untried cause, such as a changed cache setting in the same deploy, could explain the pattern better."
    - "Rolling back the index and watching the timeouts is a test the inference recommends, not one it replaces."
sources:
  - id: s1
    title: "Abduction"
    publisher: Stanford Encyclopedia of Philosophy (Douven, rev. 2025)
    url: https://plato.stanford.edu/entries/abduction
    type: scholarly-encyclopedia
    accessed: 2026-11-07
  - id: s2
    title: "Peirce on Abduction (supplement to Abduction)"
    publisher: Stanford Encyclopedia of Philosophy (Douven)
    url: https://plato.stanford.edu/entries/abduction/peirce.html
    type: scholarly-encyclopedia
    accessed: 2026-11-07
  - id: s3
    title: "The Inference to the Best Explanation"
    publisher: Philosophical Review 74(1), 88-95 (Harman, 1965); PhilArchive record
    url: https://dc2.philarchive.org/rec/HARTIT-2
    type: primary
    accessed: 2026-11-07
  - id: s4
    title: "Explanatory Preferences Shape Learning and Inference"
    publisher: Trends in Cognitive Sciences 20(10), 748-759 (Lombrozo, 2016)
    url: https://cognition.princeton.edu/sites/default/files/cognition/files/explanatory_prefs_tics.pdf
    type: peer-reviewed
    accessed: 2026-11-07
created: 2026-11-07
---

# Inference to the best explanation

Inference to the best explanation (IBE) is the move from a body of evidence to the hypothesis that would explain it better than any rival.[^s1] It is what philosophers today usually mean by "abduction".[^s1] Like induction, it is ampliative and fallible: the conclusion goes beyond what the premises guarantee.[^s1] Unlike simple induction, which projects frequencies, it rests on explanatory considerations, asking which story would make the evidence expected.[^s1] It runs through everyday reasoning, scientific discovery and medical diagnosis.[^s1]

## Origin

Charles Sanders Peirce coined "abduction" for a kind of inference he set apart from both deduction and induction.[^s2] His schema runs: a surprising fact is observed; if a hypothesis were true, the fact would be a matter of course; so there is reason to suspect the hypothesis.[^s2] For Peirce this belonged to the discovery stage, generating ideas worth testing, and he never spoke of the *best* explanation.[^s2] Gilbert Harman's 1965 paper in the *Philosophical Review*, titled "The Inference to the Best Explanation", gave the modern label.[^s3] The modern notion shifted abduction to the justification stage, where hypotheses are assessed rather than merely proposed.[^s1] Peter Lipton's book of the same name (1991; 2nd ed. 2004) gave the fullest defence of combining IBE with Bayesian reasoning.[^s1]

## How it works

The textbook rule says: given evidence and a set of candidate explanations, infer that the one that best explains the evidence is true.[^s1] Douven's entry argues this is too strong. A refined version adds a threshold: infer the best explanation only if it is also good enough as an explanation in its own right.[^s1] A third version infers only that the best explanation is closer to the truth than its rivals.[^s1]

The argument map above shows a workplace case. Checkout requests started timing out after a deploy, but only on the discount-code path. A bad new index explains both the timing and the narrow pattern. The rivals (a network fault, a traffic spike, a vendor outage) would slow everything and are contradicted by monitoring. The index hypothesis is also specific and testable, so it passes the "good enough" bar.[^s1] The verdict is "strong", not "valid": like Neptune, inferred by Adams and Leverrier to explain Uranus's orbit before it was seen, the conclusion earns belief and further testing, not certainty.[^s1] IBE is also non-monotonic: a new fact, such as a cache setting changed in the same deploy, can overturn it without any premise becoming false.[^s1]

## How to apply it

1. Write down the evidence to be explained, including the awkward details; narrow patterns often discriminate between rivals best.[^s1]
2. Generate several rival explanations before judging any of them, because the best of a poor set can still be wrong.[^s1]
3. Compare rivals on how well each makes the evidence expected, and check the winner is a satisfactory explanation on its own.[^s1]
4. Watch for appealing but improbable stories. People favour simpler explanations even when a more complex one is equally or more likely.[^s4]
5. Treat the conclusion as the hypothesis to test next, and revise it when new evidence arrives.[^s1][^s2]

## Evidence

As a normative standard IBE faces four standard objections, summarised in the Stanford entry.[^s1] Van Fraassen's "bad lot" objection notes that the best of the hypotheses we happened to consider may still be false. Critics also argue that explanatory rules can clash with Bayesian coherence. Arguments for IBE's reliability are also said to be rule-circular.[^s1] Lipton and others reply that explanatory considerations can guide Bayesian priors and likelihoods rather than compete with them.[^s1]

Psychologists have studied how people actually weigh explanations. Lombrozo's 2016 review in *Trends in Cognitive Sciences* reports that adults chose a simpler explanation even when a complex one was equally likely. In her 2007 study, the complex option needed roughly ten times the probability before most people chose it.[^s4] People also favour broad explanations and those with narrow "latent scope", meaning fewer unverified predictions.[^s4] Prompting people to explain can help them find real patterns but can also push them to over-generalise when none exists.[^s4] Experimental work also shows that people overrate the likelihood of events they can readily explain.[^s1] The Stanford entry calls the empirical picture suggestive but limited.[^s1]

## Connections

- **Contrasts with inductive reasoning.** Both are ampliative, but IBE relies on explanatory considerations rather than frequencies alone.[^s1]
- **Contrasts with deductive reasoning.** Its conclusions are not necessitated by its premises and can be defeated by new information.[^s1]
- **Introduced by Gilbert Harman.** His 1965 *Philosophical Review* paper named the inference.[^s3]
- **Influenced by Charles Sanders Peirce.** Peirce's abduction is the historical ancestor, though it concerned generating hypotheses rather than justifying them.[^s2]
- **Challenged by the bad lot objection.** Van Fraassen's objection targets the inference from "best available" to "true".[^s1]
- **Applied in medical diagnosis.** Physicians tend to favour the hypothesis that best explains a patient's symptoms.[^s1]
- **Studied in cognitive psychology.** Experiments on simplicity, breadth and latent scope measure how people judge explanations.[^s4]

## Sources

[^s1]: Douven, "Abduction", Stanford Encyclopedia of Philosophy, rev. 2025. https://plato.stanford.edu/entries/abduction (accessed 2026-11-07)
[^s2]: Douven, "Peirce on Abduction", supplement to "Abduction", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/abduction/peirce.html (accessed 2026-11-07)
[^s3]: Harman, "The Inference to the Best Explanation", *Philosophical Review* 74(1) (1965), 88-95. https://dc2.philarchive.org/rec/HARTIT-2 (accessed 2026-11-07)
[^s4]: Lombrozo, "Explanatory Preferences Shape Learning and Inference", *Trends in Cognitive Sciences* 20(10) (2016), 748-759. https://cognition.princeton.edu/sites/default/files/cognition/files/explanatory_prefs_tics.pdf (accessed 2026-11-07)
