import os, sys, json, collections
import pypdf
OUT = sys.argv[1]; DOCS = os.path.join(OUT, "docs")

QS = [
 ("G-01", "Insurance desk", "Draft the claim intimation to the insurer for the 260 Voltway packs damaged in transit.", "genesis", "", "A routine claims task: write the intimation letter for a transit-damage claim."),
 ("G-02", "Tax manager (Meera Kulkarni)", "Prepare October's TDS challan for my approval.", "genesis", "", "A month-start finance task: prepare the TDS payment challan before the 7th."),
 ("G-03", "Purchasing (Emma Clarke)", "Draft my reply to Voltway saying we will pay invoice 4471 on the normal terms.", "genesis", "", "A buyer replying to a supplier's early-payment discount offer."),
 ("G-04", "Accounts payable (Priya Shah)", "Enter Voltway's credit note VC-CN-0071 for the 40 defective packs.", "genesis", "", "An everyday AP task: post a supplier credit note for returned goods."),
 ("A-01", "Financial controller (Vikram Nair)", "Is Voltway's 0.5% discount worth taking at Treasury's fixed-deposit rate, and at the cash-credit rate?", "analytical", "", "The classic treasury question: what is the annual rate of a cash discount, and is it worth borrowing for?"),
 ("A-02", "Tax manager (Meera Kulkarni)", "How much IGST credit on Voltway's invoice 4471 can we claim this month, after the defective credit note and the damaged packs?", "analytical", "", "A monthly input-tax-credit computation with blocked credit and credit notes."),
 ("A-03", "Accounts payable (Priya Shah)", "Which open invoices have been on hold for more than 3 days, and what is their total value?", "analytical", "", "An AP ageing report of held invoices, often asked before month-end."),
 ("A-04", "Tax manager (Meera Kulkarni)", "How much have we bought from Voltway Cells this financial year, and how much of it is above the TDS threshold?", "analytical", "", "Tracking the purchase-of-goods TDS threshold per supplier, a frequent CA-forum question."),
]
for line in open(os.path.join(OUT, "questions.jsonl")):
    q = json.loads(line)
    QS.append((q["id"], q["asker_role"], q["question"], "documentation", q["type"], q["modelled_on"]))
QS += [
 ("D-11", "Accounts payable (Priya Shah)", "How far above the purchase order price can an invoice be before it goes on hold?", "documentation", "version_conflict", "An AP question where an old policy copy is still on the shared drive: which tolerance applies?"),
 ("D-12", "Tax manager (Meera Kulkarni)", "When may we claim the GST credit on a supplier invoice?", "documentation", "rule", "A common GST question since GSTR-2B became the basis for input tax credit."),
]

md = ["# Questions (20)", "", "Asked by the roles in CAPSTONE.md (Northbridge Cycles, accounts payable). Today is Monday 9 November 2026.",
      "D-01 to D-10 have reference answers and gold sources in `questions.jsonl`.", "",
      "| ID | Asked by | Question | Category | Type | Modelled on |", "|---|---|---|---|---|---|"]
for r in QS: md.append("| " + " | ".join(r) + " |")
cat = collections.Counter(r[3] for r in QS); typ = collections.Counter(r[4] for r in QS if r[4])
md += ["", "## Counts", "", "By category: " + ", ".join(f"{k} {v}" for k, v in cat.items()) + ".",
       "Documentation by type: " + ", ".join(f"{k} {v}" for k, v in sorted(typ.items())) + f" ({len(typ)} types)."]
open(os.path.join(OUT, "questions.md"), "w").write("\n".join(md) + "\n")

open(os.path.join(OUT, "mess.md"), "w").write("""# Planted mess

Every case below is deliberate, so a retriever or a wiki can be tested on it.

| # | Mess | Files | Why it matters |
|---|---|---|---|
| 1 | **Old version next to the new one** | `01_policies/POL-AP-001 Accounts Payable Policy v2.0.pdf` and `... v2.1.pdf` | v2.0 (effective 1 April 2025) says the price tolerance is 3% and drafts wait 48 hours; v2.1 (effective 1 April 2026) says 2% and 24 hours. v2.0 still says "Status: Approved" and has no "superseded" stamp. A search that finds v2.0 first gives the wrong rule (question D-11). |
| 2 | **An amendment not yet in force** | `07_correspondence/2026-11-02 FD - Payment approval limit from 1 December.eml` | The finance director lowers the large-payment limit from Rs.50,00,000 to Rs.25,00,000 from 1 December 2026. Today (9 November 2026) the old limit still applies, and POL-PAY-003 and the Approval Matrix still say Rs.50,00,000 (question D-07). |
| 3 | **A byte-identical duplicate** | `02_procedures/PRC-AP-03 Friday Payment Run Procedure.docx` and `... (1).docx` | Same bytes (same SHA-256, see check.txt). Duplicates fill the top-k with the same chunk twice. |
| 4 | **A badly named file** | `05_master_data/Final_FINAL_tax calendar Q3 (2) USE THIS.xlsx` | It is the only tax calendar in the set, so the name gives no hint of what it holds. |
| 5 | **A confidential folder** | `01_policies/HR/CONFIDENTIAL/` with `HR-CONF-003 Finance Salary Bands FY2026-27.xlsx` (HR group NBC-HR-CONF only) and `HR-CONF-005 Bank Mandate and Authorised Signatories.pdf` (NBC-FIN-CONF only) | Ordinary staff must not see these; they must be filtered out before ranking, and the answer must say something was withheld (question D-10). |
| 6 | **A fact only in a spreadsheet row** | `05_master_data/Vendor Master.xlsx`, sheet Vendors, row 6 | Saurashtra Roadways' small-transporter declaration DEC-SR-2026-014, valid until 31 March 2027, appears nowhere else. The TDS policy only says the declaration "is recorded in the Vendor Master" (question D-05). |

Other realistic traps, also on purpose:
- Two different suppliers both sent an invoice numbered **4471** (Voltway Cells and Voltway Paints & Coatings, in `06_transactions/Open AP Invoices 2026-11-09.xlsx`), as in the course kit; the supplier must be confirmed first.
- The RCM Services Table has **two rows for entry 15** with different validity dates (until 31 October 2026, and from 1 November 2026).
- The IMS match tolerance (Rs.1 per invoice) is only in an e-mail and a procedure, not in the GST policy.
- Pennine Brakes (an MSME with a 45-day payment limit) has an invoice on hold since 22 September 2026.
""")

files = [os.path.relpath(os.path.join(r, f), DOCS) for r, _, fs in os.walk(DOCS) for f in fs]
by_ext = collections.Counter(os.path.splitext(f)[1] for f in files)
pages = sum(len(pypdf.PdfReader(os.path.join(DOCS, f)).pages) for f in files if f.endswith(".pdf"))
by_dir = collections.Counter(f.split(os.sep)[0] for f in files)
open(os.path.join(OUT, "README.md"), "w").write(f"""# Northbridge Cycles: accounts payable document set (A3 Part 5)

**Everything here is invented.** The company, people, suppliers, GSTINs, PANs, policy numbers, amounts and e-mails are
fictional, made for the Enterprise Agents course. No real company, employee or customer data is used. Tax rules follow
Indian GST and income-tax law as of November 2026 as closely as the author could, but this is not tax advice.

**Today is Monday 9 November 2026.** Every document is dated relative to it: policies took effect before today, one
e-mail announces a change from 1 December 2026 (not yet in force), and the open-invoice list is as of today.

**Domain.** Accounts payable at Northbridge Cycles Pvt. Ltd., a bicycle and e-bike maker in Pune, the same company,
systems (Ledgerline, Ask Northbridge) and roles as `A1/CAPSTONE.md`: Priya Shah (accounts payable), Emma Clarke
(purchasing), Daniel Okafor (purchase manager), Ganesh Pawar (stores), Vikram Nair (financial controller), Meera Kulkarni
(tax manager), the Treasury desk and the Insurance desk. Suppliers: Voltway Cells, Voltway Paints & Coatings, Castlefield
Chargers, Pennine Brakes and Saurashtra Roadways.

## What is here

| File | What it is |
|---|---|
| `facts.jsonl` | {sum(1 for _ in open(os.path.join(OUT, 'facts.jsonl')))} facts: every limit, date, code, form number, field, owner and version. Every document is written from these. |
| `docs/` | {len(files)} files: {', '.join(f'{v} {k[1:].upper()}' for k, v in sorted(by_ext.items()))}; {pages} PDF pages |
| `questions.md` | 20 questions sorted into genesis, analytical and documentation (with types) |
| `questions.jsonl` | 10 documentation questions with reference answers, gold sources and must-contain strings |
| `mess.md` | The mess planted on purpose |
| `check.txt` | The check: every gold quote found at its location, every number in the documents is in the registry |
| `generator/` | The Python that builds every file (python-docx, reportlab, openpyxl) and runs the check |

Folders in `docs/`: {', '.join(f'{k} ({v})' for k, v in sorted(by_dir.items()))}.

To rebuild: `python generator/build.py . && python generator/questions.py . && python generator/write_md.py . && python generator/check.py .`
(run from this folder; needs python-docx, reportlab, openpyxl, pypdf).
""")
print(dict(by_ext), pages, dict(cat), dict(typ))
