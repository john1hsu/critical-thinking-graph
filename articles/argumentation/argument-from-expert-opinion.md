---
id: ct:argument-from-expert-opinion
type: ArgumentScheme
title: Argument from expert opinion
aliases: [appeal to expert opinion, argument from expertise, appeal to expertise, expert opinion scheme]
domain: argumentation
summary: >-
  The presumptive argument pattern "E is an expert in domain S, which contains
  claim A; E asserts A; so A may plausibly be accepted". It is reasonable but
  defeasible: its strength depends on answers to critical questions about the
  expert's competence, field, statement, reliability, agreement with other
  experts and evidence.
level: introductory
evidenceStatus: normative
broader: [ct:argumentation-schemes]
related: [ct:source-credibility, ct:testimony, ct:presumption, ct:burden-of-proof, ct:defeasible-reasoning, ct:ad-hominem, ct:richard-whately, ct:john-locke, ct:port-royal-logic, ct:informal-fallacy]
requires: [ct:argument]
relations:
  - {predicate: introducedBy, object: ct:douglas-walton, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:ad-verecundiam, source: s1, confidence: high}
  - {predicate: formalizedBy, object: ct:bayesian-reasoning, source: s3, confidence: high}
  - {predicate: supportedBy, object: ct:harris-2016-expert-opinion-bayesian-experiments, source: s3, confidence: medium}
  - {predicate: influencedBy, object: ct:john-locke, source: s1, confidence: medium}
criticalQuestions:
  - How credible is this person as an expert, judged by training, track record and standing in the field?
  - Is the claim actually inside the person's field of expertise, or only next to it?
  - What exactly did the expert say, and does it really imply the claim being made in their name?
  - Is the expert personally reliable here, or do conflicts of interest or a history of bias give reason for doubt?
  - Do other qualified experts in the field agree, or is this a minority or disputed view?
  - Is the expert's statement based on evidence that could be produced and checked if asked?
argumentMap:
  premises:
    - "The structural engineer we hired is a licensed specialist in load-bearing timber frames."
    - "She says the existing beam can carry the proposed rooftop plant room."
  conclusion: "We can plan on keeping the existing beam for the plant room."
  verdict: strong
  scheme: ct:argument-from-expert-opinion
  objections:
    - "Did she see the actual beam, or only the original drawings, which may not match what was built?"
    - "A second engineer's report flags rot at one bearing end, so experts do not yet agree."
sameAs: []
sources:
  - id: s1
    title: "Fallacies"
    publisher: Stanford Encyclopedia of Philosophy (Hans Hansen, first published 2015; substantive revision 2024)
    url: https://plato.stanford.edu/entries/fallacies/
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s2
    title: "On a Razor's Edge: Evaluating Arguments from Expert Opinion"
    publisher: "Argument & Computation 5(2-3), 139-159 (Douglas Walton, 2014), CORE open-access copy"
    url: https://core.ac.uk/download/72794558.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s3
    title: "The appeal to expert opinion: quantitative support for a Bayesian network approach"
    publisher: "Cognitive Science 40(6), 1496-1533 (Harris, Hahn, Madsen & Hsu, 2016), UCL Discovery author copy"
    url: https://discovery-pp.ucl.ac.uk/id/eprint/1468674/1/Harris_Hahn_Madsen_Hsu_2015.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s4
    title: "Fallacies"
    publisher: Internet Encyclopedia of Philosophy (Bradley Dowden)
    url: https://iep.utm.edu/fallacy/
    type: scholarly-encyclopedia
    accessed: 2026-11-08
created: 2026-11-08
---

# Argument from expert opinion

The argument from expert opinion moves from what a qualified source says to a conclusion about the world: E is an expert in a domain that contains claim A, E asserts A, so A is plausibly true.[^s2] It is one of the most common argumentation schemes, because nobody can check most of what they rely on for themselves.[^s4] Like other schemes it is defeasible. It creates a presumption in favour of its conclusion that holds until a critical question exposes a weakness, and the same pattern can be used well, weakly or fallaciously.[^s1]

## Origin

Appeals to authority have long been discussed as a possible fallacy. The Port-Royal *Logic* of Arnauld and Nicole (1662) described a "sophism of authority", one of the earliest modern accounts of appealing to false authority.[^s1] John Locke's *Essay Concerning Human Understanding* (1690) introduced the label *argumentum ad verecundiam* for one of several ways people win assent in argument. His wording about eminence and modesty points to deference to social rank, not expertise, and he did not call it a fallacy; later textbook writers did.[^s1] Jeremy Bentham then set out conditions under which an appeal to authority is reliable.[^s1]

The modern scheme comes from Douglas Walton. He first formulated it, with six critical questions, in his 1989 textbook *Informal Logic*, developed it in *Appeal to Expert Opinion* (1997), and restated it with Chris Reed and Fabrizio Macagno in *Argumentation Schemes* (2008).[^s2] That move turned a fallacy label into a reasonable argument form with tests for when it fails.[^s1]

## How it works

The scheme has two premises and a conclusion. The major premise says the source is an expert in a subject domain that contains the claim. The minor premise says the source asserts the claim. The conclusion accepts the claim, tentatively.[^s2] Walton's six critical questions probe it: expertise (how credible is E as an expert?), field (is A within E's field?), opinion (what did E actually say?), trustworthiness (is E personally reliable?), consistency (do other experts agree?) and backup evidence (is the assertion based on evidence?).[^s2]

In the argument map above, a building team relies on a timber-frame engineer's view that a beam can carry a new plant room. The argument is strong as it stands: she is qualified and the question lies in her field. The objections show where critical questions bite. If she saw only drawings, the backup-evidence question is open. If a second engineer has found rot, the consistency question now counts against the conclusion until it is resolved.[^s2]

Walton argues that questions differ in who must answer them. Questions treated as assumptions, such as backup evidence, must be answered by the proponent once asked. Questions treated as exceptions, such as trustworthiness or disagreement among experts, defeat the argument only if the challenger offers some evidence.[^s2] In this view, assessing experts is better done by questioning them than by trusting or distrusting them across the board.[^s2]

## How to apply it

1. Restate the argument in scheme form, naming the expert, the domain and the exact claim.[^s2]
2. Check relevance first. An authority outside their field, such as a celebrity endorsing a product, gives little support.[^s4][^s1]
3. Check what was said. Misquotation, or stretching a cautious remark into a firm verdict, is a common failure.[^s4]
4. Look for disagreement. When qualified experts disagree, citing only one side is a weak appeal; a lone dissenter against a broad consensus is a different matter.[^s4][^s1]
5. Ask for the evidence behind the opinion when the stakes justify it, and weigh any conflicts of interest.[^s2]

The Internet Encyclopedia of Philosophy stresses that most appeals to authority are not fallacious. The error is accepting a source's word when there is good reason to be suspicious of it.[^s4]

## Evidence

The scheme is a normative standard, but its critical questions have also been modelled and tested. Harris, Hahn, Madsen and Hsu (2016) built a Bayesian network in which an expert's report depends on the truth of the claim, the expert's expertise (honest error) and trustworthiness (deliberate deception), with other experts' views entering through the prior.[^s3] In two online experiments (84 and 57 participants), the model's predictions accounted for about 89% and 90% of the variance in average ratings of how convincing the arguments were. Fits for individual participants were much weaker, explaining about 38% of the variance.[^s3] Models that ignored either expertise or trustworthiness did worse. The authors argue that this supports treating Walton's questions as factors in probabilistic reasoning, not as separate yes/no tests.[^s3] These are two studies with medical topics and fixed scenarios, so the result shows that the model fits people's ratings, not that people evaluate expert claims accurately.[^s3]

## Connections

- **Introduced by Douglas Walton.** Walton's 1989 and 1997 formulations set the scheme and its critical questions now used in argumentation theory and computational argumentation.[^s2]
- **Contrasts with ad verecundiam.** The fallacy is a misuse of this scheme. A use becomes fallacious when it fails a scheme requirement while seeming correct and seriously obstructs the goal of the dialogue.[^s1]
- **Formalized by Bayesian reasoning.** Harris and colleagues give the scheme a Bayesian network form whose nodes map onto most of Walton's questions.[^s3]
- **Supported by the Harris et al. 2016 experiments,** which found close agreement between the model's predictions and average ratings.[^s3]
- **Influenced by John Locke.** Locke's discussion of *ad verecundiam* is the classic starting point for later treatments of appeals to authority.[^s1]
- **Related:** source credibility and testimony (how far to rely on what others say), presumption and burden of proof (who must answer which question), and ad hominem, which attacks a source as this scheme relies on one.[^s1][^s2]

## Sources

[^s1]: Hansen, "Fallacies", *Stanford Encyclopedia of Philosophy* (2024 revision). https://plato.stanford.edu/entries/fallacies/ (accessed 2026-11-08)
[^s2]: Walton, "On a Razor's Edge: Evaluating Arguments from Expert Opinion", *Argument & Computation* 5(2-3), 2014. https://core.ac.uk/download/72794558.pdf (accessed 2026-11-08)
[^s3]: Harris, Hahn, Madsen & Hsu, "The appeal to expert opinion: quantitative support for a Bayesian network approach", *Cognitive Science* 40(6), 2016. https://discovery-pp.ucl.ac.uk/id/eprint/1468674/1/Harris_Hahn_Madsen_Hsu_2015.pdf (accessed 2026-11-08)
[^s4]: Dowden, "Fallacies", *Internet Encyclopedia of Philosophy*. https://iep.utm.edu/fallacy/ (accessed 2026-11-08)
