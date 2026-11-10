---
id: ct:argument-from-analogy
type: ArgumentScheme
title: Argument from analogy
aliases: [argument by analogy, analogical argument, argument from similarity, argument from a parallel case]
domain: argumentation
summary: >-
  The presumptive argument pattern "case C1 is similar to case C2; conclusion A
  holds in C1; so A plausibly holds in C2". Its strength depends on whether the
  shared features are relevant to A, whether relevant differences undercut the
  comparison, and whether a rival analogy points the other way.
level: introductory
evidenceStatus: normative
broader: [ct:argumentation-schemes]
related: [ct:douglas-walton, ct:inductive-reasoning, ct:analogical-reasoning, ct:structure-mapping-theory, ct:defeasible-reasoning, ct:argument-from-expert-opinion, ct:hasty-generalization, ct:thomas-reid]
requires: [ct:argument]
relations:
  - {predicate: influencedBy, object: ct:aristotle, source: s1, confidence: high}
  - {predicate: misusedAs, object: ct:faulty-analogy, source: s4, confidence: high}
  - {predicate: contrastsWith, object: ct:inductive-reasoning, source: s1, confidence: medium}
  - {predicate: appliedIn, object: ct:legal-reasoning, source: s3, confidence: high}
criticalQuestions:
  - Are there differences between the two cases that would undermine the similarity being relied on?
  - Are the shared features actually relevant to the conclusion, or only superficial?
  - Is the conclusion really correct for the source case in the first place?
  - Is there another similar case where a different conclusion was reached?
  - Is the conclusion modest enough for the strength of the comparison?
argumentMap:
  premises:
    - "Last year the support team moved to a four-day week and its response times stayed steady."
    - "The sales team is similar: same office, similar headcount, mostly remote customer contact."
  conclusion: "The sales team can move to a four-day week without hurting its results."
  verdict: weak
  scheme: ct:argument-from-analogy
  objections:
    - "Sales closes most deals in Friday client meetings, a difference that matters to the conclusion."
    - "The engineering team tried the same change and missed two release dates, a counter-analogy."
sameAs: []
sources:
  - id: s1
    title: "Analogy and Analogical Reasoning"
    publisher: Stanford Encyclopedia of Philosophy (Paul Bartha, first published 2013; substantive revision 2019)
    url: https://plato.stanford.edu/entries/reasoning-analogy/
    type: scholarly-encyclopedia
    accessed: 2026-11-10
  - id: s2
    title: "Argumentation Schemes for Argument from Analogy"
    publisher: "Douglas Walton, in H. J. Ribeiro (ed.), Systematic Approaches to Argument by Analogy, Springer, 2014, pp. 23-40; CORE open-access copy"
    url: https://core.ac.uk/download/72794547.pdf
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "The Structure of Arguments by Analogy in Law"
    publisher: "Argumentation 31(2), 359-393 (Luís Duarte d'Almeida & Cláudio Michelon, 2017)"
    url: https://link.springer.com/article/10.1007/s10503-016-9409-3
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s4
    title: "Faulty Analogy"
    publisher: Texas State University, Department of Philosophy, fallacy definitions
    url: https://www.txst.edu/philosophy/resources/fallacy-definitions/Faulty-Analogy.html
    type: academic
    accessed: 2026-11-10
created: 2026-11-10
---

# Argument from analogy

An argument from analogy reasons from one case to another: because a source case resembles a target case in known respects, a further feature or verdict found in the source is projected onto the target.[^s1] Douglas Walton states it as a scheme with three parts. A situation is described in case C1, a conclusion A is acceptable in C1, and C1 is generally similar to C2, so A is plausibly acceptable in C2.[^s2] Like other argumentation schemes it is defeasible. It shifts a presumption toward its conclusion, and that presumption can be defeated by critical questions.[^s2] The same form covers good and bad arguments, and philosophers have not found a general inference rule that separates them.[^s1]

## Origin

Aristotle gave the first systematic treatment. His argument from example (*paradeigma*) moves from a similar case to a general premise and then applies it. One illustration runs: fighting one's neighbours is evil, and a war between two neighbouring cities is such a fight, so it is evil. He also discussed arguments from likeness, which do not depend on first securing a general premise.[^s1] In the eighteenth century Thomas Reid argued that because other planets, like Earth, orbit the sun, have moons and rotate, it is not unreasonable to think they may be inhabited. The conclusion is kept modest to match the comparison.[^s1] John Stuart Mill later treated analogy as a kind of inductive sampling argument.[^s1]

Walton turned the topic into a scheme with critical questions, as part of his broader catalogue of argumentation schemes. He also distinguishes a second, factor-based form, common in logic textbooks, that weighs shared and differing features without appealing to overall similarity.[^s2]

## How it works

Mary Hesse (1966) laid an analogy out as two columns, with known similarities (the positive analogy), known differences (the negative analogy) and features not yet known to match or differ (the neutral analogy).[^s1] An argument from analogy projects something from the source column into the target.[^s1]

In the argument map above, a manager reasons that because a four-day week worked for the support team, it will work for the similar sales team. The listed similarities (office, headcount, remote contact) are real but say little about how sales are closed. The first objection names a relevant difference, Friday client meetings. The second offers a counter-analogy, an engineering team where the change went badly. Together they leave the argument weak until the manager shows that the features that made the support trial work are also present in sales.[^s2]

## How to apply it

Walton's critical questions give the core test. Are there differences between the cases that undermine the similarity? Is the conclusion right for the source case? Is there another similar case where a different conclusion should be drawn?[^s2] The Stanford Encyclopedia lists further rules of thumb from logic textbooks. More relevant similarities and fewer differences make an analogy stronger. A more modest conclusion is easier to support. Causal and structural similarities count for more than surface ones. Several independent analogies support a conclusion better than one. The entry warns that these rules are vague and can pull against each other.[^s1]

1. Name the source case, the target case and the exact conclusion being carried over.[^s2]
2. Ask what in the source case actually produced the outcome, then check that it is present in the target. Paul Bartha's articulation model makes this the central test: a good analogy needs a clear link in the source between the shared features and the conclusion, and no critical difference that blocks that link in the target.[^s1]
3. Look for a counter-analogy, a third case that resembles the source but went the other way, and weigh the two.[^s2]
4. Scale the conclusion to the evidence. Analogy is better at making a hypothesis plausible than at settling it.[^s1]

The common failure is the faulty analogy, which assumes that things alike in some respects must be alike in another. The Texas State philosophy department's example compares a morning coffee habit with alcoholism: both involve daily reliance on a substance, but that does not make them equally serious.[^s4]

## In law

Analogy is a central case in law. Under the doctrine of precedent, courts are expected to decide similar cases consistently with earlier rulings, which the Stanford Encyclopedia justifies as a balance between predictability and gradual legal change.[^s1] Walton analyses legal argument as a three-step exchange: one side cites a precedent, the other distinguishes it or cites a counter-precedent, and the first replies.[^s2] Duarte d'Almeida and Michelon (2017) argue that the usual feature-matching account fits legal analogy poorly. They argue that a legal analogy concludes how a case ought to be decided and must reflect that the earlier case was decided by an authority.[^s3]

## Connections

- **Influenced by Aristotle.** Aristotle's argument from example is the earliest systematic account and the starting point for later treatments.[^s1]
- **Misused as faulty analogy.** The fallacy relies on surface similarities that are not relevant to the conclusion.[^s4]
- **Contrasts with inductive reasoning.** Mill and others treat analogy as induction from a sample, but the Stanford Encyclopedia argues that this fits most analogies poorly, and some authors deny that any single formal schema captures them.[^s1]
- **Applied in legal reasoning.** Reasoning from precedent is the most studied practical use, and it raises its own problems about authority and normative conclusions.[^s3]
- **Related:** Douglas Walton's scheme framework, defeasible reasoning, argument from expert opinion as a sibling scheme, and analogical reasoning and structure-mapping theory, which study how people find and use analogies.[^s2][^s1]

## Sources

[^s1]: Bartha, "Analogy and Analogical Reasoning", *Stanford Encyclopedia of Philosophy* (2019 revision). https://plato.stanford.edu/entries/reasoning-analogy/ (accessed 2026-11-10)
[^s2]: Walton, "Argumentation Schemes for Argument from Analogy", in Ribeiro (ed.), *Systematic Approaches to Argument by Analogy*, Springer, 2014. https://core.ac.uk/download/72794547.pdf (accessed 2026-11-10)
[^s3]: Duarte d'Almeida & Michelon, "The Structure of Arguments by Analogy in Law", *Argumentation* 31(2), 2017. https://link.springer.com/article/10.1007/s10503-016-9409-3 (accessed 2026-11-10)
[^s4]: Texas State University, Department of Philosophy, "Faulty Analogy". https://www.txst.edu/philosophy/resources/fallacy-definitions/Faulty-Analogy.html (accessed 2026-11-10)
