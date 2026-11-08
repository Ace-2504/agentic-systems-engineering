---
title: "SOP-INV-002 Returns to Vendor (RTV)"
type: "procedure"
slug: "sop-inv-002"
summary: "Standard operating procedure for returning non-conforming stock to vendors across Manchester and Leeds facilities."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| code | SOP-INV-002 |
| title | Returns to Vendor (RTV) |
| version | 1.3 |
| owner | Callum Shaw |
| approver | Henrik Weber |
| effective_date | 2025-01-01 |
| status | current |

SOP-INV-002 governs the identification, quarantine, and physical dispatch of non-conforming stock returned to suppliers from the Manchester plant and Leeds unit [^r1][^r3]. As of 26 October 2026, version 1.3 is in force under the ownership of stores manager [[user-cshaw|Callum Shaw]], approved by plant head [[user-hweber|Henrik Weber]] [^r1]. It covers all raw materials, frame components, electrical assemblies, and workshop consumables previously receipted into stock [^r3].

## Steps

1. Goods identified as unusable in production must be isolated immediately in the designated quarantine area [^r2].
2. Goods Inwards and Stores segregate non-conforming deliveries into the returns holding pen and apply red rejected labels [^r4].
3. Quality control inspectors examine components, record findings on an internal inspection note, and confirm whether parts warrant return, rework, or scrap [^r5].
4. Staff move items designated for return to warehouse [[data-warehouses|WH-MAN-RTV]] and label them with the RTV number [^r12].
5. Staff raise the RTV entry on screen [[screen-inv-rtv-07|INV-RTV-07]] against the GRN within 30 days of receipt, following [[pol-ret-006|POL-RET-006]] §2.1 [^r11].
6. The purchasing team contacts the vendor, secures written return authorisation, and enters the debit memo request against the original purchase order [^r6].
7. Dispatch prepares shipping crates, books the carrier, and confirms departure on the transport manifest [^r7]. For [[items-bat|battery packs]], dispatch must arrange transport exclusively through the carrier's dangerous-goods service with a UN3480 label affixed to each approved crate [^r14].
8. The collection driver signs the dispatch note before packages leave the loading bay, after which the original is sent to purchase ledger, one copy is archived in stores, and a third copy is enclosed in the consignment packing envelope [^r15].

## Forms and screens

* Screen [[screen-inv-rtv-07|INV-RTV-07]] is used to enter the RTV against the original GRN [^r11].
* Internal inspection note records quality control findings [^r5].
* Transport manifest and carrier dispatch note record physical departure and driver handover [^r7][^r15].
* Red rejected labels and UN3480 dangerous-goods labels are required for item identification and hazardous compliance [^r4][^r14].

## Checks and approvals

* Quality control inspectors must approve whether non-conforming parts warrant return, rework, or scrap [^r5].
* The purchasing team must obtain written vendor return authorisation prior to processing the debit memo request [^r6].
* If the receipted GRN has already been invoiced, Ledgerline prevents entry with error [[err-rtv-0230|ERR-RTV-0230]], requiring accounts payable to issue a debit note instead [^r13].
* Purchase ledger clerks must verify that the supplier issues a credit note matching the debit entry before closing the record on the ledger [^r8].
* Manchester and Leeds operational teams must review the open returns report weekly with purchasing to clear aged suspense records [^r9].
* Rejected stock must never be scrapped locally without formal written permission from both the supplier and the purchase ledger supervisor [^r10].

## See also

* [[data-warehouses|Warehouses]]
* [[err-rtv-0230|ERR-RTV-0230 RTV Refused Against Invoiced Receipt]]
* [[items-bat|BAT-* items]]
* [[pol-ret-006|POL-RET-006 Returns Policy]]
* [[screen-inv-rtv-07|INV-RTV-07 Return To Vendor Entry]]
* [[user-cshaw|Callum Shaw (CSHAW)]]
* [[user-hweber|Henrik Weber (HWEBER)]]

## References

[^r1]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 1, Returns to Vendor (RTV)
[^r3]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 2, §2. Scope
[^r2]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 1, §1. Purpose
[^r4]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 2, §3. Responsibilities
[^r5]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 2, §3. Responsibilities
[^r12]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 3, §5. Procedure
[^r11]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 3, §5. Procedure
[^r6]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 2, §3. Responsibilities
[^r7]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 2, §3. Responsibilities
[^r14]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 3, §5. Procedure
[^r15]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 4, §6. Records
[^r13]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 3, §5. Procedure
[^r8]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 3, §3. Responsibilities
[^r9]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 3, §3. Responsibilities
[^r10]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 3, §3. Responsibilities
