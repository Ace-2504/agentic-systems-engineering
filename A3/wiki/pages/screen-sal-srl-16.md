---
title: "SAL-SRL-16 Serial Registration Reg"
type: "screen"
slug: "screen-sal-srl-16"
summary: "Ledgerline screen holding the serial register for bike frames and battery packs to validate retailer warranty claims."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | SAL-SRL-16 |
| System | Ledgerline |
| Purpose | Serial Registration Register |
| Related procedure | SOP-SAL-002 |
| Status | current |

Ledgerline screen SAL-SRL-16 holds the serial register required for bike frame and battery pack serial numbers [^r1]. Under [[sop-sal-002|SOP-SAL-002]], warranty administrators use this screen to verify that a serial number is registered to the retailer raising a warranty claim before an RMA can be generated [^r1][^r2]. As of 26 October 2026, an absent serial registration on this screen halts claim processing [^r2].

## What it is for
Ledgerline screen SAL-SRL-16 serves as the serial register where bike frame and battery pack serial numbers must be registered for a bike shop warranty claim to be accepted [^r1]. Warranty administrators must check SAL-SRL-16 to confirm that the bike frame or battery pack appears on the register and belongs to the retailer raising the claim [^r2].

## Fields
- Frame serial number: Serial identifier for bike frames registered in the system [^r1].
- Battery pack serial number: Serial identifier for battery packs registered in the system [^r1].
- Retailer: The bike shop or retailer associated with the registered serial number [^r2].

## Messages
- [[err-rma-0210|ERR-RMA-0210]]: Triggered when a serial number is absent from the register, which prevents RMA generation [^r2].

## See also
- [[err-rma-0210|ERR-RMA-0210 Unregistered Serial Number]]
- [[sop-sal-002|SOP-SAL-002 Warranty Claims from Bike Shops]]

## References

[^r1]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 3, §5. Procedure: notes and common mistakes
