# Article schema

Each article is one **node**: `articles/<domain>/<slug>.md`, where the filename equals the id's slug and `<domain>` is a key in `topics/seeds.yaml`. Scaffold one with `python3 scripts/kg.py new <domain> <slug> <Type>`, which pre-fills the fields and sections its class needs.

```markdown
---
id: ct:affirming-the-consequent          # ct: + lowercase-hyphen slug; never changes
type: FormalFallacy                      # most specific class from ontology/ontology.ttl
title: Affirming the consequent
aliases: [converse error, fallacy of the converse]
domain: formal-fallacies                 # key in topics/seeds.yaml (becomes a SKOS ConceptScheme)
summary: >-                              # 1–2 sentence definition (skos:definition)
  The invalid inference from "if P then Q" and "Q" to "P".
level: introductory                      # introductory | intermediate | advanced
evidenceStatus: normative                # see table below
broader: [ct:formal-fallacy]             # skos:broader, 1–3; must stay acyclic
related: [ct:denying-the-antecedent]     # skos:related (symmetric)
requires: [ct:modus-ponens]              # learning prerequisites (transitive, acyclic) -> graph/learning-path.md
relations:                               # typed edges: EVERY one cites a source id below
  - {predicate: invalidFormOf, object: ct:modus-ponens, source: s1, confidence: high}
  - {predicate: confusedWith,  object: ct:modus-ponens, source: s2}          # confidence defaults to medium
criticalQuestions:                       # Fallacy >= 2, ArgumentScheme >= 3; each ends with "?"
  - Is the conditional the only way the consequent could come about?
  - Could the consequent be true while the antecedent is false?
argumentMap:                             # required for Fallacy, ReasoningForm, ArgumentScheme
  premises: ["If it rained, the street is wet.", "The street is wet."]
  conclusion: "It rained."
  verdict: invalid                       # valid | invalid | strong | weak | fallacious
  scheme: ct:modus-ponens                # optional: the scheme/form this inference claims to instantiate
  objections: ["A street cleaner could have wet the street."]   # optional: become AIF CA-nodes
sameAs: [wd:Q1063413]                    # optional entity links: Wikidata QIDs or https IRIs (incl. sibling graphs) -> skos:exactMatch
sources:                                 # >= 3; >= 2 strong; >= 1 scholarly
  - id: s1
    title: "Fallacies"
    publisher: Stanford Encyclopedia of Philosophy (Hansen, 2023)
    url: https://plato.stanford.edu/entries/fallacies/
    type: scholarly-encyclopedia
    accessed: 2026-11-02
created: 2026-11-02
modified: 2026-11-09                     # optional; set when an article is revised
---

# Affirming the consequent

Prose with footnote citations after each claim.[^s1]

## Origin
## How it works            (a worked example; reference the argument map)
## How to spot it          (Fallacy, CognitiveBias, Heuristic)
## How to counter it       (Fallacy, CognitiveBias, Heuristic)
## How to apply it         (Technique, Method: steps, when to use, pitfalls)
## Evidence                (CognitiveBias, Heuristic, Phenomenon: key studies, effect sizes, replications)
## Connections             (always: explain each edge in prose, with citations)
## Sources                 (always)
[^s1]: Hansen, "Fallacies", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/fallacies/ (accessed 2026-11-02)
```

Headings in **bold intent** above are enforced by class; `## Origin` and `## How it works` are expected for every article.

## Classes (`type`)

| Class | Use for |
|---|---|
| `Concept` | general reasoning ideas: argument, validity, soundness, burden of proof |
| `ReasoningMode` | deductive, inductive, abductive, analogical, Bayesian reasoning |
| `ReasoningForm` | valid/cogent inference patterns: modus ponens, disjunctive syllogism, IBE |
| `ArgumentScheme` | Walton-style presumptive schemes: argument from expert opinion, from analogy |
| `FormalFallacy` / `InformalFallacy` / `ProbabilisticFallacy` | the three fallacy families |
| `CognitiveBias` | systematic judgment errors: confirmation bias, anchoring |
| `Heuristic` | mental shortcuts: availability, representativeness, recognition |
| `Technique` | practical remedies: premortem, consider-the-opposite, lateral reading, ACH |
| `Framework` | models: Toulmin, Paul-Elder, dual-process theory, Bloom's taxonomy |
| `Principle` | norms: Occam's razor, principle of charity |
| `Method` | formal inquiry methods: RCTs, hypothesis testing, Socratic method, Delphi |
| `Disposition` | intellectual virtues: intellectual humility, actively open-minded thinking |
| `Phenomenon` | observed patterns: replication crisis, misinformation, regression to the mean |
| `Field` | disciplines: logic, epistemology, argumentation theory, JDM |
| `Person`, `Organization`, `Work`, `Study`, `Event` | thinkers, institutions, landmark books, landmark experiments, milestones |

Disjointness is declared (a node cannot be both a `Fallacy` and a `ReasoningForm`, both a `CognitiveBias` and a `Technique`, or both a `Concept` and a `Person`). The reasoner uses edge ranges to infer the type of unwritten nodes; two edges that imply incompatible types fail the build.

## Predicates (`relations[].predicate`)

| Predicate | Meaning | Constraint | Inferred inverse |
|---|---|---|---|
| `partOf` | component of | transitive | `hasPart` |
| `requires`* | prerequisite to understand | transitive, acyclic | `prerequisiteOf` |
| `instanceOf` | variant/instance of | | `hasInstance` |
| `invalidFormOf` | invalid look-alike of a valid form | FormalFallacy → ReasoningForm | `hasInvalidCounterpart` |
| `misusesScheme` | fallacious misuse of a scheme | Fallacy → ArgumentScheme | `misusedAs` |
| `formalizedBy` | given formal treatment by | | `formalizes` |
| `contrastsWith`, `confusedWith` | contrast / common confusion | symmetric | itself |
| `explainedBy` | mechanism or theory behind | | `explains` |
| `produces` | heuristic that can produce a bias | Heuristic → CognitiveBias | `producedBy` |
| `exploits` | rhetoric/fallacy that exploits a bias | → CognitiveBias | `exploitedBy` |
| `amplifies` | makes worse | | `amplifiedBy` |
| `counteracts`, `detects` | remedy for a failure mode | Technique/Principle/Method/Disposition/Framework → CognitiveBias/Fallacy/Heuristic/Phenomenon | `counteractedBy`, `detectedBy` |
| `appliedIn` | used in a field or setting | | |
| `demonstratedBy` | shown by a landmark study | → Study | `demonstrates` |
| `supportedBy`, `challengedBy` | evidence for / critique or failed replication | | `supports`, `challenges` |
| `introducedBy` | named/introduced by | → Person | `introduced` |
| `introducedIn` | introduced in | → Work | `introduces` |
| `authoredBy` | author of a work | Work → Person | `authored` |
| `influencedBy` | intellectual influence | | `influenced` |
| `studiedIn` | studied in a discipline | → Field | |

\* `requires` is written as its own list, not under `relations`. Never write the inverse yourself; the reasoner materialises it in `graph/inferred.nt`. If you need a new predicate, add it to `ontology/ontology.ttl` with a label, any domain/range, and its inverse/characteristics in the same commit.

## Evidence status

| value | meaning | rule |
|---|---|---|
| `normative` | a standard of good reasoning (logic, principles, fallacy definitions) | not allowed for `CognitiveBias` |
| `robust` | empirical finding that has replicated well | needs a peer-reviewed or primary study |
| `mixed` | real but smaller, moderated or context-dependent effects | needs a peer-reviewed or primary study |
| `contested` | active scholarly dispute | + a `challengedBy` relation |
| `failed-replication` | large replications failed to reproduce the original effect | + a `challengedBy` relation |
| `historical` | mainly of historical interest (people, works, events) | |

## Source types

| type | strong | scholarly | examples |
|---|---|---|---|
| `peer-reviewed` | yes | yes | *Psychological Review*, *Science*, *Cognition*, *Argumentation*, *Informal Logic*, *Judgment and Decision Making* (DOI page) |
| `primary` | yes | yes | the original study or book that introduced the idea (publisher page, author's copy) |
| `scholarly-encyclopedia` | yes | yes | Stanford Encyclopedia of Philosophy, Internet Encyclopedia of Philosophy |
| `textbook` | yes | yes | academic logic, argumentation and JDM textbooks |
| `academic` | yes | yes | university course pages, research centres, university library guides |
| `government` | yes | yes | CIA *Tradecraft Primer*, ODNI analytic standards (ICD 203), GAO, NIH |
| `intergovernmental` | yes | yes | OECD (PISA creative/critical thinking), UNESCO |
| `institutional` | yes | no | Foundation for Critical Thinking, APA, Cochrane, professional bodies |
| `encyclopedia` | yes | no | Britannica |
| `preprint`, `news`, `community` | no | no | context only, never the sole support for a claim |

**Banned:** Wikipedia (and mirrors), RationalWiki, Fandom, Quora, AI-generated pages, fallacy-poster sites, content farms and SEO listicles.

## Enforcement summary (`scripts/kg.py check`)

1. **Structure:** required fields, enums, id/filename/folder agreement, known domain, dates.
2. **Citations:** ≥ 3 sources, ≥ 2 strong, ≥ 1 scholarly, empirical claims backed by a study, https only, no banned or duplicate URLs, every source cited, every substantive paragraph cited, every typed edge cites a source.
3. **Class rules:** required sections, critical questions, argument maps, fallacy verdicts, bias evidence status, `challengedBy` for disputed claims.
4. **Graph rules:** ≥ 3 edges and ≥ 1 typed relation per node, domain/range on written targets, no cycles in `broader` / `requires` / `partOf`.
5. **Uniqueness:** no shared ids, titles or aliases; no near-identical titles; no copied text (5-gram shingles); no same-topic rewrite (TF-IDF cosine ≥ 0.80; ≥ 0.60 warns).
6. **Reasoning:** OWL 2 RL closure; any node inferred into two disjoint classes fails.
7. **SHACL:** `ontology/shapes.ttl` over the exported RDF with RDFS inference.
