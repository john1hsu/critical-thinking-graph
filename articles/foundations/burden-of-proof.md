---
id: ct:burden-of-proof
type: Concept
title: Burden of proof
aliases: [onus probandi, onus of proof, probative burden]
domain: foundations
summary: >-
  The obligation, carried by one side of a dispute, to support a claim with
  enough evidence or argument to meet the applicable standard; if the burden is
  not met, the claim is not accepted, though its opposite is not thereby proven.
level: introductory
evidenceStatus: normative
broader: [ct:argument-evaluation]
related: [ct:argument-from-ignorance, ct:presumption, ct:pragma-dialectics, ct:argumentation-schemes, ct:charles-hamblin, ct:informal-fallacy]
requires: [ct:argument]
relations:
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:legal-reasoning, source: s3, confidence: high}
  - {predicate: formalizedBy, object: ct:formal-dialogue-systems, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "A Theory of Presumption for Everyday Argumentation"
    publisher: "Pragmatics & Cognition 15(2), 2007 (Godden and Walton), PhilArchive copy"
    url: https://philarchive.org/archive/GODATO-3
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s2
    title: "Burden of Proof in Dialogue Systems, in Burden of Proof, Presumption and Argumentation"
    publisher: Cambridge University Press (Walton, 2014)
    url: https://www.cambridge.org/core/books/burden-of-proof-presumption-and-argumentation/burden-of-proof-in-dialogue-systems/B0D1865380C7A40D8005123CECA3F172
    type: primary
    accessed: 2026-11-06
  - id: s3
    title: "A Logical Analysis of Burdens of Proof, in Legal Evidence and Proof"
    publisher: Prakken and Sartor, course reading hosted by the University of Groningen
    url: https://www.ai.rug.nl/~verheij/sysu2018/readings/PrakkenSartor2009ALogicalAnalysisofBurdensofProof.pdf
    type: academic
    accessed: 2026-11-06
  - id: s4
    title: "Burden of persuasion"
    publisher: Legal Information Institute, Cornell Law School (Wex)
    url: https://www.law.cornell.edu/wex/burden_of_persuasion
    type: academic
    accessed: 2026-11-06
  - id: s5
    title: "Conceptualizing Fallacies: The Informal Logic and Pragma-Dialectic Approaches to the Argumentum ad Ignorantiam"
    publisher: ISSA Proceedings 2002 (Wagemans), Rozenberg Quarterly
    url: https://rozenbergquarterly.com/issa-proceedings-2002-conceptualizing-fallacies-the-informal-logic-and-pragma-dialectic-approaches-to-the-argumentum-ad-ignorantiam/?print=pdf
    type: peer-reviewed
    accessed: 2026-11-06
created: 2026-11-06
---

# Burden of proof

The burden of proof is the duty one party in a dispute has to back up a claim before others are obliged to accept it. Whoever holds it loses the point if they do not meet it; the other side can simply decline to be convinced. In everyday argument the burden usually falls on the person who advances a new claim, while a presumption places it on whoever wants to reject a claim that already enjoys default acceptance.[^s1] Outside courts and other institutions, failing to carry the burden carries no penalty beyond leaving the claim unpersuasive, a point Godden and Walton attribute to Sidgwick.[^s1]

## Origin

The idea, often given its Latin name *onus probandi*, comes from Roman law, where the burden lay on the party making an allegation; Rescher noted that the same default survives in modern Anglo-American procedure.[^s1] In rhetoric, Richard Whately's *Elements of Rhetoric* (1846 edition) tied the burden to presumption: a presumption in favour of a claim puts the burden on whoever disputes it, and the burden moves only when a counter-presumption is raised.[^s1] In twentieth-century argumentation theory, Charles Hamblin's 1970 *Fallacies* set the topic aside in favour of a simpler notion of initiative in formal dialogue; Douglas Walton later extended Hamblin's dialogue system to model how burdens shift during an exchange.[^s2]

## How it works

Scholars separate several burdens that ordinary talk lumps together. Law distinguishes the burden of production, the duty to bring enough evidence to put an issue in play at all, from the burden of persuasion, the duty to convince the fact-finder to the required standard.[^s4] The standard varies with the stakes: a preponderance of the evidence in most civil cases, beyond reasonable doubt for the prosecution in criminal cases.[^s4] Prakken and Sartor add a third, the tactical burden: no rule assigns it, but a party who would probably lose if the debate ended now has practical reason to produce more, and it can pass back and forth many times, whereas the legal burdens of persuasion and production stay where the law puts them.[^s3]

Argumentation theorists draw a parallel line between a global burden, which concerns the overall case one side must make, and a local burden attached to a particular claim at a particular moment.[^s1] Presumptions work locally. Rebutting one usually only requires casting enough doubt on it, not proving its opposite, and once it is defeated the burden returns to where it normally sits.[^s1]

A workplace example. An engineer proposes moving the team's build system to a new tool. The proposal changes the status quo, so the engineer carries the global burden of showing the switch is worth the cost. A colleague objects that the new tool will slow builds. If the objection comes with no evidence, it adds little; once the colleague shares benchmark data, a local, tactical burden passes back to the engineer to answer it.[^s3] Neither side has proven anything merely because the other went quiet.[^s5]

## How to apply it

1. Name the claim actually at issue and ask who is proposing a change from the default; that side normally starts with the burden.[^s1]
2. Ask what standard fits the stakes. A reversible team experiment needs less than a safety-critical change, just as civil and criminal trials use different thresholds.[^s4]
3. Track shifts. When an objection is backed by evidence, the burden to respond moves; a bare "prove it isn't so" does not move it.[^s3]
4. Watch for the step from "you have not proven P" to "so not-P". Walton treats a reversed burden that the other side cannot meet as the mark of a fallacious argument from ignorance, while pragma-dialectics treats any such step as treating a failed defence as proof of the opposite.[^s5]

## Connections

Burden of proof is a core topic of **argumentation theory**, where Walton's book-length study treats it alongside presumption in dialogue.[^s2] It is **formalized by** formal dialogue systems, which extend Hamblin's question-and-answer framework with rules for who must support what and when that obligation moves.[^s2] It is **applied in** legal reasoning, which supplies the sharpest vocabulary for its kinds: persuasion, production and tactical burdens.[^s3]

The concept is tightly bound to **presumption**, which Godden and Walton define by where it places the burden.[^s1] It underlies the **argument from ignorance**: both informal logic and pragma-dialectics analyse that fallacy as a mishandled burden, differing on whether some such arguments can still be reasonable.[^s5] In **pragma-dialectics** the burden attaches to the role of protagonist, the party who advances a standpoint, and the critic who forgets that role assignment commits the ignorance fallacy.[^s5]

## Sources

[^s1]: Godden and Walton, "A Theory of Presumption for Everyday Argumentation", *Pragmatics & Cognition* 15(2), 2007. https://philarchive.org/archive/GODATO-3 (accessed 2026-11-06)
[^s2]: Walton, "Burden of Proof in Dialogue Systems", ch. 5 of *Burden of Proof, Presumption and Argumentation*, Cambridge University Press, 2014. https://www.cambridge.org/core/books/burden-of-proof-presumption-and-argumentation/burden-of-proof-in-dialogue-systems/B0D1865380C7A40D8005123CECA3F172 (accessed 2026-11-06)
[^s3]: Prakken and Sartor, "A Logical Analysis of Burdens of Proof", in *Legal Evidence and Proof*. https://www.ai.rug.nl/~verheij/sysu2018/readings/PrakkenSartor2009ALogicalAnalysisofBurdensofProof.pdf (accessed 2026-11-06)
[^s4]: "Burden of persuasion", Wex, Legal Information Institute, Cornell Law School. https://www.law.cornell.edu/wex/burden_of_persuasion (accessed 2026-11-06)
[^s5]: Wagemans, "Conceptualizing Fallacies: The Informal Logic and Pragma-Dialectic Approaches to the Argumentum ad Ignorantiam", ISSA Proceedings 2002. https://rozenbergquarterly.com/issa-proceedings-2002-conceptualizing-fallacies-the-informal-logic-and-pragma-dialectic-approaches-to-the-argumentum-ad-ignorantiam/?print=pdf (accessed 2026-11-06)
