---
title: "ERR-PO-0412"
type: "error"
slug: "err-po-0412"
summary: "Purchase order save error on PUR-PO-01 when a non-UK supplier line has domestic tax code VAT20-UK instead of VAT20-RC."
audience: "staff"
status: "mixed"
sources: ["02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf", "02_procedures/SOP-PUR-002 PR to PO v1.4.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Error code | ERR-PO-0412 |
| Screen | PUR-PO-01 |
| Trigger | Saving an order with incorrect tax code for overseas supplier |
| Resolution | Change line tax code to VAT20-RC |

Error ERR-PO-0412 is a Ledgerline validation error encountered when saving purchase orders for non-UK suppliers on screen [[screen-pur-po-01|PUR-PO-01]]. As of 26 October 2026, it indicates that a purchase order line has been incorrectly assigned the domestic tax code VAT20-UK instead of VAT20-RC [^r1]. Resolving it requires verifying the supplier country and updating the tax code before saving the order [^r2].

## Meaning
ERR-PO-0412 indicates that an order cannot be saved because a supplier located outside the UK has a line configured with domestic VAT rather than reverse charge VAT [^r1].

## Cause
The error occurs on [[screen-pur-po-01|PUR-PO-01]] when saving an order for a supplier outside the UK if the tax code has been left as VAT20-UK instead of VAT20-RC [^r1].

## How to fix
To resolve the error, check the supplier country and change the purchase order line tax code from VAT20-UK to VAT20-RC before re-saving on [[screen-pur-po-01|PUR-PO-01]] [^r2].

## Versions and conflicts
- Today's rule (effective 2025-02-01): Error ERR-PO-0412 occurs on [[screen-pur-po-01|PUR-PO-01]] when saving an order for a supplier outside the UK if the tax code has been left as VAT20-UK instead of VAT20-RC [^r1].
- Older rule (effective 2023-05-01, superseded): In [[sop-pur-002|SOP-PUR-002]] v1.3, ERR-PO-0412 occurs on PUR-PO-01 when attempting to save an order for an overseas supplier with the default domestic tax code VAT20-UK instead of VAT20-RC [^r3].
- Kind: superseded [^r1][^r3].

## See also
- [[sop-pur-002|SOP-PUR-002 Purchase Request to Purchase Order]]
- [[screen-pur-po-01|PUR-PO-01 Purchase Order Entry]]
- [[err-scr-0221|ERR-SCR-0221 Fetch required before save]]

## References

[^r1]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 4, What to do when something does not look right
[^r3]: 02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf, p. 4, §5. Procedure: notes and common mistakes
