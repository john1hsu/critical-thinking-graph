---
id: ct:abstract-argumentation-frameworks
type: Framework
title: Abstract argumentation frameworks
aliases: [Dung argumentation framework, Dung's abstract argumentation, argumentation framework (AF)]
domain: argumentation
summary: >-
  A formal model, introduced by Phan Minh Dung in 1995, that treats arguments as bare
  nodes connected by an attack relation and defines which sets of arguments can be
  rationally accepted together (grounded, preferred, stable and complete semantics).
level: intermediate
evidenceStatus: normative
broader: [ct:argumentation-theory]
related: [ct:defeasible-reasoning, ct:artificial-intelligence, ct:legal-reasoning, ct:dialectic, ct:argument-mapping, ct:convergent-argument]
requires: [ct:argument]
relations:
  - {predicate: introducedBy, object: ct:phan-minh-dung, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:on-the-acceptability-of-arguments, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:artificial-intelligence, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:aspic-plus, source: s2, confidence: high}
  - {predicate: challengedBy, object: ct:polberg-hunter-2017-empirical-evaluation-of-abstract-argumentation, source: s3, confidence: medium}
sources:
  - id: s1
    title: "On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games"
    publisher: Artificial Intelligence 77, 321-357 (Dung, 1995)
    url: https://cse-robotics.engr.tamu.edu/dshell/cs631/papers/dung95acceptability.pdf
    type: primary
    accessed: 2026-11-27
  - id: s2
    title: "Argument (chapter 2 of Introduction to Formal Philosophy)"
    publisher: Springer Undergraduate Texts in Philosophy (Prakken, 2018), Utrecht University repository
    url: https://dspace.library.uu.nl/bitstream/handle/1874/388302/978-3-319-77434-3_2_1_.pdf?sequence=2
    type: textbook
    accessed: 2026-11-27
  - id: s3
    title: "Empirical Evaluation of Abstract Argumentation: Supporting the Need for Bipolar and Probabilistic Approaches"
    publisher: arXiv (Polberg and Hunter, University College London, 2017)
    url: https://arxiv.org/pdf/1707.09324
    type: preprint
    accessed: 2026-11-27
created: 2026-11-27
---

# Abstract argumentation frameworks

An abstract argumentation framework (AF) is a deliberately minimal model of a debate: a set of arguments plus a binary "attacks" relation between them, with nothing said about what the arguments contain.[^s1] The interesting work is done by *semantics* — rules that pick out which sets of arguments a rational evaluator could accept together, given who attacks whom.[^s1][^s2] Because it ignores internal structure, one framework can sit underneath many different logics, which is why it became a common foundation for argumentation in artificial intelligence.[^s1][^s2]

## Origin

The framework was introduced by the computer scientist Phan Minh Dung, then at the Asian Institute of Technology in Bangkok, in a 1995 paper in the journal *Artificial Intelligence*.[^s1] Dung's claim was that the acceptability of arguments is the common core of several apparently unrelated formalisms: he showed that default logic, Pollock-style defeasible reasoning and logic-programming semantics can be recast as argumentation frameworks, and that the von Neumann–Morgenstern solutions of n-person cooperative games are exactly the stable extensions of a framework built from a domination relation.[^s1] Dung himself noted that the "correctness" of the semantics cannot be proved formally and rests on how well they handle examples.[^s1]

## How it works

The core definitions build on one another:[^s1][^s3]

- A set of arguments is **conflict-free** if none of its members attacks another.[^s1]
- An argument is **acceptable** with respect to a set if the set attacks every attacker of that argument — the set *defends* it.[^s1]
- A set is **admissible** if it is conflict-free and defends all its members.[^s1]
- A **preferred** extension is a maximal admissible set; every framework has at least one.[^s1]
- A **stable** extension is conflict-free and attacks every argument outside it; every stable extension is preferred, but some frameworks have none.[^s1]
- A **complete** extension is admissible and contains every argument it defends; the **grounded** extension is the smallest complete one, the sceptical core everyone must accept.[^s1]

Prakken presents the same ideas as labellings: an argument is "in" when all its attackers are "out", and "out" when some "in" argument attacks it; grounded semantics minimises what is "in", preferred maximises it, and stable leaves nothing undecided.[^s2]

**Workplace example.** A team debates a product launch date. A: "Launch in March — the feature is code-complete." B: "Don't launch in March — the security audit isn't finished." C: "The audit finishes in February, so it won't block March." Here B attacks A and C attacks B. C is unattacked, so it is in every extension; C defends A against B; the grounded extension is {A, C} and A is justified. Now drop C and suppose A and B simply attack each other (a disagreement over whether code-complete is enough). There are then two preferred extensions, {A} and {B}, and the grounded extension is empty — the framework reports a genuine stalemate rather than inventing a winner, the pattern Dung illustrated with his "Nixon diamond" example.[^s1][^s2]

## How to apply it

1. List the competing claims as separate arguments, one node each.[^s2]
2. Draw an attack arrow wherever accepting one argument would defeat another (a rebuttal, an undercut of its inference, or an objection to a premise).[^s2]
3. Compute the grounded extension first: accept unattacked arguments, reject what they attack, repeat. What survives is safe to rely on.[^s1][^s3]
4. If the grounded extension leaves things undecided, look at the preferred extensions to see the coherent positions available, and identify which information would break the tie.[^s2]

Pitfall: the output is only as good as the attack graph. Deciding *whether* one argument really defeats another — and how strongly — happens outside the framework.[^s2]

## Evidence and limitations

Abstract frameworks are a normative, mathematical standard, but they have known limits. Prakken stresses that Dung's formalism only answers how to evaluate arguments once attacks are given, not how arguments are built or attacked; structured approaches such as ASPIC+ were developed to supply that missing layer.[^s2] Polberg and Hunter ran a study with lay participants judging dialogues and reported that people use more graded levels of agreement than the two- or three-valued statuses of Dung's semantics, often read support relations into exchanges, and do not always interpret attacks as the modeller intends; they argue this calls for bipolar (support-and-attack) and probabilistic extensions.[^s3] Their study is a preprint and its findings are best treated as suggestive.[^s3]

## Connections

The framework sits within **argumentation theory** as its most abstract formal layer and requires the basic notion of an **argument**.[^s2] It was **introduced by Phan Minh Dung** in his 1995 paper on the acceptability of arguments, written for and **applied in artificial intelligence**, where it unified nonmonotonic logics and links closely to **defeasible reasoning**.[^s1] It **contrasts with ASPIC+**, a structured framework that specifies how arguments are constructed from rules and premises and then hands the resulting attack graph to Dung-style semantics.[^s2] Its adequacy as a model of how people actually weigh arguments is **challenged by** Polberg and Hunter's empirical evaluation.[^s3] Legal reasoning and argument mapping are natural neighbours: both draw graphs of claims and objections, and Prakken notes how standards of proof differ by legal context.[^s2]

## Sources

[^s1]: Dung, P. M. (1995). "On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games." *Artificial Intelligence* 77, 321-357. https://cse-robotics.engr.tamu.edu/dshell/cs631/papers/dung95acceptability.pdf (accessed 2026-11-27)
[^s2]: Prakken, H. (2018). "Argument." In S. O. Hansson & V. F. Hendricks (eds.), *Introduction to Formal Philosophy*, Springer. https://dspace.library.uu.nl/bitstream/handle/1874/388302/978-3-319-77434-3_2_1_.pdf?sequence=2 (accessed 2026-11-27)
[^s3]: Polberg, S. & Hunter, A. (2017). "Empirical Evaluation of Abstract Argumentation: Supporting the Need for Bipolar and Probabilistic Approaches." arXiv. https://arxiv.org/pdf/1707.09324 (accessed 2026-11-27)
