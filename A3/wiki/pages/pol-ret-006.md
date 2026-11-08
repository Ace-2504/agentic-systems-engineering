---
title: "POL-RET-006 Returns Policy"
type: "policy"
slug: "pol-ret-006"
summary: "Rules governing supplier returns within 30 days, 2-year and 5-year bike shop warranty terms, dangerous goods transport, and customer credit note issuance."
audience: "staff"
status: "current"
sources: ["01_policies/POL-RET-006 Returns Policy v2.1.pdf", "02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | POL-RET-006 |
| Owner | Purchase and Sales departments |
| Approver | Henrik Weber |
| Version | 2.1 |
| Effective date | 2025-01-01 |
| Status | current |
| Audience | staff |

POL-RET-006 defines Northbridge Cycles' mandatory standards for processing returns to vendors, handling warranty claims from bike shops, and issuing customer credit notes [^r1]. Version 2.1 is currently in force across all operations, having taken effect on 2025-01-01 under the approval of plant head [[user-hweber|Henrik Weber]] [^r1]. It sets the 30-day window for supplier returns, establishes warranty coverage periods for bicycle components, and restricts hazardous battery return handling [^r2][^r4][^r5][^r6].

## Clauses

### §1. Scope and ownership
POL-RET-006 version 2.1 is effective from 2025-01-01, owned jointly by the Purchase and Sales departments, and approved by plant head [[user-hweber|Henrik Weber]] [^r1].

### §2. Returns to suppliers
Faulty or wrong goods must be returned to the supplier within 30 days of receipt using a return to vendor (RTV) document on screen [[screen-inv-rtv-07|INV-RTV-07]] [^r2]. If the supplier's invoice for the goods has already been posted, staff must raise a debit note on screen [[screen-ap-dbn-04|AP-DBN-04]] instead of an RTV credit, because Ledgerline rejects an RTV against an invoiced receipt with [[err-rtv-0230|ERR-RTV-0230]] [^r3].

### §3. Warranty returns from bike shops
Frames carry a 5-year warranty, while battery packs, motors, chargers, and all other parts carry a 2-year warranty from the date of sale to the rider [^r4]. POL-RET-006 §3.1 sets out the eligible warranty periods and terms that govern warranty claims raised under [[sop-sal-002|SOP-SAL-002]] [^r8]. If Ledgerline ERP shows that the warranty cover period specified in POL-RET-006 §3.1 has lapsed, staff must reject the RMA request and send standard out-of-warranty notification to the bike shop [^r9]. A battery pack returned under warranty is never returned to general stock, but must be transferred directly to battery refurbishment (cost centre PRD-09) or sent for recycling [^r5]. Bike shops must send lithium battery returns using the carrier's dangerous-goods service and never by ordinary parcel [^r6].

### §4. Credit notes to customers
Finance issues credit notes only after Manchester or Leeds confirms receipt and inspection of returned items, matching the credit note directly to the original sales invoice [^r7].

## Who it applies to
This policy applies to the Purchase and Sales departments managing vendor and customer claims, warehouse staff at Manchester and Leeds inspecting returned items, bike shops submitting claims under [[sop-sal-002|SOP-SAL-002]], and Finance teams issuing debit notes or customer credits [^r1][^r2][^r6][^r7][^r8].

## See also
* [[screen-inv-rtv-07|INV-RTV-07 Return To Vendor Entry]]
* [[screen-ap-dbn-04|AP-DBN-04 Debit Note Entry]]
* [[err-rtv-0230|ERR-RTV-0230 RTV Refused Against Invoiced Receipt]]
* [[sop-sal-002|SOP-SAL-002 Warranty Claims from Bike Shops]]
* [[user-hweber|Henrik Weber (HWEBER)]]

## References

[^r1]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 1, Returns Policy
[^r2]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 1, §2. Returns to suppliers
[^r4]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 2, §3. Warranty returns from bike shops
[^r5]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 3, §3. Warranty returns from bike shops
[^r6]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 3, §3. Warranty returns from bike shops
[^r3]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 2, §2. Returns to suppliers
[^r8]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 3, §5. Procedure
[^r9]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r7]: 01_policies/POL-RET-006 Returns Policy v2.1.pdf, p. 4, §4. Credit notes to customers
