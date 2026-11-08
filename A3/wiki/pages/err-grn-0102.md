---
title: "ERR-GRN-0102 PO Not Released"
type: "error"
slug: "err-grn-0102"
summary: "Ledgerline error when attempting goods receipt against an unreleased purchase order."
audience: "staff"
status: "current"
sources: ["02_procedures/sop_inv_001_goods_receipt_v2.docx"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Error code | ERR-GRN-0102 |
| Message | PO Not Released |
| System | Ledgerline |
| Associated procedure | SOP-INV-001 |

Ledgerline error ERR-GRN-0102 blocks processing during goods receipt if a purchase order is not released. It indicates that warehouse staff cannot fetch or receive against the requested order until purchasing completes release. As of 26 October 2026, staff encountering this error must resolve it through purchasing rather than attempting a forced receipt.

| Field | Detail |
|---|---|
| Error code | ERR-GRN-0102 |
| Message | PO Not Released |
| System | Ledgerline |
| Associated procedure | [[sop-inv-001|SOP-INV-001 Goods Receipt]] |

## Meaning
The error indicates that the order being fetched or received is not in released status (RL) in Ledgerline [^r1].

## Cause
ERR-GRN-0102 occurs during goods receipt when a user attempts to fetch or receive an order that has not attained released status (RL) [^r1].

## How to fix
When ERR-GRN-0102 is displayed, staff must contact purchasing to confirm order release rather than attempting to force receipt [^r2].

## See also
* [[sop-inv-001|SOP-INV-001 Goods Receipt]]
* [[screen-inv-grn-03|INV-GRN-03 Goods Receipt Note (Grn)]]
* [[err-grn-0204|ERR-GRN-0204 Quantity Exceeds PO Balance]]

## References

[^r1]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure
[^r2]: 02_procedures/sop_inv_001_goods_receipt_v2.docx, §5. Procedure: notes and common mistakes
