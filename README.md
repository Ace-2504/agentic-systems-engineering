# Agentic Systems Engineering

Designing AI agents that work **on top of** the systems companies already run (ERPs, student portals, old in-house software) instead of replacing them. The hard part isn't the chat. It is that these systems say "paid" when the money came back, record approvals nowhere, and keep their rules in people's heads. The designs here deal with that, and keep a named person approving every change.

**Highlights**
- **The silent "paid", traced end to end.** A refund the portal showed as paid for 26 days while the money sat back with the college, and an After where "paid" is said only once the bank statement confirms it.
- **Human approval built in.** The agent drafts every entry; the right person approves or amends it within 24 hours; every amendment is reported; nothing is written without a recorded yes.
- **Agents on old systems.** For a company with no API, only an XML interface and shared logins: an adapter, a read-only database copy, and an approval gateway that rebuilds the controls a modern ERP gives for free.

**Start here:** for a two-minute look, read [`A1/CAPSTONE.md`](A1/CAPSTONE.md) (half a page) and open the [capstone board](A1/CAPSTONE_SYSTEM_DESIGN_v13.png).

This is my coursework for a cohort course on agentic systems engineering (see Credits), so the repository grows one assignment at a time.

> **Everything here is fictional.** The college, the companies, the people, the codes, the amounts and the dates are invented for the assignments. No real student, staff, customer or supplier data is used.

## Contents

| Folder | Assignment | Status |
|---|---|---|
| [`A1/`](A1) | A1 · Your Before, and the After you want | Submitted |
| [`A2/`](A2) | A2 · How a brain would read your work | Submitted |
| `A3/` … `A7/` | The knowledge, the tools over MCP, the harness, a workflow, the trust layer | To come |

## A1 · Before and After

Two stories, two levels of detail.

**1. A process I know from experience, and from friends who went through it: getting a hostel deposit refunded** (Kestrel Institute of Technology, a fictional college). A student asks for a Rs.15,000 deposit back; four offices must clear him, accounts pays, and the bank sends the money back because the ERP used an old, closed account. The portal says "Refund paid" the whole time. It takes 46 days.

| Part | What it covers | File | Diagram |
|---|---|---|---|
| Part 1 · The Before | the job, all 27 steps with who, where and what they type, the counts, ten failure points (one silent outcome, one unhelpful error, one rule that lives in someone's head) and a rough cost estimate that says how it was made | [`BEFORE.md`](A1/BEFORE.md) | [PNG](A1/BEFORE_SYSTEM_DESIGN_library_hostel_mess_labs_accounts_failures_v5.png) |
| Part 2 · The After | the same process with an agent ("Ask Kestrel"): what the student says, previews, approvals, checkable proof, two ways it fails, and what stays human | [`AFTER.md`](A1/AFTER.md), with the technical side in [`AFTER_integration.md`](A1/AFTER_integration.md) | [PNG](A1/AFTER_SYSTEM_DESIGN_v7.png) |
| Part 3 · NB1 | the course notebook, run top to bottom: exercises 1–5 solved by hand, exercise 6 holds the Before above, and the two answers are in the last cell | [`NB1_before_and_after.ipynb`](A1/NB1_before_and_after.ipynb) | |

**2. The capstone: accounts payable at Northbridge Cycles**, built on the course's *Finance · payables* module kit. A supplier's Rs.2.83 crore invoice is held twice (price and quantity); today a 0.5% early-payment discount is lost while it waits, and the ERP says "paid" before the bank does. With the assistant, the holds go to the right people the same day, every entry it drafts is approved by a person within 24 hours, the discount is weighed against what Treasury says the money would earn (here it loses, so the financial controller declines it), GST credit is claimed only after GSTR-2B confirms it, reverse-charge GST and TDS are paid on time, and "paid" is said only after the bank statement confirms it.

| Part | What it covers | File | Diagram |
|---|---|---|---|
| Part 4 · Capstone sketch | the half-page sketch the brief asks for: process and people, sandbox, five activities, two never-events, open questions | [`CAPSTONE.md`](A1/CAPSTONE.md) | [PNG](A1/CAPSTONE_SYSTEM_DESIGN_v13.png) |
| Part 4 · Full design | the design behind the sketch: the people, the money, the approval loop, the morning bank check, the tax steps (GST credit check, reverse charge, TDS), guardrails against common attacks, tests, and what changes without new code | [`CAPSTONE_design.md`](A1/CAPSTONE_design.md) | |
| Extra · Legacy version | the same capstone when the company has no ERP API, only an old in-house system with an XML interface and shared logins: an adapter in front of it, a read-only database copy, and an approval layer that rebuilds every control the ERP gave for free | [`CAPSTONE_legacy.md`](A1/CAPSTONE_legacy.md) | [PNG](A1/version_legacy_v5.png) |

The three small images (`Before_Scorecard.png`, `After_Scorecard.png`, `How_It_Felt.png`) are my results from the course's Lecture 1 exercise, where I placed the same order by hand and then with the reference assistant.

## A2 · How a brain would read your work

The same Kestrel hostel refund, seen through a language model with no tools. The source text is a one-and-a-half-page refund policy I wrote for the fictional college, consistent with A1's Before: [`KESTREL_REFUND_POLICY.md`](A2/KESTREL_REFUND_POLICY.md).

| Part | What it covers | File |
|---|---|---|
| Part 1 · Tokens | the policy through Qwen's tokenizer (4,073 characters, 1,100 tokens), the ten words and codes cut into the most pieces and why that matters, words versus tokens, and a cost estimate with its working and assumptions | [`TOKENS.md`](A2/TOKENS.md) |
| Part 2 · Where it invents | three real refund questions; one asked four times to Gemini 3.8 Flash with search and tools off, exact replies pasted; one invented detail traced through the input, the next-token game, training and the cut-off; the most dangerous question | [`INVENT.md`](A2/INVENT.md) |
| Part 3 · Facts it needs | every fact the three questions need and where it lives, sorted into documents (Lecture 3) and live lookups (Lecture 4), and a real test with one fact added to the prompt | [`FACTS.md`](A2/FACTS.md) |
| Part 4 · NB2 | the course notebook, run top to bottom in Colab: six exercises solved, my policy in the last cell with a ranking cell after it, and the two answers in the last cell | [`NB2_the_brain.ipynb`](A2/NB2_the_brain.ipynb) |

## How to read the diagrams

Each diagram is a board of frames that reads left to right: an overview first, then the steps phase by phase, with **red** notes for what goes wrong today and **green** notes for what the design fixes.

- **Quick look:** open the `.png` next to each diagram.
- **Full detail:** open the `.excalidraw` file at [excalidraw.com](https://excalidraw.com) (menu → Open) or with the Excalidraw extension for VS Code. The frames list lets you jump between frames or present them one at a time.

## Running the notebooks

`NB1_before_and_after.ipynb` and `NB2_the_brain.ipynb` install the course's sandbox ERP in their first cell and run in **replay mode**: they play back recorded model replies, so they need no API key. They are meant for Google Colab (Runtime → Run all); locally they need Python 3.10 or newer and git. NB2 also downloads a small open model (Qwen2.5-0.5B-Instruct, about 1 GB) and trains a tiny GPT on CPU, which takes about 25 minutes.

## Credits

The course, the Ledgerline sandbox ERP, the payables module kit and the NB1 and NB2 notebooks are by Dr. Rajat Dandekar and Vizuara: [RajatDandekar/agents-for-enterprises](https://github.com/RajatDandekar/agents-for-enterprises). The notebooks here are the course's NB1 and NB2 with my own solutions and additions. The process write-ups, the refund policy, the capstone design and the diagrams are my own work.

## Licence

My own write-ups and diagrams in this repository are licensed under [Creative Commons Attribution 4.0 (CC BY 4.0)](LICENSE): you may reuse them with credit. The course materials (the NB1 and NB2 notebooks, the Ledgerline sandbox, the payables module kit and the names and data that come from them) belong to Dr. Rajat Dandekar and Vizuara and are **not** covered by this licence.
