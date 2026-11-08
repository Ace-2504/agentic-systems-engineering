---
title: "AP-PER-11 Ap Period"
type: "screen"
slug: "screen-ap-per-11"
summary: "Ledgerline screen used by the AP manager on working day 3 to execute the purchase ledger period close."
audience: "staff"
status: "current"
sources: ["02_procedures/SOP-AP-002 Period Close v3.0.pdf"]
created: "2026-11-07"
updated: "2026-11-07"
---

| | |
|---|---|
| Screen code | AP-PER-11 |
| Purpose | Purchase ledger period close |
| Primary user | AP manager |
| Execution timing | Working day 3 afternoon |
| Source procedure | SOP-AP-002 |

Screen AP-PER-11 is the Ledgerline interface used to execute the purchase ledger period close under [[sop-ap-002|SOP-AP-002]][^r1]. It is operated by the AP manager on the afternoon of working day 3[^r1]. The screen ensures period status integrity and verifies that no unposted transactions remain before closing the period[^r2].

## What it is for
The screen is used by the AP manager to run the purchase ledger period close on the afternoon of working day 3[^r1].

## Fields
Staff must review the document status flags on screen to confirm that no entries remain marked as unposted or suspended[^r2]. Users must also verify the ledger period field to ensure it corresponds to the period being concluded while the following period is set to open[^r2].

## Messages
When the close process halts on screen AP-PER-11, it displays error [[err-per-0010|ERR-PER-0010]][^r3]. The user must inspect the batch control screen, post valid entries or delete temporary draft batches, and retry the close once all queues are clear[^r3].

## See also
* [[sop-ap-002|SOP-AP-002 Accounts Payable Period Close]]
* [[err-per-0010|ERR-PER-0010 Unposted Documents at Period Close]]

## References

[^r1]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 3, §5. Procedure
[^r2]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 4, What to check on screen
[^r3]: 02_procedures/SOP-AP-002 Period Close v3.0.pdf, p. 4, What to do when something does not look right
