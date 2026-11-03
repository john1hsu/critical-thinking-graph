---
id: ct:heuristics-and-biases-program
type: Framework
title: Heuristics and biases program
aliases: [heuristics and biases approach, heuristics-and-biases research program, heuristics and biases tradition]
domain: heuristics-and-dual-process
summary: >-
  The research program, launched by Amos Tversky and Daniel Kahneman around
  1970, that explains intuitive judgment under uncertainty as the use of a few
  general-purpose heuristics (such as representativeness, availability and
  anchoring) which are usually serviceable but produce predictable, systematic
  errors when compared with normative rules.
level: introductory
evidenceStatus: mixed
broader: [ct:bounded-rationality]
related: [ct:anchoring-effect, ct:representativeness-heuristic, ct:availability-heuristic, ct:dual-process-theory, ct:fast-and-frugal-heuristics, ct:conjunction-fallacy]
requires: [ct:cognitive-bias]
relations:
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:judgment-under-uncertainty-heuristics-and-biases, source: s1, confidence: medium}
  - {predicate: explainedBy, object: ct:attribute-substitution, source: s3, confidence: medium}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s5, confidence: high}
  - {predicate: supportedBy, object: ct:many-labs-1-replication-project, source: s5, confidence: medium}
  - {predicate: challengedBy, object: ct:gerd-gigerenzer, source: s2, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "On the reality of cognitive illusions"
    publisher: Psychological Review 103(3), 582-591 (Kahneman & Tversky, 1996), copy hosted on an NC State course page
    url: https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Kahneman+Tversky-cognitive-illusions-1996.pdf
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s2
    title: "On narrow norms and vague heuristics: A reply to Kahneman and Tversky (1996)"
    publisher: Psychological Review 103(3), 592-596 (Gigerenzer, 1996), copy hosted on an NC State course page
    url: https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Gigerenzer-on-Kahneman+Tversky-1996.pdf
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s3
    title: "Representativeness revisited: Attribute substitution in intuitive judgment"
    publisher: "In Gilovich, Griffin & Kahneman (eds.), Heuristics and Biases: The Psychology of Intuitive Judgment, Cambridge University Press, 49-81 (Kahneman & Frederick, 2002)"
    url: https://www.cambridge.org/core/books/abs/heuristics-and-biases/representativeness-revisited-attribute-substitution-in-intuitive-judgment/AAB5D933A3F944CFB5CB02265D376C8F
    type: primary
    accessed: 2026-11-03
  - id: s4
    title: "Investigating variation in replicability: A \"Many Labs\" replication project"
    publisher: Social Psychology 45(3), 142-152 (Klein et al., 2014), Tilburg University research portal
    url: https://research.tilburguniversity.edu/en/publications/investigating-variation-in-replicability-a-many-labs-replication-/
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s5
    title: "Conceptual replication study of fifteen JDM effects: Insights from the Polish sample"
    publisher: Polish Psychological Bulletin 53(3), 138-151 (Sobkow et al., 2022)
    url: https://journals.pan.pl//Content/124284/PDF/2022-03-PPB-02-Sobkow.pdf
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s6
    title: "Daniel Kahneman, Prize Lecture: Maps of Bounded Rationality (8 December 2002)"
    publisher: The Nobel Foundation, nobelprize.org
    url: https://www.nobelprize.org/prizes/economic-sciences/2002/kahneman/lecture/?related=1
    type: institutional
    accessed: 2026-11-03
created: 2026-11-03
---

# Heuristics and biases program

The heuristics and biases program is the research tradition that treats intuitive judgment under uncertainty as the work of a small set of mental shortcuts. In Kahneman and Tversky's own description, the goal was to understand the cognitive processes behind both good and bad judgments: heuristics such as availability and representativeness are often useful, yet they sometimes produce errors that are systematic rather than random.[^s1] The program uses those predictable errors, or biases, as diagnostic clues to how judgment actually works. In the same way, visual illusions reveal how perception works.[^s1]

## Origin

Kahneman and Frederick trace the program to a 1969 survey of 84 people attending meetings of mathematical psychologists and of the American Psychological Association. The respondents included authors of statistics textbooks. They showed too much confidence in results from small samples and little sensitivity to sample size, even though most could have worked out the correct answers.[^s3] That contrast between what experts knew and what they intuitively guessed became the program's signature finding. It also raised the uncomfortable question of whether statistical intuition can be trained at all.[^s3] Tversky and Kahneman's 1974 article in *Science* catalogued a dozen such biases and became the program's best-known statement. Kahneman and Tversky later stressed that many of those biases had nothing to do with subjective probability.[^s1] Kahneman titled his 2002 Nobel lecture "Maps of Bounded Rationality", which places the program within the wider study of the limits of human rationality.[^s6]

## How it works

The program has three moves. It proposes a heuristic, a general-purpose way of answering a hard question. It derives a prediction about where that heuristic will diverge from a normative standard such as probability theory. Then it shows the predicted divergence in simple experiments.[^s1] Kahneman and Frederick later recast the heuristics as **attribute substitution**: when a target question is hard, the mind quietly answers an easier, related one. For example, it may judge "how similar" when the question was "how probable".[^s3]

*Workplace example.* A product team must estimate how likely a new feature is to cause a support spike. One manager recalls last month's vivid outage and rates the risk high (availability). Another notices that the feature "looks like" a past success and rates it low (representativeness). A third starts from the vendor's optimistic figure and adjusts too little (anchoring). The program predicts each of these departures in advance. It also says where to look for the error: in the substitution, not in a lack of knowledge.[^s1][^s3]

## How to apply it

1. When a judgment feels easy, ask which easier question you actually answered (similarity, ease of recall, a number you saw first).[^s3]
2. Compare the intuitive answer with a normative check, such as base rates, sample size or the conjunction rule, because the program locates biases exactly at those gaps.[^s1]
3. Treat a bias found in the lab as a hypothesis about your setting, not a certainty. Effect sizes vary with materials and context.[^s5]

## Evidence

Many of the program's flagship effects have replicated. Many Labs 1 (published 2014) ran 13 classic and contemporary effects in 36 samples with 6,344 participants and reproduced 10 of them consistently.[^s4] A 2022 conceptual replication of 15 judgment and decision-making effects in a Polish online sample found that anchoring in estimation tasks and the sunk-cost effect replicated. It reports that anchoring had also replicated in Many Labs 1.[^s5] The same study failed to reproduce a variant of Tversky and Kahneman's 1981 framing problem. It also notes that Many Labs 2 replicated the original framing problem, but with a much smaller effect.[^s5] Overall, the core biases appear to be real, but their sizes depend on the materials, which is why this article rates the evidence as mixed rather than robust.[^s4][^s5]

The theoretical critique is sharper. Gerd Gigerenzer argued that the program applies norms too narrowly, for instance by treating everyday words such as "probable" and "and" as if they carried only their mathematical meaning. He also argued that its heuristics are too vague to count as process models, and that presenting information as natural frequencies reduces several of the reported biases.[^s2] Kahneman and Tversky replied that he misstated their position. They pointed to studies in which frequency formats left conjunction errors and base-rate neglect in place, and they accepted only that some illusions are sometimes reduced.[^s1]

## Connections

The program was **introduced by** Amos Tversky and Daniel Kahneman, and its best-known statement was their 1974 *Science* article.[^s1] Its later account of how the heuristics work is **explained by** attribute substitution.[^s3] It is a core research line **studied in** judgment and decision making. Its anchoring result is **supported by** the Many Labs 1 replication project.[^s5] It is **challenged by** Gerd Gigerenzer's critique of narrow norms and vague heuristics, which grew into the rival fast-and-frugal heuristics program.[^s2] It sits under bounded rationality, the theme of Kahneman's Nobel lecture.[^s6] It is related to the specific heuristics it proposed and to the anchoring effect, one of its most replicated findings.[^s1][^s5]

## Sources

[^s1]: Kahneman & Tversky, "On the reality of cognitive illusions", Psychological Review 103(3), 1996. https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Kahneman+Tversky-cognitive-illusions-1996.pdf (accessed 2026-11-03)
[^s2]: Gigerenzer, "On narrow norms and vague heuristics: A reply to Kahneman and Tversky (1996)", Psychological Review 103(3), 1996. https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Gigerenzer-on-Kahneman+Tversky-1996.pdf (accessed 2026-11-03)
[^s3]: Kahneman & Frederick, "Representativeness revisited: Attribute substitution in intuitive judgment", in Heuristics and Biases, Cambridge University Press, 2002. https://www.cambridge.org/core/books/abs/heuristics-and-biases/representativeness-revisited-attribute-substitution-in-intuitive-judgment/AAB5D933A3F944CFB5CB02265D376C8F (accessed 2026-11-03)
[^s4]: Klein et al., "Investigating variation in replicability: A 'Many Labs' replication project", Social Psychology 45(3), 2014. https://research.tilburguniversity.edu/en/publications/investigating-variation-in-replicability-a-many-labs-replication-/ (accessed 2026-11-03)
[^s5]: Sobkow et al., "Conceptual replication study of fifteen JDM effects: Insights from the Polish sample", Polish Psychological Bulletin 53(3), 2022. https://journals.pan.pl//Content/124284/PDF/2022-03-PPB-02-Sobkow.pdf (accessed 2026-11-03)
[^s6]: Nobel Foundation, "Daniel Kahneman, Prize Lecture: Maps of Bounded Rationality". https://www.nobelprize.org/prizes/economic-sciences/2002/kahneman/lecture/?related=1 (accessed 2026-11-03)
