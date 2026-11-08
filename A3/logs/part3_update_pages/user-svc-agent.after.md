---
title: "Integration service account (SVC_AGENT)"
type: "person"
slug: "user-svc-agent"
summary: "System integration service account holding SYS-ADMIN with zero approval authority under POL-APR-002 and frozen from new connections under audit finding ITS-2026-07."
audience: "staff"
status: "current"
sources: ["01_policies/POL-APR-002 Approval Matrix v3.0.pdf", "01_policies/POL-ITS-008 IT Security Policy v3.2.pdf", "01_policies/POL-APR-002 Approval Matrix v3.1.pdf"]
created: "2026-11-08"
updated: "2026-11-08"
---

| | |
|---|---|
| User ID | SVC_AGENT |
| Account Type | Integration service account |
| Role | SYS-ADMIN |
| Approval Limit | None |
| Audit Status | Open finding ITS-2026-07 |
| Status | Current |

SVC_AGENT is an integration service account holding role SYS-ADMIN with every service enabled [^r1][^r2]. Under [[pol-apr-002|POL-APR-002]], it has no approval authority, and any document it approves is considered unapproved [^r4]. While the review under audit finding ITS-2026-07 remains open, no new integration, script, or external routine may use or attach to SVC_AGENT [^r2][^r3].

## Role and limits

SVC_AGENT holds the SYS-ADMIN role across every enabled service but has no approval authority or approval limit [^r2][^r4]. Under [[pol-apr-002|POL-APR-002]], any document approved by SVC_AGENT is considered unapproved [^r4]. The configuration of role SYS-ADMIN across all services with no approval limit was cited as audit finding ITS-2026-07 [^r2]. While the review under finding ITS-2026-07 remains open, no new integration, script, or external routine may use or attach to SVC_AGENT [^r3].

## Appears in

* [[pol-apr-002|POL-APR-002]] v3.1, p. 2, §4. Who may not approve [^r4]
* [[pol-its-008|POL-ITS-008]] v3.2, p. 3, §4. Service accounts [^r2][^r3]

## Versions and conflicts

* **Document approval status**: Under POL-APR-002 v3.1 (in force 2026-10-26), any document approved by SVC_AGENT is considered unapproved [^r4]. Under superseded POL-APR-002 v3.0 (2026-04-01), any document it approved was invalid and had to be cancelled or re-approved by a person [^r1]. Kind: `superseded`.

## See also

* [[pol-apr-002|POL-APR-002 Approval Matrix for Purchasing]]
* [[pol-its-008|POL-ITS-008 IT Security Policy]]

## References

[^r1]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 2, §4. Who may not approve
[^r2]: 01_policies/POL-ITS-008 IT Security Policy v3.2.pdf, p. 3, §4. Service accounts
[^r4]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 2, §4. Who may not approve
[^r3]: 01_policies/POL-ITS-008 IT Security Policy v3.2.pdf, p. 3, §4. Service accounts
