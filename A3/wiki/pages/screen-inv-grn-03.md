---
title: "INV-GRN-03 Goods Receipt Note (Grn)"
type: "screen"
slug: "screen-inv-grn-03"
summary: "Ledgerline screen used to record goods receipt against released purchase orders, enter received quantities, and assign warehouse locations."
audience: "staff"
status: "current"
sources: ["02_procedures/sop_inv_001_goods_receipt_v2.docx"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | INV-GRN-03 |
| Name | Goods Receipt Note (GRN) |
| System | Ledgerline |
| Required order status | RL |
| Default QC warehouse | WH-MAN-QC |
| Error codes | ERR-GRN-0204 |
| Governing procedure | SOP-INV-001 |

Screen INV-GRN-03 is the Ledgerline interface used by receiving staff to process and post goods receipt notes against purchase orders as detailed in [[sop-inv-001|SOP-INV-001]][^r1]. As of 26 October 2026, transactions require purchase orders to be in released status before quantities can be processed[^r1]. The screen ensures stock integrity by validating received quantities against open line balances and routing specific sensitive parts directly to quality control[^r3][^r4].

## What it is for
Screen INV-GRN-03 is used to retrieve released purchase orders, record incoming deliveries, and generate goods receipt notes in the system[^r1][^r2]. Entering the purchase order number and selecting Fetch loads the order details, which can only proceed if the document status displays RL[^r1]. It also routes items to the appropriate inventory locations, requiring sensitive lithium-cell components ([[items-bat|BAT-* items]]) to be directed to warehouse code WH-MAN-QC[^r4].

## Fields
* **Purchase Order Number**: The purchase order identifier entered by the operator to retrieve the order using the Fetch button[^r1].
* **Document Status**: Displays the current status of the order, which must show RL to allow processing to continue[^r1].
* **Quantity Received**: The line-item quantity physically received from the delivery[^r2].
* **Remarks**: Text field used to record the supplier's delivery note number prior to saving the receipt[^r2].
* **Warehouse Code**: The destination warehouse identifier, which must be set to WH-MAN-QC for sensitive lithium-cell components[^r4].

## Messages
* **[[err-grn-0204|ERR-GRN-0204]]**: An error message that halts the transaction when an operator attempts to enter a quantity that exceeds the open balance of the purchase order line[^r3].

## See also
* [[sop-inv-001|SOP-INV-001 Goods Receipt]]
* [[err-grn-0204|ERR-GRN-0204 Quantity Exceeds PO Balance]]
* [[items-bat|BAT-* items]]

## References

[^r1]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure
[^r3]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure: notes and common mistakes
[^r4]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure: notes and common mistakes
[^r2]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure
