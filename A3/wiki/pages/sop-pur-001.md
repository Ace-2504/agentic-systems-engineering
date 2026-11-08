---
title: "SOP-PUR-001 Supplier Onboarding"
type: "procedure"
slug: "sop-pur-001"
summary: "Procedure for onboarding new vendors in Ledgerline, covering duplicate checks, documentation, UN 38.3 battery certification, and bank call-back verification."
audience: "staff"
status: "mixed"
sources: ["02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf", "02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf", "02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx", "02_procedures/old/SOP-PUR-001 Supplier onboarding v2.0 (2021).docx"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-PUR-001 |
| Title | Supplier Onboarding |
| Version | 3.1 |
| Effective | 2026-09-01 |
| Owner | Luis Moreno |
| Approver | Daniel Okafor |
| Status | current |

SOP-PUR-001 defines the mandatory procedure for adding new suppliers to the Ledgerline system before any purchasing commitments or orders may be placed [^r1][^r14]. Effective 2026-09-01 under version 3.1, the process is owned by senior buyer [[user-lmoreno|Luis Moreno]] and approved by purchase manager [[user-dokafor|Daniel Okafor]] [^r1]. Receipt of a quotation from an unlisted vendor triggers this onboarding flow, requiring thorough duplicate verification, mandatory documentation collection, and finance verification [^r2][^r4][^r14]. For suppliers of [[items-bat|lithium-cell parts]], stringent UN 38.3 test validation and senior buyer sign-off are required prior to raising purchase orders [^r5][^r9].

Code: SOP-PUR-001
Owner: Luis Moreno
Approver: Daniel Okafor
Version: 3.1
Effective date: 2026-09-01
Status: current

## Steps

1. **Duplicate Search**: Search the supplier master on [[screen-pur-sup-03|PUR-SUP-03]] using one short, distinctive word of the supplier's name, then by city, and then by VAT number, attaching the printed result to the file [^r2][^r15].
2. **Raise Request**: Submit an onboarding request on form NBC-F-112 (Supplier Onboarding Request), attaching at least one written quotation and the formal justification detailing why existing suppliers cannot meet the requirement [^r3].
3. **Collect Documentation**: Gather all required vendor documents under [[pol-sup-003|POL-SUP-003]] §3.2, consisting of the VAT registration certificate, company registration number, bank letter, proof of insurance, and the signed Supplier Code of Conduct [^r4][^r17].
4. **Verify UN 38.3 Compliance**: For suppliers providing [[items-bat|lithium-cell parts]], verify that the UN 38.3 test report and test summary were issued within the preceding 12 months and carry a valid-to date at least 60 days beyond the planned date of the initial purchase order pursuant to [[amd-sup-2026-02|AMD-SUP-2026-02]] [^r5][^r18].
5. **Purchase Manager Authorization**: Obtain formal sign-off from the purchase manager via signature in box 7 of form NBC-F-112 before creating any records in the system [^r6][^r16].
6. **Create Ledgerline Record**: Enter the supplier on [[screen-pur-sup-01|PUR-SUP-01]] using service `sup_create` by supplying the name, city, two-letter country code, VAT number, and payment terms until Ledgerline confirms `SUPPLIER <code> CREATED` [^r7].
7. **Upload Certificates**: For lithium-cell parts vendors, navigate to the Certificates tab and upload the certificate using service `sup_cert_upload` under certificate type `UN38.3`, entering the document reference, valid-to date, and attaching the test report until `CERT SAVED` is confirmed [^r8][^r19].
8. **Checklist Review**: The senior buyer conducts an inspection of the uploaded UN 38.3 documentation against the test report and initials onboarding checklist form NBC-F-113 [^r9].
9. **Bank Verification**: Accounts payable validates supplier bank credentials under [[sop-ap-004|SOP-AP-004]] through a telephone call-back using a number sourced from the supplier's official letterhead or website, explicitly avoiding numbers from the bank letter or email correspondence [^r10][^r20].
10. **Rate Contract Setup**: The purchase manager's office enters the rate contract in accordance with [[sop-pur-004|SOP-PUR-004]] so that the Fetch function on [[screen-pur-po-01|PUR-PO-01]] can successfully retrieve agreed contract pricing [^r11][^r21].

## Forms and screens

* **NBC-F-112 (Supplier Onboarding Request)**: Used to submit the onboarding business justification, quotation, and obtain the purchase manager's approval in box 7 [^r3][^r6].
* **NBC-F-113 (Supplier Onboarding Checklist)**: Version 2.1 checklist (effective 2026-09-01, owned by the Purchase department, status CURRENT) covering duplicate search verification, document gathering, UN 38.3 reviews, bank verification, and rate contract entry [^r15][^r16][^r17][^r18][^r19][^r20][^r21][^r22].
* **[[screen-pur-sup-03|PUR-SUP-03]] (Supplier Enquiry)**: Screen used to run duplicate checks across supplier names, cities, and VAT numbers [^r2][^r15].
* **[[screen-pur-sup-01|PUR-SUP-01]] (Supplier Master Create)**: Screen executed with service `sup_create` to register standard supplier master records and service `sup_cert_upload` to store UN 38.3 certificates [^r7][^r8].
* **[[screen-pur-po-01|PUR-PO-01]] (Purchase Order Entry)**: Screen where purchase orders are raised against active suppliers with rate contracts [^r11].

## Checks and approvals

* **Purchase Manager Approval**: Box 7 of form NBC-F-112 must be signed by the purchase manager ([[role-pur-mgr|role PUR-MGR]]) before the supplier record is created in Ledgerline [^r6][^r16].
* **Lithium-Cell Part Ordering Control**: Ledgerline automatically marks new suppliers as ACTIVE upon creation, and parameter `PUR.CERT_CHK` is configured to `N` [^r13]. Consequently, no order for a lithium-cell part may be placed until the senior buyer ([[role-pur-sr|role PUR-SR]]) inspects the uploaded UN 38.3 certificate against the test report and initials checklist NBC-F-113, which acts as the sole operating control [^r9][^r13].
* **Bank Detail Validation**: Accounts payable must complete a mandatory telephone call-back using numbers taken strictly from vendor letterhead or public websites to verify banking details [^r10][^r20].
* **SLA Timelines**: Standard supplier onboarding takes five working days following the submission of a complete file, whereas onboarding for lithium-cell part suppliers requires at least ten working days to handle laboratory inquiries [^r12].

## Versions and conflicts

* **Duplicate search screen**: Today's rule requires searching the supplier master on [[screen-pur-sup-03|PUR-SUP-03]] by name, city, and VAT number [^r2][^r15]. Under superseded SOP-PUR-001 v2.0 (effective 2021-02-01), searches were performed on screen [[screen-supp-enq|SUPP-ENQ]] via Ledgerline 6 menu Masters > Vendors [^r23] (superseded).
* **Creation screen**: Today's rule specifies creating records on [[screen-pur-sup-01|PUR-SUP-01]] using service `sup_create` [^r7]. Superseded SOP-PUR-001 v2.0 directed staff to create records on screen [[screen-supp-ent|SUPP-ENT]] [^r25] (superseded).
* **Battery certificate timing**: Today's rule requires lithium-cell suppliers to present a UN 38.3 report issued within the last 12 months and valid for at least 60 days past the planned first purchase order prior to order creation [^r5][^r9][^r18]. Superseded SOP-PUR-001 v2.0 permitted battery pack suppliers to provide their UN 38.3 report within three months following the first order [^r25] (superseded).
* **Processing time**: Today's rule mandates five working days for standard onboarding and at least ten working days for lithium-cell suppliers [^r12]. Superseded SOP-PUR-001 v2.0 allowed three working days for the onboarding process [^r26] (superseded).

## See also

* [[pol-sup-003|POL-SUP-003 Supplier Policy]]
* [[amd-sup-2026-02|AMD-SUP-2026-02 Amendment 2 to the Supplier Policy]]
* [[sop-pur-004|SOP-PUR-004 Rate Contract Maintenance]]
* [[sop-pur-005|SOP-PUR-005 Certificate Renewal (UN 38.3)]]
* [[sop-pur-006|SOP-PUR-006 Quotations and Supplier Selection]]
* [[sop-ap-004|SOP-AP-004 Supplier Bank Detail Changes]]
* [[screen-pur-sup-01|screen-pur-sup-01]]
* [[screen-pur-sup-03|screen-pur-sup-03]]
* [[screen-pur-po-01|screen-pur-po-01]]
* [[items-bat|items-bat]]
* [[role-pur-mgr|role-pur-mgr]]
* [[role-pur-sr|role-pur-sr]]
* [[user-dokafor|user-dokafor]]
* [[user-lmoreno|user-lmoreno]]

## References

[^r1]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 1, Supplier Onboarding
[^r14]: 02_procedures/SOP-PUR-006 Quotations and Supplier Selection v1.0.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r9]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r15]: 02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx, Supplier Onboarding Checklist (NBC-F-113)
[^r3]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r17]: 02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx, Supplier Onboarding Checklist (NBC-F-113)
[^r18]: 02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx, Supplier Onboarding Checklist (NBC-F-113)
[^r6]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r16]: 02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx, Supplier Onboarding Checklist (NBC-F-113)
[^r7]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r8]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r19]: 02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx, Supplier Onboarding Checklist (NBC-F-113)
[^r10]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r20]: 02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx, Supplier Onboarding Checklist (NBC-F-113)
[^r11]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r21]: 02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx, Supplier Onboarding Checklist (NBC-F-113)
[^r22]: 02_procedures/forms/Final_FINAL_onboarding checklist NBC-F-113.docx, Supplier Onboarding Checklist (NBC-F-113)
[^r13]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 5, §6. Timing and system checks
[^r12]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 5, §6. Timing and system checks
[^r23]: 02_procedures/old/SOP-PUR-001 Supplier onboarding v2.0 (2021).docx, §5. Procedure
[^r25]: 02_procedures/old/SOP-PUR-001 Supplier onboarding v2.0 (2021).docx, §5. Procedure
[^r26]: 02_procedures/old/SOP-PUR-001 Supplier onboarding v2.0 (2021).docx, §5. Procedure
