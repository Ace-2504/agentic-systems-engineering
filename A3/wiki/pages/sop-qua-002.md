---
title: "SOP-QUA-002 Damaged Battery Pack Quarantine"
type: "procedure"
slug: "sop-qua-002"
summary: "Standard operating procedure for isolating, tagging, and booking damaged, dropped, or distressed battery packs into Ledgerline quarantine."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-INV-004 Battery Pack Storage and Handling v1.0.pdf", "02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| code | SOP-QUA-002 |
| owner | Pieter Jansen |
| approver | Henrik Weber |
| version | 1.1 |
| effective date | 2025-11-01 |
| status | current |

SOP-QUA-002 governs the immediate physical isolation, identification, and system quarantine of damaged, weeping, or dropped power packs across Northbridge Cycles facilities [^r3][^r6]. Version 1.1 remains current as of 26 October 2026, authored by quality manager [[user-pjansen|Pieter Jansen]] and approved by plant head [[user-hweber|Henrik Weber]] [^r3]. The procedure prevents hazardous units from remaining in active circulation or being allocated to production runs [^r11][^r14]. Any pack exhibiting heat or sweet odours requires immediate emergency bench evacuation rather than standard handling [^r5].

## Steps
1. Assembly operators who detect a damaged or weeping pack must halt work immediately, raise a physical quarantine flag, and alert the line supervisor without leaving the area unattended [^r7].
2. For inbound deliveries at goods-in, warehouse staff must reject consignments with crushed cartons or torn moisture barriers at the bay, place affected items directly into quarantine, and sign the delivery sheet [^r9].
3. Under [[sop-inv-004|SOP-INV-004]], any battery carton that has been dropped or shows signs of impact, crushing, dampness, or drops must not be stored in fire cells but moved immediately to quarantine holding regardless of visible damage [^r1][^r2].
4. Wearing protective gloves and eye protection, line supervisors must arrange physical transfer without testing, charging, or dismantling the unit [^r8][^r12].
5. Complete a physical red quarantine tie-on card by hand, attach it to the fireproof container, and log the serial number, reporting department, defect, and handler initials in the battery store quarantine register [^r1][^r2][^r19].
6. Within the same shift, raise a non-conformance report on screen [[screen-qa-ncr-02|QA-NCR-02]] with photographic evidence of damage, serial plate, and terminal condition [^r13]. If the serial number is defaced or unreadable, enter the batch reference on screen [[screen-qa-ncr-02|QA-NCR-02]], note it in the narrative box, and submit it for an immediate physical check by Quality [^r17].
7. Book the unit to quality hold on screen [[screen-inv-qch-11|INV-QCH-11]] to remove it from available stock and prevent allocation [^r2][^r14]. If the quality engineer is off-site, the shift supervisor must execute the transaction to prevent overnight planning runs from allocating the unit to a build order [^r11].
8. If screen [[screen-inv-qch-11|INV-QCH-11]] signals an existing allocation, the stores supervisor must strip the allocation from the production order before completing the quarantine transfer [^r18].
9. Quality must decide within 24 hours whether to return the pack to the supplier, refurbish it under PRD-09, or send it for recycling [^r15].
10. If a pack inside the red bin exhibits heat, smoke, or hissing, personnel must close the fire cell door, alert the shift supervisor immediately, and sound the local alarm without taking photographs or accessing terminals [^r16].

## Forms and screens
* Physical quarantine tie-on card (red tag) [^r1][^r2][^r19]
* Battery store quarantine register [^r19]
* Screen [[screen-qa-ncr-02|QA-NCR-02]] (Non-Conformance Report Entry) [^r13][^r17]
* Screen [[screen-inv-qch-11|INV-QCH-11]] (Quality Hold Entry) [^r14][^r18]

## Checks and approvals
* Operators must verify that a suspect pack is never left unattended once flagged [^r7].
* Supervisors must confirm that units are never tested, charged, or dismantled during handling [^r8].
* Quality engineers apply the quarantine hold in Ledgerline ERP, issue vendor defect notifications, liaise with chemical waste carriers, and authorise final scrap or return transactions [^r10].
* The stores supervisor checks and strips build order allocations when flagged on screen [[screen-inv-qch-11|INV-QCH-11]] [^r18].
* Quality holds approval authority for the final disposition decision within 24 hours [^r15].

## Versions and conflicts
* Contradiction | Damaged packs are placed into an outdoor fire-rated quarantine locker or external container using a fire-retardant transit drum and vermiculite bedding | Damaged packs are moved to the red quarantine bin inside fire cell BAT-Z4 | SOP-QUA-002 v1.1, 2025-11-01, p. 1 (§1) & p. 2 (§3) vs. p. 3 (§5) | contradiction

## See also
* [[sop-inv-004|SOP-INV-004 Battery Pack Storage and Handling]]
* [[screen-inv-qch-11|INV-QCH-11 Quality Hold Entry]]
* [[screen-qa-ncr-02|QA-NCR-02 Non-Conformance Report Entry]]
* [[items-bat|BAT-* items]]
* [[pol-bat-004|POL-BAT-004 Battery Safety and Handling Policy]]
* [[user-pjansen|Pieter Jansen (PJANSEN)]]
* [[user-hweber|Henrik Weber (HWEBER)]]

## References

[^r3]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 1, Damaged Battery Pack Quarantine
[^r6]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 2, §2. Scope
[^r11]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 3, §3. Responsibilities
[^r14]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 1, §1. Purpose
[^r7]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 2, §3. Responsibilities
[^r9]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 2, §3. Responsibilities
[^r1]: 02_procedures/SOP-INV-004 Battery Pack Storage and Handling v1.0.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-INV-004 Battery Pack Storage and Handling v1.0.pdf, p. 4, What to do when something does not look right
[^r8]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 2, §3. Responsibilities
[^r12]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 3, §5. Procedure
[^r19]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 5, §6. Records
[^r13]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 3, §5. Procedure
[^r17]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r18]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r15]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 3, §5. Procedure
[^r16]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r10]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 2, §3. Responsibilities
