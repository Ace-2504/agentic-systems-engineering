---
title: "PUR-SUP-01 Supplier Master Create"
type: "screen"
slug: "screen-pur-sup-01"
summary: "Ledgerline screen used to register and activate new supplier records and upload onboarding certificates after purchase manager approval."
audience: "staff"
status: "mixed"
sources: ["01_policies/POL-SUP-003 Supplier Policy v2.3 (1).pdf", "01_policies/POL-SUP-003 Supplier Policy v2.3.pdf", "01_policies/old/Supplier_Policy_v2.2.docx", "02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| code | PUR-SUP-01 |
| name | Supplier Master Create |
| service | sup_create, sup_cert_upload |
| status | current |
| target entity | supplier records |

Screen PUR-SUP-01 is the Ledgerline interface used to create new supplier records following written onboarding approval from the [[role-pur-mgr|purchase manager]][^r1]. The screen activates the supplier record immediately upon creation[^r2]. It also handles the entry of vendor certificates, such as those required for [[items-bat|BAT-* items]][^r5].

## What it is for
The screen is used to register new vendors in Ledgerline once onboarding documentation has been approved in writing by the [[role-pur-mgr|purchase manager]][^r1]. It executes the underlying service sup_create to create the record and make it active immediately upon entry[^r2][^r4]. In addition, the screen provides a Certificates tab running service sup_cert_upload to capture and store vendor compliance certificates[^r5].

## Fields
* **Name**: Vendor name[^r4].
* **City**: Vendor city[^r4].
* **Country code**: Two-letter country code[^r4].
* **VAT number**: Vendor VAT registration number[^r4].
* **Payment terms**: Agreed supplier payment terms[^r4].
* **Certificate type**: Compliance certificate type, such as UN38.3 on the Certificates tab[^r5].
* **Document reference**: Reference code of the attached certificate[^r5].
* **Valid-to date**: Expiration date for the certificate[^r5].
* **Attached test report**: File attachment containing the test report[^r5].

## Messages
* **SUPPLIER `<code>` CREATED**: Confirmation message displayed when the supplier code is generated upon successful registration[^r4].
* **CERT SAVED**: Status message returned when certificate details and test reports are successfully stored via the Certificates tab[^r5].
* **[[err-sup-0118|ERR-SUP-0118]]**: Error returned when entry is blocked because the entered VAT number is already registered in Ledgerline[^r3].

## Versions and conflicts
* **Duplicate copies**: Today's active supplier creation and VAT checking on PUR-SUP-01 under [[pol-sup-003|POL-SUP-003]] v2.3 exists as a duplicate file copy[^r1][^r2][^r3][^r6][^r7][^r8].
* **Superseded rules**: Supplier creation approval and duplicate VAT blocking under ERR-SUP-0118 are governed by [[pol-sup-003|POL-SUP-003]] v2.3; these replace the earlier version POL-SUP-003 v2.2[^r1][^r3][^r9].

## See also
* [[pol-sup-003|POL-SUP-003 Supplier Policy]]
* [[sop-pur-001|SOP-PUR-001 Supplier Onboarding]]
* [[err-sup-0118|ERR-SUP-0118 Duplicate VAT Number]]
* [[role-pur-mgr|Role PUR-MGR]]
* [[items-bat|BAT-* items]]

## References

[^r1]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 4, Creating the account in Ledgerline
[^r2]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 4, Creating the account in Ledgerline
[^r5]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r3]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 2, §6. Duplicate suppliers
[^r6]: 01_policies/POL-SUP-003 Supplier Policy v2.3 (1).pdf, p. 4, Creating the account in Ledgerline
[^r7]: 01_policies/POL-SUP-003 Supplier Policy v2.3 (1).pdf, p. 4, Creating the account in Ledgerline
[^r8]: 01_policies/POL-SUP-003 Supplier Policy v2.3 (1).pdf, p. 2, §6. Duplicate suppliers
[^r9]: 01_policies/old/Supplier_Policy_v2.2.docx, §3. Onboarding a new supplier
