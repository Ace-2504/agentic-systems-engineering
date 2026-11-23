# TOOL.md: `explain_hold`

A read-only tool that says why a supplier invoice is on hold, who may clear each hold, and by when it must be cleared to be paid on time.

**The data.** Northbridge Cycles, Pune, from my capstone (`A1/CAPSTONE.md`): Voltway Cells' invoice 4471 for 18,000 battery packs. The course's Ledgerline sandbox (module `fin_payables`) runs unchanged. `capstone_seed.py` rewrites only the records this tool reads, so they carry my capstone's figures (Rs., IGST, 260 damaged and 40 defective packs). The sandbox date is Monday 26th October 2026: in the capstone's "today" story, both holds are still open and Voltway has just called Emma. Every name, number and GSTIN is made up.

## 1.1 The job

**The questions people ask**

| # | Who asks | Question |
|---|---|---|
| 1 | Emma Clarke, purchasing, after Voltway's call on 26th Oct | "Why is Voltway's invoice 4471 on hold, and can we pay it Friday?" |
| 2 | Priya Shah, accounts payable | "Who has to clear the holds on 4471, and by when?" |
| 3 | Ganesh Pawar, stores | "Is anything on 4471 waiting on me?" |

**Why the existing screen does not answer them**

- **The list shows one hold, but there are two.** On FIN-AP-03, Search shows 4471 as `HD` with `H-QTY`. The price hold (`H-PRC`) only shows up after pressing Details.
- **The codes don't say what is wrong.** The gaps ("18,000 billed, 17,700 accepted" and "Rs.1,332.80 against the order's Rs.1,276.80, +4.39%") are in the hold log, behind Details.
- **Two suppliers sent an invoice numbered 4471.** Voltway Cells (Rs.2,83,08,672) and Voltway Paints & Coatings (Rs.2,17,120). Asked about "Voltway's 4471", the user has to notice there are two rows and pick the right one.
- **No screen shows who may release a hold.** That lives in table `ap_hold` and in AP policy section 4.1. Today a person finds out by pressing Release and getting `ERR-AP-0305`.
- **No screen says "by when".** The invoice is due on Monday 16th November, so the last Friday run before it is the 13th, with a Thursday 12th cut-off. Nobody puts those dates next to the holds.
- **"Can we pay it Friday?" has no answer on the screen.** It shows the status, not the rule: no payment, early or not, while the invoice is on hold.
- **The shipped tool `invoice_status` gives only the status.** It says "on hold", not why, who clears it or by when.

**Read or write:** read only. The tool never refers or releases a hold. Those are the write services `ap_hold_refer` and `ap_hold_release`, kept for my later tool `refer_hold`, behind an approval.

## 1.2 The services

**Where I looked**

- `fin_payables/data-dictionary.md`: the module's service catalogue (name, legacy title, read/write, screen, fields).
- `fin_payables/services.py`: the `@service(...)` registrations.
- `fin_payables/procs.py`: the stored procedures (`sp_ap_*`).
- `screens/FIN-AP-03.yaml`: which button calls which service.
- The shared services (`usr_get`, `usr_roles`, `sup_get`, `pt_list`).

**Candidates**

| Service | Kind | Chosen? | Why |
|---|---|---|---|
| `ap_inv_list` | read | **Yes** | Turns the supplier's printed number (4471) into our AP number, and shows that two suppliers share it. |
| `ap_inv_get` | read | **Yes** | The one call with every hold in the log (detail, date put on, released or not), the order rate, the goods receipt quantities, the due date, age and MSME flag. |
| `usr_get` | read | **Yes** | Checks that the person named for a hold still has that role, and gives their name ("Ganesh Pawar, STORES"). |
| `usr_roles` | read | No | Lists the services one user may call. It does not list who holds a role. |
| `sup_get` | read | No | `ap_inv_list` already returns the supplier name. |
| `ap_match` | read | No | It is a read, but it creates a match token as a side effect, and the hold log already has its result. |
| `ap_hold_refer`, `ap_hold_release` | write | No | This tool only reads. |
| `ap_save`, `ap_approve`, `ap_pay_sched`, `ap_pay_run` | write | No | Not about holds, and all writes. |

**What is missing.** Three answers have no read service:

1. **Which role may release each hold.** Table `ap_hold` is read only inside `sp_ap_hold_auth`, when someone tries to release.
2. **Who holds that role.** No service finds users by role.
3. **The payment run dates.** Table `ap_run` is used only by the write services.

So the tool keeps one small table from AP policy POL-AP-001 v2.1, section 4.1, with the policy version and date:

| Hold | Meaning | Who may release |
|---|---|---|
| H-PRC | Invoice rate more than 2% above the order rate | Daniel Okafor (`DOKAFOR`, purchase manager), or Vikram Nair (`VNAIR`, financial controller) |
| H-QTY | Billed quantity more than the accepted quantity | Ganesh Pawar (`GPAWAR`, stores), or Vikram Nair |
| H-GRN | No goods receipt | Accounts payable, once the receipt is posted; or Vikram Nair |
| H-DUP | Looks like a duplicate | Vikram Nair only |

The tool calls `usr_get` on each named person. If their role no longer matches, it says so instead of naming them. The run dates follow the payment policy's rule (every Friday, cut-off Thursday), so they are worked out, not looked up. The integration service account is never named, even though Ledgerline would let it release anything. The proper fix is to ask the vendor for an `ap_hold_list` read service. Until then, this table can go out of date without anyone noticing.

**One real definition** (catalogue row, then its registration):

```
| `ap_inv_get` | AP INVOICE GET | read | FIN-AP-03 | ap_no*:str |
```

```python
@service("ap_inv_get", "AP INVOICE GET", [F("ap_no", req=True, desc="AP NO")], screen=SCR_HOLD)
```

**One real raw reply**, in the system's own envelope: `ap_inv_get`, `ap_no="AP/2026/03390"`, 980 bytes.

```json
{"rc": "S", "err_cd": null, "msg": "", "data": {"ap_no": "AP/2026/03390", "inv_type": "PO", "sup_cd": "VC-EIN-0042", "sup_inv_no": "4471", "inv_dt": "2026-10-02", "po_no": "PO/2026/01120", "qty": 18000, "rate": 1332.8, "basic": 23990400.0, "tax_cd": "IGST18", "tax": 4318272.0, "gross": 28308672.0, "cc_cd": "PRD-05", "status": "HD", "hold_cd": "H-QTY", "due_dt": "2026-11-16", "entered_by": "PSHAH", "entered_on": "2026-10-05T15:05:00", "approved_by": null, "warn_cd": null, "client_ref": null, "holds": [{"hold_cd": "H-QTY", "detail": "QTY 18000 VS OPEN 17700", "put_on": "2026-10-05T15:05:00", "released_by": null, "released_on": null, "reason": null}, {"hold_cd": "H-PRC", "detail": "RATE 1332.80 VS PO 1276.80 (+4.39%)", "put_on": "2026-10-05T15:05:00", "released_by": null, "released_on": null, "reason": null}], "pays": [], "grns": [{"grn_no": "GRN/2026/07804", "qty_rcvd": 18000, "qty_acc": 17700, "grn_dt": "2026-10-02"}], "age_days": 24, "msme": "N", "po_rate": 1276.8}}
```

## 1.3 The schema

`tools/explain_hold/tool.json` has the name, title, a 261-character description written for a model choosing between tools, both schemas, an example, the four MCP annotations, and the retry policy.

- **Input:** `invoice_no` (required, string) and `supplier` (optional, string).
- **Output:** one clean answer:
  - `ok`, `supplier`, `ap_no`, `status`, `amount`, `due_date`
  - `payment`: `last_run`, `cutoff`, `this_friday`, `payable_this_friday`, `why_not`
  - `holds`: one entry per open hold, with `code`, `what_is_wrong`, `on_hold_since`, `may_release`
  - `matches` when the number is ambiguous
  - `error`, `next_step`, `ledgerline_code` when something fails
- **Enums:** `status` is an enum of six words. Each hold's `code` is an enum of the four hold codes.
- **Dates:** every date has `format: date` (YYYY-MM-DD).
- **Annotations:** `readOnlyHint: true`, `destructiveHint: false`, `idempotentHint: true`, `openWorldHint: false`. It only reads, so asking twice is safe, and it only touches our own Ledgerline.

**Two schema decisions**

1. **`invoice_no` is a string, not an integer.** A supplier's invoice number only looks like a number: it can carry leading zeros or letters, and the same field also takes Ledgerline's own `AP/2026/03390`. So `{"invoice_no": 4471}` is refused at the door, before any Ledgerline call (case B below).
2. **`supplier` is optional, and two matching invoices are an answer, not an error.** Emma says "Voltway's 4471", and two Voltways have an invoice 4471. If `supplier` were required, the model would have to fill it in, and "required is not the same as known" (Lecture 4, Section 7). So with no supplier the tool returns `ok: true` with both `matches` and a `next_step` that says to ask which one. It never picks one itself.

I also changed one thing in `tool.json` while finishing this part: the output fields `supplier` and `invoice_no` had empty descriptions, and now say what they are. Every field a model reads must say what it is.

## 1.4 The code

`tools/explain_hold/tool.py` has `run(s, invoice_no, supplier=None)`, which does three steps:

1. **Find the invoice.** `ap_inv_list` turns the printed number into one AP number. It keeps only exact matches, because `ap_inv_list` also matches part of a number (447 finds 4471).
2. **Read it.** `ap_inv_get` returns the full hold log, the order rate, the goods receipt, the due date and the status code.
3. **Check the people.** For each open hold, `usr_get` checks every person in the AP policy 4.1 table still has that role. Only Ledgerline's "no such user" reply (`ERR-SEC-0003`) means a person has left. Any other failure (a busy or silent Ledgerline) stops the call and is reported as the outage it is, never as a change of policy.

`run()` also catches a lost Ledgerline reply (after the reads' own two retries) and returns it in the error contract with `ledgerline_code: TIMEOUT` and a `next_step` written for a read-only tool: it is safe to ask again.

**What it cleans up**
- **Renames:** `HD` becomes "on hold", `due_dt` becomes `due_date`, `put_on` becomes `on_hold_since`.
- **Words:** each hold's legacy text becomes plain words: `QTY 18000 VS OPEN 17700` becomes "18,000 billed, 17,700 accepted".
- **Dropped:** everything the model does not need (`basic`, `tax`, `entered_by`, `client_ref`, `pays`, `grns`, the legacy `hold_cd` that shows only the first hold).
- **Payment dates:** it works out the Friday run dates from the payment policy's rule.

**Bytes in and bytes out** (measured by `part1_run.py`, which sizes every legacy reply in its own `{rc, err_cd, msg, data}` envelope):

| Call | Ledgerline calls | Bytes from Ledgerline | Bytes the tool returns |
|---|---|---|---|
| `{"invoice_no": "4471", "supplier": "Voltway Cells"}` | 7 (`ap_inv_list` ×2, `ap_inv_get`, `usr_get` ×4) | 2,679 | 854 (32%) |
| `{"invoice_no": "AP/2026/03390"}` | 6 | 2,133 | 854 (40%) |
| `{"invoice_no": "4471"}` (two matches) | 1 | 546 | 437 |

Two things I noticed while measuring, which I have not changed:
- `usr_get` is called once per person per hold, so Vikram Nair is looked up twice.
- On the printed-number path, `ap_inv_list` runs twice: once to find the invoice, once for the supplier's name.

Both are cheap reads, but a cache would save three calls.

## 1.5 The error contract

Every failure returns `ok: false`, `error` (in words), `next_step` and `ledgerline_code`. The code is Ledgerline's own error code, or empty when the tool or the door refused. All results below are real, from `logs/part1_trace.txt`, and every one of them passes `output_schema` (0 violations in 12 calls).

| Case | Arguments | Ledgerline calls | What comes back |
|---|---|---|---|
| A · refused at the door: missing argument | `{}` | 0 | `ok:false`, "Missing invoice_no.", next_step "Ask the user for invoice_no.", code `""` |
| B · refused at the door: wrong type | `{"invoice_no": 4471}` | 0 | `ok:false`, "'invoice_no' should be string, got int.", next_step "Pass invoice_no as string." |
| C · refused by Ledgerline: not found | `{"invoice_no": "AP/2026/99999"}` | 1 | `ok:false`, "No invoice AP/2026/99999 in Ledgerline.", next_step "Check the AP number with the user.", code **`ERR-AP-0001`** |
| D · a business answer, not an error | `{"invoice_no": "4471"}` | 1 | `ok:true`, `matches`: Voltway Paints & Coatings (Rs.2,17,120, clear to pay) and Voltway Cells Pvt. Ltd. (Rs.2,83,08,672, on hold), next_step "2 suppliers used invoice number 4471. Ask the user which…" |
| E · my choice: Ledgerline busy | `ap_inv_get` made busy 3 times | 3 (1 try + 2 retries) | `ok:false`, "Ledgerline refused ap_inv_get: Server busy, try later (ERR-SYS-0503).", next_step "Ledgerline is busy. The tool already retried…", code **`ERR-SYS-0503`**. Busy only once: retried, and the full answer comes back. |
| F · the tool's own refusal | `{"invoice_no": "4471", "supplier": "Acme"}` | 1 | `ok:false`, "No invoice 4471 from a supplier matching 'Acme'.", next_step names both suppliers that do have a 4471 |
| G · Ledgerline's reply lost | `ap_inv_get`'s reply lost 3 times | 3 (1 try + 2 retries) | `ok:false`, "Ledgerline did not reply in time (ap_inv_get), even after retrying.", next_step "This tool only reads, so it is safe to call it again in a minute. If it fails again, tell the user Ledgerline is not answering.", code **`TIMEOUT`** |

One more case is a warning, not a failure:
- **The policy table is out of date.** When Ganesh Pawar no longer has the stores role, the tool still answers (`ok: true`). It leaves him out of `may_release` and adds `next_step`: "AP policy 4.1 is out of date: Ganesh Pawar no longer has the stores role. Ask Vikram Nair who releases these holds now."
- **Why this matters:** the tool depends on my copy of the policy table, so it checks that copy against Ledgerline on every call. It never names someone who can no longer release a hold.

## 1.6 Tests

`tests/test_explain_hold.py` has 11 tests, all plain asserts. Run it with `python tests/test_explain_hold.py` (or with pytest). Each test starts from a fresh Ledgerline, and every result is also checked against `output_schema`.

| Test | What it checks |
|---|---|
| happy path | both holds come back, not just the one the list shows; the exact gaps; who may release each; the run dates (13 Nov, cut-off 12 Nov, this Friday 30 Oct, not payable); every service called is a read |
| clean result | no legacy field (`rc`, `err_cd`, `msg`, `data`, `hold_cd`, `sup_cd`, `due_dt`) in the result |
| two suppliers, one number | `ok: true`, both suppliers listed, no holds, next_step asks which |
| wrong type | the error contract, and 0 Ledgerline calls |
| missing argument | the error contract, and 0 Ledgerline calls |
| unknown AP number | the error contract with `ERR-AP-0001` |
| unknown invoice number | the error contract |
| Ledgerline busy | one busy reply is retried and answers; three give `ERR-SYS-0503` after exactly 3 calls |
| busy while checking people | `usr_get` busy 3 times gives `ERR-SYS-0503`, never "GPAWAR is no longer in Ledgerline" |
| a person who really left | when GPAWAR is deleted from Ledgerline (`ERR-SEC-0003`), he is dropped from `may_release` and `next_step` says the policy table is out of date |
| a lost reply | on each of `ap_inv_list`, `ap_inv_get`, `usr_get`: `TIMEOUT`, with a `next_step` this server can follow (it names no tool the server does not offer) |

```
PASS test_a_person_who_really_left_is_still_reported
PASS test_business_answer_two_suppliers_same_number
PASS test_busy_usr_get_is_an_outage_not_a_policy_change
PASS test_clean_result_not_the_envelope
PASS test_happy_path_two_holds_who_and_when
PASS test_ledgerline_busy_retried_then_given_up
PASS test_lost_reply_gives_a_next_step_this_server_can_follow
PASS test_refused_at_the_door_missing_argument
PASS test_refused_at_the_door_wrong_type
PASS test_refused_by_ledgerline_unknown_ap_number
PASS test_unknown_invoice_number
11 passed
```

The tool returns one invoice, not a list, so there is nothing to paginate. When two suppliers match, it returns two rows at most, one per supplier.

## Loaded next to the shipped tools, and linted

```python
from a4_setup import load_tool          # add_tool_folder("tools/explain_hold"), next to the 15 shipped tools
from ledgerline.course.l4 import lint_tool, validate_args
name = load_tool()
lint_tool(name)                         # -> []
validate_args(name, {"invoice_no": 4471})   # -> ["invoice_no: 4471 is not of type 'string'"]
```

`lint_tool("explain_hold")` returns **`[]`**.

**How to reproduce:**
- `a4_setup.py` builds the sandbox: the course kit's `fin_payables` Ledgerline, my capstone's records from `capstone_seed.py`, and the tool loaded with `add_tool_folder`.
- `python part1_run.py` prints every case above and writes `logs/part1.json`.
- `python tests/test_explain_hold.py` runs the tests.
