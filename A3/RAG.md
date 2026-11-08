# A3 · Part 2 · RAG, tuned

**Total model spend for A3: US$3.48**, which is $0.48 over the brief's $3 cap (live calls to Gemini 3.8 Flash,
costed at $0.825 / $4.125 per million input / output tokens). Parts 1 and 2 call no model (Part 2 is retrieval only).
Part 3, the wiki: $1.96 (see WIKI.md section 6). Part 4, the race: $1.15 (see RACE.md section 8).
Part 5, my domain: $0.36 (see DOMAIN.md section 9).

**Agentic Systems Engineering · Lecture 3 · Harman Singh Sandhu**

Every number here comes from section "A3 · Part 2" of my notebook (`A3_harman.ipynb`), run live on my own machine:
RTX 3060 (12 GB), Python 3.11.9, PyTorch 2.6.0 with CUDA 12.4, Chroma 1.0.15. Nothing in Part 2 is replayed. All 108
configurations were built and timed on that one machine, one after another, in 16.4 minutes.

## Key findings

- **The winner meets both targets:** structured parser, structure-aware 400-token chunks, hybrid search (BM25 +
  `bge-small`) with the `bge-reranker-base` reranker. recall@5 **0.909** (target ≥ 0.90), search p95 **139 ms**
  (target ≤ 200 ms) on an RTX 3060 (section 4).
- **Keyword search beats meaning search on this corpus:** mean recall@5 BM25 0.761, hybrid 0.693, dense 0.514. Dense
  search missed the gold source for 3 of the 4 error-code questions entirely; BM25 found all 4 (sections 3 and 5).
- **The reranker is the biggest single gain and the biggest cost:** +0.11 mean recall@5, from about 18 ms to 125 ms
  median p95 (section 3).
- **A part tuned on its own is not a better system.** Tuning BM25's k1 and b raised BM25-alone recall@5 from 0.697 to
  0.849 (+5 questions), but inside the full pipeline the same tuning changed at most one question, because the
  reranker only needs the right passage somewhere in the top 20. A setting has to be measured in the pipeline that
  will ship (section 6).

## 1. The golden subset

**Rule:** 4 questions of each of the 10 documentation types in `eval/questions.jsonl` (40 in all). Emma's two running
questions are always in: Q-EMMA (multi-hop) and Q-0412 (exact code). The rest of each type is a seeded random draw, so every run gets the same 40. Parts 3 and 4 use the same 40.

| Type | Questions | Scored for recall |
|---|---|---:|
| exact_code | Q-0412, Q-705, Q-703, Q-711 | 4 |
| multi_hop | Q-EMMA, Q-502, Q-510, Q-505 | 4 |
| not_in_docs | Q-811 (abstain), Q-809 (abstain), Q-808 (abstain), Q-802 (abstain) | 0 |
| permission | Q-907, Q-904 (refuse), Q-903 (refuse), Q-906 (refuse) | 1 |
| procedure | Q-110, Q-104, Q-112, Q-118 | 4 |
| rule | Q-219, Q-222, Q-208, Q-213 | 4 |
| service_field | Q-312, Q-322, Q-334, Q-335 | 4 |
| single_lookup | Q-002, Q-011, Q-010, Q-020 | 4 |
| table_lookup | Q-412, Q-422, Q-413, Q-433 | 4 |
| version_conflict | Q-618, Q-610, Q-615, Q-607 | 4 |
| **Total** | **40** | **33** |

Not-in-the-documents questions (abstain) and permission questions that must be refused have no gold source to find;
they are scored on the answer in Part 4. That leaves **33 questions scored for recall, so one question is worth
0.030**: any two configurations closer than that differ by less than one question. Their gold sources are 39 files in
9 folders (01_policies 13, 03_ledgerline_manuals 6, 02_procedures 5, 04_service_definitions 4, 05_master_data 4,
09_email_archive 3, 08_release_notes 2, 10_meeting_notes 1, 11_training 1). The full list, with every gold source down
to the page or sheet row, is the output of cell A3 · Part 2 · 1. Before anything was scored, that cell checked that
every gold file was among the parsed files and that the 4 HR files were flagged confidential.

## 2. The selection rule, fixed before the grid ran

> Among configurations whose search p95 is at most **200 ms**, choose the highest **recall@5**. An exact tie goes to
> the higher MRR, then the lower p95.

The limit and the goal are my Part 1 targets (AUDIT.md section 3): search p95 ≤ 200 ms and recall@5 ≥ 90%. The rule
was written into the notebook and this file before the grid ran.

## 3. The grid

| | Values |
|---|---|
| **Varied** | parser (plain, structured) × chunker (fixed, recursive, structure-aware) × size (200, 400, 800 tokens) × search (BM25, dense, hybrid) × reranker (off, on) = **108 configurations** |
| **Fixed** | 15% overlap · embeddings `bge-small` (BAAI/bge-small-en-v1.5, 384 dimensions) in Chroma with `rag.HNSW` (cosine, ef_search 4000, ef_construction 200, max_neighbors 32) · hybrid = BM25 and dense top 20 each, fused by RRF (k = 60) · reranker `bge-reranker-base` over the top 20 · top 10 returned · no query rewriting · permission filter before ranking |
| **Timing** | search time per question, from question in to ranked passages out, measured one question at a time after one untimed warm-up search per configuration; p50 and p95 over the 40 questions |

### Every configuration, best recall@5 first

| # | Parser | Chunker | Size | Search | Reranker | Chunks | Recall@5 | Recall@10 | MRR | p50 ms | p95 ms |
|---:|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | structured | structure | 400 | hybrid (bge-small) | on | 13,734 | 0.909 | 0.970 | 0.761 | 131.0 | 139.2 |
| 2 | structured | structure | 400 | bm25 | on | 13,734 | 0.909 | 0.939 | 0.731 | 115.5 | 120.2 |
| 3 | structured | structure | 200 | bm25 | on | 28,953 | 0.909 | 0.939 | 0.689 | 68.3 | 74.5 |
| 4 | structured | recursive | 200 | bm25 | on | 28,711 | 0.879 | 0.909 | 0.712 | 70.4 | 74.8 |
| 5 | plain | structure | 400 | bm25 | on | 9,671 | 0.879 | 0.879 | 0.631 | 114.3 | 121.5 |
| 6 | structured | fixed | 200 | bm25 | on | 27,811 | 0.849 | 0.909 | 0.684 | 71.6 | 77.1 |
| 7 | structured | recursive | 400 | hybrid (bge-small) | on | 14,040 | 0.849 | 0.939 | 0.660 | 131.1 | 139.6 |
| 8 | structured | recursive | 400 | bm25 | on | 14,040 | 0.849 | 0.909 | 0.645 | 116.5 | 121.8 |
| 9 | structured | fixed | 400 | bm25 | on | 13,973 | 0.849 | 0.909 | 0.606 | 116.4 | 122.9 |
| 10 | structured | fixed | 200 | hybrid (bge-small) | on | 27,811 | 0.818 | 0.939 | 0.708 | 87.0 | 97.6 |
| 11 | structured | structure | 200 | hybrid (bge-small) | on | 28,953 | 0.818 | 0.939 | 0.640 | 82.5 | 88.7 |
| 12 | structured | fixed | 400 | hybrid (bge-small) | on | 13,973 | 0.818 | 0.909 | 0.575 | 131.7 | 137.7 |
| 13 | plain | structure | 200 | bm25 | on | 19,634 | 0.788 | 0.849 | 0.618 | 56.0 | 66.1 |
| 14 | plain | recursive | 200 | bm25 | on | 19,621 | 0.788 | 0.818 | 0.616 | 56.0 | 67.9 |
| 15 | structured | fixed | 200 | bm25 | off | 27,811 | 0.788 | 0.879 | 0.569 | 0.2 | 0.3 |
| 16 | structured | fixed | 800 | bm25 | off | 7,223 | 0.788 | 0.939 | 0.557 | 0.2 | 0.2 |
| 17 | structured | recursive | 800 | bm25 | on | 7,243 | 0.788 | 0.849 | 0.552 | 119.4 | 127.3 |
| 18 | plain | structure | 400 | hybrid (bge-small) | on | 9,671 | 0.788 | 0.818 | 0.551 | 129.6 | 136.6 |
| 19 | structured | structure | 800 | bm25 | off | 6,853 | 0.788 | 0.909 | 0.546 | 0.2 | 0.2 |
| 20 | structured | recursive | 400 | bm25 | off | 14,040 | 0.788 | 0.818 | 0.527 | 0.2 | 0.3 |
| 21 | structured | fixed | 800 | bm25 | on | 7,223 | 0.788 | 0.849 | 0.516 | 118.7 | 125.3 |
| 22 | structured | recursive | 200 | hybrid (bge-small) | on | 28,711 | 0.758 | 0.849 | 0.710 | 85.8 | 94.2 |
| 23 | plain | recursive | 800 | bm25 | on | 5,345 | 0.758 | 0.788 | 0.594 | 117.8 | 123.7 |
| 24 | plain | structure | 800 | bm25 | on | 5,072 | 0.758 | 0.788 | 0.593 | 118.5 | 123.5 |
| 25 | plain | recursive | 400 | bm25 | on | 9,988 | 0.758 | 0.849 | 0.587 | 112.3 | 118.8 |
| 26 | plain | fixed | 400 | bm25 | on | 9,970 | 0.758 | 0.849 | 0.572 | 113.4 | 120.7 |
| 27 | structured | recursive | 800 | bm25 | off | 7,243 | 0.758 | 0.939 | 0.550 | 0.2 | 0.3 |
| 28 | structured | recursive | 200 | bm25 | off | 28,711 | 0.758 | 0.818 | 0.549 | 0.2 | 0.3 |
| 29 | plain | fixed | 200 | hybrid (bge-small) | off | 19,859 | 0.758 | 0.788 | 0.548 | 15.9 | 20.8 |
| 30 | structured | fixed | 400 | bm25 | off | 13,973 | 0.758 | 0.818 | 0.524 | 0.2 | 0.2 |
| 31 | structured | structure | 200 | bm25 | off | 28,953 | 0.758 | 0.909 | 0.520 | 0.2 | 0.3 |
| 32 | structured | structure | 200 | hybrid (bge-small) | off | 28,953 | 0.758 | 0.849 | 0.500 | 14.3 | 18.2 |
| 33 | plain | recursive | 200 | bm25 | off | 19,621 | 0.758 | 0.849 | 0.477 | 0.2 | 0.3 |
| 34 | plain | recursive | 200 | hybrid (bge-small) | off | 19,621 | 0.727 | 0.818 | 0.600 | 16.6 | 19.0 |
| 35 | plain | recursive | 200 | hybrid (bge-small) | on | 19,621 | 0.727 | 0.758 | 0.591 | 72.7 | 77.1 |
| 36 | plain | structure | 800 | hybrid (bge-small) | on | 5,072 | 0.727 | 0.758 | 0.578 | 134.8 | 143.8 |
| 37 | plain | fixed | 400 | hybrid (bge-small) | on | 9,970 | 0.727 | 0.849 | 0.565 | 128.6 | 136.0 |
| 38 | plain | fixed | 200 | bm25 | on | 19,859 | 0.727 | 0.849 | 0.559 | 61.9 | 77.3 |
| 39 | plain | fixed | 200 | hybrid (bge-small) | on | 19,859 | 0.727 | 0.788 | 0.535 | 76.9 | 87.0 |
| 40 | structured | recursive | 800 | hybrid (bge-small) | on | 7,243 | 0.727 | 0.818 | 0.532 | 136.5 | 144.4 |
| 41 | structured | structure | 800 | bm25 | on | 6,853 | 0.727 | 0.788 | 0.496 | 118.5 | 123.5 |
| 42 | plain | fixed | 200 | bm25 | off | 19,859 | 0.727 | 0.849 | 0.492 | 0.2 | 0.3 |
| 43 | structured | fixed | 800 | hybrid (bge-small) | on | 7,223 | 0.727 | 0.818 | 0.478 | 134.9 | 143.3 |
| 44 | plain | structure | 200 | hybrid (bge-small) | on | 19,634 | 0.697 | 0.818 | 0.584 | 75.1 | 81.0 |
| 45 | plain | fixed | 800 | bm25 | on | 5,238 | 0.697 | 0.818 | 0.579 | 122.0 | 126.4 |
| 46 | plain | recursive | 800 | hybrid (bge-small) | on | 5,345 | 0.697 | 0.758 | 0.577 | 132.5 | 138.2 |
| 47 | plain | structure | 200 | hybrid (bge-small) | off | 19,634 | 0.697 | 0.849 | 0.554 | 18.9 | 24.0 |
| 48 | plain | recursive | 400 | hybrid (bge-small) | on | 9,988 | 0.697 | 0.849 | 0.550 | 129.8 | 136.9 |
| 49 | structured | structure | 400 | bm25 | off | 13,734 | 0.697 | 0.909 | 0.541 | 0.2 | 0.4 |
| 50 | structured | fixed | 200 | hybrid (bge-small) | off | 27,811 | 0.697 | 0.849 | 0.520 | 16.9 | 20.9 |
| 51 | plain | structure | 400 | bm25 | off | 9,671 | 0.697 | 0.788 | 0.495 | 0.2 | 0.3 |
| 52 | structured | recursive | 200 | hybrid (bge-small) | off | 28,711 | 0.697 | 0.818 | 0.487 | 14.4 | 17.8 |
| 53 | structured | structure | 400 | hybrid (bge-small) | off | 13,734 | 0.697 | 0.788 | 0.478 | 16.1 | 21.6 |
| 54 | plain | fixed | 800 | hybrid (bge-small) | on | 5,238 | 0.667 | 0.818 | 0.565 | 134.7 | 138.4 |
| 55 | structured | recursive | 400 | dense (bge-small) | on | 14,040 | 0.667 | 0.697 | 0.555 | 130.6 | 136.4 |
| 56 | plain | recursive | 200 | dense (bge-small) | on | 19,621 | 0.667 | 0.667 | 0.543 | 71.6 | 79.6 |
| 57 | structured | fixed | 400 | dense (bge-small) | on | 13,973 | 0.667 | 0.727 | 0.519 | 130.5 | 137.4 |
| 58 | plain | fixed | 800 | bm25 | off | 5,238 | 0.667 | 0.818 | 0.496 | 0.2 | 0.4 |
| 59 | structured | structure | 800 | hybrid (bge-small) | on | 6,853 | 0.667 | 0.788 | 0.483 | 135.8 | 142.9 |
| 60 | structured | fixed | 800 | dense (bge-small) | on | 7,223 | 0.667 | 0.667 | 0.452 | 133.3 | 140.1 |
| 61 | plain | structure | 200 | bm25 | off | 19,634 | 0.667 | 0.818 | 0.442 | 0.2 | 0.3 |
| 62 | structured | structure | 400 | dense (bge-small) | on | 13,734 | 0.636 | 0.667 | 0.551 | 128.7 | 136.4 |
| 63 | plain | fixed | 400 | bm25 | off | 9,970 | 0.636 | 0.788 | 0.546 | 0.2 | 0.3 |
| 64 | plain | fixed | 400 | dense (bge-small) | on | 9,970 | 0.636 | 0.667 | 0.513 | 128.9 | 137.8 |
| 65 | plain | recursive | 400 | bm25 | off | 9,988 | 0.636 | 0.818 | 0.496 | 0.2 | 0.3 |
| 66 | plain | structure | 800 | bm25 | off | 5,072 | 0.636 | 0.788 | 0.494 | 0.2 | 0.3 |
| 67 | plain | recursive | 800 | bm25 | off | 5,345 | 0.636 | 0.758 | 0.486 | 0.2 | 0.3 |
| 68 | structured | fixed | 400 | hybrid (bge-small) | off | 13,973 | 0.636 | 0.788 | 0.486 | 16.9 | 17.9 |
| 69 | structured | recursive | 400 | hybrid (bge-small) | off | 14,040 | 0.636 | 0.818 | 0.483 | 13.7 | 18.2 |
| 70 | structured | fixed | 800 | hybrid (bge-small) | off | 7,223 | 0.636 | 0.849 | 0.471 | 14.0 | 18.1 |
| 71 | plain | recursive | 400 | hybrid (bge-small) | off | 9,988 | 0.606 | 0.697 | 0.514 | 15.8 | 21.7 |
| 72 | plain | structure | 200 | dense (bge-small) | on | 19,634 | 0.606 | 0.636 | 0.476 | 74.1 | 82.8 |
| 73 | plain | fixed | 200 | dense (bge-small) | on | 19,859 | 0.606 | 0.636 | 0.475 | 77.5 | 84.9 |
| 74 | structured | recursive | 800 | dense (bge-small) | on | 7,243 | 0.606 | 0.606 | 0.446 | 135.0 | 141.1 |
| 75 | structured | recursive | 200 | dense (bge-small) | on | 28,711 | 0.576 | 0.606 | 0.566 | 84.2 | 92.9 |
| 76 | plain | recursive | 400 | dense (bge-small) | on | 9,988 | 0.576 | 0.667 | 0.524 | 130.8 | 136.2 |
| 77 | structured | structure | 200 | dense (bge-small) | on | 28,953 | 0.576 | 0.697 | 0.487 | 81.8 | 88.6 |
| 78 | plain | fixed | 400 | hybrid (bge-small) | off | 9,970 | 0.576 | 0.697 | 0.473 | 13.4 | 16.8 |
| 79 | structured | recursive | 800 | hybrid (bge-small) | off | 7,243 | 0.576 | 0.818 | 0.472 | 19.2 | 22.3 |
| 80 | structured | structure | 800 | hybrid (bge-small) | off | 6,853 | 0.576 | 0.818 | 0.436 | 13.1 | 15.2 |
| 81 | plain | structure | 400 | hybrid (bge-small) | off | 9,671 | 0.576 | 0.727 | 0.419 | 15.9 | 20.8 |
| 82 | structured | fixed | 200 | dense (bge-small) | on | 27,811 | 0.545 | 0.576 | 0.499 | 88.4 | 98.4 |
| 83 | plain | recursive | 200 | dense (bge-small) | off | 19,621 | 0.545 | 0.667 | 0.461 | 15.3 | 18.3 |
| 84 | structured | structure | 800 | dense (bge-small) | on | 6,853 | 0.545 | 0.576 | 0.437 | 133.8 | 143.9 |
| 85 | plain | fixed | 800 | dense (bge-small) | on | 5,238 | 0.545 | 0.576 | 0.433 | 135.9 | 142.1 |
| 86 | structured | structure | 800 | dense (bge-small) | off | 6,853 | 0.545 | 0.576 | 0.429 | 15.7 | 17.2 |
| 87 | plain | fixed | 800 | hybrid (bge-small) | off | 5,238 | 0.545 | 0.727 | 0.379 | 14.2 | 23.0 |
| 88 | structured | structure | 200 | dense (bge-small) | off | 28,953 | 0.515 | 0.667 | 0.423 | 14.3 | 18.0 |
| 89 | structured | recursive | 400 | dense (bge-small) | off | 14,040 | 0.515 | 0.636 | 0.402 | 15.8 | 18.8 |
| 90 | plain | recursive | 400 | dense (bge-small) | off | 9,988 | 0.515 | 0.667 | 0.392 | 13.9 | 17.8 |
| 91 | plain | structure | 800 | hybrid (bge-small) | off | 5,072 | 0.515 | 0.697 | 0.348 | 18.7 | 21.4 |
| 92 | plain | structure | 200 | dense (bge-small) | off | 19,634 | 0.485 | 0.606 | 0.448 | 17.4 | 22.5 |
| 93 | structured | recursive | 200 | dense (bge-small) | off | 28,711 | 0.485 | 0.545 | 0.439 | 15.4 | 20.9 |
| 94 | plain | fixed | 200 | dense (bge-small) | off | 19,859 | 0.485 | 0.606 | 0.424 | 16.2 | 19.6 |
| 95 | structured | fixed | 400 | dense (bge-small) | off | 13,973 | 0.485 | 0.576 | 0.382 | 14.0 | 18.7 |
| 96 | plain | recursive | 800 | hybrid (bge-small) | off | 5,345 | 0.485 | 0.667 | 0.319 | 13.3 | 17.2 |
| 97 | plain | structure | 400 | dense (bge-small) | on | 9,671 | 0.455 | 0.545 | 0.399 | 131.6 | 139.9 |
| 98 | structured | fixed | 200 | dense (bge-small) | off | 27,811 | 0.455 | 0.515 | 0.398 | 20.2 | 24.0 |
| 99 | structured | structure | 400 | dense (bge-small) | off | 13,734 | 0.455 | 0.636 | 0.390 | 14.2 | 18.4 |
| 100 | structured | recursive | 800 | dense (bge-small) | off | 7,243 | 0.455 | 0.485 | 0.377 | 14.4 | 20.8 |
| 101 | plain | fixed | 400 | dense (bge-small) | off | 9,970 | 0.455 | 0.606 | 0.341 | 14.2 | 21.8 |
| 102 | plain | structure | 800 | dense (bge-small) | on | 5,072 | 0.424 | 0.485 | 0.358 | 133.2 | 141.5 |
| 103 | plain | structure | 400 | dense (bge-small) | off | 9,671 | 0.394 | 0.515 | 0.353 | 14.1 | 22.1 |
| 104 | plain | recursive | 800 | dense (bge-small) | on | 5,345 | 0.394 | 0.455 | 0.326 | 131.2 | 138.0 |
| 105 | plain | fixed | 800 | dense (bge-small) | off | 5,238 | 0.394 | 0.485 | 0.279 | 15.3 | 19.8 |
| 106 | plain | structure | 800 | dense (bge-small) | off | 5,072 | 0.333 | 0.424 | 0.259 | 12.4 | 20.2 |
| 107 | structured | fixed | 800 | dense (bge-small) | off | 7,223 | 0.303 | 0.485 | 0.310 | 14.2 | 16.5 |
| 108 | plain | recursive | 800 | dense (bge-small) | off | 5,345 | 0.303 | 0.394 | 0.252 | 13.8 | 18.4 |

### What each setting does on its own

Each row averages every configuration that uses that value, so a setting is seen across all combinations of the others.

| Setting | Value | Configurations | Mean recall@5 | Best recall@5 | Median p95 ms |
|---|---|---:|---:|---:|---:|
| parser | plain | 54 | 0.625 | 0.879 | 45.0 |
| parser | structured | 54 | 0.687 | 0.909 | 49.2 |
| chunker | fixed | 36 | 0.656 | 0.849 | 50.5 |
| chunker | recursive | 36 | 0.657 | 0.879 | 45.1 |
| chunker | structure | 36 | 0.656 | 0.909 | 45.0 |
| size | 200 | 36 | 0.689 | 0.909 | 45.0 |
| size | 400 | 36 | 0.672 | 0.909 | 70.5 |
| size | 800 | 36 | 0.607 | 0.788 | 73.2 |
| retrieval | bm25 | 36 | 0.761 | 0.909 | 33.2 |
| retrieval | dense | 36 | 0.514 | 0.667 | 51.8 |
| retrieval | hybrid | 36 | 0.693 | 0.909 | 50.5 |
| rerank | False | 54 | 0.601 | 0.788 | 18.1 |
| rerank | True | 54 | 0.711 | 0.909 | 124.5 |

In the lecture's terms:

- **Search method.** BM25 is the strongest single search (mean recall@5 0.761), hybrid is second (0.693) and dense
  is last (0.514); the best dense configuration reaches only 0.667. The lecture found the same order on all 224
  questions: BM25 alone beat the best embedding model. Northbridge's questions are full of codes, item numbers and
  document numbers, which a keyword match finds and a meaning match blurs (section 5).
- **Reranker.** It is the largest single gain: mean recall@5 0.601 → 0.711 (+0.110, the same +0.11 the lecture
  measured), and the best configuration without it stops at 0.788. It is also the largest cost: median search p95 goes
  from 18 ms to 125 ms. With BM25 on structured, structure-aware chunks it adds about 75 ms at 200 tokens and about
  120 ms at 400, because it reads question and passage together and longer passages take longer to read.
- **Parser.** Structured beats plain on average (0.687 vs 0.625) and at the top (0.909 vs 0.879). This is Part 1's finding at scale. The structured side differs in two ways at once: rows keep
  their column names (and e-mails lose their transport headers), and every chunk starts with a context header
  (title, version, status, heading). The grid compares the two parsers as the course code builds them, so it
  measures both together.
- **Chunk size.** 200 (0.689) and 400 (0.672) are close; 800 is clearly worse (0.607, best only 0.788). With BM25
  alone, which reads every word of a chunk, 800 is not worse (0.788, the same as 200 and 400); the drop is in the
  configurations that use the embedding model or the reranker. Section 7 measures why: both models read at most 512
  of their own tokens, and most 800-token chunks are longer than that.
- **Chunker.** The three chunkers have the same average (0.656), but only structure-aware chunking reaches the top.
  Holding everything else equal (structured parser, 200 tokens, BM25 + reranker): structure-aware 0.909, recursive
  0.879, fixed 0.849. Keeping a section, row or e-mail whole matters most once the rest of the pipeline is good.
- **Latency.** On the RTX 3060 every one of the 108 configurations met the 200 ms limit: BM25 alone answers in under
  half a millisecond, dense and hybrid in 15 to 24 ms (p95), and every configuration with the reranker in 66 to
  144 ms. So on this machine the limit ruled nothing out and the rule came down to recall@5 and its tie-break.

## 4. The choice

**Winner: `structured-structure-400-o15 | bge-small | hybrid | rr1 | qr0 | k10`**: structured parser, structure-aware
chunks of 400 tokens with 15% overlap (13,734 chunks), hybrid search (BM25 + `bge-small`, fused by RRF), reranked by
`bge-reranker-base`, top 10.

| Metric | Result | Target (AUDIT.md) | |
|---|---:|---:|---|
| recall@5 | **0.909** (30 of 33) | ≥ 0.90 | met |
| recall@10 | 0.970 (32 of 33) | report | |
| MRR | 0.761 | report | |
| search p50 | 131.0 ms | | |
| search p95 | **139.2 ms** | ≤ 200 ms | met |

**The tie.** Three configurations reached the best recall@5, 0.909:

| Configuration | recall@5 | recall@10 | MRR | search p95 |
|---|---:|---:|---:|---:|
| structured · structure · 400 · **hybrid + reranker** | 0.909 | 0.970 | **0.761** | 139.2 ms |
| structured · structure · 400 · BM25 + reranker | 0.909 | 0.939 | 0.731 | 120.2 ms |
| structured · structure · 200 · BM25 + reranker | 0.909 | 0.939 | 0.689 | 74.5 ms |

The rule breaks the tie by MRR, so the hybrid configuration wins: it puts the first gold source higher on average and
finds one more question in its top 10. The third row is the lecture's own winner. It is half as slow and only one
question behind on recall@10. On a slower machine, or under a tighter latency target, it would be the right choice;
under the rule I fixed before the grid ran, the hybrid configuration stands.

**By question type**, the winner's recall@5:

| Type | Scored questions | recall@5 |
|---|---:|---:|
| procedure | 4 | 0.75 |
| table_lookup | 4 | 0.75 |
| version_conflict | 4 | 0.75 |
| single_lookup | 4 | 1.00 |
| rule | 4 | 1.00 |
| service_field | 4 | 1.00 |
| multi_hop | 4 | 1.00 |
| exact_code | 4 | 1.00 |
| permission | 1 | 1.00 |

Recall@5 counts a question as found when **at least one** of its gold sources is in the top 5. 16 of the 33 scored
questions have two or more gold sources (Q-EMMA has 11), so for multi-hop questions 1.00 means "at least one source
found", not "every source found".

**What it misses at 5:**

| Question | Type | Rank of the first gold source |
|---|---|---:|
| Q-110 "How do I raise a purchase request?" | procedure | 9 |
| Q-615 "Did chargers always need UN 38.3?" | version_conflict | 6 |
| Q-422 "What is the warehouse WH-MAN-BAT?" | table_lookup | not in the top 10 |

The answer step in Part 4 reads all 10 passages, so Q-110 and Q-615 still reach the answer model; Q-422 is the one
question where the gold source never arrives.

## 5. Exact codes: where dense search fails and BM25 does not

The four exact-code questions, on the winner's chunking, with each search on its own (no fusion, no reranker):

| Question | Dense: rank of the gold source | BM25: rank of the gold source |
|---|---:|---:|
| Q-0412 "What does ERR-PO-0412 mean and how do I fix it?" | 3 | 1 |
| Q-705 "What does ERR-SUP-0118 mean?" | not in the top 10 | 6 |
| Q-703 "What does ERR-PO-0610 mean?" | not in the top 10 | 7 |
| Q-711 "What does ERR-SEC-0001 say?" | not in the top 10 | 2 |

**Q-711, "What does ERR-SEC-0001 say?"** Gold source: MAN-ERR-72 (Message and Error Code Reference) v7.2.3, p.23.

| Rank | Dense (`bge-small`) | BM25 |
|---:|---|---|
| 1 | MAN-SAL-72 v7.2.3, p.7, § Questions users ask | Ledgerline_7.2_tables_and_fields.xlsx, Error codes rows 209-227 |
| 2 | MAN-SAL-72 v7.2.3, pp.36-37, § Questions users ask | **MAN-ERR-72 v7.2.3, p.23, § ERR-SEC-0001 ACCESS DENIED** (gold) |
| 3 | MAN-AP-72 v7.2.3, p.64, § ERR-TAX-0001 | svc:po_approve, § request.fields |

Dense search reads the question for its meaning, "an error message and what it says", and returns passages that are
about error messages in general: the sales manual's FAQ and a different code, ERR-TAX-0001. To an embedding model every
ERR-code looks alike. BM25's tokenizer keeps `ERR-SEC-0001` whole as one search word (and adds its parts), so the one
page that contains exactly that code scores high. Dense misses 3 of the 4 code questions entirely; BM25 finds all 4 in
its top 10. This is why the winner keeps BM25 in a hybrid, and the reranker then lifts all four gold sources into the
top 5 (the winner's exact-code recall@5 is 1.00).

## 6. Sensitivity check, after the grid: BM25's k1 and b

The grid used BM25's textbook settings everywhere: **k1 = 1.2** (how fast repeated words stop counting) and
**b = 0.75** (how strongly long chunks are scaled down). After the grid I varied both on the winner's chunking
(structured, structure-aware, 400 tokens): k1 ∈ {0.6, 0.9, 1.2, 1.5, 2.0} × b ∈ {0.3, 0.5, 0.75, 0.9, 1.0},
25 settings, each scored for BM25 on its own and for the full winning pipeline (50 runs, 3.4 minutes, cell
A3 · Part 2 · 6).

**Decision rule, fixed before the check ran:** keep k1 = 1.2, b = 0.75 unless a setting raises the winning
pipeline's recall@5 by at least two questions (2 / 33 = 0.061) with search p95 still ≤ 200 ms.

**BM25 on its own**: recall@5 (MRR); rows are k1, columns are b.

| k1 \ b | 0.3 | 0.5 | 0.75 | 0.9 | 1.0 |
|---:|---:|---:|---:|---:|---:|
| 0.6 | 0.788 (0.583) | 0.788 (0.581) | 0.788 (0.554) | 0.727 (0.530) | 0.727 (0.540) |
| 0.9 | 0.849 (0.570) | 0.788 (0.582) | 0.727 (0.543) | 0.667 (0.530) | 0.667 (0.543) |
| 1.2 | 0.818 (0.586) | 0.758 (0.588) | 0.697 (0.541) | 0.667 (0.548) | 0.667 (0.544) |
| 1.5 | 0.818 (0.591) | 0.788 (0.604) | 0.697 (0.556) | 0.667 (0.566) | 0.667 (0.564) |
| 2.0 | 0.818 (0.606) | 0.788 (0.616) | 0.697 (0.571) | 0.667 (0.572) | 0.667 (0.562) |

**The winning pipeline (hybrid + reranker)**: recall@5 (MRR); rows are k1, columns are b.

| k1 \ b | 0.3 | 0.5 | 0.75 | 0.9 | 1.0 |
|---:|---:|---:|---:|---:|---:|
| 0.6 | 0.909 (0.761) | 0.909 (0.761) | 0.909 (0.761) | 0.879 (0.736) | 0.909 (0.717) |
| 0.9 | 0.909 (0.761) | 0.909 (0.761) | 0.909 (0.761) | 0.909 (0.761) | 0.909 (0.717) |
| 1.2 | 0.909 (0.741) | 0.909 (0.741) | 0.909 (0.761) | 0.909 (0.736) | 0.909 (0.711) |
| 1.5 | 0.909 (0.741) | 0.909 (0.736) | 0.909 (0.736) | 0.939 (0.742) | 0.939 (0.718) |
| 2.0 | 0.879 (0.726) | 0.909 (0.741) | 0.939 (0.742) | 0.939 (0.742) | 0.909 (0.717) |

What it shows:

- **BM25 on its own gains a lot from a lower b.** Default: recall@5 0.697. Best: k1 0.9, b 0.3, recall@5 **0.849**,
  five questions more, still at 0.2 ms. The pattern holds for every k1: b = 0.3 is never below 0.788, b ≥ 0.9 never
  above 0.727. A high b scales long chunks down hard, and in this corpus the answers often sit in long chunks (a full
  manual or policy section), competing with short ones (a single YAML service, a short e-mail) that mention a
  question word once. Scaling length down less lets the long, relevant sections through. That is also the best
  configuration without a reranker anywhere in this work (the grid's best was 0.788).
- **In the full pipeline the effect disappears.** Almost every setting gives 0.909; the best, k1 1.5 and b 0.9,
  gives 0.939, one question more (Q-615 moves from rank 6 to 5) and one question's gold source drops from rank 1 to 3
  (Q-322), so its MRR is lower (0.742 vs 0.761). The best setting even points the other way (higher b). The reranker
  re-reads the top 20 of the fused list, so what matters is only whether the gold passage reaches those 20, not its
  exact BM25 rank, and with dense search in the mix it nearly always does.
- **Decision: keep k1 = 1.2, b = 0.75.** No setting is two questions better for the winning pipeline; +1 question on
  33 is within noise. The run with the defaults reproduced the grid's winner exactly (0.909).
- **The lesson:** tuning one part on its own (+5 questions for BM25) can look like a big win and still change nothing
  in the full system. A setting has to be measured in the pipeline that will ship. The tuned BM25 is still worth
  knowing: if the 139 ms of the reranker ever became too slow, BM25 alone with b = 0.3 gives 0.849 in under a
  millisecond.

## 7. Limitations

**1. Chunks longer than the models can read.** `bge-small` (the embedding model) and `bge-reranker-base` (the
reranker) read at most 512 of their own tokens; the reranker's 512 also include the question. Counted with each
model's own tokenizer on my chunks (the median question is 12 reranker tokens):

| Chunking | Chunks | Cut by the embedding model | Text it never reads | Cut by the reranker | Text it never reads |
|---|---:|---:|---:|---:|---:|
| structured · structure-aware · 200 | 28,953 | 0.0% | 0.0% | 0.0% | 0.0% |
| structured · structure-aware · 400 (the winner) | 13,734 | 3.3% | 0.2% | 9.1% | 0.5% |
| structured · structure-aware · 800 | 6,853 | 87.1% | 37.9% | 89.0% | 39.2% |

So the 800-token configurations were not tested on equal terms: dense search and the reranker never saw about 38%
of their text. Truncation is not the whole reason long chunks do worse, though. In the lecture's own grid
(`experiments/logs/rag_grid.json`), `nomic`, an embedding model that reads 2,048 tokens and so is not truncated at
800, still loses recall as chunks grow (dense recall@5 0.659 at 200, 0.600 at 400, 0.571 at 800): one vector has to
stand for a longer passage, and the answer becomes a smaller part of it. The fair conclusion is narrower than "800
is too big": **with these two models, a chunk must fit in 512 of their tokens**, and longer chunks are also diluted.
The winner's 400-token chunks are essentially unaffected (under 1% of their text is cut).

**2. The golden set does not list every correct source.** Recall counts a hit only when a retrieved passage comes
from a source the golden set labels as gold. For Q-711 ("What does ERR-SEC-0001 say?") BM25's first result was the
data dictionary's error-code table (`07_data_dictionary/Ledgerline_7.2_tables_and_fields.xlsx`, sheet Error codes);
its row 215 reads `ERR-SEC-0001 | ACCESS DENIED`, exactly the fact the answer must contain, but only MAN-ERR-72 p.23
is gold, so that passage counts as a miss. Part 1 showed the same with Q-402, where Voltway's e-mails state the new
£119.00 price but only the rate-contract row is gold. Recall therefore measures "found the labelled source", which
can understate a configuration that finds an equally good one. The golden set is the course's
(`eval/questions.jsonl`); I report against it as given.

## 8. How it was run

- Cells A3 · Part 2 · 1 to 6 in the notebook, after NB3 section 7. The grid builds one chunking at a time (chunk, embed
  into Chroma, run its 6 searches on the 40 questions), saves after every configuration and resumes if interrupted.
  Indexes are kept outside the submission folder.
- Building an index took 19 to 60 s per chunking on the RTX 3060 (embedding 12 to 34 s, adding to Chroma 4 to 16 s).
- Running locally on Windows needed two fixes, both in the notebook's "A3 · Running locally" cell: file paths are
  turned into forward slashes (the course code produced back-slashes, which matched no gold source and left the HR
  folder unflagged), and Git is told not to change line endings when cloning the dump. With both, the local structured
  parse gives 51,325 units and 4,644,607 tokens, one token fewer than the Colab run in Part 1 (4,644,608); the
  difference is the local Tesseract version reading one scanned page slightly differently.
