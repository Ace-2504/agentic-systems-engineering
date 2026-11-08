---
title: "SOP-IT-002 Service Account Management"
type: "procedure"
slug: "sop-it-002"
summary: "Standard operating procedure governing the creation, rotation, security controls, and review of automated background service accounts."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-IT-002 Service Account Management v1.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-IT-002 |
| Title | Service Account Management |
| Owner | Rhys Pryce |
| Approver | Henrik Weber |
| Version | 1.0 |
| Effective | 2025-09-01 |
| Status | current |
| Audience | staff |

SOP-IT-002 governs the administration, lifecycle, and security controls for all automated service accounts across Northbridge Cycles systems [^r1]. Service accounts run automated tasks without human intervention, have interactive logins disabled, and must never be assigned approval authority [^r2][^r3][^r7]. The procedure is currently in force under the ownership of IT manager [[user-rpryce|Rhys Pryce]] and approval of plant head [[user-hweber|Henrik Weber]] [^r1].

## Steps
1. Define the operational scope and verify that the account is intended solely for automated jobs, background interfaces, or operating system tasks such as nightly ledger postings, routine backups, printer spooling services, or data transfers between Manchester and Leeds [^r2].
2. Designate a named primary custodian within IT and an operational business sponsor from the relevant department, documenting a written list of required services [^r4][^r5].
3. Ensure interactive login rights remain disabled and verify that standard staff accounts are not substituted for system tasks [^r3].
4. Store any emergency override passwords directly in the central IT safe rather than on local spreadsheets [^r9].
5. Issue service account keys via screen [[screen-sys-api-14|SYS-API-14]], ensuring keys are valid for at most 90 days and rotated before expiry [^r6].
6. Record the account details—including business justification, linked batch job, primary owner, and repository confirmation—in the central systems register maintained by the IT department [^r11].
7. Execute the quarterly review routine JOB-SYS-015 to verify all active accounts [^r8].

## Forms and screens
- Screen [[screen-sys-api-14|SYS-API-14]] (Service Account Key Issue): used to generate and rotate service account keys that are valid for up to 90 days [^r6].
- Routine JOB-SYS-015: quarterly service account review routine that must be signed off by the IT manager [^r8].
- Central systems register: IT-held register capturing business justification, linked batch job, primary owner, and repository confirmation [^r11].

## Checks and approvals
- In accordance with [[pol-apr-002|POL-APR-002]] §4.2, a service account must never approve documents [^r7].
- If an account appears on an authorisation record or approval queue, its profile must be revoked from the approval workflow immediately and pending documents reassigned [^r10].
- Every service account requires a named primary custodian within IT, a named operational business sponsor, and a written list of needed services [^r4][^r5].
- Quarterly review routine JOB-SYS-015 requires formal sign-off by the IT manager [^r8].

## See also
- [[pol-apr-002|POL-APR-002 Approval Matrix for Purchasing]]
- [[screen-sys-api-14|SYS-API-14 Service Account Key Issue]]
- [[user-hweber|Henrik Weber (HWEBER)]]
- [[user-rpryce|Rhys Pryce (RPRYCE)]]

## References

[^r1]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 1, §1. Purpose
[^r2]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 1, §1. Purpose
[^r3]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 1, §1. Purpose
[^r7]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 2, §3. Responsibilities
[^r5]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 3, §5. Procedure
[^r9]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 3, §3. Responsibilities
[^r6]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 3, §5. Procedure
[^r11]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 5, §6. Records
[^r8]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 3, §5. Procedure
[^r10]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 4, §5. Procedure: notes and common mistakes
