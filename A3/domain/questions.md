# Questions (20)

Asked by the roles in CAPSTONE.md (Northbridge Cycles, accounts payable). Today is Monday 9 November 2026.
D-01 to D-10 have reference answers and gold sources in `questions.jsonl`.

| ID | Asked by | Question | Category | Type | Modelled on |
|---|---|---|---|---|---|
| G-01 | Insurance desk | Draft the claim intimation to the insurer for the 260 Voltway packs damaged in transit. | genesis |  | A routine claims task: write the intimation letter for a transit-damage claim. |
| G-02 | Tax manager (Meera Kulkarni) | Prepare October's TDS challan for my approval. | genesis |  | A month-start finance task: prepare the TDS payment challan before the 7th. |
| G-03 | Purchasing (Emma Clarke) | Draft my reply to Voltway saying we will pay invoice 4471 on the normal terms. | genesis |  | A buyer replying to a supplier's early-payment discount offer. |
| G-04 | Accounts payable (Priya Shah) | Enter Voltway's credit note VC-CN-0071 for the 40 defective packs. | genesis |  | An everyday AP task: post a supplier credit note for returned goods. |
| A-01 | Financial controller (Vikram Nair) | Is Voltway's 0.5% discount worth taking at Treasury's fixed-deposit rate, and at the cash-credit rate? | analytical |  | The classic treasury question: what is the annual rate of a cash discount, and is it worth borrowing for? |
| A-02 | Tax manager (Meera Kulkarni) | How much IGST credit on Voltway's invoice 4471 can we claim this month, after the defective credit note and the damaged packs? | analytical |  | A monthly input-tax-credit computation with blocked credit and credit notes. |
| A-03 | Accounts payable (Priya Shah) | Which open invoices have been on hold for more than 3 days, and what is their total value? | analytical |  | An AP ageing report of held invoices, often asked before month-end. |
| A-04 | Tax manager (Meera Kulkarni) | How much have we bought from Voltway Cells this financial year, and how much of it is above the TDS threshold? | analytical |  | Tracking the purchase-of-goods TDS threshold per supplier, a frequent CA-forum question. |
| D-01 | Insurance desk | What is Northbridge's transit insurance policy number? | documentation | single_lookup | A common claims-desk question: which policy number do I quote on a transit claim? |
| D-02 | Stores (Ganesh Pawar) | Some packs arrived damaged in transit. What do I have to do, and by when? | documentation | procedure | A frequent warehouse question about transit damage: who to tell and how fast so the insurance claim is not rejected. |
| D-03 | Accounts payable (Priya Shah) | Can we pay the reverse-charge GST on Saurashtra Roadways' freight from our input tax credit? | documentation | rule | A common GST forum question: can RCM liability be set off against the electronic credit ledger? |
| D-04 | Accounts payable (Priya Shah) | On FIN-AP-05 a payment shows status PK. Will it go out in Friday's run? | documentation | service_field | An ERP user-forum question: what does this payment status code mean and why was my payment not sent? |
| D-05 | Tax manager (Meera Kulkarni) | What is Saurashtra Roadways' small-transporter declaration number, and until when is it valid? | documentation | table_lookup | A TDS question auditors ask: where is the transporter's declaration for not deducting TDS on freight? |
| D-06 | Accounts payable (Priya Shah) | Pennine Brakes' invoice PB-118 got ERR-AP-0215 when it was entered. Which hold is that, and who can release it? | documentation | multi_hop | A typical AP question that needs the error list and the policy: what does this ERP error mean and who clears it? |
| D-07 | Financial controller (Vikram Nair) | Above what amount does a payment need my approval? | documentation | version_conflict | A controller's question when a policy change has been announced but not yet applied: which limit applies today? |
| D-08 | Accounts payable (Priya Shah) | Ledgerline shows ERR-GST-0418 on an invoice. What does it mean? | documentation | exact_code | A frequent e-invoicing helpdesk question: what does this IRN validation error mean? |
| D-09 | Purchasing (Emma Clarke) | What late-payment interest can Voltway Cells charge us under its contract? | documentation | not_in_docs | A buyer's question about a supplier's contract clause that the shared drive does not hold. |
| D-10 | Accounts payable (Priya Shah) | What is the salary band for an accounts payable executive? | documentation | permission | A common internal-chatbot question that must be refused: what do people in my role earn? |
| D-11 | Accounts payable (Priya Shah) | How far above the purchase order price can an invoice be before it goes on hold? | documentation | version_conflict | An AP question where an old policy copy is still on the shared drive: which tolerance applies? |
| D-12 | Tax manager (Meera Kulkarni) | When may we claim the GST credit on a supplier invoice? | documentation | rule | A common GST question since GSTR-2B became the basis for input tax credit. |

## Counts

By category: genesis 4, analytical 4, documentation 12.
Documentation by type: exact_code 1, multi_hop 1, not_in_docs 1, permission 1, procedure 1, rule 2, service_field 1, single_lookup 1, table_lookup 1, version_conflict 2 (10 types).
