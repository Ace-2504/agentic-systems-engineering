# A3 · Part 3 · A mini LLM Wiki

Every number here comes from section "A3 · Part 3" of my notebook (`A3_harman.ipynb`, cells 0 to 8). Every model call was first made **live**: Gemini 3.8 Flash through Google's endpoint. Each call is recorded in
`cassettes/`, so a rerun of the notebook replays it for free. Replayed calls in the notebook: the full ingest's 4 calls that the pilot
had already made, 116 of the lint's 118 review calls, and the 2 calls of the fixes (section 6 says where each was
first paid for). Part 3 spent **$1.96** in total.

The wiki is in `wiki/`: the schema `AGENTS.md`, `pages/` (staff), `restricted/` (HR only), `index.md`,
`restricted/index.md` and `log.md`. Logs of the queries, the lint and the update are in `logs/`.

## 1. The schema

`wiki/AGENTS.md` is my own. It follows Karpathy's three layers: the raw sources (never edited), the wiki (written by
the model) and the schema (written by me). It sets:

- **Scope:** `01_policies` and `02_procedures`, 50 files. A question that needs another folder gets "this wiki does
  not cover it". A document outside the scope that an in-scope source mentions (a manual such as MAN-PUR-72, a release
  note, a service, a meeting) gets no page: it is named by its code in the text, without a link.
- **11 page types:** policy, procedure, screen, error, supplier, item-family, role, person, data-source, topic, answer.
  A **slug** is built from the record's own code wherever one exists (`pol-pur-001`, `err-po-0412`,
  `screen-pur-po-01`, `user-eclarke`), so every source that names a thing lands on the same page. Confidential HR
  documents get `hr-` slugs.
- **The sections each type must have.** For example, a policy has *Clauses* in its own numbering and *Who it
  applies to*; a procedure has *Steps*, *Forms and screens*, *Checks and approvals*. Every page also has front matter
  (title, type, summary, audience, sources, status, dates), a lead, an infobox, *Versions and conflicts* when sources
  disagree, and *See also*.
- **Citations:** every sentence that states a fact ends with `[^rN]`. The build turns each key into one raw location
  (file, page and section heading for a PDF; sheet and row for a spreadsheet). A citation always points to a raw
  source, never to another wiki page.
- **Versions:** the rule in force on 26 Oct 2026 is written first. A newer version or amendment replaces the older
  text; byte-identical copies count as one source; superseded and future rules stay visible, with their dates.
- **Permissions:** facts from `01_policies/HR/CONFIDENTIAL/` go only on `audience: hr` pages. These are listed in
  `restricted/index.md`, never in `index.md`, and never linked from staff pages.

## 2. Ingest

The course's wiki code (`wiki_build`) did the ingest, with my `AGENTS.md` in place of the course's schema. It reads
each source once, collects facts (each with a quote that code checks against the source), writes each page from its
facts, then builds `index.md` and `log.md`. Before it could run on Windows, I fixed two problems (notebook cell 0):

- **Back-slash file paths.** The HR folder would not be recognised, and salary facts would have landed on
  staff pages. The cell checks that exactly 4 HR files are flagged before anything is spent.
- **Text encoding.** Page files would be written in Windows' old encoding, which cannot hold → or ≤.

I ran a 3-file pilot first ($0.13, 18 calls, 14 pages, in a scratch folder) to estimate the cost. Then I ran the full
ingest of all 50 files.

| | Result |
|---|---:|
| Sources ingested | 50 (41 current, 6 superseded, 2 not yet in force, 1 byte-identical copy) |
| Pages | **118** at the build; 119 after the lint fixes in section 4 |
| Pages by type | 29 screen · 23 procedure · 23 error · 17 policy · 13 person · 5 role · 4 supplier · 2 item-family · 1 data-source · 1 topic |
| Staff / HR pages | 114 / 4 (115 / 4 after the fixes) |
| Links between pages | **496**, every one to a page that exists (500 after the fixes) |
| References (`[^rN]` used in pages) | **773** |
| Facts collected | 838; the quotes of 830 (99.0%) were found word for word in the source |
| Pages with a *Versions and conflicts* entry | 37 |
| Words | 54,882 |
| `index.md` / `log.md` | one line per staff page, grouped by type / one line per ingested file, then every later operation |
| Model calls | **169**: 50 reads, 1 merge, 118 page writes. 165 were live; 4 replayed from the pilot |
| Tokens | 744,563 in, 219,040 out |
| Time | **244 s** wall clock: 33 s parse, 99 s read, 2 s merge, 110 s write (8 calls in parallel; 1,656 s of model time) |
| Cost | **$1.46** for the build, plus $0.13 for the pilot |

**What a page looks like.** `pages/pol-pur-001.md` keeps the policy's clauses in its own numbering. Its *Versions and
conflicts* section says:
- the direct-order limit is £50,000 today and drops to £25,000 from 1 Dec 2026 under AMD-PUR-2026-03;
- the contract-price tolerance is 2% today, where the superseded v4.0 said 5%;
- the UN 38.3 battery-safety certificate rule is wider than in v3.0.

Each claim has its own reference to a raw file and section.

## 3. Query by navigation

There were three questions, all from my 40-question golden subset (Part 2), so each answer could be checked against
the course's reference answer.
- **Navigation:** the course's `Navigator`. The model reads `index.md`, opens up to 3 pages a turn, follows
  `[[links]]` on the pages it has read, and stops when it has enough (at most 4 turns).
- **Answer:** the shared answer step that Part 4 also uses: the same prompt, model and 250-word cap.
- **Checks:** the course's fact check, its LLM judge and its citation check.

**Q-510 (multi-hop):** *"Can I raise a direct order for £40,000 of brake pads next month?"*

| Turn | What the model did |
|---|---|
| 0 | read `index.md` |
| 1 | opened `[[pol-pur-001]]` from the index, and `[[amd-pur-2026-03]]`, which is linked from it |
| 2 | followed links to `[[pol-apr-002]]` (linked from pol-pur-001) and `[[role-pur-exec]]` (linked from pol-apr-002) |
| 3 | done: "next month is November 2026 … permitted up to £50,000 gross" |

> Answer (abridged): Yes, you can raise a direct order for £40,000 next month (November 2026) [1][2]. Until 30 November
> 2026, direct purchase orders without a prior purchase request are permitted up to £50,000 gross value including VAT
> [1][2]. … From 1 December 2026, under amendment AMD-PUR-2026-03, the direct order limit drops to £25,000 or less; any
> direct order exceeding £25,000 gross raised on or after that date will be rejected with error ERR-PO-0610 [1][2].

The citations name wiki pages ([1] `pol-pur-001`, [2] `amd-pur-2026-03`, [3] `pol-apr-002`). Each page's references
lead to the raw text:
- the £50,000 limit: `POL-PUR-001_Purchase_Policy_v4.1.pdf`, p. 1, §3;
- the £25,000 limit: `AMD-PUR-2026-03_Amendment3_PurchasePolicy_DIRlimit.pdf`, p. 1, §1.

The judge marked it **correct**. The fact check passed, and the citation check passed: 2 of the 3 cited pages
contain a gold fact or cite a gold source, which is what the course's citation check counts. Cost: 3 navigation calls (12.0 s, $0.0156) plus the answer ($0.0100).

It is multi-hop because it needs two documents and a date. The policy gives today's limit; the amendment changes it
from 1 December; and "next month" has to be worked out as November.

**Q-610 (version conflict):** *"What hotel rate can I book in London?"*
The chain was: `index.md` → `[[pol-tex-007]]` → done (2 calls, 6.7 s, $0.0060 + $0.0032).

> Answer: Under the current Travel and Expenses Policy (POL-TEX-007 version 2.4), hotel room bookings in London are
> capped at up to £190 a night, including breakfast [1]. From 1 January 2027, under version 3.0, the cap increases to
> £210 a night, inclusive of breakfast and local taxes [1].

The two sentences trace back to `POL-TEX-007 … v2.4.pdf`, p. 2, §3 and `POL-TEX-007 … v3.0 (effective
2027-01-01).pdf`, p. 2, §3. The judge, fact check and citation check all passed.

One page was enough. The schema made the ingest put both versions on one page, today's rule first, so navigation
did not need to find the second document.

**Q-213 (rule):** *"Who approves an order above £5,000,000?"*
The chain was: `index.md` → `[[pol-apr-002]]` from the index, plus `[[pol-pur-001]]` and `[[role-plant-head]]`, both
linked from it → done (2 calls, 5.0 s, $0.0091 + $0.0046).

> Answer: A purchase order exceeding £5,000,000 gross triggers Ledgerline error ERR-APR-0009 and requires the Managing
> Director's written approval outside Ledgerline [1]. This approval is subsequently recorded by the plant head's
> office [1].

This traces back to `POL-APR-002 Approval Matrix v3.0.pdf`, §3 (p. 1). The judge, fact check and citation check all
passed.

**Summary:** 3 of 3 correct; 7 navigation calls, 23.7 s; $0.051 including answers and judging. Three questions show
how navigation works; they do not measure accuracy. Part 4 races both methods on all 40 questions.

## 4. Lint

The lint (notebook cell 4) ran on the wiki as the ingest built it, before any fix, in three passes:

1. **The course's code checks and the conflicts the ingest recorded.** These cost no model calls. They cover orphans,
   links to missing pages, quotes not found at the cited place, uncited paragraphs, duplicate and near-duplicate
   files, superseded and future-dated sources, naming, tables in PDFs, and confidential files.
2. **One check of my own:** an HR-only page built from a staff document.
3. **The course's LLM review on every page.** It is one model call per page, sending the page and up to 120 of the
   facts it was built from, with the course's own prompt (`wiki_lint.REVIEW`). The course's code reviews only pages
   whose sources disagree in date or status; I ran it on all 118 pages, staff and HR. Every reply could be read.

**Result:** 193 findings: 61 superseded, 44 tables in PDFs, 23 uncited, 18 future-dated, 16 duplicate, 7 near-duplicate,
5 citation not found, 5 naming, 4 orphan, 4 confidential, 3 contradiction, 1 legacy term, 1 rule not in policy, and
1 from my own check. 
By pass: 100 from the code checks, 72 recorded by the ingest, 20 from the review, 1 from my check.

**What the review added.** It flagged 13 of the 118 pages, with 20 findings:
- 8 duplicate: pages that cite both copies of the Supplier Policy;
- 8 superseded: older versions still present, such as Supplier Policy v2.2, Purchase Policy v4.0 and SOP-PUR-002 v1.3;
- 3 future-dated: AMD-PUR-2026-03, and POL-TEX-007 v3.0;
- 1 contradiction: POL-APR-002 §3.2 against §4.1, inside one document.

All 20 are about the sources, not mistakes on the pages. I checked the future-dated ones: `err-po-0610` says the error
"is not yet active" and starts on 1 December 2026, and `user-gwhitaker` lists POL-TEX-007 v3.0 as a future rule. The
review found no page that states a superseded or future rule as today's, and no contradiction between pages.

**Against the dump's planted problems.** I read `eval/messiness.json` only after the lint had run; it played no part
in choosing what to review. 13 of its 40 planted problems have all their files among my 50. The lint found **12 of
the 13** under the same kind (or family). It found the 13th only under another label: the AMD-SUP-2026-02 amendment
replacing POL-SUP-003 §4.4 was reported as "superseded", not "contradiction". The wiki pages handle it correctly:
`pol-sup-003` gives the amended 12-month rule as today's and keeps the old 24-month rule under *Versions and
conflicts*.

Five of the problems, and how each is fixed:

| # | Problem | Found by | Fix |
|---|---|---|---|
| 1 | **The IT Security Policy was hidden from staff.** `pol-its-008` sat in `restricted/`, titled "POL-ITS-008 README ACCESS". The cause is a bug in the course code (`wiki_sources.build_registry`): `HR/CONFIDENTIAL/README_ACCESS.txt` mentions POL-ITS-008 in its first lines, so the parser gave it that document code. The registry keeps the first file it meets for each code, and the README is listed before the real policy. So the page took the README's HR flag and title, and the README's 3 facts landed on it. Rajat's own `wiki_v4` has the same page with the same title. | my own check | **Fixed** (cell 5). In the code, a document code now takes its audience and title from the file whose own name carries the code. The page was rewritten as a staff page from the policy's own 8 facts, and the README's 3 facts went to a new HR page, `hr-readme-access` (2 calls, $0.01). The model repeated the infobox as plain lines under the new page's lead; cell 5 removes them. Staff can now open the policy, and it is in `index.md`. |
| 2 | **Contradiction inside POL-APR-002.** §3.2 says a document within the raiser's own limit is approved when submitted, with the raiser recorded as approver; §4.1 says nobody may approve a document they raised (ERR-APR-0003). | LLM review | Not a wiki error; the source disagrees with itself. The wiki should state both clauses under *Versions and conflicts* rather than pick one, and the document's owner (D. Okafor) should reword §3.2. The wiki then takes the fix through an update (section 5). |
| 3 | **Superseded documents still in the dump.** Examples: Purchase Policy v4.0 next to v4.1 (5% vs 2% price tolerance), SOP-PUR-002 v1.3 "(FINAL)" next to v1.4, the `old/` folders, and a byte-identical POL-SUP-003 "(1)" copy. | code checks | In the wiki the older versions are marked superseded and placed under *Versions and conflicts*. The byte-identical copy is not: it is ingested as a separate source and cited next to the original on 6 pages, against my own schema's rule that copies count as one source. Fix: point those references to the original file (the bytes are the same, so page and section stay the same) and, in a rebuild, skip duplicate copies before reading. At the source, the old versions should be moved out of the shared folders and the copy deleted. |
| 4 | **Orphan page.** `sup-vpc-rot-0107` (Voltway Paints & Coatings) had no page linking to it. | code checks | **Fixed**: linked from Voltway Cells' page (`sup-vc-ein-0042`), the supplier it must not be confused with. The 4 HR pages are orphans on purpose, because staff pages must never link to them. |
| 5 | **Quotes not found at the cited place** on 5 pages (for example 4 references on `pol-sup-003`), and **uncited paragraphs** on 23 pages. | code checks | Re-run the write step for those pages, telling it to cite every paragraph and to drop references whose quote does not check. Until then, a reader should open the raw source for those claims. |

Cell 5 also fixes one small thing without a model call: `topic-price-tolerance` had its slug as its title; it is now
titled "Price tolerance".

The lint also shows a second case of the parser bug in finding 1: `old/Supplier_Policy_v2.2.docx` is labelled with the
document code POL-PUR-001, because its purpose clause cites "POL-PUR-001 §6" in its first lines.

## 5. Update: one source changes

**The change.** I made a v3.1 of the approval matrix, `changed_source/01_policies/POL-APR-002 Approval Matrix v3.1.pdf`,
from v3.0's text. It raises the purchase executive's limit from £250,000 to £300,000 from 26 Oct 2026, and updates
example §5.1: Emma's £285,600 order is now within her own limit. This document is made up for the test. To keep Part
4 fair:
- the raw dump was not touched;
- the update ran on a copy of the wiki, so Part 4 uses the wiki built from the real documents.

The pages before and after the update are in `logs/part3_update_pages/`.

**Wiki** (`wiki_build.update`, cell 6):
- It read only the new file.
- It added 23 facts to the pages that file touches, and rewrote those pages from their current text plus the new
  facts.
- It rebuilt the index.

| | Wiki | RAG (the Part 2 winner) |
|---|---:|---:|
| What has to be redone | read 1 file, rewrite the pages it touches | parse and chunk 1 file, embed its chunks, add them to Chroma, rebuild BM25 |
| Pages or chunks changed | **12 pages rewritten**, 0 created | 3 chunks added (index now 13,737) |
| Model calls | 13 (1 read, 12 writes) | 0 |
| Time | **43.3 s** (21 s read, 22 s write) | 0.52 s parse and chunk + 0.07 s embed + 2.5 s Chroma add (including opening the index) + 2.7 s BM25 rebuild ≈ **5.8 s** |
| Cost | **$0.128** | **$0** |

**Which pages actually changed.** Of the 12 rewritten pages, 3 changed in substance:
- `pol-apr-002` now gives £300,000 as today's limit, with v3.0's £250,000 under *Versions and conflicts*;
- `role-pur-exec` changed the same way;
- `user-eclarke` now says Emma's orders up to £300,000 are self-approved.

The other 9 (the other roles, two error codes, three people) were rewritten because they cite the matrix, but say the
same thing in new words.

**The wiki update was not complete.** 4 pages mentioned £250,000 before the update (cell 7). All 4 were rewritten,
but `user-dokafor` still says Daniel Okafor approves Emma's "purchase orders exceeding £250,000 gross". That was
today's rule before the change, and is now stale. So an update can rewrite a page and still keep an old rule as if it
were current. The lint's LLM review (section 4) is the check meant to catch it; I did not run it on the updated copy.

**RAG is fast and free to update but does not know which version applies.** After adding v3.1, the index holds both
versions of the matrix, both marked CURRENT, and nothing in it says v3.1 replaces v3.0. I measured what the Part 2
winner itself returns (hybrid search + reranker, top 10, as a purchase executive, with the confidential filter; notebook
cell 8). The winner's index was copied to a scratch folder and v3.1's 3 chunks were added to the copy's chunk list,
BM25 and Chroma. The Part 2 index was not touched.

| Question | Before: POL-APR-002 ranks | After: v3.0 ranks | After: v3.1 ranks |
|---|---|---|---|
| What is the approval limit of a purchase executive? | v3.0 at 2, 5 | 3, 6 | **2**, 7 |
| Emma Clarke raises an order of £285,600 gross. Who approves it? | v3.0 at 1 | **1** | 2 |
| Can a purchase executive approve an order of £280,000 on their own? | v3.0 at 1, 2 | **1, 2** | 3, 5 |

In all three questions, both versions are in the winner's top 5, so the answer step gets £250,000 and £300,000 side by
side, both labelled CURRENT, and has to decide which applies. In two of the three, the old v3.0 ranks above v3.1. For the
first question, a 2016 intranet page (`approval_limits.html`) ranks first, above both. RAG would need v3.0 removed, or
marked superseded in its metadata, for the change to be clean.

The wiki pays 43 s and $0.13 per changed document to state, once, which rule applies today. RAG pays about 6 s and nothing,
and leaves that question to every answer.

## 6. Spend

| Step | Calls | Cost |
|---|---:|---:|
| Pilot, 3 files | 18 | $0.129 |
| Full ingest, 50 files | 165 live (+4 replayed) | $1.460 |
| 3 navigation queries: navigation, answers, judge | 7 + 3 + 3 | $0.051 |
| Lint: LLM review of every page | 121 live calls (see below) | $0.186 |
| Lint fixes: 2 pages rewritten | 2 | $0.011 |
| Update: 1 document, 12 pages | 13 | $0.128 |
| **Part 3 total** | **332** | **$1.965** |

The lint's review calls were made while I developed the lint: 121 live calls, $0.186 in all, recorded in
`cassettes/A3_wiki_lint.jsonl`. The notebook's cell 4 reviews the 118 pages with 2 live calls and replays the other
116 from those recordings, so its output shows $0.003. The fixes in cell 5 replay their 2 calls the same way.

## 7. Limits of this part

- **The scope covers only 13 of the 33 answerable golden-subset questions.** These are the 13 whose gold sources all
  sit in `01_policies` or `02_procedures`. Questions on error codes, services and tables need folders this wiki does
  not cover; that is the cost of a 50-file wiki, and it will show in Part 4.
- **The update's changed document is one I made**, from v3.0's text. It is clearly marked, and kept out of the raw
  dump and out of the wiki that Part 4 uses.
