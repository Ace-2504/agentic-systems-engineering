---
title: "POL-PUR-001 Purchase Policy"
type: "policy"
slug: "pol-pur-001"
summary: "Core purchasing policy covering purchase requests, direct order thresholds, cost centres, approval limits, supplier qualification, and contract pricing."
audience: "staff"
status: "mixed"
sources: ["01_policies/AMD-PUR-2026-03_Amendment3_PurchasePolicy_DIRlimit.pdf", "01_policies/POL-APR-002 Approval Matrix v3.0.pdf", "01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf", "01_policies/old/Purchase Policy v4.0.docx", "01_policies/old/purchase_policy_v3_2019.docx", "02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Document code | POL-PUR-001 |
| Owner | [[user-dokafor|Daniel Okafor]] |
| Approver | [[user-hweber|Henrik Weber]] |
| Effective date | 2026-04-01 |
| Status | current |
| Version | 4.1 |

POL-PUR-001 governs procurement across Northbridge Cycles, defining the requirements for requisitions, approvals, supplier qualifications, and contract pricing [^r3][^r4]. Version 4.1 is currently in force as of 26 October 2026, authored by [[user-dokafor|Daniel Okafor]] and approved by plant head [[user-hweber|Henrik Weber]] [^r3]. It mandates that purchases through Ledgerline ERP adhere to cost centre budgets and strict gross-value approval thresholds [^r4][^r8][^r10].

## Who it applies to

The purchase policy applies to every purchase made through Ledgerline ERP for the Manchester plant (NBC-MAN-01) and the Leeds unit (NBC-LDS-01) [^r4].

## Clauses

### 3. Requests before orders

Every purchase in Ledgerline must start with a purchase request naming the item, quantity, need-by date, warehouse, and cost centre, unless it qualifies as a direct order [^r5]. A direct purchase order without a prior purchase request is permitted only when its gross value, including VAT, is £50,000 or less [^r6]. A purchase order raised against an approved purchase request must not exceed the quantity requested [^r7].

### 4. Cost centres and budgets

Every purchase request and purchase order must be charged to an open cost centre, as Ledgerline saves an order against a closed cost centre as a Draft that cannot be sent to a supplier [^r8]. Purchasing staff must check a cost centre's status in Ledgerline on screen [[screen-fin-cc-01|FIN-CC-01]] or verify with Finance before raising an order [^r9].

### 5. Approval limits

Purchasing approval limits apply strictly to the gross order value including VAT, freight, and packing, as defined in approval matrix [[pol-apr-002|POL-APR-002]] [^r1][^r10]. Self-approval is strictly prohibited, meaning no employee may approve a purchase order they raised, which triggers Ledgerline error [[err-apr-0003|ERR-APR-0003]] if attempted [^r2][^r11]. An order exceeding the raiser's approval limit must be approved by the next person up the line whose authority covers the gross value [^r12]. Approval of a purchase request covers the subsequent purchase order, provided the original approver's limit covers the order's gross value [^r13].

### 6. Supplier qualification

Orders may only be placed with active suppliers onboarded in the supplier master under Supplier Policy [[pol-sup-003|POL-SUP-003]] [^r14]. Lithium-cell parts such as battery packs, hub motors, chargers, and any item marked cell_safety = 1 may only be purchased from suppliers holding a verified, valid UN 38.3 test certificate uploaded in Ledgerline [^r15]. An expired UN 38.3 test certificate counts as no certificate, and orders must not be placed until a valid certificate is on file [^r16]. Buyers must prefer suppliers with a current rate contract, and a cheaper quotation from a new supplier does not justify switching suppliers for a lithium-cell part [^r17].

### 7. Prices

Purchase orders must use the rate in the current rate contract, and any order placed at more than 2% above the contract rate requires the manager's written justification in the remarks [^r18]. Items covered by an active rate contract do not require quotations and must be ordered directly at the contract rate per POL-PUR-001 §7.1 [^r21].

### 8. Tax

Invoices and purchase orders for UK suppliers must use UK VAT tax codes ending in -UK, while non-UK suppliers must be assigned reverse-charge tax codes ending in -RC [^r19].

### 9. Records

A purchase order must reach Released status and carry an official Ledgerline document number before the supplier is instructed to deliver or the requester is notified [^r20].

## Versions and conflicts

- Direct order threshold: Today, direct purchase orders without a purchase request are permitted up to £50,000 gross value including VAT [^r6][^r22]. From 1 December 2026, under amendment [[amd-pur-2026-03|AMD-PUR-2026-03]], direct orders are restricted to £25,000 or less [^r23]. In superseded version 3.0, the limit was £30,000 [^r38]. Sources: POL-PUR-001 v4.1 (2026-04-01), AMD-PUR-2026-03 v1.0 (2026-12-01), and purchase_policy_v3_2019.docx (2019-04-01); kinds: future_dated, superseded.
- Contract price tolerance: Today, an order placed at more than 2% above the contract rate requires written justification [^r18]. In superseded version 4.0, the threshold was 5% [^r34]. Sources: POL-PUR-001 v4.1 (2026-04-01) and Purchase Policy v4.0.docx; kind: superseded.
- Scope of UN 38.3 certification: Today, UN 38.3 certificates are required for all lithium-cell parts including battery packs, hub motors, chargers, and items with cell_safety = 1 [^r15]. In superseded version 3.0, this applied only to battery packs and explicitly excluded hub motors and chargers [^r40]. Sources: POL-PUR-001 v4.1 (2026-04-01) and purchase_policy_v3_2019.docx (2019-04-01); kind: superseded.

## See also

- [[pol-apr-002|POL-APR-002 Approval Matrix for Purchasing]]
- [[pol-sup-003|POL-SUP-003 Supplier Policy]]
- [[amd-pur-2026-03|AMD-PUR-2026-03 Amendment 3 to the Purchase Policy]]
- [[screen-fin-cc-01|FIN-CC-01 Cost Centre Entry]]
- [[sop-pur-006|SOP-PUR-006 Quotations and Supplier Selection]]
- [[err-apr-0003|ERR-APR-0003]]
- [[user-dokafor|Daniel Okafor (DOKAFOR)]]
- [[user-hweber|Henrik Weber (HWEBER)]]

## References

[^r3]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 1, Purchase Policy
[^r4]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 1, §2. Scope
[^r8]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 1, §4. Cost centres and budgets
[^r10]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §5. Approval limits
[^r5]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 1, §3. Requests before orders
[^r6]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 1, §3. Requests before orders
[^r7]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 1, §3. Requests before orders
[^r9]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 1, §4. Cost centres and budgets
[^r1]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, §1. Purpose
[^r2]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 2, §4. Who may not approve
[^r11]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §5. Approval limits
[^r12]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §5. Approval limits
[^r13]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §5. Approval limits
[^r14]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §6. Supplier qualification
[^r15]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §6. Supplier qualification
[^r16]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §6. Supplier qualification
[^r17]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §6. Supplier qualification
[^r18]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §7. Prices
[^r21]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 3, §5. Procedure
[^r19]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §8. Tax
[^r20]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §9. Records
[^r22]: 01_policies/AMD-PUR-2026-03_Amendment3_PurchasePolicy_DIRlimit.pdf, p. 1, §1. What changes
[^r23]: 01_policies/AMD-PUR-2026-03_Amendment3_PurchasePolicy_DIRlimit.pdf, p. 1, §1. What changes
[^r38]: 01_policies/old/purchase_policy_v3_2019.docx, # 3. Requests before orders
[^r34]: 01_policies/old/Purchase Policy v4.0.docx, §7. Prices
[^r40]: 01_policies/old/purchase_policy_v3_2019.docx, # 6. Supplier qualification
