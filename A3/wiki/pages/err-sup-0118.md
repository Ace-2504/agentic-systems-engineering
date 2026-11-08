---
title: "ERR-SUP-0118 Duplicate VAT Number"
type: "error"
slug: "err-sup-0118"
summary: "Ledgerline error raised when attempting to register a supplier using a VAT registration number that already exists in master data."
audience: "staff"
status: "mixed"
sources: ["01_policies/POL-SUP-003 Supplier Policy v2.3 (1).pdf", "01_policies/POL-SUP-003 Supplier Policy v2.3.pdf", "01_policies/old/Supplier_Policy_v2.2.docx"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | ERR-SUP-0118 |
| Type | Error |
| Module | Supplier Master |
| System | Ledgerline |
| Trigger | Duplicate VAT registration number |
| Status | Current |

ERR-SUP-0118 is a Ledgerline validation error that prevents duplicate supplier onboarding across Northbridge Cycles records. As of 26 October 2026, the system actively blocks creation whenever an input VAT registration number matches an existing entry in the master data. Resolving this requires verifying existing vendor accounts before proceeding with new supplier creation.

## Meaning
ERR-SUP-0118 signifies that Ledgerline has identified a matching VAT registration number in the supplier master and refuses to create the supplier record [^r1][^r2]. 

## Cause
The error is triggered when attempting to register a supplier using a VAT registration number that already exists in the master data [^r1].

## How to fix
Staff must check existing records to confirm whether the supplier is already registered under an existing record rather than creating a duplicate entry [^r1][^r2].

## Versions and conflicts
- duplicate | Ledgerline triggers ERR-SUP-0118 and refuses record creation if the entered VAT number is already registered | Identical rule documented across duplicate source files | [^r1], [^r2]
- superseded | Under current [[pol-sup-003|POL-SUP-003]] v2.3 (effective 2026-04-01), ERR-SUP-0118 triggers and blocks registration when a VAT number already exists | In superseded POL-SUP-003 v2.2, Ledgerline raises ERR-SUP-0118 and refuses to create a second supplier if the VAT number is already registered | [^r1], [^r3]

## See also
* [[pol-sup-003|POL-SUP-003 Supplier Policy]]
* [[screen-pur-sup-01|PUR-SUP-01 Supplier Master Create]]
* [[screen-pur-sup-03|PUR-SUP-03 Supplier Enquiry]]
* [[err-sup-0031|ERR-SUP-0031 Supplier Blocked]]

## References

[^r1]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §6. Duplicate suppliers
[^r2]: 01_policies/POL-SUP-003 Supplier Policy v2.3 (1).pdf, p. 2, §6. Duplicate suppliers
[^r3]: 01_policies/old/Supplier_Policy_v2.2.docx, §6. Duplicate suppliers
