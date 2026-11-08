---
title: "SOP-AP-001 Three-Way Invoice Matching"
type: "procedure"
slug: "sop-ap-001"
summary: "Standard operating procedure for three-way supplier invoice matching against purchase orders and receipts in Ledgerline."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-AP-001 |
| Title | Three-Way Invoice Matching |
| Version | 2.1 |
| Status | current |
| Effective date | 2025-04-01 |
| Owner | Marta Kowalski |
| Approver | Grace Whitaker |

SOP-AP-001 defines the operational procedure for matching incoming supplier invoices against purchase orders and goods receipts in Ledgerline [^r1][^r2]. As of 26 October 2026, version 2.1 is current and governs all invoice processing across Northbridge Cycles [^r1]. Automated holds apply to discrepancies in rates and quantities, with match overrides restricted to designated authority [^r3][^r4][^r5].

## Steps

1. Enter every supplier invoice on screen [[screen-ap-inv-01|AP-INV-01]] against its corresponding purchase order [^r2].
2. For invoices from overseas suppliers using -RC tax codes, record the invoice without supplier VAT, allowing Ledgerline to automatically account for the reverse charge [^r6].
3. Run or await the background job JOB-AP-010 to execute the automated three-way match comparing the entered invoice with purchase order data and recorded receipts [^r2].
4. Resolve holds applied by the system:
   * A line is placed on price hold (HOLD-PRC) when the rate differs from the purchase order rate by more than 2% or by more than £50, whichever is smaller [^r3].
   * A line is placed on quantity hold (HOLD-QTY) when the invoiced quantity exceeds the recorded quantity received [^r4].
5. Transfer physical goods receipt dockets from the Leeds unit promptly to the central accounts office in Manchester following receipting [^r7].

## Forms and screens

* Screen [[screen-ap-inv-01|AP-INV-01]] (Supplier Invoice Entry): used to record every supplier invoice against its purchase order [^r2].
* Background job JOB-AP-010: executes the three-way comparison between invoice lines, purchase orders, and physical receipts [^r2].
* Physical goods receipt dockets: documentation transferred from Leeds to Manchester [^r7].

## Checks and approvals

* Only AP manager [[user-mkowalski|Marta Kowalski]] possesses authority to override a match [^r1][^r5].
* Attempting a match override without permission triggers error [[err-mat-0420|ERR-MAT-0420]] [^r5].
* The procedure is approved by financial controller [[user-gwhitaker|Grace Whitaker]] [^r1].
* Rate variations are governed by the [[topic-price-tolerance|price tolerance]] thresholds of 2% or £50, whichever is smaller [^r3].

## See also

* [[screen-ap-inv-01|AP-INV-01 Supplier Invoice Entry]]
* [[err-mat-0420|ERR-MAT-0420 Match Override Permission Denied]]
* [[user-gwhitaker|Grace Whitaker]]
* [[user-mkowalski|Marta Kowalski]]
* [[topic-price-tolerance|topic-price-tolerance]]

## References

[^r1]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 1, Three-Way Invoice Matching
[^r2]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 3, §5. Procedure
[^r3]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 3, §5. Procedure
[^r6]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 3, §5. Procedure
[^r7]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 5, §6. Records
