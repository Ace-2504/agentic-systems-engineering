---
title: "ERR-RTV-0230 RTV Refused Against Invoiced Receipt"
type: "error"
slug: "err-rtv-0230"
summary: "Ledgerline error when an RTV is attempted against an already invoiced receipt, requiring Accounts Payable to raise a debit note."
audience: "staff"
status: "current"
sources: ["01_policies/POL-RET-006 Returns Policy v2.1.pdf", "02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Error code | ERR-RTV-0230 |
| System | Ledgerline |
| Screen | INV-RTV-07 |
| Trigger | RTV attempted on invoiced receipt |
| Resolution | Pass docket to Accounts Payable for debit note on AP-DBN-04 |

Error ERR-RTV-0230 is a Ledgerline system error generated when attempting to return goods to a supplier against a receipt that has already been billed. It prevents warehouse staff from reversing or processing returns directly once the transaction has reached the purchase ledger. As of 26 October 2026, the issue is handled by routing the documentation to Accounts Payable to generate a vendor debit note.

Error code: ERR-RTV-0230  
System: Ledgerline  
Screen: INV-RTV-07  
Trigger: RTV attempted on invoiced receipt  
Resolution: Raise debit note via Accounts Payable on AP-DBN-04  

## Meaning
ERR-RTV-0230 indicates that a return to vendor cannot be processed because the relevant purchase order receipt has already been invoiced and posted [^r1]. It signifies that the goods receipt note has already been matched to an invoice or passed for payment in Ledgerline [^r3].

## Cause
The error is triggered on screen [[screen-inv-rtv-07|INV-RTV-07]] when a user attempts to process an RTV against an invoiced purchase order receipt [^r1]. It occurs when an operator attempts to raise a return against a receipt that is already matched or cleared for payment [^r3].

## How to fix
When ERR-RTV-0230 occurs, users must not reverse the receipt or force the transaction [^r4]. Staff must note the purchase order reference and pass the quarantine docket to the purchase ledger team [^r2]. Users must contact accounts payable to raise a debit note against the vendor account instead [^r4]. Accounts payable then processes the debit note on screen [[screen-ap-dbn-04|AP-DBN-04]] [^r2].

## See also
* [[pol-ret-006|POL-RET-006 Returns Policy]]
* [[sop-inv-002|SOP-INV-002 Returns to Vendor (RTV)]]
* [[screen-inv-rtv-07|INV-RTV-07 Return To Vendor Entry]]
* [[screen-ap-dbn-04|AP-DBN-04 Debit Note Entry]]

## References

[^r1]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 2, §2. Returns to suppliers
[^r3]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r4]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r2]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 2, §2. Returns to suppliers
