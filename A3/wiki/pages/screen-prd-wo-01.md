---
title: "PRD-WO-01 Work Order Entry"
type: "screen"
slug: "screen-prd-wo-01"
summary: "Ledgerline screen used to release work orders at least two days before the start date, subject to stock availability."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | PRD-WO-01 |
| Name | Work Order Entry |
| System | Ledgerline |
| Associated procedure | SOP-PRD-001 |
| Status | current |

PRD-WO-01 is the Ledgerline work order entry screen used to release production work orders [^r1]. Under [[sop-prd-001|SOP-PRD-001]], staff must release orders on this screen at least two days before the scheduled start date [^r1]. A release cannot proceed if any required raw material or sub-assembly line has a component shortage [^r1][^r2].

Screen code: PRD-WO-01
Name: Work Order Entry
System: Ledgerline
Associated procedure: [[sop-prd-001|SOP-PRD-001]]
Status: current

## What it is for

Staff use PRD-WO-01 to execute the release of work orders at least two days prior to their start date [^r1]. The screen verifies component availability across all raw material and sub-assembly lines before allowing the release to complete [^r1][^r2].

## Fields

Staff must review component availability for all raw materials and sub-assemblies to verify that every item displays adequate free stock rather than a deficit [^r2].

## Messages

If any raw material or sub-assembly line displays a component shortage deficit upon attempting release, the action fails and the screen triggers error [[err-wo-0310|ERR-WO-0310]] [^r1][^r2].

## See also

* [[sop-prd-001|SOP-PRD-001 Work Order Release and Backflush]]
* [[err-wo-0310|ERR-WO-0310 Component Shortage on Work Order Release]]

## References

[^r1]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 4, §5. Procedure: notes and common mistakes
