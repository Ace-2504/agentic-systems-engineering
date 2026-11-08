"""Document bodies. Blocks: ("h1", text) numbered section, ("h2", text) subsection, ("p", text), ("table", rows)."""
from content import CO

def cover(code, title, version, effective, owner, approver, status="Approved"):
    return {"code": code, "title": title, "version": version, "effective": effective,
            "owner": owner, "approver": approver, "status": status}

AP_COMMON_HEAD = [
 ("h1", "1. Purpose"),
 ("p", f"This policy sets the rules {CO} follows from the moment a supplier invoice arrives until it is paid and "
       "confirmed by the bank. Northbridge Cycles Pvt. Ltd. makes bicycles and e-bikes in Pune, Maharashtra; GSTIN 27AAACN2604B1Z9. "
       "The policy applies to every invoice entered in Ledgerline, whether it is drafted by a person or by Ask Northbridge."),
 ("h1", "2. Roles"),
 ("p", "Priya Shah (accounts payable) enters and approves invoices. Emma Clarke (purchasing) deals with suppliers. "
       "Daniel Okafor (purchase manager) owns prices. Ganesh Pawar (stores) owns quantities received. "
       "Vikram Nair (financial controller) owns this policy. Meera Kulkarni (tax manager) owns GST and TDS. "
       "Henrik Weber (cost-centre owner) approves invoices without a purchase order on his cost centre. "
       "The Treasury desk and the Insurance desk are roles, not named people."),
]

def ap_policy(tol, hours):
    return AP_COMMON_HEAD + [
 ("h1", "3. Holds"),
 ("p", "Ledgerline matches every invoice with its purchase order and goods receipt before it can be posted. "
       "An invoice that fails a check is placed on hold and cannot be paid until the hold is released."),
 ("h2", "3.1 Price tolerance"),
 ("p", f"An invoice whose unit price is more than {tol} above the purchase order price goes on price hold H-PRC. "
       "The tolerance is checked line by line, not on the invoice total."),
 ("h2", "3.2 Quantity"),
 ("p", "An invoice whose billed quantity is more than the accepted quantity goes on quantity hold H-QTY. "
       "Accepted quantity is the quantity on the goods receipt after damaged and defective goods are taken out."),
 ("h2", "3.3 Duplicates"),
 ("p", "The same supplier GSTIN and invoice number in the same financial year is blocked as a duplicate. "
       "Two different suppliers may use the same invoice number; the supplier must always be confirmed first."),
 ("h1", "4. Releasing holds and approving invoices"),
 ("h2", "4.1 Who releases a hold"),
 ("p", "A price hold is released by the purchase manager (Daniel Okafor) or the financial controller. "
       "A quantity hold is released by stores (Ganesh Pawar) or the financial controller. "
       "Accounts payable never releases a hold it has raised."),
 ("h2", "4.2 Invoices without a purchase order"),
 ("p", "An invoice without a purchase order is approved by the cost-centre owner, never by the person who entered it."),
 ("h1", "5. The assistant"),
 ("h2", "5.1 Drafts from the assistant"),
 ("p", f"Every entry drafted by Ask Northbridge must be approved or amended within {hours}; otherwise it is escalated "
       "to the financial controller. The assistant never posts, releases or pays on its own."),
 ("h1", "6. Records"),
 ("p", "Ledgerline keeps the invoice, the match result, every hold and its release, and the name of each approver. "
       "Accounts payable keeps the supplier's PDF and the goods receipt with the invoice."),
]

AP21 = (cover("POL-AP-001", "Accounts Payable Policy", "v2.1", "1 April 2026", "Vikram Nair (financial controller)",
              "Finance director"),
        ap_policy("2%", "24 hours") + [
 ("h1", "7. Revision history"),
 ("table", [["Version", "Effective from", "Change"],
            ["v2.0", "1 April 2025", "First version for Ledgerline"],
            ["v2.1", "1 April 2026", "Price tolerance and draft approval time tightened; supersedes v2.0"]]),
])
AP20 = (cover("POL-AP-001", "Accounts Payable Policy", "v2.0", "1 April 2025", "Vikram Nair (financial controller)",
              "Finance director"),
        ap_policy("3%", "48 hours") + [
 ("h1", "7. Revision history"),
 ("table", [["Version", "Effective from", "Change"], ["v2.0", "1 April 2025", "First version for Ledgerline"]]),
])

PAY = (cover("POL-PAY-003", "Payment Run and Early Payment Policy", "v1.4", "1 October 2026",
             "Vikram Nair (financial controller)", "Finance director"), [
 ("h1", "1. Purpose"),
 ("p", "This policy decides when Northbridge pays an approved invoice, who must approve a payment, and how an "
       "early-payment discount offered by a supplier is judged."),
 ("h1", "2. Payment runs"),
 ("h2", "2.1 Payment runs"),
 ("p", "Payment runs are on Fridays; the cut-off for a run is 6 PM on the Thursday before. "
       "A payment approved after the cut-off moves to the next Friday run. The run dates are in the Payment Calendar "
       "in master data."),
 ("h2", "2.2 Which run"),
 ("p", "An invoice is paid in the last Friday run on or before its due date. Paying after the due date breaks the "
       "supplier's credit terms and is not allowed without the financial controller's written reason."),
 ("h1", "3. Approvals"),
 ("h2", "3.1 Early payments"),
 ("p", "A payment made more than 7 days before its due date is an early payment and needs the financial "
       "controller's approval and a reason. No early payment is approved while the invoice is on hold."),
 ("h2", "3.2 Large payments"),
 ("p", "Any payment above Rs.50,00,000 needs the financial controller's approval, in addition to accounts payable. "
       "The approval is recorded in Ledgerline against the payment proposal on FIN-AP-05."),
 ("h1", "4. Early-payment discounts"),
 ("h2", "4.1 Is the discount worth it"),
 ("p", "Paying early is not free: the money paid early could have earned interest or reduced borrowing. "
       "An early-payment discount is taken only if its yearly rate, discount / (cash paid early x days early / 365), "
       "is higher than Treasury's rate for the same days."),
 ("h2", "4.2 Treasury's rate"),
 ("p", "Treasury says where the money would come from: surplus cash is compared with the bank's fixed-deposit rate "
       "for that term; money drawn from the cash-credit limit with the cash-credit interest rate. "
       "Ask Northbridge asks Treasury by internal e-mail and shows both rates to the financial controller, who decides."),
 ("h2", "4.3 No reply"),
 ("p", "If Treasury has not replied before the run's cut-off, the draft says rate not received and makes no "
       "recommendation. The financial controller may still decide."),
 ("h1", "5. Confirmation"),
 ("h2", "5.1 When a payment is paid"),
 ("p", "A payment is reported as paid only after the bank statement confirms it. A payment the bank returns is "
       "reported as returned the same day, and is re-issued only after the bank-account checks in POL-SEC-004."),
 ("h1", "6. Revision history"),
 ("table", [["Version", "Effective from", "Change"],
            ["v1.3", "1 April 2026", "Friday runs and the large-payment limit"],
            ["v1.4", "1 October 2026", "Last run on or before the due date; early payment means more than 7 days early; Treasury's rate"]]),
])

GST = (cover("POL-TAX-005", "GST Input Tax Credit Policy", "v1.2", "1 November 2026",
             "Meera Kulkarni (tax manager)", "Vikram Nair (financial controller)"), [
 ("h1", "1. Purpose"),
 ("p", "This policy decides when Northbridge may claim back the GST it pays on purchases (input tax credit), "
       "and who checks it. Credit claimed wrongly must be paid back with interest, so every claim is checked first."),
 ("h1", "2. Conditions for credit"),
 ("h2", "2.1 When credit may be claimed"),
 ("p", "GST input tax credit is claimed only after the invoice appears in GSTR-2B (CGST Act section 16(2)(aa)). "
       "The goods must also have been received, as shown by the goods receipt."),
 ("h2", "2.2 E-invoices"),
 ("p", "An invoice from a supplier that must issue e-invoices but has no valid IRN gets no credit and is held for "
       "the tax manager. Ask Northbridge checks the IRN when the invoice is entered."),
 ("h1", "3. The monthly cycle"),
 ("p", "IMS review on the 12th and 13th; GSTR-2B on the 14th; GSTR-3B filed by the 20th; supplier filing check on the 25th. "
       "Any invoice left without action in IMS counts as accepted, so every invoice is reviewed before the 14th."),
 ("h1", "4. Escalation"),
 ("h2", "4.1 Escalation"),
 ("p", "Every GST reconciliation issue is escalated to the tax manager, Meera Kulkarni, within 24 hours. "
       "This includes an invoice missing from GSTR-2B, a value or tax mismatch, and an invoice in GSTR-2B that is not in Ledgerline."),
 ("h1", "5. Reversals"),
 ("h2", "5.1 The 180-day rule"),
 ("p", "180-day rule: a warning on day 150 after the invoice date; on day 181 the credit on the unpaid part is "
       "reversed with interest. A payment counts only once the bank statement confirms it."),
 ("h2", "5.2 Blocked credit"),
 ("p", "Credit on goods lost, stolen, destroyed or written off is blocked (CGST Act section 17(5)(h)) and reversed "
       "in GSTR-3B table 4(B)(1). Goods damaged in transit fall under this rule; defective goods returned to the "
       "supplier are covered by the supplier's credit note instead."),
 ("h1", "6. Contract GST payment terms"),
 ("p", "Contract GST payment terms: T1 pays the full invoice less TDS, and the GST is recovered if the invoice is not "
       "in GSTR-2B within 2 months; T2 pays the taxable value first and the GST after GSTR-2B shows the invoice. "
       "Each supplier's term is in the Vendor Master."),
 ("h1", "7. Revision history"),
 ("table", [["Version", "Effective from", "Change"], ["v1.2", "1 November 2026", "IMS review, escalation to the tax manager, contract GST terms"]]),
])

TDS = (cover("POL-TAX-006", "TDS Policy", "v1.1", "1 April 2026", "Meera Kulkarni (tax manager)",
             "Vikram Nair (financial controller)"), [
 ("h1", "1. Purpose"),
 ("p", "This policy decides how much tax Northbridge deducts at source (TDS) from supplier payments under the "
       "Income-tax Act 2025, and how it is deposited, returned and certified."),
 ("h1", "2. Deciding the section"),
 ("h2", "2.1 Which section applies"),
 ("p", "The approved TDS Section Table decides the section and rate; past invoices only suggest one; a new row is "
       "proposed by the tax manager and approved by the financial controller. The table maps the old section numbers "
       "to the new Act."),
 ("h1", "3. Rates"),
 ("h2", "3.1 Purchase of goods"),
 ("p", "Purchase of goods: Income-tax Act 2025 section 393(1), Table Sl. No. 8(ii) (formerly section 194Q): 0.1% of "
       "purchases above Rs.50,00,000 from one supplier in a financial year, because Northbridge's turnover is above "
       "Rs.10 crore. GST shown separately on the invoice is left out of the amount."),
 ("h2", "3.2 No PAN or inoperative PAN"),
 ("p", "With no PAN, or an inoperative PAN, TDS on a purchase of goods is 5%. A PAN not linked with Aadhaar is inoperative."),
 ("h2", "3.3 Transporters"),
 ("p", "No TDS on freight paid to a transporter owning not more than 10 goods carriages who gives its PAN and a "
       "declaration (formerly section 194C(6)). The declaration is recorded in the Vendor Master."),
 ("h1", "4. Certificates"),
 ("h2", "4.1 Lower or nil certificates"),
 ("p", "A lower or nil deduction certificate is used only after it is verified on TRACES. Its number is kept with "
       "every deduction made at the lower rate."),
 ("h1", "5. Deposit, return and certificate"),
 ("h2", "5.1 Deposit"),
 ("p", "TDS is deposited by the 7th of the following month. The deposit is complete only when the bank statement shows the challan."),
 ("h2", "5.2 Quarterly return"),
 ("p", "The quarterly TDS return is Form 140 (formerly Form 26Q); for October to December it is due by 31 January."),
 ("h2", "5.3 Certificate"),
 ("p", "The TDS certificate to the supplier is Form 131 (formerly Form 16A). Accounts payable sends it; the assistant only drafts the e-mail."),
])

RCM = (cover("POL-TAX-007", "Reverse Charge Policy", "v1.0", "1 November 2026", "Meera Kulkarni (tax manager)",
             "Vikram Nair (financial controller)"), [
 ("h1", "1. Purpose"),
 ("p", "For some services the law makes the buyer pay the GST instead of the supplier (reverse charge). "
       "This policy says how Northbridge finds those services, pays the tax and claims it back. "
       "The list of services and rates is the RCM Services Table in master data, kept by the tax manager."),
 ("h1", "2. Paying"),
 ("h2", "2.1 Paying reverse-charge GST"),
 ("p", "Reverse-charge GST is paid in cash only, never from input tax credit (CGST Act section 49(4)). "
       "It can be claimed back as credit in the same return, after it is paid."),
 ("h1", "3. Timing and documents"),
 ("h2", "3.1 When the tax is due"),
 ("p", "For services under reverse charge, the tax is due on the earlier of the payment date and the 61st day after "
       "the supplier's invoice date."),
 ("h2", "3.2 Self-invoice"),
 ("p", "For a supplier that is not registered, a self-invoice is issued within 30 days of receiving the service (Rule 47A)."),
 ("h1", "4. Unclear cases"),
 ("p", "If a service is not clearly in the RCM Services Table, the bill is held for the tax manager. "
       "Ask Northbridge reads only the approved table."),
])

INS = (cover("POL-INS-002", "Transit Insurance Claims Policy", "v1.0", "1 November 2026",
             "Vikram Nair (financial controller)", "Finance director"), [
 ("h1", "1. Scope"),
 ("h2", "1.1 Goods covered"),
 ("p", "This policy covers goods bought by Northbridge that are damaged while being carried to its Pune factory."),
 ("h2", "1.2 The policy"),
 ("p", "Northbridge's transit insurance policy number is TRN-2026-08812. The Insurance desk holds the policy schedule."),
 ("h1", "2. When goods arrive damaged"),
 ("h2", "2.1 Notifying the insurer"),
 ("p", "Goods damaged in transit are Northbridge's risk; the insurer must be notified within 24 hours of delivery. "
       "Asking the supplier for a credit note first is not allowed, because it delays the notice."),
 ("h2", "2.2 Keeping the goods"),
 ("p", "Damaged goods are kept aside, with photographs, until the insurer's surveyor has inspected them. "
       "The driver signs a remark on the consignment note before leaving."),
 ("h1", "3. The transporter"),
 ("h2", "3.1 Notice to the transporter"),
 ("p", "Written notice of claim goes to the transporter within 7 days of delivery; the legal limit is 180 days "
       "(Carriage by Road Act 2007, section 16). The notice protects the insurer's right to recover from the transporter."),
 ("h1", "4. The claim"),
 ("h2", "4.1 What is claimed"),
 ("p", "The claim includes the GST that cannot be claimed back as credit, because credit on damaged goods is blocked."),
 ("h1", "5. Responsibilities"),
 ("h2", "5.1 Who writes"),
 ("p", "The Insurance desk sends every notice to the insurer and the transporter; Ask Northbridge only drafts. "
       "Stores records the damage; accounts payable books the claim."),
])

SEC = (cover("POL-SEC-004", "Supplier Bank Account Change Policy", "v2.0", "1 July 2026",
             "Vikram Nair (financial controller)", "Finance director"), [
 ("h1", "1. Purpose"),
 ("p", "A changed bank account is the most common route for payment fraud. This policy sets the checks before any "
       "payment goes to a supplier's new account."),
 ("h1", "2. The four checks"),
 ("p", "A supplier bank account change needs a call-back to the number on file, a Rs.1 test credit, the financial "
       "controller's approval and a 24-hour hold before the first payment. The request is made on form FRM-SEC-02."),
 ("h1", "3. E-mails about bank details"),
 ("p", "E-mails asking to change bank details are never acted on directly; they are forwarded to "
       "security@northbridgecycles.example. This applies even when the e-mail appears to come from a known supplier."),
])

AGT = (cover("POL-AGT-001", "Ask Northbridge Assistant Policy", "v1.0", "1 September 2026",
             "Vikram Nair (financial controller)", "Finance director"), [
 ("h1", "1. Purpose"),
 ("p", "Ask Northbridge is the assistant that drafts payables entries in Ledgerline. This policy sets what it may "
       "and may not do."),
 ("h1", "2. Limits"),
 ("h2", "2.1 Internal only"),
 ("p", "Ask Northbridge never writes to anyone outside Northbridge; staff send what it drafts."),
 ("h2", "2.2 Tax actions"),
 ("p", "Ask Northbridge never clicks in IMS, pays tax or files a return. It prepares figures for the tax manager."),
 ("h2", "2.3 Approvals"),
 ("p", "Every entry it drafts waits for the right person's approval, as set in POL-AP-001 and the Approval Matrix."),
])

MAN = (cover("LL-AP", "Ledgerline Payables User Manual", "v4.2", "15 August 2026", "Ledgerline vendor", "Northbridge IT"), [
 ("h1", "1. Introduction"),
 ("h2", "1.1 Who this manual is for"),
 ("p", "This manual is for accounts payable, purchasing and finance users of the Ledgerline payables module."),
 ("h2", "1.2 Screens covered"),
 ("p", "The payables screens are FIN-AP-01 (invoice entry), FIN-AP-03 (hold queue) and FIN-AP-05 (payment proposal and run). "
       "The assistant, Ask Northbridge, uses the same screens through the service layer."),
 ("h1", "2. Signing in"),
 ("p", "Each user signs in with their own account. Approvals are recorded under the name of the user who signs in."),
 ("h1", "3. FIN-AP-01 Invoice entry"),
 ("h2", "3.1 Entering an invoice"),
 ("p", "Select the supplier first, then the purchase order. Ledgerline copies the order lines and the goods receipt, "
       "and runs the price, quantity and duplicate checks when the invoice is saved."),
 ("h2", "3.2 Fields on FIN-AP-01"),
 ("table", [["Field", "Meaning", "Rule"],
            ["Supplier Invoice No.", "The supplier's own invoice number", "Takes at most 16 characters"],
            ["IRN", "E-invoice reference number", "Checked against the e-invoice portal"],
            ["TDS Section", "Section under which TDS is deducted", "New-Act code, for example 393(1)-8(ii)"],
            ["Hold Code", "Why the invoice is held", "H-PRC, H-QTY, H-DUP or H-BNK"]]),
 ("p", "On FIN-AP-01 the field Supplier Invoice No. takes at most 16 characters. "
       "On FIN-AP-01 the field TDS Section takes the new-Act code, for example 393(1)-8(ii)."),
 ("h1", "4. FIN-AP-03 Hold queue"),
 ("p", "The hold queue lists every held invoice with its hold code and the date it was held. "
       "Only a user allowed by the Approval Matrix sees the Release button."),
 ("h1", "5. FIN-AP-05 Payment proposal and run"),
 ("h2", "5.1 Building a proposal"),
 ("p", "FIN-AP-05 proposes every approved invoice due in or before the selected run. Payments that need further "
       "approval are blocked until it is given."),
 ("h2", "5.2 Payment status codes"),
 ("table", [["Code", "Meaning"], ["SCH", "scheduled"], ["PK", "parked"], ["SNT", "sent to bank"], ["CNF", "confirmed by the bank statement"]]),
 ("p", "A payment with status PK is parked: it is not in the run and will not be paid until the block is cleared. "
       "A parked payment can look scheduled on the proposal list; always read the status code."),
 ("h1", "6. Messages"),
 ("p", "Error messages and their codes are listed in the LL-ERR Error Code Reference."),
])

ERR = (cover("LL-ERR", "Ledgerline Error Code Reference", "v4.0", "15 August 2026", "Ledgerline vendor", "Northbridge IT"), [
 ("h1", "1. How to read this reference"),
 ("p", "Each code is followed by the exact message shown on screen and what the user should do. "
       "Codes are grouped by the screen or check that raises them."),
 ("h1", "2. Invoice entry (FIN-AP-01)"),
 ("table", [["Code", "Message", "What to do"],
            ["ERR-AP-0107", "Duplicate invoice: supplier GSTIN and invoice number already posted in this financial year.", "Check the supplier; do not re-enter."],
            ["ERR-AP-0212", "Price variance above tolerance. Invoice placed on hold H-PRC.", "Ask the purchase manager to confirm the price."],
            ["ERR-AP-0215", "Billed quantity exceeds accepted quantity. Invoice placed on hold H-QTY.", "Ask stores to confirm the accepted quantity."]]),
 ("h1", "3. Tax checks"),
 ("table", [["Code", "Message", "What to do"],
            ["ERR-GST-0418", "IRN not found or cancelled on the e-invoice portal. Input tax credit not booked.", "Refer to the tax manager; ask the supplier for a valid e-invoice."],
            ["ERR-TDS-0505", "PAN inoperative. TDS rate set to the no-PAN rate.", "Ask the supplier to link PAN and Aadhaar."]]),
 ("h1", "4. Payments (FIN-AP-05)"),
 ("table", [["Code", "Message", "What to do"],
            ["ERR-PAY-0331", "Payment parked: approval missing for amount above limit.", "Get the financial controller's approval."],
            ["ERR-PAY-0340", "Run cut-off passed. Payment moved to the next Friday run.", "Check the payment calendar."],
            ["ERR-BNK-0602", "Bank account changed less than 24 hours ago. Payment blocked.", "Wait for the hold to end."]]),
])

HRBANK = (cover("HR-CONF-005", "Bank Mandate and Authorised Signatories", "v1.0", "1 July 2026",
                "Vikram Nair (financial controller)", "Finance director", status="CONFIDENTIAL - NBC-FIN-CONF only"), [
 ("h1", "1. Accounts and signatories"),
 ("p", "Northbridge's payments account and its two authorised signatories (the financial controller and the finance "
       "director), each up to Rs.2,00,00,000 a payment. Readable only by NBC-FIN-CONF."),
 ("table", [["Account", "Bank", "Signatories"],
            ["Payments account", "Western India Bank, Pune", "Financial controller; finance director"]]),
])

PDFS = {"AP21": AP21, "AP20": AP20, "PAY": PAY, "GST": GST, "TDS": TDS, "RCM": RCM, "INS": INS, "SEC": SEC,
        "AGT": AGT, "MAN": MAN, "ERR": ERR, "HRBANK": HRBANK}

# ----------------------------------------------------------------------------- DOCX procedures and forms
DOCX = {
 "PRC01": ("PRC-AP-01 Invoice Entry Procedure", [
   ("Purpose", ["How accounts payable enters a supplier invoice in Ledgerline on FIN-AP-01."]),
   ("Steps", ["1. Confirm the supplier first: two suppliers may use the same invoice number.",
              "2. Select the purchase order and check the goods receipt, including damaged and defective goods.",
              "3. Enter the Supplier Invoice No. (at most 16 characters) and the IRN.",
              "4. Save. Ledgerline runs the price, quantity and duplicate checks and may place a hold.",
              "5. Ask Northbridge drafts the entry; Priya Shah approves or amends it within 24 hours."]),
   ("Related", ["POL-AP-001, LL-AP Payables User Manual, LL-ERR Error Code Reference."])]),
 "PRC02": ("PRC-AP-02 Hold Release Procedure", [
   ("Purpose", ["How a held invoice is referred and released."]),
   ("Steps", ["1. Open FIN-AP-03 and read the hold code.",
              "2. H-PRC goes to the purchase manager (Daniel Okafor); H-QTY goes to stores (Ganesh Pawar).",
              "3. The financial controller may release either hold.",
              "4. The person releasing records the reason in Ledgerline."]),
   ("Related", ["POL-AP-001 section 4.1, Hold Codes in master data."])]),
 "PRC03": ("PRC-AP-03 Friday Payment Run Procedure", [
   ("Purpose", ["How the Friday payment run is prepared and confirmed."]),
   ("Steps", ["1. By Thursday 6 PM, accounts payable builds the proposal on FIN-AP-05.",
              "2. Every invoice goes in the last Friday run on or before its due date.",
              "3. Payments above Rs.50,00,000 and early payments wait for the financial controller.",
              "4. Read the status code of each payment: PK means parked, not scheduled.",
              "5. After the run, the morning bank check confirms each payment (PRC-AP-04)."]),
   ("Related", ["POL-PAY-003, Payment Calendar FY2026-27."])]),
 "PRC04": ("PRC-AP-04 Morning Bank Check Procedure", [
   ("Purpose", ["How each payment is confirmed against the bank statement."]),
   ("Steps", ["1. Ask Northbridge reads the bank's e-mail and the bank statement.",
              "2. A payment credited to the supplier is set to CNF and only then reported as paid.",
              "3. A payment the bank returns is reported as returned the same day.",
              "4. TDS and reverse-charge challans are confirmed the same way."]),
   ("Related", ["POL-PAY-003 section 5.1."])]),
 "PRCT1": ("PRC-TAX-01 Monthly GST Reconciliation Procedure", [
   ("Purpose", ["How GST credit is checked each month before it is claimed."]),
   ("IMS review", ["On the 12th and 13th, Ask Northbridge checks each invoice in IMS: is it ours, do the details match "
                   "Ledgerline, have the goods arrived, is anything in dispute. It recommends accept, reject or keep pending; "
                   "Meera Kulkarni acts in IMS."]),
   ("Matching GSTR-2B", ["On the 14th, GSTR-2B is matched both ways with Ledgerline, within a tolerance of Rs.1 per invoice."]),
   ("Escalation", ["Every GST reconciliation issue is escalated to the tax manager, Meera Kulkarni, within 24 hours."]),
   ("Filing", ["Meera Kulkarni files GSTR-3B by the 20th."])]),
 "PRCT2": ("PRC-TAX-02 TDS Deposit and Quarterly Return Procedure", [
   ("Purpose", ["How TDS is deposited, returned and certified."]),
   ("Deposit", ["TDS is deposited by the 7th of the following month. The tax manager approves the challan and the financial "
                "controller authorises it at the bank."]),
   ("Quarterly return", ["The quarterly TDS return is Form 140; for October to December it is due by 31 January."]),
   ("Certificate", ["The tax manager downloads Form 131 from TRACES; accounts payable sends it to the supplier."])]),
 "PRCT3": ("PRC-TAX-03 Reverse Charge and Self-Invoice Procedure", [
   ("Purpose", ["How a bill under reverse charge is handled."]),
   ("Steps", ["1. Ask Northbridge checks the service against the RCM Services Table.",
              "2. If it is unclear, the bill goes to the tax manager.",
              "3. For a supplier that is not registered, a self-invoice is issued within 30 days.",
              "4. The tax is paid in cash with GSTR-3B and claimed back in the same return."])]),
 "PRCI1": ("PRC-INS-01 Damaged Goods Claim Procedure", [
   ("Purpose", ["How a claim is raised for goods damaged in transit."]),
   ("Steps", ["1. Stores records the damaged goods on the goods receipt with photographs and the driver's signed remark.",
              "2. Ask Northbridge drafts the claim intimation on form FRM-INS-01 the same day.",
              "3. The Insurance desk sends it to the insurer within 24 hours of delivery, quoting policy TRN-2026-08812.",
              "4. The Insurance desk sends written notice of claim to the transporter within 7 days.",
              "5. Stores keeps the goods aside until the surveyor has inspected them.",
              "6. Accounts payable books the claim, including the GST that cannot be claimed back."]),
   ("Related", ["POL-INS-002."])]),
 "PRCP1": ("PRC-PUR-01 Defective Goods Return Procedure", [
   ("Purpose", ["How defective goods are returned to the supplier."]),
   ("Time limit", ["Defective goods are claimed from the supplier within 2 days of delivery and returned against the "
                   "supplier's GST credit note."]),
   ("Steps", ["1. Stores records the defective goods at inspection.",
              "2. Ask Northbridge drafts the claim; Emma Clarke sends it to the supplier.",
              "3. Accounts payable enters the supplier's GST credit note when it arrives."])]),
 "PRCY1": ("PRC-TRY-01 Early Payment Discount Check Procedure", [
   ("Purpose", ["How an early-payment discount offer is judged."]),
   ("Steps", ["1. Ask Northbridge works out the discount as a yearly rate on the cash paid early.",
              "2. It e-mails Treasury: where would the money come from, and at what rate for those days?",
              "3. Surplus cash is compared with the fixed-deposit rate; the cash-credit limit with its interest rate.",
              "4. The financial controller decides; Emma Clarke tells the supplier."])]),
 "FRM7": ("FRM-AP-07 Early Payment Request Form", [
   ("Instructions", ["Use this form for any payment made more than 7 days before its due date."]),
   ("Fields", ["Supplier and invoice number", "Due date and proposed run", "Discount offered and its yearly rate",
               "Treasury's rate and source of funds", "Reason", "Financial controller's approval"])]),
 "FRMS2": ("FRM-SEC-02 Bank Account Change Request Form", [
   ("Instructions", ["Use this form for every change to a supplier's bank account (POL-SEC-004)."]),
   ("Fields", ["Supplier", "New account details", "Call-back made to the number on file (date, by whom)",
               "Rs.1 test credit confirmed", "Financial controller's approval", "24-hour hold ends at"])]),
 "FRMI1": ("FRM-INS-01 Insurance Claim Intimation Form", [
   ("Instructions", ["Drafted by Ask Northbridge, sent by the Insurance desk within 24 hours of delivery."]),
   ("Fields", ["Policy number", "Supplier, invoice and consignment note", "Quantity damaged and photographs",
               "Estimated loss including GST that cannot be claimed back", "Notice sent to the transporter (date)"])]),
}

# ----------------------------------------------------------------------------- XLSX
XLSX = {
 "VEND": {"Vendors": [
   ["Vendor ID", "Name", "State", "GSTIN", "PAN", "MSME", "GST term", "Payment terms (days)", "FY 2026-27 purchases before 2 October 2026", "Notes"],
   ["VC-EIN-0042", "Voltway Cells Pvt. Ltd.", "Gujarat", "24AABCV4471K1Z2", "AABCV4471K", "No", "T1", 45, "Rs.38,30,400", ""],
   ["VP-PNT-0107", "Voltway Paints & Coatings", "Gujarat", "", "", "No", "T2", 30, "", ""],
   ["CC-CHG-0018", "Castlefield Chargers", "Maharashtra", "", "", "No", "T1", 30, "", ""],
   ["PB-BRK-0031", "Pennine Brakes", "Karnataka", "", "", "Yes (45-day payment limit)", "T2", 45, "", ""],
   ["SR-GTA-0009", "Saurashtra Roadways", "Gujarat (Rajkot)", "", "", "No", "Reverse charge", "", "",
    "Goods transport agency; small-transporter declaration DEC-SR-2026-014, valid until 31 March 2027"]]},
 "APPR": {"Approvals": [
   ["Action", "Approver", "Stand-in", "Limit or note"],
   ["Price hold release", "Purchase manager", "Financial controller", "H-PRC"],
   ["Quantity hold release", "Stores", "Financial controller", "H-QTY"],
   ["Invoice without purchase order", "Cost-centre owner", "Financial controller", "Never the person who entered it"],
   ["Early payment", "Financial controller", "Finance director", "More than 7 days before the due date"],
   ["Large payment", "Financial controller", "Finance director", "Above Rs.50,00,000"],
   ["GST credit claim or reversal", "Tax manager", "Financial controller", ""],
   ["TDS challan", "Tax manager", "Financial controller", "Authorised at the bank by the financial controller"],
   ["Supplier bank account change", "Financial controller", "Finance director", "After call-back and Rs.1 test"],
   ["Insurance claim notice", "Insurance desk", "Financial controller", "Within 24 hours of delivery"]]},
 "HOLD": {"Hold codes": [
   ["Code", "Meaning", "Released by"],
   ["H-PRC", "price", "Purchase manager or financial controller"],
   ["H-QTY", "quantity", "Stores or financial controller"],
   ["H-DUP", "duplicate", "Accounts payable after checking the supplier"],
   ["H-BNK", "bank account change", "Financial controller after the 24-hour hold"]]},
 "RCMT": {"Services": [
   ["Entry", "Service", "Supplier to recipient", "Rate", "Credit for Northbridge", "Valid from", "Valid until", "Source"],
   ["1", "Goods transport by road", "Goods transport agency not opted to charge GST, to a registered person", "5%", "Yes", "1 November 2026", "", "Notification 13/2017"],
   ["2", "Legal services", "Advocate or firm of advocates, to a business entity", "18%", "Yes", "1 November 2026", "", "Notification 13/2017"],
   ["5AB", "Renting of property other than a dwelling", "Unregistered person, to a registered person", "18%", "Yes", "1 November 2026", "", "Notification 13/2017"],
   ["6", "Director's services", "Director, to the company", "18%", "Yes", "1 November 2026", "", "Notification 13/2017"],
   ["14", "Security staff", "Person other than a body corporate, to a registered person", "18%", "Yes", "1 November 2026", "", "Notification 13/2017"],
   ["15", "Cab or bus hire with fuel", "Non-body-corporate not charging 18%, to a body corporate", "5%", "Blocked unless more than 13 seats", "1 November 2026", "", "Notification 8/2026"],
   ["15", "Cab or bus hire with fuel", "Non-body-corporate not charging 12%, to a body corporate", "5%", "Blocked unless more than 13 seats", "", "31 October 2026", "Notification 13/2017"]]},
 "TDST": {"Sections": [
   ["Nature of purchase", "Section (Income-tax Act 2025)", "Former section", "Rate", "Threshold", "Valid from"],
   ["Purchase of goods", "393(1)-8(ii)", "194Q", "0.1%", "Above Rs.50,00,000 a year from one supplier", "1 April 2026"],
   ["Contract work and transport", "393(1)", "194C", "1% for individuals and HUFs, 2% for others", "Above Rs.30,000 a payment or Rs.1,00,000 a year", "1 April 2026"],
   ["Transport by a small transporter", "393(1)", "194C(6)", "Nil with PAN and declaration", "", "1 April 2026"],
   ["Professional fees", "393(1)", "194J", "10%", "Above Rs.50,000 a year", "1 April 2026"],
   ["No PAN or inoperative PAN (purchase of goods)", "393(1)-8(ii)", "206AA", "5%", "", "1 April 2026"]]},
 "CAL": {"Runs": [
   ["Run date", "Cut-off"],
   ["Friday 13 November 2026", "Thursday 12 November 2026, 6 PM"],
   ["Friday 20 November 2026", "Thursday 19 November 2026, 6 PM"],
   ["Friday 27 November 2026", "Thursday 26 November 2026, 6 PM"],
   ["Friday 4 December 2026", "Thursday 3 December 2026, 6 PM"],
   ["Friday 11 December 2026", "Thursday 10 December 2026, 6 PM"],
   ["Friday 18 December 2026", "Thursday 17 December 2026, 6 PM"]]},
 "GL": {"Accounts": [
   ["Account", "Name"],
   [1380, "Insurance claim receivable"], [1451, "IGST credit waiting for GSTR-2B"], [1452, "IGST credit available"],
   [2310, "TDS payable"], [2320, "IGST payable under reverse charge"], [5120, "Freight inward"], [5810, "Loss in transit"]]},
 "TAXCAL": {"Calendar": [
   ["Task", "Due", "Owner"],
   ["October TDS deposit", "7 November 2026", "Tax manager"],
   ["IMS review for October", "12 and 13 November 2026", "Tax manager"],
   ["GSTR-3B for October", "20 November 2026", "Tax manager"],
   ["November TDS deposit", "7 December 2026", "Tax manager"],
   ["Form 140 for October to December", "31 January 2027", "Tax manager"]]},
 "OPEN": {"Invoices": [
   ["Supplier", "Invoice", "Date", "Taxable", "CGST", "SGST", "IGST", "Total", "Due", "Status", "Note"],
   ["Voltway Cells Pvt. Ltd.", "4471", "2 October 2026", 23990400, None, None, 4318272, 28308672, "16 November 2026",
    "Approved; scheduled for the 13 November 2026 run", "18,000 packs at Rs.1,332.80; 260 damaged in transit (blocked IGST Rs.62,375.04; insurance claim Rs.4,08,903.04)"],
   ["Voltway Cells Pvt. Ltd.", "VC-CN-0071", "6 October 2026", -53312, None, None, -9596.16, -62908.16, "", "Credit note", "40 defective packs"],
   ["Voltway Paints & Coatings", "4471", "20 October 2026", 184000, None, None, 33120, 217120, "19 November 2026", "Approved", ""],
   ["Castlefield Chargers", "CC-2290", "27 October 2026", 640000, 57600, 57600, None, 755200, "", "Hold H-PRC since 28 October 2026", ""],
   ["Pennine Brakes", "PB-118", "19 September 2026", 325000, None, None, 58500, 383500, "", "Hold H-QTY since 22 September 2026", ""],
   ["Saurashtra Roadways", "SR-0912", "2 October 2026", 120000, None, None, None, 120000, "", "Paid on 9 October 2026",
    "Reverse charge IGST Rs.6,000 payable by Northbridge"]],
  "Offers": [
   ["Supplier", "Offer date", "Offer"],
   ["Voltway Cells Pvt. Ltd.", "7 October 2026", "0.5% if paid within 15 days of delivery, 0.25% within 30 days"]]},
 "HRSAL": {"Bands": [
   ["Role", "Band", "Annual range", "Access"],
   ["Accounts payable executive", "F2", "Rs.6,00,000 to Rs.8,50,000", "NBC-HR-CONF only"],
   ["Purchasing executive", "F2", "Rs.6,00,000 to Rs.8,50,000", "NBC-HR-CONF only"],
   ["Tax manager", "F4", "Rs.16,00,000 to Rs.22,00,000", "NBC-HR-CONF only"]]},
}

# ----------------------------------------------------------------------------- e-mails and notes
EML = {
 "EM1": ("Finance Director <fd@northbridgecycles.example>", "Finance team <finance@northbridgecycles.example>",
         "Mon, 02 Nov 2026 10:15:00 +0530", "Payment approval limit from 1 December",
         "Team,\n\nFrom 1 December 2026 the large-payment limit becomes Rs.25,00,000: any payment above it needs the "
         "financial controller's approval. Until then the limit in POL-PAY-003 (Rs.50,00,000) still applies. "
         "Vikram will update the policy and the Approval Matrix before the date.\n\nRegards,\nFinance Director"),
 "EM2": ("Treasury desk <treasury@northbridgecycles.example>", "Vikram Nair <vikram.nair@northbridgecycles.example>",
         "Tue, 03 Nov 2026 16:40:00 +0530", "Rates for early payment decisions",
         "Vikram,\n\nFor early-payment decisions this month: our surplus cash sits in fixed deposits at 6.5% a year for "
         "15 to 45 days. If a payment has to come from the cash-credit limit, the rate is 9.75% a year.\n\nTreasury desk"),
 "EM3": ("Meera Kulkarni <meera.kulkarni@northbridgecycles.example>", "Accounts payable <ap@northbridgecycles.example>",
         "Thu, 05 Nov 2026 09:05:00 +0530", "IMS reminder and match tolerance",
         "Hi all,\n\nReminder: anything left without action in IMS counts as accepted, so the October review runs on the "
         "12th and 13th. The match tolerance is Rs.1 per invoice; anything above it comes to me.\n\nMeera"),
}
MD = {
 "MD1": "# Meeting notes - GST reconciliation escalations\n\nDate: 21 October 2026\nPresent: Vikram Nair, Meera Kulkarni, Priya Shah\n\n"
        "## Decisions\n\n- GST reconciliation issues go to Meera Kulkarni; the 24-hour timer starts when the agent raises the issue.\n"
        "- Vikram Nair stands in for Meera Kulkarni when she is away.\n",
 "MD2": "# Meeting notes - Insurance desk start\n\nDate: 28 October 2026\nPresent: Vikram Nair, Ganesh Pawar, Priya Shah\n\n"
        "## Decisions\n\n- The Insurance desk starts on 1 November 2026 and owns all insurer and transporter correspondence.\n"
        "- Stores photographs damaged goods at the goods receipt and keeps them aside for the surveyor.\n",
}
