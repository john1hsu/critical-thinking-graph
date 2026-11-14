---
id: ct:duhem-quine-thesis
type: Concept
title: Duhem–Quine thesis
aliases: [Quine–Duhem thesis, Duhem–Quine problem, Quine–Duhem problem, confirmation holism, Duhem thesis, holist underdetermination]
domain: scientific-reasoning
summary: >-
  The thesis that no scientific hypothesis can be tested in isolation: a
  prediction follows only from the hypothesis together with auxiliary
  assumptions, so a failed prediction shows that something in the bundle is
  false without saying which part.
level: intermediate
evidenceStatus: normative
broader: [ct:underdetermination]
related: [ct:falsifiability, ct:ad-hoc-hypothesis, ct:hypothesis-testing, ct:philosophy-of-science, ct:karl-popper, ct:imre-lakatos, ct:bayesian-reasoning]
requires: [ct:modus-tollens, ct:hypothesis-testing]
relations:
  - {predicate: introducedBy, object: ct:pierre-duhem, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:willard-van-orman-quine, source: s3, confidence: high}
  - {predicate: studiedIn, object: ct:philosophy-of-science, source: s2, confidence: high}
  - {predicate: formalizedBy, object: ct:bayesian-reasoning, source: s5, confidence: medium}
  - {predicate: contrastsWith, object: ct:crucial-experiment, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Pierre Duhem"
    publisher: Stanford Encyclopedia of Philosophy
    url: https://plato.stanford.edu/ENTRiES/duhem/
    type: scholarly-encyclopedia
    accessed: 2026-11-14
  - id: s2
    title: "Underdetermination of Scientific Theory"
    publisher: Stanford Encyclopedia of Philosophy (Stanford)
    url: https://plato.stanford.edu/ENTRIES/scientific-underdetermination/
    type: scholarly-encyclopedia
    accessed: 2026-11-14
  - id: s3
    title: "Two Dogmas of Empiricism"
    publisher: The Philosophical Review 60 (Quine, 1951), course reprint, University of Nevada, Las Vegas
    url: https://beisecker.faculty.unlv.edu/Courses/Phi-425/Quine-Two_Dogmas_of_Empiricism.html
    type: primary
    accessed: 2026-11-14
  - id: s4
    title: "Duhem, Quine, and the Multiplicity of Scientific Tests"
    publisher: Philosophy of Science 61(4) (Balashov, 1994)
    url: https://www.cambridge.org/core/journals/philosophy-of-science/article/abs/duhem-quine-and-the-multiplicity-of-scientific-tests/F084044F7FA8022B8C4F71590E42DCA5
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "The Bayesian Treatment of Auxiliary Hypotheses"
    publisher: British Journal for the Philosophy of Science 52(3) (Strevens, 2001), PhilArchive record
    url: https://dc2.philarchive.org/rec/STRTBT-2
    type: peer-reviewed
    accessed: 2026-11-14
created: 2026-11-14
---

# Duhem–Quine thesis

The Duhem–Quine thesis says that a scientific hypothesis never faces a test on its own. To get a checkable prediction out of a hypothesis, you must combine it with auxiliary assumptions: background theory, claims about how the instruments work, and assumptions about the conditions of the experiment. When the prediction fails, logic tells you only that at least one member of that bundle is false, not which one.[^s2][^s1] The thesis is a claim about the limits of refutation, and it is the main reason a single failed experiment rarely settles a scientific dispute.[^s2]

## Origin

The French physicist and historian of science Pierre Duhem (1861–1916) set out the argument in *La Théorie physique* (1906; second edition 1914; English translation *The Aim and Structure of Physical Theory*, 1954).[^s1] Duhem held that a physicist can never submit an isolated hypothesis to experiment, and drew the corollary that a true "crucial experiment", one that decides between two rival hypotheses, is impossible in physics.[^s1] His example was Foucault's measurement showing that light travels more slowly in water than in air, widely read as refuting the particle (emission) theory of light. Duhem replied that the result condemned the whole group of assumptions behind the emission theory, and that the wave theory had not thereby been proved, since other hypotheses remained possible.[^s1][^s2] To guide the choice of which assumption to revise he appealed to the scientist's "good sense" (*bon sens*), a notion critics have found vague.[^s1]

W. V. Quine generalised the idea in "Two Dogmas of Empiricism" (1951). He argued that statements about the world meet experience not one by one but as a corporate body, that total science is a fabric touching experience only at its edges, and that any statement can be kept true come what may if enough adjustments are made elsewhere, including revisions to logic.[^s3] In a note Quine credited the holistic view to Duhem, which is how the two names became joined.[^s3][^s1] The pairing hides real differences. Duhem restricted his claim to physics and denied that every hypothesis can be rescued; his point was that refutation is ambiguous. Quine extended holism to all empirical belief and embraced the stronger conclusion.[^s1]

## How it works

The logic is modus tollens applied to a conjunction. If hypothesis H together with auxiliaries A1, A2 and A3 entails observation O, and O fails to appear, then the conjunction H-and-A1-and-A2-and-A3 is false. Nothing in the logic says to reject H rather than one of the auxiliaries.[^s2]

The classic illustration is a pair of planetary anomalies. When Uranus strayed from its predicted orbit, astronomers kept Newtonian mechanics and revised an auxiliary assumption about how many planets exist; the hypothesised planet was found as Neptune. When the same move was tried for an anomaly in Mercury's orbit, the extra planet never turned up, and the anomaly was eventually explained by general relativity instead.[^s2] In advance, nothing in the evidence alone said which strategy would work.[^s2]

A workplace version: an analytics team predicts that a new onboarding email will raise week-one activation. The A/B test shows no lift. The failed prediction could mean the email does not work, but it could equally mean the tracking event fired incorrectly, the random assignment was broken, the test ran in an atypical holiday week, or the sample was too small to detect a real effect. Each is an auxiliary assumption the prediction depended on. A team that knows the thesis lists those auxiliaries before running the test and checks them independently, rather than either declaring the idea dead or explaining the result away after the fact.[^s2][^s4]

## How to apply it

- **Name the auxiliaries in advance.** Before a test, write down what else must be true for the prediction to follow: measurement validity, sample, conditions, background theory.[^s2]
- **Check auxiliaries independently.** Holism does not forbid locating the fault; it forbids pretending logic alone locates it. Independent checks on instruments and conditions narrow the culprit.[^s4]
- **Look across several tests.** Yuri Balashov (1994) argues that when a theory meets multiple adverse results, the pattern of failures across tests that share some assumptions and not others can point to a weak spot.[^s4]
- **Assign degrees of belief.** Bayesian treatments divide blame between hypothesis and auxiliaries according to their prior plausibility, though Michael Strevens (2001) argues that the standard Bayesian solution begs the question and proposes an alternative.[^s5]
- **Watch for ad hoc rescues.** Because blaming an auxiliary is always logically available, ask whether the rescue has any support beyond the anomaly it removes.[^s2][^s5]

## Limitations and debate

The thesis is a philosophical claim, judged by argument rather than experiment. Larry Laudan (1990) argued that holists have exaggerated it: showing that many responses to a failed test are logically or psychologically possible does not show that they are all rationally defensible.[^s2] Others, including Lakatos and later sociologists of knowledge, took holism to show that non-evidential factors such as the resources of a theory's advocates or social interests help decide which beliefs survive.[^s2] A middle view, defended by Balashov, holds that holism leaves room for methodologically responsible ways of resolving conflicts with experience, even if none is logically compelling.[^s4]

## Connections

- **Underdetermination:** the thesis is the "holist" form of underdetermination, in which evidence fails to fix which belief to revise.[^s2]
- **Introduced by Pierre Duhem and W. V. Quine:** Duhem stated the physics-specific version in 1906, and Quine's 1951 essay gave the generalised version and the joint name.[^s1][^s3]
- **Crucial experiment:** Duhem's argument was directed against the idea that one experiment can decide between two hypotheses.[^s1]
- **Philosophy of science:** it is a standing problem in the field's accounts of confirmation and theory choice.[^s2]
- **Bayesian reasoning:** Bayesian confirmation theory offers a formal treatment of how to share blame between a hypothesis and its auxiliaries.[^s5]
- **Falsifiability and ad hoc hypotheses:** because blame can always be shifted to an auxiliary, the thesis challenges naive falsificationism and explains why ad hoc rescues are always available.[^s2]

## Sources

[^s1]: "Pierre Duhem", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/ENTRiES/duhem/ (accessed 2026-11-14)
[^s2]: Stanford, "Underdetermination of Scientific Theory", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/ENTRIES/scientific-underdetermination/ (accessed 2026-11-14)
[^s3]: Quine, "Two Dogmas of Empiricism", The Philosophical Review 60 (1951): 20–43; course reprint, UNLV. https://beisecker.faculty.unlv.edu/Courses/Phi-425/Quine-Two_Dogmas_of_Empiricism.html (accessed 2026-11-14)
[^s4]: Balashov, "Duhem, Quine, and the Multiplicity of Scientific Tests", Philosophy of Science 61(4), 1994, doi:10.1086/289825. https://www.cambridge.org/core/journals/philosophy-of-science/article/abs/duhem-quine-and-the-multiplicity-of-scientific-tests/F084044F7FA8022B8C4F71590E42DCA5 (accessed 2026-11-14)
[^s5]: Strevens, "The Bayesian Treatment of Auxiliary Hypotheses", British Journal for the Philosophy of Science 52(3), 2001: 515–537. https://dc2.philarchive.org/rec/STRTBT-2 (accessed 2026-11-14)
