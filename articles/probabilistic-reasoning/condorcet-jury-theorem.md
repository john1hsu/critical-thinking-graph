---
id: ct:condorcet-jury-theorem
type: Principle
title: Condorcet jury theorem
aliases: [Condorcet's jury theorem, CJT, jury theorem]
domain: probabilistic-reasoning
summary: >-
  The result that if each member of a group is more likely than not to be
  right on a yes-or-no question, and their judgments are independent, then
  the chance that the majority is right grows with group size and tends
  toward certainty. Its premises double as a test of when popularity is
  evidence and when it is not.
level: intermediate
evidenceStatus: normative
broader: [ct:probability-theory]
related: [ct:ad-populum, ct:wisdom-of-crowds, ct:groupthink, ct:bandwagon-effect, ct:kenneth-arrow, ct:argument-from-expert-opinion, ct:conditional-probability]
requires: [ct:conditional-probability]
relations:
  - {predicate: detects, object: ct:ad-populum, source: s2, confidence: high}
  - {predicate: introducedBy, object: ct:marquis-de-condorcet, source: s1, confidence: high}
  - {predicate: explains, object: ct:wisdom-of-crowds, source: s1, confidence: medium}
  - {predicate: appliedIn, object: ct:epistemic-democracy, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:social-epistemology, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Jury Theorems"
    publisher: "Stanford Encyclopedia of Philosophy (Kai Spiekermann, first published 2021)"
    url: https://plato.stanford.edu/ENTRIES/jury-theorems/
    type: scholarly-encyclopedia
    accessed: 2026-11-18
  - id: s2
    title: "Is an Appeal to Popularity a Fallacy of Popularity?"
    publisher: "Informal Logic 39(2), 147-167 (Don Dedrick, 2019), PhilArchive record"
    url: https://dc2.philarchive.org/rec/DEDIAA-4
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "Independent Opinions? On the Causal Foundations of Belief Formation and Jury Theorems"
    publisher: "Mind 122(487), 655-685 (Franz Dietrich & Kai Spiekermann, 2013), PhilArchive author copy"
    url: https://philarchive.org/archive/DIEIO
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Epistemic Democracy with Defensible Premises (MPRA Paper No. 40135)"
    publisher: "Franz Dietrich & Kai Spiekermann, Munich Personal RePEc Archive, 2012 working paper"
    url: https://core.ac.uk/download/213937818.pdf
    type: preprint
    accessed: 2026-11-18
created: 2026-11-18
---

# Condorcet jury theorem

The Condorcet jury theorem is a probabilistic result about majority judgment on a question with two possible answers, one of them correct. In its classical form it assumes that every member of the group is more likely than not to pick the right answer (competence) and that members' correctness is independent. Under those premises, the probability that the majority is right rises as the group gets larger and approaches one.[^s1] For critical thinkers its main value is the reverse reading: the premises spell out exactly what has to be true for "most people think so" to count as evidence.[^s2]

## Origin

The Marquis de Condorcet set out the result in his 1785 *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix*, written before modern probability notation; later authors such as Bernard Grofman restated it formally, and Grofman coined the name "Condorcet Jury Theorem" in 1975.[^s1] The theorem was later taken up by epistemic democrats, who use it to argue that majority voting tracks truth, and by social epistemologists studying courts, online crowds and peer disagreement.[^s1]

## How it works

The theorem has two conclusions that are worth keeping apart. The modest one is growing reliability: adding competent, independent voters makes a correct majority more likely. The strong one is asymptotic infallibility: a large enough group is almost certain to be right. The Stanford Encyclopedia entry argues that the strong conclusion is not tenable for real groups.[^s1]

The weak point is independence. Real voters share evidence, methods, news sources and even moods, and these common causes make their errors move together; a crowd of people who all read the same misleading report is, in effect, one witness repeated many times.[^s1] Dietrich and Spiekermann show that the classical independence condition holds only when the true state of the world is the sole common cause of opinions, and propose conditioning on the whole decision problem instead.[^s3] Once that is done, a striking result follows: on "hard" problems where individuals tend to be wrong, a bigger crowd becomes *more* reliably wrong.[^s3] In a stylised case from their working paper, voters who are right 99% of the time on easy problems but 49% on hard ones are individually right about 74% of the time, yet huge majorities drift toward a coin flip on the hard cases.[^s4]

A workplace example: twelve team leads all say a supplier is reliable. If each formed that view from separate dealings with the supplier, the agreement is real evidence. If all twelve are repeating one glowing case study the supplier sent round, the twelve votes carry roughly the weight of one, and the theorem gives no support to the majority.[^s3]

## How to apply it

Dedrick argues that the theorem rescues some appeals to popularity as legitimate inferences and that its conditions work as critical tools for judging any given appeal.[^s2] Before treating agreement as evidence, ask:

1. **Is there a fact of the matter?** The theorem needs a correct answer fixed independently of the vote, not a matter of taste or convention.[^s4]
2. **Are the people competent here?** Each must be better than chance on this kind of question; a crowd of people guessing about something they cannot observe adds nothing.[^s1]
3. **Did they judge independently?** Look for a shared source, an opinion leader others copy, or social pressure to conform.[^s1][^s3]
4. **Are they reporting sincerely?** Strategic or expressive voting can break the link between votes and private judgment; Austen-Smith and Banks showed that sincere voting is often not an equilibrium when voters hold private information.[^s1]
5. **Is the question easy or hard?** On hard questions, size does not cure systematic error.[^s3]

## Limitations

The theorem is a conditional mathematical result, not an empirical finding, so its force depends entirely on whether its premises hold. Critics such as David Estlund doubt that voter competence can be established beyond reasonable doubt, and heterogeneous competence means adding less competent members can make a group worse.[^s1] Treating the theorem as a blanket licence for majorities commits the very ad populum error it is best used to diagnose.[^s2]

## Connections

- It **helps detect** the ad populum fallacy: Dedrick proposes its conditions as critical tools for separating good appeals to popularity from fallacious ones.[^s2]
- It was **introduced by** the Marquis de Condorcet in 1785.[^s1]
- It offers one **explanation** of the wisdom of crowds; the SEP entry links jury reasoning to Galton's 1907 finding that the median guess at a fair came within 0.8% of an ox's weight.[^s1]
- It is **applied in** epistemic democracy, where it is used to argue for the truth-tracking value of majority rule.[^s1]
- It is **studied in** social epistemology.[^s1]
- It sits near groupthink and the bandwagon effect, both of which are ways the independence premise fails; when people copy one another or an opinion leader, their judgments stop being independent.[^s1][^s3]

## Sources

[^s1]: Spiekermann, "Jury Theorems", Stanford Encyclopedia of Philosophy (2021). https://plato.stanford.edu/ENTRIES/jury-theorems/ (accessed 2026-11-18)
[^s2]: Dedrick, "Is an Appeal to Popularity a Fallacy of Popularity?", Informal Logic 39(2), 2019, 147-167. https://dc2.philarchive.org/rec/DEDIAA-4 (accessed 2026-11-18)
[^s3]: Dietrich & Spiekermann, "Independent Opinions? On the Causal Foundations of Belief Formation and Jury Theorems", Mind 122(487), 2013, 655-685. https://philarchive.org/archive/DIEIO (accessed 2026-11-18)
[^s4]: Dietrich & Spiekermann, "Epistemic Democracy with Defensible Premises", MPRA Paper No. 40135 (2012). https://core.ac.uk/download/213937818.pdf (accessed 2026-11-18)
