---
id: ct:argument-from-fallacy
type: FormalFallacy
title: Argument from fallacy
aliases: [fallacy fallacy, argumentum ad logicam, fallacist's fallacy, argument to logic]
domain: formal-fallacies
summary: >-
  The invalid inference from "the argument offered for P is fallacious" to
  "P is false". A bad argument shows only that the conclusion has not been
  supported by that argument; the conclusion may still be true.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:denying-the-antecedent, ct:soundness, ct:argument-evaluation, ct:ad-hominem, ct:argument-from-ignorance, ct:informal-fallacy, ct:burden-of-proof]
requires: [ct:validity, ct:soundness]
relations:
  - {predicate: contrastsWith, object: ct:ad-hominem, source: s1, confidence: medium}
  - {predicate: introducedBy, object: ct:david-hackett-fischer, source: s1, confidence: medium}
  - {predicate: introducedIn, object: ct:historians-fallacies, source: s1, confidence: medium}
criticalQuestions:
  - Does the critic only show that the argument fails, or do they also give an independent reason to think the conclusion is false?
  - Are there other, better arguments or evidence for the same conclusion that the critique leaves untouched?
  - Was the alleged fallacy actually committed, or has the argument been misdiagnosed or uncharitably reconstructed?
  - Would it be enough to say "not yet supported" instead of "false"?
argumentMap:
  premises:
    - "The vendor argued that the new scheduling tool will cut overtime, citing a single hand-picked pilot site."
    - "Generalizing from one hand-picked site is a hasty generalization."
  conclusion: "So the new scheduling tool will not cut overtime."
  verdict: invalid
  objections:
    - "The flaw shows only that the vendor's evidence is too thin; the tool might still cut overtime, which a proper trial across several sites could reveal."
    - "Rejecting the vendor's argument justifies suspending judgment, not accepting the opposite claim."
sameAs: []
sources:
  - id: s1
    title: "The Fallacy Fallacy: From the Owl of Minerva to the Lark of Arete"
    publisher: "Argumentation (Andrew Aberdein, 2023), author's copy on PhilArchive"
    url: https://philarchive.org/archive/ABETFF-2
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "Argument from Fallacy"
    publisher: "Christian Cotton, in Arp, Barbone & Bruce (eds.), Bad Arguments, Wiley, 2018 (record on PhilPapers)"
    url: https://philpapers.org/rec/COTAFF-3
    type: textbook
    accessed: 2026-11-17
  - id: s3
    title: "Fallacies"
    publisher: Internet Encyclopedia of Philosophy (Bradley Dowden)
    url: https://iep.utm.edu/fallacy/
    type: scholarly-encyclopedia
    accessed: 2026-11-17
  - id: s4
    title: "SticiGui: Reasoning (chapter on logic and fallacies)"
    publisher: "Department of Statistics, University of California, Berkeley (SticiGui course text)"
    url: https://www.stat.berkeley.edu/~stark/SticiGui/Text/reasoning.htm
    type: academic
    accessed: 2026-11-17
created: 2026-11-17
---

# Argument from fallacy

The argument from fallacy, often called the *fallacy fallacy*, *argumentum ad logicam* or the *fallacist's fallacy*, is the move from "the argument for this claim is fallacious" to "this claim is false".[^s2] The error confuses two different things that can go wrong. Truth and falsity belong to claims, while fallacies are mistakes in the reasoning that connects premises to a conclusion. Someone who reasons badly has made a logical mistake, not necessarily a factual one.[^s2] As the Internet Encyclopedia of Philosophy puts it, a true conclusion can be reached by poor reasoning, so reaching the truth is no proof of good reasoning, and the converse holds too: poor reasoning is no proof of a false conclusion.[^s3]

## Origin

Aberdein traces the idea back to Schopenhauer's *The Art of Controversy* (1896), which ironically recommends a trick: refute an opponent's weak proof and then claim the whole position refuted.[^s1] The label "fallacist's fallacy" was coined by the historian David Hackett Fischer in *Historians' Fallacies* (1970), in a list of propositions about fallacies, two of which match the modern notion.[^s1] Aberdein credits Cotton's chapter in the collection *Bad Arguments* as the first stand-alone treatment, and notes that authors use the label in two senses. One is misdiagnosis: calling a view fallacious without showing any actual error. The other, the sense used here, is inferring that the conclusion is false.[^s1][^s2]

## How it works

The fallacy has the form: *argument A for P is fallacious (or unsound); therefore not-P*. Read as an inference, it relies on a hidden conditional, "if A is a good argument, P is true", and then denies the antecedent. A failed argument leaves the truth of P undetermined, just as denying the antecedent leaves the consequent undetermined.[^s4][^s2] Cotton's own illustration is affirming the consequent: the form is invalid, yet particular instances can have true conclusions.[^s2]

The argument map above gives a workplace version. A vendor claims a new scheduling tool will cut overtime, but supports the claim with a single hand-picked pilot site. A manager correctly spots the hasty generalization and then announces that the tool will not cut overtime. The first step is good criticism; the second is the fallacy. The vendor's evidence is too thin to show anything either way, and a fair trial across several sites might well show savings.[^s2][^s4]

Aberdein sharpens the distinction by separating two kinds of fallacy charge. An *undercutting* charge says only that the inference fails, which is a legitimate and necessary part of evaluating arguments. A *rebutting* charge goes further and declares the conclusion false. Every rebutting charge includes an undercutting one, but the extra step needs evidence of its own.[^s1]

## How to spot it

Watch for a critique that names a flaw in someone's reasoning and then treats the matter as settled against their conclusion: "That's a straw man, so you're wrong."[^s1][^s2] Ask whether the critic has offered any independent reason to think the conclusion false, or only a reason to distrust one argument for it.[^s1] Be alert to the misdiagnosis form too. The IEP warns that a charge of fallacious reasoning always needs to be justified, and that attaching a fallacy name is no substitute for examining the passage, since some reasoning that looks fallacious turns out not to be.[^s3]

## How to counter it

Keep the verdict proportional to the finding. If you have shown that an argument is invalid or rests on a false premise, the honest conclusion is "this argument does not establish P", followed by suspending judgment or looking for better evidence.[^s2][^s4] Before rejecting the conclusion, check whether other arguments support it; refuting the weakest case for a position does not touch the strongest.[^s1] Aberdein suggests that fallacy labels, like other tools for spotting bad argument, can themselves be misused, and argues that cultivating argumentative virtues is the remedy.[^s1]

## Connections

- **Contrasts with ad hominem.** Aberdein argues that the fallacy fallacy does to the appraisal of arguments what the ad hominem does to the appraisal of arguers: it moves from a fault found in the reasoning, or the reasoner, to the falsity of the claim.[^s1]
- **Introduced by David Hackett Fischer in *Historians' Fallacies*.** Fischer's "fallacist's fallacy" is the earliest named version Aberdein identifies; Schopenhauer anticipated the idea without naming it.[^s1]
- **Related to denying the antecedent.** Treating a failed argument as proof of the opposite has the shape of denying the antecedent, which leaves the conclusion undetermined.[^s4]
- **Related to soundness, validity and argument evaluation.** The fallacy arises from forgetting that validity and soundness are properties of arguments, while truth is a property of claims.[^s2][^s4]
- **Related to argument from ignorance and burden of proof.** Both fallacies treat a gap in support, whether an absent proof or a bad one, as if it were evidence for the opposite, whereas a flawed argument shows only that the claim is so far unsupported.[^s2]

## Sources

[^s1]: Aberdein, "The Fallacy Fallacy: From the Owl of Minerva to the Lark of Arete", *Argumentation*, 2023 (author's copy). https://philarchive.org/archive/ABETFF-2 (accessed 2026-11-17)
[^s2]: Cotton, "Argument from Fallacy", in Arp, Barbone & Bruce (eds.), *Bad Arguments*, Wiley, 2018. https://philpapers.org/rec/COTAFF-3 (accessed 2026-11-17)
[^s3]: Dowden, "Fallacies", *Internet Encyclopedia of Philosophy*. https://iep.utm.edu/fallacy/ (accessed 2026-11-17)
[^s4]: "Reasoning", *SticiGui* online text, Department of Statistics, University of California, Berkeley. https://www.stat.berkeley.edu/~stark/SticiGui/Text/reasoning.htm (accessed 2026-11-17)
