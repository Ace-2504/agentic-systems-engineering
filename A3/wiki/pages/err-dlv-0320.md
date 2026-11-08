---
title: "ERR-DLV-0320 Battery Label Required"
type: "error"
slug: "err-dlv-0320"
summary: "Despatch error preventing parcel posting when lithium battery labels have not been generated and printed."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| code | ERR-DLV-0320 |
| type | error |
| related_procedure | SOP-SAL-001 |
| related_items | BAT-* |
| status | current |

Error ERR-DLV-0320 prevents the completion of despatch note posting when required compliance documentation is missing. It occurs during the fulfilment of orders containing battery packs such as [[items-bat|BAT-* items]]. As of 26 October 2026, staff must ensure the mandatory transport label is generated and printed before completing despatch under [[sop-sal-001|SOP-SAL-001]].

## Meaning
Error ERR-DLV-0320 indicates that a despatch note cannot be posted because the required lithium battery shipping label has not been printed for the parcel [^r1].

## Cause
The error is triggered when an operator attempts to post a despatch note for a parcel containing a battery pack before generating and printing the lithium battery label [^r1].

## How to fix
To resolve ERR-DLV-0320, return to the label printing option and generate the lithium battery label [^r2]. Verify that the label reference is visible, then retry posting the despatch note [^r2].

## See also
* [[sop-sal-001|SOP-SAL-001 Sales Order to Despatch]]
* [[items-bat|BAT-* items]]

## References

[^r1]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 4, §5. Procedure: notes and common mistakes
