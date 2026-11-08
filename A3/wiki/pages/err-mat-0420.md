---
title: "ERR-MAT-0420 Match Override Permission Denied"
type: "error"
slug: "err-mat-0420"
summary: "Ledgerline error triggered when a user lacking AP manager permissions attempts to override a three-way invoice match hold."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Error code | ERR-MAT-0420 |
| System | Ledgerline |
| Type | Permission denied |
| Applies to | Three-way match hold override |
| Status | Current |

Error ERR-MAT-0420 is a Ledgerline system error generated when an unauthorized user attempts to bypass a match hold during invoice processing [^r1]. Under [[sop-ap-001|SOP-AP-001]], only the AP manager possesses authorization to override a three-way invoice match hold [^r1]. Repeated override attempts by unauthorized staff will not clear the hold [^r2].

## Meaning

The error indicates that the current user lacks the required override permission to clear a match hold [^r2].

## Cause

The error is generated whenever any user other than the AP manager attempts to override a three-way invoice match hold in Ledgerline [^r1].

## How to fix

Users without AP manager authorization must stop repeated override attempts, as additional tries will not clear the match hold [^r2]. The hold must instead be escalated to the AP manager for review and override [^r1].

## See also

* [[sop-ap-001|SOP-AP-001 Three-Way Invoice Matching]]
* [[screen-ap-inv-01|AP-INV-01 Supplier Invoice Entry]]
* [[topic-price-tolerance]]
* [[user-gwhitaker]]
* [[user-mkowalski]]

## References

[^r1]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 4, Common mistakes when entering invoices
