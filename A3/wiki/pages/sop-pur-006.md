---
title: "SOP-PUR-006 Quotations and Supplier Selection"
type: "procedure"
slug: "sop-pur-006"
summary: "Procedure for gathering, evaluating, and recording supplier quotations for purchases exceeding thresholds or requiring technical certification."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-PUR-006 |
| Owner | Daniel Okafor |
| Approver | Henrik Weber |
| Version | v1.0 |
| Effective date | 2024-09-01 |
| Status | current |

SOP-PUR-006 defines the process Northbridge Cycles follows to obtain, evaluate, and record supplier quotations prior to issuing purchase orders [^r1]. It covers direct materials for Manchester, sub-assemblies for Leeds, and indirect purchases across the company [^r1]. The standard ensures compliance with quotation thresholds, master contract terms, and battery safety certification rules [^r3][^r4][^r6].

## Steps

1. **Assess procurement requirement and grouping**: Group purchase requisitions for the same project or related parts together rather than splitting them to determine the total gross requirement [^r7].
2. **Verify existing rate contracts**: Check whether the required items are covered under a current rate contract; if covered, order directly at the agreed contract rate under [[pol-pur-001|POL-PUR-001]] clause 7.1 without soliciting new quotations [^r4]. If a quoted price differs from an active rate contract, stop transactions immediately and refer the discrepancy to the contracts team before raising a purchase order [^r11].
3. **Obtain written quotations**: If the new procurement requirement exceeds £100,000 gross, obtain three written quotations [^r3]. If only two quotations can be obtained above this threshold, request written dispensation from [[user-dokafor|Daniel Okafor]] before signing the comparison form [^r8].
4. **Verify supplier onboarding and certificates**:
   - If a quotation arrives from a supplier not listed in the supplier master, initiate onboarding under [[sop-pur-001|SOP-PUR-001]] and withhold acceptance until onboarding completes [^r5]. If an order is entered for an unlisted vendor, hold it in the system and do not release it until onboarding finishes and the ledger account is active [^r10].
   - For [[items-bat|lithium-cell parts]], compare only quotations from suppliers with a valid UN 38.3 test certificate, and ensure price alone does not determine selection [^r6]. Set aside any quotation immediately if its UN 38.3 certificate is unverified, expired, incomplete, or ambiguous until verified by quality engineering [^r9].
5. **Evaluate and record**: Compare the quotes on form NBC-F-118 [^r3]. Compile all requests, written quotes, evaluation matrices, and signed approval notes into a single sourcing pack, then attach it to the master supplier file and requisition trail in Ledgerline ERP [^r12].

## Forms and screens

- Form NBC-F-118 (quotation comparison form) [^r3][^r8]
- Ledgerline ERP requisition trail and master supplier file attachment screens [^r12]

## Checks and approvals

- Owner: Purchase Manager [[user-dokafor|Daniel Okafor]] [^r2].
- Approved by: Plant Head [[user-hweber|Henrik Weber]] on 2024-09-01 [^r2].
- Written dispensation from the purchasing manager is mandatory to sign form NBC-F-118 when fewer than three quotations are obtained for requirements above £100,000 gross [^r3][^r8].
- Quality engineering verification is required before progressing quotes with ambiguous, unverified, incomplete, or expired UN 38.3 test certificates [^r9].

## See also

- [[items-bat|BAT-* items]]
- [[pol-pur-001|POL-PUR-001 Purchase Policy]]
- [[sop-pur-001|SOP-PUR-001 Supplier Onboarding]]
- [[sop-pur-005|SOP-PUR-005 Certificate Renewal (UN 38.3)]]
- [[user-dokafor|Daniel Okafor]]
- [[user-hweber|Henrik Weber]]

## References

[^r1]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 1, §1. Purpose
[^r3]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 3, §5. Procedure
[^r6]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 3, §5. Procedure
[^r7]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 3, §5. Procedure: notes and common mistakes
[^r11]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 4, What to do when something does not look right
[^r8]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 4, What to do when something does not look right
[^r5]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 3, §5. Procedure
[^r10]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 4, What to do when something does not look right
[^r9]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 4, What to do when something does not look right
[^r12]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 4, Records
[^r2]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 1, Version history
