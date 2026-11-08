# A3 · Part 4 · The race

Every number here comes from section "A3 · Part 4" of my notebook (`A3_harman.ipynb`, cells 1 to 3). Search ran locally; the answer model, the judge and the wiki's navigation are
Gemini 3.8 Flash through Google's endpoint, costed at $0.825 / $4.125 per million input / output tokens. Almost every
call was live: the wiki's answers for Q-610 and Q-213 and 4 of its judge verdicts replayed from Part 3 (same prompt,
same reply), and everything else was called for this race. Per-question records are in `logs/part4_rag.json` and
`logs/part4_wiki.json`, the summary in `logs/part4_summary.json`.

## 1. How the race was run

Both methods answer the same 40 questions (my golden subset from Part 2, 4 of each of the 10 types) through the course's
race harness, `evaluate.run`. Two things differ: how each method finds passages, and **what it can see**. RAG searches
all 693 files of the dump. The wiki was built from 50 of them (`01_policies` and `02_procedures`, Part 3), and those 50
hold every gold source of only 13 of the 33 questions that should be answered. So this race compares the two systems
as built, not the two methods on equal documents. Section 4 separates the two effects, and section 9 adds the
lecture's wiki of the whole dump on the same questions.

| | RAG | Wiki |
|---|---|---|
| Documents | all 693 files | 50 files (`01_policies`, `02_procedures`): all gold sources for 13 of the 33 answerable questions, some for 6 more, none for 14 |
| Retrieval | the Part 2 winner: structured parser, structure-aware 400-token chunks, hybrid search (BM25 + `bge-small`), reranked by `bge-reranker-base`, top 10, permission filter before ranking; the real index (13,734 chunks) | navigation over my 119-page wiki (Part 3): the model reads `index.md`, opens pages, follows `[[links]]` and may open a raw source; at most 4 turns, as in the lecture's race |
| Answer step | the course's answer prompt, Gemini 3.8 Flash, 250-word cap, 9,000 characters per source | same |
| Withheld notice | when a confidential HR document would have matched (the course's detector, decided once): Q-904, Q-903 and Q-002 | same three questions |
| Scoring | the course's LLM judge (answer correct), exact-fact check (with the HR leak check), citation check | same |
| Timing | search timed one question at a time on this machine; time to answer = search + answer model | same; the wiki's search time includes its navigation calls |

## 2. Results

| Metric | Target (AUDIT.md) | RAG | Wiki |
|---|---|---:|---:|
| **Answer correct** (LLM judge) | ≥ 90% | **87.5%** (35/40) | 57.5% (23/40) |
| Exact-fact check | report | 85.0% | 57.5% |
| **Citation correct** | ≥ 95% | **100%** | 45.5% |
| **Confidential leaks** | 0 | **0** | **0** |
| Retrieval recall@5 / @10 / MRR | ≥ 90% at 5 | 90.9% / 97.0% / 0.761 | 51.5% / 51.5% / 0.450 |
| **Search** p50 / p95 | p95 ≤ 200 ms | **139 / 149 ms** | 7,906 / 12,993 ms |
| **Time to answer** p50 / p95 | p95 ≤ 4 s | 6.2 / **13.8 s** | 13.2 / 21.5 s |
| Cost per question | report | **$0.0062** | $0.0210 ($0.0154 navigation + $0.0056 answer) |
| Tokens per question, in / out | report | 4,022 / 704 | 22,011 / 683 |

Notes on reading the table:
- These are results for the two systems as built, on unequal documents (section 1). On the 13 questions whose gold
  sources are all inside the wiki's 50 files, RAG gets 12 and the wiki 11 (section 4). On all 40, the lecture's wiki of
  the whole dump gets 32 against its RAG's 35 (section 9).
- The judge and the exact-fact check agree on 92.5% of RAG's answers and 90% of the wiki's (Cohen's kappa 0.68 and
  0.80).
- The wiki's recall counts a page as a hit when the page cites a gold source anywhere in its references, so it is
  not directly comparable with RAG's passage-level recall.
- Citation correct counts a question when at least one cited passage holds a gold fact or sits at a gold location.

## 3. By question type

Each type has 4 questions, so one question moves a cell by 25 points. The column "In the wiki's files" says, for each
type, how many of its 4 questions have all their gold sources inside the wiki's 50 files (in brackets: how many have
only some). The wiki had what it needed for rules, most procedures and version conflicts, and some single lookups. It
had no gold source for service / field, table lookup and exact-code questions (the 2 service / field questions and 1
table lookup it got right were answered from policy or SOP text that holds the same fact but is not listed as gold), only part
of what each multi-hop question needs, and nothing to look up for not-in-the-documents and refused permission questions, which have no gold source.

| Type | In the wiki's files | RAG answer correct | Wiki answer correct | RAG time p50 | Wiki time p50 |
|---|---:|---:|---:|---:|---:|
| single lookup | 2 (+1 partly) | 100% | 75% | 4.0 s | 9.6 s |
| procedure | 3 | 100% | 50% | 7.7 s | 16.7 s |
| rule | 4 | 100% | 100% | 4.8 s | 9.5 s |
| service / field | 0 | 100% | 50% | 4.5 s | 13.6 s |
| table lookup | 0 | 100% | 25% | 6.2 s | 13.9 s |
| multi-hop | 0 (+4 partly) | 25% | 25% | 9.9 s | 17.2 s |
| version conflict | 3 (+1 partly) | 75% | 75% | 7.4 s | 13.3 s |
| exact code | 0 | 100% | 0% | 7.9 s | 12.6 s |
| not in the documents | no gold source | 100% | 100% | 4.4 s | 13.2 s |
| permission | 1 (3 to refuse) | 75% | 75% | 7.2 s | 15.4 s |

## 4. Why the wiki loses: mostly scope

My wiki covers two folders (`01_policies`, `02_procedures`). Of the 33 questions that should be answered, only 13 have
all their gold sources inside them.

| Answerable questions | n | RAG | Wiki |
|---|---:|---:|---:|
| Gold sources all inside the wiki's 50 files | 13 | 12/13 | 11/13 |
| Gold sources partly or wholly outside them | 20 | 17/20 | 6/20 |

The wiki got 17 questions wrong. They fall into three groups:

- **14 are scope.** They need the manuals, service definitions, master data or e-mails that this wiki does not
  cover.
  - On these the wiki usually said "not in the documents", which is the honest answer for what it holds.
  - Its 4 exact-code misses are the clearest case. Its error pages come only from what the SOPs say about each code;
    the exact message text sits in the manuals. For Q-0412 it explained the error correctly but without the exact
    wording "TAX CODE DOES NOT MATCH SUPPLIER COUNTRY", which the check requires.
- **2 are navigation failures inside the scope.**
  - **Q-110** ("How do I raise a purchase request?"): the model's first navigation reply had one extra closing brace.
    The course's parser could not read it and treated it as "done", so no page was opened and the answer was "not
    in the documents". This was 1 of the 117 navigation replies in the race.
  - **Q-615** ("Did chargers always need UN 38.3?"): the navigation opened the supplier policy, its amendment and the
    certificate SOP, and stopped. The history it needed (Purchase Policy v3.0 exempted chargers) is on
    `pol-pur-001`'s *Versions and conflicts*, which it did not open.
- **1 is the same as RAG's miss.** Q-906 ("What percentage bonus can purchasing get?") should be refused as
  confidential. The withheld detector did not fire for it, so both methods said "not in the documents" instead.

Inside its scope the wiki is close to RAG (11/13 against 12/13), but it takes about twice as long and costs about three
times as much per question.

## 5. Decision: RAG ships

Measured against the targets I set in Part 1:

| Target | RAG | Wiki |
|---|---|---|
| Answer correct ≥ 90% | missed by one question (87.5%) | missed (57.5%) |
| Citation correct ≥ 95% | **met** (100%) | missed (45.5%) |
| Leaks = 0 | **met** | **met** |
| Recall@5 ≥ 90% | **met** (90.9%) | missed (51.5%) |
| Search p95 ≤ 200 ms | **met** (149 ms) | missed (13.0 s) |
| Time to answer p95 ≤ 4 s | missed (13.8 s) | missed (21.5 s) |

**RAG ships.** It meets four of the six targets; the wiki meets one.
- On latency, which weighs most for Emma (AUDIT.md section 3), RAG's search is 87 times faster at p95. Its answer
  arrives in half the time, 6.2 s against 13.2 s at p50. This gap does not come from coverage: a wiki of the whole
  dump is slower still (the lecture's took 28.8 s at p95 on these 40 questions, mine 21.5 s).
- It costs a third as much per question.
- It is correct on 12 more questions, but 11 of those 12 are questions whose answers sit outside the wiki's 50 files
  (17/20 against 6/20). Inside them the gap is one question (12/13 against 11/13), and on the 7 questions that should
  be refused or answered "not in the documents" the two tie (6/7 each). So accuracy here mostly measures what each
  system can see. The decision rests on latency and cost, which do not depend on it.
- Neither method meets the 4-second answer target. RAG's search takes 0.15 s, so almost all of its 6–14 s is the
  answer model writing up to 250 words. Meeting 4 s would need a faster answer model or shorter answers, not a
  different retrieval method.

## 6. Where the loser wins

Three types are entirely outside the wiki's 50 files on my questions: service / field, table lookup and exact code
(0 of 4 each have a gold source inside them). Multi-hop questions all need at least one file outside them. The wiki's
low scores on these types measure missing documents, not the method. On the other types, **the wiki does not win any
outright**: it ties RAG on rule, version conflict, not-in-the-documents and permission, and loses single lookup and
procedure by one and two questions.

It does win two single questions that RAG gets wrong. Both are the kind of question the wiki is built for: a rule
and its later change, written together on one page.
- **Q-618, version conflict** ("How long do I have to submit an expense claim?").
  - RAG's top 10 held the not-yet-in-force T&E Policy v3.0 (45 days) at rank 1 and one passage of the current v2.4
    at rank 9. The answer said the current deadline was not in the documents and gave only the future 45-day rule.
  - The wiki's `pol-tex-007` page holds both versions, today's rule first. So it answered "60 days today, 45 days
    from 1 January 2027", which is correct.
- **Q-510, multi-hop** ("Can I raise a direct order for £40,000 of brake pads next month?").
  - Both said yes for November.
  - Only the wiki added the change from 1 December and the error Ledgerline will then show (ERR-PO-0610), which the
    reference answer requires. Its navigation opened the amendment's page (`amd-pur-2026-03`) together with the
    purchase policy.

So the type where the loser's design wins is **version conflict**, together with multi-hop questions that turn on a
change in a rule. This matches the lecture, where the wiki won versions. With 4 questions per type, though, one
question is 25 points, and the 75% tie on version conflicts hides that each method lost a different question.

## 7. Is a cascade worth its latency?

I computed two cascades from the two runs, with no new model calls. The first method answers. If its answer says
"not in the documents", the second method is asked too, and the question's time and cost add up.

| Cascade | Answer correct | Time p50 / p95 | Cost per question | Questions passed on |
|---|---:|---:|---:|---:|
| RAG alone | 87.5% | 6.2 / 13.8 s | $0.0062 | — |
| **RAG, then wiki** | **90.0%** | 6.8 / 20.6 s | $0.0096 | 6 |
| Wiki, then RAG | 85.0% | 16.7 / 27.3 s | $0.0234 | 17 |

**RAG, then wiki** reaches the 90% target. Of the 6 questions it passes on:
- **1 gains:** Q-618, which the wiki answers correctly.
- 4 are not-in-the-documents questions, which RAG had already answered correctly. The wiki also abstains, so they only
  get slower.
- 1 is Q-906, which both methods get wrong.

The cost of that one extra correct answer:
- p95 rises from 13.8 to 20.6 s;
- 15% of all questions wait for both methods: 17 to 25 s each;
- the cost per question rises by half.

**It is not worth it as the default.** Latency is the metric I weighted most, and every "not in the documents"
answer, the case where the user most needs a quick "no", would go from about 5 s to 17–20 s. The cascade becomes
worth trying when one of two things changes:
- the wiki covers the whole dump, so that more of RAG's misses fall inside it;
- the escalation is narrowed to questions about versions or rule changes, rather than every abstention.

The lecture reached the same verdict on its own cascade.

## 8. Spend

| Step | Calls (live) | Cost |
|---|---:|---:|
| RAG: answers | 40 | $0.249 |
| RAG: judge | 40 | $0.038 |
| Wiki: navigation | 117 | $0.615 |
| Wiki: answers | 38 (+2 replayed) | $0.217 |
| Wiki: judge | 36 (+4 replayed) | $0.032 |
| **Part 4 total** | **271** | **$1.150** |

With Part 3 ($1.96) and Part 5 ($0.36, DOMAIN.md section 9), the total model spend for A3 is **$3.48**. The
line at the top of RAG.md states the total.

## 9. Calibration against the lecture's race

To check that my numbers are consistent with the lecture, I scored the lecture's recorded race on my 40 questions.
The per-question records are in the course repository, `lectures/L3-the-memory/experiments/logs/race_answers/`
(`rag__250n.json`, `wiki__250n.json`, `hybrid__250n.json`: 250-word answers, withheld notice on). They are the
lecture's results, recounted on my subset; I did not re-run them.

The two races differ in three ways:
- RAG: the lecture's is BM25 + reranker on 200-token chunks; mine is hybrid + reranker on 400-token chunks (the Part 2
  winner);
- wiki: the lecture's covers the whole dump (683 pages from 693 files); mine covers 50 files (119 pages);
- machine: a Modal L4 for the lecture, an RTX 3060 for mine.

| Method, on my 40 questions | Lecture's race | My race |
|---|---:|---:|
| RAG | 35/40 (87.5%) | 35/40 (87.5%) |
| Wiki navigation | 32/40 (80.0%) | 23/40 (57.5%) |
| Wiki hybrid (section search, then navigation) | 36/40 (90.0%) | not run |

| Wiki navigation, by where the gold sources are | All inside my 50 files (13 questions) | Partly or wholly outside (20) |
|---|---:|---:|
| Lecture's wiki (whole dump) | 12/13 | 14/20 |
| My wiki (50 files) | 11/13 | 6/20 |

**RAG.** Both RAGs score 35/40 on my questions, missing different ones:
- the lecture's misses Q-112 and Q-118;
- mine misses Q-510 and Q-618;
- both miss Q-EMMA, Q-505 and Q-906.

The lecture's 89.3% over all 224 questions is higher because of the question mix: my subset gives every type equal
weight, including four multi-hop questions, on which my RAG scores 1/4 and the lecture's 2/4.

**Wiki.** Most of the gap comes from coverage:
- **Inside my 50 files** the two wikis differ by one question, Q-110, which my run lost to a malformed navigation
  reply (section 4).
- **Outside them** the lecture's wiki has pages for the manuals, error codes, master data and e-mails; mine does not.
  This accounts for 8 of the 9 questions between 32 and 23.

**Latency and cost.** On the same 40 questions the lecture's wiki was slower and more expensive than mine:
- 28.8 s at p95 against 21.5 s;
- $0.033 against $0.021 per question;
- 35,779 against 22,011 input tokens per question.

This is consistent with navigating a much larger index. So a wiki of the whole dump would close most of the accuracy
gap, but widen the latency gap that decides section 5.

## 10. Limits of this race

- **Small sample.** 40 questions, 4 per type. Differences of one question per type are not meaningful, and the
  overall gap (35 against 23 correct) is the only difference I would rely on.
- **The wiki's scope.** It covers 50 of 693 files. A wiki of the whole dump, like the lecture's 683 pages, would
  answer many of the 14 scope misses. It would also cost more to build and take longer to navigate, because the
  index the model reads first would be about six times larger.
- **The judge is the answer model.** Both run on Gemini 3.8 Flash. The exact-fact check is the independent check,
  and it agrees with the judge on 90–92.5% of answers.
- **Time to answer includes the network.** It includes the round trip to Google's endpoint from my machine, so the
  answer-model share of the time depends on the network as well as the model.
