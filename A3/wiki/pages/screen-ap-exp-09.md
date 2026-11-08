---
title: "AP-EXP-09 Expense Claim Entry"
type: "screen"
slug: "screen-ap-exp-09"
summary: "Ledgerline screen used to generate expense headers and enter line items for out-of-pocket business expense claims within 60 days."
audience: "staff"
status: "mixed"
sources: ["01_policies/POL-TEX-007 Travel and Expenses Policy v2.4.pdf", "01_policies/POL-TEX-007 Travel and Expenses Policy v3.0 (effective 2027-01-01).pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | AP-EXP-09 |
| Screen name | Expense Claim Entry |
| System | Ledgerline ERP |
| Current deadline | 60 days from expense |
| Governing policy | POL-TEX-007 |
| Status | current |

Screen AP-EXP-09 is the Ledgerline ERP screen used to generate expense headers and record individual line items for reimbursement [^r1]. Today, staff must enter claims within 60 days of incurring the expense [^r1]. Once approved by the line manager within the screen, claims automatically transfer to the purchase ledger clerk for payment processing [^r2].

## What it is for
Screen AP-EXP-09 is used to generate expense claim headers and enter individual claim line items detailing business expenses [^r1]. Once a line manager approves a claim in screen AP-EXP-09, the workflow automatically forwards it to the purchase ledger clerk for payment processing [^r2].

## Fields
- **Business purpose**: Description of the business purpose for each individual line item [^r1].
- **Cost centre**: The internal department or cost centre allocation for the line item [^r1].
- **Ledger allocation / nominal headings**: The ledger allocation or nominal heading assigned to each expense item [^r1][^r4].

## Messages
The accounts team rejects the entire expense batch if an incorrect cost centre or nominal heading is selected on screen AP-EXP-09 [^r4].

## Versions and conflicts
- **Expense submission window**: Today, staff must enter expense line items on screen AP-EXP-09 within 60 days of the expense [^r1]. From 2027-01-01 under [[pol-tex-007|POL-TEX-007]] v3.0, staff must record out-of-pocket business expenses directly into Ledgerline ERP using screen AP-EXP-09 within 45 days of the spend, and submitting claims after this 45-day window has expired will require exceptional sign-off from senior management [^r3][^r5] (kind: `future_dated`).

## See also
- [[pol-tex-007|POL-TEX-007 Travel and Expenses Policy]]

## References

[^r1]: 01_policies/POL-TEX-007 Travel and Expenses Policy v2.4.pdf, p. 4, §5. Claims
[^r2]: 01_policies/POL-TEX-007 Travel and Expenses Policy v2.4.pdf, p. 4, §5. Claims
[^r4]: 01_policies/POL-TEX-007 Travel and Expenses Policy v3.0 (effective 2027-01-01).pdf, p. 3, Common Errors
[^r3]: 01_policies/POL-TEX-007 Travel and Expenses Policy v3.0 (effective 2027-01-01).pdf, p. 2, Purpose and Process
[^r5]: 01_policies/POL-TEX-007 Travel and Expenses Policy v3.0 (effective 2027-01-01).pdf, p. 3, Common Errors
