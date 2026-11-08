---
title: "PUR-PR-01 Purchase Request Entry"
type: "screen"
slug: "screen-pur-pr-01"
summary: "Ledgerline screen used to enter purchase requisitions, populate item defaults, save drafts, and submit requests for departmental approval."
audience: "staff"
status: "mixed"
sources: ["02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf", "02_procedures/SOP-PUR-002 PR to PO v1.4.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | PUR-PR-01 |
| Name | Purchase Request Entry |
| System | Ledgerline |
| Procedure | SOP-PUR-002 |
| Draft save key | F8 (Status DR) |
| Submission key | F9 |

PUR-PR-01 is the Ledgerline screen used to create and submit purchase requisitions under [[sop-pur-002|SOP-PUR-002]][^r1][^r3]. Users enter item codes and fetch default data such as cost centres and estimated pricing prior to saving or submitting the requisition[^r1][^r3]. As of 26 October 2026, the screen does not validate whether a default cost centre is closed, requiring manual check on [[screen-fin-cc-01|FIN-CC-01]][^r2].

## What it is for
PUR-PR-01 serves as the entry screen for purchase requests in Ledgerline[^r1]. Entering an item code and pressing F3 (Fetch) automatically populates the line item's unit of measure, warehouse, default cost centre, and an estimated rate derived from the last released purchase order[^r1]. Once item details are populated, pressing F8 saves the requisition in draft status DR, while pressing F9 submits it for departmental approval or immediate sign-off[^r3].

## Fields
* **Item code:** Entered by the user to identify the required item before fetching line details[^r1].
* **Unit of measure:** Automatically populated upon pressing F3 (Fetch) based on the entered item code[^r1].
* **Warehouse:** Automatically populated upon pressing F3 (Fetch)[^r1].
* **Default cost centre:** Automatically populated upon pressing F3 (Fetch)[^r1]. Screen PUR-PR-01 does not check or alert users if this cost centre has been closed by Finance, so staff must manually verify its status on [[screen-fin-cc-01|FIN-CC-01]] before saving[^r2].
* **Estimated rate:** Automatically populated upon pressing F3 (Fetch) using the rate from the last released purchase order[^r1].

## Messages
PUR-PR-01 does not alert users if their default cost centre has been closed by Finance[^r2]. 

## Versions and conflicts
* **Departmental approval submission:** Under current SOP-PUR-002 v1.4 (effective 2025-02-01), pressing F9 submits the requisition for departmental approval or immediate sign-off[^r3]. Under superseded SOP-PUR-002 v1.3 (effective 2023-05-01), pressing F9 submits the requisition for approval without noting immediate sign-off[^r5] (kind: `superseded`).
* **Item fetch behavior:** Both SOP-PUR-002 v1.4 and superseded SOP-PUR-002 v1.3 specify that entering an item code and pressing F3 populates the unit, warehouse, default cost centre, and estimated rate from the last released order[^r1][^r4] (kind: `superseded`).

## See also
* [[sop-pur-002|SOP-PUR-002 Purchase Request to Purchase Order]]
* [[screen-fin-cc-01|FIN-CC-01 Cost Centre Entry]]
* [[screen-pur-po-01|PUR-PO-01 Purchase Order Entry]]
* [[screen-pur-por-05|PUR-POR-05 Purchase Order Release]]
* [[err-scr-0221|ERR-SCR-0221 Fetch required before save]]

## References

[^r1]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r3]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf, p. 3, §5. Procedure
