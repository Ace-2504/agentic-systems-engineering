---
title: "POL-SUP-003 Supplier Policy"
type: "policy"
slug: "pol-sup-003"
summary: "Policy governing Ledgerline supplier master onboarding, documentation, duplicate checks, blocking rules, and amended UN 38.3 lithium battery certification standards."
audience: "staff"
status: "mixed"
sources: ["01_policies/AMD-SUP-2026-02 Amendment 2 Supplier Policy.pdf", "01_policies/POL-QUA-005 Quality Policy v3.0.pdf", "01_policies/POL-SUP-003 Supplier Policy v2.3 (1).pdf", "01_policies/POL-SUP-003 Supplier Policy v2.3.pdf", "01_policies/old/Supplier_Policy_v2.2.docx", "02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | POL-SUP-003 |
| Owner | Purchase department |
| Approver | Daniel Okafor |
| Version | 2.3 (as amended by AMD-SUP-2026-02) |
| Effective date | 2026-04-01 (amended 2026-09-01) |
| Classification | INTERNAL |
| Status | current |

POL-SUP-003 establishes the rules for entering suppliers into the Ledgerline supplier master, duplicate prevention, blocking procedures, and ongoing compliance requirements [^r5]. Effective 1 September 2026 under amendment [[amd-sup-2026-02|AMD-SUP-2026-02]], lithium-cell suppliers must meet stricter certificate validity windows before purchase orders may be placed [^r1]. The policy applies across both Manchester and Leeds operating locations [^r6].

### 1. Purpose
POL-SUP-003 sits under [[pol-pur-001|Purchase Policy POL-PUR-001]] §6 and establishes how suppliers enter the Ledgerline supplier master, required documentation, blocking rules, and duplicate registration prevention [^r5]. The policy is owned by the Purchase department, was approved by Purchase Manager [[user-dokafor|Daniel Okafor]], and is classified as INTERNAL [^r4].

### 2. Scope
The policy covers every supplier of materials, components, packing, and services to Manchester plant NBC-MAN-01 and Leeds unit NBC-LDS-01, excluding one-time cash purchases under £5,000 from petty cash [^r6].

### 3. Onboarding a new supplier
A new supplier proposal requires at least one written quotation and an operational justification detailing why an existing supplier cannot meet the need [^r7]. Before supplier creation, the proposer must collect the VAT registration certificate (VAT number), company registration number, bank letter confirming the account, proof of insurance, and signed Supplier Code of Conduct [^r8]. The proposer must search the supplier master in Ledgerline screen [[screen-pur-sup-03|PUR-SUP-03]] by name, city, and VAT number, attaching the search result to the onboarding file [^r9]. The purchase manager must approve the onboarding file before a supplier may be created in Ledgerline [^r10]. A newly created supplier is ACTIVE from creation, but orders may not be placed until all onboarding documents and any required lithium-cell certificates are on file [^r11]. Supplier onboarding normally takes five working days from a complete file, and urgency does not permit skipping any onboarding step [^r12].

### 4. UN 38.3 certificates
Suppliers of lithium-cell parts (battery packs, hub motors, chargers, or items marked lithium-cell in the item master) must hold a UN 38.3 test report from an accredited laboratory such as ISO/IEC 17025 [^r13]. The UN 38.3 certificate is uploaded in Ledgerline against the supplier under certificate type UN38.3 with its document reference and valid-to date, and must be verified by the senior buyer before the first order [^r14]. Under amendment [[amd-sup-2026-02|AMD-SUP-2026-02]] effective 1 September 2026, §4.4 is replaced so that a UN 38.3 certificate is accepted only if issued within the last 12 months and valid for at least 60 days after the purchase order date [^r1]. Any certificate satisfying the former rule is treated as non-existent for new orders placed on or after 1 September 2026 [^r2]. A fresh test report is required if the supplier changes part design, cells, or cell chemistry [^r15]. Ledgerline does not automatically block purchase orders to suppliers lacking a certificate, so the order raiser and approver must verify certificates manually [^r16].

### 5. Blocking and unblocking
A supplier is BLOCKED in Ledgerline if replaced by a new code, if it fails two consecutive quality audits, or upon Finance request for unpaid debit notes [^r17]. A blocked supplier retains its code and history, but Ledgerline refuses new purchase orders with error [[err-sup-0031|ERR-SUP-0031]] [^r18]. Only the purchase manager may request IT in writing to unblock a supplier, specifying the reason [^r19]. When a supplier is issued a new code, the old code is blocked and renamed with suffix '(old code, do not use)' [^r20].

### 6. Duplicate suppliers
Each legal entity must have exactly one active code, and two master records sharing the same VAT number are considered the same supplier [^r21]. Ledgerline blocks the creation of a second supplier record having an existing VAT number with error [[err-sup-0118|ERR-SUP-0118]] [^r22]. Name variants close to an existing supplier in the same city must be treated as that supplier until proven otherwise, whereas near-matches in different cities or with different VAT numbers are distinct suppliers [^r26]. An accidental duplicate supplier record must be reported to the purchase manager on the same day, blocked, and its open documents transferred to the correct code [^r23].

### 7. Rate contracts
Regular suppliers of regular items have Ledgerline rate contracts with valid-from and valid-to dates, which are reviewed semi-annually in March and September [^r24][^r27].

### 8. Supplier performance
The senior buyer conducts quarterly supplier performance reviews assessing on-time delivery, rejection rate, and price [^r28]. Suppliers with a rejection rate exceeding 2% across two consecutive quarters are placed on watch in accordance with POL-SUP-003 §8.2 and receive a Quality visit [^r3][^r28].

## Who it applies to
This policy applies to all personnel purchasing goods or services for Manchester plant NBC-MAN-01 and Leeds unit NBC-LDS-01, including purchase proposers, senior buyers, purchase managers, and approving authorities [^r6][^r7][^r10][^r14][^r16].

## Versions and conflicts
- **UN 38.3 certificate acceptance window** | Today's rule: A UN 38.3 certificate is accepted only if issued within the last 12 months and valid for at least 60 days after the purchase order date [^r1]. | Older rule: The certificate was valid if issued within the last 24 months and its valid-to date had not passed [^r25]. | Replaced by AMD-SUP-2026-02 effective 2026-09-01; former certificates are treated as non-existent for orders on or after 1 September 2026 [^r1][^r2]. | `superseded`

## See also
- [[amd-sup-2026-02|AMD-SUP-2026-02 Amendment 2 to the Supplier Policy]]
- [[err-sup-0031|ERR-SUP-0031 Supplier Blocked]]
- [[err-sup-0118|ERR-SUP-0118 Duplicate VAT Number]]
- [[pol-pur-001|POL-PUR-001 Purchase Policy]]
- [[screen-pur-sup-03|PUR-SUP-03 Supplier Enquiry]]
- [[user-dokafor|Daniel Okafor (DOKAFOR)]]

## References

[^r5]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 1, §1. Purpose
[^r1]: 01_policies/AMD-SUP-2026-02 Amendment 2 Supplier Policy.pdf, p. 1, §1. What changes
[^r6]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 1, §2. Scope
[^r4]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 1, Supplier Policy
[^r7]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 1, §3. Onboarding a new supplier
[^r8]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 1, §3. Onboarding a new supplier
[^r9]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 1, §3. Onboarding a new supplier
[^r10]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 1, §3. Onboarding a new supplier
[^r11]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 1, §3. Onboarding a new supplier
[^r12]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 1, §3. Onboarding a new supplier
[^r13]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §4. UN 38.3 certificates
[^r14]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §4. UN 38.3 certificates
[^r2]: 01_policies/AMD-SUP-2026-02 Amendment 2 Supplier Policy.pdf, p. 1, §1. What changes
[^r15]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §4. UN 38.3 certificates
[^r16]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §4. UN 38.3 certificates
[^r17]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §5. Blocking and unblocking
[^r18]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §5. Blocking and unblocking
[^r19]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §5. Blocking and unblocking
[^r20]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §5. Blocking and unblocking
[^r21]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §6. Duplicate suppliers
[^r22]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §6. Duplicate suppliers
[^r26]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §6. Duplicate suppliers
[^r23]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §6. Duplicate suppliers
[^r24]: 02_procedures/SOP-PUR-004 Rate Contract Maintenance v2.0.pdf, p. 3, §5. Procedure
[^r27]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 3, §7. Rate contracts
[^r28]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 3, §8. Supplier performance
[^r3]: 01_policies/POL-QUA-005 Quality Policy v3.0.pdf, p. 3, §4. Supplier quality
[^r25]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §4. UN 38.3 certificates
