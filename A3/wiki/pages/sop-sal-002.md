---
title: "SOP-SAL-002 Warranty Claims from Bike Shops"
type: "procedure"
slug: "sop-sal-002"
summary: "Standard operating procedure for receiving, assessing, and settling electric bicycle warranty claims submitted by bike shops."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Code | SOP-SAL-002 |
| Owner | Isla Morgan |
| Approver | Pieter Jansen |
| Version | 1.1 |
| Effective | 2025-03-01 |
| Status | current |

SOP-SAL-002 defines the standard operating procedure for receiving, evaluating, and resolving warranty claims submitted by bike shops for electric bicycles and sub-assemblies [^r2]. As of 26 October 2026, the procedure is current under the ownership of sales manager [[user-imorgan|Isla Morgan]] following approval by quality manager [[user-pjansen|Pieter Jansen]] [^r1]. Direct retail customer submissions are out of scope and must be redirected to the original supplying retailer [^r2].

| Field | Value |
|---|---|
| Code | SOP-SAL-002 [^r1] |
| Owner | [[user-imorgan|Isla Morgan]] [^r1] |
| Approver | [[user-pjansen|Pieter Jansen]] [^r1] |
| Version | 1.1 [^r1] |
| Effective date | 2025-03-01 [^r1] |
| Status | CURRENT [^r1] |

## Steps

1. The Leeds sales office acts as the primary contact to receive the warranty claim from the bike shop, requiring the frame or pack serial number [^r3][^r4].
2. The serial number must be verified against [[screen-sal-srl-16|SAL-SRL-16]], and if unregistered, the claim is refused with [[err-rma-0210|ERR-RMA-0210]] [^r4].
3. Warranty coverage periods must be verified in accordance with [[pol-ret-006|POL-RET-006]] §3.1 [^r5].
4. Approved claims are assigned an RMA number, and bike shops returning battery packs must send them exclusively via the dangerous-goods service [^r6].
5. If a battery pack arrives through an ordinary parcel carrier rather than the dangerous-goods route, staff must notify the safety officer immediately and log the incident on the claim file before unpacking [^r8].
6. The Manchester plant warehouse receives and inspects the physical goods [^r3].
7. If physical items received do not match the RMA record serial number or description, staff must pause the claim, keep the package in the returns bay, and refer the issue to Quality instead of forwarding mismatched items to the workshop [^r9].
8. Quality conducts an assessment and must decide whether to repair, replace, or refuse the claim within 10 working days of receipt [^r7].
9. Manchester accounts staff apply credit notes to the sales ledger once goods inwards or technical services sign off [^r3].

## Forms and screens

- [[screen-sal-srl-16|SAL-SRL-16]] (Serial Registration Reg): screen where frame or pack serial numbers must be registered [^r4].
- [[err-rma-0210|ERR-RMA-0210]]: error code generated when an unregistered serial number is submitted [^r4].
- RMA record: generated authorization number tracking approved claims and item descriptions [^r6][^r9].

## Checks and approvals

- Technical services desk reviews reported faults and authorizes returns or replacement parts [^r3].
- Frame or pack serial numbers must validate in [[screen-sal-srl-16|SAL-SRL-16]] or trigger refusal under [[err-rma-0210|ERR-RMA-0210]] [^r4].
- Warranty eligibility must comply with the periods established in [[pol-ret-006|POL-RET-006]] §3.1 [^r5].
- Quality must determine whether to repair, replace, or refuse the claim within 10 working days of item receipt [^r7].
- Goods inwards or technical services sign-off is mandatory before Manchester accounts can apply credit notes [^r3].

## See also

- [[err-rma-0210|ERR-RMA-0210 Unregistered Serial Number]]
- [[pol-ret-006|POL-RET-006 Returns Policy]]
- [[screen-sal-srl-16|SAL-SRL-16 Serial Registration Reg]]
- [[user-imorgan|Isla Morgan]]
- [[user-pjansen|Pieter Jansen]]

## References

[^r2]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 2, §2. Scope
[^r1]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 1, Field Value
[^r3]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 2, §3. Responsibilities
[^r4]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 3, §5. Procedure
[^r5]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 3, §5. Procedure
[^r6]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 3, §5. Procedure
[^r8]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r9]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 4, §5. Procedure: notes and common mistakes
[^r7]: 02_procedures/SOP-SAL-002 Warranty Claims (RMA) v1.1.pdf, p. 3, §5. Procedure
