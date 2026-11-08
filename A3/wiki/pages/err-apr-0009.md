---
title: "ERR-APR-0009"
type: "error"
slug: "err-apr-0009"
summary: "Ledgerline error when an order exceeds £5,000,000 gross, signalling that Managing Director approval outside Ledgerline is required."
audience: "staff"
status: "current"
sources: ["01_policies/POL-APR-002 Approval Matrix v3.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Error code | ERR-APR-0009 |
| System | Ledgerline |
| Trigger condition | Order exceeds £5,000,000 gross |
| Source document | POL-APR-002 |

Ledgerline error ERR-APR-0009 indicates that no approver could be found within the system for an order [^r1]. It displays when an order exceeds £5,000,000 gross, reaching beyond the configured in-system approval limits defined in [[pol-apr-002|POL-APR-002]] [^r1]. The message signals that written approval from the Managing Director outside Ledgerline is required to proceed [^r1].

## Meaning
ERR-APR-0009 means "no approver found" within the Ledgerline system routing [^r1].

## Cause
The error triggers when a purchase order value exceeds £5,000,000 gross, exceeding the highest automated approval threshold in Ledgerline [^r1].

## How to fix
Obtain written approval from the Managing Director outside Ledgerline [^r1].

## See also
* [[pol-apr-002|POL-APR-002 Approval Matrix for Purchasing]]
* [[err-apr-0003|ERR-APR-0003]]

## References

[^r1]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, §3. The limits
