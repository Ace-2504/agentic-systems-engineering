---
title: "POL-BAT-004 Battery Safety and Handling Policy"
type: "policy"
slug: "pol-bat-004"
summary: "Battery safety and handling policy governing storage limits, inspection, quarantine, transport labelling, and required handling training for lithium-cell parts across Northbridge sites."
audience: "staff"
status: "current"
sources: ["01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf", "01_policies/POL-RET-006 Returns Policy v2.1.pdf", "02_procedures/SOP-INV-004 Battery Pack Storage and Handling v1.0.pdf", "02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf", "02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| code | POL-BAT-004 |
| version | v1.2 |
| effective date | 2025-11-01 |
| status | current |
| audience | staff |

POL-BAT-004 establishes safety, handling, storage, and transport standards for all lithium-cell components at Northbridge Cycles[^r1]. It sets strict capacity caps across Manchester fire cells, mandates a 30% to 50% state of charge, and specifies dangerous-goods shipping rules[^r4][^r6][^r7][^r10]. Compliance is mandatory for all personnel handling covered stock across both Manchester and Leeds facilities[^r3][^r12].

| Field | Detail |
|---|---|
| Document Code | POL-BAT-004 |
| Version | v1.2 |
| Effective Date | 2025-11-01 |
| Status | Current |

## Clauses

### 1. Purpose and scope
POL-BAT-004 covers every lithium-cell part at Northbridge, including battery packs, cells, hub and mid-drive motors, chargers, and any item marked with the lithium-cell flag in the item master[^r1]. Purchasing parts covered by this policy is governed by [[pol-pur-001|Purchase Policy POL-PUR-001]] §6.2 and [[pol-sup-003|Supplier Policy POL-SUP-003]] §4[^r2]. In the Manchester plant, all covered parts must move directly to designated bunded battery cages, while at the Leeds unit, items must remain in the segregated storage area until required on sub-assembly benches[^r3]. Without a valid UN 38.3 test summary, lithium-ion battery stock cannot be moved by freight carriers, stored at Manchester works, or transferred to Leeds per [[sop-pur-005|SOP-PUR-005]][^r16]. Any internal design modification to lithium-ion battery management firmware or casing seals invalidates earlier UN 38.3 test documentation and requires recertification[^r17].

### 2. Storage
Battery packs are stored in the fire-cell area inside Manchester main stores across bin zones BAT-Z1 to BAT-Z4 and booked in Ledgerline to warehouse WH-MAN-STR per [[data-warehouses|warehouse records]][^r4]. The legacy warehouse code WH-MAN-BAT was merged into WH-MAN-STR in 2019 and must not be used[^r5]. No more than 1,500 battery packs may be stored in any single fire cell, limiting the Manchester fire-cell area to a maximum capacity of 6,000 packs across BAT-Z1 to BAT-Z4[^r6]. Under [[sop-inv-004|SOP-INV-004]], battery packs must be put away only into fire cells BAT-Z1 to BAT-Z4, with a mandatory check ensuring no cell exceeds the maximum limit of 1,500 packs[^r15]. Packs must be kept at a state of charge between 30% and 50% while in store, and stores staff must never charge a pack inside the store boundary[^r7]. Per [[sop-qua-001|SOP-QUA-001]], section 2.3 defines the incoming inspection acceptance criteria requiring battery packs to maintain a state of charge between 30% and 50%, failing which the pack is rejected[^r18].

### 3. Damaged packs
Any damaged, swollen, wet, or dropped battery pack must be moved at once to the red quarantine bin in fire cell BAT-Z4 and reported to Quality in the same shift with a non-conformance report on screen [[screen-qa-ncr-02|QA-NCR-02]][^r8]. Quarantined damaged packs in the red bin inside fire cell BAT-Z4 must be placed flat and fully covered by vermiculite granules using heat-resistant gloves per [[sop-qua-002|SOP-QUA-002]][^r9]. Battery packs returned under warranty governed by [[pol-ret-006|POL-RET-006]] must never be returned to general stock and must be routed to battery refurbishment (cost centre PRD-09) or recycling[^r13].

### 4. Transport
A standalone battery pack shipped on its own is declared as UN3480, whereas a pack fitted to a bicycle or packed with it is declared as UN3481[^r10]. Every parcel containing a battery pack must carry the lithium battery handling label, item PKG-LBL-UN under [[items-pkg|PKG-* items]], affixed flat and clearly visible alongside the carrier delivery note[^r11]. Returned lithium battery packs must be transported using a carrier's dangerous-goods service rather than ordinary parcel post[^r14].

### 5. Training
Anyone handling [[items-bat|battery packs]] must complete the battery-handling course BHT-01 before their first shift in the fire-cell area and renew it every 24 months[^r12].

## Who it applies to
This policy applies to all personnel purchasing, receiving, storing, assembling, testing, or shipping lithium-cell components and [[items-bat|BAT-* items]] at both the Manchester plant and the Leeds unit[^r1][^r3]. It directly binds stores and sub-assembly operators, quality inspectors executing incoming goods inspections, logistics teams preparing dangerous-goods shipments, and any staff entering the Manchester fire-cell area[^r3][^r11][^r12][^r18].

## Versions and conflicts
- Battery packs in Ledgerline are assigned to warehouse WH-MAN-STR | The legacy warehouse code WH-MAN-BAT was merged into WH-MAN-STR in 2019 and must not be used | POL-BAT-004 v1.2 (2025-11-01) §2 [^r4][^r5] | superseded

## See also
- [[pol-pur-001|POL-PUR-001 Purchase Policy]]
- [[pol-sup-003|POL-SUP-003 Supplier Policy]]
- [[pol-ret-006|POL-RET-006 Returns Policy]]
- [[sop-inv-004|SOP-INV-004 Battery Pack Storage and Handling]]
- [[sop-pur-005|SOP-PUR-005 Certificate Renewal (UN 38.3)]]
- [[sop-qua-001|SOP-QUA-001 Incoming Inspection]]
- [[sop-qua-002|SOP-QUA-002 Damaged Battery Pack Quarantine]]
- [[screen-qa-ncr-02|QA-NCR-02 Non-Conformance Report Entry]]
- [[items-bat|BAT-* items]]
- [[items-pkg|PKG-* items]]
- [[data-warehouses|Warehouses]]

## References

[^r1]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 1, §1. Purpose and scope
[^r4]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 2, §2. Storage
[^r6]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 2, §2. Storage
[^r7]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 2, §2. Storage
[^r10]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 4, §4. Transport
[^r3]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 1, §1. Purpose and scope
[^r12]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 4, §5. Training
[^r2]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 1, §1. Purpose and scope
[^r16]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 1, §1. Purpose
[^r17]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 1, §1. Purpose
[^r5]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 2, §2. Storage
[^r15]: 02_procedures/SOP-INV-004 Battery Pack Storage and Handling v1.0.pdf, p. 3, §5. Procedure
[^r18]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 3, §5. Procedure
[^r8]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 3, §3. Damaged packs
[^r9]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 3, §3. Damaged packs
[^r13]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 3, §3. Warranty returns from bike shops
[^r11]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 4, §4. Transport
[^r14]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 3, §3. Warranty returns from bike shops
