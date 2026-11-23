# PRODUCTION.md: is `explain_hold` production grade?

**How it was measured:**
- **One script:** `python production.py` measures all seven criteria and writes `logs/production.json`.
- **Sandbox:** every number comes from a fresh Ledgerline (the course kit's `fin_payables` with my capstone's records), as Emma Clarke (`ECLARKE`).
- **Notebook:** `A4_explain_hold.ipynb` runs it, in its Part 4 section.

## 4.1 The criteria that matter here (seven measured)

| # | Criterion | Why it matters for this tool |
|---|---|---|
| 1 | Schema | Claude Code reads `structuredContent` (Part 3), so the result must match `outputSchema` exactly, dates included. |
| 2 | Reliability | Emma and Priya type invoice numbers by hand: spaces, lower case, partial numbers, the wrong supplier. Every odd input must come back as a business answer, never a crash. |
| 4 | Latency | It is called in the middle of a chat, once or twice per question. |
| 5 | Payload | Its result goes straight into the model's context window, on every later call of the conversation. |
| 7 | Timeouts | Ledgerline is a legacy system that gets busy. This tool is the only thing between an outage and what the model tells Emma. |
| 8 | Regression | The tool depends on a copied policy table and on hold-text formats. Both will change, so every fix must stay fixed. |
| 9 | MCP compliance | It has to work on any MCP host. Part 3 already ran it on two. |

**Why the other three matter less here:**
- **6 · Idempotency:** the tool only reads. Asking twice cannot post anything twice, and the tests check that every service it calls is a read.
- **3 · LLM usability:** it matters, but measuring it properly needs a set of golden questions run live on several hosts. Part 3 is one data point: both hosts picked the right tool with the right arguments, but only one asked which Voltway.
- **10 · Change management:** a release process with client sign-off cannot happen in a sandbox.

## 4.2 The measurements

| Criterion | Threshold | How it was measured | Result |
|---|---|---|---|
| **1 · Schema** | 0 violations; both schemas valid | 724 results (every real invoice, 3 ways each, plus 300 fuzzed calls), each checked against `output_schema` with `jsonschema`, date formats included; both schemas checked as valid JSON Schema | **0 violations**, both schemas valid ✅ |
| **2 · Reliability** | ≤ 0.1% of calls outside the error contract | 1,903 fuzzed calls (see the list below). A call counts as outside the contract if it is not an answer or a business failure with `error`, `next_step` and `ledgerline_code`, if it crashed inside the tool (`INTERNAL`), or if its `next_step` names a tool this server does not offer | **0 of 1,903 (0%)** ✅ |
| **4 · Latency** | p50 ≤ 50 ms, p95 ≤ 100, p99 ≤ 200 | 800 calls, mixed real and failing arguments. The tool's own time is the wall time minus Ledgerline's service time (`CallRecord.ms`) | **p50 0.096, p95 0.202, p99 0.235 ms** ✅ |
| **5 · Payload** | no result above 4 KB (my limit: about 1,000 tokens, nearly 5× the real answer); a list says how many rows it has | the largest result over every real invoice; then the same invoice number from 10, 50 and 200 extra suppliers | real: **854 bytes** ✅; 10 suppliers: 2,198 B ✅; 50: **9,238 B** ❌; 200: **35,639 B, 202 rows, no count** ❌ |
| **7 · Timeouts** | defined and tested on every service the tool calls | Ledgerline busy (`ERR-SYS-0503`), once (must recover to the same answer) and 3 times (must fail inside the error contract with `ERR-SYS-0503` and a `next_step` this server can act on), on each of `ap_inv_list`, `ap_inv_get`, `usr_get` | **6 of 6** ✅ (5 of 6 when first measured: see 4.3) |
| **8 · Regression** | 100% of tests | `tests/test_explain_hold.py`, run before every change | **11 of 11** ✅ |
| **9 · MCP compliance** | 100% of checks | a real stdio session with `serve_explain_hold.py`: initialize agrees on 2025-06-18; ping; tools/list shape; both schemas valid; a good call (isError false, `structuredContent` matches `outputSchema`, text and structured agree); a failed call (isError true, full contract); a wrong type (refused); an unknown method (-32601); an unknown tool (refused). Plus the two hosts in Part 3, which accepted and called the tool | **10 of 10** ✅ |

**The fuzz inputs** (criterion 2):
- **Wrong types:** `None`, numbers, `True`, lists, dicts.
- **Odd strings:** empty and blank strings; spaces, tabs and newlines around real numbers; lower case (`ap/2026/03390`, `sv/0912`).
- **Broken AP numbers:** half numbers (`AP/2026/`).
- **Hostile input:** a 10,000-character string, SQL-like text, Devanagari digits, an emoji, `%`, `_`, a NUL character.
- **Wrong arguments:** an unknown argument; a wrong-case argument name.
- **Random:** 1,500 random strings.

Each was crossed with ten supplier values. I also confirmed that `" 4471 "`, `"4471\n"`, `"ap/2026/03390"` and `"AP/2026/03390 "` all find the right invoice, so there is no quiet wrong answer behind the clean contract numbers.

The latency is that small because the sandbox's Ledgerline is in memory. On a real ERP, its services would take most of the time. This criterion measures only what my code adds, which is the part I control.

## 4.3 The failure I found and fixed: timeouts, 5 of 6 → 6 of 6

**What failed when I first measured** (`logs/production_before_fix.txt`): one of the six timeout drills.

| Service | Fault | What the tool said |
|---|---|---|
| `usr_get` | busy, 3 times | `ok: true` and *"AP policy 4.1 is out of date: GPAWAR is no longer in Ledgerline. Ask Vikram Nair who releases these holds now."* |

**Why this is a serious bug: a wrong answer, said with confidence.**
- `releasers()` caught every `ToolError` from `usr_get` as if the person had left the company. So a busy Ledgerline became a false business fact, sent to Emma with a recommended action.
- Nothing in the error contract flagged it: the result was `ok: true` and passed the schema. Only a test that injects the fault and reads the words finds it.

**The fix** (in `releasers()`, `tools/explain_hold/tool.py`):

```python
except ToolError as e:
    if e.code != "ERR-SEC-0003":      # only "NO SUCH USER" means the person has left;
        raise                          # a busy or failing Ledgerline is an outage, reported as one
    problems.append(f"{user_id} is no longer in Ledgerline")
```

I found `ERR-SEC-0003` by calling `usr_get` with a user that does not exist. Ledgerline answers `{"rc": "E", "err_cd": "ERR-SEC-0003", "msg": "NO SUCH USER"}`.

**After the fix:**
- **Timeouts:** 6 of 6. A busy `usr_get` now returns `ok: false`, "Ledgerline refused usr_get: Server busy, try later (ERR-SYS-0503)", with next_step "Ledgerline is busy. The tool already retried; try again in a minute, or tell the user."
- **The other criteria did not move.**

**Turned into tests.** Lecture 4: turn every bug you fix into a test.
- **`test_busy_usr_get_is_an_outage_not_a_policy_change`** failed on the code before the fix and passes now.
- **`test_a_person_who_really_left_is_still_reported`** guards what the fix had to keep: when GPAWAR really is deleted from Ledgerline, the tool still drops him and says the policy table is out of date.

## How to reproduce

```
python production.py                   # all seven criteria, writes logs/production.json
python tests/test_explain_hold.py      # 11 tests
```
