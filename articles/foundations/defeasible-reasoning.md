---
id: ct:defeasible-reasoning
type: ReasoningMode
title: Defeasible reasoning
aliases: [defeasible inference, defeasible argument, defeasibility, prima facie reasoning]
domain: foundations
summary: >-
  Reasoning whose premises give real but provisional support to a conclusion,
  so that the conclusion can be rationally withdrawn when new information (a
  defeater) arrives, even though none of the original premises is retracted.
level: intermediate
evidenceStatus: normative
broader: [ct:reasoning]
related: [ct:inductive-reasoning, ct:inference-to-the-best-explanation, ct:toulmin-model, ct:argumentation-schemes, ct:argument-from-expert-opinion, ct:argument-from-analogy, ct:presumption, ct:burden-of-proof, ct:hasty-generalization, ct:modus-ponens, ct:cogency]
requires: [ct:argument, ct:validity]
relations:
  - {predicate: contrastsWith, object: ct:deductive-reasoning, source: s1, confidence: high}
  - {predicate: formalizedBy, object: ct:nonmonotonic-logic, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:h-l-a-hart, source: s1, confidence: medium}
  - {predicate: appliedIn, object: ct:legal-reasoning, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:artificial-intelligence, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:suppression-effect, source: s4, confidence: medium}
argumentMap:
  premises: ["The office thermostat reads 21 degrees.", "Thermostat readings are normally accurate."]
  conclusion: "The office is about 21 degrees."
  verdict: strong
  objections: ["Facilities reports that this thermostat's sensor has been faulty all week (undercutting defeater).", "A freshly calibrated thermometer on the same desk reads 26 degrees (rebutting defeater)."]
sameAs: []
sources:
  - id: s1
    title: "Defeasible Reasoning"
    publisher: Stanford Encyclopedia of Philosophy (Robert Koons, first published 2005, substantive revision 2025)
    url: https://plato.stanford.edu/entries/reasoning-defeasible
    type: scholarly-encyclopedia
    accessed: 2026-11-10
  - id: s2
    title: "Defeasible Reasoning (Cognitive Science 11(4), 1987, 481-518)"
    publisher: John L. Pollock, Cognitive Science, record on PhilPapers
    url: https://philpapers.org/rec/POLDR
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "Philosophy, Computing, and Artificial Intelligence (PHI 319), lecture on defeasible reasoning"
    publisher: Thomas A. Blackson, Arizona State University course notes
    url: https://tomblackson.com/PHI_319_420/lecture12.html
    type: academic
    accessed: 2026-11-10
  - id: s4
    title: "Inference Suppression and Working Memory Capacity: Inhibition of the Disabler Search"
    publisher: De Neys, Dieussaert, Schaeken and d'Ydewalle, Proceedings of the Annual Meeting of the Cognitive Science Society 26, 2004, eScholarship
    url: https://escholarship.org/content/qt1v95d3dg/qt1v95d3dg.pdf?t=op2jgy
    type: peer-reviewed
    accessed: 2026-11-10
created: 2026-11-10
---

# Defeasible reasoning

Defeasible reasoning is inference in which the premises give genuine rational support to a conclusion without guaranteeing it, so that further information can defeat that support.[^s1] The key mark is that a conclusion which was reasonable to draw can stop being reasonable when something is *added*, not because any premise turned out false. Logicians call this property nonmonotonicity: in classical deduction, adding premises never removes a conclusion, while in defeasible reasoning it can.[^s1] Most everyday and professional judgment works this way, because people must act on generalizations that hold only normally and on evidence they cannot exhaustively check.[^s2][^s3]

## Origin

The idea is old. Aristotle's dialectical reasoning in the *Topics* already relied on generalizations that hold only "for the most part".[^s1] The modern notion of defeasibility came from law: the legal philosopher H. L. A. Hart argued, in a paper presented to the Aristotelian Society in 1949, that legal claims such as "there is a valid contract" are defeasible, because a recognised exception can defeat them even when every standard condition is met.[^s1] In epistemology, Roderick Chisholm treated sensory appearances as giving reasons that can be overridden, and Stephen Toulmin's model of argument separated a warrant from the rebuttals that can block it.[^s1]

John Pollock turned these hints into a theory. In a 1987 *Cognitive Science* paper he argued against the long-standing view that good reasoning must be deductively valid, pointing out that many familiar kinds of reasoning are not valid yet still justify their conclusions.[^s2] His framework of *prima facie reasons* and *defeaters* is now standard.[^s1][^s3] In parallel, artificial-intelligence researchers who needed machines to reason about a world they only partly knew built nonmonotonic logics around 1980, including John McCarthy's circumscription, Ray Reiter's default logic and Drew McDermott and Jon Doyle's non-monotonic logic.[^s1]

## How it works

A defeasible inference moves from a reason to a conclusion that the reason supports *unless* something defeats it. Pollock distinguished two kinds of defeater.[^s1][^s3] A **rebutting defeater** is a reason to think the conclusion is false. An **undercutting defeater** is a reason to doubt that the premises support the conclusion in this case, without saying the conclusion is false.[^s3]

Take the argument map: an office thermostat reads 21 degrees, readings are normally accurate, so the room is about 21 degrees. That is a good inference. If facilities says the sensor has been faulty all week, the reading no longer supports the conclusion, but the room might still be 21 degrees; that is an undercutter. If a calibrated thermometer on the same desk reads 26 degrees, that is direct evidence against the conclusion; that is a rebutter. Blackson's notes give the parallel perceptual case of an object that looks red but turns out to be lit by red lights.[^s3]

Defeaters can themselves be defeated. If the "faulty sensor" report turns out to come from an unreliable source, the original inference is reinstated.[^s3] When two arguments of equal standing defeat each other, as in the textbook case of someone who is both a Quaker (typically pacifist) and a Republican (typically not), the rational response is to suspend judgment.[^s3]

## How to apply it

1. **Name the default.** State the generalization the inference leans on ("readings are normally accurate", "experts are usually right in their field") and treat it as a presumption, not a certainty.[^s1]
2. **Hunt for defeaters of both kinds.** Ask what would show the conclusion false (rebutters) and what would show this reason unreliable *here* (undercutters).[^s3]
3. **Match diligence to stakes.** Pollock's work, as summarised by Blackson, notes that a belief adequate for a trivial question may need much stronger support once the question becomes important.[^s3]
4. **Stay ready to retract.** Withdrawing a conclusion after a defeater appears is not inconsistency; it is what the inference always licensed.[^s1]

## Evidence and limitations

People do reason this way. In Ruth Byrne's 1989 suppression task, adding a premise that mentions a possible disabler (for instance, that a student will study late only if the library is open) makes many participants reject a modus ponens conclusion they would otherwise accept.[^s4] De Neys and colleagues reported in 2004 that this suppression effect has been confirmed in many studies and appeared in their own experiment at every level of working-memory capacity.[^s4] Researchers read such results as everyday reasoning taking background exceptions into account, not simply as logical error.[^s4]

The theory has open problems. Philosophers and AI researchers still disagree about which formal properties defeasible consequence should keep, such as cautious monotony or rational monotony, and about how to rank conflicting defaults.[^s1] Koons also notes that the narrow usage of the term sets aside induction, abduction and analogy, a boundary he calls somewhat artificial.[^s1]

## Connections

- **Broader: reasoning.** Defeasible inference is one of the main modes of reasoning, alongside deduction.[^s2]
- **Contrasts with deductive reasoning.** Deduction is monotonic; defeasible reasoning is not.[^s1]
- **Formalized by nonmonotonic logic.** Default logic, circumscription and related systems give defeasible consequence a formal treatment.[^s1]
- **Introduced by H. L. A. Hart.** Hart's 1949 analysis of legal concepts brought the term "defeasible" into philosophy.[^s1]
- **Applied in legal reasoning and artificial intelligence.** Legal argument with exceptions and commonsense reasoning in AI are its two classic applications.[^s1]
- **Supported by the suppression effect.** Suppression experiments show ordinary reasoners withdrawing conclusions when disablers are mentioned.[^s4]
- **Related: Toulmin model, argumentation schemes and presumption.** Toulmin's rebuttals and the critical questions attached to presumptive schemes work as ways to locate defeaters.[^s1]

## Sources

[^s1]: Robert Koons, "Defeasible Reasoning", *Stanford Encyclopedia of Philosophy* (substantive revision 2025). https://plato.stanford.edu/entries/reasoning-defeasible (accessed 2026-11-10)
[^s2]: John L. Pollock, "Defeasible Reasoning", *Cognitive Science* 11(4), 1987, 481-518, PhilPapers record. https://philpapers.org/rec/POLDR (accessed 2026-11-10)
[^s3]: Thomas A. Blackson, PHI 319 *Philosophy, Computing, and Artificial Intelligence*, lecture notes on defeasible reasoning, Arizona State University. https://tomblackson.com/PHI_319_420/lecture12.html (accessed 2026-11-10)
[^s4]: Wim De Neys, Kristien Dieussaert, Walter Schaeken and Géry d'Ydewalle, "Inference Suppression and Working Memory Capacity: Inhibition of the Disabler Search", *Proceedings of the Annual Meeting of the Cognitive Science Society* 26, 2004. https://escholarship.org/content/qt1v95d3dg/qt1v95d3dg.pdf?t=op2jgy (accessed 2026-11-10)
