# CAPSTONE: Ask Northbridge for accounts payable

Built on the course's **Finance · payables** module kit (`fin_payables`), with my own changes to its sandbox. All companies, people and amounts are fictional; amounts are in rupees.

## Summary

1. **The process and the people.** Paying a supplier's invoice at Northbridge Cycles, on the course's Finance · payables kit, because it has the same failure pattern as my own Before: money leaves after checks, and "paid" isn't really paid. My own hostel refund is hard to sandbox on its own: it spans EduDesk, four office modules, the Accounts ERP and the bank, and faking all of them is far beyond the course's budget for one module (3 screens, about 8 services), so I use the course's kit option. Priya Shah (accounts payable) and Emma Clarke (purchasing) speak to the assistant; Daniel Okafor, Ganesh Pawar and Vikram Nair decide in their own logins. The record lives in Ledgerline, the ERP.
2. **The sandbox.** The kit's Ledgerline (44 records, hold codes with release lists, Friday payment runs, and its traps: the silent park, two invoices numbered 4471, the resent 4471-R), with my changes: Indian setting (Rs., GST 18%, TDS), a contract and Voltway's discount offer, 300 packs broken in transit, a draft queue where a person approves every entry within 24 hours, and a bank statement, return file and bank-alerts mailbox with a spoofed email.
3. **Five activities.** `invoice_status`: find an invoice and say whose it is. `explain_hold`: why it is on hold, who can clear it, by when. `enter_invoice`: draft an invoice or credit note for approval. `refer_hold`: send a hold to the person allowed to clear it. `schedule_payment`: draft a payment for a Friday run and record the bank's answer.
4. **Two never-events.** Nothing is written, released or approved without the right person's recorded authority. The assistant never says paid, scheduled, released or posted while anything is held, parked, waiting, still a draft or not confirmed by the bank.
5. **Open questions.** How do we stop Priya rubber-stamping drafts she approves 98% of the time? And when the bank's email and statement disagree, how long does the agent wait, and which wins?

**The worked example:** today Voltway's 0.5% discount on invoice 4471 lapses while the invoice sits on hold; with the assistant it can be taken in the 16th October run (Rs.1,19,952, about 4.4% a year on the money paid early, which Vikram weighs against what that money costs Northbridge), and "paid" is said only after the bank confirms.

The full design behind this summary (the people, the money, the approval loop, the bank check, guardrails, tests and what changes without new code) is in `CAPSTONE_design.md`, and the picture is `CAPSTONE_SYSTEM_DESIGN_v13.excalidraw`.
