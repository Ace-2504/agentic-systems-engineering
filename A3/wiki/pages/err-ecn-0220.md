---
title: "ERR-ECN-0220 Open work orders on old revision"
type: "error"
slug: "err-ecn-0220"
summary: "Error preventing ECN release in Ledgerline when active works orders, assembly cards, or unfinished kitting lists remain open on the earlier revision."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Error code | ERR-ECN-0220 |
| Screen | [[screen-prd-ecn-06|PRD-ECN-06]] |
| Governing procedure | [[sop-prd-002|SOP-PRD-002]] |
| Status | Current |

ERR-ECN-0220 is a Ledgerline error encountered during engineering change processing under [[sop-prd-002|SOP-PRD-002]][^r1]. It blocks the system from releasing an ECN whenever active shop-floor records are still linked to an older revision[^r1]. Resolving it requires clearing or re-issuing open assembly tickets with production control before proceeding[^r2].

## Meaning

The error indicates that Ledgerline refuses to release an ECN because active works orders, assembly cards, or unfinished kitting lists remain open on the earlier revision[^r1].

## Cause

The condition is triggered when an engineering change release is attempted while open manufacturing orders, uncompleted kitting documents, or active assembly cards continue to reference the superseded revision in the system[^r1].

## How to fix

To resolve ERR-ECN-0220, generate the live assembly listing to identify the specific open order numbers[^r2]. Liaise directly with production control to complete these orders or close and re-issue the tickets before attempting to release the change again[^r2].

## See also

* [[screen-prd-ecn-06|PRD-ECN-06 Engineering Change Entry]]
* [[sop-prd-002|SOP-PRD-002 Engineering Change (ECN)]]

## References

[^r1]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 4, §5. Procedure: notes and common mistakes
