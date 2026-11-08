---
title: "ERR-PAY-0430 Approver Cannot Be Proposer"
type: "error"
slug: "err-pay-0430"
summary: "Ledgerline error raised when an accounts payable clerk attempts to approve a payment proposal they created or amended."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Error code | ERR-PAY-0430 |
| Name | Approver Cannot Be Proposer |
| Module | Accounts Payable |
| Procedure | SOP-AP-003 |
| Status | current |

Error ERR-PAY-0430 is an accounts payable validation rule in Ledgerline that prevents self-approval of payment batches. As of 26 October 2026, it enforces segregation of duties during payment processing under [[sop-ap-003|SOP-AP-003 Supplier Payment Run]]. It requires an independent review and sign-off by an authorized manager before payments can proceed.

## Meaning
Error ERR-PAY-0430 indicates "Approver Cannot Be Proposer" and blocks the approval of a payment run by the same user who prepared it[^r1].

## Cause
The error is triggered when an accounts payable clerk who created or amended the payment proposal attempts to approve it[^r1].

## How to fix
To resolve error ERR-PAY-0430, the user must log out and the accounts payable manager must log in with their own credentials to perform the independent review[^r2].

## See also
* [[sop-ap-003|SOP-AP-003 Supplier Payment Run]]
* [[screen-ap-pay-03|AP-PAY-03 Payment Run]]
* [[err-bnk-0101|ERR-BNK-0101 Unverified Supplier Bank Details]]
* [[user-gwhitaker|Grace Whitaker (GWHITAKER)]]
* [[user-mkowalski|Marta Kowalski (MKOWALSKI)]]

## References

[^r1]: 02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf, p. 3, §5. Procedure: notes and common mistakes
[^r2]: 02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf, p. 4, Actions when something does not look right
