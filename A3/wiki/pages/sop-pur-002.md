---
title: "SOP-PUR-002 Purchase Request to Purchase Order"
type: "procedure"
slug: "sop-pur-002"
summary: "Procedure for raising, approving, and converting purchase requests into standard purchase orders, followed by order release in Ledgerline."
audience: "staff"
status: "mixed"
sources: ["02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf", "02_procedures/SOP-PUR-002 PR to PO v1.4.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-PUR-002 |
| Owner | Daniel Okafor |
| Approver | Henrik Weber |
| Version | 1.4 |
| Effective date | 2025-02-01 |
| Status | current |

SOP-PUR-002 governs the end-to-end process of raising purchase requests, converting them into purchase orders, and releasing them to suppliers in Ledgerline [^r1]. Under current version 1.4, which took effect on 2025-02-01, using the Fetch function is mandatory to avoid save errors [^r1][^r2][^r8]. The procedure applies across purchasing operations and is authored by Purchase Manager [[user-dokafor|Daniel Okafor]] and approved by Plant Head [[user-hweber|Henrik Weber]] [^r1].

## Steps

1. To raise a purchase request on [[screen-pur-pr-01|PUR-PR-01]], enter the item code and press F3 (Fetch) to automatically populate the unit, warehouse, default cost centre, and estimated rate from the last released order [^r3].
2. Verify on [[screen-fin-cc-01|FIN-CC-01]] that the default cost centre is open prior to saving, as Ledgerline provides no warning on PUR-PR-01 if Finance has closed it [^r5].
3. Press F8 to save the request in status DR, then press F9 to submit it [^r6].
4. Once the request reaches status AP, raise the purchase order on [[screen-pur-po-01|PUR-PO-01]] using order type STD and input the request reference into the Source PR field [^r7].
5. On PUR-PO-01, enter the supplier and item and press F3 (Fetch) to prevent saving from being refused [^r8].
6. Check the populated tax code; if the supplier is outside the UK, manually change the default tax code from VAT20-UK to VAT20-RC [^r9].
7. Save the order and inspect the header Status field to verify whether it is held (DR), waiting for approval (PA), or ready for release (AP) [^r10].
8. For orders in status AP, navigate to [[screen-pur-por-05|PUR-POR-05]] and press F9 to release the order [^r12].
9. Confirm that the order status has updated to RL before notifying the requester [^r12].

## Forms and screens

* [[screen-pur-pr-01|PUR-PR-01]]: Used to raise purchase requests; pressing F3 (Fetch) populates line details and the estimated rate from the last released order rather than the contract rate [^r3][^r4].
* [[screen-fin-cc-01|FIN-CC-01]]: Consulted by originators to ensure the target cost centre is open before saving a request [^r5].
* [[screen-pur-po-01|PUR-PO-01]]: Used to generate STD purchase orders referencing the source PR; requires pressing F3 (Fetch) or save fails with [[err-scr-0221|ERR-SCR-0221]] [^r7][^r8]. Fetch defaults tax to VAT20-UK, which must be updated to VAT20-RC for non-UK vendors to avoid [[err-po-0412|ERR-PO-0412]] [^r9]. The screen status bar displays SAVED regardless of the true outcome, requiring users to check the header Status field [^r10].
* [[screen-pur-por-05|PUR-POR-05]]: Used to execute order release via F9 [^r12].

## Checks and approvals

* On PUR-PR-01, pressing F9 immediately approves requests within the originator's delegated limit, whereas requests exceeding limits route to the manager [^r6].
* Orders stuck in header status DR on PUR-PO-01 typically indicate a closed cost centre accompanied by warning W-CC-114 [^r11].
* Status PA indicates an order is awaiting approval, and status AP signifies it is ready for release [^r10].
* Transmission to the supplier occurs only when the order status reaches RL on PUR-POR-05, at which point requesters may be notified [^r12].

## Versions and conflicts

* **Mandatory Fetch on PUR-PO-01**: Version 1.4 (effective 2025-02-01) made Fetch mandatory in Ledgerline 7.2.3, failing which save is refused with ERR-SCR-0221 [^r2][^r8]. In superseded version 1.3 (effective 2023-05-01), which introduced the approval inbox, this mandatory requirement was not present [^r2][^r13]. (superseded)

## See also

* [[screen-pur-pr-01|PUR-PR-01 Purchase Request Entry]]
* [[screen-pur-po-01|PUR-PO-01 Purchase Order Entry]]
* [[screen-pur-por-05|PUR-POR-05 Purchase Order Release]]
* [[screen-fin-cc-01|FIN-CC-01 Cost Centre Entry]]
* [[err-scr-0221|ERR-SCR-0221 Fetch required before save]]
* [[err-po-0412|ERR-PO-0412]]
* [[user-dokafor|Daniel Okafor (DOKAFOR)]]
* [[user-hweber|Henrik Weber (HWEBER)]]

## References

[^r1]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 1, Purchase Request to Purchase Order
[^r2]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 1, Version history
[^r8]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r3]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r6]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r7]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r9]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r10]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r12]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r11]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r13]: 02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf, p. 1, §1. Purpose
