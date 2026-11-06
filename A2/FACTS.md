# FACTS: what the model would need to answer correctly

**A2 · Part 3** · Questions Q1–Q3 from [`INVENT.md`](INVENT.md). Systems and people are those of my A1 Before ([`../A1/BEFORE.md`](../A1/BEFORE.md)).

## 1. The missing facts

| Question | Fact needed | Where it lives today |
|---|---|---|
| **Q1** Has my refund been paid? | the request's current status and its four clearance lines | **EduDesk** (the request, and its hostel, mess and lab modules) and the separate **library module** |
| Q1 | whether a refund voucher exists, its amount and its status (waiting, paid, returned) | **Accounts ERP** (refund voucher `RV-…`) |
| Q1 | whether the bank actually credited the money or sent it back | **the bank statement**, imported into the Accounts ERP; a returned payment sits in the **reconciliation exceptions queue** until someone matches it |
| Q1 | what "Refund paid" on EduDesk really means | **the policy** (5.3) says the money has reached the student, but the **ERP link** sends "paid" as soon as the bank processes the payment and its acknowledgement returns the UTR, before anyone knows whether the student's bank accepted it; it never sends "returned" (A1, steps 18–20, failure 1) |
| **Q2** How much for a lost key? | the charge for a lost room key (Rs.750, lock change included) | **the policy, Annexure A**: an extract of the Damage Rate Card |
| Q2 | whether that rate is this year's | the **full rate card displayed in each hostel office**; the extract is for 2024-25, and charges are "reviewed every academic year" |
| Q2 | whether a lost key was actually recorded against Aarav's room | **the hostel module** (inspection and key return) |
| **Q3** On what date will the money arrive? | the date the request reached Accounts | **EduDesk** ("Forwarded to Accounts") |
| Q3 | that refunds are paid only in runs on the 1st and 15th (in A1, the run due on Sunday the 15th went out on Monday the 16th) | **the finance system's payment calendar**, known to Accounts staff. Students cannot see it, and the policy only says "normally within 30 working days" |
| Q3 | whether the only signatory for the student-deposit account is available | **the Accounts staff's knowledge of Mr. Batra's leave**; no system or document in A1 records it. He is the only person registered with the bank (A1, failure 4) |
| Q3 | that an off-cycle payment run is possible with the finance head's approval | **Ms. Rao's and the Accounts staff's heads**; A1 says only Accounts staff know it (failure 3) |
| Q3 | which bank account the ERP will pay | the **ERP student master record**, *not* the verified account on the refund form (A1, failure 2) |
| Q3 | how long NEFT takes to credit | **the policy** (5.3: "up to 2 working days") |

## 2. Knowledge or tools

| Fact | Knowledge or tools | Why |
|---|---|---|
| Request status and clearance lines | **Tools** | changes several times a week and differs for every student; must be read from EduDesk at the moment of the question |
| Refund voucher amount and status | **Tools** | created and updated by Accounts; only the ERP knows its state right now |
| Whether the bank credited or returned it | **Tools** | changes within hours (a NEFT return comes back the same day); must come from the imported bank statement, not from EduDesk's status |
| What "Refund paid" means | **Knowledge**, but the document must be **corrected first** | it changes only when the process changes, so it belongs in documents. Today the policy's wording is wrong, so retrieving it would make the assistant repeat the error |
| Lost-key charge | **Knowledge** | a written rule that changes once a year; retrieve the clause from the policy |
| Whether the rate card is current | **Knowledge**, if the current card is published | the yearly card is displayed in hostel offices; it has to be put into the document store each year, or the assistant will quote last year's rates |
| Whether a lost key was recorded for Aarav | **Tools** | specific to one student and one inspection; lives in the hostel module |
| Date forwarded to Accounts | **Tools** | one student's live record in EduDesk |
| Payment runs on the 1st and 15th | **Knowledge**, once **published** | it is a stable rule that changes rarely, so it belongs in documents. Today it sits only in the finance system's calendar, which students and their assistant cannot see; Accounts would have to publish it (or give the assistant read access to that calendar) first |
| Signatory availability | **Neither yet**, then **tools** | it changes week to week, so it must be looked up live. But today no system records it, only people's knowledge, so Accounts would first have to keep a leave or authorisation calendar the assistant can read |
| Off-cycle runs with the finance head's approval | **Knowledge**, once **written down** | a stable rule, but unwritten; like the payment calendar, it must be documented before any assistant can use it |
| Which bank account the ERP will pay | **Tools** | one student's master record; it is exactly the fact that went wrong in A1 |
| NEFT credit time | **Knowledge** | a stable banking rule, already in the policy |

**The two hard cases.** First, a fact that lives only in people's heads (the off-cycle rule, the signatory's leave) is neither knowledge nor a tool yet, and one that sits in an internal system students cannot see (the payment calendar) is not usable either. Someone has to write it down or publish it before Lecture 3 can retrieve it. Second, when the written rule and the system disagree ("Refund paid" means credited; the refund goes to the account on the form), the system is what actually happens to the money. So for "what will happen to *my* refund" the assistant must use tools, and the policy has to be fixed so that knowledge and tools tell the same story.

## 3. Test it

**Question:** Q1, "Has my hostel deposit refund been paid yet? My request number is REQ-26-0417."

Same model and settings as Part 2 (Gemini 3.8 Flash in AI Studio, search and all tools off, thinking Medium), new chat. I added one fact line at the end of the same system prompt, the way NB2 exercise 6 adds the Ledgerline stock line. It holds what EduDesk and the ERP would actually show:

**Fact line added to the system prompt:**

```
EduDesk, REQ-26-0417: Forwarded to Accounts on 2 Nov 2026. Accounts ERP, refund voucher RV-26-0611: Rs.14,460, status Waiting for payment run.
```

AI Studio counted the prompt as 159 tokens (100 without the fact). The whole exchange came to 504 tokens.

**Exact reply:**

```
No, your refund has not been paid yet.

Your request (REQ-26-0417) was forwarded to Accounts on 2 November 2026. Refund voucher RV-26-0611 for Rs. 14,460 has been generated and is currently waiting for the scheduled payment run.
```

**What happened.** It used the fact, all of it: the date, the voucher number and the amount are all correct (it rewrote "2 Nov 2026" as "2 November 2026" and "Rs.14,460" as "Rs. 14,460"), and it opens with a plain "No". The invented details from Part 2 are gone: no "7 to 10 working days", no "Finance tab", no claim that clearance was approved. It added very little. "Has been generated" is a fair reading of a voucher existing, and "**scheduled** payment run" adds the idea that a run is scheduled, which the fact does not say. It did not invent a date. But that means the answer is correct and still not useful for the question Aarav really has (Q3, *when*). The payment calendar was not in its input, so an honest model can only say "waiting". The fact line is also only as true as EduDesk. In A1, EduDesk said "Refund paid" while the money had come back. If that line had been the fact, the model would have repeated it faithfully. In A1 the ERP's refund status also still said "Paid" until the return was matched by hand. So the fact must come from the record that actually knows (the imported bank statement line, matched to the refund voucher), not from a status that summarises it.
