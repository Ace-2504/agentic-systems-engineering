---
title: "SOP-FIN-001 Cost Centre Open and Close"
type: "procedure"
slug: "sop-fin-001"
summary: "Operating procedure for opening and retiring Ledgerline ERP cost centres across Manchester and Leeds sites."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Document code | SOP-FIN-001 |
| Title | Cost Centre Open and Close |
| Version | 1.1 |
| Effective date | 2025-01-01 |
| Owner | Grace Whitaker |
| Approver | Henrik Weber |
| Status | current |
| Audience | staff |

SOP-FIN-001 governs how cost centres are opened and retired in Ledgerline ERP across the Manchester plant and Leeds unit [^r1][^r3]. All financial postings require an active, validated cost centre before transactions can proceed [^r2]. As of 26 October 2026, version 1.1 remains the current standard for cost centre hierarchy changes and settlement controls [^r1].

Code: SOP-FIN-001
Version: 1.1
Owner: [[user-gwhitaker|Grace Whitaker]]
Approved by: [[user-hweber|Henrik Weber]]
Effective date: 2025-01-01
Status: current

## Steps

1. Department heads at the Manchester plant and Leeds unit formally request changes to the cost centre hierarchy [^r3].
2. For cost centre creation at the start of a production programme, Finance opens the record in Ledgerline ERP [^r4].
3. Prior to closing a cost centre at the end of a production programme, Finance notifies buyers 10 working days in advance [^r4][^r5].
4. The cost centre manager certifies that all purchase orders, subcontract charges, and timesheet allocations are fully settled [^r3].
5. Any remaining open documents must be moved or cancelled; otherwise, closing the cost centre triggers error [[err-cc-0310]] [^r7].
6. Finance executes the closure in Ledgerline ERP [^r4].
7. Affected cost centre owners submit an access request to IT under [[sop-it-001|SOP-IT-001]], because Ledgerline ERP does not automatically reassign users' default cost centres upon closure [^r6].
8. When retired, the final balance listing and closure sign-off sheet must be attached to the original opening document, filed alphabetically by department name, and retained indefinitely in the finance archive at Manchester with a scanned copy saved to the shared network drive [^r8].

## Forms and screens

* Screen [[screen-fin-cc-01|FIN-CC-01]]: Used by Finance to open and close cost centres at the start and end of production programmes [^r4].
* IT access request form: Submitted under [[sop-it-001|SOP-IT-001]] to reassign user default cost centres following a closure [^r6].
* Closure sign-off sheet: Completed alongside the final balance listing and original opening document for permanent archive retention [^r8].

## Checks and approvals

* Document ownership and sign-off: Owned by Financial Controller [[user-gwhitaker|Grace Whitaker]] and approved by Plant Head [[user-hweber|Henrik Weber]] [^r1].
* Hierarchy alteration requests: Department heads at the Manchester plant and Leeds unit must formally submit alteration requests [^r3].
* Pre-closure validation: The cost centre manager must formally certify settlement of all purchase orders, subcontract charges, and timesheet allocations before closure proceeds [^r3].
* Open document check: Ledgerline ERP blocks closure and issues [[err-cc-0310]] if any open documents remain tied to the cost centre [^r7].

## See also

* [[err-cc-0310]]
* [[screen-fin-cc-01|FIN-CC-01 Cost Centre Entry]]
* [[sop-it-001|SOP-IT-001 User Access Request]]
* [[user-gwhitaker|Grace Whitaker (GWHITAKER)]]
* [[user-hweber|Henrik Weber (HWEBER)]]

## References

[^r1]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 1, Cost Centre Open and Close
[^r3]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 2, §3. Responsibilities
[^r2]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 2, §2. Scope
[^r4]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 3, §5. Procedure
[^r7]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 3, §5. Procedure
[^r6]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 3, §5. Procedure
[^r8]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 4, §6. Records
