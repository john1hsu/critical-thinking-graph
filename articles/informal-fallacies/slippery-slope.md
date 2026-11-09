---
id: ct:slippery-slope
type: InformalFallacy
title: Slippery slope
aliases: [slippery slope argument, slippery slope fallacy, thin edge of the wedge, wedge argument]
domain: informal-fallacies
summary: >-
  An argument that a proposed first step should be rejected because it would
  set off a chain of further steps ending in an unacceptable outcome; it is
  fallacious when the chain, the point of no return or the outcome's
  likelihood is asserted rather than supported.
level: introductory
evidenceStatus: normative
broader: [ct:informal-fallacy]
related: [ct:argumentation-schemes, ct:burden-of-proof, ct:post-hoc-ergo-propter-hoc, ct:vagueness, ct:sorites-paradox, ct:false-dilemma]
requires: [ct:argument]
relations:
  - {predicate: instanceOf, object: ct:argument-from-consequences, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:bayesian-reasoning, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s1, confidence: high}
criticalQuestions:
  - What are the intermediate steps between the first move and the feared outcome, and is each one supported by evidence rather than just asserted?
  - Why would we lose the ability to stop partway, and could a clear rule or bright line be drawn to halt the slide?
  - How likely is the final outcome, and is it really as bad as claimed?
  - Is the argument just a warning about bad consequences dressed up as an unstoppable chain?
argumentMap:
  premises:
    - "If we let the design team work from home on Fridays, the other teams will ask for the same."
    - "Once every team has Fridays at home, people will start asking for Mondays too, and soon nobody will come in at all."
    - "An empty office would destroy our collaboration and culture."
  conclusion: "So we must not let the design team work from home on Fridays."
  verdict: fallacious
  scheme: ct:argument-from-consequences
  objections:
    - "No evidence is offered that each step makes the next one likely; requests for Fridays at home do not force management to grant Mondays."
    - "Management keeps control at every step: a written policy capping remote days is a bright line that stops the slide."
    - "The feared end state is assumed to be catastrophic without asking how other firms with hybrid schedules have fared."
sameAs: []
sources:
  - id: s1
    title: "The Basic Slippery Slope Argument"
    publisher: "Informal Logic 35(3), 273-311 (Walton, 2015); CRRAR, University of Windsor"
    url: https://scholar.uwindsor.ca/crrarpub/29
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s2
    title: "The psychological mechanism of the slippery slope argument"
    publisher: "Journal of Memory and Language 64(2), 133-152 (Corner, Hahn & Oaksford, 2011); ORCA, Cardiff University"
    url: https://orca.cardiff.ac.uk/id/eprint/30687/
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "Slippery slope arguments imply opposition to change"
    publisher: "Memory & Cognition 44(5), 819-836 (Haigh, Wood & Stewart, 2016); Northumbria Research Link"
    url: https://nrl.northumbria.ac.uk/id/eprint/26101
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "2.6: Slippery Slope Arguments"
    publisher: "Decoding Deception (Daly & Jarrette, University of Arizona), Humanities LibreTexts"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Decoding_Deception_(Daly_and_Jarrette)/02%3A_Common_Fallacies_(and_How_to_Find_Them)/2.06%3A_Slippery_Slope_Arguments
    type: textbook
    accessed: 2026-11-09
created: 2026-11-09
---

# Slippery slope

A slippery slope argument objects to a proposed action by claiming that it is the first step in a sequence that will end somewhere unacceptable, so the first step should not be taken.[^s1] Textbooks summarise the pattern as "if we take step A, we will inevitably slide into Z", and call it a fallacy when the slide is asserted without evidence or reasoning for the links in between.[^s4] Argumentation theorists stress that the same form can also be a reasonable warning, so the real task is telling a supported chain from an imagined one.[^s1]

## Origin

In Douglas Walton's account, the earliest informal-logic author to single out the pattern was Alfred Sidgwick, who in 1910 called it the "thin edge of the wedge" objection.[^s1] Monroe Beardsley's 1966 textbook helped make it a standard entry in lists of informal fallacies, though by 1975 he conceded that such arguments can sometimes be good.[^s1] Later work, including Trudy Govier's in 1982 and Walton's 1992 book, sorted slippery slopes into causal, precedent, linguistic (vagueness-driven) and mixed types.[^s1] Because that taxonomy lacked a single defining structure, Walton proposed a basic argumentation scheme for all of them in 2015.[^s1]

## How it works

Walton's basic scheme has six premises: an agent is considering an action; the action would lead through a sequence of further actions to an outcome; the sequence passes through a gray zone with no sharp boundaries; the agent can stop until some unclear point in that zone; past that point control is lost; and the final outcome should be avoided. The conclusion is that the first step should not be taken.[^s1] The gray zone plus the loss of control is what makes the slope slippery; a mere chain of consequences is not enough.[^s1] Drivers such as precedent, growing public acceptance or a vague term can support particular links.[^s1]

The workplace argument mapped above shows a weak version. A manager rejects a remote-Friday request for one team by forecasting a cascade that ends in an empty office. Each link is asserted, not shown, and management plainly keeps the power to stop at any step, so the loss-of-control premise is missing.[^s1][^s4] Walton calls arguments like this compressed: they state only the first step and the disaster, leaving the sequence and the point of no return for the listener to supply, and he judges them weak until those gaps are filled.[^s1] By contrast, he treats a parent's warning against trying heroin, which spells out gratification, tolerance, withdrawal and loss of control, as fairly reasonable, because every part of the scheme is present and supported, even though the slide is not inevitable for everyone.[^s1]

## How to spot it

Listen for inevitability language such as "before you know it" or "where do we draw the line?", followed by an outcome many steps removed from the proposal.[^s4] Check whether the intermediate steps are named at all; a supported chain backs each step with evidence and shows that each one is probable, not just possible.[^s4] People also read these arguments as revealing the speaker's attitude: in four experiments reported in 2016, readers took a slippery slope claim to signal opposition to the proposal, and how strongly they drew that inference depended on how undesirable the predicted outcome seemed.[^s3]

## How to counter it

Ask the critical questions above, starting with the one Walton ranks among the most important: can a bright line be drawn in the gray zone to stop the slide?[^s1] A critic can press that point even without saying exactly where the line should go.[^s1] When an argument leaves out required premises, the burden shifts back to its proponent to supply the missing evidence before the objection carries weight.[^s1] Rebuilding the chain link by link, with evidence for each, turns a vague alarm into something that can be checked, as textbook examples comparing supported and unsupported versions of the same warning show.[^s4]

## Evidence

Whether a slippery slope is persuasive is partly an empirical question. Building on Hahn and Oaksford's Bayesian decision-theoretic treatment, Corner, Hahn and Oaksford reported in 2011 that the probability of the feared outcome strongly affected how strong participants judged an argument to be.[^s2] Their experiments also linked argument strength to categorisation: arguments seemed stronger when similar items were grouped in the same category, and confidence in category judgements predicted perceived strength.[^s2] The authors concluded that much of the argument's force follows rational cognitive principles rather than simple error.[^s2] Haigh, Wood and Stewart's 2016 studies, including an eye-tracking experiment, found that readers treat these arguments as negative-consequence arguments and find them more persuasive when the speaker's known views fit that reading.[^s3] These are laboratory studies with constructed arguments, and no large multi-lab replication has been reported in the sources reviewed here; the normative status of the fallacy does not rest on them.[^s2][^s3]

## Connections

Walton holds that every slippery slope argument is a special case of **argument from negative consequences**, so it is an instance of that pattern; the fallacious version claims a cascade of consequences it does not support.[^s1] The Bayesian account of Corner, Hahn and Oaksford **explains** argument strength in terms of outcome probability and category boundaries, linking the topic to **Bayesian reasoning**.[^s2] The pattern is a long-standing case study in **argumentation theory** and its catalogue of **argumentation schemes**, where its gray zone ties it to **vagueness** and the **sorites paradox**, and its shifting of proof ties it to the **burden of proof**.[^s1] Like **post hoc ergo propter hoc**, it can rest on unsupported causal claims, and like the **false dilemma**, it narrows the listener's attention to a single feared future.[^s4]

## Sources

[^s1]: Walton, "The Basic Slippery Slope Argument", Informal Logic 35(3), 273-311 (2015). https://scholar.uwindsor.ca/crrarpub/29 (accessed 2026-11-09)
[^s2]: Corner, Hahn & Oaksford, "The psychological mechanism of the slippery slope argument", Journal of Memory and Language 64(2), 133-152 (2011). https://orca.cardiff.ac.uk/id/eprint/30687/ (accessed 2026-11-09)
[^s3]: Haigh, Wood & Stewart, "Slippery slope arguments imply opposition to change", Memory & Cognition 44(5), 819-836 (2016). https://nrl.northumbria.ac.uk/id/eprint/26101 (accessed 2026-11-09)
[^s4]: Daly & Jarrette, "2.6: Slippery Slope Arguments", Decoding Deception, Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Decoding_Deception_(Daly_and_Jarrette)/02%3A_Common_Fallacies_(and_How_to_Find_Them)/2.06%3A_Slippery_Slope_Arguments (accessed 2026-11-09)
