---
title: "POL-ITS-008 IT Security Policy"
type: "policy"
slug: "pol-its-008"
summary: "Baseline IT security rules for Ledgerline access, service accounts, password expiry, document classification, and incident reporting."
audience: "staff"
status: "current"
sources: ["01_policies/POL-ITS-008 IT Security Policy v3.2.pdf"]
created: "2026-11-07"
updated: "2026-11-08"
---

| | |
|---|---|
| code | POL-ITS-008 |
| owner | IT department |
| version | 3.2 |
| approver | Rhys Pryce |
| effective | 2025-09-01 |
| status | current |

POL-ITS-008 establishes mandatory IT security controls across Northbridge Cycles, covering system access, account governance, and data classification [^r1]. Version 3.2 is currently in force and is owned by the IT department following approval by IT manager [[user-rpryce|Rhys Pryce]] [^r1]. It sets operational restrictions on Ledgerline passwords, session timeouts, and integration accounts, including an active block on new integrations using [[user-svc-agent|SVC_AGENT]] [^r2][^r3][^r5].

## Clauses

### §2. Passwords
Ledgerline passwords must be at least 12 characters long and expire every 60 days, overriding the vendor shipped defaults [^r2].

### §3. Sessions and sign-in
An idle Ledgerline session is closed after 15 minutes by parameter SYS.SESSION_TIMEOUT, and three wrong passwords lock the user ID for 30 minutes [^r3].

### §4. Service accounts
Every service account must have a named owner, hold only the services it needs, and be reviewed every quarter under job JOB-SYS-015 [^r4]. Under finding ITS-2026-07, integration account [[user-svc-agent|SVC_AGENT]] holds role SYS-ADMIN with every service and no approval limit, and until its review closes no new integration may use it [^r5].

### §5. Information classification
Company documents are INTERNAL unless marked CONFIDENTIAL, and confidential HR documents must be stored only in the restricted HR folder readable solely by the NBC-HR-CONF group [^r6].

### §6. Remote access
Remote access to Ledgerline requires connecting via the company VPN with multi-factor authentication [^r7].

### §7. Reporting incidents
Suspected security incidents must be reported immediately to the IT service desk on internal extension 2210 [^r8].

## Who it applies to
The policy applies to all staff accessing Ledgerline, owners of system and service accounts, and anyone handling internal or confidential company records [^r2][^r4][^r6][^r7].

## See also
* [[user-rpryce|Rhys Pryce (RPRYCE)]]
* [[user-svc-agent|Integration service account (SVC_AGENT)]]

## References

[^r1]: 01_policies/POL-ITS-008 IT Security Policy v3.2.pdf, p. 1, IT Security Policy
[^r2]: 01_policies/POL-ITS-008 IT Security Policy v3.2.pdf, p. 1, §2. Passwords
[^r3]: 01_policies/POL-ITS-008 IT Security Policy v3.2.pdf, p. 2, §3. Sessions and sign-in
[^r5]: 01_policies/POL-ITS-008 IT Security Policy v3.2.pdf, p. 3, §4. Service accounts
[^r4]: 01_policies/POL-ITS-008 IT Security Policy v3.2.pdf, p. 3, §4. Service accounts
[^r6]: 01_policies/POL-ITS-008 IT Security Policy v3.2.pdf, p. 4, §5. Information classification
[^r7]: 01_policies/POL-ITS-008 IT Security Policy v3.2.pdf, p. 5, §6. Remote access
[^r8]: 01_policies/POL-ITS-008 IT Security Policy v3.2.pdf, p. 5, §7. Reporting incidents
