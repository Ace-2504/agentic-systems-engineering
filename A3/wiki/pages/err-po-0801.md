---
title: "ERR-PO-0801 Cannot Amend Order in CN, RJ or CL Status"
type: "error"
slug: "err-po-0801"
summary: "Ledgerline error thrown when attempting to amend a purchase order that is in cancelled, rejected, or closed status."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | ERR-PO-0801 |
| Screen | PUR-POM-06 |
| Status | Current |
| Procedure | SOP-PUR-003 |

Error ERR-PO-0801 prevents modifications to purchase orders that have already reached a concluded lifecycle state in Ledgerline [^r1]. It blocks staff from amending orders that are marked as cancelled, rejected, or closed [^r1]. Users must raise a replacement order rather than attempting to alter the existing record [^r2].

Code: ERR-PO-0801
Screen: [[screen-pur-pom-06|PUR-POM-06]]
Status: Current
Procedure: [[sop-pur-003|SOP-PUR-003]]

## Meaning
Error ERR-PO-0801 indicates that a purchase order cannot be amended because it is in cancelled (CN), rejected (RJ), or closed (CL) status [^r1].

## Cause
The error is returned when an attempt is made to amend a purchase order that has already been placed into cancelled (CN), rejected (RJ), or closed (CL) status [^r1].

## How to fix
When ERR-PO-0801 occurs, staff must check the historical log to identify who closed or cancelled the file [^r2]. Staff must raise a replacement transaction rather than forcing changes on concluded records [^r2].

## See also
* [[sop-pur-003|SOP-PUR-003 Purchase Order Amendment]]
* [[screen-pur-pom-06|PUR-POM-06 Purchase Order Amendment]]

## References

[^r1]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 4, §5. Procedure: notes and common mistakes
