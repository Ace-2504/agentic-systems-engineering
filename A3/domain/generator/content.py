"""All facts and all document text for the Northbridge Cycles payables domain (A3 Part 5).
Everything is invented. TODAY is fixed. Every number in a document must also appear in a fact."""

TODAY = "Monday 9 November 2026"
CO = "Northbridge Cycles Pvt. Ltd."

# ---------------------------------------------------------------- file paths
P = {
 "AP21": "01_policies/POL-AP-001 Accounts Payable Policy v2.1.pdf",
 "AP20": "01_policies/POL-AP-001 Accounts Payable Policy v2.0.pdf",
 "PAY": "01_policies/POL-PAY-003 Payment Run and Early Payment Policy v1.4.pdf",
 "GST": "01_policies/POL-TAX-005 GST Input Tax Credit Policy v1.2.pdf",
 "TDS": "01_policies/POL-TAX-006 TDS Policy v1.1.pdf",
 "RCM": "01_policies/POL-TAX-007 Reverse Charge Policy v1.0.pdf",
 "INS": "01_policies/POL-INS-002 Transit Insurance Claims Policy v1.0.pdf",
 "SEC": "01_policies/POL-SEC-004 Supplier Bank Account Change Policy v2.0.pdf",
 "AGT": "01_policies/POL-AGT-001 Ask Northbridge Assistant Policy v1.0.pdf",
 "HRSAL": "01_policies/HR/CONFIDENTIAL/HR-CONF-003 Finance Salary Bands FY2026-27.xlsx",
 "HRBANK": "01_policies/HR/CONFIDENTIAL/HR-CONF-005 Bank Mandate and Authorised Signatories.pdf",
 "PRC01": "02_procedures/PRC-AP-01 Invoice Entry Procedure.docx",
 "PRC02": "02_procedures/PRC-AP-02 Hold Release Procedure.docx",
 "PRC03": "02_procedures/PRC-AP-03 Friday Payment Run Procedure.docx",
 "PRC03DUP": "02_procedures/PRC-AP-03 Friday Payment Run Procedure (1).docx",
 "PRC04": "02_procedures/PRC-AP-04 Morning Bank Check Procedure.docx",
 "PRCT1": "02_procedures/PRC-TAX-01 Monthly GST Reconciliation Procedure.docx",
 "PRCT2": "02_procedures/PRC-TAX-02 TDS Deposit and Quarterly Return Procedure.docx",
 "PRCT3": "02_procedures/PRC-TAX-03 Reverse Charge and Self-Invoice Procedure.docx",
 "PRCI1": "02_procedures/PRC-INS-01 Damaged Goods Claim Procedure.docx",
 "PRCP1": "02_procedures/PRC-PUR-01 Defective Goods Return Procedure.docx",
 "PRCY1": "02_procedures/PRC-TRY-01 Early Payment Discount Check Procedure.docx",
 "MAN": "03_ledgerline_manuals/LL-AP Payables User Manual v4.2.pdf",
 "ERR": "03_ledgerline_manuals/LL-ERR Error Code Reference v4.0.pdf",
 "FRM7": "04_forms/FRM-AP-07 Early Payment Request Form.docx",
 "FRMS2": "04_forms/FRM-SEC-02 Bank Account Change Request Form.docx",
 "FRMI1": "04_forms/FRM-INS-01 Insurance Claim Intimation Form.docx",
 "VEND": "05_master_data/Vendor Master.xlsx",
 "APPR": "05_master_data/Approval Matrix.xlsx",
 "HOLD": "05_master_data/Hold Codes.xlsx",
 "RCMT": "05_master_data/RCM Services Table.xlsx",
 "TDST": "05_master_data/TDS Section Table.xlsx",
 "CAL": "05_master_data/Payment Calendar FY2026-27.xlsx",
 "GL": "05_master_data/GL Account Codes.xlsx",
 "TAXCAL": "05_master_data/Final_FINAL_tax calendar Q3 (2) USE THIS.xlsx",
 "OPEN": "06_transactions/Open AP Invoices 2026-11-09.xlsx",
 "EM1": "07_correspondence/2026-11-02 FD - Payment approval limit from 1 December.eml",
 "EM2": "07_correspondence/2026-11-03 Treasury - Rates for early payment decisions.eml",
 "EM3": "07_correspondence/2026-11-05 Tax - IMS reminder and match tolerance.eml",
 "MD1": "07_correspondence/2026-10-21 Meeting notes - GST reconciliation escalations.md",
 "MD2": "07_correspondence/2026-10-28 Meeting notes - Insurance desk start.md",
}

F = []  # (id, fact, file key, section)
def fact(fid, text, fkey, sec):
    F.append((fid, text, fkey, sec))

# ---------------------------------------------------------------- company and people
fact("F-001", f"Today for this document set is {TODAY}.", "README", "Today")
fact("F-002", "Northbridge Cycles Pvt. Ltd. makes bicycles and e-bikes in Pune, Maharashtra; GSTIN 27AAACN2604B1Z9.", "AP21", "1. Purpose")
fact("F-003", "People: Priya Shah (accounts payable), Emma Clarke (purchasing), Daniel Okafor (purchase manager), Ganesh Pawar (stores), Vikram Nair (financial controller), Meera Kulkarni (tax manager), Henrik Weber (cost-centre owner), Treasury desk (role), Insurance desk (role).", "AP21", "2. Roles")
fact("F-004", "The ERP is Ledgerline; the payables screens are FIN-AP-01 (invoice entry), FIN-AP-03 (hold queue) and FIN-AP-05 (payment proposal and run). The assistant is Ask Northbridge.", "MAN", "1.2 Screens covered")

# ---------------------------------------------------------------- POL-AP-001 v2.1 and v2.0
fact("F-010", "POL-AP-001 Accounts Payable Policy v2.1 is effective from 1 April 2026, owned by Vikram Nair, and supersedes v2.0.", "AP21", "Cover")
fact("F-011", "POL-AP-001 v2.1, section 3.1: an invoice whose unit price is more than 2% above the purchase order price goes on price hold H-PRC.", "AP21", "3.1 Price tolerance")
fact("F-012", "POL-AP-001 v2.0 (effective 1 April 2025, superseded on 1 April 2026), section 3.1, allowed a price tolerance of 3%.", "AP20", "3.1 Price tolerance")
fact("F-013", "An invoice whose billed quantity is more than the accepted quantity goes on quantity hold H-QTY.", "AP21", "3.2 Quantity")
fact("F-014", "Duplicate check: the same supplier GSTIN and invoice number in the same financial year is blocked as a duplicate.", "AP21", "3.3 Duplicates")
fact("F-015", "A price hold is released by the purchase manager (Daniel Okafor) or the financial controller; a quantity hold by stores (Ganesh Pawar) or the financial controller.", "AP21", "4.1 Who releases a hold")
fact("F-016", "An invoice without a purchase order is approved by the cost-centre owner, never by the person who entered it.", "AP21", "4.2 Invoices without a purchase order")
fact("F-017", "Every entry drafted by Ask Northbridge must be approved or amended within 24 hours; otherwise it is escalated to the financial controller.", "AP21", "5.1 Drafts from the assistant")
fact("F-018", "POL-AP-001 v2.0 gave draft approvals 48 hours.", "AP20", "5.1 Drafts from the assistant")

# ---------------------------------------------------------------- POL-PAY-003
fact("F-020", "POL-PAY-003 Payment Run and Early Payment Policy v1.4 is effective from 1 October 2026 and owned by Vikram Nair; v1.3 was effective from 1 April 2026.", "PAY", "Cover")
fact("F-021", "Payment runs are on Fridays; the cut-off for a run is 6 PM on the Thursday before.", "PAY", "2.1 Payment runs")
fact("F-022", "An invoice is paid in the last Friday run on or before its due date.", "PAY", "2.2 Which run")
fact("F-023", "A payment made more than 7 days before its due date is an early payment and needs the financial controller's approval and a reason.", "PAY", "3.1 Early payments")
fact("F-024", "Any payment above Rs.50,00,000 needs the financial controller's approval.", "PAY", "3.2 Large payments")
fact("F-025", "From 1 December 2026 the large-payment limit becomes Rs.25,00,000 (finance director's e-mail of 2 November 2026); it is not yet in force on 9 November 2026.", "EM1", "Body")
fact("F-026", "An early-payment discount is taken only if its yearly rate, discount / (cash paid early x days early / 365), is higher than Treasury's rate for the same days.", "PAY", "4.1 Is the discount worth it")
fact("F-027", "Treasury says where the money would come from: surplus cash is compared with the bank's fixed-deposit rate for that term; money drawn from the cash-credit limit with the cash-credit interest rate.", "PAY", "4.2 Treasury's rate")
fact("F-028", "If Treasury has not replied before the run's cut-off, the draft says rate not received and makes no recommendation.", "PAY", "4.3 No reply")
fact("F-029", "A payment is reported as paid only after the bank statement confirms it.", "PAY", "5.1 When a payment is paid")
fact("F-030", "Treasury's rates on 3 November 2026: fixed deposit 6.5% a year for 15 to 45 days; cash-credit limit 9.75% a year.", "EM2", "Body")
fact("F-031", "Voltway Cells offered 0.5% if paid within 15 days of delivery or 0.25% within 30 days (offer of 7 October 2026).", "OPEN", "Offers")

# ---------------------------------------------------------------- POL-TAX-005 GST credit
fact("F-040", "POL-TAX-005 GST Input Tax Credit Policy v1.2 is effective from 1 November 2026 and owned by Meera Kulkarni.", "GST", "Cover")
fact("F-041", "GST input tax credit is claimed only after the invoice appears in GSTR-2B (CGST Act section 16(2)(aa)).", "GST", "2.1 When credit may be claimed")
fact("F-042", "An invoice from a supplier that must issue e-invoices but has no valid IRN gets no credit and is held for the tax manager.", "GST", "2.2 E-invoices")
fact("F-043", "Monthly cycle: IMS review on the 12th and 13th; GSTR-2B on the 14th; GSTR-3B filed by the 20th; supplier filing check on the 25th.", "GST", "3. The monthly cycle")
fact("F-044", "Any invoice left without action in IMS counts as accepted.", "GST", "3. The monthly cycle")
fact("F-045", "Every GST reconciliation issue is escalated to the tax manager, Meera Kulkarni, within 24 hours.", "GST", "4.1 Escalation")
fact("F-046", "180-day rule: a warning on day 150 after the invoice date; on day 181 the credit on the unpaid part is reversed with interest.", "GST", "5.1 The 180-day rule")
fact("F-047", "Credit on goods lost, stolen, destroyed or written off is blocked (CGST Act section 17(5)(h)) and reversed in GSTR-3B table 4(B)(1).", "GST", "5.2 Blocked credit")
fact("F-048", "Contract GST payment terms: T1 pays the full invoice less TDS, and the GST is recovered if the invoice is not in GSTR-2B within 2 months; T2 pays the taxable value first and the GST after GSTR-2B shows the invoice.", "GST", "6. Contract GST payment terms")
fact("F-049", "IMS match tolerance is Rs.1 per invoice (tax manager's e-mail of 5 November 2026).", "EM3", "Body")

# ---------------------------------------------------------------- POL-TAX-006 TDS
fact("F-050", "POL-TAX-006 TDS Policy v1.1 is effective from 1 April 2026 and owned by Meera Kulkarni.", "TDS", "Cover")
fact("F-051", "The approved TDS Section Table decides the section and rate; past invoices only suggest one; a new row is proposed by the tax manager and approved by the financial controller.", "TDS", "2.1 Which section applies")
fact("F-052", "Purchase of goods: Income-tax Act 2025 section 393(1), Table Sl. No. 8(ii) (formerly section 194Q): 0.1% of purchases above Rs.50,00,000 from one supplier in a financial year, because Northbridge's turnover is above Rs.10 crore.", "TDS", "3.1 Purchase of goods")
fact("F-053", "With no PAN, or an inoperative PAN, TDS on a purchase of goods is 5% (formerly section 206AA).", "TDS", "3.2 No PAN or inoperative PAN")
fact("F-054", "No TDS on freight paid to a transporter owning not more than 10 goods carriages who gives its PAN and a declaration (formerly section 194C(6)).", "TDS", "3.3 Transporters")
fact("F-055", "A lower or nil deduction certificate is used only after it is verified on TRACES.", "TDS", "4.1 Lower or nil certificates")
fact("F-056", "TDS is deposited by the 7th of the following month.", "TDS", "5.1 Deposit")
fact("F-057", "The quarterly TDS return is Form 140 (formerly Form 26Q); for October to December it is due by 31 January.", "TDS", "5.2 Quarterly return")
fact("F-058", "The TDS certificate to the supplier is Form 131 (formerly Form 16A).", "TDS", "5.3 Certificate")

# ---------------------------------------------------------------- POL-TAX-007 RCM
fact("F-060", "POL-TAX-007 Reverse Charge Policy v1.0 is effective from 1 November 2026 and owned by Meera Kulkarni.", "RCM", "Cover")
fact("F-061", "Reverse-charge GST is paid in cash only, never from input tax credit (CGST Act section 49(4)).", "RCM", "2.1 Paying reverse-charge GST")
fact("F-062", "For services under reverse charge, the tax is due on the earlier of the payment date and the 61st day after the supplier's invoice date.", "RCM", "3.1 When the tax is due")
fact("F-063", "For a supplier that is not registered, a self-invoice is issued within 30 days of receiving the service (Rule 47A).", "RCM", "3.2 Self-invoice")
fact("F-064", "Goods transport by a goods transport agency that has not opted to charge GST: reverse charge at 5% (Notification 13/2017). Other rows in force from 1 November 2026: entry 2 legal services 18%, entry 5AB renting of property by an unregistered person 18%, entry 6 director's services 18%, entry 14 security staff 18%.", "RCMT", "Services row 2")
fact("F-065", "Cab or bus hire with fuel from a non-body-corporate not charging 18%: reverse charge at 5%, valid from 1 November 2026 (Notification 8/2026); the earlier row (not charging 12%) applied until 31 October 2026. Credit on entry 15 is blocked unless the vehicle has more than 13 seats.", "RCMT", "Services rows 7 and 8")

# ---------------------------------------------------------------- POL-INS-002
fact("F-070", "POL-INS-002 Transit Insurance Claims Policy v1.0 is effective from 1 November 2026 and owned by Vikram Nair.", "INS", "Cover")
fact("F-071", "Northbridge's transit insurance policy number is TRN-2026-08812.", "INS", "1.2 The policy")
fact("F-072", "Goods damaged in transit are Northbridge's risk; the insurer must be notified within 24 hours of delivery.", "INS", "2.1 Notifying the insurer")
fact("F-073", "Damaged goods are kept aside, with photographs, until the insurer's surveyor has inspected them.", "INS", "2.2 Keeping the goods")
fact("F-074", "Written notice of claim goes to the transporter within 7 days of delivery; the legal limit is 180 days (Carriage by Road Act 2007, section 16).", "INS", "3.1 Notice to the transporter")
fact("F-075", "The claim includes the GST that cannot be claimed back as credit.", "INS", "4.1 What is claimed")
fact("F-076", "The Insurance desk sends every notice to the insurer and the transporter; Ask Northbridge only drafts.", "INS", "5.1 Who writes")

# ---------------------------------------------------------------- defective goods
fact("F-077", "Defective goods are claimed from the supplier within 2 days of delivery and returned against the supplier's GST credit note.", "PRCP1", "Time limit")

# ---------------------------------------------------------------- POL-SEC-004
fact("F-080", "POL-SEC-004 Supplier Bank Account Change Policy v2.0 is effective from 1 July 2026.", "SEC", "Cover")
fact("F-081", "A supplier bank account change needs a call-back to the number on file, a Rs.1 test credit, the financial controller's approval and a 24-hour hold before the first payment.", "SEC", "2. The four checks")
fact("F-082", "E-mails asking to change bank details are never acted on directly; they are forwarded to security@northbridgecycles.example.", "SEC", "3. E-mails about bank details")

# ---------------------------------------------------------------- POL-AGT-001
fact("F-085", "POL-AGT-001 Ask Northbridge Assistant Policy v1.0 is effective from 1 September 2026.", "AGT", "Cover")
fact("F-086", "Ask Northbridge never writes to anyone outside Northbridge; staff send what it drafts.", "AGT", "2.1 Internal only")
fact("F-087", "Ask Northbridge never clicks in IMS, pays tax or files a return.", "AGT", "2.2 Tax actions")
fact("F-088", "Every entry Ask Northbridge drafts waits for the right person's approval, as set in POL-AP-001 and the Approval Matrix.", "AGT", "2.3 Approvals")

# ---------------------------------------------------------------- manual and errors
fact("F-090", "LL-AP Payables User Manual v4.2 is dated 15 August 2026.", "MAN", "Cover")
fact("F-091", "On FIN-AP-01 the field Supplier Invoice No. takes at most 16 characters.", "MAN", "3.2 Fields on FIN-AP-01")
fact("F-092", "On FIN-AP-01 the field TDS Section takes the new-Act code, for example 393(1)-8(ii).", "MAN", "3.2 Fields on FIN-AP-01")
fact("F-093", "Payment status codes on FIN-AP-05: SCH scheduled, PK parked, SNT sent to bank, CNF confirmed by the bank statement.", "MAN", "5.2 Payment status codes")
fact("F-094", "A payment with status PK is parked: it is not in the run and will not be paid until the block is cleared.", "MAN", "5.2 Payment status codes")
fact("F-095", "LL-ERR Error Code Reference v4.0 is dated 15 August 2026.", "ERR", "Cover")
fact("F-096", "ERR-AP-0107: Duplicate invoice: supplier GSTIN and invoice number already posted in this financial year.", "ERR", "2. Invoice entry (FIN-AP-01)")
fact("F-097", "ERR-AP-0212: Price variance above tolerance. Invoice placed on hold H-PRC.", "ERR", "2. Invoice entry (FIN-AP-01)")
fact("F-098", "ERR-AP-0215: Billed quantity exceeds accepted quantity. Invoice placed on hold H-QTY.", "ERR", "2. Invoice entry (FIN-AP-01)")
fact("F-099", "ERR-GST-0418: IRN not found or cancelled on the e-invoice portal. Input tax credit not booked.", "ERR", "3. Tax checks")
fact("F-100", "ERR-TDS-0505: PAN inoperative. TDS rate set to the no-PAN rate.", "ERR", "3. Tax checks")
fact("F-101", "ERR-PAY-0331: Payment parked: approval missing for amount above limit.", "ERR", "4. Payments (FIN-AP-05)")
fact("F-102", "ERR-PAY-0340: Run cut-off passed. Payment moved to the next Friday run.", "ERR", "4. Payments (FIN-AP-05)")
fact("F-103", "ERR-BNK-0602: Bank account changed less than 24 hours ago. Payment blocked.", "ERR", "4. Payments (FIN-AP-05)")

# ---------------------------------------------------------------- master data
fact("F-110", "Vendor VC-EIN-0042 Voltway Cells Pvt. Ltd., Gujarat, GSTIN 24AABCV4471K1Z2, PAN AABCV4471K, not an MSME, GST term T1, payment terms 45 days, purchases before 2 October 2026 in FY 2026-27: Rs.38,30,400.", "VEND", "Vendors row 2")
fact("F-111", "Vendor VP-PNT-0107 Voltway Paints & Coatings, Gujarat, GST term T2, payment terms 30 days.", "VEND", "Vendors row 3")
fact("F-112", "Vendor CC-CHG-0018 Castlefield Chargers, Maharashtra, GST term T1, payment terms 30 days.", "VEND", "Vendors row 4")
fact("F-113", "Vendor PB-BRK-0031 Pennine Brakes, Karnataka, MSME (45-day payment limit), GST term T2, payment terms 45 days.", "VEND", "Vendors row 5")
fact("F-114", "Vendor SR-GTA-0009 Saurashtra Roadways, Rajkot, Gujarat, goods transport agency under reverse charge; small-transporter declaration DEC-SR-2026-014, valid until 31 March 2027.", "VEND", "Vendors row 6")
fact("F-115", "Approval matrix: GST credit claims and reversals are approved by the tax manager (stand-in: financial controller); TDS challans are approved by the tax manager and authorised at the bank by the financial controller.", "APPR", "Approvals rows 7 and 8")
fact("F-116", "Hold codes: H-PRC price, H-QTY quantity, H-DUP duplicate, H-BNK bank account change.", "HOLD", "Hold codes")
fact("F-117", "Friday payment runs: 13, 20 and 27 November 2026; 4, 11 and 18 December 2026; cut-off 6 PM the Thursday before (12, 19 and 26 November; 3, 10 and 17 December 2026).", "CAL", "Runs")
fact("F-118", "GL accounts: 1380 insurance claim receivable, 1451 IGST credit waiting for GSTR-2B, 1452 IGST credit available, 2310 TDS payable, 2320 IGST payable under reverse charge, 5120 freight inward, 5810 loss in transit.", "GL", "Accounts")
fact("F-119", "TDS Section Table: contract work and transport (formerly 194C) 1% for individuals and HUFs, 2% for others, above Rs.30,000 a payment or Rs.1,00,000 a year; professional fees (formerly 194J) 10% above Rs.50,000 a year.", "TDST", "Sections rows 3 to 5")
fact("F-120", "Tax calendar Q3 FY2026-27: October TDS by 7 November 2026; IMS review 12 and 13 November 2026; GSTR-3B for October by 20 November 2026; November TDS by 7 December 2026; Form 140 for October to December by 31 January 2027.", "TAXCAL", "Calendar")

# ---------------------------------------------------------------- open invoices (analytical data)
fact("F-130", "Invoice 4471 from Voltway Cells, dated 2 October 2026: 18,000 packs at Rs.1,332.80, taxable Rs.2,39,90,400, IGST Rs.43,18,272, total Rs.2,83,08,672, due 16 November 2026, scheduled for the 13 November 2026 run.", "OPEN", "Invoices row 2")
fact("F-131", "Credit note VC-CN-0071 from Voltway Cells, dated 6 October 2026, for 40 defective packs: Rs.53,312 plus IGST Rs.9,596.16, total Rs.62,908.16.", "OPEN", "Invoices row 3")
fact("F-132", "260 packs of invoice 4471 were damaged in transit; their blocked IGST is Rs.62,375.04 and the insurance claim is Rs.4,08,903.04.", "OPEN", "Invoices row 2")
fact("F-133", "Invoice 4471 from Voltway Paints & Coatings, dated 20 October 2026: taxable Rs.1,84,000, IGST Rs.33,120, total Rs.2,17,120, due 19 November 2026.", "OPEN", "Invoices row 4")
fact("F-134", "Invoice CC-2290 from Castlefield Chargers, dated 27 October 2026: taxable Rs.6,40,000, CGST Rs.57,600, SGST Rs.57,600, total Rs.7,55,200, on hold H-PRC since 28 October 2026.", "OPEN", "Invoices row 5")
fact("F-135", "Invoice PB-118 from Pennine Brakes, dated 19 September 2026: taxable Rs.3,25,000, IGST Rs.58,500, total Rs.3,83,500, on hold H-QTY since 22 September 2026.", "OPEN", "Invoices row 6")
fact("F-136", "Invoice SR-0912 from Saurashtra Roadways, dated 2 October 2026: freight Rs.1,20,000, no GST charged (reverse charge IGST Rs.6,000), paid on 9 October 2026.", "OPEN", "Invoices row 7")

# ---------------------------------------------------------------- confidential
fact("F-140", "HR-CONF-003: accounts payable executive band F2, Rs.6,00,000 to Rs.8,50,000 a year; tax manager band F4, Rs.16,00,000 to Rs.22,00,000 a year. Readable only by the HR group NBC-HR-CONF.", "HRSAL", "Bands rows 2 and 4")
fact("F-141", "HR-CONF-005: Northbridge's payments account and its two authorised signatories (the financial controller and the finance director), each up to Rs.2,00,00,000 a payment. Readable only by NBC-FIN-CONF.", "HRBANK", "1. Accounts and signatories")

# ---------------------------------------------------------------- notes
fact("F-150", "Meeting of 21 October 2026: GST reconciliation issues go to Meera Kulkarni; the 24-hour timer starts when the agent raises the issue.", "MD1", "Decisions")
fact("F-151", "Meeting of 28 October 2026: the Insurance desk starts on 1 November 2026 and owns all insurer and transporter correspondence.", "MD2", "Decisions")

FACT_TEXT = {fid: t for fid, t, _, _ in F}
