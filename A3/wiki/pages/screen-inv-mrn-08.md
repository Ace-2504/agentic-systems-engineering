---
title: "INV-MRN-08 Material Issue Entry"
type: "screen"
slug: "screen-inv-mrn-08"
summary: "Ledgerline screen used to manually issue serialized battery packs to work orders instead of automatic backflushing."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | INV-MRN-08 |
| Screen name | Material Issue Entry |
| Purpose | Serialized material issue |
| System | Ledgerline |

INV-MRN-08 Material Issue Entry is a Ledgerline screen used to issue serialized components to production work orders. Under [[sop-prd-001|SOP-PRD-001]], [[items-bat|battery packs]] cannot be backflushed automatically and must be issued individually by serial number on this screen [^r1]. It ensures that each battery pack is explicitly tracked and linked to its target work order before assembly is completed [^r1][^r2].

Screen code: INV-MRN-08
Screen name: Material Issue Entry
Purpose: Serialized material issue
System: Ledgerline

## What it is for
The screen is used to manually issue battery packs by serial number rather than relying on automatic backflushing [^r1]. Scanned battery pack serial numbers must be verified as allocated directly to the specific work order number, and the issued count must tally exactly with the finished electric bicycles reported on completion [^r2].

## Fields
* **Work Order Number**: The specific work order to which the scanned serial numbers are allocated [^r2].
* **Battery Pack Serial Number**: The individual serial number of each battery pack being issued [^r1][^r2].

## Messages
The provided sources do not list specific system messages or error codes displayed directly on screen INV-MRN-08.

## See also
* [[items-bat|BAT-* items]]
* [[sop-prd-001|SOP-PRD-001 Work Order Release and Backflush]]
* [[screen-prd-wo-01|PRD-WO-01 Work Order Entry]]
* [[err-wo-0310|ERR-WO-0310 Component Shortage on Work Order Release]]

## References

[^r1]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 4, §5. Procedure: notes and common mistakes
