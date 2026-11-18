---
id: ct:probabilistic-modus-tollens
type: FormalFallacy
title: Probabilistic modus tollens
aliases: [illusion of probabilistic proof by contradiction, illusion of attaining improbability, probabilistic proof by contradiction]
domain: formal-fallacies
summary: >-
  The invalid inference from "if H, then E is very improbable" and "E
  occurred" to "H is probably false". It copies the shape of modus tollens,
  but once the conditional is only probabilistic the conclusion no longer
  follows, and it underlies a common misreading of significance tests.
level: intermediate
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:modus-tollens, ct:inverse-fallacy, ct:null-hypothesis-significance-testing, ct:likelihood-ratio, ct:hypothesis-testing, ct:probabilistic-fallacy, ct:denying-the-antecedent, ct:jacob-cohen]
requires: [ct:modus-tollens, ct:conditional-probability, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:modus-tollens, source: s1, confidence: high}
  - {predicate: confusedWith, object: ct:reductio-ad-absurdum, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:inverse-fallacy, source: s1, confidence: medium}
  - {predicate: contrastsWith, object: ct:likelihood-ratio, source: s3, confidence: high}
criticalQuestions:
  - Does the hypothesis actually rule out the observation, or does it only make it unlikely?
  - How probable would the same observation be under the most plausible rival hypothesis?
  - How plausible was the hypothesis before the observation, and has that prior been ignored?
  - Is a probability of the data given the hypothesis being reported as if it were the probability of the hypothesis given the data?
argumentMap:
  premises:
    - "If a support ticket comes from a paying customer, it very probably does not come from our single largest account."
    - "This ticket comes from our single largest account."
  conclusion: "This ticket probably does not come from a paying customer."
  verdict: invalid
  scheme: ct:modus-tollens
  objections:
    - "The largest account is itself a paying customer, so the conclusion is certainly false even though both premises are true."
    - "The first premise is true only because there are thousands of customers; rarity under the hypothesis says nothing about rarity under the alternatives."
sources:
  - id: s1
    title: "The Earth is round (p < .05)"
    publisher: American Psychologist 49(12), 997-1003 (Cohen, 1994)
    url: https://www.stat.cmu.edu/~brian/nynke/726-2007/726-402%20papers%20and%20projects/Cohen_AmerPsych_1994.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "Significance tests die hard: The amazing persistence of a probabilistic misconception"
    publisher: Theory & Psychology 5(1), 75-98 (Falk & Greenbaum, 1995), Hebrew University research portal
    url: https://cris.huji.ac.il/en/publications/significance-tests-die-hard-the-amazing-persistence-of-a-probabil/
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "Intelligent design and probability reasoning"
    publisher: International Journal for Philosophy of Religion 52(2), 65-80 (Sober, 2002), author's copy hosted by the University of Illinois
    url: https://courses.physics.illinois.edu/phys419/sp2011/lectures/Sober-Intelligent%20Design-27.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Commentary: The need for Bayesian hypothesis testing in psychological science"
    publisher: Frontiers in Psychology 8, 1434 (Perezgonzalez, 2017)
    url: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.01434/full
    type: peer-reviewed
    accessed: 2026-11-18
created: 2026-11-18
---

# Probabilistic modus tollens

Probabilistic modus tollens is the inference "if hypothesis H is true, observation E is very unlikely; E occurred; therefore H is probably false". It borrows the shape of modus tollens, which is deductively valid when the conditional is strict: if H guarantees not-E and E occurs, H must be false. Once the first premise only says that E is improbable under H, the guarantee is gone and the argument becomes invalid: both premises can be true while the conclusion is false.[^s1][^s3] Falk and Greenbaum called the resulting belief the illusion of probabilistic proof by contradiction.[^s2]

## Origin

The criticism grew out of debates about null hypothesis significance testing in psychology. Jacob Cohen's 1994 *American Psychologist* paper set the valid strict syllogism beside its probabilistic twin and showed the twin fails, crediting the counterexample to Pollard and Richardson (1987) and noting that Falk and Greenbaum had named the error the illusion of attaining improbability.[^s1] Falk and Greenbaum (1995) argued that this illusion is the main reason significance tests persist despite their logical problems, presenting data from a student sample and examples from the research literature.[^s2] Philosopher Elliott Sober (2002) generalised the point: probabilistic reasoning has an analogue of modus ponens but, in his view, no analogue of modus tollens.[^s3]

## How it works

Cohen's illustration makes the gap obvious. "If a person is an American, he is probably not a member of Congress; this person is a member of Congress; so he is probably not an American" has true premises and a false conclusion.[^s1] The argument map above has the same structure in a workplace setting. Almost every paying customer is not the largest account, so the first premise is true, yet the ticket from the largest account is certainly from a paying customer. The premise is true only because the reference class is large, not because the hypothesis is doubtful.

Sober's cases show the same thing. A fair, well-shuffled deck gives any particular card a 1-in-52 chance, but drawing the seven of hearts is no evidence that the deck is rigged. In a long run of roulette spins, every exact sequence is wildly improbable under the fair-wheel hypothesis, yet some sequence must occur.[^s3] Low probability under H is common and, on its own, tells you nothing about H.

The fallacy often travels with confusion of the inverse. A p value reports the probability of data at least this extreme given the null hypothesis, but the probabilistic modus tollens reader treats a small p value as a small probability that the null is true. Cohen's screening example, with a rare condition and a test significant at p < .05, leaves the probability that a flagged case is normal at about .60.[^s1]

## How to spot it

Look for a conclusion of the form "so H is probably false" or "so this can't be chance" resting only on a premise that the observation would be unlikely under H. Warning signs include no stated alternative hypothesis, no mention of how plausible H was beforehand, and a p value or "one in a million" figure presented as if it were the probability of the hypothesis itself.[^s1][^s2] Falk and Greenbaum also point to wording that blurs the probability of the data with the probability of the hypothesis as a reason the illusion feels convincing.[^s2]

## How to counter it

Ask the comparative question: how probable is the observation under the best rival hypothesis? Sober, following the law of likelihood, holds that evidence favours H1 over H2 only when it is more probable under H1 than under H2, so evidence is always weighed against alternatives rather than against a single hypothesis in isolation.[^s3] A likelihood ratio makes that comparison explicit, and adding a prior probability turns it into a posterior. Where a hypothesis strictly entails an outcome, ordinary modus tollens still applies and a failed prediction refutes it.[^s3]

Not every critic accepts that significance testing commits the fallacy. Perezgonzalez (2017) argues that a frequentist test can be read as a strict modus tollens about whether a result falls in a pre-set rejection region. On that reading, the error lies in the probabilistic paraphrase, not in the test itself.[^s4]

## Connections

It is the invalid counterpart of modus tollens: the valid form needs a strict conditional, and weakening it to "very probably not" breaks validity.[^s1] Falk and Greenbaum trace its appeal to its resemblance to proof by contradiction, so it is commonly confused with a legitimate reductio ad absurdum.[^s2] It contrasts with confusion of the inverse, a separate error that often accompanies it when P(data | H0) is read as P(H0 | data).[^s1] It contrasts with the comparative reasoning of the likelihood-ratio framework, which Sober offers in its place.[^s3] It sits under formal fallacies and bears directly on how results of null hypothesis significance testing are reported and read.[^s1][^s4]

## Sources

[^s1]: Cohen, J. (1994). "The Earth is round (p < .05)." *American Psychologist*, 49(12), 997-1003. https://www.stat.cmu.edu/~brian/nynke/726-2007/726-402%20papers%20and%20projects/Cohen_AmerPsych_1994.pdf (accessed 2026-11-18)
[^s2]: Falk, R., & Greenbaum, C. W. (1995). "Significance tests die hard: The amazing persistence of a probabilistic misconception." *Theory & Psychology*, 5(1), 75-98. https://cris.huji.ac.il/en/publications/significance-tests-die-hard-the-amazing-persistence-of-a-probabil/ (accessed 2026-11-18)
[^s3]: Sober, E. (2002). "Intelligent design and probability reasoning." *International Journal for Philosophy of Religion*, 52(2), 65-80. https://courses.physics.illinois.edu/phys419/sp2011/lectures/Sober-Intelligent%20Design-27.pdf (accessed 2026-11-18)
[^s4]: Perezgonzalez, J. D. (2017). "Commentary: The need for Bayesian hypothesis testing in psychological science." *Frontiers in Psychology*, 8, 1434. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.01434/full (accessed 2026-11-18)
