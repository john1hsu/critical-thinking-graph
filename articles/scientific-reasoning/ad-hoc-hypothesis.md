---
id: ct:ad-hoc-hypothesis
type: Concept
title: Ad hoc hypothesis
aliases: [ad hoc rescue, ad hoc auxiliary hypothesis, ad hoc modification, ad hocness]
domain: scientific-reasoning
summary: >-
  An auxiliary assumption added to a theory only to accommodate evidence that
  would otherwise refute it, with no independent support and no new testable
  consequences of its own; it protects the theory instead of extending it.
level: intermediate
evidenceStatus: normative
broader: [ct:scientific-method]
related: [ct:falsifiability, ct:karl-popper, ct:duhem-quine-thesis, ct:no-true-scotsman, ct:occams-razor, ct:hypothesis-testing]
requires: [ct:falsifiability]
relations:
  - {predicate: explainedBy, object: ct:duhem-quine-thesis, source: s4, confidence: high}
  - {predicate: contrastsWith, object: ct:falsifiability, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:inference-to-the-best-explanation, source: s2, confidence: medium}
  - {predicate: studiedIn, object: ct:philosophy-of-science, source: s3, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Karl Popper: Philosophy of Science"
    publisher: Internet Encyclopedia of Philosophy (Shea)
    url: https://iep.utm.edu/pop-sci/
    type: scholarly-encyclopedia
    accessed: 2026-11-13
  - id: s2
    title: "The Magic of Ad Hoc Solutions"
    publisher: Journal of the American Philosophical Association 9(4) (Smid, 2023)
    url: https://www.cambridge.org/core/product/244434941F3F11E1AB9BE7A50240A071/core-reader
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "On Ad Hoc Hypotheses"
    publisher: Philosophy of Science 79(1) (Hunt, 2012)
    url: https://cambridge.org/core/journals/philosophy-of-science/article/on-ad-hoc-hypotheses/EE289E1F40825CEEB93B7F3DD12AC201
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "Underdetermination of Scientific Theory"
    publisher: Stanford Encyclopedia of Philosophy (Stanford, rev. 2023)
    url: https://plato.stanford.edu/entries/scientific-underdetermination/
    type: scholarly-encyclopedia
    accessed: 2026-11-13
  - id: s5
    title: "Philosophical perspectives on ad hoc hypotheses and the Higgs mechanism"
    publisher: arXiv (Friederich, Harlander and Karaca)
    url: https://arxiv.org/pdf/1305.5110
    type: preprint
    accessed: 2026-11-13
created: 2026-11-13
---

# Ad hoc hypothesis

An ad hoc hypothesis is an extra assumption bolted onto a theory for one purpose: to explain away an observation that contradicts it. In Karl Popper's influential treatment, what makes such an assumption illegitimate is that it yields no new predictions that could themselves be checked, so its only effect is to shield the theory from refutation.[^s1] Not every rescue is ad hoc. Adding an assumption is a normal and often fruitful move in science; the trouble starts when the assumption is supported by nothing except the anomaly it was invented to absorb.[^s4][^s5]

## Origin

The worry follows from a point made by Pierre Duhem: hypotheses are never tested alone but in bundles with auxiliary assumptions, so a failed prediction shows only that something in the bundle is wrong, not which part.[^s4] W. V. Quine pushed this further, holding that almost any belief can be kept if enough adjustments are made elsewhere, while conceding that many such adjustments strike us as ad hoc.[^s4] Popper popularised the term in the philosophy of science and turned it into a methodological rule: rescue a theory only with auxiliary hypotheses that can be tested independently.[^s5][^s1] He charged that defenders of Marxism had broken this rule, blaming failed forecasts on unspecified counter-revolutionary activity that predicted nothing new.[^s1]

Later philosophers tried to define the notion more precisely. Jarrett Leplin (1975) proposed conditions under which a hypothesis counts as ad hoc, centred on its being introduced in response to an experimental anomaly that provides its only support.[^s5] Adolf Grünbaum argued that ad hocness is time-relative: a hypothesis can shed the label once later evidence confirms it.[^s5] More recently Jan Smid (2023) has argued that an ad hoc solution is one that removes a problem without explaining it, where an explanation could reasonably be demanded.[^s2]

## How it works

The textbook contrast is two planetary anomalies. When Uranus strayed from its predicted orbit, astronomers did not abandon Newtonian mechanics; they posited an unseen planet, which was then looked for and found as Neptune in 1846.[^s1][^s4] When the same strategy was tried for Mercury's orbit, the hypothesised planet Vulcan was never found, and the anomaly was eventually explained by general relativity.[^s4] Both rescues added an assumption; the Neptune hypothesis stopped being suspect because it made an independently checkable prediction that came true.[^s1][^s5]

A workplace version: a product team predicts that a redesigned checkout page will raise conversions. The A/B test shows no lift. Someone suggests that the test week happened to attract unusually indecisive shoppers. If that claim comes with a check (for example, comparing visitor mix with previous weeks, or re-running the test), it is a legitimate auxiliary hypothesis. If it is offered with no way to check it, and the team quietly decides the redesign still works, it is ad hoc: the only evidence for the indecisive shoppers is the failed prediction they were invented to excuse.[^s1][^s5]

## How to recognise it

- **Timing and motive.** Was the assumption introduced only after the contrary result, specifically to accommodate it?[^s5]
- **Independent support.** Is there any reason to believe it apart from the anomaly it removes?[^s5]
- **New consequences.** Does it predict anything else that could turn out false? Popper's test is whether it adds testable content or subtracts it.[^s1]
- **Explanation.** Does it say why the problem arose, or merely make the problem disappear?[^s2]

## Limitations of the concept

Philosophers disagree about whether ad hocness can be defined at all. J. Christopher Hunt (2012) reviewed the accounts of Popper, Leplin and Gerald Holton and argued that judgements of ad hocness rest largely on individual scientists' aesthetic sense, and that a hypothesis can be reclassified as non-ad hoc once later data arrive, which he took to undermine the term's usefulness.[^s3] Smid replies that testability is the wrong criterion: the Lorentz–FitzGerald contraction, a standard example of an ad hoc hypothesis, did have testable consequences, and he locates its defect in its lack of explanation instead.[^s2] Since even successful auxiliaries such as Neptune began with only one piece of support, the label is best applied with hindsight and with attention to whether the rescue was later tested.[^s4][^s5]

## Connections

- **Duhem–Quine thesis:** holism about testing explains why an ad hoc rescue is always logically available, since evidence never singles out one hypothesis for blame.[^s4]
- **Falsifiability:** an ad hoc rescue works against falsifiability by reducing what the rescued theory forbids, which is why Popper treated it as a move out of science.[^s1]
- **Inference to the best explanation:** Smid's account defines ad hoc solutions as non-explanatory fixes, the opposite of accepting a hypothesis because it explains well.[^s2]
- **Philosophy of science:** the concept is a long-running object of analysis in the field, from Popper and Leplin to Hunt and Smid.[^s3][^s2]

## Sources

[^s1]: Shea, "Karl Popper: Philosophy of Science", Internet Encyclopedia of Philosophy. https://iep.utm.edu/pop-sci/ (accessed 2026-11-13)
[^s2]: Smid, "The Magic of Ad Hoc Solutions", Journal of the American Philosophical Association 9(4), 2023, doi:10.1017/apa.2022.27. https://www.cambridge.org/core/product/244434941F3F11E1AB9BE7A50240A071/core-reader (accessed 2026-11-13)
[^s3]: Hunt, "On Ad Hoc Hypotheses", Philosophy of Science 79(1), 2012, doi:10.1086/663238. https://cambridge.org/core/journals/philosophy-of-science/article/on-ad-hoc-hypotheses/EE289E1F40825CEEB93B7F3DD12AC201 (accessed 2026-11-13)
[^s4]: Stanford, "Underdetermination of Scientific Theory", Stanford Encyclopedia of Philosophy (rev. 2023). https://plato.stanford.edu/entries/scientific-underdetermination/ (accessed 2026-11-13)
[^s5]: Friederich, Harlander and Karaca, "Philosophical perspectives on ad hoc hypotheses and the Higgs mechanism", arXiv. https://arxiv.org/pdf/1305.5110 (accessed 2026-11-13)
