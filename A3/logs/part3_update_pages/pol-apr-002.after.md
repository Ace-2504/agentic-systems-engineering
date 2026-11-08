---
title: "POL-APR-002 Approval Matrix for Purchasing"
type: "policy"
slug: "pol-apr-002"
summary: "Purchasing approval matrix establishing gross monetary limits per document, prohibition of self-approval, and escalation rules up to the Managing Director."
audience: "staff"
status: "mixed"
sources: ["01_policies/POL-APR-002 Approval Matrix v3.0.pdf", "01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf", "01_policies/old/Approval_Matrix_v2.0_2024.docx", "01_policies/old/purchase_policy_v3_2019.docx", "02_procedures/SOP-IT-001 User Access Request v1.6.pdf", "02_procedures/SOP-IT-002 Service Account Management v1.0.pdf", "01_policies/POL-APR-002 Approval Matrix v3.1.pdf"]
created: "2026-11-08"
updated: "2026-11-08"
---

| | |
|---|---|
| Document code | POL-APR-002 |
| Title | Approval Matrix for Purchasing |
| Owner | Plant head's office |
| Approver | Henrik Weber |
| Effective date | 2026-10-26 |
| Version | 3.1 |
| Status | current |

| | |
|---|---|
| Document code | POL-APR-002 |
| Title | Approval Matrix for Purchasing |
| Owner | Plant head's office |
| Approver | Henrik Weber |
| Effective date | 2026-10-26 |
| Version | 3.1 |
| Status | current |

POL-APR-002 defines the financial approval matrix for purchase requests and purchase orders across Northbridge Cycles, serving as the matrix referenced in [[pol-pur-001|POL-PUR-001]] §5.2 [^r2]. Version 3.1 is effective from 2026-10-26, owned by the Plant head's office, approved by Plant Head [[user-hweber|Henrik Weber]], and replaces version 3.0 [^r26]. It establishes per-document gross monetary limits for each purchasing role, regulates delegation, and strictly prohibits self-approval and service account authorisation in Ledgerline [^r27][^r30][^r34][^r35].

## Clauses

### §1. Purpose
POL-APR-002 establishes who may approve a purchase request or purchase order and up to what value, serving as the matrix referenced in Purchase Policy §5.2 [^r2]. Version 3.1 took effect on 2026-10-26 under the ownership of the Plant head's office, with approval from Plant Head [[user-hweber|Henrik Weber]], replacing version 3.0 [^r26].

### §2. How limits are measured
Every approval limit is measured on the gross value of one document including VAT, with freight and packing charged on the order counting towards the gross value [^r14][^r27]. Approval limits apply per document rather than per day or per supplier [^r28]. Splitting requirements to stay inside an approval limit is prohibited, and orders for the same item from the same supplier raised within seven days of each other are treated as one requirement [^r29].

### §3. The limits
The gross approval limits including VAT are £300,000 for [[role-pur-exec|PUR-EXEC]] (Purchase executive), £500,000 for [[role-pur-sr|PUR-SR]] (Senior buyer), £1,000,000 for [[role-pur-mgr|PUR-MGR]] (Purchase manager), and £5,000,000 for [[role-plant-head|PLANT-HEAD]] (Plant head), while [[role-stores|STORES]] has no approval authority [^r30]. A document within the raiser's own approval limit is approved upon submission, and Ledgerline records the raiser as the approver [^r31]. A document above the raiser's limit routes to their manager, and escalates up the reporting line until reaching the first person whose limit covers it [^r32]. Orders above £5,000,000 trigger Ledgerline error [[err-apr-0009|ERR-APR-0009]] and require the Managing Director's written approval outside Ledgerline before being recorded by the plant head's office [^r33].

### §4. Who may not approve
Nobody may approve a document they raised under Purchase Policy §5.3, and Ledgerline blocks such attempts with [[err-apr-0003|ERR-APR-0003]] [^r10][^r34]. Integration and service accounts holding role SYS-ADMIN (such as [[user-svc-agent|SVC_AGENT]]) possess no approval authority under POL-APR-002, and any document approved by them is deemed unapproved and must be cancelled or re-approved by a person [^r16][^r35]. An approver on leave may delegate authority in writing to an individual holding the same or a higher role for a stated period, but delegation to a lower role is prohibited [^r36].

### §5. Procedure and access alignment
User approval limits assigned during Ledgerline access setup must strictly match the approval matrix in POL-APR-002 for that job title [^r15].

### §6. Review
The plant head reviews POL-APR-002 annually every April and whenever organizational changes occur [^r37].

## Who it applies to
This policy applies to all personnel raising or approving purchasing documents, including roles [[role-pur-exec|PUR-EXEC]], [[role-pur-sr|PUR-SR]], [[role-pur-mgr|PUR-MGR]], [[role-plant-head|PLANT-HEAD]], and [[role-stores|STORES]], as well as IT administrators assigning user roles and managing service accounts [^r15][^r16][^r30][^r35]. Plant Head [[user-hweber|Henrik Weber]] governs its approval and annual review [^r26][^r37].

## Versions and conflicts
- Gross approval limits | Gross limits are £300,000 for PUR-EXEC, £500,000 for PUR-SR, £1,000,000 for PUR-MGR, and £5,000,000 for PLANT-HEAD [^r30] | Under superseded POL-APR-002 v3.0 (2026-04-01), the limit for PUR-EXEC was £250,000 [^r6], and under superseded v2.0 (2024-04-01) the limits were £200,000 for PUR-EXEC, £400,000 for PUR-SR, £750,000 for PUR-MGR, and £5,000,000 for PLANT-HEAD [^r24] | POL-APR-002 v3.1, p. 1, §3; POL-APR-002 v3.0, p. 1, §3; Approval_Matrix_v2.0_2024.docx, Practical tips | superseded
- Ownership | Version 3.1 (2026-10-26) is owned by the Plant head's office [^r26], matching superseded v2.0 [^r17] | Superseded version 3.0 (2026-04-01) listed author D. Okafor [^r1] | POL-APR-002 v3.1, p. 1, §1; POL-APR-002 v3.0, p. 1, Version history; Approval_Matrix_v2.0_2024.docx, Practical tips | superseded

## See also
- [[pol-pur-001|POL-PUR-001 Purchase Policy]]
- [[sop-it-001|SOP-IT-001 User Access Request]]
- [[sop-it-002|SOP-IT-002 Service Account Management]]
- [[err-apr-0003|ERR-APR-0003]]
- [[err-apr-0009|ERR-APR-0009]]
- [[role-plant-head|Role PLANT-HEAD]]
- [[role-pur-exec|Role PUR-EXEC]]
- [[role-pur-mgr|Role PUR-MGR]]
- [[role-pur-sr|Role PUR-SR]]
- [[role-stores|Role STORES]]
- [[user-dokafor|Daniel Okafor (DOKAFOR)]]
- [[user-hweber|Henrik Weber (HWEBER)]]
- [[user-svc-agent|Integration service account (SVC_AGENT)]]

## References

[^r2]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, §1. Purpose
[^r26]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 1, §1. Purpose
[^r27]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 1, §2. How limits are measured
[^r30]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 1, §3. The limits
[^r34]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 2, §4. Who may not approve
[^r35]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 2, §4. Who may not approve
[^r14]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §5. Approval limits
[^r28]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 1, §2. How limits are measured
[^r29]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 1, §2. How limits are measured
[^r31]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 1, §3. The limits
[^r32]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 1, §3. The limits
[^r33]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 1, §3. The limits
[^r10]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 2, §4. Who may not approve
[^r16]: 02_procedures/SOP-IT-002 Service Account Management v1.0.pdf, p. 3, §5. Procedure
[^r36]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 2, §4. Who may not approve
[^r15]: 02_procedures/SOP-IT-001 User Access Request v1.6.pdf, p. 3, §5. Procedure
[^r37]: 01_policies/POL-APR-002 Approval Matrix v3.1.pdf, p. 2, §6. Review
[^r6]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, §3. The limits
[^r24]: 01_policies/old/Approval_Matrix_v2.0_2024.docx, Practical tips
[^r17]: 01_policies/old/Approval_Matrix_v2.0_2024.docx, Practical tips
[^r1]: 01_policies/POL-APR-002 Approval Matrix v3.0.pdf, p. 1, Version history
