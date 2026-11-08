---
title: "SOP-PRD-001 Work Order Release and Backflush"
type: "procedure"
slug: "sop-prd-001"
summary: "Procedure for releasing work orders and backflushing components in Manchester and Leeds assembly operations."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-PRD-001 |
| Title | Work Order Release and Backflush |
| Version | v1.5 |
| Effective date | 2024-11-01 |
| Status | current |
| Classification | INTERNAL |
| Owner | Stefan Berg |
| Approver | Henrik Weber |

SOP-PRD-001 governs the formal release of production orders and component backflushing across assembly lines at the Manchester plant and the Leeds sub-assembly unit [^r2]. As of 26 October 2026, version 1.5 is the active standard approved by plant head [[user-hweber|Henrik Weber]] and owned by production planner [[user-sberg|Stefan Berg]] [^r1]. It covers standard electric bicycle builds, frame prep operations, and battery housing assemblies [^r2].

## Steps
1. Release work orders on [[screen-prd-wo-01|screen PRD-WO-01]] at least two days before the scheduled start date [^r3].
2. If components are missing during release, resolve the resulting shortage error before proceeding [^r3].
3. For [[items-bat|battery packs]], book items by individual serial number on [[screen-inv-mrn-08|screen INV-MRN-08]] instead of relying on automated clearing [^r4][^r6].
4. Run standard component issues automatically via background job JOB-PRD-015 when work order completions are posted [^r4].
5. Close work orders within five working days following the final completion entry [^r5].
6. Box all original traveller documents, manual component issue slips, inspection sheets, and final completion tickets by production run, and transfer them to the site records room [^r7].

## Forms and screens
* [[screen-prd-wo-01|Screen PRD-WO-01]]: used to release work orders at least two days prior to the production start date [^r3].
* [[screen-inv-mrn-08|Screen INV-MRN-08]]: used to manually issue serialized [[items-bat|battery packs]] by serial number [^r4][^r6].
* JOB-PRD-015: background job that automatically executes backflushing for standard components upon posting completions [^r4].
* Physical records: traveller documents, manual component issue slips, inspection sheets, and final completion tickets [^r7].

## Checks and approvals
* SOP-PRD-001 v1.5 is approved by plant head [[user-hweber|Henrik Weber]] and managed by production planner [[user-sberg|Stefan Berg]] [^r1].
* System checks on [[screen-prd-wo-01|screen PRD-WO-01]] block work order release and raise error [[err-wo-0310|ERR-WO-0310]] if any component shortage exists [^r3].
* Work order completion requires production supervisors to verify that work orders are formally closed within five working days of the last completion [^r5].
* Physical documentation must be verified and transferred by production supervisors to the site records room by production run [^r7].

## See also
* [[screen-prd-wo-01|PRD-WO-01 Work Order Entry]]
* [[screen-inv-mrn-08|INV-MRN-08 Material Issue Entry]]
* [[err-wo-0310|ERR-WO-0310 Component Shortage on Work Order Release]]
* [[items-bat|BAT-* items]]
* [[user-hweber|Henrik Weber (HWEBER)]]
* [[user-sberg|Stefan Berg (SBERG)]]

## References

[^r2]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 2, §2. Scope
[^r1]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 1, Work Order Release and Backflush
[^r3]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 3, §5. Procedure
[^r6]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 3, §5. Procedure: notes and common mistakes
[^r5]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 3, §5. Procedure
[^r7]: 02_procedures/SOP-PRD-001 Work Order Release and Backflush v1.5.pdf, p. 4, §6. Records
