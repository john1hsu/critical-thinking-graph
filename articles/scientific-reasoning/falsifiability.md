---
id: ct:falsifiability
type: Principle
title: Falsifiability criterion
aliases: [falsifiability, refutability, falsificationism, Popper's demarcation criterion, criterion of falsifiability]
domain: scientific-reasoning
summary: >-
  Karl Popper's proposal that a claim or theory counts as scientific only if
  some possible observation could show it to be false; a theory that is
  compatible with every conceivable outcome tells us nothing testable about
  the world.
level: introductory
evidenceStatus: normative
broader: [ct:scientific-method]
related: [ct:karl-popper, ct:problem-of-induction, ct:modus-tollens, ct:pseudoscience, ct:ad-hoc-hypothesis, ct:hypothesis-testing]
requires: [ct:modus-tollens]
relations:
  - {predicate: introducedBy, object: ct:karl-popper, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:the-logic-of-scientific-discovery, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:verifiability-criterion, source: s2, confidence: high}
  - {predicate: challengedBy, object: ct:duhem-quine-thesis, source: s4, confidence: high}
  - {predicate: challengedBy, object: ct:methodology-of-scientific-research-programmes, source: s2, confidence: medium}
  - {predicate: studiedIn, object: ct:philosophy-of-science, source: s2, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Karl Popper"
    publisher: Stanford Encyclopedia of Philosophy (Thornton, rev. 2026)
    url: https://plato.stanford.edu/entries/popper/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
  - id: s2
    title: "Science and Pseudo-Science"
    publisher: Stanford Encyclopedia of Philosophy (Hansson, rev. 2025)
    url: https://plato.stanford.edu/entries/pseudo-science/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
  - id: s3
    title: "Popper, Karl: Philosophy of Science"
    publisher: Internet Encyclopedia of Philosophy
    url: https://iep.utm.edu/pop-sci/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
  - id: s4
    title: "Underdetermination of Scientific Theory"
    publisher: Stanford Encyclopedia of Philosophy (Stanford, rev. 2023)
    url: https://plato.stanford.edu/entries/scientific-underdetermination/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
created: 2026-11-04
---

# Falsifiability criterion

The falsifiability criterion holds that a theory is scientific only if it is incompatible with some possible observation: it must forbid something, so that the world could in principle show it wrong.[^s1] Popper offered it as an answer to the *demarcation problem*, the question of what separates science from non-science, and stressed that falsifiability depends on the logical form of a claim, not on whether anyone has yet tested it.[^s2] A non-falsifiable idea is not thereby meaningless or worthless on his view; it simply is not an empirical scientific claim.[^s3]

## Origin

Karl Popper set out the criterion in *Logik der Forschung* (Vienna: Springer, imprint 1935), later translated by him as *The Logic of Scientific Discovery* (1959).[^s1][^s3] The book was aimed largely at the Vienna Circle, whose members had proposed around 1930 that meaningful scientific statements are those that can, at least in principle, be verified.[^s2][^s3] Popper rejected verifiability and replaced it with falsifiability.[^s2] He also accepted Hume's argument that induction cannot be justified, but denied that this leaves science without a method: science, he argued, proceeds by bold conjectures exposed to severe tests.[^s1]

## How it works

The criterion rests on a logical asymmetry. No finite number of observations can verify a universal claim, yet a single genuine counter-instance refutes it.[^s1] Many white swans do not prove "all swans are white"; one black swan disproves it.[^s3] The refutation has the shape of modus tollens: if the theory is true, this observation should occur; it did not occur; so the theory (or something it was tested with) is false.

Popper's own contrast cases made the idea vivid. Einstein's relativity predicted that starlight would bend near the sun by a definite amount, so Eddington's 1919 eclipse measurements could have sunk it; that riskiness is what made it scientific.[^s1] By contrast, Popper read the psychoanalytic theories of Freud and Adler as able to explain any behaviour whatever, including both drowning a child and saving one, which meant no observation could count against them.[^s3] Popper also held that a theory can start out testable and lose that status: he argued that Marxism made real predictions but was later shielded from their failure by ad hoc reinterpretations.[^s1][^s3]

Falsifiability comes in degrees. A theory that rules out more possible observations has more informative content and is more falsifiable, and Popper preferred such bold theories.[^s3] A theory that survives a severe test is *corroborated*, which for Popper means it has withstood a serious attempt at refutation, not that it is proven or even probable.[^s3]

**Workplace example.** A product team claims, "The redesign improves engagement." Stated this way, any later dashboard can be read as support. A falsifiable version commits in advance: "If the redesign works, seven-day retention for new sign-ups will rise by at least two points within six weeks; if it doesn't, we drop it." Now the claim forbids an outcome, so the data can count against it, which is the riskiness Popper prized in Einstein's eclipse prediction.[^s1]

## How to apply it

1. Ask of any claim, "What observation would show this is wrong?" If the honest answer is "nothing," the claim is not making an empirical bet.[^s1]
2. Write down the disconfirming outcome *before* collecting data, so later results cannot be reinterpreted to fit.[^s3]
3. Prefer sharper, riskier predictions over vague ones; they say more and are easier to test.[^s3]
4. When a prediction fails, be suspicious of rescue moves that add an assumption without producing any new, checkable prediction. A rescue that does yield a new test is legitimate: astronomers saved Newtonian mechanics from the anomalous orbit of Uranus by positing an unseen planet, which was then found.[^s3]

## Evidence and limitations

As a norm rather than an empirical finding, the criterion is judged by philosophical argument, and it has faced sustained criticism. The most basic is holism, associated with Duhem and Quine: a hypothesis yields predictions only together with auxiliary assumptions about instruments, conditions and background theory, so a failed prediction shows that *something* in the bundle is wrong without saying what.[^s4] Scientists can therefore keep a theory by revising an auxiliary, a move that sometimes succeeds (Neptune) and sometimes fails (the hypothetical planet Vulcan).[^s4] Critics also argue that conclusive falsification is no easier than conclusive verification, and that what counts as an observation is itself shaped by theory.[^s3]

Historians and philosophers of science raised further objections. Kuhn argued that Popper's picture fits only rare revolutionary episodes and that normal science is puzzle-solving within a paradigm.[^s2] Lakatos proposed a "sophisticated falsificationism" that judges whole research programmes by whether they keep making successful new predictions, rather than single theories by single tests.[^s2] The criterion has been faulted both for excluding legitimate science and for admitting some pseudosciences; astrology, for instance, has been tested and failed, which suggests its problem is not untestability.[^s2] Even so, the practical demand to state in advance what would count against a claim remains a widely used tool in reasoning about evidence.

## Connections

The criterion was **introduced by Karl Popper**[^s1] in ***The Logic of Scientific Discovery***.[^s3] It **contrasts with the verifiability criterion** of the Vienna Circle, which it was designed to replace.[^s2] It is **challenged by the Duhem-Quine thesis**, which denies that hypotheses can be refuted in isolation,[^s4] and by Lakatos's **methodology of scientific research programmes**, which shifts appraisal from single falsifications to the progress of a programme over time.[^s2] It is **studied in the philosophy of science** as the best-known proposal for demarcating science from **pseudoscience**.[^s2] It presupposes **modus tollens** and responds to Hume's **problem of induction**,[^s1] and its warning against **ad hoc hypotheses** grounds a practical habit of **hypothesis testing**: fix the disconfirming outcome before looking.[^s3]

## Sources

[^s1]: Thornton, S., "Karl Popper", Stanford Encyclopedia of Philosophy (rev. 2026). https://plato.stanford.edu/entries/popper/ (accessed 2026-11-04)
[^s2]: Hansson, S. O., "Science and Pseudo-Science", Stanford Encyclopedia of Philosophy (rev. 2025). https://plato.stanford.edu/entries/pseudo-science/ (accessed 2026-11-04)
[^s3]: "Popper, Karl: Philosophy of Science", Internet Encyclopedia of Philosophy. https://iep.utm.edu/pop-sci/ (accessed 2026-11-04)
[^s4]: Stanford, K., "Underdetermination of Scientific Theory", Stanford Encyclopedia of Philosophy (rev. 2023). https://plato.stanford.edu/entries/scientific-underdetermination/ (accessed 2026-11-04)
