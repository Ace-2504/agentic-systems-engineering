---
title: "ERR-WO-0310 Component Shortage on Work Order Release"
type: "error"
slug: "err-wo-0310"
summary: "Ledgerline error when releasing a work order with component shortages, requiring verification with inventory control rather than bypassing."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Error code | ERR-WO-0310 |
| Screen | PRD-WO-01 |
| Trigger | Component shortage on work order release |
| Severity | Blocking |
| Owner | Production / Inventory Control |
| Status | Current |

Error ERR-WO-0310 prevents the release of a work order when required components are missing from stock [^r1]. It triggers directly within the work order entry interface when component availability checks fail [^r1]. Operators encountering this condition must contact inventory control to resolve stock discrepancies rather than attempting to bypass the control [^r2].

## Meaning

Error ERR-WO-0310 indicates that component shortages exist for raw materials or sub-assemblies required by the work order [^r1]. The system blocks the release of the order to prevent production from starting without sufficient stock [^r1].

## Cause

The error occurs when attempting to release a work order on screen [[screen-prd-wo-01|PRD-WO-01]] while raw material or sub-assembly component shortages exist in inventory [^r1].

## How to fix

When ERR-WO-0310 appears, staff must not bypass the check under any circumstances [^r2]. Staff must speak immediately with the inventory control desk to verify if components are physically present awaiting inspection or if an urgent PO is pending [^r2].

## See also

* [[screen-prd-wo-01|PRD-WO-01 Work Order Entry]]
* [[sop-prd-001|SOP-PRD-001 Work Order Release and Backflush]]

## References

[^r1]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 4, §5. Procedure: notes and common mistakes
