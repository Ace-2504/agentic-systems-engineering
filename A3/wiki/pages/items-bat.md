---
title: "BAT-* items"
type: "item-family"
slug: "items-bat"
summary: "Rules, storage limits, dangerous-goods transport, and UN 38.3 compliance controls governing BAT-* lithium-cell battery packs across purchasing, assembly, and warehousing."
audience: "staff"
status: "mixed"
sources: ["01_policies/AMD-SUP-2026-02 Amendment 2 Supplier Policy.pdf", "01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf", "01_policies/POL-DRP-009 Data Retention Policy v1.4.pdf", "01_policies/POL-HSE-010 Health and Safety Policy v5.0.pdf", "01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf", "01_policies/POL-QUA-005 Quality Policy v3.0.pdf", "01_policies/POL-SUP-003 Supplier Policy v2.3.pdf", "01_policies/old/Purchase Policy v4.0.docx", "01_policies/old/purchase_policy_v3_2019.docx", "02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf", "02_procedures/SOP-INV-004 Battery Pack Storage and Handling v1.0.pdf", "02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf", "02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf", "02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf", "02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf", "02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf", "02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf", "02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf", "02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf", "02_procedures/old/SOP-PUR-001 Supplier onboarding v2.0 (2021).docx", "02_procedures/sop_inv_001_goods_receipt_v2.docx"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Item prefix | BAT-* |
| Category | Lithium-cell battery packs |
| Storage location | WH-MAN-STR (fire cells BAT-Z1 to BAT-Z4) |
| Storage capacity | 1,500 packs per cell (6,000 packs total) |
| Inspection level | AQL 0.65 |
| Transport class | UN3480 (alone) / UN3481 (with bike) |

BAT-* items are lithium-cell battery packs utilized across electric bicycle manufacturing and spare parts distribution [^r2][^r10]. As of Monday 26 October 2026, purchasing, receiving, storing, assembling, and shipping these packs requires strict compliance with dangerous-goods handling protocols and active UN 38.3 test certification [^r1][^r2][^r5]. All movements and environmental tolerances are strictly monitored across the Manchester and Leeds sites to prevent fire hazards and product degradation [^r4][^r8][^r22].

## Items
* BAT-* lithium-cell battery packs [^r2].
* Associated lithium-cell assemblies such as hub motors and chargers marked `cell_safety = 1` or designated lithium-cell in the item master [^r10][^r13].

## Rules that apply

### Sourcing, Quotations, and Contracts
* **UN 38.3 certification**: Parts marked lithium-cell can only be purchased from active suppliers holding a valid UN 38.3 test certificate uploaded and verified in Ledgerline ERP [^r10][^r13]. Before placing any purchase order, staff must confirm that the UN 38.3 certificate was issued within the last 12 months and has a valid-to date at least 60 days past the order date [^r1]. New purchase orders cannot be raised once fewer than 60 days remain before certificate expiry [^r24].
* **Quotations and supplier selection**: Quotations may only be compared among suppliers with a valid UN 38.3 test certificate, and technical compliance takes precedence over price [^r26]. If a supplier submits an expired, incomplete, or ambiguous certificate, its quotation must be set aside until quality engineering verifies the testing documentation [^r27]. Furthermore, lithium-cell suppliers cannot be replaced merely on the basis of a cheaper quotation if an incumbent supplier holds an active rate contract [^r11].
* **Rate contracts**: Rate contracts for battery packs are permitted to run for six-month terms rather than standard 12-month annual agreements [^r23].
* **Engineering changes**: Any engineering modification to a lithium-cell part introducing an alternate cell maker, modified design, or chemistry change requires a fresh UN 38.3 test report before Ledgerline release [^r14][^r21]. Releasing an unverified alteration causes incoming battery packs to be quarantined at Manchester and stops sub-assembly at Leeds [^r22].

### Receiving and Quality Inspection
* **Goods inwards quarantine**: Lithium-cell shipments must be booked into warehouse WH-MAN-QC upon receipt and cannot be transferred to Manchester main stores fire-cell storage until Quality approves them [^r34]. Parcels showing outer packaging damage such as tears, dents, dampness, or crushed corners must be rejected at the loading bay, photographed, and reported to Quality under [[sop-qua-002|SOP-QUA-002]] [^r35]. If an active UN 38.3 certificate is missing or lapsed upon arrival at Manchester or Leeds, Goods Inwards must immediately place the delivery into quarantine [^r25].
* **Incoming quality control**: Under [[pol-qua-005|POL-QUA-005]], lithium-cell parts undergo inspection at AQL 0.65 [^r12]. Every sampled pack requires an open-circuit voltage check [^r12][^r28].
* **State of charge (SoC)**: Packs must arrive and remain at an SoC between 30% and 50%; any sample pack falling below 30% or exceeding 50% must be rejected under [[pol-bat-004|POL-BAT-004]] §2.3 [^r3][^r28]. If a single sample pack fails this requirement, the entire lot is declared non-conforming and cannot be resampled or topped up before assembly [^r29].

### Storage and Handling
* **Warehouse locations**: BAT-* packs must be stored solely in warehouse WH-MAN-STR within fire cells BAT-Z1 to BAT-Z4 [^r2][^r17]. Each cell holds a maximum of 1,500 packs, capping total warehouse capacity at 6,000 packs [^r2][^r17].
* **Stacking and rotation**: Battery cartons must remain on pallets during transit and must never be stacked more than four cartons high to prevent crushing internal pack enclosures [^r17][^r18]. Stock must be issued on a FIFO basis according to carton label dates [^r17].
* **Charging prohibition**: Battery packs must never be charged while in the store [^r3].

### Production and Work Orders
* **Serial number tracking**: Battery packs are excluded from standard production backflushing and must be individually issued against work orders by serial number via [[screen-inv-mrn-08|INV-MRN-08]] [^r19].
* **Validation blocks**: If a pack serial number fails validation on [[screen-inv-mrn-08|INV-MRN-08]], the completed electric bicycle cannot move to finished goods packing until the inventory team reconciles the physical pack with the Ledgerline system record [^r20].

### Damaged Packs, Safety, and Fire Procedures
* **Quarantine of damaged packs**: Damaged, dropped, wet, or swollen packs must be placed flat and covered in vermiculite inside the red quarantine bin located in fire cell BAT-Z4, and logged on [[screen-qa-ncr-02|QA-NCR-02]] during the same shift [^r4]. They must also be booked to quality hold on [[screen-inv-qch-11|INV-QCH-11]] [^r30]. Quality engineering must decide within 24 hours whether to return the pack to the supplier, refurbish it under PRD-09, or scrap it for recycling [^r31].
* **Fire emergencies**: If a battery pack smokes or ignites, personnel must raise the alarm, evacuate the area, and notify fire wardens, as only trained fire wardens may approach a burning pack [^r8]. Standard water or carbon dioxide extinguishers are ineffective on burning packs and can trigger dangerous flare-ups [^r9].

### Despatch, Transport, and Returns
* **Dangerous-goods transport**: When shipped alone, battery packs are consigned under UN3480; when packed with or installed on a bicycle, they are consigned under UN3481, requiring the PKG-LBL-UN handling label [^r5].
* **Sales despatch**: Outbound shipments containing battery packs must have a lithium battery label printed before posting despatch in Ledgerline, or posting is blocked by [[err-dlv-0320|ERR-DLV-0320]] [^r32]. Consignments must be booked with Moorland Logistics under dangerous-goods service code DGX using screen [[screen-sal-frt-12|SAL-FRT-12]] [^r33].
* **Returns to vendor (RTV)**: Supplier returns must only use dangerous-goods carrier services with UN3480 labels fixed to approved exterior crates [^r15]. If compliant transport boxes or UN3480 labels are missing or damaged, carrier collections must not be booked until proper packaging is obtained through the dispatch supervisor [^r16].

### Data Retention
* Quality must retain battery end-of-line test results for 15 years [^r6].
* Purchasing must retain supplier UN 38.3 test certificates for 10 years after a supplier is blocked [^r7].

## Versions and conflicts
* **UN 38.3 upload timing**: Today, suppliers must have a verified UN 38.3 test certificate uploaded in Ledgerline before any order is placed, valid for at least 60 days post-order [^r1][^r10][^r24]. Under superseded [[sop-pur-001|SOP-PUR-001]] v2.0, suppliers were permitted to provide test reports within three months following the initial order [^r38]. Kind: `superseded`.
* **Scope of lithium certification**: Today, all lithium-cell components (including battery packs, hub motors, and chargers marked `cell_safety = 1`) require uploaded UN 38.3 certification [^r10][^r13]. Superseded policy [[pol-pur-001|POL-PUR-001]] v3.0 mandated certification solely for battery packs, explicitly excluding hub motors and chargers [^r37]. Kind: `superseded`.

## See also
* [[amd-sup-2026-02|AMD-SUP-2026-02 Amendment 2 to the Supplier Policy]]
* [[err-dlv-0320|ERR-DLV-0320 Battery Label Required]]
* [[items-pkg|PKG-* items]]
* [[pol-bat-004|POL-BAT-004 Battery Safety and Handling Policy]]
* [[pol-drp-009|POL-DRP-009 Data Retention Policy]]
* [[pol-hse-010|POL-HSE-010 Health and Safety Policy]]
* [[pol-pur-001|POL-PUR-001 Purchase Policy]]
* [[pol-qua-005|POL-QUA-005 Quality Policy]]
* [[pol-sup-003|POL-SUP-003 Supplier Policy]]
* [[screen-inv-mrn-08|INV-MRN-08 Material Issue Entry]]
* [[screen-inv-qch-11|INV-QCH-11 Quality Hold Entry]]
* [[screen-qa-ncr-02|QA-NCR-02 Non-Conformance Report Entry]]
* [[screen-sal-frt-12|SAL-FRT-12 Carrier Booking Quote]]
* [[sop-inv-002|SOP-INV-002 Returns to Vendor (RTV)]]
* [[sop-inv-004|SOP-INV-004 Battery Pack Storage and Handling]]
* [[sop-prd-001|SOP-PRD-001 Work Order Release and Backflush]]
* [[sop-prd-002|SOP-PRD-002 Engineering Change (ECN)]]
* [[sop-pur-004|SOP-PUR-004 Rate Contract Maintenance]]
* [[sop-pur-005|SOP-PUR-005 Certificate Renewal (UN 38.3)]]
* [[sop-pur-006|SOP-PUR-006 Quotations and Supplier Selection]]
* [[sop-qua-001|SOP-QUA-001 Incoming Inspection]]
* [[sop-qua-002|SOP-QUA-002 Damaged Battery Pack Quarantine]]
* [[sop-sal-001|SOP-SAL-001 Sales Order to Despatch]]

## References

[^r2]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 2, §2. Storage
[^r10]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §6. Supplier qualification
[^r1]: 01_policies/AMD-SUP-2026-02 Amendment 2 Supplier Policy.pdf, p. 1, §3. What purchase staff must do
[^r5]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 4, §4. Transport
[^r4]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 3, §3. Damaged packs
[^r8]: 01_policies/POL-HSE-010 Health and Safety Policy v5.0.pdf, p. 3, §4. Battery fires
[^r22]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 3, §5. Procedure: notes and common mistakes
[^r13]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §4. UN 38.3 certificates
[^r24]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 3, §5. Procedure
[^r26]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 3, §5. Procedure
[^r27]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 4, What to do when something does not look right
[^r11]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §6. Supplier qualification
[^r23]: 02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf, p. 3, §5. Procedure
[^r14]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §4. UN 38.3 certificates
[^r21]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 3, §5. Procedure
[^r34]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure
[^r35]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure: notes and common mistakes
[^r25]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 2, §3. Responsibilities
[^r12]: 01_policies/POL-QUA-005 Quality Policy v3.0.pdf, p. 2, §3. Incoming inspection
[^r28]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 3, §5. Procedure
[^r3]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 2, §2. Storage
[^r29]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r17]: 02_procedures/SOP-INV-004 Battery Pack Storage and Handling v1.0.pdf, p. 3, §5. Procedure
[^r18]: 02_procedures/SOP-INV-004 Battery Pack Storage and Handling v1.0.pdf, p. 3, §5. Procedure
[^r19]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 3, §5. Procedure
[^r20]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r30]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 3, §5. Procedure
[^r31]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 3, §5. Procedure
[^r9]: 01_policies/POL-HSE-010 Health and Safety Policy v5.0.pdf, p. 4, §4. Battery fires
[^r32]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 3, §5. Procedure
[^r33]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 3, §5. Procedure: notes and common mistakes
[^r15]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r16]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r6]: 01_policies/POL-DRP-009 Data Retention Policy v1.4.pdf, p. 3, Table 1. Retention periods
[^r7]: 01_policies/POL-DRP-009 Data Retention Policy v1.4.pdf, p. 3, Table 1. Retention periods
[^r38]: 02_procedures/old/SOP-PUR-001 Supplier onboarding v2.0 (2021).docx, §5. Procedure
[^r37]: 01_policies/old/purchase_policy_v3_2019.docx, # 6. Supplier qualification
