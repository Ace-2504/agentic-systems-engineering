---
title: "QA-NCR-02 Non-Conformance Report Entry"
type: "screen"
slug: "screen-qa-ncr-02"
summary: "Ledgerline screen to raise non-conformance reports for rejected inspection lots and damaged battery packs."
audience: "staff"
status: "current"
sources: ["01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf", "02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf", "02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | QA-NCR-02 |
| Screen name | Non-Conformance Report Entry |
| System | Ledgerline |
| Status | current |

Screen QA-NCR-02 is the Ledgerline screen used to raise non-conformance reports (NCRs) across receiving and handling operations. It is used to generate an immediate NCR whenever an inspection lot fails, as well as to report damaged, dropped, wet, or swollen battery packs moved to quarantine. Logging issues on this screen alerts Stores to freeze intake pallets and flags units for physical inspection by Quality.

Screen code: QA-NCR-02
Screen name: Non-Conformance Report Entry
System: Ledgerline
Status: current

## What it is for

Under [[sop-qua-001|SOP-QUA-001]], an NCR must be raised on QA-NCR-02 for every rejected lot immediately upon inspection failure [^r2]. Under [[pol-bat-004|POL-BAT-004]], team leaders use QA-NCR-02 before the end of the shift to report damaged, dropped, wet, or swollen [[items-bat|battery packs]] moved to the BAT-Z4 red quarantine bin, capturing the batch number stamped on the casing so Stores can freeze the remaining units from that intake pallet [^r1]. Under [[sop-qua-002|SOP-QUA-002]], the screen requires non-conformance reports for damaged battery packs to be logged during the discovering shift with photographs of the casing, serial plate, and terminals attached [^r4].

## Fields

When generating an NCR for an incoming inspection rejection, the delivery reference, part identification, and failure reasons populate from the inspection sheet before submission [^r3].

For damaged battery packs, the operator must verify that the header serial number matches the casing label [^r5]. If a pack's serial number is defaced, the batch reference is entered into QA-NCR-02 with a narrative explanation flagging it for physical inspection by Quality [^r6]. The user must also enter the batch number stamped on the casing [^r1]. In addition, the screen requires specifying the defect classification covering casing rupture, terminal shorting, or swelling [^r5], and attaching photographs showing the casing, serial plate, and terminals [^r4].

## Messages

If a defaced serial number is entered with a batch reference and narrative explanation, QA-NCR-02 flags the record for physical inspection by Quality [^r6].

## See also

* [[pol-bat-004|POL-BAT-004 Battery Safety and Handling Policy]]
* [[sop-qua-001|SOP-QUA-001 Incoming Inspection]]
* [[sop-qua-002|SOP-QUA-002 Damaged Battery Pack Quarantine]]
* [[items-bat|BAT-* items]]
* [[screen-qa-ins-01|QA-INS-01 Incoming Inspection Entry]]
* [[screen-inv-qch-11|INV-QCH-11 Quality Hold Entry]]

## References

[^r2]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 3, §5. Procedure
[^r1]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 3, §3. Damaged packs
[^r4]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 3, §5. Procedure: notes and common mistakes
[^r3]: 02_procedures/SOP-QUA-001 Incoming Inspection v2.0.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r5]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r6]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 4, §5. Procedure: notes and common mistakes
