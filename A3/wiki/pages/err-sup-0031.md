---
title: "ERR-SUP-0031 Supplier Blocked"
type: "error"
slug: "err-sup-0031"
summary: "Ledgerline error raised when attempting to place a new purchase order with a supplier marked BLOCKED."
audience: "staff"
status: "mixed"
sources: ["01_policies/POL-SUP-003 Supplier Policy v2.3 (1).pdf", "01_policies/POL-SUP-003 Supplier Policy v2.3.pdf", "01_policies/old/Supplier_Policy_v2.2.docx"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Error code | ERR-SUP-0031 |
| System | Ledgerline |
| Trigger | Placing order with BLOCKED supplier |
| Policy | POL-SUP-003 |
| Status | Current |

Ledgerline error ERR-SUP-0031 indicates that an order cannot be processed because the selected supplier has been marked with BLOCKED status [^r1]. As of 26 October 2026, the system strictly refuses new purchase orders whenever an order is attempted against a blocked vendor record [^r1][^r2]. Users must verify vendor status under [[pol-sup-003|POL-SUP-003]] before attempting to re-issue orders [^r1].

## Meaning

ERR-SUP-0031 indicates that Ledgerline has blocked an order attempt because the targeted vendor record carries a BLOCKED status flag [^r1]. When this error is returned, the system refuses to create or process the new purchase order [^r2].

## Cause

The error is triggered whenever a user attempts to place a new purchase order with a supplier whose profile is set to BLOCKED [^r1][^r2].

## How to fix

To resolve ERR-SUP-0031, users must not proceed with order placement against the vendor while the block remains active [^r1][^r2]. Operational resolution requires reviewing the supplier's standing under [[pol-sup-003|POL-SUP-003]] procedures regarding blocking and unblocking [^r1].

## Versions and conflicts

* **Current rule (in force 2026-04-01):** Ledgerline returns ERR-SUP-0031 and refuses new purchase orders when an attempt is made to place a new purchase order with a supplier marked BLOCKED [^r1][^r2].
* **Superseded rule:** Superseded documentation in POL-SUP-003 v2.2 similarly stated Ledgerline displays ERR-SUP-0031 when attempting to place a new purchase order with a blocked supplier [^r3].
* **Duplicate copy:** A duplicate file of POL-SUP-003 v2.3 restates the identical blocking error condition [^r2].

## See also

* [[pol-sup-003|POL-SUP-003 Supplier Policy]]
* [[screen-pur-sup-03|PUR-SUP-03 Supplier Enquiry]]
* [[err-sup-0118|ERR-SUP-0118 Duplicate VAT Number]]

## References

[^r1]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §5. Blocking and unblocking
[^r2]: 01_policies/POL-SUP-003 Supplier Policy v2.3 (1).pdf, p. 2, §5. Blocking and unblocking
[^r3]: 01_policies/old/Supplier_Policy_v2.2.docx, §5. Blocking and unblocking
