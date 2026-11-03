"""End-to-end tests for scripts/kg.py against a throwaway tree of fixture articles.

Fixtures use example.org URLs and synthetic prose: they exercise the validator,
reasoner, SHACL shapes and exports, and are never part of the real graph.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
KG = REPO / "scripts" / "kg.py"


def body(slug: str, sections: list[str]) -> str:
    def para(i: int) -> str:
        words = " ".join(f"{slug.replace('-', '')}{i}w{j}" for j in range(150))
        return f"Synthetic fixture prose for {slug} paragraph {i}: {words}.[^s1][^s2][^s3]"
    out = [f"# {slug}", "", para(0), "", para(1), ""]
    for k, s in enumerate(sections, 2):
        out += [s, "", para(k), ""]
    out += ["## Connections", "", para(99), "", "## Sources", "",
            "[^s1]: Fixture one. https://example.org/1", "[^s2]: Fixture two. https://example.org/2",
            "[^s3]: Fixture three. https://example.org/3"]
    return "\n".join(out) + "\n"


SOURCES = """sources:
  - {id: s1, title: Fixture one, publisher: Example, url: "https://example.org/SLUG/1", type: peer-reviewed, accessed: 2026-11-02}
  - {id: s2, title: Fixture two, publisher: Example, url: "https://example.org/SLUG/2", type: scholarly-encyclopedia, accessed: 2026-11-02}
  - {id: s3, title: Fixture three, publisher: Example, url: "https://example.org/SLUG/3", type: textbook, accessed: 2026-11-02}
created: 2026-11-02
"""

ARTICLES = {
    ("cognitive-biases", "confirmation-bias"): ("""id: ct:confirmation-bias
type: CognitiveBias
title: Confirmation bias
aliases: [myside bias]
domain: cognitive-biases
summary: The tendency to search for, interpret and recall information in ways that support existing beliefs.
level: introductory
evidenceStatus: robust
broader: [ct:cognitive-bias]
related: [ct:motivated-reasoning]
requires: [ct:hypothesis]
relations:
  - {predicate: demonstratedBy, object: ct:wason-selection-task, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:peter-wason, source: s2}
sameAs: [wd:Q431498]
""", ["## Evidence", "## How to spot it", "## How to counter it"]),
    ("debiasing-and-metacognition", "consider-the-opposite"): ("""id: ct:consider-the-opposite
type: Technique
title: Consider the opposite
domain: debiasing-and-metacognition
summary: A debiasing strategy in which people deliberately generate reasons why their initial judgment might be wrong.
level: introductory
evidenceStatus: robust
broader: [ct:debiasing]
requires: [ct:confirmation-bias]
relations:
  - {predicate: counteracts, object: ct:confirmation-bias, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:anchoring-effect, source: s1}
""", ["## How to apply it"]),
    ("formal-logic", "modus-ponens"): ("""id: ct:modus-ponens
type: ReasoningForm
title: Modus ponens
domain: formal-logic
summary: The valid inference from a conditional and its antecedent to the conditional's consequent.
level: introductory
evidenceStatus: normative
broader: [ct:deductive-reasoning]
related: [ct:modus-tollens]
relations:
  - {predicate: studiedIn, object: ct:logic, source: s3}
argumentMap:
  premises: ["If it rains, the street is wet.", "It is raining."]
  conclusion: "The street is wet."
  verdict: valid
""", []),
    ("formal-fallacies", "affirming-the-consequent"): ("""id: ct:affirming-the-consequent
type: FormalFallacy
title: Affirming the consequent
domain: formal-fallacies
summary: The invalid inference from a conditional and its consequent to the conditional's antecedent.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
requires: [ct:modus-ponens]
relations:
  - {predicate: invalidFormOf, object: ct:modus-ponens, source: s3, confidence: high}
  - {predicate: confusedWith, object: ct:modus-ponens, source: s2}
criticalQuestions:
  - Is the conditional the only way the consequent could come about?
  - Could the consequent be true while the antecedent is false?
argumentMap:
  premises: ["If it rains, the street is wet.", "The street is wet."]
  conclusion: "It is raining."
  verdict: invalid
  objections: ["A street cleaner could have wet the street."]
""", ["## How to spot it", "## How to counter it"]),
}


def make_tree(tmp: Path, articles=ARTICLES) -> Path:
    for d in ("ontology", "topics", "queries"):
        shutil.copytree(REPO / d, tmp / d)
    for (dom, slug), (fm, secs) in articles.items():
        p = tmp / "articles" / dom / f"{slug}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"---\n{fm}{SOURCES.replace('SLUG', slug)}---\n{body(slug, secs)}")
    return tmp


def run(tmp: Path, *args: str, hashseed: str = "random") -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(KG), *args], cwd=tmp, env={"PYTHONHASHSEED": hashseed, "CT_KG_ROOT": str(tmp), "PATH": ""},
                          capture_output=True, text=True)


def test_valid_tree_builds(tmp_path):
    t = make_tree(tmp_path)
    r = run(t, "build")
    assert r.returncode == 0, r.stdout + r.stderr
    g = t / "graph"
    inferred = (g / "inferred.nt").read_text()
    # inverse property materialised by the reasoner
    assert "confirmation-bias> <https://github.com/john1hsu/critical-thinking-graph/ontology#counteractedBy>" in inferred
    # symmetric property materialised
    assert "modus-ponens> <https://github.com/john1hsu/critical-thinking-graph/ontology#confusedWith>" in inferred
    # range axiom types the unwritten frontier node
    assert "wason-selection-task> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> " \
           "<https://github.com/john1hsu/critical-thinking-graph/ontology#Study>" in inferred
    frontier = (g / "frontier.md").read_text()
    assert "`ct:peter-wason`" in frontier and "Person" in frontier
    assert "<< <" in (g / "edge-evidence.ttls").read_text()
    assert "flowchart TD" in (g / "argument-maps.md").read_text()
    idx = json.loads((g / "index.json").read_text())
    assert {x["id"] for x in idx} == {"ct:confirmation-bias", "ct:consider-the-opposite", "ct:modus-ponens",
                                      "ct:affirming-the-consequent"}
    comp = (g / "competency.md").read_text()
    assert "ct:consider-the-opposite" in comp
    path = (g / "learning-path.md").read_text()
    assert path.index("Modus ponens") < path.index("Affirming the consequent")
    # deterministic: second build produces identical outputs
    # deterministic: rebuilding under different hash seeds (as CI and scheduled runs do) is byte-identical
    before = {p.name: p.read_text() for p in g.iterdir()}
    for seed in ("1", "2", "3", "4"):
        assert run(t, "build", hashseed=seed).returncode == 0
        assert before == {p.name: p.read_text() for p in g.iterdir()}, f"output changed with PYTHONHASHSEED={seed}"


def mutate(key, old, new):
    arts = dict(ARTICLES)
    fm, secs = arts[key]
    assert old in fm
    arts[key] = (fm.replace(old, new), secs)
    return arts


@pytest.mark.parametrize("key,old,new,expect", [
    (("formal-fallacies", "affirming-the-consequent"), "type: FormalFallacy", "type: Technique",
     "invalidFormOf expects subject"),
    (("cognitive-biases", "confirmation-bias"), "source: s2}", "source: s9}", "unknown source"),
    (("cognitive-biases", "confirmation-bias"), "evidenceStatus: robust", "evidenceStatus: contested",
     "needs a challengedBy"),
    (("formal-fallacies", "affirming-the-consequent"),
     "  - Could the consequent be true while the antecedent is false?\n", "", ">= 2 criticalQuestions"),
    (("debiasing-and-metacognition", "consider-the-opposite"), "title: Consider the opposite",
     "title: Consider the opposite\naliases: [myside bias]", "collides"),
    (("cognitive-biases", "confirmation-bias"), "introducedBy, object: ct:peter-wason",
     "introducedBy, object: ct:wason-selection-task", "contradiction"),
])
def test_rejections(tmp_path, key, old, new, expect):
    t = make_tree(tmp_path, mutate(key, old, new))
    r = run(t, "check")
    assert r.returncode == 1 and expect in r.stdout, r.stdout


def test_requires_cycle(tmp_path):
    arts = mutate(("formal-logic", "modus-ponens"), "related: [ct:modus-tollens]",
                  "related: [ct:modus-tollens]\nrequires: [ct:affirming-the-consequent]")
    r = run(make_tree(tmp_path, arts), "check")
    assert r.returncode == 1 and "cycle in 'requires'" in r.stdout


def test_banned_source(tmp_path):
    t = make_tree(tmp_path)
    p = t / "articles" / "formal-logic" / "modus-ponens.md"
    p.write_text(p.read_text().replace("https://example.org/modus-ponens/1", "https://en.wikipedia.org/wiki/X"))
    r = run(t, "check")
    assert r.returncode == 1 and "banned domain" in r.stdout


def test_similar_and_new(tmp_path):
    t = make_tree(tmp_path)
    r = run(t, "similar", "myside bias")
    assert r.returncode == 0 and r.stdout.splitlines()[1].split()[3] == "ct:confirmation-bias"
    r = run(t, "new", "informal-fallacies", "straw-man", "InformalFallacy")
    assert r.returncode == 0
    text = (t / "articles" / "informal-fallacies" / "straw-man.md").read_text()
    assert "criticalQuestions" in text and "## How to counter it" in text


def test_empty_tree(tmp_path):
    t = make_tree(tmp_path, {})
    r = run(t, "build")
    assert r.returncode == 0, r.stdout
