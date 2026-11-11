---
id: ct:behavioral-economics
type: Field
title: Behavioral economics
aliases: [behavioural economics, psychology and economics, economics and psychology]
domain: decision-making
summary: >-
  The branch of economics that builds more psychologically realistic
  assumptions about attention, willpower and social motives into economic
  models, usually by keeping the standard framework of utility maximization
  and equilibrium and changing one or two assumptions at a time to explain
  documented anomalies.
level: introductory
evidenceStatus: historical
broader: [ct:economics]
related: [ct:judgment-and-decision-making, ct:prospect-theory, ct:bounded-rationality, ct:expected-utility-theory, ct:loss-aversion, ct:choice-architecture, ct:experimental-economics, ct:publication-bias]
requires: [ct:expected-utility-theory]
relations:
  - {predicate: influencedBy, object: ct:herbert-simon, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:prospect-theory, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:heuristics-and-biases-program, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:expected-utility-theory, source: s1, confidence: medium}
  - {predicate: supportedBy, object: ct:madrian-shea-2001-automatic-enrollment-study, source: s3, confidence: high}
  - {predicate: challengedBy, object: ct:maier-2022-nudging-publication-bias-reanalysis, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Behavioral Economics: Past, Present, Future (introduction to Advances in Behavioral Economics)"
    publisher: Camerer & Loewenstein, Caltech and Carnegie Mellon, draft of the introductory chapter to Advances in Behavioral Economics (Princeton University Press, 2004), hosted on an Iowa State University faculty archive
    url: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/CamererIntroChapter.AdvancesBE.pdf
    type: primary
    accessed: 2026-11-11
  - id: s2
    title: "The Prize in Economic Sciences 2017: press release"
    publisher: The Royal Swedish Academy of Sciences, NobelPrize.org (9 October 2017)
    url: https://www.nobelprize.org/prizes/economic-sciences/2017/press-release/
    type: institutional
    accessed: 2026-11-11
  - id: s3
    title: "The Power of Suggestion: Inertia in 401(k) Participation and Savings Behavior"
    publisher: NBER Working Paper 7682 (Madrian & Shea, 2000; Quarterly Journal of Economics 116(4), 2001)
    url: https://www.nber.org/papers/w7682
    type: primary
    accessed: 2026-11-11
  - id: s4
    title: "Evaluating replicability of laboratory experiments in economics"
    publisher: Science 351(6280), 1433-1436 (Camerer, Dreber, Forsell, Ho, Huber, Johannesson, Kirchler et al., 2016), Caltech Authors repository
    url: https://authors.library.caltech.edu/records/gr9cr-qjb08
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "No evidence for nudging after adjusting for publication bias"
    publisher: Proceedings of the National Academy of Sciences 119(31), e2200300119 (Maier, Bartos, Stanley, Shanks, Harris & Wagenmakers, 2022), PubMed record
    url: https://www.pubmed.gov/35858389/
    type: peer-reviewed
    accessed: 2026-11-11
created: 2026-11-11
---

# Behavioral economics

Behavioral economics is the part of economics that tries to make economic models more accurate by giving them more realistic psychological foundations. In Colin Camerer and George Loewenstein's account, it usually does not throw out the standard toolkit of utility maximization, equilibrium and efficiency. Instead it changes one or two assumptions at a time, such as the assumption that people ignore fairness or discount the future at a constant rate, and checks whether the modified model predicts better.[^s1] They judge such models by realism, generality and tractability, and tie the limits on computation and willpower they add to Herbert Simon's idea of procedural rationality.[^s1]

## Origin

Camerer and Loewenstein note that psychology was part of economics from the start. Adam Smith's *Theory of Moral Sentiments* already describes something like loss aversion, and Bentham and Edgeworth wrote about the psychology of utility.[^s1] Around 1900, economists tried to purge psychology from the discipline as unscientific. Critics such as Simon, Katona and Scitovsky pushed back without changing the field's direction.[^s1] Expected utility and discounted utility then gave economists precise, testable models, and Allais, Ellsberg and others soon documented anomalies in them.[^s1]

The turning point came from cognitive psychology. Tversky and Kahneman's 1974 *Science* paper on heuristics and their 1979 *Econometrica* paper on prospect theory were especially influential in economics.[^s1] A 1986 Chicago conference and a 1997 special issue of the *Quarterly Journal of Economics* signalled acceptance in the mainstream.[^s1] In 2017 Richard Thaler received the Nobel memorial prize for this work. The Royal Swedish Academy of Sciences cited his work on limited rationality (mental accounting and the endowment effect), social preferences (fairness and the dictator game) and lack of self-control (a planner-doer model and the idea of the nudge).[^s2]

## How it works

Camerer and Loewenstein describe a four-step recipe. First, identify a standard assumption. Second, document behavior that violates it and rule out conventional explanations. Third, build an alternative model from the anomaly. Fourth, derive and test the new model's implications.[^s1] The field is defined by its psychological content, not by a single method. It uses laboratory and field experiments, field data and even brain imaging, and in this it differs from experimental economics, which is defined by its method.[^s1] Its main topics include reference dependence and loss aversion, framing and preference reversals, mental accounting, hyperbolic discounting and self-control, fairness and reciprocity, and behavioral game theory.[^s1]

A workplace example shows how this can be put to use. A firm's retirement plan has generous terms but low enrollment, because employees have to opt in. A standard model says the default should not matter, since anyone who values the plan will sign up. Madrian and Shea studied a large US employer that switched to automatic enrollment with an opt-out, while leaving the plan's economic terms unchanged.[^s3] Participation rose substantially, and new hires tended to keep the default contribution rate and fund. The authors attributed this to inertia and to employees reading the default as implicit advice.[^s3] For a critical thinker, the lesson is to ask what a model assumes about attention and willpower before trusting its prediction.

## Evidence and limitations

The field's laboratory base has held up better than many psychology findings. In a 2016 *Science* project, Camerer and colleagues replicated 18 economics experiments published in the *American Economic Review* and *Quarterly Journal of Economics* between 2011 and 2014. Eleven (61%) produced a significant effect in the original direction, and replicated effect sizes averaged about two-thirds of the originals.[^s4] The policy branch is more disputed. In a 2022 *PNAS* letter, Maier and colleagues argued that once publication bias is corrected for, the meta-analytic evidence for nudge interventions in general is not convincing, though some individual nudges may still work.[^s5]

There are also conceptual objections. Camerer and Loewenstein grant that many heuristics may be near-optimal in their usual environments, so calling them irrational can be unfair. They also grant that a catalogue of anomalies is not yet a unified theory to replace utility maximization.[^s1] They expected the "behavioral" label to fade as realistic assumptions became ordinary economics, with strict rationality kept as a useful special case.[^s1]

## Connections

Behavioral economics is **influenced by** Herbert Simon's bounded rationality, by the heuristics and biases program and by prospect theory, which Camerer and Loewenstein single out as its most influential imports from psychology.[^s1] It **contrasts with** expected utility theory, whose anomalies it set out to explain, while usually keeping it as the benchmark model.[^s1] Its policy claims are **supported by** default-effect field studies such as Madrian and Shea's automatic-enrollment study.[^s3] They are **challenged by** Maier and colleagues' publication-bias reanalysis of nudging.[^s5] It overlaps heavily with judgment and decision making, the psychology-based field that supplied many of its findings. Choice architecture and loss aversion are among its best-known concepts, and the 2016 replication project placed it within the wider debate on publication bias and replicability.[^s1][^s2][^s4]

## Sources

[^s1]: Camerer & Loewenstein, "Behavioral Economics: Past, Present, Future", introduction to Advances in Behavioral Economics (draft, 2002). https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/CamererIntroChapter.AdvancesBE.pdf (accessed 2026-11-11)
[^s2]: Royal Swedish Academy of Sciences, "The Prize in Economic Sciences 2017" press release, 9 October 2017. https://www.nobelprize.org/prizes/economic-sciences/2017/press-release/ (accessed 2026-11-11)
[^s3]: Madrian & Shea, "The Power of Suggestion: Inertia in 401(k) Participation and Savings Behavior", NBER Working Paper 7682, 2000. https://www.nber.org/papers/w7682 (accessed 2026-11-11)
[^s4]: Camerer et al., "Evaluating replicability of laboratory experiments in economics", Science 351(6280), 2016. https://authors.library.caltech.edu/records/gr9cr-qjb08 (accessed 2026-11-11)
[^s5]: Maier et al., "No evidence for nudging after adjusting for publication bias", PNAS 119(31), 2022. https://www.pubmed.gov/35858389/ (accessed 2026-11-11)
