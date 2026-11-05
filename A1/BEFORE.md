# BEFORE: Hostel deposit refund

A realistic process, based on my own experience and what friends told me about theirs, set at a fictional college (Kestrel Institute of Technology), May–July 2025. The names, codes, amounts and exact dates are invented. No real student or staff data is used.

## The setting and the people

The diagram for this file is `BEFORE_SYSTEM_DESIGN_library_hostel_mess_labs_accounts_failures_v5.excalidraw`, laid out as three frames read left to right: the request and the four clearances (2nd–12th May), accounts, payment and the silent return (12th–23rd May), and the ticket and the recovery (28th May–17th June). The failure numbers in its red boxes match section 3.

**Kestrel Institute of Technology** is a fictional college with hostels for its students. Every student pays a Rs.15,000 hostel security deposit, refunded when they move out.

| Who | Role | What they do in this story |
|---|---|---|
| Aarav | Student, room `H3-214` | Finishes his exams, moves out on 12th May and asks for his deposit back |
| The lab assistant | Labs | Confirms Aarav has no lab equipment or lab dues |
| Mr. Joseph | Hostel caretaker | Inspects the room, records damage, takes back the room key |
| Dr. Menon | Hostel warden | Assigns room inspections and approves them (she does approvals on Fridays) |
| Mr. Gill | Mess office | Takes back the mess card `MC-3381` |
| Ms. Iyer | Accounts clerk | Runs the refund payment runs (1st and 15th of each month) and the month-end bank reconciliation |
| Mr. Batra | Accounts officer; the only signatory registered with the bank for the student-deposit account | Authorises every payment file from that account, and approves changes to bank details in the ERP |
| Ms. Rao | Finance head, Mr. Batra's manager | Can approve an off-cycle payment run; nobody asks her in this story, so she is not counted among the people in section 2 |

**The systems:** EduDesk (the student portal, with its hostel, mess and lab inventory modules, the caretaker's checklist app and the helpdesk), the library module, the Accounts ERP, the bank's corporate internet banking, email and the phone.

After this section, people are named without their roles.

## 1. The job

When a student moves out of the hostel at Kestrel Institute of Technology, they ask for their
Rs.15,000 hostel security deposit back. Before the money can be refunded, four offices (library,
hostel, mess and labs) must each confirm the student owes nothing, and the Accounts ERP
then applies any deductions and pays the balance into the student's bank account.

- **Who asks:** the student who is leaving the hostel.
- **How often:** about 600 times a year, mostly in the two weeks after end-semester exams.
- **What record it creates or changes:** a no-dues clearance request on the student portal
  (EduDesk), a refund document in the Accounts ERP, and a bank transfer to the student.

## 2. The route

What actually happened to Aarav's refund, step by step. Aarav applied on 2nd May, after his last exam, and kept living in room `H3-214` until he moved out on 12th May. Steps 2–13 are grouped by office: the four clearances ran at the same time, so their dates overlap.

| # | Date | Who | System | What they type, choose or remember |
|---|---|---|---|---|
| 1 | 2nd May | Aarav | EduDesk | Logs in; fills "No-Dues & Deposit Refund": types enrollment no., hostel code `H3-214`, bank account no. and IFSC (verified on the spot by a Rs.1 test transfer). Gets `REQ-25-0917`. |
| 2 | 2nd May | (library module, automatic) | Library module → EduDesk, email | Finds one book returned 4 days late (fine Rs.40) and posts the fine to the request as a deduction from the deposit refund. The Library line shows "Clear", with "Rs.40 to be deducted from your deposit refund", and Aarav is emailed the same details. |
| 3 | 2nd May | (EduDesk, automatic) | EduDesk lab inventory module, email | The request appears in the lab assistant's Labs worklist with an email alert. The lab inventory module shows no equipment issued to Aarav and no lab dues. |
| 4 | 6th May | Lab assistant | EduDesk, email | Reviews the worklist, confirms nothing is outstanding and marks the Labs line "Clear". Aarav is emailed. |
| 5 | 2nd May (Fri) | (EduDesk hostel module, automatic) | Hostel module, email | The request appears in Dr. Menon's hostel worklist and she gets an email alert. It is Friday evening, so she picks it up on Monday. |
| 6 | 5th May (Mon) | Dr. Menon (warden) | Hostel module | Opens her worklist and assigns the inspection of room `H3-214` to Mr. Joseph, to be done before Aarav leaves. The task appears on Mr. Joseph's phone. |
| 7 | 5th May | Mr. Joseph (caretaker) | Phone | Phones Aarav to agree a time for the inspection: 7th May, 4 PM. |
| 8 | 7th May | Mr. Joseph | Hostel module app | Inspects room `H3-214` with the checklist app; records a broken chair, Rs.500 from the damage rate card, with a photo. The charge is posted to the Hostel line as proposed, and Dr. Menon gets an email: inspection waiting for her approval. |
| 9 | 7th May | Aarav | EduDesk, email | Sees the proposed Rs.500 and the photo on his portal (also emailed, with Accept / Dispute); accepts the charge. |
| 10 | 9th May (Fri) | Dr. Menon | Hostel module | Works through her approvals (she does them on Fridays); approves the inspection. The Hostel line shows "Clear" with the Rs.500 deduction recorded. |
| 11 | 12th May | Mr. Joseph | Hostel module app | Aarav's last day: he returns his room key; Mr. Joseph marks the room vacated. |
| 12 | 2nd May | (EduDesk mess module, automatic) | Mess module, email | The request appears in Mr. Gill's mess worklist with an email alert. Mess card `MC-3381` is still active, so Aarav's portal shows: "Mess: pending, return mess card `MC-3381` at the mess office." No dues are outstanding. |
| 13 | 12th May | Mr. Gill (mess) | Mess module | Aarav's last day: he returns his mess card at the mess counter (he needed it to eat until then). Mr. Gill marks `MC-3381` returned; the Mess line shows "Clear" and Aarav is emailed. |
| 14 | 12th May | (EduDesk, automatic) | EduDesk, email | All four lines are clear, so the request is forwarded to Accounts automatically: "Forwarded to Accounts". Aarav is emailed. |
| 15 | 12th May (Mon) | (Accounts ERP, automatic) | Accounts ERP, EduDesk | The ERP creates refund document `RV-25-1184` for Rs.14,460 (Rs.15,000 deposit minus the Rs.500 hostel deduction and the Rs.40 library fine). It takes the bank account from Aarav's **student master record**: the account he added at admission in 2022, which he closed in 2024. The verified account on his refund form stays on the request in EduDesk and is never sent to the ERP: the bank fields were added to the refund form in a later EduDesk update, and the EduDesk-to-ERP link was never changed to carry them. Status: waiting for the payment run. EduDesk shows "Forwarded to Accounts", with no expected date. |
| 16 | 15th May (Thu) | Ms. Iyer (accounts) | Accounts ERP, corporate internet banking | Runs the refund payment run (the 1st and 15th of each month), which turns the refunds due, including `RV-25-1184`, into a payment file, and uploads it to the college's corporate internet banking. Refunds are paid from a separate student-deposit bank account. The file waits as "pending authorisation": the bank never lets the person who prepared a file authorise it, and Mr. Batra, the only authorised signatory registered for that account, is on leave until 20th May. |
| 17 | 22nd May (Thu) | Mr. Batra (accounts officer, authorised signatory) | Corporate internet banking | Back from leave on 21st May, he works through his backlog and authorises the payment file the next morning. |
| 18 | 22nd May (Thu) | (bank and Accounts ERP, automatic) | Bank → Accounts ERP, EduDesk, email | The bank processes the payment. The bank's acknowledgement returns the UTR; the ERP marks `RV-25-1184` "Paid", EduDesk shows "Refund paid" with the UTR, and Aarav is emailed that Rs.14,460 was sent. |
| 19 | 22nd May (Thu) | (bank, automatic) | Bank | Returns the payment within hours (NEFT returns must be made within 2 hours): the account is closed. The money goes back to the college's account. The statement line shows a short return reason code and the bank's own reference; the original UTR appears only in its free-text description. |
| 20 | 23rd May (Fri) | (Accounts ERP, automatic) | Accounts ERP | Imports the previous day's bank statement, as it does every working morning. The return line carries the original UTR only in its free-text description. The ERP can be set up to search that text, but Kestrel's matching rules only look at the amount and reference fields, so it cannot be matched automatically and goes to the reconciliation exceptions queue. The refund still says "Paid" and EduDesk still says "Refund paid". **Nobody is told.** |
| 21 | 28th May (Wed) | Aarav | EduDesk helpdesk | No money has arrived; raises a helpdesk ticket quoting `REQ-25-0917` and the UTR. |
| 22 | 2nd June (Mon) | Ms. Iyer | Accounts ERP, helpdesk | Month-end bank reconciliation: matches the return to `RV-25-1184` through the UTR and marks it "Returned". Answers the ticket: the refund went to the closed account on his student record and will be paid to the account on his refund form. |
| 23 | 2nd June | Ms. Iyer | Accounts ERP | Re-types the bank account from the verified refund form into Aarav's ERP student record by hand. Bank details are a protected field, so the change waits for Mr. Batra to approve it. |
| 24 | 3rd June (Tue) | Mr. Batra | Accounts ERP | Checks the change against the form's Rs.1 test transfer and approves it. |
| 25 | 16th June (Mon) | Ms. Iyer | Accounts ERP, corporate internet banking | Next payment run (the 15th was a Sunday); re-issues `RV-25-1184` to the corrected account and uploads the payment file for authorisation. |
| 26 | 16th June | Mr. Batra | Corporate internet banking | Authorises the payment file with the re-issued refund. |
| 27 | 17th June (Tue) | (bank and Accounts ERP, automatic) | Bank → Accounts ERP, EduDesk, email | Payment processed and credited the same day. EduDesk shows "Refund paid" with the new UTR; Aarav is emailed and gets a bank SMS. |

### Counts

| What | Count | How it was counted |
|---|---|---|
| Steps | 27 | every row above |
| Systems | 6 | EduDesk (with its hostel, mess and lab inventory modules, the caretaker's app and the helpdesk), library module, Accounts ERP, the bank's corporate internet banking, the bank itself (it processes and returns the payment), phone. Email only carries notifications, so it is not counted |
| People | 7 | Aarav, lab assistant, Mr. Joseph, Dr. Menon, Mr. Gill, Ms. Iyer, Mr. Batra |
| Codes | 9 | enrollment no., `H3-214`, bank account no., IFSC, `REQ-25-0917`, `MC-3381`, `RV-25-1184`, the UTR, the return code `RTN-03`: each typed, read or quoted by someone |
| Hand-offs | 14 | each time the next step is done by a different person from the step before (automatic steps by the system and the bank are not counted) |
| In-person visits | 1 | mess counter, to return the card (the room inspection and the key return happen in the hostel, as part of moving out) |
| Times bank details were typed | 2 | Aarav on the refund form (step 1); Ms. Iyer copying them into the ERP student record by hand (step 23) |

## 3. Failure points

One of each type the brief asks for: Failure 1 is the **silent outcome**, Failure 5 the **error that does not help**, and Failure 2 the **rule that lives in someone's head**.

**The main ones (1–6)**

### Failure 1 (silent outcome): "Refund paid" when the money came back

- **What happened:** On 22nd May EduDesk showed "Refund paid" with a UTR, and Aarav was emailed that Rs.14,460 had been sent. Within hours the bank returned it because the account was closed. He only learned the truth from the helpdesk reply on 2nd June. Even then, EduDesk still said "Refund paid" after Ms. Iyer marked the refund Returned on 2nd June: the refund status in EduDesk is set only by the ERP link, which sends "paid" but never "returned", and staff cannot edit it. It stayed wrong until the re-issued payment went through on 17th June.
- **What Aarav sees:** EduDesk says "Refund paid" with the UTR, and an email says Rs.14,460 was sent to his bank. Nothing ever says it came back.
- **Who noticed, and when:** The ERP put the return in the exceptions queue on 23rd May, but nobody looks at that queue until month-end, and nothing told Aarav or updated EduDesk. Only Aarav acted, raising a ticket on 28th May.
- **What it cost:** Aarav did not know the payment had come back for 11 days (22nd May → 2nd June). The status page was wrong for 26 days (22nd May → 17th June): anyone who checked it, Aarav or staff, saw "Refund paid" with a UTR for money that had come back. In all, 46 days instead of about 20.
- **Why:** The ERP sends EduDesk the "paid" event but not the "returned" event, and the return was not matched to the refund until month-end (Failures 5 and 6).
- **What you would need to know to avoid it:** "Refund paid" only means the college sent the money. Check your bank account within a day, and raise a ticket at once if nothing has arrived.

### Failure 2 (rule in someone's head): two copies of the bank details, and the payment used the stale one

- **What happened:** Aarav entered his current account on the refund form on 2nd May, and it was verified. But the ERP created the refund from his student master record, which still held the account he added at admission in 2022 and closed in 2024.
- **What Aarav sees:** nothing. The form shows his verified account; no screen shows which account the ERP will actually pay.
- **What it cost:** The bounce, and everything after it.
- **Why:** The link from EduDesk to the ERP sends student master data, not the bank fields on the request. The bank fields were added to the refund form in a later EduDesk update; the EduDesk-to-ERP link was never changed to carry them. Each system was right about its own copy.
- **What you would need to know to avoid it:** what only the accounts staff know: the refund is paid to the bank account on the ERP student record, not the one typed on the refund form. A student who knew would ask accounts to update the record first.

### Failure 3: the payment calendar is not visible to the student

- **What happened:** Refunds go out only in the payment runs on the 1st and 15th. The calendar lives in the finance system; EduDesk just said "Forwarded to Accounts", with no date.
- **What Aarav sees:** "Forwarded to Accounts", with no date.
- **What it cost:** 3 days the first time (12th → 15th May) and 14 days after the return (2nd → 16th June), with Aarav not knowing either time. The ERP allows off-cycle payments with the approval of the finance head (Ms. Rao), but nobody asked for one, so the re-issue waited for the next run.
- **What you would need to know to avoid it:** refunds go out only on the 1st and 15th, and the finance head can approve an off-cycle run. Both are known only to accounts staff.

### Failure 4: only one authorised signatory registered for the student-deposit account

- **What happened:** Refunds are paid from a separate student-deposit bank account. Every payment file from it must be authorised by a signatory registered with the bank for that account, and the bank never lets the person who prepared a file authorise it. Ms. Iyer prepared and uploaded the run on 15th May, but Mr. Batra, the only signatory registered for this account, was on leave until 20th May. Salaries and supplier payments go from the college's other accounts, which have other signatories, so only refunds were held up. Adding a second signatory needs bank paperwork (a board resolution and signature forms), so nobody could step in. He authorised the file on the morning of 22nd May.
- **What people see:** Ms. Iyer sees the file as "pending authorisation" in internet banking; Aarav sees nothing at all.
- **What it cost:** 7 days (15th → 22nd May), and every refund in that run waited with Aarav's.
- **Why:** The control itself is sound (one person prepares, another authorises), but with only one authorised person it becomes a single point of failure.
- **What you would need to know to avoid it:** who the only signatory is and when he is on leave, so the run can be done before he leaves.

### Failure 5 (error that does not help): the matching rules can't read the returned payment

- **What happened:** The bank's return line carried a short reason code and the bank's own reference, not `RV-25-1184`. The return line carries the original UTR only in its free-text description. The ERP can be set up to search that text, but Kestrel's matching rules only look at the amount and reference fields, so it could not be matched automatically and sat in the exceptions queue unexplained.
- **What Ms. Iyer sees:** one line in the exceptions queue, `UNMATCHED CR 14,460.00 · RTN-03 · KTB/N22052025/0419`, with no refund number and no explanation of the code.
- **What it cost:** It needed a person to find and match it by hand.
- **What you would need to know to avoid it:** RTN-03 is the bank's code for "account closed", and the original UTR sits in the line's free-text description, so searching for the UTR finds the refund.

### Failure 6: exceptions wait for the month-end reconciliation

- **What happened:** The unmatched return sat in the queue from 23rd May until Ms. Iyer's month-end reconciliation on 2nd June. Aarav's ticket waited with it, past the helpdesk's 2-working-day response target (due 30th May, answered 2nd June).
- **What people see:** nothing until month-end; nobody opens the queue in between.
- **What it cost:** 10 days in the queue (23rd May → 2nd June).
- **What you would need to know to avoid it:** the exceptions queue is only looked at during month-end reconciliation, so a missing refund needs a ticket to get attention sooner.

**Smaller ones (7–10): they cost little or nothing this time**

### Failure 7: the Hostel line is cleared before the key is returned

- **What happened:** The room was inspected on 7th May and the Hostel line went "Clear" on 9th May, but Aarav lived there until 12th May and returned his key that day. Nothing ties the clearance to the key return.
- **What people see:** the Hostel line shows "Clear" on 9th May, three days before the key comes back.
- **What it cost:** Nothing this time. But any damage between 7th and 12th May would never have been charged, and a student who left without returning the key would already have been cleared.
- **Why:** The hostel module treats the approved inspection as the end of the hostel's part. The key return is recorded separately and nothing links the two.
- **What you would need to know to avoid it:** hostel staff would have to remember to keep the line open until the key is back; nothing on the screen reminds them.

### Failure 8: approvals wait for the warden's Friday session

- **What happened:** Dr. Menon got an email the moment the inspection was submitted on 7th May, but she does her approvals on Fridays, so she approved it on 9th May.
- **What people see:** Dr. Menon gets an email; Aarav sees "Hostel: waiting for approval".
- **What it cost:** 2 days. It did not change the outcome this time, because the request was waiting for the Mess line until 12th May anyway.
- **Why:** The system notifies, but the person batches. An approver who receives many of these emails works through them in one weekly session.
- **What you would need to know to avoid it:** Dr. Menon approves on Fridays, so an inspection done early in the week waits until Friday.

### Failure 9: the inspection is arranged by phone, outside the system

- **What happened:** The system gave Mr. Joseph the inspection task, but he and Aarav agreed the time by phone.
- **What people see:** a phone call; nothing in EduDesk.
- **What it cost:** Nothing this time. But nothing records the agreed time, so a missed call or a forgotten slot would delay the inspection with no trace in the system.
- **What you would need to know to avoid it:** write the agreed time down somewhere, because the system has no place for it.

### Failure 10: no move-in record to compare against

- **What happened:** The Rs.500 charge for the broken chair rests only on the 7th May inspection. There is no record of the room's condition when Aarav moved in.
- **What Aarav sees:** the Rs.500 charge with a photo of the broken chair.
- **What it cost:** Nothing this time, because Aarav accepted the charge. Had he said the chair was already broken when he moved in, neither side could have proved it.
- **What you would need to know to avoid it:** photograph the room on the day you move in.

## 4. Cost

### First time (what actually happened)

| Measure | Value |
|---|---|
| Elapsed time, application to money received | **46 days** (2nd May → 17th June) |
| Aarav's hands-on time | **about 1 hour 35 minutes** |
| Staff hands-on time (all 6 staff together) | **about 1½ hours** |
| Visits in person | 1 (mess counter) |
| Helpdesk messages written by people | 2 (Aarav's ticket, Ms. Iyer's reply; automatic emails from the system not counted) |
| Times the same refund was authorised | 2 |

Aarav's 1 hour 35 minutes, broken down:

| Activity | Time |
|---|---|
| Filling in the EduDesk form | 20 min |
| Checking the status page and his emails | 15 min |
| Inspection call, being present for the inspection, accepting the charge | 20 min |
| Returning the mess card at the counter | 10 min |
| Checking his bank account after the "Refund paid" email (22nd–28th May) | 20 min |
| Raising the helpdesk ticket | 10 min |
| **Total** | **1 h 35 min** |

### Careful path (someone who knows every trap)

A student who knew every rule would:
- agree the earliest possible inspection time when the caretaker calls,
- make sure the bank account on their student record is current, not only the one on the form,
- time the application so all clearances finish before a payment run (1st or 15th).

| Measure | Value |
|---|---|
| Hands-on time | **about 1 hour** |
| Elapsed time | **14–21 days** |

Why still 14–21 days: some waits cannot be avoided by knowing the rules. The warden approves only on Fridays, the mess card can only be returned on the last day, refunds go out only on the 1st and 15th, and a payment run waits if the only bank signatory is away. That gives about 14 days if the signatory is in, and about 21 days if he is away, as he was.

**Knowing the traps cut the hands-on time by more than a third and removed the 26-day delay from the bounce, but the process still takes two to three weeks.**

### Where the 46 days went

| Stretch | Days |
|---|---|
| Four offices clearing at their own pace (2nd → 12th May) | 10 |
| Waiting for the 15th payment run (12th → 15th May) | 3 |
| Waiting for the only signatory (15th → 22nd May) | 7 |
| Payment sent, returned by the bank and imported by the ERP (22nd → 23rd May) | 1 |
| Return in the exceptions queue until month-end reconciliation (23rd May → 2nd June) | 10 |
| Waiting for the next payment run (2nd → 16th June) | 14 |
| Payment sent and credited (16th → 17th June) | 1 |
| **Total** | **46** |

**About 3 hours of actual work, by everyone together, was spread across 46 days. The rest was waiting: for a payment run, a signatory, a reconciliation, or for someone to notice.**

### How these were estimated

- **Timeline:** how long each stage took (the offices clearing, waiting for a payment run, waiting for the signatory, a returned payment sitting until month-end) comes from my own experience and my friends' accounts. The exact dates are set to fit those stages, so they are illustrative, not recorded.
- **Aarav's hands-on time:** a rough guess per activity from those accounts, ±30 minutes in total.
- **Staff hands-on time:** a rough guess per step (for example 5 minutes for an office to mark its line Clear, 15 minutes for a room inspection, about 20 minutes to find and match a returned payment), ±50%.
- **Careful path:** reasoned from the fixed rules in the route (Friday approvals, the last-day card return, the 1st/15th payment runs, about a day for a transfer), assuming everything else goes right. It is a best case, not a measurement.
- **Where the 46 days went:** each gap between one step and the next in the route, in days.
