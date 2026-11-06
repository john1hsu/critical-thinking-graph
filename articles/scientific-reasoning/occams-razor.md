---
id: ct:occams-razor
type: Principle
title: Occam's razor
aliases: [Ockham's razor, principle of parsimony, law of parsimony, law of economy]
domain: scientific-reasoning
summary: >-
  The methodological principle that, other things being equal, you should
  prefer the explanation or theory that postulates fewer entities, causes or
  assumptions; it ranks rival hypotheses that fit the evidence equally well,
  and does not show that the simpler one is true.
level: introductory
evidenceStatus: normative
broader: [ct:philosophy-of-science]
related: [ct:inference-to-the-best-explanation, ct:falsifiability, ct:ad-hoc-hypothesis, ct:hypothesis-testing, ct:posterior-analytics, ct:overfitting]
requires: []
relations:
  - {predicate: introducedBy, object: ct:william-of-ockham, source: s2, confidence: medium}
  - {predicate: studiedIn, object: ct:philosophy-of-science, source: s1, confidence: high}
  - {predicate: formalizedBy, object: ct:akaike-information-criterion, source: s1, confidence: medium}
  - {predicate: contrastsWith, object: ct:hickams-dictum, source: s4, confidence: high}
  - {predicate: contrastsWith, object: ct:principle-of-plenitude, source: s1, confidence: medium}
  - {predicate: appliedIn, object: ct:medical-diagnosis, source: s4, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Simplicity"
    publisher: Stanford Encyclopedia of Philosophy (Baker, first published 2004, revised 2022)
    url: https://plato.stanford.edu/entries/simplicity/
    type: scholarly-encyclopedia
    accessed: 2026-11-06
  - id: s2
    title: "Occam's razor"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/topic/occams-razor
    type: encyclopedia
    accessed: 2026-11-06
  - id: s3
    title: "Simplicity and probability in causal explanation"
    publisher: Cognitive Psychology 55(3), 232-257 (Lombrozo, 2007), PubMed record
    url: https://pubmed.ncbi.nlm.nih.gov/17097080/
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s4
    title: "Occam's razor and Hickam's dictum: a dermatologic perspective"
    publisher: Diagnosis (Stein & Lowenstein, 2022), De Gruyter
    url: https://www.degruyterbrill.com/document/doi/10.1515/dx-2022-0093/html
    type: peer-reviewed
    accessed: 2026-11-06
created: 2026-11-06
---

# Occam's razor

Occam's razor, also called the principle or law of parsimony, says that when rival theories compete, the one that posits fewer entities should be preferred.[^s2] Contemporary philosophers read it as a rule of theory choice that applies only when other things are equal: if two hypotheses explain the evidence equally well, favour the more parsimonious one.[^s1] It is a guide to which hypothesis to work with first, not proof that the simpler hypothesis is true.[^s1]

Philosophers separate two kinds of simplicity that the razor can target. *Parsimony* (ontological simplicity) counts the kinds of things a theory says exist; *elegance* (syntactic simplicity) counts how many basic principles it needs and how compactly they are stated.[^s1] The two can pull apart: postulating the planet Neptune added an entity to astronomy but kept the laws of celestial mechanics unchanged.[^s1]

## Origin

The principle carries the name of the fourteenth-century Scholastic philosopher William of Ockham (c. 1285–1347/49), who used it so often and so sharply that it became attached to him; Britannica renders his phrasing as "plurality should not be posited without necessity".[^s2] He was not its inventor: Durandus of Saint-Pourçain invoked it earlier.[^s2] The familiar slogan "entities are not to be multiplied beyond necessity" is a later formulation that is only loosely tied to Ockham's own texts.[^s1]

Versions of the idea are much older and much newer. Aristotle, in the *Posterior Analytics*, preferred demonstrations that rest on fewer postulates; Aquinas held that nature does not use two instruments where one suffices; Newton's first rule of reasoning in the *Principia* admits no more causes than are true and sufficient to explain the phenomena.[^s1] Lavoisier used the same reasoning against phlogiston: if chemistry works without it, the substance is probably a gratuitous supposition.[^s1]

## How it works

Suppose a product team sees sign-ups fall 30% on the day a new website release ships. One analyst proposes a single cause: the release broke the sign-up tracking tag. Another proposes three independent ones at once: a seasonal dip, a competitor's campaign and a search-ranking change. If both accounts fit the data so far, the razor says to adopt the one-cause story as the working hypothesis and test it first, because it asks fewer things to have gone wrong together.[^s1] It does not say the one-cause story is correct. A quick check of the tag either confirms it or knocks it out, after which the more complex account earns attention.

The phrase *other things being equal* does a lot of work. The razor ranks hypotheses only when they explain the same facts equally well, a situation the Stanford entry describes as comparatively rare, so an appeal to parsimony often shifts the burden of proof rather than refuting the rival outright.[^s1]

## How to apply it

1. **Check the tie first.** Confirm that the rival explanations really account for the same evidence; a simpler story that leaves facts unexplained is not the parsimonious winner, it is the weaker one.[^s1]
2. **Count the right thing.** Say whether you are counting causes, kinds of entity or free parameters, since parsimony and elegance can disagree.[^s1]
3. **Treat the choice as provisional.** Use the simpler hypothesis to decide what to test next, and drop it when probability information clearly favours a complex explanation.[^s3]
4. **Watch for domains where many causes are normal.** In clinical diagnosis, the search for one unifying diagnosis is often useful but can hide a fuller picture; Hickam's dictum reminds clinicians that a patient can have several conditions at once.[^s4]

## Evidence and limitations

The razor is a normative principle, but how people actually use simplicity has been studied. A 2007 set of four experiments found that, other things equal, people prefer explanations invoking fewer causes, and that when simplicity and probability conflict they appear to give simpler explanations a higher prior, so a complex explanation needs disproportionately strong evidence to win; committing to a simple but unlikely explanation also led people to overestimate how common its cause was.[^s3] The same study found the preference could be overridden when probability information clearly favoured the complex explanation.[^s3]

Its philosophical justification is unsettled. Theological defences (Leibniz, Kepler, Newton) are now rarely accepted, appeals to scientific practice are hard to test cleanly, and Kuhn treated the weight given to simplicity as partly a matter of taste.[^s1] Statistical model selection gives the most precise version: the Akaike information criterion trades fit against the number of adjustable parameters, and Forster and Sober argue it justifies simplicity as a route to predictive accuracy rather than to truth.[^s1] Counter-principles also exist: Ockham's contemporary Walter of Chatton proposed an "anti-razor" for adding entities when fewer cannot do the job, and principles of plenitude conflict with the razor directly.[^s1]

## Connections

- **Philosophy of science** is the field that studies the razor as a principle of theory choice and debates its justification.[^s1]
- **William of Ockham** gives the principle its name, though earlier thinkers stated it.[^s2]
- **Akaike information criterion** gives parsimony a formal, quantitative treatment by penalising extra parameters.[^s1]
- **Hickam's dictum** is the clinical counterweight: in diagnosis, several concurrent conditions may be the right answer, so the search for one cause can mislead.[^s4]
- **Principle of plenitude** pulls in the opposite direction, favouring the existence of more kinds of thing.[^s1]
- **Inference to the best explanation**, **falsifiability**, **ad hoc hypotheses**, **overfitting** and **hypothesis testing** are related ideas about choosing between rival explanations; Aristotle's **Posterior Analytics** contains an early version of the preference for fewer postulates.[^s1]

## Sources

[^s1]: Baker, "Simplicity", Stanford Encyclopedia of Philosophy (rev. 2022). https://plato.stanford.edu/entries/simplicity/ (accessed 2026-11-06)
[^s2]: "Occam's razor", Encyclopaedia Britannica. https://britannica.com/topic/occams-razor (accessed 2026-11-06)
[^s3]: Lombrozo, "Simplicity and probability in causal explanation", Cognitive Psychology 55(3), 232-257 (2007). https://pubmed.ncbi.nlm.nih.gov/17097080/ (accessed 2026-11-06)
[^s4]: Stein & Lowenstein, "Occam's razor and Hickam's dictum: a dermatologic perspective", Diagnosis (2022). https://www.degruyterbrill.com/document/doi/10.1515/dx-2022-0093/html (accessed 2026-11-06)
