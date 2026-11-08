---
title: "AP-BNK-06 Supplier Bank Details Entry"
type: "screen"
slug: "screen-ap-bnk-06"
summary: "Ledgerline screen used by accounts payable staff to invoke service bnk_verify and log verification calls for supplier bank amendments."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-AP-004 Supplier Bank Detail Changes v2.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | AP-BNK-06 |
| System | Ledgerline |
| Service invoked | bnk_verify |
| Status | current |

Screen AP-BNK-06 is the Ledgerline interface used by accounts payable staff to record verification details for supplier bank amendments [^r1]. Logging verification calls on this screen invokes service bnk_verify to clear supplier payment holds [^r1][^r2]. As of 26 October 2026, it remains the standard screen governed by [[sop-ap-004|SOP-AP-004]] for bank change verification [^r1][^r2].

Screen code: AP-BNK-06
System: Ledgerline
Service invoked: bnk_verify
Status: current

## What it is for
Accounts payable staff use Ledgerline screen AP-BNK-06 to record mandatory verification call details for supplier bank amendments [^r1]. Logging the verification calls on AP-BNK-06 invokes service bnk_verify to clear supplier payment holds [^r1][^r2].

## Fields
Supplier bank verification call details must be logged on this screen [^r1][^r2].

## Messages
The screen invokes service bnk_verify upon entry of the verification call details [^r1][^r2].

## See also
* [[sop-ap-004|SOP-AP-004 Supplier Bank Detail Changes]]
* [[user-gwhitaker|Grace Whitaker (GWHITAKER)]]
* [[user-mkowalski|Marta Kowalski (MKOWALSKI)]]
* [[w-bnk-120|W-BNK-120 Supplier Bank Details Hold]]

## References

[^r1]: 02_procedures/SOP-AP-004 Supplier Bank Detail Changes v2.0.pdf, p. 4, What to check on the screen
[^r2]: 02_procedures/SOP-AP-004 Supplier Bank Detail Changes v2.0.pdf, p. 3, §5. Procedure
