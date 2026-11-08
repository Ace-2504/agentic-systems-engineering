---
title: "PRD-ECN-06 Engineering Change Entry"
type: "screen"
slug: "screen-prd-ecn-06"
summary: "Ledgerline screen used to raise engineering changes, record cut-over dates, check department sign-offs, and log battery compliance documentation."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | PRD-ECN-06 |
| Screen name | Engineering Change Entry |
| System | Ledgerline |
| Purpose | Raising engineering changes and cut-over management |
| Related procedure | SOP-PRD-002 |

Screen PRD-ECN-06 is the Ledgerline interface used to raise engineering changes and capture effective cut-over dates across Northbridge Cycles production operations [^r1]. Prior to release, users must ensure effective cut-over dates coordinate with stock availability and procurement lead times while verifying departmental sign-offs [^r2]. For modifications involving battery components, the screen enforces specific compliance tracking fields [^r3].

## What it is for
Screen PRD-ECN-06 is used to raise engineering changes and record effective cut-over dates under [[sop-prd-002|SOP-PRD-002]] [^r1]. Before an engineering change notice (ECN) can be released on PRD-ECN-06, the effective date must align with stock availability and procurement lead times [^r2].

## Fields
* **Effective date**: Captures the effective cut-over date, which must align with stock availability and procurement lead times prior to release [^r1][^r2].
* **Quality sign-off indicator**: Displays a completed marker required before releasing an ECN [^r2].
* **Purchasing sign-off indicator**: Displays a completed marker required before releasing an ECN [^r2].
* **Documentation reference**: Records the compliance report reference for alterations affecting [[items-bat|battery cells]] [^r3].
* **Attached file flag**: Confirms that the test report is in the central archive for changes affecting battery cells [^r3].

## Messages
Both the Quality and Purchasing sign-off indicators must display completed markers on screen before an ECN can be released [^r2].

## See also
* [[sop-prd-002|SOP-PRD-002 Engineering Change (ECN)]]
* [[items-bat|BAT-* items]]
* [[err-ecn-0220|ERR-ECN-0220 Open work orders on old revision]]

## References

[^r1]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 3, §5. Procedure: notes and common mistakes
[^r3]: 02_procedures/SOP-PRD-002 Engineering Change v1.0.pdf, p. 3, §5. Procedure: notes and common mistakes
