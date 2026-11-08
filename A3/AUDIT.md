# A3 · Part 1 · Audit and metrics

Corpus: `northbridge-docs` (github.com/RajatDandekar/northbridge-docs).
All numbers in this file come from the A3 Part 1 cells in my notebook (`A3_harman.ipynb`, section "A3 · Part 1"),
which reuse NB3's parsers (`ledgerline.course.l3.corpus`). No model was called for Audits: spend $0.00.

## 1. The audit

### How it was counted

- **Files:** every file in the repository except `.git/` and `eval/` (the course's answer key): **693**.
  The dump's own `eval/stats.json` says 697 because it counts differently; I count only what an assistant would be given.
- **PDF pages:** the page count of every PDF (pypdf), scans included.
- **Rows:** one per spreadsheet or CSV data row, as the structured parser reads it (title and header rows excluded).
- **Tokens:** **tiktoken `o200k_base`**, on the **structured parser's** text: every table row written as
  `column: value` pairs, e-mail headers decoded, the six scans read by OCR (Tesseract). One count per file, with the
  file's units joined by newlines. NB3 section 1 adds the units up one by one and gets 4,644,608 in my run; the 47,620 tokens
  between the two are mostly the newlines between a file's 51,325 units. I use the per-file count throughout.
- **Mess:** found by cell 1b from the documents themselves: file hashes, the parser's own flags (each document's
  status, effective date and folder), and a clause-by-clause comparison of every document that exists as more than
  one file. The cells never read `eval/messiness.json`, the dump's answer key.
- **Classes**, by file format: **structured** = XLSX, CSV; **semi-structured** = YAML, XML, WSDL, JSON, EDI, EML, HTML,
  MD; **unstructured** = PDF, DOCX, TXT.

### By folder

| Folder | Files | PDF pages | Rows | Tokens (o200k) | Share of tokens | Plain-parser tokens |
|---|---:|---:|---:|---:|---:|---:|
| (root) | 1 | 0 | 0 | 780 | 0.0% | 783 |
| 01_policies | 24 | 58 | 8 | 32,181 | 0.7% | 33,193 |
| 02_procedures | 26 | 116 | 0 | 55,512 | 1.2% | 58,921 |
| 03_ledgerline_manuals | 13 | 496 | 0 | 288,094 | 6.1% | 302,991 |
| 04_service_definitions | 405 | 0 | 400 | 162,467 | 3.5% | 155,669 |
| 05_master_data | 15 | 0 | 18,592 | 1,126,597 | 24.0% | 645,745 |
| 06_transactions | 26 | 483 | 25,353 | 2,892,604 | 61.6% | 2,009,767 |
| 07_data_dictionary | 4 | 27 | 1,188 | 43,306 | 0.9% | 25,982 |
| 08_release_notes | 18 | 53 | 9 | 29,125 | 0.6% | 30,865 |
| 09_email_archive | 79 | 0 | 0 | 19,419 | 0.4% | 26,772 |
| 10_meeting_notes | 32 | 0 | 0 | 19,268 | 0.4% | 18,675 |
| 11_training | 34 | 26 | 0 | 16,342 | 0.3% | 27,206 |
| 12_integrations | 10 | 8 | 7 | 5,999 | 0.1% | 6,615 |
| 99_scans | 6 | 6 | 0 | 534 | 0.0% | 0 |
| **Total** | **693** | **1,273** | **45,557** | **4,692,228** | 100% | **3,343,184** |

### By class

| Class | Files | Share of files | PDF pages | Rows | Tokens (o200k) | Share of tokens | Plain-parser tokens |
|---|---:|---:|---:|---:|---:|---:|---:|
| Structured (XLSX, CSV) | 27 | 3.9% | 0 | 45,557 | 3,262,429 | 69.5% | 1,914,476 |
| Semi-structured (YAML, XML, EML, HTML, MD …) | 521 | 75.2% | 0 | 0 | 179,398 | 3.8% | 200,339 |
| Unstructured (PDF, DOCX, TXT) | 145 | 20.9% | 1,273 | 0 | 1,250,401 | 26.6% | 1,228,369 |
| **Total** | **693** | 100% | **1,273** | **45,557** | **4,692,228** | 100% | **3,343,184** |

### What the counts say

- **Most files are text; most tokens are tables.** Semi-structured files are 75% of the files (405 service definitions
  and 79 e-mails) but under 4% of the tokens. The 27 spreadsheets and CSVs are 4% of the files and 69.5% of the tokens.
- **Two folders are 85.7% of the dump.** `06_transactions` (61.6%) and `05_master_data` (24.0%) are row data. Transaction
  rows answer analytical questions, not documentation questions, so most of the tokens are
  data that today's questions rarely need.
- **The structured parser costs 40.4% more tokens overall**: structured / plain = **1.404×** (4,692,228 against
  3,343,184; cell 1a), and all of that comes from
  tables: +74.5% in `05_master_data`, +66.7% in `07_data_dictionary`, +43.9% in `06_transactions`, because every row
  repeats its column names. In the text folders it is *smaller*: `11_training` −39.9% (no HTML markup) and
  `09_email_archive` −27.5% (no quoted-printable line breaks). This is because structured parser removed the junk that plain parser left. The scans go from 0 to 534 tokens with OCR.
- **The knowledge the documentation questions need is small.** Policies, procedures, manuals, release notes, e-mails,
  meeting notes and training together are about 460k tokens, under 10% of the dump.

### Three kinds of mess, each with a file

| Kind | File(s) | What is wrong | Why it hurts retrieval |
|---|---|---|---|
| **Superseded copy still on the share** | `01_policies/old/Purchase Policy v4.0.docx` next to `01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf` | Grouping files by document code finds 7 documents that exist as more than one file; POL-PUR-001 has three (v3.0 from 2019 and v4.0, both SUPERSEDED, and v4.1, current from 2026-04-01). Comparing v4.0 with v4.1 clause by clause finds the changes: §7.2 "Any order at a rate more than **5%** above the contract rate needs the manager's written reason" became **2%**; §6.2 added chargers to the lithium-cell rule; §6.4 is new. 14 files are flagged superseded: 9 say SUPERSEDED in their own text, 5 (`_legacy_6x/`, `old/` exports) are old only by their folder name. | Both versions use the same words, so a search can rank the old §7.2 first and the answer gives last year's tolerance. Even the current v4.1 contains "5%", in its revision table. Every chunk needs its version and status, and a status filter alone would miss the 5 files that are old only by folder. |
| **Byte-identical duplicate** | `01_policies/POL-SUP-003 Supplier Policy v2.3.pdf` and `01_policies/POL-SUP-003 Supplier Policy v2.3 (1).pdf` | The same file twice (identical SHA-1 hash), the "(1)" of a second download. | Every passage comes back twice and takes two of the top-5 slots, pushing a different gold source out. Deduplicate by hash at ingest, or treat both copies as one source when scoring. |
| **Image-only scans** | the 6 files in `99_scans/`, e.g. `99_scans/2019_Voltway_code_change_approval_signed.pdf` | Scanned paper with no text layer: the plain parser reads **0 tokens** from all six; OCR recovers 534 (74 to 132 per page; 74 for the Voltway approval). | Without OCR the facts on these pages (who signed the 1998 licence, the approval on PO/2026/00452) cannot be found at all. Questions Q-014, Q-015 and Q-019 depend on them. |

Also present, not counted in the three: three documents not yet in force (`AMD-PUR-2026-03` from 1 December 2026,
`POL-TEX-007 v3.0` from 1 January 2027, the `RN-7.3 PREVIEW`). The same clause comparison shows what the future
one would change: today's Travel and Expenses Policy v2.4 allows £140 a night outside London, £35 a day for meals
and claims within 60 days; v3.0 says £150, £40 and 45 days from 2027-01-01, so an answer that cites v3.0 today is
wrong. Also: four confidential HR files under
`01_policies/HR/CONFIDENTIAL/` that only HR may read; and inconsistent naming
(`02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx`,
`02_procedures/sop_inv_001_goods_receipt_v2.docx` against the `SOP-XXX-000 Title vN.pdf` convention).

## 2. Two parsers

The **plain** parser takes a file's text as it comes. The **structured** parser reads each format properly: e-mail
headers decoded, every spreadsheet row written as `column: value`, scans read by OCR, PDF sections and tables kept.
Same file, both parsers, from my run (NB3 section 2 and cell A3 · Part 1 · 2):

| File | Plain parser | Structured parser | What plain loses |
|---|---|---|---|
| `09_email_archive/2026/2026-10-22_Quotation Q-BE-26-0917 - Brightcell Energy.eml` | 310 tokens, starting with raw mail headers (`Message-ID`, `X-Mailer`, `Content-Transfer-Encoding: quoted-printable`) | 229 tokens: subject, sender and date, then the body ("£104.00 per pack, delivered (DAP)") | More tokens and less meaning: transport headers and quoted-printable line breaks instead of the message |
| `99_scans/2019_Voltway_code_change_approval_signed.pdf` | 0 tokens (image-only page) | 74 tokens by OCR: old code VC-EIN-0009 blocked, new code VC-EIN-0042, approved by G. Sutcliffe, 21/03/2019 (plus OCR noise from the signature, "we Vt") | Everything |
| `05_master_data/SUPPLIER_MASTER.xlsx`, sheet Suppliers, row 4 | `VC-EIN-0042 Voltway Cells NL859312774B01 NL Eindhoven ACTIVE N45 BAT …` | `sup_cd: VC-EIN-0042; name: Voltway Cells; vat_no: NL859312774B01; … pt_cd: N45; supplies: BAT; …` | The column names: nothing says that NL859312774B01 is the VAT number or N45 the payment terms |

### The example: a rate-contract row and the question it breaks

File: `05_master_data/Rate Contracts 2025-26 and 2026-27.xlsx`, sheet 2026-27, rows 1449 and 1450.
Question: **Q-402, "What is Voltway Cells' contract rate for BAT-500 now?"** Reference answer: £119.00, from
1 October 2026 to 31 March 2027 (it was £114.00 from April to September). The answer must contain `119.00`.

The two gold rows, as each parser writes them:

| Row | Plain parser | Structured parser |
|---|---|---|
| 1449 | `VC-EIN-0042/BAT-500/2026-04-01 VC-EIN-0042 BAT-500 114 2026-04-01 2026-09-30` | `line: VC-EIN-0042/BAT-500/2026-04-01; sup_cd: VC-EIN-0042; itm_cd: BAT-500; rate: 114.00; valid_from: 2026-04-01; valid_to: 2026-09-30` |
| 1450 | `VC-EIN-0042/BAT-500/2026-10-01 VC-EIN-0042 BAT-500 119 2026-10-01 2027-03-31` | `line: VC-EIN-0042/BAT-500/2026-10-01; sup_cd: VC-EIN-0042; itm_cd: BAT-500; rate: 119.00; valid_from: 2026-10-01; valid_to: 2027-03-31` |

What the plain parser loses, three times over:

1. **The fact itself.** Plain writes the cell as `119`, so the required fact `119.00` is not in its text at all
   (`'119.00' visible: False` for both rows). The structured parser formats money columns and keeps `rate: 119.00`.
2. **Which row is in force.** Plain gives two rows of bare numbers and two dates each. Nothing says which number is the
   rate or which date is "valid from" and which "valid to", so a reader (or a model) cannot tell that £119 applies
   today and £114 ended on 30 September. With `valid_from` / `valid_to` the answer is a comparison with today's date.
3. **Findability.** The same chunker (structure-aware, 200 tokens, 15% overlap) and the same BM25 over the whole dump,
   searched as Emma (HR excluded):

| Parse | Chunks | Rank of the first gold row |
|---|---:|---:|
| Plain | 19,634 | not in the top 50 |
| Structured | 28,953 | 11 |

Without column names the row shares almost no words with the question: no "rate", no "contract", not even
"Voltway" (only its code, VC-EIN-0042). With them, `rate:` and the context header (the file's title, "Rate Contracts") match.

**The question that fails:** Q-402. With the plain parser the gold row is never retrieved, and if it were, the answer
could neither contain `119.00` nor say which rate is current. It fails retrieval, the exact-fact check and the judge.

Two honest caveats, both from the same run:

- **Structured is better, not solved.** Rank 11 is outside the top 10 for BM25 alone. It is inside the top 20, so whether the reranker lifts it into the top 5 is a Part 2 measurement.
- **Both parsers rank e-mails first:** Voltway's "BAT-500 price from 1 October 2026" thread (4 copies: the original, a
  FW and two replies) shares the question's words. Those e-mails announce the new price but are not the contract, and
  in the structured run the four near-copies of one thread fill four of the top five slots. That is section 1's
  duplication problem in near-copy form, hurting retrieval directly.

## 3. My metrics

**My users** are Northbridge's purchasing and stores staff (Emma Clarke, purchase executive; Luis Moreno, senior
buyer; Daniel Okafor, purchase manager; Aiko Tanaka, stores), asking documentation questions: how to do something,
which rule applies, what a code or field means. **What I measure on** is the golden set in `eval/questions.jsonl`
(my run of NB3 section 3): 304 questions, of which 224 are documentation questions in ten types (single lookup 23,
procedure 20, rule 25, service/field 32, table lookup 34, multi-hop 21, version/conflict 20, exact code 27, not in
the documents 12, permission 10). Each has a reference answer, gold sources down to the page, section or sheet row,
and the strings a correct answer must contain. Parts 2 to 4 use my 40-question subset of it.

| Metric | How I measure it | Target |
|---|---|---|
| **Retrieval recall@5** | Share of questions with at least one gold source (same file, and the same page or sheet row where the gold source gives one) in the top 5 passages. Only questions that should be answered count: not-in-the-documents questions and refused permission questions are scored on the answer instead. | ≥ 90% |
| Recall@10, MRR | As above at 10; MRR = mean of 1 / rank of the first gold source | report |
| **Answer correct** | An LLM judge compares the answer with the reference answer (and the expected behaviour: answer, abstain or refuse); an exact-fact check confirms every `must_contain` string is in it. I report both and how often they agree. | ≥ 90% |
| **Citation correct** | Of the questions that should be answered: at least one cited passage contains a gold fact or sits at a gold location | ≥ 95% |
| **Confidential leaks** | Answers to a non-HR user that contain any value from `01_policies/HR/CONFIDENTIAL/` (the leak check in the exact-fact check) | **0**, with no exceptions |
| **Search latency** | Milliseconds from question to ranked passages, p50 and p95, timed one question at a time, every method on the same machine (one Colab runtime) | p95 ≤ 200 ms |
| **Time to answer** | Seconds from question to finished answer (search + answer model), p50 and p95 | p95 ≤ 4 s |
| Cost per question | Tokens in and out × the model's price (gemini-3.8-flash: $0.825 / $4.125 per million), including any model calls inside retrieval | report |
| Update cost | Time and $ to absorb one changed document: re-chunk and rebuild the index for RAG; pages rewritten and model calls for the wiki | report |

I added one target the lecture did not list as its own row: **zero confidential leaks**. Henrik's one explicit
condition was that nothing from the HR folder reaches anyone outside HR, so a single leak fails the system whatever
its accuracy. The other targets are the lecture's; I keep the 4 s answer target even though no method in the
lecture's race met it, because it comes from what Emma needs, not from what the model can do today.

**Why latency weighs this much.** Emma asks in the middle of her work, with a half-filled purchase order open in
Ledgerline and the supplier waiting on a quote, so every second of an answer is a second her task is stopped, and the
slow answer at p95 is the one she remembers. Search must stay a rounding error (≤ 200 ms) because it runs on every
question, and in Lecture 5's agents several times per task, where six searches at 5 s each would be half a minute
before the agent acts.

## 4. Paste-all

The simplest memory would be to paste every document into the prompt with each question. Against one model:

| | Tokens | Gemini 3.8 Flash's window (1,048,576) | The largest window listed (2,000,000) |
|---|---:|---:|---:|
| The whole dump | 4,692,228 | **4.5×** too big | 2.3× too big |
| Without `06_transactions` | 1,799,624 | 1.7× too big | fits |
| Without `05_master_data` and `06_transactions` | 673,027 | fits (64% of it) | fits |

Window sizes as NB3 section 4 gives them (OpenRouter's listing on 3 Nov 2026); my run of that cell, on NB3's own total
of 4,644,608, gives the same 4.4–4.5× and 2.3×.

**Input cost of one question, if the whole dump fitted:** 4,692,228 tokens × $0.825 per million = **$3.87**, before
a single output token (NB3's cell, on its total: $3.83). The model would re-read all 4.7 million tokens for every
question; nothing it read for the last question is kept.

Even the part that fits, the 673,027 tokens left without the master data and transactions, costs $0.56 of input per
question. At 224 questions a day (the size of the golden set, as an example) that is about $124 a day, and every
answer waits for the model to read two thirds of a million tokens. It would also lose every table-lookup answer,
which lives in the master data. Against the targets in section 3 (search p95 ≤ 200 ms, answer p95 ≤ 4 s), pasting
everything fails on fit, cost and latency at once. A big window is not a memory: the assistant has to find the few
passages that matter, which is what Parts 2 and 3 build.
