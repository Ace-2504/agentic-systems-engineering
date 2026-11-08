---
title: "ERR-SCR-0221 Fetch required before save"
type: "error"
slug: "err-scr-0221"
summary: "Ledgerline error code on screen PUR-PO-01 when saving a purchase order without fetching master data linkages first."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PUR-002 PR to PO v1.4.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| code | ERR-SCR-0221 |
| screen | PUR-PO-01 |
| procedure | SOP-PUR-002 |
| trigger | Save attempt without prior fetch |
| resolution | Press F3 then F8 |
| status | current |

Error ERR-SCR-0221 is a Ledgerline system error encountered during purchase order entry. It informs the operator that required background master data linkages have not been retrieved before attempting a save operation [^r1]. As of 26 October 2026, operators encountering this error must execute the fetch command to populate master data prior to saving the record [^r2].

## Meaning
ERR-SCR-0221 signifies that a user attempted to commit an order on [[screen-pur-po-01|screen PUR-PO-01]] before retrieving necessary background master data linkages [^r1]. The system blocks the save action until the fetch process has been executed [^r1].

## Cause
This error occurs in [[sop-pur-002|SOP-PUR-002]] when an operator tries to save an order directly without first pressing F3 (Fetch) to pull the background master data linkages on screen PUR-PO-01 [^r1].

## How to fix
To fix ERR-SCR-0221, place the cursor back into the line details area of screen PUR-PO-01 [^r2]. Press F3 to fetch the required master data, and then press F8 to save the order [^r2].

## See also
* [[screen-pur-po-01|PUR-PO-01 Purchase Order Entry]]
* [[sop-pur-002|SOP-PUR-002 Purchase Request to Purchase Order]]
* [[err-po-0412|ERR-PO-0412]]

## References

[^r1]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 4, What to do when something does not look right
