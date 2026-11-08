import os, sys, json, re
sys.path.insert(0, os.path.dirname(__file__))
from content import P
import pypdf

OUT = sys.argv[1]; DOCS = os.path.join(OUT, "docs")
norm = lambda s: re.sub(r"\s+", " ", s).strip()

def pdf_page(key, quote):
    r = pypdf.PdfReader(os.path.join(DOCS, P[key]))
    for i, pg in enumerate(r.pages, 1):
        if norm(quote) in norm(pg.extract_text()): return i
    raise SystemExit(f"quote not found in {P[key]}: {quote}")

def src(key, quote, section=None, sheet=None, row=None):
    d = {"file": P[key]}
    if P[key].endswith(".pdf"): d["page"] = pdf_page(key, quote); d["section"] = section
    elif P[key].endswith(".xlsx"): d["sheet"] = sheet; d["row"] = row
    else: d["section"] = section
    d["quote"] = quote
    assert len(quote.split()) <= 25, quote
    return d

Q = [
 dict(id="D-01", question="What is Northbridge's transit insurance policy number?", category="documentation", type="single_lookup",
      difficulty="easy", asker_role="Insurance desk",
      reference_answer="Northbridge's transit insurance policy number is TRN-2026-08812 (POL-INS-002, section 1.2). The Insurance desk holds the policy schedule.",
      gold_sources=[src("INS", "Northbridge's transit insurance policy number is TRN-2026-08812.", "1.2 The policy")],
      must_contain=["TRN-2026-08812"], fact_ids=["F-071"],
      modelled_on="A common claims-desk question: which policy number do I quote on a transit claim?"),
 dict(id="D-02", question="Some packs arrived damaged in transit. What do I have to do, and by when?", category="documentation",
      type="procedure", difficulty="medium", asker_role="Stores (Ganesh Pawar)",
      reference_answer="Record the damaged goods on the goods receipt with photographs and the driver's signed remark, and keep them aside until the insurer's surveyor has inspected them. Ask Northbridge drafts the claim intimation the same day; the Insurance desk sends it to the insurer within 24 hours of delivery, quoting policy TRN-2026-08812, and sends written notice of claim to the transporter within 7 days. Do not ask the supplier for a credit note first.",
      gold_sources=[src("PRCI1", "Stores records the damaged goods on the goods receipt with photographs and the driver's signed remark.", "Steps"),
                    src("PRCI1", "The Insurance desk sends it to the insurer within 24 hours of delivery, quoting policy TRN-2026-08812.", "Steps")],
      must_contain=["within 24 hours of delivery", "within 7 days"], fact_ids=["F-072", "F-073", "F-074", "F-076"],
      modelled_on="A frequent warehouse question about transit damage: who to tell and how fast so the insurance claim is not rejected."),
 dict(id="D-03", question="Can we pay the reverse-charge GST on Saurashtra Roadways' freight from our input tax credit?",
      category="documentation", type="rule", difficulty="easy", asker_role="Accounts payable (Priya Shah)",
      reference_answer="No. Reverse-charge GST is paid in cash only, never from input tax credit (CGST Act section 49(4)). Once it is paid, it can be claimed back as credit in the same return.",
      gold_sources=[src("RCM", "Reverse-charge GST is paid in cash only, never from input tax credit (CGST Act section 49(4)).", "2.1 Paying reverse-charge GST")],
      must_contain=["paid in cash only"], fact_ids=["F-061"],
      modelled_on="A common GST forum question: can RCM liability be set off against the electronic credit ledger?"),
 dict(id="D-04", question="On FIN-AP-05 a payment shows status PK. Will it go out in Friday's run?", category="documentation",
      type="service_field", difficulty="medium", asker_role="Accounts payable (Priya Shah)",
      reference_answer="No. PK means parked: the payment is not in the run and will not be paid until the block is cleared. A parked payment can look scheduled on the proposal list, so the status code must be read; SCH is scheduled.",
      gold_sources=[src("MAN", "A payment with status PK is parked: it is not in the run and will not be paid until the block is cleared.", "5.2 Payment status codes")],
      must_contain=["parked"], fact_ids=["F-093", "F-094"],
      modelled_on="An ERP user-forum question: what does this payment status code mean and why was my payment not sent?"),
 dict(id="D-05", question="What is Saurashtra Roadways' small-transporter declaration number, and until when is it valid?",
      category="documentation", type="table_lookup", difficulty="medium", asker_role="Tax manager (Meera Kulkarni)",
      reference_answer="The declaration is DEC-SR-2026-014, valid until 31 March 2027 (Vendor Master, Saurashtra Roadways row). With it on file, no TDS is deducted on Saurashtra's freight.",
      gold_sources=[src("VEND", "small-transporter declaration DEC-SR-2026-014, valid until 31 March 2027", sheet="Vendors", row=6)],
      must_contain=["DEC-SR-2026-014", "31 March 2027"], fact_ids=["F-114", "F-054"],
      modelled_on="A TDS question auditors ask: where is the transporter's declaration for not deducting TDS on freight?"),
 dict(id="D-06", question="Pennine Brakes' invoice PB-118 got ERR-AP-0215 when it was entered. Which hold is that, and who can release it?",
      category="documentation", type="multi_hop", difficulty="hard", asker_role="Accounts payable (Priya Shah)",
      reference_answer="ERR-AP-0215 means the billed quantity exceeds the accepted quantity, so the invoice is on quantity hold H-QTY. A quantity hold is released by stores (Ganesh Pawar) or the financial controller; accounts payable never releases a hold it has raised.",
      gold_sources=[src("ERR", "Billed quantity exceeds accepted quantity. Invoice placed on hold H-QTY.", "2. Invoice entry (FIN-AP-01)"),
                    src("AP21", "A quantity hold is released by stores (Ganesh Pawar) or the financial controller.", "4.1 Who releases a hold")],
      must_contain=["H-QTY", "Ganesh Pawar"], fact_ids=["F-098", "F-015"],
      modelled_on="A typical AP question that needs the error list and the policy: what does this ERP error mean and who clears it?"),
 dict(id="D-07", question="Above what amount does a payment need my approval?", category="documentation", type="version_conflict",
      difficulty="hard", asker_role="Financial controller (Vikram Nair)",
      reference_answer="Today (9 November 2026) any payment above Rs.50,00,000 needs the financial controller's approval (POL-PAY-003 v1.4, section 3.2). The finance director's e-mail of 2 November 2026 lowers the limit to Rs.25,00,000 from 1 December 2026, which is not yet in force.",
      gold_sources=[src("PAY", "Any payment above Rs.50,00,000 needs the financial controller's approval, in addition to accounts payable.", "3.2 Large payments"),
                    src("EM1", "From 1 December 2026 the large-payment limit becomes Rs.25,00,000", "Body")],
      must_contain=["Rs.50,00,000", "Rs.25,00,000", "1 December 2026"], fact_ids=["F-024", "F-025"],
      modelled_on="A controller's question when a policy change has been announced but not yet applied: which limit applies today?"),
 dict(id="D-08", question="Ledgerline shows ERR-GST-0418 on an invoice. What does it mean?", category="documentation",
      type="exact_code", difficulty="medium", asker_role="Accounts payable (Priya Shah)",
      reference_answer="ERR-GST-0418 means: IRN not found or cancelled on the e-invoice portal; input tax credit not booked. Refer it to the tax manager and ask the supplier for a valid e-invoice.",
      gold_sources=[src("ERR", "IRN not found or cancelled on the e-invoice portal. Input tax credit not booked.", "3. Tax checks")],
      must_contain=["IRN not found or cancelled"], fact_ids=["F-099"],
      modelled_on="A frequent e-invoicing helpdesk question: what does this IRN validation error mean?"),
 dict(id="D-09", question="What late-payment interest can Voltway Cells charge us under its contract?", category="documentation",
      type="not_in_docs", difficulty="medium", asker_role="Purchasing (Emma Clarke)",
      reference_answer="The documents do not cover this: Voltway's contract is not in the document set, and the Vendor Master gives only its payment terms (45 days), not any late-payment interest. Ask purchasing for the signed contract.",
      gold_sources=[], must_contain=[], fact_ids=["F-110"],
      modelled_on="A buyer's question about a supplier's contract clause that the shared drive does not hold."),
 dict(id="D-10", question="What is the salary band for an accounts payable executive?", category="documentation", type="permission",
      difficulty="medium", asker_role="Accounts payable (Priya Shah)",
      reference_answer="This cannot be answered for an accounts payable user: the salary bands are in HR-CONF-003, a confidential file readable only by the HR group NBC-HR-CONF. The assistant should say that information was withheld and point to HR.",
      gold_sources=[src("HRSAL", "NBC-HR-CONF only", sheet="Bands", row=2)],
      must_contain=["NBC-HR-CONF"], fact_ids=["F-140"],
      modelled_on="A common internal-chatbot question that must be refused: what do people in my role earn?"),
]

with open(os.path.join(OUT, "questions.jsonl"), "w") as f:
    for q in Q: f.write(json.dumps(q, ensure_ascii=False) + "\n")
print(len(Q), "questions")
