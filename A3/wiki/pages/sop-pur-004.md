---
title: "SOP-PUR-004 Rate Contract Maintenance"
type: "procedure"
slug: "sop-pur-004"
summary: "Standard operating procedure for maintaining supplier rate contracts in Ledgerline under role PUR-MGR, including validity periods, reviews, and line updates."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Document code | SOP-PUR-004 |
| Title | Rate Contract Maintenance |
| Version | 2.0 |
| Status | CURRENT |
| Effective date | 2024-03-01 |
| Author | Daniel Okafor |
| Approver | Henrik Weber |

SOP-PUR-004 defines how Northbridge Cycles maintains supplier rate contracts in Ledgerline ERP [^r1][^r9]. As of 26 October 2026, version 2.0 remains in force to ensure all active agreements, validity dates, and unit prices reflect authorized terms [^r1][^r2]. Compliance prevents automated purchase orders from retrieving conflicting or unpredictable pricing [^r9].

## Steps
1. Review expiring agreements identified via expiry report JOB-PUR-031, which lists contracts ending within 45 days during the biannual reviews conducted in March and September pursuant to [[pol-sup-003|POL-SUP-003]] §7.3 [^r5].
2. Access the Rate contracts tab of the supplier master in Ledgerline exclusively under role [[role-pur-mgr|PUR-MGR]] [^r2].
3. Set the contract duration to run for at most 12 months, typically from 1 April to 31 March, or for six months in the case of contracts for [[items-bat|battery packs]] [^r3].
4. Enter the valid-from date for any new rate contract line [^r4].
5. End an existing contract line and add a distinct new line whenever pricing changes, ensuring staff never alter the rate on an existing contract line directly [^r4].
6. Retain all historical contract rows without deleting them, as removing rows damages transaction logs within the system [^r7].
7. Archive agreement documentation: the Manchester buying team retains the definitive master file for each supplier agreement, while the Leeds unit keeps local copies for parts called off directly into their assembly store [^r8].

## Forms and screens
* Supplier master, Rate contracts tab: used exclusively under role [[role-pur-mgr|PUR-MGR]] to enter and maintain contract records [^r2].
* JOB-PUR-031: rate-contract expiry report listing contracts ending within 45 days [^r5].

## Checks and approvals
* SOP-PUR-004 version 2.0 was authored by Purchase Manager [[user-dokafor|Daniel Okafor]], approved by Plant Head [[user-hweber|Henrik Weber]], and became effective on 2024-03-01 with a status of CURRENT [^r1].
* Rate contracts must only be entered by the purchase manager's office under role [[role-pur-mgr|PUR-MGR]] [^r2].
* Staff maintaining contract records must confirm that the unit of purchase and pricing currency are stated in pounds and correspond with standard ordering increments [^r6].
* Staff must manually verify validity dates because Ledgerline ERP does not always block overlapping validity periods automatically, which can cause the purchasing module to select unpredictable prices on automatically generated purchase orders [^r9].

## See also
* [[items-bat|BAT-* items]]
* [[pol-sup-003|POL-SUP-003 Supplier Policy]]
* [[role-pur-mgr|Role PUR-MGR]]
* [[user-dokafor|Daniel Okafor (DOKAFOR)]]
* [[user-hweber|Henrik Weber (HWEBER)]]

## References

[^r1]: 02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf, p. 1, Field Value
[^r9]: 02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf, p. 3, §5. Procedure: notes and common mistakes
[^r2]: 02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf, p. 3, §5. Procedure
[^r3]: 02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf, p. 3, §5. Procedure
[^r7]: 02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf, p. 4, What to do when something does not look right
[^r8]: 02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf, p. 4, §6. Records
[^r6]: 02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf, p. 4, What to check on the screen
