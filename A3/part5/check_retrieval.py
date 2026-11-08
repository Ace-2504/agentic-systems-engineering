"""A3 Part 5 · the CI check (rule 12: measure again after every change, in CI).

Rebuilds the index from domain/docs with the configuration Part 5 picked (logs/part5_grid.json) and fails (exit code 1)
if retrieval or the permission filter regresses. No model calls, no key, a few seconds on a GPU. Run it after any
change to the documents, the parser, the chunking or the search settings:

    python part5/check_retrieval.py            # retrieval, permissions, versions
    python part5/check_retrieval.py --latency  # also the search p95 target (only meaningful on the machine that set it)
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
A3 = HERE.parent
sys.path.insert(0, str(HERE))

import domain_rules as DR  # noqa: E402
from ledgerline.course.l3 import corpus as C  # noqa: E402
from ledgerline.course.l3 import evaluate as E  # noqa: E402
from ledgerline.course.l3 import rag  # noqa: E402

MIN_RECALL5 = 0.90   # AUDIT.md's target, kept for this domain
MAX_P95_MS = 200     # search p95 on the RTX 3060


def main(latency: bool) -> int:
    cfg = rag.Config.from_id(json.loads((A3 / "logs" / "part5_grid.json").read_text(encoding="utf-8"))["winner"])
    units, rep = DR.handle_versions(DR.parse(A3 / "domain" / "docs"))
    chunks = C.chunk(units, cfg.chunker, cfg.size, cfg.overlap)
    models = [] if cfg.retrieval == "bm25" else [cfg.embed]
    idx = rag.Index.build(chunks, models, pathlib.Path.home() / ".cache" / "a3-domain-ci" / cfg.chunking)
    ret = rag.Retriever(idx, cfg)
    ret.search("warm-up", role="AP-EXEC")

    qs = DR.load_golden(HERE / "golden_v2.jsonl")
    G = DR.DomainGolden(A3 / "domain" / "docs", qs, {})
    scored = [q for q in qs if G.expected(q) == "answer"]
    r = E.retrieval_only(lambda question, role: ret.search(question, role=role), G, qs=scored)
    recall5 = r["summary"]["overall"]["recall@5"]
    p95_ms = r["summary"]["latency_s"]["p95"] * 1000
    leaked = sorted({q["id"] for q in qs for it in ret.search(q["question"], role=q["asker_role"])["items"]
                     if (it.get("meta") or {}).get("confidential")})
    live_versions = {d: [f for f in fs if not rep["metas"][f].get("superseded") and not rep["metas"][f]["future"]]
                     for d, fs in rep["versions"].items()}

    checks = {
        f"recall@5 >= {MIN_RECALL5:.0%} on {len(scored)} questions (got {recall5:.0%})": recall5 >= MIN_RECALL5,
        f"no confidential chunk returned to a non-HR role (leaked on: {leaked or 'none'})": not leaked,
        "each document with several versions has exactly one version in force":
            all(len(v) == 1 for v in live_versions.values()),
    }
    if latency:
        checks[f"search p95 <= {MAX_P95_MS} ms (got {p95_ms:.0f} ms)"] = p95_ms <= MAX_P95_MS
    print(f"configuration: {cfg.id}")
    for name, ok in checks.items():
        print(("PASS  " if ok else "FAIL  ") + name)
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main("--latency" in sys.argv))
