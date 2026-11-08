---
title: "SOP-AP-004 Supplier Bank Detail Changes"
type: "procedure"
slug: "sop-ap-004"
summary: "Standard operating procedure for verifying and updating supplier bank details to prevent fraud, requiring two-person call-backs and dual-signatory approval."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-AP-004 Supplier Bank Detail Changes v2.0.pdf", "02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Document code | SOP-AP-004 |
| Title | Supplier Bank Detail Changes |
| Owner | Marta Kowalski (AP manager) |
| Approver | Grace Whitaker (Financial controller) |
| Version | 2.0 |
| Effective date | 2025-10-01 |
| Status | current |

SOP-AP-004 defines the mandatory verification procedure for processing changes to supplier bank details across Northbridge Cycles[^r1]. Version 2.0 has been in effect since 2025-10-01 and is owned by AP manager [[user-mkowalski|Marta Kowalski]] with approval from financial controller [[user-gwhitaker|Grace Whitaker]][^r1]. Today, 26 October 2026, it ensures that all modifications to creditor banking information undergo independent call-back confirmation and strict segregation of duties to prevent fraudulent impersonation[^r2][^r3][^r5].

## Steps

1. **Receipt and logging of request**: A change request is received, but it must never be accepted by e-mail alone due to the risk of fraudulent impersonation[^r2]. A purchase ledger clerk logs the request, but this clerk is strictly prohibited from confirming the change with the supplier[^r5].
2. **Independent telephone verification**: Accounts payable staff verify the bank detail changes by calling the supplier back using a telephone number obtained independently from a letterhead, website, or the supplier master, and never from the change request itself[^r3]. Two people from AP must participate in the call-back[^r3]. If the contact on the call cannot answer routine questions regarding recent orders, purchase order references, or previous banking details, staff must terminate the call immediately without disclosing information from the screen[^r7].
3. **Recording and payment hold**: The verification call is logged in the system, initiating an automated hold on disbursements[^r4].
4. **Senior review and ERP update**: Once independent verification notes are recorded, a senior finance officer reviews the documentation before unlocking the creditor record in Ledgerline ERP to enter the revised sort code and account number[^r6].
5. **Signatory release**: A second authorised signatory performs a final review of the record to release the hold[^r6].
6. **Filing and archiving**: The complete physical verification pack—comprising the original notice, callback record sheet, and signed change authorisation form—is filed in the supplier amendment binder in the Manchester finance office[^r8]. The Leeds office posts physical paperwork to Manchester and keeps a scanned counter-copy[^r8].

## Forms and screens

* Form NBC-F-113 (Supplier Onboarding Checklist) mandates that Accounts Payable verify bank details by call-back under SOP-AP-004[^r9].
* Screen [[screen-ap-bnk-06|AP-BNK-06]] is used to record the verification call using service `bnk_verify`[^r4].
* Warning [[w-bnk-120|W-BNK-120]] holds all disbursements to the supplier while the verification process is underway on screen AP-BNK-06[^r4].
* A callback record sheet and signed change authorisation form are completed and archived in the physical verification pack[^r8].

## Checks and approvals

* **Segregation of duties**: The purchase ledger clerk who logs the bank change request must not be the individual who confirms the change with the supplier[^r5].
* **Two-person call-back**: Two staff members from AP must take part in the verification phone call[^r3].
* **Pre-update verification**: A senior finance officer must inspect the verification notes before unlocking the creditor record in Ledgerline ERP to enter the new sort code and account number[^r6].
* **Dual-signatory release**: Release of the payment hold following the detail update requires review by a second authorised signatory[^r6].

## See also

* [[screen-ap-bnk-06|AP-BNK-06 Supplier Bank Details Entry]]
* [[user-gwhitaker|Grace Whitaker (GWHITAKER)]]
* [[user-mkowalski|Marta Kowalski (MKOWALSKI)]]
* [[sop-pur-001|SOP-PUR-001 Supplier Onboarding]]
* [[w-bnk-120|W-BNK-120 Supplier Bank Details Hold]]

## References

[^r1]: 02_procedures/SOP-AP-004 Supplier Bank Detail Changes v2.0.pdf, p. 1, Supplier Bank Detail Changes
[^r2]: 02_procedures/SOP-AP-004 Supplier Bank Detail Changes v2.0.pdf, p. 3, §5. Procedure
[^r3]: 02_procedures/SOP-AP-004 Supplier Bank Detail Changes v2.0.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-AP-004 Supplier Bank Detail Changes v2.0.pdf, p. 2, §3. Responsibilities
[^r7]: 02_procedures/SOP-AP-004 Supplier Bank Detail Changes v2.0.pdf, p. 4, What to do when something does not look right
[^r4]: 02_procedures/SOP-AP-004 Supplier Bank Detail Changes v2.0.pdf, p. 3, §5. Procedure
[^r6]: 02_procedures/SOP-AP-004 Supplier Bank Detail Changes v2.0.pdf, p. 2, §3. Responsibilities
[^r8]: 02_procedures/SOP-AP-004 Supplier Bank Detail Changes v2.0.pdf, p. 5, Practical operation
[^r9]: 02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx, Supplier Onboarding Checklist (NBC-F-113)
