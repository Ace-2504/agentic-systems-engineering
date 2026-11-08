---
title: "PUR-PO-01 Purchase Order Entry"
type: "screen"
slug: "screen-pur-po-01"
summary: "Ledgerline screen for creating purchase orders from requisitions, fetching contract rates, and managing status codes and tax configurations."
audience: "staff"
status: "mixed"
sources: ["02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf", "02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf", "02_procedures/SOP-PUR-002 PR to PO v1.4.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen | PUR-PO-01 |
| Name | Purchase Order Entry |
| System | Ledgerline |
| Supported Order Types | STD |
| Status | current |

PUR-PO-01 is the Ledgerline screen used to raise and enter purchase orders from approved purchase requisitions [^r3]. It relies on existing rate contracts to populate unit rates and requires mandatory fetch actions before saving [^r1][^r4]. Operators must verify document header statuses directly on this screen because status bar confirmations display even when validation issues hold an order [^r6].

| Field | Value |
|---|---|
| Screen | PUR-PO-01 |
| Name | Purchase Order Entry |
| System | Ledgerline |
| Supported Order Types | STD |
| Status | current |

## What it is for

PUR-PO-01 is used to enter standard purchase orders raised from approved requisitions using order type STD as specified in [[sop-pur-002|SOP-PUR-002]] [^r3]. The screen connects to rate contracts maintained under [[sop-pur-004|SOP-PUR-004]], allowing its Fetch function to automatically populate agreed unit rates [^r1]. Due to Ledgerline parameter PUR.CERT_CHK being configured as N, PUR-PO-01 does not validate certificate validity when saving purchase orders [^r2].

## Fields

* **Source PR**: The field where the request number must be entered for standard purchase orders converted from requisitions [^r3].
* **Order Type**: Entered as STD for standard purchase orders [^r3].
* **Supplier**: Populated with the supplier identifier prior to fetching rates [^r4].
* **Item**: Populated with the required item prior to fetching rates [^r4].
* **Tax Code**: Automatically fills with VAT20-UK upon pressing Fetch, but operators must manually edit this to VAT20-RC for overseas suppliers to avoid save failures [^r5].
* **Header Status**: Displays the true processing status of the document, showing DR (held/draft), PA (awaiting approval), or AP (approved) [^r6].

## Messages

* **SAVED**: Displayed on the status bar upon save even if the purchase order fails validation, requiring staff to inspect the header Status field rather than relying on the bar [^r6].
* **[[err-scr-0221|ERR-SCR-0221]]**: Triggered when attempting to save the record without first pressing F3 (Fetch) after entering the supplier and item [^r4].
* **[[err-po-0412|ERR-PO-0412]]**: Triggered upon save if the default tax code VAT20-UK is not changed to VAT20-RC for an overseas supplier [^r5].
* **W-CC-114**: Warning displayed when an order line references a closed cost centre, causing the order to remain held in DR status [^r7].

## Versions and conflicts

* Standard PO creation and validation rules on PUR-PO-01 under current [[sop-pur-002|SOP-PUR-002]] v1.4 (effective 2025-02-01) | Handled under identical steps in superseded SOP-PUR-002 v1.3 (effective 2023-05-01) | SOP-PUR-002 v1.4 p. 3-4, SOP-PUR-002 v1.3 p. 3 | superseded [^r3][^r4][^r5][^r6][^r7][^r8][^r9][^r10]

## See also

* [[err-po-0412|ERR-PO-0412]]
* [[err-scr-0221|ERR-SCR-0221]]
* [[sop-pur-001|SOP-PUR-001 Supplier Onboarding]]
* [[sop-pur-002|SOP-PUR-002 Purchase Request to Purchase Order]]
* [[sop-pur-004|SOP-PUR-004 Rate Contract Maintenance]]

## References

[^r3]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r1]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 3, §5. Procedure
[^r4]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r6]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-PUR-001 Supplier Onboarding v3.1.pdf, p. 5, §6. Timing and system checks
[^r5]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 3, §5. Procedure
[^r7]: 02_procedures/SOP-PUR-002 PR to PO v1.4.pdf, p. 4, What to do when something does not look right
[^r8]: 02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf, p. 3, §5. Procedure
[^r9]: 02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf, p. 3, §5. Procedure
[^r10]: 02_procedures/SOP-PUR-002 PR to PO v1.3 (FINAL).pdf, p. 3, §5. Procedure
