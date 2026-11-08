---
title: "QA-INS-01 Incoming Inspection Entry"
type: "screen"
slug: "screen-qa-ins-01"
summary: "Ledgerline screen used to conduct incoming inspection at defined AQL levels, capture test outcomes including battery voltage, and place failed items on hold."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | QA-INS-01 |
| Name | Incoming Inspection Entry |
| Primary procedure | SOP-QUA-001 |
| System | Ledgerline |
| Status | current |

QA-INS-01 is the Ledgerline screen used to conduct incoming inspection at the AQL defined in [[pol-qua-005|POL-QUA-005]] §3.1 and must be opened before beginning physical checks [^r1]. Inspectors use it to verify item details against physical labels and record inspection test results [^r2]. Marking a line as failed on this screen automatically places stock balances on hold to prevent transfer to general stores [^r4].

## What it is for

The screen is used during [[sop-qua-001|SOP-QUA-001]] to carry out incoming inspections against defined quality standards before physical checking starts [^r1]. It also holds stock in the system if inspection requirements are not satisfied [^r4].

## Fields

Inspectors must verify that the purchase order line and part description on QA-INS-01 match the physical delivery note and carton labels before recording test outcomes [^r2]. For [[items-bat|battery packs]], the screen requires entry lines to record individual open-circuit voltage values to verify that the state of charge is between 30% and 50% [^r3].

## Messages

When a line is marked as failed on QA-INS-01, the system updates the inspection status to hold the stock balance and prevent transfer to general stores [^r4].

## See also

* [[sop-qua-001|SOP-QUA-001 Incoming Inspection]]
* [[pol-qua-005|POL-QUA-005 Quality Policy]]
* [[items-bat|BAT-* items]]

## References

[^r1]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r4]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r3]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 4, §5. Procedure: notes and common mistakes
