---
id: ct:value-based-practical-reasoning
type: ArgumentScheme
title: Value-based practical reasoning
aliases: [VBPR, practical reasoning from values, AS1 practical reasoning scheme, Atkinson-Bench-Capon practical reasoning scheme]
domain: argumentation
summary: >-
  An argumentation scheme for deciding what to do: in the current
  circumstances, an action should be performed because it will bring about new
  circumstances that realise a goal and promote a value. Developed by Katie
  Atkinson, Trevor Bench-Capon and Peter McBurney from Walton's practical
  reasoning scheme, it separates consequences, goals and values so a proposal
  can be challenged on facts, on alternatives, on side effects, or on which
  values matter most.
level: intermediate
evidenceStatus: normative
broader: [ct:argumentation-schemes]
related: [ct:argument-from-consequences, ct:conductive-argument, ct:value-focused-thinking, ct:legal-reasoning, ct:defeasible-reasoning, ct:the-new-rhetoric]
requires: [ct:argumentation-schemes]
relations:
  - {predicate: introducedBy, object: ct:katie-atkinson, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:douglas-walton, source: s1, confidence: high}
  - {predicate: formalizedBy, object: ct:value-based-argumentation-frameworks, source: s1, confidence: medium}
  - {predicate: contrastsWith, object: ct:instrumental-practical-reasoning, source: s3, confidence: high}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s3, confidence: high}
criticalQuestions:
  - Are the circumstances really as the proposer describes them?
  - Will the action actually bring about the promised new circumstances, and do those circumstances realise the goal?
  - Is there another action that would realise the same goal or promote the same value at lower cost?
  - Does the action have side effects that demote this value or some other value the audience cares about?
  - Does the goal really promote the stated value, and is that value one the audience accepts?
  - Is the action possible for this agent at all?
  - Would a different ranking of the competing values lead a reasonable audience to a different decision?
argumentMap:
  premises:
    - "Our team is split across three time zones, and the weekly status meeting falls at 7 a.m. or 9 p.m. for half of us."
    - "Replacing the meeting with a written update thread would let everyone contribute during their own working hours."
    - "Letting everyone contribute in working hours treats all team members fairly."
  conclusion: "We should replace the weekly status meeting with a written update thread."
  verdict: strong
  scheme: ct:value-based-practical-reasoning
  objections:
    - "Rotating the meeting time would also share the burden fairly while keeping live discussion (an alternative that promotes the same value)."
    - "Dropping all live contact may weaken team cohesion, a value some members rank above convenience (a side effect demoting another value)."
sameAs: []
sources:
  - id: s1
    title: "Computational Representation of Practical Argument"
    publisher: "Synthese 152, 157-206 (Katie Atkinson, Trevor Bench-Capon & Peter McBurney, 2006), University of Liverpool author copy"
    url: https://cgi.csc.liv.ac.uk/~katie/synthese06.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "Persuasion in Practical Argument Using Value-based Argumentation Frameworks"
    publisher: "Journal of Logic and Computation 13(3) (Trevor Bench-Capon, 2003), University of Liverpool author copy"
    url: https://cgi.csc.liv.ac.uk/~tbc/publications/jcl03.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "Practical Reasoning Arguments: A Modular Approach"
    publisher: "Argumentation 32(4), 519-547 (Fabrizio Macagno & Douglas Walton, 2018), PhilArchive copy"
    url: https://philarchive.org/archive/MACPRA-13
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# Value-based practical reasoning

Value-based practical reasoning is an argumentation scheme for conclusions about action rather than about fact. Its standard form runs: in the circumstances R, we should perform action A, which will achieve new circumstances S, which will realise goal G, which will promote value V.[^s1] The scheme is presumptive. It gives a reason to act that stands until one of its critical questions is raised and not answered, and it is built so that a proposal can be attacked at each of its links: the facts, the causal claim, the goal, the value, or the choice of action.[^s1][^s3]

## Origin

The scheme was set out by Katie Atkinson, Trevor Bench-Capon and Peter McBurney at the University of Liverpool, most fully in a 2006 *Synthese* paper, building on an earlier proposal by Greenwood and colleagues (2003).[^s1] It extends Douglas Walton's 1996 sufficient-condition scheme for practical reasoning, which had four critical questions. The authors argued that Walton's word "goal" was ambiguous, covering the state an action produces, the feature of that state that is wanted, and the reason it is wanted, so they split it into three separate elements: new circumstances, goal and value.[^s1]

The value element connects the scheme to Bench-Capon's value-based argumentation frameworks (2003). Following Perelman's *New Rhetoric*, Bench-Capon held that practical disputes are often about which values to rank higher, not about logical error, and that an argument can defeat its rival for one audience but not for another.[^s2]

## How it works

Atkinson and colleagues pair the scheme with sixteen critical questions, grouped by what they challenge: whether there are alternative ways to reach the same circumstances, goal or value; whether the action is possible; whether it promotes or blocks other values; whether it has side effects that demote this value or another one; whether the circumstances are true and the action really produces the claimed result; whether the goal promotes the value and the value is legitimate; and whether the goal state is achievable at all.[^s1] They also sort the matching attacks into three kinds of dispute: about what is true, about what is best, and about how the problem is represented.[^s1]

The argument map above shows the scheme in a workplace decision. A team lead proposes replacing a weekly meeting with a written thread, citing the current time-zone spread (circumstances), the expected result (everyone posts in working hours), and the value served (fairness). The proposal is strong, but the two objections show where the critical questions bite. Rotating the meeting time is an alternative that serves the same value, and losing live contact is a side effect that demotes cohesion.[^s1] Which objection wins can depend on how the team ranks fairness against cohesion, the point Bench-Capon's frameworks model: when an argument attacks another backed by a value the audience ranks higher, the attack does not succeed for that audience.[^s2]

## How to apply it

1. State the proposal as the five-part scheme, naming each element explicitly; vague proposals usually hide a missing goal or value.[^s1]
2. Ask the factual questions first (circumstances, effect of the action), then the comparative ones (alternatives, side effects), then the value questions.[^s1]
3. Where people still disagree after the facts are settled, check whether they rank values differently. Bench-Capon shows that such disagreement can be fully rational, and that persuasion works best on arguments every value ranking accepts.[^s2]

## Limitations

Macagno and Walton (2018) credit the scheme with tying values to actions and with listing many ways a proposal can fail, but raise three objections. It leaves unstated whether the inference runs from an action's consequences or from its being the best means to a goal; it leaves the relations between goals, actions and values implicit; and its sixteen questions have no priority order, so an analyst has to check them all.[^s3] They propose instead a modular structure that separates justifying an action, evaluating its consequences, and classifying the situation.[^s3] The scheme was also designed partly for software agents, so its full question set is heavier than most everyday deliberation needs.[^s1]

## Connections

- **Introduced by Katie Atkinson,** with Bench-Capon and McBurney, in the 2006 *Synthese* account.[^s1]
- **Influenced by Douglas Walton,** whose sufficient-condition practical reasoning scheme it extends.[^s1]
- **Formalized by value-based argumentation frameworks,** which the authors use to filter competing practical arguments by audience value rankings.[^s1][^s2]
- **Contrasts with instrumental practical reasoning,** Walton's simpler means-to-goal scheme, which leaves values out.[^s3]
- **Studied in argumentation theory,** where Macagno and Walton compare it with other practical reasoning schemes.[^s3]
- **Related:** argument from consequences is commonly classed under it; conductive arguments weigh pros and cons in a similar way; value-focused thinking makes values explicit in decision analysis; legal reasoning and *The New Rhetoric* supply its examples and its view of audiences.[^s2][^s3]

## Sources

[^s1]: Atkinson, Bench-Capon & McBurney, "Computational Representation of Practical Argument", *Synthese* 152, 2006, 157-206. https://cgi.csc.liv.ac.uk/~katie/synthese06.pdf (accessed 2026-11-17)
[^s2]: Bench-Capon, "Persuasion in Practical Argument Using Value-based Argumentation Frameworks", *Journal of Logic and Computation* 13(3), 2003. https://cgi.csc.liv.ac.uk/~tbc/publications/jcl03.pdf (accessed 2026-11-17)
[^s3]: Macagno & Walton, "Practical Reasoning Arguments: A Modular Approach", *Argumentation* 32(4), 2018, 519-547. https://philarchive.org/archive/MACPRA-13 (accessed 2026-11-17)
