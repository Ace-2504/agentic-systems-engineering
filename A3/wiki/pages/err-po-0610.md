---
title: "ERR-PO-0610"
type: "error"
slug: "err-po-0610"
summary: "Ledgerline error code blocking direct purchase orders over £25,000 gross value, effective from 1 December 2026."
audience: "staff"
status: "future"
sources: ["01_policies/AMD-PUR-2026-03_Amendment3_PurchasePolicy_DIRlimit.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | ERR-PO-0610 |
| System | Ledgerline |
| Status | Future (effective 2026-12-01) |
| Trigger | Direct purchase order gross value > £25,000 |

ERR-PO-0610 is a forthcoming Ledgerline validation error introduced by [[amd-pur-2026-03|AMD-PUR-2026-03 Amendment 3 to the Purchase Policy]][^r1]. As of today, 26 October 2026, this error code is not yet active in Ledgerline[^r1]. It takes effect on 1 December 2026 to prevent users from saving direct purchase orders that exceed standard thresholds under [[pol-pur-001|POL-PUR-001 Purchase Policy]][^r1].

## Meaning
ERR-PO-0610 indicates that a direct purchase order exceeds the gross value limit permitted for direct order entry[^r1].

## Cause
From 1 December 2026, Ledgerline triggers ERR-PO-0610 when a user attempts to save a direct purchase order exceeding £25,000 gross value[^r1].

## How to fix
Users must ensure the direct purchase order does not exceed £25,000 gross value once the rule takes effect on 1 December 2026[^r1]. Orders over this threshold cannot be saved as direct purchase orders and must follow the standard procurement process governed by [[pol-pur-001|POL-PUR-001 Purchase Policy]][^r1].

## Versions and conflicts
- **Today's rule:** As of 26 October 2026, ERR-PO-0610 is not yet in force[^r1].
- **Future rule:** From 1 December 2026, Ledgerline triggers ERR-PO-0610 whenever a user attempts to save a direct purchase order exceeding £25,000 gross value[^r1].
- **Sources and dates:** [[amd-pur-2026-03|AMD-PUR-2026-03]] (v1.0, dated 2026-12-01)[^r1].
- **Kind:** `future_dated`.

## See also
- [[amd-pur-2026-03|AMD-PUR-2026-03 Amendment 3 to the Purchase Policy]]
- [[pol-pur-001|POL-PUR-001 Purchase Policy]]

## References

[^r1]: 01_policies/AMD-PUR-2026-03_Amendment3_PurchasePolicy_DIRlimit.pdf, p. 1, §3. What changes in Ledgerline
