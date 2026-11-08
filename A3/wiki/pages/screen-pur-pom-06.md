---
title: "PUR-POM-06 Purchase Order Amendment"
type: "screen"
slug: "screen-pur-pom-06"
summary: "Ledgerline screen used to fetch purchase orders and amend order quantity, need-by date, or cost centre."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | PUR-POM-06 |
| Purpose | Purchase Order Amendment |
| Application | Ledgerline |
| Editable fields | Quantity, need-by date, cost centre |
| Non-editable fields | Supplier, item, rate |
| Status | Current |

Screen PUR-POM-06 is the Ledgerline screen used under [[sop-pur-003|SOP-PUR-003]] to retrieve existing purchase orders and make specific modifications [^r1]. As of Monday 26 October 2026, it allows adjustments exclusively to order quantities, need-by dates, and cost centres [^r1]. It restricts modifications to active orders, blocking changes to orders that are closed, rejected, or cancelled [^r2].

## What it is for
Screen PUR-POM-06 allows users to fetch an order and amend only quantity, need-by date, or cost centre [^r1]. Direct editing of supplier, item, or rate is not permitted on this screen [^r1]. Pressing Cancel on PUR-POM-06 requires entering a reason, but it does not transmit an automated cancellation message to the vendor [^r4].

## Fields
* **Quantity**: Editable field for amending order volume [^r1].
* **Need-by date**: Editable field for adjusting delivery timing [^r1].
* **Cost centre**: Editable field for reallocating department accounts [^r1].
* **Supplier**: Non-editable display field [^r1].
* **Item**: Non-editable display field [^r1].
* **Rate**: Non-editable display field [^r1].

## Messages
* **[[err-po-0801|ERR-PO-0801]]**: Error produced when attempting to commit modifications on screen PUR-POM-06 against orders in closed, rejected, or cancelled states [^r2].
* **W-CC-114**: Warning displayed on screen PUR-POM-06 when an unapproved draft order fails validation due to a closed department account [^r3].

## See also
* [[sop-pur-003|SOP-PUR-003 Purchase Order Amendment and]]
* [[err-po-0801|ERR-PO-0801 Cannot Amend Order in CN, RJ or CL Status]]

## References

[^r1]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r4]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r3]: 02_procedures/SOP-PUR-003 PO Amendment and Cancellation v1.2.pdf, p. 4, §5. Procedure: notes and common mistakes
