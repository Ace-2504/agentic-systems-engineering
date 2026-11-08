---
title: "Price tolerance"
type: "topic"
slug: "topic-price-tolerance"
summary: "Price variance rules governing purchase order placement against contract rates and three-way invoice matching tolerances in Accounts Payable."
audience: "staff"
status: "mixed"
sources: ["01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf", "01_policies/old/Purchase Policy v4.0.docx", "02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| PO contract price tolerance | 2% |
| PO excess requirement | Written justification from manager in remarks |
| Invoice price tolerance | 2% or £50, whichever is smaller |
| Invoice price hold code | HOLD-PRC |
| Invoice quantity hold code | HOLD-QTY |

Price tolerance rules define the allowable rate variances when placing purchase orders against rate contracts and when matching supplier invoices against purchase orders. Today, purchasing allows a 2% variance over rate contracts before requiring manager justification, while Accounts Payable holds invoices exceeding purchase order rates by more than 2% or £50. These controls ensure cost discipline across procurement and invoice settlement.

## Purchasing rate contract tolerance

Under [[pol-pur-001|POL-PUR-001]] v4.1, effective 2026-04-01, the purchasing price tolerance over the rate contract is 2% [^r1]. Any rate exceeding 2% above the contract requires written justification from the manager in the remarks [^r1].

## Invoice matching price tolerance

Under [[sop-ap-001|SOP-AP-001]], invoice lines are held on HOLD-PRC if the unit rate differs from the purchase order rate by more than 2% or £50, whichever is smaller [^r2]. Additionally, invoice lines are held on HOLD-QTY if the invoiced quantity is greater than the recorded quantity received [^r3].

## Versions and conflicts

- **Purchasing rate contract tolerance limit**: Today, purchasing price tolerance over the rate contract is 2%, with any rate exceeding 2% above contract requiring written justification from the manager in the remarks [^r1]. Under superseded POL-PUR-001 v4.0, any order placed at a rate exceeding 5% above the contract rate required the manager's written reason recorded in the remarks [^r4]. Sources: POL-PUR-001 v4.1 (effective 2026-04-01) and POL-PUR-001 v4.0 (superseded). Kind: `superseded`.

## See also

* [[pol-pur-001|POL-PUR-001 Purchase Policy]]
* [[sop-ap-001|SOP-AP-001 Three-Way Invoice Matching]]

## References

[^r1]: 01_policies/POL-PUR-001_Purchase_Policy_v4.1.pdf, p. 2, §7. Prices
[^r2]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 3, §5. Procedure
[^r3]: 02_procedures/SOP-AP-001 Three-Way Invoice Matching v2.1.pdf, p. 3, §5. Procedure
[^r4]: 01_policies/old/Purchase Policy v4.0.docx, §7. Prices
