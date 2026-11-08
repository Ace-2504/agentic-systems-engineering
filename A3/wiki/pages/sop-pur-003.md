---
title: "SOP-PUR-003 Purchase Order Amendment and"
type: "procedure"
slug: "sop-pur-003"
summary: "Standard operating procedure for amending or cancelling purchase orders in Ledgerline, including allowed field changes and approval resets."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Document code | SOP-PUR-003 |
| Version | 1.2 |
| Effective date | 2025-02-01 |
| Status | current |
| Owner | Daniel Okafor |
| Approver | Henrik Weber |

SOP-PUR-003 governs the procedure for modifying or cancelling purchase orders in Ledgerline [^r1]. As of 26 October 2026, version 1.2 remains in force under the ownership of purchase manager [[user-dokafor|Daniel Okafor]] following approval by plant head [[user-hweber|Henrik Weber]] [^r1]. It restricts amendments to specific fields and ensures orders exceeding approval thresholds return to approval workflows [^r2][^r4].

## Steps

1. Navigate to screen [[screen-pur-pom-06|PUR-POM-06]] and fetch the existing purchase order [^r2].
2. For open orders requiring field updates, modify only the quantity, need-by date, or cost centre [^r2]. If an order needs a different supplier, item, or rate, cancel the original order and raise a new one instead [^r2].
3. For draft orders blocked on a closed cost centre displaying warning W-CC-114, update the cost centre to an open one to allow transition to AP or PA according to standard rules [^r3].
4. For part-received orders where the remaining balance is no longer required, close the line for further receipt instead of reducing the original total quantity [^r7].
5. To cancel an order, press Cancel and enter a justification reason [^r5].
6. Because Ledgerline does not issue automated cancellation notifications, email the supplier on the same day the cancellation is processed [^r5].
7. File all revised electronic records, hard copies, supplier quotations, written notices, and supplier acknowledgements together [^r5][^r8].

## Forms and screens

* Screen [[screen-pur-pom-06|PUR-POM-06]] is used to retrieve and process purchase order modifications and cancellations [^r2].
* Records generated include revised order printouts, original supplier quotations, written cancellation notices, and supplier acknowledgement records, which buyers must maintain in both electronic and hard copy formats [^r5][^r8].

## Checks and approvals

* Orders in closed (CL), rejected (RJ), or cancelled (CN) status cannot be modified and produce error [[err-po-0801|ERR-PO-0801]] [^r6].
* Any amendment that increases the gross order value beyond the existing approval coverage automatically reverts the order to pending approval (PA), even if it was previously released [^r4].

## See also

* [[screen-pur-pom-06|PUR-POM-06 Purchase Order Amendment]]
* [[err-po-0801|ERR-PO-0801 Cannot Amend Order in CN, RJ or CL Status]]
* [[user-dokafor|Daniel Okafor (DOKAFOR)]]
* [[user-hweber|Henrik Weber (HWEBER)]]

## References

[^r1]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 1, Header
[^r2]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 3, §5. Procedure
[^r3]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 3, §5. Procedure
[^r7]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 3, §3. Responsibilities
[^r5]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 3, §5. Procedure
[^r8]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 4, §6. Records
[^r6]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 3, §5. Procedure
