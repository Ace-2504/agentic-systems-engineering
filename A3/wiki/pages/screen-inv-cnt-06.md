---
title: "INV-CNT-06 Stock Count Entry"
type: "screen"
slug: "screen-inv-cnt-06"
summary: "Ledgerline screen used to lock and freeze a physical stock count area before counting begins."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-INV-003 Stock Count v1.2.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | INV-CNT-06 |
| Name | Stock Count Entry |
| System | Ledgerline |
| Purpose | Freeze physical count area |
| Status | Current |

Ledgerline screen INV-CNT-06 is used during stocktaking under [[sop-inv-003|SOP-INV-003]] to freeze a physical count area prior to counting stock [^r1]. It ensures inventory activity is halted in the designated area so counting can proceed against frozen records [^r1]. As of 26 October 2026, the screen requires all pending activity to be cleared, refusing to lock any count zone that contains open transactions [^r2].

Screen code: INV-CNT-06
Name: Stock Count Entry
System: Ledgerline
Purpose: Freeze physical count area
Status: Current

## What it is for
Screen INV-CNT-06 is used to freeze the physical count area prior to counting stock [^r1].

## Fields
This screen operates on the target count zone to apply a freeze for counting [^r1][^r2].

## Messages
Ledgerline screen INV-CNT-06 refuses to lock a count zone if there are open transactions such as unposted pick lists, work orders, or inter-site transfers [^r2]. When this occurs, an error such as [[err-cnt-0230|ERR-CNT-0230 Open Transactions in Count Area]] may be encountered [^r2].

## See also
* [[sop-inv-003|SOP-INV-003 Stock Count (cycle and annual)]]
* [[err-cnt-0230|ERR-CNT-0230 Open Transactions in Count Area]]
* [[screen-inv-ccp-14|INV-CCP-14 Cycle Count Plan Entry]]

## References

[^r1]: 02_procedures/SOP-INV-003 Stock Count v1.2.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-INV-003 Stock Count v1.2.pdf, p. 4, §5. Procedure: notes and common mistakes
