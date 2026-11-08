---
title: "SOP-SAL-001 Sales Order to Despatch"
type: "procedure"
slug: "sop-sal-001"
summary: "Standard operating procedure governing sales order entry, picking, carrier booking, dangerous goods labelling, and despatch confirmation for bicycles and accessories."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-SAL-001 |
| Owner | Isla Morgan |
| Approver | Henrik Weber |
| Version | 2.2 |
| Effective date | 2025-03-01 |
| Status | current |

SOP-SAL-001 defines the end-to-end standard procedure for processing bike shop orders through to physical despatch and carrier collection [^r1][^r4]. As of 26 October 2026, version 2.2 is in force across both the Manchester factory and the Leeds site [^r1][^r2]. Compliance ensures correct automated credit control checks, mandatory hazardous goods handling for parcels containing battery packs, and prompt revenue recognition upon despatch [^r3][^r4][^r6][^r7].

| Field | Value |
|---|---|
| Code | SOP-SAL-001 |
| Title | Sales Order to Despatch |
| Owner | [[user-imorgan|Isla Morgan]] |
| Approver | [[user-hweber|Henrik Weber]] |
| Version | 2.2 |
| Effective date | 2025-03-01 |
| Status | current |

## Steps

1. Enter the bike shop's order on screen [[screen-sal-so-01|SAL-SO-01]] and confirm it, drawing complete frames and finished electric bicycles from the Manchester factory, or allocating certain boxed accessories and replacement [[items-bat|battery units]] from Leeds [^r2][^r4].
2. Confirm the order before the 15:30 cut-off to ensure warehouse staff pick the goods on the same day for next working day UK delivery [^r5].
3. Print a lithium battery label for every parcel containing a battery pack before posting the despatch confirmation [^r6].
4. Book the consignment on screen [[screen-sal-frt-12|SAL-FRT-12]] using contract carrier [[sup-moorland-logistics|Moorland Logistics]], selecting dangerous-goods service code DGX for all battery consignments [^r7].
5. Post the despatch confirmation against the sales order record so that Finance can raise the sales invoice [^r3].
6. Hand parcels to the carrier at the loading bay, collect the signed collection manifests, pair them with the office copy of the delivery note, and file them chronologically by despatch sequence in the despatch office [^r8][^r9].

## Forms and screens

* Screen [[screen-sal-so-01|SAL-SO-01]]: Used to input customer sales orders and run automated credit limit validations [^r4].
* Screen [[screen-sal-frt-12|SAL-FRT-12]]: Used to book carrier transport, specifically requiring service code DGX with [[sup-moorland-logistics|Moorland Logistics]] for battery consignments [^r7].
* Physical documents: Office copy of the delivery note and signed carrier collection manifests, which must be filed chronologically by despatch sequence in the despatch office [^r9].

## Checks and approvals

* Credit check: Confirming the order on screen [[screen-sal-so-01|SAL-SO-01]] automatically performs a credit limit validation, triggering error [[err-crd-0207|ERR-CRD-0207]] if the customer's account limit is exceeded [^r4].
* Lithium battery check: A lithium battery label must be printed for every parcel containing a battery pack prior to posting the despatch, or error [[err-dlv-0320|ERR-DLV-0320]] is raised by the system [^r6].
* Service code validation: Battery consignments must be booked under dangerous-goods service code DGX rather than standard service, or [[sup-moorland-logistics|Moorland Logistics]] will refuse collection at the loading bay or return the parcels [^r7][^r8].
* Invoice release prerequisite: Finance is permitted to raise the sales invoice only after despatch confirmation has been posted against the sales order record [^r3].
* Management approvals: Procedure ownership is held by sales manager [[user-imorgan|Isla Morgan]] with formal operational sign-off by plant head [[user-hweber|Henrik Weber]] [^r1].

## See also

* [[screen-sal-so-01|SAL-SO-01 Sales Order]]
* [[screen-sal-frt-12|SAL-FRT-12 Carrier Booking Quote]]
* [[err-crd-0207|ERR-CRD-0207 Credit Limit Exceeded]]
* [[err-dlv-0320|ERR-DLV-0320 Battery Label Required]]
* [[items-bat|BAT-* items]]
* [[sup-moorland-logistics|Moorland Logistics]]
* [[user-hweber|Henrik Weber (HWEBER)]]
* [[user-imorgan|Isla Morgan (IMORGAN)]]

## References

[^r1]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 1, Sales Order to Despatch
[^r4]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 1, §1. Purpose
[^r3]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 2, §2. Scope
[^r6]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 3, §5. Procedure
[^r7]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 3, §5. Procedure
[^r8]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 3, §5. Procedure: notes and common mistakes
[^r9]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 4, §6. Records
