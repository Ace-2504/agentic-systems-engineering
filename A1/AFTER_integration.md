# AFTER: how Ask Kestrel connects to the college's systems (technical note)

This is the technical side of `AFTER.md`, kept separate so that `AFTER.md` stays about the experience, as the brief asks. It also supports frame 3 of `AFTER_SYSTEM_DESIGN_v7.excalidraw`.

## 1. The best way into each system

The college keeps its systems, so the agent uses the best way in that each one offers, from the top of this list down:

1. **API**, if the system has one.
2. **Events**: the system announces changes ("line cleared", "request forwarded"), so the agent does not keep checking.
3. **File exchange**: the system's own import and export files, such as the ERP's bulk-import template (the ERP checks every row) and the bank's statement and return files.
4. **Read-only SQL views**: if there is no API but the database is on the college's servers, the agent reads through fixed queries on prepared views, never live tables.
5. **Screen driver**: the last resort; the agent uses the screens like a person and reads back every entry.
6. **Never**: direct SQL writes into the ERP's tables, which would skip its checks, ledger posting, approvals and audit trail.

**Each system's best way in, if it has no API:**

| System | Reading | Writing |
|---|---|---|
| EduDesk (request, chat, status) | Events or read-only views | Screen driver, every write read back |
| Library, hostel, mess and lab modules | Read-only views (dues, worklists, inventory) or nightly exports | None: staff act in their own modules |
| Accounts ERP | Read-only views (refunds, exceptions queue) | The ERP's import file or its interface (staging) tables; screen driver only if neither exists |
| Bank: payments | Payment status from the bank's return file | The agent prepares the file; Ms. Iyer uploads it; Mr. Batra authorises it |
| Bank: statements and returns | Daily statement file plus the return file, which gives each return with its reason code and original reference | None |
| Rs.1 test transfer | Reuses the Rs.1 check EduDesk already runs on the form | None |
| HR leave module | Read-only view of approved leave dates only | None |
| Email and SMS | None | EduDesk's notification service, or its messaging screen |

If the accounts system were an old one with no API, no roles and one shared login, a small **gateway** would sit in front of it: the agent proposes an entry, the right person approves it in the gateway, and only the gateway writes it (with the login kept in a vault), reads it back and logs it. Every night it compares the old system's entries with its own record, and flags any made directly with the shared login. The real fix, giving each person their own login, is the college's decision.

**How the agent itself is controlled:** its own account with only the access above; every action logged with the values before and after; it never authorises a payment or approves a bank change; one key per request, so a retry never creates a second refund; and one switch stops all its writes.

## 2. Better fixed by configuration

These failures from `BEFORE.md` (marked (*) in the diagram) could also be fixed by changing settings or links between the college's systems. Ask Kestrel covers them until IT makes the changes.

| Failure | Configuration fix |
|---|---|
| 2: two copies of the bank details | Send the form's verified bank details to the ERP as a bank-change request for Mr. Batra's approval; pay only to an approved account |
| 3: payment date not shown | Show the next payment-run date on the request in EduDesk |
| 5: the return can't be matched | Use the bank's return file (confirm the bank offers one), or add a matching rule that searches the free text for the UTR |
| 7: Hostel clears before the key | A hostel module rule (or vendor change): Clear only after the inspection is approved and the key is returned |
| 1: "Refund paid" after a return | Show "Payment sent" at sending and "Refund paid" only once the bank confirms; send the ERP's "returned" event to EduDesk (needs the fix for Failure 5 first) |
