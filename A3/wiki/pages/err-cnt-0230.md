---
title: "ERR-CNT-0230 Open Transactions in Count Area"
type: "error"
slug: "err-cnt-0230"
summary: "Ledgerline error when freezing a count area on INV-CNT-06 while open transactions remain."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-INV-003 Stock Count v1.2.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| code | ERR-CNT-0230 |
| module | Ledgerline Inventory |
| screen | INV-CNT-06 |
| trigger | Freezing count area with open transactions |
| status | current |

Error ERR-CNT-0230 is a Ledgerline system error triggered during inventory counting procedures defined in [[sop-inv-003|SOP-INV-003 Stock Count (cycle and annual)]][^r1]. It prevents users from freezing a specified count area when unresolved inventory movements are still pending[^r1]. Resolving the underlying pending transactions is required before the count area can be successfully frozen for counting[^r1].

## Meaning
ERR-CNT-0230 indicates that an attempt to freeze a count area failed because active, uncompleted transactions exist within that area[^r1].

## Cause
The error occurs when an operator attempts to freeze a count area on [[screen-inv-cnt-06|INV-CNT-06 Stock Count Entry]] while open transactions remain in that area[^r1].

## How to fix
Clear or complete all open transactions within the target count area before attempting to freeze the area again on [[screen-inv-cnt-06|INV-CNT-06]][^r1].

## See also
* [[screen-inv-cnt-06|INV-CNT-06 Stock Count Entry]]
* [[sop-inv-003|SOP-INV-003 Stock Count (cycle and annual)]]

## References

[^r1]: 02_procedures/SOP-INV-003 Stock Count v1.2.pdf, p. 3, §5. Procedure
