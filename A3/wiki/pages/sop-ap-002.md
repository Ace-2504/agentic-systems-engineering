---
title: "SOP-AP-002 Accounts Payable Period Close"
type: "procedure"
slug: "sop-ap-002"
summary: "Standard operating procedure governing purchase ledger cut-off, accruals, and monthly closing steps across the Manchester and Leeds sites."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-AP-002 Period Close v3.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-AP-002 |
| Version | v3.0 |
| Effective | 2025-04-01 |
| Status | current |
| Owner | Marta Kowalski |
| Approver | Grace Whitaker |

SOP-AP-002 defines the monthly accounts payable closing procedure across Northbridge Cycles' Manchester and Leeds operations [^r1][^r2]. Effective from 1 April 2025, it establishes the operational timeline for invoice registration, accrual generation, cut-off, and ledger sign-off [^r1][^r5][^r6][^r7]. Following these instructions ensures ledger closure is completed without unposted transactions and supporting records are formally archived [^r7][^r10].

## Steps
1. On working day 1, run the goods received not invoiced (GRNI) accrual job JOB-AP-040 at 21:00 [^r5].
2. If the overnight GRNI accrual job fails to complete, notify IT support and do not proceed with manual period closure until accrual balances are regenerated and matched against warehouse receipts [^r9].
3. Apply the accounts payable cut-off on working day 3 at 12:00, posting any invoices received after this deadline to the following period [^r6].
4. During the afternoon of working day 3, close the period on screen [[screen-ap-per-11|AP-PER-11]], resolving error [[err-per-0010|ERR-PER-0010]] if any documents remain unposted [^r7].
5. On working day 4, review the reverse-charge listing JOB-AP-045 in Finance for the VAT return [^r8].
6. Following ledger closure, obtain the finance manager's countersignature on paper printouts of the final aged creditors listing, period summary report, and reconciliation sheet alongside the bank reconciliation, and file them in the monthly purchase ledger binder in Manchester [^r10].

## Forms and screens
* [[screen-ap-per-11|AP-PER-11]] is used by the accounts payable manager to execute the period closure [^r7].
* Ledgerline displays error [[err-per-0010|ERR-PER-0010]] on screen AP-PER-11 if period closure is attempted while unposted documents remain [^r7].
* The procedure references scheduled jobs JOB-AP-040 for GRNI accruals and JOB-AP-045 for reverse-charge VAT listings [^r5][^r8].
* Physical records generated include the final aged creditors listing, period summary report, and reconciliation sheet [^r10].

## Checks and approvals
* The purchase ledger closing procedure applies across both the Manchester assembly works and the Leeds distribution unit [^r2].
* In Manchester, the purchase ledger clerk registers incoming delivery notes, matches site invoices, and reviews the unregistered invoice log [^r3].
* In Leeds, the administrator collects delivery paperwork, logs workshop receipts, and forwards matched invoices to central finance [^r3].
* The accounts supervisor reviews disputed balances, checks parked documents, and verifies supplier statement reconciliations for high-volume accounts [^r4].
* The financial controller, [[user-gwhitaker|Grace Whitaker]], reviews the preliminary aged creditors trial balance, reviews proposed accruals, and signs off the final close [^r1][^r4].
* The procedure is owned by accounts payable manager [[user-mkowalski|Marta Kowalski]] [^r1].

## See also
* [[screen-ap-per-11]]
* [[err-per-0010]]
* [[user-gwhitaker]]
* [[user-mkowalski]]

## References

[^r1]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 1, Accounts Payable Period Close
[^r2]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 1, §1. Purpose
[^r5]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 3, §5. Procedure
[^r6]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 3, §5. Procedure
[^r7]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 3, §5. Procedure
[^r10]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 5, §6. Records
[^r9]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 4, What to do when something does not look right
[^r8]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 3, §5. Procedure
[^r3]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 2, §3. Responsibilities
[^r4]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 2, §3. Responsibilities
