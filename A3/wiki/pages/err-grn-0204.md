---
title: "ERR-GRN-0204 Quantity Exceeds PO Balance"
type: "error"
slug: "err-grn-0204"
summary: "Ledgerline error when receipt quantity exceeds the purchase order line open balance during goods receipt."
audience: "staff"
status: "current"
sources: ["02_procedures/sop_inv_001_goods_receipt_v2.docx"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| code | ERR-GRN-0204 |
| module | Ledgerline Inventory / Receiving |
| trigger | Receipt quantity exceeds open balance |
| status | current |
| owner | Inventory Control |

Ledgerline error ERR-GRN-0204 prevents receiving items beyond the authorized purchase order quantities during goods receipt processing under [[sop-inv-001|SOP-INV-001]]. It ensures warehouse staff do not accept excess inventory without proper procurement adjustments.

## Meaning
The error indicates that the entered receipt quantity exceeds the remaining open balance on the purchase order line [^r1].

## Cause
Over-delivery triggers ERR-GRN-0204 when a user attempts to record a delivery volume larger than what remains open on the purchase order [^r2].

## How to fix
When over-delivery triggers ERR-GRN-0204, receiving staff must halt the transaction immediately [^r2]. Staff may receive only the valid balance if instructed, or hold the entire shipment pending resolution [^r2]. Receiving staff must never manually inflate order balances to clear the error [^r2].

## See also
* [[sop-inv-001|SOP-INV-001 Goods Receipt]]
* [[screen-inv-grn-03|INV-GRN-03 Goods Receipt Note (Grn)]]
* [[err-grn-0102|ERR-GRN-0102 PO Not Released]]

## References

[^r1]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure
[^r2]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure: notes and common mistakes
