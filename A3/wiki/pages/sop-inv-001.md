---
title: "SOP-INV-001 Goods Receipt"
type: "procedure"
slug: "sop-inv-001"
summary: "Standard operating procedure for booking incoming deliveries against purchase orders across Manchester and Leeds sites."
audience: "staff"
status: "current"
sources: ["02_procedures/sop_inv_001_goods_receipt_v2.docx"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-INV-001 |
| Title | Goods Receipt |
| Owner | [[user-cshaw|Callum Shaw]] |
| Version | 2.0 |
| Effective date | 2024-10-01 |
| Status | current |
| Scope | Manchester plant and Leeds unit |

SOP-INV-001 defines the goods receiving process for incoming consignments across the Manchester plant and Leeds unit[^r2]. It governs receipts against valid, released purchase orders for production parts, raw materials, tooling, and consumables as of 26 October 2026[^r2][^r4]. Special handling applies to incoming [[items-bat|lithium-cell parts]], requiring strict quarantine and parcel refusal protocols for damaged packaging[^r7][^r8].

## Steps

1. Verify that the incoming delivery corresponds to an existing purchase order, as unpurchased deliveries, customer returns, and inter-site transfers are excluded from this procedure[^r2][^r3].
2. Confirm that the purchase order holds status RL before attempting receipt, as Ledgerline blocks unreleased orders[^r4].
3. Open screen [[screen-inv-grn-03|INV-GRN-03]], input the PO number, and select Fetch[^r5].
4. Input the received quantity and enter the supplier's delivery note number into the Remarks field[^r5].
5. Ensure distinct Goods Receipt Notes are generated for part deliveries without exceeding the PO balance[^r6].
6. For [[items-bat|lithium-cell parts]], route the receipt directly into the quality hold warehouse WH-MAN-QC[^r7].
7. If battery delivery packaging is damaged, refuse receipt from the carrier, capture photographs, and notify Quality immediately[^r8].
8. Select Save on [[screen-inv-grn-03|INV-GRN-03]] to record the transaction[^r5].

## Forms and screens

* Screen [[screen-inv-grn-03|INV-GRN-03]] (Goods Receipt Note) is used to look up purchase orders, specify received quantities, enter delivery note references, and record receipts[^r5].

## Checks and approvals

* Purchase order status checks: Only purchase orders with status RL can be received; attempting to process orders with other statuses triggers [[err-grn-0102|ERR-GRN-0102]][^r4].
* Quantity checks: Ledgerline blocks any receipt quantity that exceeds the order balance with [[err-grn-0204|ERR-GRN-0204]][^r6].
* Lithium battery checks: Battery deliveries must be held in WH-MAN-QC until Quality grants release to the Manchester main stores fire-cell area[^r7].
* Damaged packaging controls: Damaged battery parcels must be rejected at delivery and reported under [[sop-qua-002|SOP-QUA-002]][^r8].

## See also

* [[err-grn-0102|ERR-GRN-0102 PO Not Released]]
* [[err-grn-0204|ERR-GRN-0204 Quantity Exceeds PO Balance]]
* [[items-bat|BAT-* items]]
* [[screen-inv-grn-03|INV-GRN-03 Goods Receipt Note (Grn)]]
* [[sop-qua-002|SOP-QUA-002 Damaged Battery Pack Quarantine]]
* [[user-cshaw|Callum Shaw (CSHAW)]]

## References

[^r2]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §2. Scope
[^r4]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure
[^r7]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure
[^r8]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure
[^r3]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §2. Scope
[^r5]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure
[^r6]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure
