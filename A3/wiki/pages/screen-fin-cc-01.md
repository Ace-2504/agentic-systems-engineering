---
title: "FIN-CC-01 Cost Centre Entry"
type: "screen"
slug: "screen-fin-cc-01"
summary: "Ledgerline screen used to maintain, open, and close cost centres, and to check active cost centre status prior to raising purchasing documents."
audience: "staff"
status: "mixed"
sources: ["01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf", "01_policies/old/Purchase Policy v4.0.docx", "02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf", "02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf", "02_procedures/SOP-PUR-002 PR to PO v1.4.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | FIN-CC-01 |
| Name | Cost Centre Entry |
| Module | Finance / Purchasing |
| Used by | Finance, Purchasing staff |
| Status | Current |

Screen FIN-CC-01 is the Ledgerline screen used by finance to open, amend, and close cost centres across production programmes, as well as by purchasing staff to confirm cost centre status[^r1][^r2]. As of 26 October 2026, staff must check that a cost centre is open on this screen before raising purchase requests or orders and when resolving held orders[^r1][^r5]. It also prevents closing any cost centre that retains open paperwork or ledger balances[^r3][^r4].

Screen code: FIN-CC-01
Name: Cost Centre Entry
Module: Finance / Purchasing
Used by: Finance, Purchasing staff
Status: Current

## What it is for

Screen FIN-CC-01 is used by finance to open, amend, and close cost centres at the start and end of each production programme[^r2]. In purchasing, staff use the screen under [[pol-pur-001|POL-PUR-001]] to check cost centre status and verify that a cost centre is open prior to raising an order[^r1]. Under [[sop-pur-002|SOP-PUR-002]], staff must also consult FIN-CC-01 to verify whether a cost centre remains active before saving purchase requests or resolving held orders[^r5]. If an order is held in DR status due to warning W-CC-114, staff inspect FIN-CC-01 to find an active alternative cost centre for the department[^r6].

## Fields

Before saving changes on FIN-CC-01, users must verify the status indicator on the screen[^r3]. Users must ensure the description field matches the authorised programme schedule[^r3]. Users must also inspect the open balance and commitments tabs to confirm zero ledger balances, and verify that no live sales orders, work orders, or subcontract manifests remain attached[^r3].

## Messages

Screen FIN-CC-01 triggers error alert [[err-cc-0310|ERR-CC-0310]] if an operator attempts to close a cost centre with outstanding commitments or open paperwork attached[^r4].

## Versions and conflicts

Checking cost centre status on FIN-CC-01 prior to creating purchase documents or releasing held orders is governed today by POL-PUR-001 v4.1 (effective 2026-04-01) and SOP-PUR-002 v1.4 (effective 2025-02-01)[^r1][^r5]. In superseded POL-PUR-001 v4.0, FIN-CC-01 was specified for checking cost centre status before raising a purchase order[^r7]. Under superseded SOP-PUR-002 v1.3 (effective 2023-05-01), users were required to consult FIN-CC-01 prior to saving a purchase request or when fixing a stuck order in DR status to confirm that the assigned cost centre was active[^r8]. (Kind: superseded).

## See also

* [[err-cc-0310|ERR-CC-0310]]
* [[pol-pur-001|POL-PUR-001 Purchase Policy]]
* [[sop-fin-001|SOP-FIN-001 Cost Centre Open and Close]]
* [[sop-pur-002|SOP-PUR-002 Purchase Request to Purchase Order]]

## References

[^r1]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 1, §4. Cost centres and budgets
[^r2]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r3]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 4, What to check on the screen
[^r4]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 4, What to check on the screen
[^r6]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 4, What to do when something does not look right
[^r7]: 01_policies/old/Purchase Policy v4.0.docx, §4. Cost centres and budgets
[^r8]: 02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf, p. 3, §5. Procedure
