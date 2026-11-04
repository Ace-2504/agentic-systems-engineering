# AFTER: Hostel deposit refund

The same fictional process as BEFORE.md (Kestrel Institute of Technology, May 2025), as it should work with an AI agent. The college keeps its systems: EduDesk, the library, hostel, mess and lab modules, the Accounts ERP and the bank's corporate internet banking. What changes is that an agent, **Ask Kestrel**, sits across them. Students and staff ask it in plain words. It does the coordinating, checking, data entry and reconciliation, and every decision that needs judgement or carries money stays with a named person.

The diagram for this file is `AFTER_SYSTEM_DESIGN_v6.excalidraw`, laid out as frames: an overview (the key, what stays human, the result), 2nd–12th May (the request, the bank check and the clearances), 12th–15th May (refund, payment and the bank's answer), and how it would work on an old accounts system. The tables that used to sit beside the flow are now in sections 6 and 7 of this file. The people are the same as in BEFORE.md, plus one: Aarav (student), the lab assistant, Mr. Joseph (caretaker), Dr. Menon (warden), Mr. Gill (mess), Ms. Iyer (accounts clerk), the signatory (Mr. Batra, accounts officer and the only person registered with the bank to authorise payments from the student-deposit account) and the finance head (Ms. Rao, Mr. Batra's manager). After the table below they are named without their roles.

### The people

| Who | Role | What they do in the AFTER |
|---|---|---|
| Aarav | Student, room `H3-214` | Tells Ask Kestrel what he wants, gives his bank account once, says yes to previews |
| The lab assistant | Labs | Confirms in one click that nothing is outstanding |
| Mr. Joseph | Hostel caretaker | Inspects the room, records any damage with a photo, takes back the key |
| Dr. Menon | Hostel warden | Approves inspections and decides any disputed deduction |
| Mr. Gill | Mess office | Takes back the mess card `MC-3381` |
| Ms. Iyer | Accounts clerk | Reviews the payment file the agent builds and sends it to the bank (maker); handles bank lines the agent cannot match |
| Mr. Batra | Accounts officer; the only signatory registered for the student-deposit account | Approves bank-detail changes; authorises payment files at the bank (checker) |
| Ms. Rao | Finance head, Mr. Batra's manager | Approves off-cycle payment runs |
| The HR head | HR | Gives the agent read-only access to approved leave dates (with Ms. Rao) |
| **Ask Kestrel** | The AI agent | Coordinates, checks, drafts and reconciles; never authorises money or approves an exception |

## 1. The sentence

Instead of filling a form and checking four status lines, people would say:

**Aarav (student)**

1. *"I move out on 12th May. Please refund my hostel deposit."*
   One sentence, plus his current bank account, replaces the form.
2. *"What do I still owe before I get my deposit back?"*
   Today he pieces it together from four separate lines on EduDesk.
3. *"Why is Rs.540 being taken off my refund?"*
   Today the Rs.40 library fine and the Rs.500 chair sit in two different modules.
4. **"Has my refund actually reached my bank? If not, why not, and when will it?"**
   **No current screen answers this.** In the BEFORE, EduDesk said "Refund paid" for 26 days while the money was back with the college, because EduDesk only ever hears that a payment was sent.

**Staff**

5. Ms. Iyer: *"Which refunds are due in the next run, are all their bank accounts approved, and did anything come back from the bank this morning?"*
   Today she finds a returned payment at month-end reconciliation.
6. Mr. Batra and Ms. Rao: *"What is waiting for my approval, and why?"*
7. Dr. Menon: *"Which inspections need my approval before the next payment run?"*

## 2. Feel and trust

### What Aarav sees

On 2nd May, one checklist in plain words, with the reason and the next action for each line:

> - **Library:** one book returned 4 days late, fine Rs.40. It will be deducted from your refund; nothing to do.
> - **Labs:** nothing issued to you. Waiting for the lab assistant to confirm, usually within 2 working days.
> - **Hostel:** your room needs an inspection. *Mr. Joseph can come on 7th May, 4 PM. Confirm?* Return your key on your last day.
> - **Mess:** return mess card `MC-3381` at the mess office on your last day.
> - **Bank:** your college record still has the account you added in 2022, which is closed. I sent Rs.1 to the account you just gave me and it arrived. Mr. Batra must approve the change before your refund can use it.
> - **Your refund:** Rs.14,460 (Rs.15,000 − Rs.500 hostel − Rs.40 library) if nothing else changes. Expected payment: 15th May.

Where he is waiting, it says on whom and until when. On 12th May it tells him: *"The 15th May payment run would wait for Mr. Batra, who is on leave from 15th May. I've asked Ms. Rao for an earlier run on 14th May."*

### How much he does

| | Before | After |
|---|---|---|
| Typing | the full form (enrollment no., `H3-214`, account no., IFSC) and a helpdesk ticket | **one sentence and his bank account, once**, then taps (Confirm, Accept) |
| Codes he types, reads or quotes | 7 (enrollment no., `H3-214`, account no., IFSC, `MC-3381`, `REQ-25-0917`, the UTR) | **2** (account no. and IFSC, once) |
| Visits in person | 1 (mess counter) | **1** (handing in the mess card and key is physical) |
| Helpdesk tickets | 1 | **0** |
| Hands-on time | about 1 hour 35 minutes | **about 40 minutes** |
| Elapsed time | 46 days (2nd May → 17th June) | **12 days** (2nd May → 14th May) |

Aarav's 40 minutes: 5 minutes telling Ask Kestrel and giving his account, 20 minutes for the inspection and accepting the charge, 10 minutes returning his key and mess card, 5 minutes reading updates. These are estimates, like the BEFORE figures.

### What is previewed before anything is saved

Nothing is submitted or changed without a preview and the right person's yes:

- **The refund request:** deposit, every deduction known so far, and the expected payment date. Aarav says yes.
- **The bank account:** the Rs.1 test-transfer result, shown to Aarav, then sent to Mr. Batra with the proof attached.
- **Each deduction:** the Rs.500 chair with Mr. Joseph's photo and the rate-card line, with Accept and Dispute, before any money moves.
- **The payment file:** every amount and account checked by the agent, then reviewed by Ms. Iyer before it goes to the bank.

### How he knows it is done

Only when **the bank** confirms the money arrived, never when the college merely sends it:

1. 14th May: *"Payment sent to your bank. UTR `KTB2505140019`. I'll confirm when the bank statement shows it."* (not done yet)
2. 15th May: *"Rs.14,460 was credited to your account ending ••4721 on 14th May (UTR `KTB2505140019`). Request `REQ-25-0917` is closed."* (done)

EduDesk shows "Payment sent" after the first and "Refund credited" only after the second.

### What would make him trust it

- **The numbers match.** The amount it says arrived is the amount on his bank SMS, and the deductions add up to the difference.
- **Every deduction has a name, a reason and evidence**, and he could dispute it before it was paid.
- **It tells him early, in plain words,** when something is waiting and on whom. He never has to raise a ticket to find out.
- **It is right about dates.** When the date moved, it told him why and gave the new one.

### What would make him give up on it

- **It says "done" and the money does not arrive.** That is exactly what EduDesk did in the BEFORE. One repeat and he goes back to the helpdesk.
- **It asks for the same details again**, such as his bank account, after he already gave and confirmed them.
- **It cannot say why** something is stuck, or answers with a status code.
- **It acts without asking**, for example submitting the request before he said yes.

## 3. Approvals

### What needs a human yes

Ask Kestrel prepares, checks and explains. These decisions stay with a named person, and each one is shown as a preview that waits for that person's yes.

| Decision | Whose yes | Rule |
|---|---|---|
| Submit the refund request | Aarav | always |
| Change the bank account in the ERP student record | Mr. Batra | always; bank details are protected, and the Rs.1 test-transfer proof is attached |
| Record room damage and its amount | Mr. Joseph | from the rate card, with a photo |
| Accept a deduction, or dispute it | Aarav | before the refund is paid |
| Decide a disputed deduction | Dr. Menon | every dispute, with the evidence the agent collects |
| Approve the room inspection | Dr. Menon | before the Hostel line can clear; the line clears only after the key is back |
| Clear an office's line | that office (the lab assistant, Mr. Gill; the library fine is posted by the library module) | only the office itself can clear its own line |
| Review the payment file and send it to the bank (maker) | Ms. Iyer | every run; the agent builds and checks the file |
| Pay outside the 1st/15th calendar (off-cycle run) | Ms. Rao | every off-cycle run |
| Authorise the payment file at the bank (checker) | Mr. Batra | every file; the bank's own rule |
| Let the agent read approved leave dates | HR head and Ms. Rao | once, read-only, dates only |

Approvers ask in plain words too. Mr. Batra: *"Show me what is waiting for my approval."* He sees each bank change with its Rs.1 proof, and each payment file with its total and the refunds in it, before he says yes.

### What must never happen

1. **Money is never paid into an account that has not been verified and approved.** The Rs.1 test transfer must succeed and Mr. Batra must approve the change first.
2. **A refund is never paid twice.** Each refund carries one reference; if it is unclear whether a payment went through, the agent checks with the bank and never sends again on a guess.
3. **Nothing is deducted without a recorded reason, evidence and the office that made it.**
4. **Nothing is reported as "paid", "credited" or "done" before the bank confirms the money arrived.**
5. **The agent never authorises a payment, approves a bank change or approves an exception.** It only prepares and asks.
6. **No one approves their own work.** Ms. Iyer prepares the file; Mr. Batra authorises it.
7. **The agent never writes straight into a system's database.** It writes only through the system's own API, import files or screens, so the system's checks, approvals and audit trail always run.
8. **One student's dues, deductions or bank details are never shown to another student.**

## 4. Proof

Every time Ask Kestrel says something has happened, it gives a reference from the system that actually holds the record, so Aarav never has to take its word for it.

### What Aarav gets back

| When | What he gets | How he can check it himself |
|---|---|---|
| Request submitted (2nd May) | Request number `REQ-25-0917` and a link to its EduDesk page | Open EduDesk directly: the same request, date and status |
| Bank account checked (2nd May) | *"Rs.1 sent to your account ending ••4721: arrived"* | The Rs.1 credit in his own bank app |
| Bank change approved (5th May) | *"Mr. Batra approved your new account on 5th May"* | The accounts office can see the approval in the ERP |
| Each office clears him | *"Library: 2nd May"*, *"Labs: confirmed by the lab assistant, 5th May"*, *"Hostel: cleared after your key was returned, 12th May"*, *"Mess: card returned, 12th May"* | Each office's own line on EduDesk, with its date |
| A deduction is recorded (7th May) | *"Rs.500, broken chair, recorded by Mr. Joseph"*, with the photo and rate-card line | The inspection record in the hostel module |
| Refund created (12th May) | Refund `RV-25-1184` for **Rs.14,460** (Rs.15,000 − Rs.500 − Rs.40) | The amount must equal the deposit minus the listed deductions |
| Payment sent (14th May) | The UTR | The bank's own tracking number for the payment |
| Money arrived (15th May) | *"Rs.14,460 credited on 14th May"*, with the UTR | **His own bank statement, app or SMS:** a credit of Rs.14,460 with the same UTR and date |
| Request closed (15th May) | *"Request `REQ-25-0917` is closed"* | EduDesk shows it closed |

### The check that matters most

**The bank's own record.** The final proof does not come from the college or from the agent: it is the credit on Aarav's bank statement, with a UTR he can match. In the BEFORE, EduDesk said "Refund paid" and nothing could prove it wrong except money that never came. In the AFTER, "credited" is only said once the bank statement shows it.

### Proof for staff too

- **Ms. Iyer** sees, for every refund in a run, the approved account and the Rs.1 proof, and each morning a list of bank lines matched, returned or left for her.
- **Mr. Batra** sees exactly what he authorised; his authorisation is recorded by the bank against the file.
- **Ms. Rao** sees why an off-cycle run was asked for (the leave dates) and what it contains; her approval is recorded in the ERP.
- **Every action by the agent is logged**: what it did, when, on whose request, with the values before and after.

## 5. Failure

Two ways it can go wrong: one where it misunderstands the person, one where a system fails.

### Failure A: it misunderstands, a room change read as a move-out

- **What happens:** Suppose Aarav were only moving rooms next semester (H3 to H5) but typed *"I'm moving out of the hostel this week."* Ask Kestrel reads this as leaving the hostel and prepares a deposit refund, which would **end his hostel place**.
- **Who notices, and how fast:** Aarav, **immediately, at the preview**. Before anything is submitted it says in bold: *"This ends your hostel place for next semester and refunds your Rs.15,000 deposit. Submit?"*
- **How it is undone:** He taps *Change something* and says he is only changing rooms. **Nothing was submitted**, so there is nothing to undo.
- **Harm in between:** None. This is why every preview states the consequence in plain words, not just the form fields.
- **If he had tapped Yes anyway:** The agent also sees he has a room booked in H5 for next semester and flags the clash to Dr. Menon. Four offices and a payment run still stand between the request and any money, and he can cancel with one sentence at any point before the run.

### Failure B: a system fails, the bank's acknowledgement is lost

- **What happens:** On 14th May the payment file goes to the bank, but **the bank's acknowledgement never comes back**. Nobody knows whether Rs.14,460 went out.
- **Who notices, and how fast:** Ask Kestrel, **within the hour**, because it waits for that acknowledgement.
- **How it is handled:** It **does not send the file again**. It asks the bank for the file's status (through the bank's API, or Ms. Iyer checks the file status in internet banking if there is no API), finds the payment **was** made once, and records that. It tells Ms. Iyer: *"The file for 14th May was processed once; the acknowledgement was lost; no action needed."* Aarav is told only what is true: *"Payment sent; waiting for the bank statement to confirm."* The next morning's statement confirms it.
- **Harm in between:** None to Aarav. The harm avoided is **paying him twice** (Rs.28,920 out instead of Rs.14,460), which accounts would then have to recover from a student who has left.
- **If the bank says it was not processed:** The agent prepares the same payment again with the same reference, Ms. Iyer sends it and Mr. Batra authorises it again, so a late duplicate can be spotted and refused.

**The same idea covers the BEFORE's bounce.** Every morning the agent reads the bank statement and return file and matches each line. If a payment comes back, it marks the refund Returned in the ERP, updates EduDesk and tells the student **the same day**, not after month-end. It then raises the bank change and an off-cycle re-issue for Mr. Batra and Ms. Rao to approve. Lines it cannot match go to Ms. Iyer the same day, with its evidence.

## 6. What stays human

Ask Kestrel removes the running around: finding out what is owed, chasing offices, re-typing bank details, building and checking payment files, reading the bank statement, and telling people where things stand. These stay with a person:

| What | Who | Why it stays human |
|---|---|---|
| **Inspecting the room and deciding what is damage** | Mr. Joseph | It needs eyes on the room and judgement: a chair broken by misuse is a deduction; one worn out after ten years is not. |
| **Settling a dispute about a deduction** | Dr. Menon | A student who disagrees deserves to be heard by a person who can weigh both sides. |
| **Approving a bank-detail change** | Mr. Batra | Changing where money goes is a classic fraud route, so a named person checks the proof. |
| **Paying outside the calendar** | Ms. Rao | An off-cycle run is an exception to the college's own payment rules. |
| **Authorising money leaving the college** | Mr. Batra | The bank requires a registered signatory, and someone must answer for every payment. |
| **Bank lines the agent cannot match** | Ms. Iyer | When the evidence does not settle it, a person decides instead of the agent guessing. |
| **Taking back physical items** | Mr. Gill (mess card), Mr. Joseph (room key) | Someone has to receive them. |
| **Giving the agent access, and changing the rules** | College administration, HR head and Ms. Rao | Adding a second signatory, changing the payment calendar or granting access to leave dates are policy decisions. The agent follows the rules; it does not write them. |

### What the agent does not fix

- **Failure 10 (no move-in record):** nothing can be done for Aarav, who moved in in 2022 with no record. From now on the agent collects a move-in checklist with photos and compares it at move-out.
- **Failures 4 and 8 are only eased:** the agent warns three days early about the single signatory, and shows Dr. Menon the approval deadline, but adding a signatory and changing her Friday habit are human decisions.
- **Better fixed by configuration:** Failures 1, 2, 3, 5 and 7 can also be fixed by changing settings or links between systems (the table below; marked (*) in the diagram). The agent covers them until IT does. Its lasting value is the work no single system owns: talking to the student, coordinating four offices, accounts and the bank, reading the leave calendar, chasing approvals and handing exceptions to Ms. Iyer with evidence.

| Failure | Configuration fix |
|---|---|
| 2: two copies of the bank details | Send the form's verified bank details to the ERP as a bank-change request for Mr. Batra's approval; pay only to an approved account |
| 3: payment date not shown | Show the next payment-run date on the request in EduDesk |
| 5: the return can't be matched | Use the bank's return file (confirm the bank offers one), or add a matching rule that searches the free text for the UTR |
| 7: Hostel clears before the key | A hostel module rule (or vendor change): Clear only after the inspection is approved and the key is returned |
| 1: "Refund paid" after a return | Show "Payment sent" at sending and "Refund paid" only once the bank confirms; send the ERP's "returned" event to EduDesk (needs the fix for Failure 5 first) |

**The line between the two:** Ask Kestrel does the work that is the same every time and can be checked. People keep the work that needs judgement, accountability or a hand to receive something.

## 7. How Ask Kestrel connects to the college's systems

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

**How the agent itself is controlled (panel 4):** its own account with only the access above; every action logged with the values before and after; it never authorises a payment or approves a bank change; one key per request, so a retry never creates a second refund; and one switch stops all its writes.
