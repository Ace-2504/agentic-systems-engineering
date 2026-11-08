---
title: "ERR-APR-0003"
type: "error"
slug: "err-apr-0003"
summary: "Ledgerline error triggered when a user attempts to approve a purchase document that they raised themselves."
audience: "staff"
status: "current"
sources: ["01_policies/POL-APR-002 Approval Matrix v3.0.pdf", "01_policies/POL-APR-002 Approval Matrix v3.1.pdf"]
created: "2026-11-08"
updated: "2026-11-08"
---

| | |
|---|---|
| code | ERR-APR-0003 |
| type | Ledgerline error |
| module | Purchasing approval |
| source | POL-APR-002 |
| status | current |

Ledgerline error ERR-APR-0003 prevents self-approval across purchasing workflows. Under [[pol-apr-002|POL-APR-002]], the system raises this error whenever an approver attempts to authorize a document they initiated. As of 26 October 2026, segregation of duties requires another authorized user to approve the record.

## Meaning

ERR-APR-0003 indicates an invalid self-approval attempt in Ledgerline [^r1][^r2].

## Cause

The error is triggered when a user attempts to approve a document that they raised [^r1][^r2].

## How to fix

To resolve the error, the user who raised the document must not attempt to authorize it [^r1][^r2]. The document must instead be routed to another user holding the required approval role under [[pol-apr-002|POL-APR-002]].

## See also

* [[pol-apr-002|POL-APR-002 Approval Matrix for Purchasing]]
* [[err-apr-0009|ERR-APR-0009]]

## References

[^r1]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 2, §4. Who may not approve
[^r2]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 2, §4. Who may not approve
