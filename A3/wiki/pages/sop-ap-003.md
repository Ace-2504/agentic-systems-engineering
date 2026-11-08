---
title: "SOP-AP-003 Supplier Payment Run"
type: "procedure"
slug: "sop-ap-003"
summary: "Procedure for bi-weekly supplier payment runs, proposal approval, bank file transmission, and disbursement record retention."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-AP-003 |
| Version | 1.4 |
| Owner | Marta Kowalski |
| Approved by | Grace Whitaker |
| Effective date | 2024-06-01 |
| Status | current |

SOP-AP-003 defines the procedure for executing Northbridge Cycles' standard bi-weekly supplier payment runs [^r1][^r2]. As of 26 October 2026, it governs the automated generation of payment proposals, segregation of duties during approval, and same-day bank transmission deadlines [^r2][^r3][^r4]. It also mandates strict handling of unverified banking details and archiving requirements across sites [^r5][^r7].

## Steps

1. Execute the proposal job JOB-AP-030 at 10:00 on Tuesdays and Thursdays to generate the payment proposal [^r2].
2. Review the generated payment proposal as an AP clerk on [[screen-ap-pay-03|AP-PAY-03]] [^r3].
3. Exclude suppliers automatically if they hold unverified bank details, which triggers [[err-bnk-0101|ERR-BNK-0101]] [^r5].
4. Submit the proposal to the AP manager for sign-off, ensuring that the approver is not the proposer [^r3].
5. Release the payment file JOB-AP-031 in format STD18 to the bank by 14:30 for same-day processing [^r4].
6. File payment run packs chronologically by payment date at Manchester and Leeds locations [^r7].

## Forms and screens

* Screen [[screen-ap-pay-03|AP-PAY-03]]: Used by the AP clerk to review the proposed disbursements [^r3].
* Job JOB-AP-030: Automated proposal job scheduled at 10:00 on Tuesdays and Thursdays [^r2].
* Job JOB-AP-031: Payment file transmission job output in format STD18 [^r4].
* Payment run pack: Physical record set consisting of the signed authorisation sheet, system report of proposed disbursements, final payment summary, and bank transmission confirmation [^r7].

## Checks and approvals

* Owner and approval: Owned by AP manager [[user-mkowalski|Marta Kowalski]] and approved by financial controller [[user-gwhitaker|Grace Whitaker]] [^r1].
* Segregation of duties: The AP manager must approve the proposal reviewed by the AP clerk, but the approver cannot be the proposer [^r3].
* Bank detail validation: System checks automatically reject suppliers with unverified bank details under error [[err-bnk-0101|ERR-BNK-0101]] [^r5].
* Bank detail freezing: Alterations to supplier bank details cannot be made while the payment run is open; staff must wait until the cycle concludes or cancel and rebuild the proposal [^r6].
* Bank deadline check: Transmission of JOB-AP-031 must occur by 14:30 to secure same-day processing [^r4].

## See also

* [[err-bnk-0101|ERR-BNK-0101 Unverified Supplier Bank Details]]
* [[err-pay-0430|ERR-PAY-0430 Approver Cannot Be Proposer]]
* [[screen-ap-pay-03|AP-PAY-03 Payment Run]]
* [[user-gwhitaker|Grace Whitaker (GWHITAKER)]]
* [[user-mkowalski|Marta Kowalski (MKOWALSKI)]]

## References

[^r1]: 02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf, p. 1, Supplier Payment Run
[^r2]: 02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf, p. 3, §5. Procedure
[^r3]: 02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf, p. 3, §5. Procedure
[^r7]: 02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf, p. 4, §6. Records
[^r6]: 02_procedures/SOP-AP-003 Supplier Payment Run v1.4.pdf, p. 3, §5. Procedure: notes and common mistakes
