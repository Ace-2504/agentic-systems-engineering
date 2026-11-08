---
title: "ERR-BNK-0101 Unverified Supplier Bank Details"
type: "error"
slug: "err-bnk-0101"
summary: "Ledgerline error that automatically excludes suppliers missing verified banking data from the payment proposal."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| code | ERR-BNK-0101 |
| name | Unverified Supplier Bank Details |
| module | Accounts Payable |
| status | current |
| source | SOP-AP-003 |

Error ERR-BNK-0101 is an Accounts Payable validation error in Ledgerline that prevents payments to unverified accounts. It automatically excludes any supplier missing verified banking data from the payment proposal run [^r1]. When this error occurs, expected supplier invoices fail to populate on the payment screen until bank verification paperwork is resolved [^r2].

Code: ERR-BNK-0101
Name: Unverified Supplier Bank Details
Module: Accounts Payable
Status: current

## Meaning
Error ERR-BNK-0101 indicates that a supplier cannot be included in a payment proposal because their banking data has not been verified [^r1].

## Cause
The error is triggered automatically during the payment proposal generation when Ledgerline detects that a supplier is missing verified banking data [^r1]. As a result, an expected supplier invoice will be missing from screen [[screen-ap-pay-03|AP-PAY-03]] [^r2].

## How to fix
When an expected supplier invoice does not appear on screen [[screen-ap-pay-03|AP-PAY-03]] due to ERR-BNK-0101, staff must check procurement to determine whether supplier paperwork is currently awaiting bank verification [^r2].

## See also
* [[sop-ap-003|SOP-AP-003 Supplier Payment Run]]
* [[screen-ap-pay-03|AP-PAY-03 Payment Run]]
* [[err-pay-0430|ERR-PAY-0430 Approver Cannot Be Proposer]]

## References

[^r1]: 02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf, p. 4, Actions when something does not look right
