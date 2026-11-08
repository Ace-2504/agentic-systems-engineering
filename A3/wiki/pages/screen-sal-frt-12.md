---
title: "SAL-FRT-12 Carrier Booking Quote"
type: "screen"
slug: "screen-sal-frt-12"
summary: "Ledgerline carrier booking quote screen used to book battery consignments with Moorland Logistics under dangerous-goods service code DGX."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | SAL-FRT-12 |
| Purpose | Carrier Booking Quote |
| Carrier | Moorland Logistics |
| Service code | DGX |
| Source procedure | SOP-SAL-001 |

Screen SAL-FRT-12 is the Ledgerline carrier booking quote interface used during sales despatch operations [^r1]. As of 26 October 2026, staff use this screen to book carrier consignments with contract carrier [[sup-moorland-logistics|Moorland Logistics]] using dangerous-goods service code DGX for battery shipments [^r1]. A successful booking requires complete parcel dimensions and descriptions so the details transfer properly into the carrier's system [^r2].

## What it is for
Screen SAL-FRT-12 is used to book carrier consignments under [[sop-sal-001|SOP-SAL-001 Sales Order to Despatch]] [^r1]. Specifically, it handles bookings with contract carrier [[sup-moorland-logistics|Moorland Logistics]] for consignments requiring dangerous-goods service code DGX, which applies to [[items-bat|battery shipments]] [^r1].

## Fields
* **Parcel dimensions:** Must be fully populated to enable transmission to the carrier system [^r2].
* **Descriptions:** Must be fully populated for the Moorland Logistics booking to transfer successfully [^r2].
* **Service code:** Populated with dangerous-goods code DGX for battery shipments [^r1].

## Messages
The provided sources do not specify system message codes directly displayed on this screen [^r1][^r2].

## See also
* [[sop-sal-001|SOP-SAL-001 Sales Order to Despatch]]
* [[sup-moorland-logistics|Moorland Logistics]]
* [[items-bat|BAT-* items]]

## References

[^r1]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 4, §5. Procedure: notes and common mistakes
