---
title: "ERR-PER-0010 Unposted Documents at Period Close"
type: "error"
slug: "err-per-0010"
summary: "Ledgerline error preventing period close on screen AP-PER-11 when unposted documents, batches, journals, or matchings remain open."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-AP-002 Period Close v3.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| code | ERR-PER-0010 |
| type | Error |
| system | Ledgerline |
| source document | SOP-AP-002 |
| status | current |

Error ERR-PER-0010 is a Ledgerline system error encountered during the accounts payable period-end routine.[^r1] It blocks an operator from closing a financial period whenever open or unposted transactions remain in the system.[^r1] Resolving the error requires posting valid entries or removing draft batches before re-attempting the closure.[^r2]

## Meaning
ERR-PER-0010 indicates that unposted documents, batches, journals, or matchings remain pending in Ledgerline while an attempt is made to close the period.[^r1]

## Cause
The error triggers on screen [[screen-ap-per-11|AP-PER-11]] when a user attempts to execute a period close while there are still open or draft batches, unposted journals, or incomplete document matchings.[^r1]

## How to fix
Inspect the on-screen batch control screen to identify which specific batch contains open transactions.[^r2] Complete the posting routines for all valid entries, or delete and remove draft batches that should not be posted.[^r2] Once the open items are cleared, retry closing the period on screen [[screen-ap-per-11|AP-PER-11]].[^r2]

## See also
* [[sop-ap-002|SOP-AP-002 Accounts Payable Period Close]]
* [[screen-ap-per-11|AP-PER-11 Ap Period]]

## References

[^r1]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 4, What to do when something does not look right
