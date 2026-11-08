---
title: "err-cc-0310"
type: "error"
slug: "err-cc-0310"
summary: "Error raised when attempting to close a cost centre that still has open documents, active commitments, or incomplete purchase orders."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Error code | ERR-CC-0310 |
| Type | Cost centre closure validation error |
| Source procedure | SOP-FIN-001 |
| Screen | FIN-CC-01 |
| Trigger | Open commitments or unposted documents |
| Resolution | Clear, cancel, or transfer all commitments |

Error ERR-CC-0310 is a validation block triggered in Ledgerline during cost centre maintenance under [[sop-fin-001|SOP-FIN-001]]. It prevents staff from closing any cost centre that continues to hold active financial transactions, incomplete purchase orders, or unposted goods receipts [^r1]. As of 26 October 2026, the error requires users to clear all commitments before the cost centre record can be successfully closed [^r1][^r2].

Error code: ERR-CC-0310
Type: Cost centre closure validation error
Source procedure: SOP-FIN-001
Screen: FIN-CC-01
Trigger: Open commitments or unposted documents
Resolution: Clear, cancel, or transfer all commitments

## Meaning

Error ERR-CC-0310 signals that a cost centre cannot be closed because it remains associated with active accounting or purchasing transactions [^r1].

## Cause

The error occurs when an attempt is made to close a cost centre that still contains open documents, incomplete purchase orders, open purchase requisitions, unposted goods receipts, or active commitments [^r1].

## How to fix

To resolve ERR-CC-0310, users must run the commitment enquiry to identify every open document tied to the cost centre [^r2]. Users must then arrange for originators to cancel redundant orders or transfer ongoing commitments to a replacement cost centre before reattempting closure [^r2].

## See also

* [[sop-fin-001|SOP-FIN-001 Cost Centre Open and Close]]
* [[screen-fin-cc-01|FIN-CC-01 Cost Centre Entry]]

## References

[^r1]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 3, Common mistakes
[^r2]: 02_procedures/SOP-FIN-001 Cost Centre Open and Close v1.1.pdf, p. 4, What to do when something does not look right
