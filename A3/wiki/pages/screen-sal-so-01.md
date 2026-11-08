---
title: "SAL-SO-01 Sales Order"
type: "screen"
slug: "screen-sal-so-01"
summary: "Ledgerline screen used to enter retailer orders, featuring automated credit checks upon order confirmation."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | SAL-SO-01 |
| System | Ledgerline ERP |
| Purpose | Retailer order entry |
| Related procedure | SOP-SAL-001 |

Screen SAL-SO-01 is the Ledgerline ERP interface used to record incoming retailer orders [^r1]. When an order is confirmed, the system runs an automated credit check against the retailer's account [^r1]. If the retailer's credit limit is exceeded, order confirmation is halted and the record remains unconfirmed until accounts clears the outstanding balance [^r1][^r2].

## What it is for
Staff use screen SAL-SO-01 to enter retailer orders under [[sop-sal-001|SOP-SAL-001]] [^r1]. Confirming an entered order initiates an automated credit verification routine in Ledgerline ERP [^r1].

## Fields
The screen captures retailer order entry details prior to order confirmation [^r1].

## Messages
When a customer exceeds their credit limit during confirmation, Ledgerline ERP halts the process and outputs the credit error message [[err-crd-0207|ERR-CRD-0207]] [^r1][^r2]. The order remains unconfirmed in the system until accounts resolves the balance [^r2].

## See also
* [[sop-sal-001|SOP-SAL-001 Sales Order to Despatch]]
* [[err-crd-0207|ERR-CRD-0207 Credit Limit Exceeded]]

## References

[^r1]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-SAL-001 Sales Order to Despatch v2.2.pdf, p. 4, §5. Procedure: notes and common mistakes
