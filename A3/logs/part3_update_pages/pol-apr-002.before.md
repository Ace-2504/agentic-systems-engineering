---
title: "POL-APR-002 Approval Matrix for Purchasing"
type: "policy"
slug: "pol-apr-002"
summary: "Purchasing approval matrix setting gross monetary limits per document for purchasing roles, prohibition of self-approval, and routing rules up to the Managing Director."
audience: "staff"
status: "mixed"
sources: ["01_policies/POL-APR-002 Approval Matrix v3.0.pdf", "01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf", "01_policies/old/Approval_Matrix_v2.0_2024.docx", "01_policies/old/purchase_policy_v3_2019.docx", "02_procedures/SOP-IT-001 User Access Request v1.6.pdf", "02_procedures/SOP-IT-002 Service Account Management v1.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Document code | POL-APR-002 |
| Title | Approval Matrix for Purchasing |
| Owner | D. Okafor |
| Approver | Henrik Weber |
| Effective date | 2026-04-01 |
| Version | 3.0 |
| Status | current |

POL-APR-002 defines the financial approval matrix for purchase requests and purchase orders across Northbridge Cycles, serving as the matrix referenced in [[pol-pur-001|POL-PUR-001]] §5.2 [^r2]. Version 3.0 took effect on 2026-04-01 following approval by Plant Head [[user-hweber|Henrik Weber]], replacing version 2.0 [^r1]. It sets the per-document gross monetary limits for each purchasing role, controls delegation, and enforces strict prohibitions against self-approval and service account authorisation in Ledgerline [^r3][^r6][^r10][^r11].

## Clauses

### §1. Purpose
POL-APR-002 establishes who may approve a purchase request or purchase order and up to what value, serving as the matrix referenced in Purchase Policy §5.2 [^r2].

### §2. How limits are measured
Every approval limit is evaluated against the gross value including VAT of a single document, and any freight or packing charged on the order counts toward this gross value [^r3][^r14]. Approval limits apply per document, not per day or per supplier [^r4]. Splitting a single requirement into multiple orders to remain within an approval limit is prohibited, and orders for the same item from the same supplier raised within seven days are treated as one requirement [^r5].

### §3. The limits
The gross approval limits including VAT are £250,000 for [[role-pur-exec|PUR-EXEC]], £500,000 for [[role-pur-sr|PUR-SR]], £1,000,000 for [[role-pur-mgr|PUR-MGR]], and £5,000,000 for [[role-plant-head|PLANT-HEAD]], while [[role-stores|STORES]] has no approval authority [^r6]. A document falling within the raiser's own approval limit is automatically approved upon submission, with Ledgerline recording the raiser as approver [^r7]. A document exceeding the raiser's limit routes to the raiser's manager, continuing up the management line until reaching the first person whose limit covers the gross value [^r8]. Documents exceeding £5,000,000 gross trigger Ledgerline error [[err-apr-0009|ERR-APR-0009]] and require the Managing Director's written approval outside Ledgerline, which is subsequently recorded by the plant head's office [^r9].

### §4. Who may not approve
Under Purchase Policy §5.3, users cannot approve documents they raised, and Ledgerline blocks self-approval attempts with [[err-apr-0003|ERR-APR-0003]] [^r10]. Integration and service accounts holding role SYS-ADMIN (such as [[user-svc-agent|SVC_AGENT]]) possess no approval authority under POL-APR-002, and any document approved by a service account is treated as unapproved and must be cancelled or re-approved by a person [^r11][^r16]. An approver on leave may delegate approval authority in writing to an individual of the same or higher role for a stated period, but delegation to a lower role is prohibited [^r12].

### §5. Procedure and access alignment
User approval limits assigned during Ledgerline access setup must strictly match the approval matrix in POL-APR-002 for that job title [^r15].

### §6. Review
The plant head reviews POL-APR-002 annually every April, as well as whenever organisational changes occur [^r13].

## Who it applies to
This policy applies to all personnel raising or approving purchasing documents, including roles [[role-pur-exec|PUR-EXEC]], [[role-pur-sr|PUR-SR]], [[role-pur-mgr|PUR-MGR]], [[role-plant-head|PLANT-HEAD]], and [[role-stores|STORES]], as well as IT administrators assigning user roles and managing service accounts [^r6][^r11][^r15][^r16]. Author [[user-dokafor|D. Okafor]] and Plant Head [[user-hweber|Henrik Weber]] govern its issue and annual review [^r1][^r13].

## Versions and conflicts
- Gross approval limits | Gross limits are £250,000 for PUR-EXEC, £500,000 for PUR-SR, £1,000,000 for PUR-MGR, and £5,000,000 for PLANT-HEAD [^r6] | Under superseded POL-APR-002 v2.0 (2024-04-01), the limits were £200,000 for PUR-EXEC, £400,000 for PUR-SR, £750,000 for PUR-MGR, and £5,000,000 for PLANT-HEAD [^r24] | POL-APR-002 v3.0, p. 1, §3; Approval_Matrix_v2.0_2024.docx, Practical tips | superseded
- Ownership | Version 3.0 (2026-04-01) was authored by D. Okafor and approved by Plant Head Henrik Weber [^r1] | Under superseded v2.0 (2024-04-01), the document owner was the Plant head's office [^r17] | POL-APR-002 v3.0, p. 1, Version history; Approval_Matrix_v2.0_2024.docx, Practical tips | superseded

## See also
- [[pol-pur-001|POL-PUR-001 Purchase Policy]]
- [[sop-it-001|SOP-IT-001 User Access Request]]
- [[sop-it-002|SOP-IT-002 Service Account Management]]
- [[err-apr-0003|ERR-APR-0003]]
- [[err-apr-0009|ERR-APR-0009]]
- [[role-pur-exec|Role PUR-EXEC]]
- [[role-pur-sr|Role PUR-SR]]
- [[role-pur-mgr|Role PUR-MGR]]
- [[role-plant-head|Role PLANT-HEAD]]
- [[role-stores|Role STORES]]
- [[user-dokafor|Daniel Okafor (DOKAFOR)]]
- [[user-hweber|Henrik Weber (HWEBER)]]
- [[user-svc-agent|Integration service account (SVC_AGENT)]]

## References

[^r2]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, §1. Purpose
[^r1]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, Version history
[^r3]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, §2. How limits are measured
[^r6]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, §3. The limits
[^r10]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 2, §4. Who may not approve
[^r11]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 2, §4. Who may not approve
[^r14]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §5. Approval limits
[^r4]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, §2. How limits are measured
[^r5]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, §2. How limits are measured
[^r7]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, §3. The limits
[^r8]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, §3. The limits
[^r9]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, §3. The limits
[^r16]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 3, §5. Procedure
[^r12]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 2, §4. Who may not approve
[^r15]: 02_procedures/SOP-IT-001 User Access Request v1.6.pdf, p. 3, §5. Procedure
[^r13]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 2, §6. Review
[^r24]: 01_policies/old/Approval_Matrix_v2.0_2024.docx, Practical tips
[^r17]: 01_policies/old/Approval_Matrix_v2.0_2024.docx, Practical tips
