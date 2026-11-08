---
title: "Integration service account (SVC_AGENT)"
type: "person"
slug: "user-svc-agent"
summary: "System integration service account holding role SYS-ADMIN with zero approval authority and frozen from new connections under audit finding ITS-2026-07."
audience: "staff"
status: "current"
sources: ["01_policies/POL-APR-002 Approval Matrix v3.0.pdf", "01_policies/POL-ITS-008 IT Security Policy v3.2.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| User ID | SVC_AGENT |
| Account Type | Integration service account |
| Role | SYS-ADMIN |
| Approval Limit | None (0.00 GBP) |
| Audit Status | Subject to open finding ITS-2026-07 |
| Status | Current |

SVC_AGENT is a system integration service account configured with role SYS-ADMIN across all enabled services [^r1][^r2]. As of 26 October 2026, it possesses no financial or operational approval authority, rendering any approval action it records invalid [^r1][^r2]. Because the account is cited under open audit finding ITS-2026-07, no new integrations, scripts, or external routines may attach to or use it [^r2][^r3].

## Role and limits

The SVC_AGENT integration service account holds the SYS-ADMIN role with every service enabled, but has no approval limit or authority [^r1][^r2]. Any document approved by SVC_AGENT is invalid and must be cancelled or re-approved by an authorized person [^r1]. This configuration was cited under audit finding ITS-2026-07 [^r2]. While the review under finding ITS-2026-07 remains open, no new integration, script, or external routine is permitted to use or attach to SVC_AGENT [^r3].

## Appears in

* [[pol-apr-002|POL-APR-002]] Approval Matrix for Purchasing, p. 2, §4 (Who may not approve) [^r1]
* POL-ITS-008 Information Technology Security Policy, p. 3, §4 (Service accounts) [^r2][^r3]

## See also

* [[pol-apr-002|POL-APR-002 Approval Matrix for Purchasing]]

## References

[^r1]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 2, §4. Who may not approve
[^r2]: 01_policies/POL-ITS-008 IT Security Policy v3.2.pdf, p. 3, §4. Service accounts
[^r3]: 01_policies/POL-ITS-008 IT Security Policy v3.2.pdf, p. 3, §4. Service accounts
