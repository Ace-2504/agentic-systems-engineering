---
title: "Warehouses"
type: "data-source"
slug: "data-warehouses"
summary: "Master data list of Northbridge Cycles warehouse codes, including designated return holding and battery storage locations."
audience: "staff"
status: "current"
sources: ["01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf", "02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Source type | Master data reference |
| Current warehouses | WH-MAN-STR, WH-MAN-RTV |
| Deprecated warehouses | WH-MAN-BAT |
| Scope | Northbridge inventory and storage locations |

This data source defines operational warehouse codes and their designated storage uses across Northbridge Cycles as of 26 October 2026. Active facilities include WH-MAN-STR for general and battery stock and WH-MAN-RTV for rejected stock awaiting return to vendor [^r1][^r2]. Historical codes such as WH-MAN-BAT have been merged and remain retired to prevent misallocation [^r1].

## What it holds
The warehouse master records designate specific facilities and holding zones for operational inventory, rejected materials, and specialized components [^r1][^r2]. Under [[pol-bat-004|POL-BAT-004]], warehouse WH-MAN-STR contains bin zones BAT-Z1 through BAT-Z4 dedicated to lithium-ion battery packs [^r1]. Under [[sop-inv-002|SOP-INV-002]], warehouse WH-MAN-RTV functions as the return holding warehouse where rejected stock must be physically transferred and labelled with an RTV number [^r2].

## Columns
* **Warehouse Code**: The unique code identifying the facility (for example, WH-MAN-STR or WH-MAN-RTV) [^r1][^r2].
* **Function / Usage**: The designated operational role, such as battery storage or return holding [^r1][^r2].
* **Permitted Zones**: Specific sub-locations or bins within the facility, such as BAT-Z1 to BAT-Z4 for battery packs [^r1].
* **Status**: Operational lifecycle status indicating whether the code is current or merged [^r1].

## How to look up a row
To look up a warehouse allocation:
1. Locate the item category or transaction type, such as lithium-ion battery handling or rejected stock returns [^r1][^r2].
2. Identify the active facility code, confirming that WH-MAN-STR is used for battery stock and WH-MAN-RTV is used for return holding [^r1][^r2].
3. For battery packs, assign storage specifically within bin zones BAT-Z1 to BAT-Z4, ensuring the retired code WH-MAN-BAT is avoided [^r1].

## Versions and conflicts
* **Today's rule**: Warehouse WH-MAN-STR is used for lithium-ion battery pack storage (in bin zones BAT-Z1 to BAT-Z4) [^r1]. | **Older rule**: Warehouse code WH-MAN-BAT was used until it was merged into WH-MAN-STR in 2019 and prohibited [^r1]. | Sources: POL-BAT-004 v1.2 (2025-11-01) [^r1]. | Kind: `superseded`.

## See also
* [[pol-bat-004|POL-BAT-004 Battery Safety and Handling Policy]]
* [[sop-inv-002|SOP-INV-002 Returns to Vendor (RTV)]]

## References

[^r1]: 01_policies/POL-BAT-004 Battery Safety and Handling Policy v1.2.pdf, p. 2, §2. Storage
[^r2]: 02_procedures/SOP-INV-002 Returns to Vendor (RTV) v1.3.pdf, p. 3, §5. Procedure
