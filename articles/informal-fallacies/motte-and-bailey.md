---
id: ct:motte-and-bailey
type: InformalFallacy
title: Motte-and-bailey
aliases: [motte-and-bailey fallacy, motte-and-bailey doctrine, motte and bailey]
domain: informal-fallacies
summary: >-
  The tactic of advancing a bold, hard-to-defend claim (the bailey) and, when
  challenged, retreating to a modest, easily defended claim that sounds similar
  (the motte), then returning to the bold claim once the pressure has passed.
level: intermediate
evidenceStatus: normative
broader: [ct:informal-fallacy]
related: [ct:equivocation, ct:straw-man-fallacy, ct:ambiguity, ct:vagueness, ct:precising-definition, ct:principle-of-charity, ct:burden-of-proof, ct:ad-hoc-hypothesis, ct:falsifiability]
requires: [ct:argument, ct:ambiguity]
relations:
  - {predicate: introducedBy, object: ct:nicholas-shackel, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:the-vacuity-of-postmodernist-methodology, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:equivocation, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:ambiguity, source: s1, confidence: medium}
  - {predicate: instanceOf, object: ct:strategic-ambiguity, source: s3, confidence: medium}
criticalQuestions:
  - What exactly is the claim being defended right now, and is it the same claim that was asserted at the start?
  - If the modest version is granted, does the bold version actually follow from it?
  - Once the critic falls silent, does the speaker go back to drawing conclusions that only the bold version supports?
  - Is the speaker really shifting position, or did they hold the modest reading all along, so that calling it a retreat would be uncharitable?
  - Can both versions be stated precisely enough, side by side, that everyone can see which one is in play?
argumentMap:
  premises:
    - "Bailey (stated in the planning meeting): The new dashboard proves the onboarding redesign doubled customer retention, so we should roll it out to every region now."
    - "Motte (stated when a colleague asks for the analysis): All I am saying is that the dashboard shows retention went up after the redesign."
    - "Nobody disputes that retention went up after the redesign."
  conclusion: "So the full regional rollout is justified."
  verdict: fallacious
  objections:
    - "Retention rising after the redesign does not show that the redesign caused the rise, still less that it doubled retention."
    - "Conceding the motte leaves the bailey undefended; the rollout needed the bold causal claim, which was never argued for."
sameAs: []
sources:
  - id: s1
    title: "The Vacuity of Postmodernist Methodology"
    publisher: Metaphilosophy 36(3), 295-320 (Shackel, 2005), author's archived copy via PhilArchive
    url: https://philarchive.org/archive/SHATVO-2
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Motte and Bailey Doctrines"
    publisher: Practical Ethics blog, Oxford Uehiro Centre for Practical Ethics, University of Oxford (Shackel, 2014, updated 2015)
    url: https://blog.practicalethics.ox.ac.uk/?p=9229
    type: academic
    accessed: 2026-11-15
  - id: s3
    title: "Strategic Ambiguity in the Social Sciences"
    publisher: Social Psychological Bulletin 18, e9923 (Frankenhuis, Panchanathan & Smaldino, 2023)
    url: https://spb.psychopen.eu/index.php/spb/article/download/9923/9923.html?inline=1
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Motte-and-bailey

A motte-and-bailey is a two-level position whose holder asserts a bold, attractive but hard-to-defend claim, the bailey, and, when someone challenges it, falls back to a dull but easily defended claim, the motte, that sounds much the same.[^s1] Once the critic gives up, the bold claim is quietly reasserted. Frankenhuis, Panchanathan and Smaldino summarise the effect: the bold claim is never defended, yet never refuted either, and the speaker can paint the critic as unreasonable for attacking something so obviously true.[^s3]

## Origin

The philosopher Nicholas Shackel introduced the term in "The Vacuity of Postmodernist Methodology", published in *Metaphilosophy* in 2005.[^s1] He took it from a medieval castle design: a stone tower on a raised mound (the motte) overlooking enclosed farmland (the bailey), with a ditch around both. Nobody wants to live in the tower; its only purpose is to protect the productive land. Under light raids the ditch is enough, but under heavy attack the defenders abandon the bailey, shelter in the motte until the attackers leave, and then reoccupy the fields.[^s1] Shackel used the image to diagnose doctrines that, he argued, survive only by alternating between an exciting claim and a trivial one. His simplest case is the "troll's truism": a mildly ambiguous sentence that smuggles an exciting falsehood in on the back of a trivial truth.[^s1] In a 2014 post on the Oxford Uehiro Centre's Practical Ethics blog he gave the example "morality is socially constructed", which sounds radical but is trivially true if morality just means people's beliefs about right and wrong, and he noted that the term had spread into discussion of ethical, political and religious positions, including posts on the Slate Star Codex blog.[^s2]

## How it works

The worked example above is set in a workplace. In a planning meeting a manager claims the new dashboard proves an onboarding redesign doubled retention and that the redesign should go to every region. When a colleague asks to see the analysis, the manager retreats: all they meant was that retention rose after the redesign. That modest claim is true and nobody disputes it, so the colleague drops the point, and the meeting goes ahead and approves the rollout, a decision that only the bold causal claim could justify. The structure matches Shackel's account: the bold claim holds the valuable conclusions, the modest one exists only to survive scrutiny, and the position depends on moving between them.[^s1]

Shackel insists that, strictly, a motte-and-bailey doctrine is neither a fallacy nor an equivocation, because a doctrine is a set of claims rather than an inference.[^s2] It nevertheless enables fallacious moves, chiefly reasoning "motte, therefore bailey" and the cycle of advancing the bailey, retreating under criticism and returning later.[^s2] The motte and bailey need not even come from one person: one member of a group may voice the bold claim while another defends the modest one, so the pattern can be criticised even when no individual argument is invalid.[^s2]

## How to spot it

Look for a claim that seems to change size depending on how hard it is pushed. Shackel's signal is ambiguity in a key term, an "equivocal fulcrum" such as "truth", "knowledge" or "constructed", that lets the speaker use the strong sense when unchallenged and plead the weak sense when challenged.[^s1] Frankenhuis and colleagues describe close relatives in research: "theory stretching", where an author answers counter-evidence by saying the theory can be stretched to cover it, and quiet narrowing of a claim after the broader version fails.[^s3] Another warning sign is a critic being accused of attacking an absurd position nobody holds, immediately after that position was used to reach a conclusion.[^s2]

## How to counter it

Write both versions down and ask which one is being defended.[^s1] If the answer is the motte, grant it explicitly, then point out that it does not support the conclusions drawn from the bailey and ask for those conclusions to be withdrawn or argued for separately. Frankenhuis and colleagues recommend making terms, scope and assumptions explicit, and favouring preregistration and formal models so that what counts as support is fixed in advance.[^s3] Apply charity too: some speakers genuinely meant the modest claim all along, and Shackel notes that the diagnosis targets a doctrine whose survival depends on the alternation, not every clarification of an overstated remark.[^s1]

## Connections

Shackel introduced the concept in his 2005 *Metaphilosophy* paper, which is why the node links to him and to that work.[^s1] He explains the manoeuvre through ambiguity: equivocal key terms supply the cover for moving between the two claims.[^s1] He also contrasts it with equivocation, which shifts a word's meaning within an argument, whereas the motte-and-bailey is a doctrine that alternates between two claims across a whole exchange.[^s2] Frankenhuis, Panchanathan and Smaldino treat it as an instance of strategic ambiguity, the wider practice of keeping a claim vague enough to escape refutation.[^s3] Its relatives in the graph include the straw man, which the motte-holder often accuses critics of committing,[^s2] and ad hoc rescues of failing hypotheses, which the theory-stretching cases resemble.[^s3]

## Sources

[^s1]: Shackel, "The Vacuity of Postmodernist Methodology", Metaphilosophy 36(3), 295-320 (2005). https://philarchive.org/archive/SHATVO-2 (accessed 2026-11-15)
[^s2]: Shackel, "Motte and Bailey Doctrines", Practical Ethics blog, Oxford Uehiro Centre for Practical Ethics (2014, updated 2015). https://blog.practicalethics.ox.ac.uk/?p=9229 (accessed 2026-11-15)
[^s3]: Frankenhuis, Panchanathan & Smaldino, "Strategic Ambiguity in the Social Sciences", Social Psychological Bulletin 18, e9923 (2023). https://spb.psychopen.eu/index.php/spb/article/download/9923/9923.html?inline=1 (accessed 2026-11-15)
