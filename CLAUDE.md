# Critical Thinking Graph — run playbook

This repo is a citation-backed, reasoner-checked knowledge graph of critical thinking: logic and reasoning forms, argumentation, formal/informal/probabilistic fallacies, cognitive biases and heuristics, scientific reasoning, evidence and information literacy, structured decision making, debiasing and metacognition, philosophy of reasoning, and the history of the ideas. A scheduled run adds **exactly one new, unique article** per run. Follow these steps in order. Read `SCHEMA.md` before writing.

## 1. Sync and orient
```bash
pip install -r requirements.txt --break-system-packages -q
git pull --rebase origin main
python3 scripts/kg.py build      # must print OK; fix the repo first if it doesn't
```
Read `graph/stats.md`, `graph/frontier.md`, `graph/competency.md` and `topics/seeds.yaml`. `graph/index.json` lists every node (ids, titles, aliases, edges, critical questions, source URLs).

## 2. Pick the topic (graph-driven)
Use the current UTC hour modulo 3:
- **0 → depth.** Take the top node in `graph/frontier.md` that fits a domain, **skipping any node that would belong to the domain with the most articles** ("Domain coverage" in `graph/stats.md`; on a tie for most, skip all tied domains), so one domain's dense cross-links can't snowball into a lopsided graph. Use its *Expected type* (inferred by the reasoner) as the article's `type` unless it is clearly wrong.
- **1 → breadth.** Take the domain at the top of "Domain coverage" in `graph/stats.md` (fewest articles; skip the domain of the most recent commit on ties) and pick an unwritten seed or another important topic in it.
- **2 → gap.** Take the first row of the first non-empty *(gap)* section in `graph/competency.md` and write the article that closes it (e.g. a technique that counteracts an unremedied bias, the valid form a formal fallacy imitates, the person or work that introduced an unattributed concept).
- If the chosen mode yields nothing, fall back to breadth.

Then prove it is unique:
```bash
python3 scripts/kg.py similar "<candidate title>"
```
If any score ≥ 0.5, or an existing title/alias names the same thing, pick a different topic. Never write a second article on an existing subject — not a rename, a sub-angle that restates it, an abbreviation, or a synonym. Record alternate names as `aliases`.

## 3. Research
- Run several web searches and read the actual pages (WebFetch). Don't rely on snippets or memory.
- Collect 3–6 credible sources: ≥ 1 scholarly and ≥ 2 strong (see `SCHEMA.md`). Prefer the original study or book, peer-reviewed reviews and meta-analyses, the Stanford or Internet Encyclopedia of Philosophy, academic textbooks, and government tradecraft texts (CIA, ODNI) for analytic techniques. **Never cite Wikipedia** or the other banned sources.
- Every URL you cite must be one you opened this run. Never invent a URL, DOI or Wikidata id. Only add `sameAs: [wd:Q…]` if you opened that Wikidata page and it is the same concept.
- Psychology is not settled by one study. For any bias, heuristic or effect, look for replication evidence (large multi-lab replications, meta-analyses) and set `evidenceStatus` honestly; if it is `contested` or `failed-replication`, add a `challengedBy` edge to the critique or replication.
- Date time-sensitive figures ("a 2023 meta-analysis of 54 studies found…"). Attribute claims of a single author or school.
- Paraphrase. No quotation longer than 15 words; at most one quote per source.

## 4. Write the node
```bash
python3 scripts/kg.py new <domain> <slug> <Type>   # scaffold with the fields and sections the class requires
```
- 400–1,000 words, practitioner level: definition, origin (who, where, when), how it works with a concrete everyday or workplace example, how to spot it / apply it, evidence and limitations, and **Connections**.
- Every substantive paragraph carries footnote citations `[^sN]`; list every source in `## Sources`.
- Edges: 1–3 `broader`, `related` as needed, `requires` for genuine prerequisites, and ≥ 1 (ideally 2–5) typed `relations`, **each citing the source that supports it** and a confidence. Link to existing ids wherever they fit (`graph/index.json`); new target ids are fine and join the frontier. Pick relation directions that match the predicate's domain and range (`SCHEMA.md`). Never write inverses — the reasoner adds them.
- Fallacies, reasoning forms and argument schemes need an `argumentMap` (a short, realistic worked example) and fallacies/schemes need `criticalQuestions` a reader could actually ask.
- If a needed class or predicate is missing, add it to `ontology/ontology.ttl` (label, domain/range, inverse/characteristics) in the same commit. Keep the ontology small; reuse first.
- Back-links: if `graph/suggested-links.md` or the new node shows an existing article should point to it, you may add the id to that article's `related` (or a sourced typed relation). Don't otherwise rewrite existing articles.

## 5. Validate, build, commit, push
```bash
python3 scripts/kg.py build    # fix every problem (structure, citations, reasoning contradictions, SHACL) and re-run until OK
git add -A
git commit -m "Add <Title> (<domain>, <mode> run)"
git pull --rebase origin main && python3 scripts/kg.py build && git push origin main
```
If the push is rejected, pull --rebase, rebuild, and push again (once). Commit regenerated `graph/` files with the article; CI fails if they are stale.

## Don'ts
- Don't add more than one article per run, delete articles, or rewrite history.
- Don't commit if validation fails; leave the repo clean.
- Don't cite a source you didn't open, or attach a source to an edge it doesn't support.
- Don't hand-edit anything in `graph/`.
- Don't use real, named private individuals or current partisan figures in argument-map examples; use neutral, everyday or workplace scenarios.
