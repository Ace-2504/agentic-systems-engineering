---
title: "AP-INV-01 Supplier Invoice Entry"
type: "screen"
slug: "screen-ap-inv-01"
summary: "Ledgerline screen used to enter supplier invoices against purchase orders for automated three-way matching."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | AP-INV-01 |
| Name | Supplier Invoice Entry |
| System | Ledgerline |
| Associated procedure | SOP-AP-001 |
| Automated job | JOB-AP-010 |

Screen AP-INV-01 is the Ledgerline interface used to capture incoming supplier invoices against purchase orders for three-way matching [^r1]. It executes match processing through background job JOB-AP-010 to verify invoice totals against purchase orders and receipt balances [^r1]. Today, accounts payable staff must review flagged holds and tax settings on this screen before posting invoices forward [^r2][^r3][^r4].

## What it is for

On screen AP-INV-01, accounts payable staff enter supplier invoices directly against their corresponding purchase orders to execute automated three-way matching via job JOB-AP-010 [^r1].

## Fields

Key fields and panes to check on screen AP-INV-01 include the purchase order reference field, the line details grid, the receipt balance on the matching pane, the unit rate comparison, the tax code field, and the hold status pane [^r2]. Domestic invoices entered on screen AP-INV-01 carry the standard rate, whereas overseas supplier invoices show designated -RC tax codes with zero supplier-entered tax [^r3].

## Messages

Lines flagged on screen AP-INV-01 with HOLD-PRC or HOLD-QTY indicate matching exceptions and must be examined immediately rather than posted forward [^r4].

## See also

* [[sop-ap-001|SOP-AP-001 Three-Way Invoice Matching]]
* [[err-mat-0420|ERR-MAT-0420 Match Override Permission Denied]]
* [[topic-price-tolerance]]

## References

[^r1]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 4, What to check on screen AP-INV-01
[^r3]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 4, What to check on screen AP-INV-01
[^r4]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 4, What to check on screen AP-INV-01
