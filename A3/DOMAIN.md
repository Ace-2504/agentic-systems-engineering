# A3 · Part 5 · My domain: accounts payable at Northbridge Cycles (Pune)

Every number here comes from section "A3 · Part 5" of my notebook (`A3_harman.ipynb`, cells 1 to 5). The answer model
and the judge are Gemini 3.8 Flash through Google's endpoint; of the 24 calls behind section 6, 20 were live and 4
replayed an identical earlier call. Per-question records are in `logs/part5_run.json`; the grid and the exact-code
test are in `logs/part5_grid.json`.

## 1. The domain and the documents

The domain is my A1 capstone's: **Ask Northbridge for accounts payable** at Northbridge Cycles Pvt. Ltd., a bicycle and
e-bike maker in Pune. The users are Priya Shah (accounts payable), Emma Clarke (purchasing), Ganesh Pawar (stores),
Meera Kulkarni (tax manager), Vikram Nair (financial controller) and the Insurance desk. They ask about invoices,
holds, the payment run, GST and TDS.

**The documents and questions are invented, not real.** I have no real accounts payable documents I may share, so an
AI agent generated the set at my request (`domain/README.md`). It was modelled on the kinds of documents and questions
a real AP team has: each question records what real question it is modelled on. No real company, person or customer
data is used.

| | |
|---|---|
| Files | 41: 12 PDF (18 pages), 14 DOCX, 10 XLSX, 3 e-mails, 2 Markdown |
| Folders | policies, procedures, Ledgerline manuals, forms, master data, transactions, correspondence |
| Size | 9,731 o200k tokens after the structured parse; 51 chunks at 400 tokens |
| Confidential | 2 files in `01_policies/HR/CONFIDENTIAL/` (salary bands; bank mandate) |
| Today | Monday 9 November 2026 |

**The audit (rule 1)**, by folder and by class, with o200k tokens of the structured parse:

| Folder or class | Files | PDF pages | Spreadsheet rows | Tokens |
|---|---:|---:|---:|---:|
| 01_policies | 11 | 15 | 3 | 4,386 |
| 02_procedures | 11 | 0 | 0 | 1,492 |
| 03_ledgerline_manuals | 2 | 3 | 0 | 967 |
| 04_forms | 3 | 0 | 0 | 242 |
| 05_master_data | 8 | 0 | 48 | 1,670 |
| 06_transactions | 1 | 0 | 7 | 460 |
| 07_correspondence | 5 | 0 | 0 | 514 |
| structured (XLSX) | 10 | 0 | 58 | 2,242 |
| semi-structured (e-mail, Markdown) | 5 | 0 | 0 | 514 |
| unstructured (PDF, DOCX) | 26 | 18 | 0 | 6,975 |
| **all** | **41** | **18** | **58** | **9,731** |

The set contains six kinds of deliberate mess (`domain/mess.md`):
- an old policy version (POL-AP-001 v2.0, 3% price tolerance) beside the current one (v2.1, 2%), both marked
  "Approved";
- an e-mail lowering the large-payment limit from Rs.50,00,000 to Rs.25,00,000 from 1 December, which is not yet in
  force;
- two byte-identical copies of the Friday payment-run procedure;
- a file named `Final_FINAL_tax calendar Q3 (2) USE THIS.xlsx`;
- the confidential folder;
- a fact that exists only in one spreadsheet row.

**My checks before using it.** I checked the dataset independently with the course's own parser (structured), not
with the generator's checker:
- all 41 files parse;
- both confidential files are flagged confidential;
- every gold quote is found at the page, section or row its question names;
- every must-contain string is in its gold source;
- each planted mess is present in the parsed text. For example, v2.0 says 3% and v2.1 says 2%, and the two procedure
  copies are byte-identical.

## 2. The twelve rules

The twelve rules from Lecture 3, section 10 ("Twelve rules, in the order we used them"), and how Part 5 follows
each:

| # | Rule | How Part 5 follows it | Met? |
|---:|---|---|---|
| 1 | Audit the corpus: files, shapes, tokens, the mess. | Files, pages, rows and tokens by folder and class (section 1). Every planted mess checked with the parser. | Yes |
| 2 | Collect real questions and sort them: genesis, analytical, documentation. | 20 questions sorted (section 3), modelled on real ones and written the way their askers would type them. | Partly: no real users |
| 3 | Set metrics and targets with the users, latency included. | Targets set for accounts payable, with me standing in for the users (section 5). | Partly: no real users |
| 4 | Build a golden set from real questions, with gold sources. | 12 documentation questions with reference answers, each gold quote checked at its page, section or row (section 4). | Yes, with rule 2's limit |
| 5 | Parse by document type; never one reader for all. | The course's structured parser: PDF pages, DOCX sections, one unit per spreadsheet row, e-mail bodies. | Yes |
| 6 | Chunk by structure, small, with each document's header. | Structure-aware chunks; the header carries document, version, effective date and status. 400 tokens won the grid. | Yes |
| 7 | Pick an embedding model by measurement (domain models for medicine). | Four models measured on this domain: bge-small, bge-base, e5-small, gte-small (section 7). | Yes |
| 8 | Use BM25 or hybrid search wherever codes matter. | Every code in the documents searched on its own; this ruled out the dense-only configuration the grid first picked (section 7). | Yes |
| 9 | Filter by permission before ranking, and say what was withheld. | Confidential chunks are kept out of every non-HR search before ranking, and the "withheld" notice tells the model a restricted source exists. 0 leaks. | Yes |
| 10 | Handle versions and effective dates explicitly. | Effective dates are read in any written form; an older version still in force is marked superseded; out-of-date spreadsheet rows say so (`part5/domain_rules.py`). | Yes |
| 11 | Choose a wiki when synthesis across documents matters and the corpus changes slowly. | Considered and not chosen: 41 files, one multi-hop question in twelve, and the whole set fits in one prompt. | Yes (a decision) |
| 12 | Measure again after every change, in CI. | Re-measured on this domain (sections 6 and 7). `part5/check_retrieval.py` fails (exit code 1) if recall@5, the permission filter or the version marks regress, and runs without a key. | Partly: not yet wired into a CI service |

## 3. Twenty questions, sorted

The lecture sorts questions into genesis (make something), analytical (compute across records) and documentation
(answer from a document). The brief sets no split, so this set has 4, 4 and 12. Each question is written the way its
asker would type it, without the documents' own terms.

| Id | Asked by | Question | Category | Type |
|---|---|---|---|---|
| G-01 | Insurance desk | Draft the claim intimation to the insurer for the 260 Voltway packs damaged in transit. | genesis | |
| G-02 | Tax manager | Prepare October's TDS challan for my approval. | genesis | |
| G-03 | Purchasing | Draft my reply to Voltway saying we will pay invoice 4471 on the normal terms. | genesis | |
| G-04 | Accounts payable | Enter Voltway's credit note VC-CN-0071 for the 40 defective packs. | genesis | |
| A-01 | Financial controller | Is Voltway's 0.5% discount worth taking at Treasury's fixed-deposit rate, and at the cash-credit rate? | analytical | |
| A-02 | Tax manager | How much IGST credit on Voltway's invoice 4471 can we claim this month, after the defective credit note and the damaged packs? | analytical | |
| A-03 | Accounts payable | Which open invoices have been on hold for more than 3 days, and what is their total value? | analytical | |
| A-04 | Tax manager | How much have we bought from Voltway Cells this financial year, and how much of it is above the TDS threshold? | analytical | |
| D-01 | Insurance desk | need our insurance policy no. for the claim on stuff damaged on the way here, what is it? | documentation | single_lookup |
| D-02 | Stores | truck just came in and some of the battery packs are smashed. what do I need to do, and how fast? | documentation | procedure |
| D-03 | Accounts payable | can we set off the RCM on Saurashtra's freight bill against our ITC, or does it have to be paid? | documentation | rule |
| D-04 | Accounts payable | one supplier payment shows PK on the payments screen. is it going out in this friday's batch? | documentation | service_field |
| D-05 | Tax manager | do we have Saurashtra Roadways' no-TDS declaration on file? what's the number and when does it expire? | documentation | table_lookup |
| D-06 | Accounts payable | Pennine's bill PB-118 threw ERR-AP-0215 when I keyed it in. what's blocking it and whose sign-off clears it? | documentation | multi_hop |
| D-07 | Financial controller | from what amount do payments need my sign-off? | documentation | version_conflict |
| D-08 | Accounts payable | getting ERR-GST-0418 on a bill, what's that about? | documentation | exact_code |
| D-09 | Purchasing | if we pay Voltway Cells late, how much interest can they charge us? | documentation | not_in_docs |
| D-10 | Accounts payable | how much does an AP exec earn here? what's the pay range? | documentation | permission |
| D-11 | Accounts payable | how much over the PO rate can a supplier bill before the invoice gets stuck? | documentation | version_conflict |
| D-12 | Tax manager | at what point can we take input credit on a supplier bill? | documentation | rule |

The documentation questions cover all ten of the lecture's types: one each, plus a second rule and a second
version_conflict.

## 4. The golden set: reference answers and gold sources

All 12 documentation questions have a reference answer and a gold source (`part5/golden_v2.jsonl`). The dataset gave
D-01 to D-10; I wrote D-11 and D-12 from the documents. Every gold quote was checked with the parser at the page,
section or row it names.

| Id | Type | Reference answer (short) | Gold source |
|---|---|---|---|
| D-01 | single_lookup | TRN-2026-08812 | POL-INS-002 v1.0, p.1, § 1.2 |
| D-02 | procedure | Record the damage with photos and the driver's signed remark, keep the goods aside for the surveyor; the Insurance desk notifies the insurer within 24 hours of delivery and the transporter within 7 days | PRC-INS-01, § Steps |
| D-03 | rule | No: reverse-charge GST is paid in cash only (CGST Act s.49(4)), then claimed back as credit | POL-TAX-007 v1.0, p.1, § 2.1 |
| D-04 | service_field | No: PK means parked, not in the run | LL-AP Payables User Manual v4.2, p.2, § 5.2 |
| D-05 | table_lookup | DEC-SR-2026-014, valid until 31 March 2027 | Vendor Master.xlsx, Vendors, row 6 |
| D-06 | multi_hop | Quantity hold H-QTY; released by stores (Ganesh Pawar) or the financial controller | LL-ERR v4.0, p.1, § 2 **and** POL-AP-001 v2.1, p.1, § 4.1 |
| D-07 | version_conflict | Rs.50,00,000 today; Rs.25,00,000 from 1 December 2026 | POL-PAY-003 v1.4, p.1, § 3.2 **and** the 2 November e-mail |
| D-08 | exact_code | IRN not found or cancelled; input tax credit not booked; refer to the tax manager | LL-ERR v4.0, p.1, § 3 |
| D-09 | not_in_docs | Not in the documents | (none) |
| D-10 | permission | Refuse: confidential, NBC-HR-CONF only | HR-CONF-003 (must not be shown) |
| D-11 | version_conflict | 2% (POL-AP-001 v2.1); v2.0's 3% is superseded | POL-AP-001 v2.1, p.1, § 3.1 |
| D-12 | rule | Only after the invoice appears in GSTR-2B and the goods are received; no valid IRN, no credit | POL-TAX-005 v1.2, p.1, § 2.1 |

## 5. Targets for accounts payable (rule 3)

AUDIT.md set its targets for the Northbridge dump. For this domain I set them as the capstone's designer, standing in
for the users I don't have:

| Metric | Target | Why |
|---|---|---|
| Retrieval recall@5 | ≥ 90% | as before |
| Answer correct | ≥ 90%, and every permission and payment-status answer right | the capstone's two never-events: nothing confidential leaks, and nothing is called paid or scheduled while it is parked or held |
| Citation correct | ≥ 95% | as before |
| Search p95 | ≤ 200 ms | as before; the configuration rule uses it |
| Time to answer p95 | ≤ 10 s | Priya asks while working through holds and the Friday run, not with a supplier waiting on the phone |

## 6. Results

The Part 4 winner, unchanged: structured parser, structure-aware 400-token chunks with 15% overlap, bge-small + BM25
hybrid search, reranked by bge-reranker-base, top 10, with the permission filter before ranking. Re-measured on this
domain (section 7), it is also the configuration this domain's own measurement picks. The 12 documentation questions
went through Part 4's harness (`evaluate.run`) with the same answer model, 250-word cap, judge, checks and withheld
notice.

**Recall@5 = 100% (10 of 10). Answer correct = 92% (11 of 12).**

| Metric | Target | Result | |
|---|---|---:|---|
| Retrieval recall@5 | ≥ 90% | 100% (10/10) | met |
| Recall@1 / @3, MRR | report | 70% / 90%, 0.82 | |
| Gold sources covered in the top 5 | report | 95% (D-06 found 1 of its 2) | |
| Answer correct (LLM judge) | ≥ 90% | 92% (11/12) | met |
| Payment-status (D-04) and permission (D-10) answers | all right | 2/2 | met |
| Exact-fact check | report | 92% (11/12); agrees with the judge on all 12 (kappa 1.0) | |
| Citation correct | ≥ 95% | 100% | met |
| Confidential leaks | 0 | 0 | met |
| Search p50 / p95 | p95 ≤ 200 ms | 135 / 145 ms | met |
| Time to answer p50 / p95 | p95 ≤ 10 s | 5.2 / 7.5 s | met |
| Cost per question | report | $0.0047 | |

| Id | Type | Gold rank | Answer | Note |
|---|---|---:|---|---|
| D-01 | single_lookup | 1 | ✓ | |
| D-02 | procedure | 1 | ✓ | every step, and both deadlines |
| D-03 | rule | 1 | ✓ | "RCM" and "ITC" found the reverse-charge policy |
| D-04 | service_field | 5 | ✓ | the hardest to find: "payments screen" and "batch" are not the manual's words; ranks 1 and 2 are the two identical copies of PRC-AP-03 |
| D-05 | table_lookup | 1 | ✓ | the fact is only in a spreadsheet row |
| D-06 | multi_hop | 2 | ✗ | see below |
| D-07 | version_conflict | 1 | ✓ | Rs.50,00,000 today, Rs.25,00,000 from 1 December |
| D-08 | exact_code | 1 | ✓ | |
| D-09 | not_in_docs | n/a | ✓ | "NOT IN THE DOCUMENTS", nothing invented |
| D-10 | permission | n/a | ✓ | refused and named NBC-HR-CONF; its only citation is the withheld notice; nothing leaked |
| D-11 | version_conflict | 2 | ✓ | 2%, and says v2.0's 3% is superseded; v2.0 was third in the results, labelled SUPERSEDED |
| D-12 | rule | 1 | ✓ | |

**The miss, D-06, is a multi-hop retrieval failure.** The question needs two documents: the error reference
(ERR-AP-0215 means hold H-QTY) and the AP policy (who releases H-QTY). Search found the first at rank 2, but the
policy's section 4.1 was not in the top 10. So the answer named the hold and said "ask stores", but not Ganesh Pawar
or the financial controller, and the judge and the exact check both marked it wrong. Recall@5 counts a question as
found when any one of its gold sources is found, so it shows 100% here. Coverage (95%) shows the gap. The lecture
found multi-hop hard for every method too. A fix would be to search again for the second hop: here, the hold code the
first answer returns.

## 7. Re-measuring retrieval on this domain (rules 5 to 8 and 12)

The Part 2 grid, re-run here as retrieval only: 54 configurations, all on the RTX 3060. The settings were:
- chunk size 200, 400 or 800;
- BM25, dense or hybrid search;
- four embedding models;
- the reranker on or off.

Each configuration was scored on the 10 questions with gold sources. The pick rule was fixed before the grid ran:
highest recall@5 with search p95 ≤ 200 ms; ties go to the higher MRR, then the lower p95.

**The users' wording makes retrieval hard.** Only 10 of the 54 configurations found a gold source for every question
in their top 5. D-04 ("payments screen", "batch") fell out of the top 5 in 34 of them, D-11 ("PO rate", "gets
stuck") in 24, and D-02 in 7.

| Setting | Value | Configurations | Median recall@5 | Median MRR |
|---|---|---:|---:|---:|
| Search | BM25 | 6 | 0.75 | 0.683 |
| | dense | 24 | 0.90 | 0.728 |
| | hybrid | 24 | 0.90 | 0.727 |
| Reranker | off | 27 | 0.80 | 0.623 |
| | on | 27 | 0.90 | **0.820** |
| Embedding | bge-small | 12 | 0.90 | 0.691 |
| | bge-base | 12 | 0.85 | 0.727 |
| | e5-small | 12 | 0.90 | 0.685 |
| | gte-small | 12 | 0.90 | 0.727 |
| Chunk size | 200 | 18 | 0.90 | 0.700 |
| | 400 | 18 | 0.95 | 0.727 |
| | 800 | 18 | 0.90 | 0.730 |

- **The reranker is the largest single gain:** median MRR from 0.62 to 0.82. Every configuration that reached 100%
  recall@5 with MRR above 0.8 uses it.
- **BM25 alone is weakest** (median recall@5 0.75). The users' words "RCM", "ITC", "sign-off" and "batch" are not the
  documents' words, so exact word matching misses them.
- **Embeddings (rule 7).** No model is best everywhere. gte-small has the best MRR with dense search and the reranker;
  bge-base is no better than bge-small.

The configurations that reached 100% recall@5:

| Configuration (structured, structure-aware, 15% overlap, top 10) | Recall@1 | MRR | Search p95 |
|---|---:|---:|---:|
| 400 tokens, gte-small, dense, reranker | 0.90 | 0.925 | 130 ms |
| 400 tokens, bge-small, dense, reranker | 0.80 | 0.875 | 130 ms |
| 400 tokens, e5-small, dense, reranker | 0.80 | 0.870 | 130 ms |
| 400 tokens, bge-base, dense, reranker | 0.70 | 0.825 | 129 ms |
| **400 tokens, bge-small, hybrid, reranker (the Part 4 winner)** | 0.70 | 0.820 | 128 ms |
| 400 tokens, bge-base, hybrid, reranker | 0.70 | 0.820 | 131 ms |
| 400 tokens, gte-small, hybrid, reranker | 0.70 | 0.820 | 134 ms |
| 200 tokens, gte-small, hybrid, no reranker | 0.60 | 0.723 | 16 ms |
| 400 tokens, gte-small, hybrid, no reranker | 0.50 | 0.662 | 17 ms |
| 400 tokens, gte-small, dense, no reranker | 0.40 | 0.598 | 16 ms |

**Rule 8 changed the pick.** By the rule, the grid first picked gte-small dense search with the reranker (MRR 0.925).
But only a few of the 10 questions contain a code, too few to show whether dense search finds codes. So cell 3
searched every code-like string in the staff documents on its own, as a user pastes it from a screen: 46 codes, such
as ERR-AP-0215, DEC-SR-2026-014 and VC-CN-0071. The decision rule was written into the cell before it ran.

| Configuration (400-token chunks, reranker) | Codes found in the top 5 | Missed |
|---|---:|---|
| BM25 alone; and every hybrid (bge-small, bge-base, e5-small, gte-small) | 46/46 | none |
| dense, bge-small | 45/46 | FY2026-27 |
| dense, bge-base | 45/46 | VC-CN-0071 |
| dense, gte-small (the grid's first pick) | 43/46 | CC-2290, FY2026-27, VC-CN-0071 |
| dense, e5-small | 42/46 | CC-CHG-0018, DEC-SR-2026-014, FY2026-27, PB-BRK-0031 |

Dense search alone misses codes that hybrid finds, so rule 8 applies, and the pick was redone among hybrid and BM25
configurations by the same rule. Three reranked hybrids tie on recall@5 (100%) and MRR (0.820). The last tie-break,
p95, picks bge-small hybrid, which is the Part 4 winner. The margin is 3 ms, which is noise, so any of the three would
do. The measurement on this domain therefore agrees with the configuration chosen on Northbridge, and section 6
reports it.

**At this size, sending the whole set with every question is also possible.** It is 9,731 tokens, under 1% of Gemini
3.8 Flash's window, about $0.008 of input per question against RAG's $0.0026. RAG pays off as the document set grows.

## 8. Which rules mattered most, and what is still not met

**Mattered most: rules 2 and 4, a golden set in the users' own words.** Every other measurement depends on it:
- only 10 of the 54 configurations found everything;
- BM25 alone is the weakest setting;
- the reranker is the largest gain.

These are facts about how users ask, not about the documents.

**Also decisive:**
- **Rule 8.** Without the code test, the grid's own rule would have shipped a dense-only configuration that misses 3
  of the 46 codes users paste.
- **Rule 9.** D-10's refusal rests on the withheld notice. Its single citation is the notice, and NBC-HR-CONF, the
  group it names, appears in no staff document. The filter kept both confidential files out of every non-HR search.
- **Rule 10.** v2.0 of the AP policy reached the model labelled "SUPERSEDED", and D-11 says the 3% no longer applies.
  The v2.1 page also says "supersedes v2.0" in its revision history, so this run does not show the label alone made
  the difference.
- **Rule 12.** Re-measuring here is what showed the reranker's value on users' wording, and the dense pick's blind
  spot for codes.

**Still not fully met:**
- **Rules 2 and 3 need real users.** The questions are invented and their wording is mine. The targets are set by me
  as the capstone's designer, not agreed with an AP team.
- **Rule 12 says "in CI".** `part5/check_retrieval.py` is ready for that: it runs without a key, takes about 25
  seconds, and exits with 1 on a regression. It is not yet wired into a CI service.

The golden set is also small (10 questions scored for recall), and the configuration was picked on the same questions
it is reported on, as in Part 2. One multi-hop question in twelve is not enough to measure multi-hop, which is where
the one miss happened.

## 9. How it was run, and the spend

| Cell | What it does | Model calls |
|---|---|---|
| 1 | Checks, the audit, versions and dates, the 12-question golden set | none |
| 2 | The 54-configuration grid | none |
| 3 | The 46-code test and the rule-8 decision | none |
| 4 | The 12 questions through Part 4's harness on the picked configuration | 24 |
| 5 | `part5/check_retrieval.py` in a fresh process: all checks pass, exit code 0 | none |

Changes to the course's harness for this domain:
- **Answer prompt.** Its first two lines name this company and its date instead of Manchester and 26 October. The rest
  is the course's, word for word.
- **Roles.** Each asker is mapped to a role code, none of them HR.
- **Question reader.** The course's reader is replaced by one that reads this dataset.
- **Leak check.** It looks for the rupee amounts in the two confidential files.

**Part 5 spend: US$0.364**, summed from the recorded calls (`cassettes/A3_domain_*`): 65 answer calls ($0.306) and
62 judge verdicts ($0.058). Of that:
- the run in section 6 cost **$0.054**;
- **$0.310** went on earlier runs of this part, which this report replaces.

With Parts 3 and 4, the **total for A3 is US$3.48**, $0.48 over the brief's $3 cap (see the line at the top of RAG.md).
