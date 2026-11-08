---
title: "PUR-POR-05 Purchase Order Release"
type: "screen"
slug: "screen-pur-por-05"
summary: "Ledgerline screen used to release approved purchase orders from AP to RL status via F9."
audience: "staff"
status: "mixed"
sources: ["02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf", "02_procedures/SOP-PUR-002 PR to PO v1.4.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | PUR-POR-05 |
| Purpose | Purchase Order Release |
| Action key | F9 |
| Input status | AP (Approved) |
| Target status | RL (Released) |

PUR-POR-05 is the Ledgerline screen used to release approved purchase orders.[^r1] Operating staff access this screen to execute order release by pressing F9 for orders currently in status AP.[^r1] As of 26 October 2026, users must ensure the order status updates from AP to RL to verify transmission file generation and receipt by the supplier.[^r2]

## What it is for
The PUR-POR-05 screen releases purchase orders that are in approved status AP.[^r1] Triggering release using the F9 key generates the transmission file and sends the order to the supplier.[^r1][^r2]

## Fields
Users view and verify the order status field on PUR-POR-05 to ensure the order transitions from AP to RL.[^r2]

## Messages
No specific screen messages are documented in the procedures for PUR-POR-05.

## Versions and conflicts
* **Today's rule**: Purchase orders in approved status AP are released on PUR-POR-05 by pressing F9, and users must verify that the status transitions from AP to RL to confirm transmission file creation and supplier receipt (SOP-PUR-002 v1.4, effective 2025-02-01).[^r1][^r2]
* **Older rule**: Approved purchase orders are released on PUR-POR-05 using key F9 to move order status to RL (SOP-PUR-002 v1.3, effective 2023-05-01).[^r3]
* **Kind**: superseded

## See also
* [[sop-pur-002|SOP-PUR-002 Purchase Request to Purchase Order]]
* [[screen-pur-po-01|PUR-PO-01 Purchase Order Entry]]
* [[screen-pur-pr-01|PUR-PR-01 Purchase Request Entry]]

## References

[^r1]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 4, What to check on the screen
[^r3]: 02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf, p. 3, §5. Procedure
