---
title: "PUR-SUP-03 Supplier Enquiry"
type: "screen"
slug: "screen-pur-sup-03"
summary: "Ledgerline screen used to search the supplier master by company name, city, and VAT registration number prior to supplier onboarding."
audience: "staff"
status: "mixed"
sources: ["01_policies/POL-SUP-003 Supplier Policy v2.3 (1).pdf", "01_policies/POL-SUP-003 Supplier Policy v2.3.pdf", "01_policies/old/Supplier_Policy_v2.2.docx", "02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | PUR-SUP-03 |
| Screen name | Supplier Enquiry |
| System | Ledgerline |
| Purpose | Supplier master search |
| Audience | Staff |
| Status | Current |

Screen PUR-SUP-03 is the Ledgerline enquiry screen used to search the supplier master prior to onboarding a new supplier [^r1][^r3]. Staff use it to check for existing active or dormant records across company name, city, and VAT registration number [^r1][^r2]. Search results must be captured and attached directly to the onboarding file [^r2][^r3].

## What it is for
Screen PUR-SUP-03 is used to search the supplier master across company name, city, and VAT registration number prior to compiling onboarding paperwork [^r1]. Proposers must use this screen to verify that no active or dormant record exists for a prospective vendor [^r1][^r2]. The resulting search output must be printed or captured and attached directly to the onboarding file to prove no duplicate record exists [^r2][^r3].

## Fields
- **Company name**: search by entering one short, distinctive name word [^r1][^r3].
- **City**: search by vendor city [^r1][^r3].
- **VAT registration number**: search by vendor VAT number [^r1][^r3].

## Messages
The screen returns search results matching the query parameters, which must be printed or captured for the file [^r2][^r3].

## Versions and conflicts
- Today's rule: Under [[pol-sup-003|POL-SUP-003]] v2.3 and [[sop-pur-001|SOP-PUR-001]] v3.1, proposers must search across company name (entering one short, distinctive name word), city, and VAT registration number, and attach the captured output directly to the onboarding file [^r1][^r2][^r3].
- Older rule: Under superseded POL-SUP-003 v2.2, screen PUR-SUP-03 was used to search by name, city, and VAT number before submitting a new supplier onboarding file [^r5].
- Sources and dates: POL-SUP-003 v2.3 (2026-04-01), SOP-PUR-001 v3.1 (2026-09-01), and POL-PUR-001 citing superseded POL-SUP-003 v2.2 [^r1][^r2][^r3][^r5].
- Kind: `superseded`, `duplicate`.

## See also
- [[pol-sup-003|POL-SUP-003 Supplier Policy]]
- [[sop-pur-001|SOP-PUR-001 Supplier Onboarding]]
- [[screen-pur-sup-01|PUR-SUP-01 Supplier Master Create]]
- [[err-sup-0118|ERR-SUP-0118 Duplicate VAT Number]]

## References

[^r1]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 3, Checking for duplicate master records
[^r3]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r2]: 01_policies/POL-SUP-003 Supplier Policy v2.3.pdf, p. 1, §3. Onboarding a new supplier
[^r5]: 01_policies/old/Supplier_Policy_v2.2.docx, §3. Onboarding a new supplier
