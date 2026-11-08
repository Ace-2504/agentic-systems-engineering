---
title: "INV-RTV-07 Return To Vendor Entry"
type: "screen"
slug: "screen-inv-rtv-07"
summary: "Ledgerline screen used by stock control within 30 days of receipt to generate return to vendor documentation and reverse receipt accruals."
audience: "staff"
status: "current"
sources: ["01_policies/POL-RET-006 Returns Policy v2.1.pdf", "02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | INV-RTV-07 |
| Application | Ledgerline |
| Purpose | Return to Vendor Entry |
| Used by | Stock control |
| Timeframe | Within 30 days of receipt |
| Status | Current |

Screen INV-RTV-07 is the Ledgerline interface used by stock control to generate return to vendor documentation within 30 days of receipt [^r1]. It clears items from quarantine and reverses the receipt accrual recorded against the purchase order [^r1]. Returns cannot be processed through this screen once a supplier invoice has been posted [^r2].

## What it is for

Stock control uses screen INV-RTV-07 within 30 days of delivery to raise returns against the goods received note (GRN) [^r1][^r3]. Processing a return on this screen generates return to vendor documentation, clears the items out of quarantine, and reverses the receipt accrual on the purchase order [^r1]. Before confirming a return, users must verify that the stock currently sits in incoming or general inspection, that it is not committed to an active works order, and that the status flag indicates the line has not undergone purchase ledger processing [^r5].

## Fields

Staff raising a return on screen INV-RTV-07 must verify the part description, PO reference, and quantity received against the original GRN [^r3]. The screen contains a rejection quantity field, which prevents entry of any quantity greater than the unissued balance remaining on the receipt line [^r4]. Users must also check the line status flag to verify that purchase ledger processing has not taken place [^r5].

## Messages

The screen displays error [[err-rtv-0230|ERR-RTV-0230]] when a user attempts to process a return for a line where the supplier invoice has already been posted [^r2].

## See also

* [[err-rtv-0230|ERR-RTV-0230 RTV Refused Against Invoiced Receipt]]
* [[pol-ret-006|POL-RET-006 Returns Policy]]
* [[sop-inv-002|SOP-INV-002 Returns to Vendor (RTV)]]

## References

[^r1]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 2, §2. Returns to suppliers
[^r2]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 2, §2. Returns to suppliers
[^r3]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r5]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r4]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 4, §5. Procedure: notes and common mistakes
