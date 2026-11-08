---
title: "INV-QCH-11 Quality Hold Entry"
type: "screen"
slug: "screen-inv-qch-11"
summary: "Ledgerline screen used to transfer suspect battery serial numbers to quality hold, reducing main stores balance and blocking pick list allocation."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | INV-QCH-11 |
| Name | Quality Hold Entry |
| System | Ledgerline |
| Status | Current |

Screen INV-QCH-11 is the Ledgerline screen used to transfer suspect battery serial numbers to quality hold status. As of 26 October 2026, placing units into quality hold via this screen reduces the main stores balance and prevents the battery pack from being issued or allocated to pick lists. When a serial number is already allocated to a build order, the movement must not be cancelled, and the stores supervisor must strip the allocation from the production order first.

Screen code: INV-QCH-11
Name: Quality Hold Entry
System: Ledgerline
Status: Current

## What it is for

Screen INV-QCH-11 is used to transfer suspect battery serial numbers to quality hold so that the main stores balance is reduced and the pack cannot be issued or allocated to pick lists [^r1].

## Fields

When an entry is processed, screen INV-QCH-11 displays an active hold flag that prevents assembly orders and pick lists from allocating the quarantined serial number [^r3].

## Messages

When INV-QCH-11 shows that a serial number is already allocated to a build order, the movement must not be cancelled; the stores supervisor must strip the allocation from the production order first [^r2].

## See also

* [[sop-qua-002|SOP-QUA-002 Damaged Battery Pack Quarantine]]
* [[items-bat|BAT-* items]]
* [[screen-qa-ncr-02|QA-NCR-02 Non-Conformance Report Entry]]
* [[user-hweber|Henrik Weber (HWEBER)]]
* [[user-pjansen|Pieter Jansen (PJANSEN)]]

## References

[^r1]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r3]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r2]: 02_procedures/SOP-QUA-002 Damaged Battery Pack Quarantine v1.1.pdf, p. 4, §5. Procedure: notes and common mistakes
