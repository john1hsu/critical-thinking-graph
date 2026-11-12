# Critical Thinking Graph

A growing, citation-backed knowledge graph of critical thinking: logic and reasoning forms, argumentation schemes, formal, informal and probabilistic fallacies, cognitive biases and heuristics, scientific reasoning, evidence and information literacy, structured analytic techniques, debiasing and metacognition, and the thinkers and works behind them. A scheduled run researches one new topic, writes it as a node with evidenced, typed edges, and only commits it if the validator, the OWL reasoner and the SHACL shapes all agree it is sound.

**Read it online: https://john1hsu.github.io/critical-thinking-graph/** (rebuilt automatically on every new article by `.github/workflows/pages.yml` from `site/build.py`).

## Architecture

```
articles/<domain>/<slug>.md          Markdown + YAML frontmatter (one node each)
        │  scripts/kg.py
        ▼
 1. structural validation      citations, uniqueness (shingles + TF-IDF), class-specific rules, acyclicity
 2. RDF assembly               SKOS + PROV-O + schema.org + AIF argument maps, one named graph per article
 3. OWL 2 RL reasoning         inverse / symmetric / transitive properties, domain & range typing
 4. consistency checking       disjoint-class contradictions, domain/range violations
 5. SHACL validation           ontology/shapes.ttl (semantic contract on the exported RDF)
 6. exports + analytics        graph/  (regenerated on every commit; CI fails if stale)
```

| Layer | What | Where |
|---|---|---|
| Ontology | OWL 2 RL classes (ReasoningForm, ArgumentScheme, Formal/Informal/ProbabilisticFallacy, CognitiveBias, Heuristic, Technique, Framework, Principle, Disposition, Study, …) and typed relations with inverses, symmetry, transitivity, domains, ranges and disjointness; aligned with SKOS, PROV-O, schema.org and the Argument Interchange Format (AIF) | `ontology/ontology.ttl` |
| Shapes | SHACL constraints: every node defined, sourced, levelled and evidence-rated; fallacies carry critical questions and a worked example; schemes carry ≥ 3 critical questions | `ontology/shapes.ttl` |
| Nodes | One Markdown article per entity with frontmatter holding id, class, hierarchy, prerequisites, evidenced typed edges, critical questions, an argument map, evidence status, entity links and sources | `articles/<domain>/` |
| Linked data | N-Triples (asserted), N-Triples (inferred by OWL-RL), TriG with per-article named graphs and provenance, Turtle-star edge evidence (RDF 1.2), JSON-LD, JSON index | `graph/triples.nt`, `graph/inferred.nt`, `graph/graph.trig`, `graph/edge-evidence.ttls`, `graph/graph.jsonld`, `graph/index.json` |
| Analytics | PageRank, betweenness, Louvain communities, k-core, coverage by type/domain/level/evidence | `graph/stats.md` |
| Frontier | Unwritten nodes ranked by referrer count weighted by referrer centrality, with the **type the reasoner expects** them to have | `graph/frontier.md` |
| Link prediction | Adamic-Adar scores for written nodes that should probably be connected | `graph/suggested-links.md` |
| Competency questions | SPARQL over asserted + inferred triples; *gap* queries (unremedied biases, unattributed concepts, orphans, unlinked formal fallacies) drive gap-filling runs | `queries/*.rq` → `graph/competency.md` |
| Learning path | Topological layers of the `requires` prerequisite DAG | `graph/learning-path.md` |
| Argument maps | AIF I-/RA-/CA-nodes in RDF, rendered as Mermaid diagrams | `graph/argument-maps.md` |

## What makes it more than a link list

- **Every typed edge is evidenced.** Each relation cites the source that supports it and carries a confidence; the evidence is published as RDF-star annotations on the edge itself.
- **Reasoning, not just storage.** Writers state one direction (`consider-the-opposite counteracts confirmation-bias`); the OWL-RL reasoner materialises `counteractedBy`, symmetric `confusedWith`, transitive `requires`/`partOf`/`broaderTransitive`, and types unwritten nodes from property ranges. If two articles imply a node is both a `Person` and a `Work`, the build fails.
- **Domain-aware epistemics.** Every node has an `evidenceStatus` (normative, robust, mixed, contested, failed-replication, historical). Empirical claims need a study; disputed ones need a `challengedBy` edge. Biases cannot be marked normative.
- **Argumentation structure.** Fallacies, reasoning forms and argumentation schemes carry worked argument maps (AIF) and critical questions (Walton), so the graph can be used to *check* an argument, not just to look one up.
- **Self-directing growth.** Runs rotate between depth (frontier), breadth (least-covered domain) and gap (SPARQL competency gaps).
- **Reproducible.** Outputs are byte-for-byte deterministic; CI re-runs tests and the build and fails if `graph/` is stale.

## Usage

```bash
pip install -r requirements.txt
python3 scripts/kg.py check                         # validate + reason + SHACL
python3 scripts/kg.py build                         # ...and regenerate graph/
python3 scripts/kg.py similar "Myside bias" --summary "Favouring evidence for one's own side"   # meaning-based duplicate check
python3 scripts/kg.py new cognitive-biases anchoring-effect CognitiveBias   # scaffold
python3 scripts/kg.py query queries/02-remedy-coverage.rq                   # or an inline SPARQL string
python3 -m pytest -q tests                          # end-to-end tests on fixture articles
```

Steer what gets written by editing `topics/seeds.yaml`. The run playbook is `CLAUDE.md`; the article format is `SCHEMA.md`. The `.nt`, `.trig` and `.jsonld` exports load into Apache Jena/Fuseki, GraphDB, Oxigraph, rdflib, or Neo4j via n10s; `.ttls` needs an RDF 1.2 / RDF-star aware store (Jena, GraphDB, Oxigraph).
