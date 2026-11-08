---
title: "SOP-PUR-005 Certificate Renewal (UN 38.3)"
type: "procedure"
slug: "sop-pur-005"
summary: "Standard operating procedure for tracking, requesting, validating, and recording renewed UN 38.3 transport test summaries for battery items."
audience: "staff"
status: "current"
sources: ["01_policies/AMD-SUP-2026-02 Amendment 2 Supplier Policy.pdf", "02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf", "02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf", "02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| code | SOP-PUR-005 |
| owner | [[user-lmoreno|Luis Moreno]] (senior buyer) |
| approved_by | [[user-dokafor|Daniel Okafor]] (purchase manager) |
| version | 1.1 |
| effective | 2026-09-01 |
| status | current |

SOP-PUR-005 governs the renewal and verification of UN 38.3 transport test summaries for lithium-cell items such as [[items-bat|BAT-* items]][^r4][^r16]. As of Monday 26 October 2026, UN 38.3 certificates must have been issued within the preceding 12 months and maintain validity for at least 60 days following order placement under [[amd-sup-2026-02]][^r2]. Without an active UN 38.3 test summary confirming compliance with transport testing requirements, battery stock cannot legally be moved by freight carriers, stored at the Manchester works, or transferred to the Leeds unit[^r4]. Any internal design revision to battery management firmware or casing seals invalidates the previous certificate and requires fresh certification[^r7].

## Steps

1. On the first working day of each month, the [[role-pur-sr|senior buyer]] runs the certificate-expiry report (job JOB-PUR-022; manual reference MAN-PUR-72 §22.6) using a 90-day window[^r1][^r10].
2. For every UN 38.3 certificate expiring within 90 days, purchasing writes to the supplier using letter template NBC-L-07 to request a new test report[^r1][^r11].
3. If no new report arrives 60 days before expiry, purchasing issues a second reminder and notifies the [[role-pur-mgr|purchase manager]]; under [[amd-sup-2026-02]], no new purchase order may be raised once fewer than 60 days remain[^r12].
4. When a renewed certificate is received, purchasing verifies that the transport test summary includes test laboratory details and the manufacturer's authorised signature, rather than requiring the full factory test report[^r6].
5. Purchasing uploads the certificate in Ledgerline ERP as a new row on the supplier compliance sub-screen rather than overwriting historical rows[^r14].
6. Quality Assurance cross-checks model designations, cell combinations, and ratings against engineering drawings and logs formal sign-off in the system[^r8].
7. Hard copies of renewed test summaries are printed and filed into dangerous goods binders in dispatch offices at Manchester and Leeds, while obsolete certificates are marked as superseded and archived[^r15].
8. If a certificate expires without a valid replacement, purchasing e-mails all buyers with the exact subject 'CERT EXPIRED - DO NOT ORDER' together with the supplier's name and code[^r13].

## Forms and screens

* NBC-L-07: Purchasing letter template used to request updated test reports from suppliers 90 days prior to certificate expiry[^r11].
* Final_FINAL_onboarding checklist NBC-F-113.docx (NBC-F-113): [[sop-pur-001|Supplier Onboarding Checklist]] where check 4 verifies the UN 38.3 report was issued within 12 months and is valid to at least 60 days after the first order, and check 5 records the upload under document type UN38.3 with its document reference and valid-to date[^r17][^r18].
* Ledgerline ERP supplier compliance sub-screen: Screen where renewed certificates are uploaded as new rows alongside existing historical records[^r14].
* JOB-PUR-022: Certificate-expiry batch report job run monthly with a 90-day parameter window[^r1][^r10].

## Checks and approvals

* Goods receiving staff at Manchester verify that incoming battery deliveries cite the active certificate before signing carrier consignment notes or moving crates into stores[^r5].
* Goods Inwards staff place consignments into quarantine immediately if an active UN 38.3 certificate is missing or lapsed at receipt in Manchester or Leeds[^r9].
* Lithium-cell quotation comparisons under [[sop-pur-006]] require a verified UN 38.3 test certificate attached to the supplier master record or entered against the quotation entry in Ledgerline ERP[^r16].
* Quality Assurance performs technical sign-off by verifying model designations, cell combinations, and ratings against engineering drawings[^r8].
* The procedure is owned by Senior Buyer [[user-lmoreno|Luis Moreno]] and approved by Purchase Manager [[user-dokafor|Daniel Okafor]][^r3].

## See also

* [[amd-sup-2026-02|AMD-SUP-2026-02 Amendment 2 to the Supplier Policy]]
* [[items-bat|BAT-* items]]
* [[role-pur-mgr|Role PUR-MGR]]
* [[role-pur-sr|Role PUR-SR]]
* [[sop-pur-001|SOP-PUR-001 Supplier Onboarding]]
* [[sop-pur-006|SOP-PUR-006 Quotations and Supplier Selection]]
* [[user-dokafor|Daniel Okafor (DOKAFOR)]]
* [[user-lmoreno|Luis Moreno (LMORENO)]]

## References

[^r4]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 1, §1. Purpose
[^r16]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 4, What to check on the screen
[^r2]: 01_policies/AMD-SUP-2026-02 Amendment 2 Supplier Policy.pdf, p. 1, §1. What changes
[^r7]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 1, §1. Purpose
[^r1]: 01_policies/AMD-SUP-2026-02 Amendment 2 Supplier Policy.pdf, p. 1, §3. What purchase staff must do
[^r10]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 3, §5. Procedure
[^r11]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 3, §5. Procedure
[^r12]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 3, §5. Procedure
[^r6]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 1, §1. Purpose
[^r14]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 3, §5. Procedure
[^r8]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 2, §3. Responsibilities
[^r15]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 4, §6. Records
[^r13]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 3, §5. Procedure
[^r17]: 02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx, Supplier Onboarding Checklist (NBC-F-113)
[^r18]: 02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx, Supplier Onboarding Checklist (NBC-F-113)
[^r5]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 1, §1. Purpose
[^r9]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 2, §3. Responsibilities
[^r3]: 02_procedures/SOP-PUR-005 Certificate Renewal (UN 38.3) v1.1.pdf, p. 1, Certificate Renewal (UN 38.3)
