---
id: ct:attribute-substitution
type: Framework
title: Attribute substitution
aliases: [substitution of an easier question, heuristic attribute substitution, Kahneman-Frederick model of heuristic judgment]
domain: heuristics-and-dual-process
summary: >-
  Kahneman and Frederick's model of heuristic judgment: when a target
  attribute is hard to assess, people often answer by assessing a related,
  more accessible heuristic attribute instead, usually without noticing the
  swap, which produces systematic biases wherever the two attributes diverge.
level: intermediate
evidenceStatus: mixed
broader: [ct:heuristics-and-biases-program]
related: [ct:dual-process-theory, ct:availability-heuristic, ct:representativeness-heuristic, ct:affect-heuristic, ct:conjunction-fallacy, ct:base-rate-neglect, ct:cognitive-reflection-test, ct:scope-neglect, ct:bounded-rationality]
requires: [ct:heuristics-and-biases-program, ct:dual-process-theory]
relations:
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:shane-frederick, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:accessibility, source: s3, confidence: high}
  - {predicate: demonstratedBy, object: ct:strack-martin-schwarz-1988-dating-happiness-study, source: s5, confidence: medium}
  - {predicate: challengedBy, object: ct:effort-reduction-framework, source: s4, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s3, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Representativeness revisited: Attribute substitution in intuitive judgment"
    publisher: "Heuristics and Biases: The Psychology of Intuitive Judgment, eds. Gilovich, Griffin & Kahneman, Cambridge University Press, 49-81 (Kahneman & Frederick, 2002)"
    url: https://www.cambridge.org/core/books/abs/heuristics-and-biases/representativeness-revisited-attribute-substitution-in-intuitive-judgment/AAB5D933A3F944CFB5CB02265D376C8F
    type: primary
    accessed: 2026-11-11
  - id: s2
    title: "A model of heuristic judgment"
    publisher: "The Cambridge Handbook of Thinking and Reasoning, Cambridge University Press, 267-289 (Kahneman & Frederick, 2005), authors' manuscript"
    url: https://cdn2.psychologytoday.com/assets/model_of_heuristic_judgment.pdf
    type: primary
    accessed: 2026-11-11
  - id: s3
    title: "A perspective on judgment and choice: Mapping bounded rationality"
    publisher: American Psychologist 58(9), 697-720 (Kahneman, 2003), PubMed record
    url: https://pubmed.ncbi.nlm.nih.gov/14584987/
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "Heuristics made easy: An effort-reduction framework"
    publisher: Psychological Bulletin 134(2), 207-222 (Shah & Oppenheimer, 2008), Princeton University record
    url: https://collaborate.princeton.edu/en/publications/heuristics-made-easy-an-effort-reduction-framework/
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "Maps of bounded rationality: Psychology for behavioral economics"
    publisher: American Economic Review 93(5) (Kahneman, 2003), Princeton author page
    url: https://kahneman.scholar.princeton.edu/document/8
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s6
    title: "Rain & happiness: Why didn't Schwarz & Clore (1983) 'replicate'?"
    publisher: Data Colada 43 (Simonsohn, 2015, updated 2020)
    url: https://datacolada.org/43
    type: community
    accessed: 2026-11-11
created: 2026-11-11
---

# Attribute substitution

Attribute substitution is Daniel Kahneman and Shane Frederick's general account of how heuristics work. When people must judge a *target attribute* of something that is hard to assess (a probability, a total, a long-run value), they often assess a different *heuristic attribute* of the same thing that comes to mind more easily, and report that answer as if it answered the original question.[^s1][^s2] The swap is usually unnoticed: people feel they have answered the question they were asked.[^s5] Wherever the two attributes come apart, the substitution builds in a systematic bias.[^s2]

## Origin

Kahneman and Frederick introduced the idea in "Representativeness revisited", a chapter in the 2002 Cambridge volume *Heuristics and Biases*, which reframed the classic Tversky-Kahneman heuristics as cases of one process rather than a list of separate shortcuts.[^s1] Kahneman developed it in his 2002 Nobel lecture, published in 2003 in the *American Economic Review* and in a longer *American Psychologist* review, where accessibility, the ease with which thoughts come to mind, is the concept that explains which attribute gets substituted.[^s5][^s3] A 2005 handbook chapter by the same pair restated it as "a model of heuristic judgment" and tied it explicitly to a two-system view of the mind.[^s2]

## How it works

Three things must hold. The target attribute is relatively inaccessible; a related attribute is highly accessible, either because it is always computed (similarity, size, affect) or because something has just primed it; and the substitution is not caught and corrected by deliberate, System 2 checking.[^s2][^s5] On this view the availability heuristic substitutes ease of recall for frequency, the representativeness heuristic substitutes similarity to a prototype for probability, and the affect heuristic substitutes a good-or-bad feeling for a weighing of risks and benefits.[^s2][^s5]

A classic demonstration is a survey by Strack, Martin and Schwarz (1988). When students were asked how happy they were with life in general and then how many dates they had had last month, the two answers barely correlated; when the dating question came first, the correlation rose to about 0.66. Kahneman reads this as the dating question making romantic satisfaction accessible, so it was used as the answer to the much harder global-happiness question.[^s5][^s2] In contingent-valuation surveys, households offered roughly the same payment to save 2,000, 20,000 or 200,000 birds from oil ponds, consistent with an emotional reaction to a single bird image standing in for the value of the whole outcome.[^s5]

*Workplace example.* A hiring panel is asked to judge how likely a candidate is to perform well over the next three years. That is hard to estimate, so the panel answers an easier question instead: how impressive was the interview presentation? Kahneman and Frederick give the parallel case of judging tenure prospects from the quality of a job talk.[^s2] The panel's ratings will then track presentation polish, a cue that may only loosely predict later performance, and the panel will not experience its judgment as a substitution.[^s2][^s5]

Correction is possible but weak. Kahneman notes that System 2 monitors intuitive answers only lightly; time pressure, concurrent load and good mood make errors more likely, while high need for cognition and salient cues to a neglected factor (such as explicit base rates) make correction more likely.[^s5] The bat-and-ball puzzle, whose quick but wrong answer about half of Princeton students gave, is his illustration of how readily a plausible intuitive answer passes unchecked.[^s5][^s2]

## How to spot it

Ask whether the question being answered is the question that was posed. Warning signs include judgments that ignore quantities that should matter (scope, sample size, base rates), confident answers to questions that are objectively hard, and ratings that move with whatever was discussed just beforehand.[^s5][^s2] A useful check is to restate the target attribute out loud ("probability of success over three years") and ask what evidence would bear on it directly.[^s2]

## Evidence

The model organises a large body of robust findings, including the conjunction fallacy, base-rate neglect and scope insensitivity, under one mechanism.[^s5][^s3] Shah and Oppenheimer's 2008 *Psychological Bulletin* review argues it is only a partial account: it explains reliance on easy-to-access cues, but not other ways heuristics save effort, such as examining fewer alternatives or simplifying how cues are weighted, and they note that some applications assert substitution without showing that people actually reframed the question.[^s4] Some vivid illustrations have also weakened. Simonsohn's 2015 analysis, drawing on two large survey studies of around 90,000 and 1 million respondents, concluded that the data are strongly inconsistent with the famous finding that sunny weather raises reported life satisfaction, an example the model's authors used to show how a reminder of the weather blocks substitution, while noting this does not refute mood-as-information theory itself.[^s6][^s2] Because the mechanism is strongly supported in some paradigms but disputed as a complete theory, its status here is mixed.[^s4][^s6]

## Connections

- **Introduced by** Daniel Kahneman and Shane Frederick in their 2002 chapter, as a reinterpretation of the heuristics-and-biases program.[^s1]
- **Explained by** accessibility: Kahneman's 2003 review uses the ease with which attributes come to mind to explain which one is substituted.[^s3]
- **Demonstrated by** the Strack, Martin and Schwarz (1988) dating-and-happiness item-order study, which Kahneman uses as a clean case of substitution.[^s5]
- **Challenged by** Shah and Oppenheimer's effort-reduction framework, which treats substitution as one principle among several.[^s4]
- **Studied in** judgment and decision-making research.[^s3]
- **Related to** dual-process theory, whose System 1 and System 2 supply the proposal-and-correction structure of the model, and to the availability, representativeness and affect heuristics, which it reinterprets as substitutions.[^s2]

## Sources

[^s1]: Kahneman & Frederick, "Representativeness revisited: Attribute substitution in intuitive judgment", in Heuristics and Biases, Cambridge University Press (2002). https://www.cambridge.org/core/books/abs/heuristics-and-biases/representativeness-revisited-attribute-substitution-in-intuitive-judgment/AAB5D933A3F944CFB5CB02265D376C8F (accessed 2026-11-11)
[^s2]: Kahneman & Frederick, "A model of heuristic judgment", in The Cambridge Handbook of Thinking and Reasoning (2005). https://cdn2.psychologytoday.com/assets/model_of_heuristic_judgment.pdf (accessed 2026-11-11)
[^s3]: Kahneman, "A perspective on judgment and choice: Mapping bounded rationality", American Psychologist 58 (2003). https://pubmed.ncbi.nlm.nih.gov/14584987/ (accessed 2026-11-11)
[^s4]: Shah & Oppenheimer, "Heuristics made easy: An effort-reduction framework", Psychological Bulletin 134 (2008). https://collaborate.princeton.edu/en/publications/heuristics-made-easy-an-effort-reduction-framework/ (accessed 2026-11-11)
[^s5]: Kahneman, "Maps of bounded rationality: Psychology for behavioral economics", American Economic Review 93 (2003). https://kahneman.scholar.princeton.edu/document/8 (accessed 2026-11-11)
[^s6]: Simonsohn, "Rain & happiness: Why didn't Schwarz & Clore (1983) 'replicate'?", Data Colada 43 (2015). https://datacolada.org/43 (accessed 2026-11-11)
