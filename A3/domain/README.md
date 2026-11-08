# Northbridge Cycles: accounts payable document set (A3 Part 5)

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
| `facts.jsonl` | 101 facts: every limit, date, code, form number, field, owner and version. Every document is written from these. |
| `docs/` | 41 files: 14 DOCX, 3 EML, 2 MD, 12 PDF, 10 XLSX; 18 PDF pages |
| `questions.md` | 20 questions sorted into genesis, analytical and documentation (with types) |
| `questions.jsonl` | 10 documentation questions with reference answers, gold sources and must-contain strings |
| `mess.md` | The mess planted on purpose |
| `check.txt` | The check: every gold quote found at its location, every number in the documents is in the registry |
| `generator/` | The Python that builds every file (python-docx, reportlab, openpyxl) and runs the check |

Folders in `docs/`: 01_policies (11), 02_procedures (11), 03_ledgerline_manuals (2), 04_forms (3), 05_master_data (8), 06_transactions (1), 07_correspondence (5).

To rebuild: `python generator/build.py . && python generator/questions.py . && python generator/write_md.py . && python generator/check.py .`
(run from this folder; needs python-docx, reportlab, openpyxl, pypdf).
