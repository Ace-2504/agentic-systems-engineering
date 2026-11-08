---
title: "SOP-PRD-002 Engineering Change (ECN)"
type: "procedure"
slug: "sop-prd-002"
summary: "Standard operating procedure governing permanent engineering changes to frames, drives, and components across Manchester and Leeds facilities."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-PRD-002 |
| Author | Stefan Berg |
| Approver | Henrik Weber |
| Effective date | 2024-02-01 |
| Status | current |
| Applies to | Manchester works, Leeds unit |

SOP-PRD-002 defines the standard operating procedure for executing permanent engineering changes across the Manchester works and Leeds unit [^r1][^r2]. Authored by production planner [[user-sberg|Stefan Berg]] and approved by plant head [[user-hweber|Henrik Weber]], it has been in force since 2024-02-01 [^r1]. It ensures design and bought-in component alterations are formally validated by Quality and Purchasing while preventing premature releases through Ledgerline controls [^r3][^r5].

## Steps

1. Identify the need for a permanent alteration to bicycle frames, electrical drive assemblies, sub-assemblies, or bought-in components, excluding temporary workshop deviations and immediate safety stops [^r2].
2. Raise the engineering change on screen [[screen-prd-ecn-06|PRD-ECN-06]] with a specified effective date [^r3].
3. If the engineering change involves a [[items-bat|lithium-cell part]] with a new cell maker or new design, obtain a fresh UN 38.3 test report before release pursuant to [[pol-sup-003|POL-SUP-003]] §4.6 [^r4].
4. Obtain sign-off approvals from both Quality and Purchasing prior to release [^r3].
5. Close or clear all work orders and active assemblies remaining on the earlier revision across Manchester and Leeds to avoid Ledgerline blocking the release [^r5].
6. Upon master sign-off, file the paper pack in the engineering archives and update the electronic record [^r6].
7. Ensure the systems administrator archives the superseded bill of materials, locks the active revision, and distributes an approved copy to Quality [^r6].
8. Record the serial number of the first completed bicycle utilizing the revised component directly onto the signed change document [^r7].

## Forms and screens

* [[screen-prd-ecn-06|PRD-ECN-06]] (Engineering Change Entry): Used to raise the engineering change with its effective date [^r3].

## Checks and approvals

* Approvals from both Quality and Purchasing are mandatory before any engineering change can be released [^r3].
* Release of an ECN for lithium-cell parts with a new maker or design is blocked without a fresh UN 38.3 test report under [[pol-sup-003|POL-SUP-003]] §4.6 [^r4].
* Ledgerline verifies that no active assemblies or work orders remain open on the previous revision across Manchester or Leeds, halting with [[err-ecn-0220|ERR-ECN-0220]] if any are detected [^r5].

## See also

* [[err-ecn-0220|ERR-ECN-0220 Open work orders on old revision]]
* [[items-bat|BAT-* items]]
* [[pol-sup-003|POL-SUP-003 Supplier Policy]]
* [[screen-prd-ecn-06|PRD-ECN-06 Engineering Change Entry]]
* [[user-hweber|Henrik Weber (HWEBER)]]
* [[user-sberg|Stefan Berg (SBERG)]]

## References

[^r1]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 1, §1. Purpose
[^r2]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 2, §2. Scope
[^r3]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 3, §5. Procedure
[^r6]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 4, §6. Records
[^r7]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 5, §6. Records
