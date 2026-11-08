---
title: "SOP-QUA-001 Incoming Inspection"
type: "procedure"
slug: "sop-qua-001"
summary: "Procedure for inspecting incoming production parts, raw materials, and battery packs across Manchester and Leeds goods inwards bays."
audience: "staff"
status: "current"
sources: ["01_policies/POL-QUA-005 Quality Policy v3.0.pdf", "02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-QUA-001 |
| Owner | Pieter Jansen |
| Approver | Henrik Weber |
| Version | 2.0 |
| Effective date | 2024-04-01 |
| Status | current |

SOP-QUA-001 defines the mandatory incoming inspection process for production materials and battery packs received at goods inwards bays [^r3][^r4]. In effect as of 26 October 2026, it ensures that deliveries are verified against quality sampling standards before being booked into free stock [^r3][^r5][^r6]. All rejected lots are halted in quarantine and reported immediately to purchasing through formal non-conformance records [^r5][^r7][^r10].

| Key | Value |
|---|---|
| Code | SOP-QUA-001 |
| Owner | [[user-pjansen|Pieter Jansen]] |
| Approver | [[user-hweber|Henrik Weber]] |
| Version | 2.0 |
| Effective date | 2024-04-01 |
| Status | current |

## Steps

1. Goods inward staff receive deliveries of production parts, raw materials, or sub-assemblies at Manchester or Leeds and place them into the designated quarantine bay instead of booking directly into free stock [^r4][^r5]. Consumables and general stationery bypass this process [^r4].
2. The inspector opens [[screen-qa-ins-01|QA-INS-01]] to perform inspection according to the Acceptable Quality Level specified in [[pol-qua-005|POL-QUA-005 §3.1]] [^r8]. General incoming parts are inspected at AQL 1.5, whereas incoming lithium-cell parts require inspection at AQL 0.65 [^r1].
3. For [[items-bat|incoming battery packs]], the inspector measures and records the individual open-circuit voltage for every sample pack using calibrated testing meters [^r2][^r9]. Any battery pack with a state of charge below 30% or above 50% fails inspection under [[pol-bat-004|POL-BAT-004 §2.3]] [^r9].
4. If any sample battery pack falls below 30% or above 50% state of charge, the inspector marks the entire lot as non-conforming without re-sampling or testing additional units [^r11].
5. For accepted deliveries, the inspector records the results on the terminal, transfers the stock status from quarantine to free stock, and affixes green acceptance tags so store personnel can rack the items [^r6].
6. For rejected deliveries, the inspector attaches red rejection labels to the parts, raises an immediate NCR on [[screen-qa-ncr-02|QA-NCR-02]], and notifies the purchasing team [^r7][^r10].
7. The purchasing team raises a debit note and contacts the vendor regarding the non-conforming lot [^r7].

## Forms and screens

* [[screen-qa-ins-01|QA-INS-01]]: Incoming inspection entry terminal used to conduct inspections at designated AQL thresholds and record open-circuit voltages [^r8][^r9].
* [[screen-qa-ncr-02|QA-NCR-02]]: Non-conformance report screen used to register an immediate NCR for any failed lot [^r10].

## Checks and approvals

* Effective version 2.0 is owned by Quality Manager [[user-pjansen|Pieter Jansen]] and approved by Plant Head [[user-hweber|Henrik Weber]] [^r3].
* Sampling requires AQL 0.65 for lithium cells and AQL 1.5 for other incoming parts [^r1].
* Every sample battery pack must undergo open-circuit voltage verification on calibrated testing meters and must fall strictly between 30% and 50% state of charge [^r2][^r9].
* Rejection is immediate if a single battery pack falls outside the 30% to 50% range, with no additional sampling permitted [^r11].

## See also

* [[pol-qua-005|POL-QUA-005 Quality Policy]]
* [[pol-bat-004|POL-BAT-004 Battery Safety and Handling Policy]]
* [[screen-qa-ins-01|QA-INS-01 Incoming Inspection Entry]]
* [[screen-qa-ncr-02|QA-NCR-02 Non-Conformance Report Entry]]
* [[items-bat|BAT-* items]]
* [[user-pjansen|Pieter Jansen (PJANSEN)]]
* [[user-hweber|Henrik Weber (HWEBER)]]

## References

[^r3]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 1, Incoming Inspection
[^r4]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 2, §2. Scope
[^r5]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 2, §2. Scope
[^r6]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 2, §3. Responsibilities
[^r7]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 2, §3. Responsibilities
[^r10]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 3, §5. Procedure
[^r8]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 3, §5. Procedure
[^r1]: 01_policies/POL-QUA-005 Quality Policy v3.0.pdf, p. 2, §3. Incoming inspection
[^r2]: 01_policies/POL-QUA-005 Quality Policy v3.0.pdf, p. 2, §3. Incoming inspection
[^r9]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 3, §5. Procedure
[^r11]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 4, §5. Procedure: notes and common mistakes
