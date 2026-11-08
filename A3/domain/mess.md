# Planted mess

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
