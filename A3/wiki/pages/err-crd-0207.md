---
title: "ERR-CRD-0207 Credit Limit Exceeded"
type: "error"
slug: "err-crd-0207"
summary: "Ledgerline error when sales order confirmation fails because a bike shop account exceeds its agreed credit limit."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Error code | ERR-CRD-0207 |
| Description | Credit Limit Exceeded |
| Screen | SAL-SO-01 |
| Trigger | Sales order confirmation |
| Resolution | Contact accounts to review ledger or take payment |
| Status | Current |

Error ERR-CRD-0207 is a Ledgerline order entry error encountered during sales processing under [[sop-sal-001|SOP-SAL-001]]. It occurs when an order cannot be confirmed because a customer account has breached its established credit boundary [^r1]. Staff must resolve the balance issue through the accounts department rather than attempting manual overrides [^r2].

## Meaning
The error indicates that confirming an order would place the bike shop account's balance above its agreed credit limit [^r1].

## Cause
ERR-CRD-0207 is triggered upon attempting a sales order confirmation in [[screen-sal-so-01|SAL-SO-01]] when the bike shop account exceeds its agreed credit limit [^r1].

## How to fix
Staff must not attempt to force the order through in the system [^r2]. Instead, staff must notify the accounts department to review the ledger, obtain payment in pounds, or adjust the account status before reconfirming the order [^r2].

## See also
* [[screen-sal-so-01|SAL-SO-01 Sales Order]]
* [[sop-sal-001|SOP-SAL-001 Sales Order to Despatch]]

## References

[^r1]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 4, §5. Procedure: notes and common mistakes
