# HARNESSES.md: the same question on two harnesses

**The question.** Emma Clarke, purchasing, after Voltway's call on Monday 26th October: *"Why is Voltway's invoice 4471 on hold, and can we pay it Friday?"* This is question 1 from TOOL.md.

It is a good test because "Voltway's 4471" is ambiguous: two suppliers named Voltway each sent an invoice numbered 4471.

**The same tool and data on both sides:**
- **Server:** `explain_hold` on `serve_explain_hold.py` (Part 2), acting as Emma (`ECLARKE`).
- **Data:** the `fin_payables` sandbox with my capstone's records, where Ledgerline's date is Monday 26 October 2026.
- **Runs:** both were live on my own computer on 17 November 2026, started by `run_part3.py`.
- **Logs:** everything quoted here is in `logs/`.

## 3.1 Claude's harness: Claude Code, headless

**Command** (`run_part3.py` builds it):

```
claude -p "Why is Voltway's invoice 4471 on hold, and can we pay it Friday?" \
  --mcp-config logs/claude_mcp_local.json --strict-mcp-config \
  --allowedTools mcp__northbridge-ap__explain_hold \
  --disallowedTools Bash,Read,Edit,Write,Glob,Grep,WebFetch,WebSearch,Task,NotebookEdit,TodoWrite \
  --output-format stream-json --verbose
```

**How it was set up:**
- **Version and model:** Claude Code 2.1.326, model `claude-opus-5-5`.
- **No other servers:** `--strict-mcp-config` loads only my server.
- **No file access:** the run starts in an empty folder (`logs/claude_cwd`), and the file and shell tools are switched off. So Claude Code cannot open `tool.py` or anything else in this folder.
- **No approval clicks:** `--allowedTools` pre-approves my read-only tool. In the desktop app this is the "Allow" click.
- **One turn was enough:** a second turn would only have run if Claude had asked which invoice, and it did not ask.

**The transcript** (from `logs/claude_turn1.jsonl`, via `part3_claude_summary.py`):

```
CALL   ToolSearch {"query": "select:mcp__northbridge-ap__explain_hold", "max_results": 1}

RESULT (the tool definition, loaded by ToolSearch)

CALL   mcp__northbridge-ap__explain_hold {"invoice_no": "4471", "supplier": "Voltway"}

RESULT {"ok":true,"matches":[{"ap_no":"AP/2026/03409","supplier":"Voltway Paints & Coatings","invoice_date":"2026-10-20","amount":217120,"status":"clear to pay"},{"ap_no":"AP/2026/03390","supplier":"Voltway Cells Pvt. Ltd.","invoice_date":"2026-10-02","amount":28308672,"status":"on hold"}],"next_step":"2 suppliers used invoice number 4471. Ask the user which: Voltway Paints & Coatings or Voltway Cells Pvt. Ltd."}

TEXT   Two suppliers have used invoice number 4471. Only Voltway Cells' invoice is on hold, so I'll look that one up.

CALL   mcp__northbridge-ap__explain_hold {"invoice_no": "4471", "supplier": "Voltway Cells"}

RESULT {"ok":true,"supplier":"Voltway Cells Pvt. Ltd.","ap_no":"AP/2026/03390","status":"on hold","invoice_no":"4471","amount":28308672,"due_date":"2026-11-16","payment":{"last_run":"2026-11-13","cutoff":"2026-11-12","this_friday":"2026-10-30","payable_this_friday":false,"why_not":"on hold; nothing is paid while an invoice is on hold"},"holds":[{"code":"H-QTY","what_is_wrong":"18,000 billed, 17,700 accepted","on_hold_since":"2026-10-05","may_release":[{"name":"Ganesh Pawar","role":"stores"},{"name":"Vikram Nair","role":"financial controller"}]},{"code":"H-PRC","what_is_wrong":"billed at Rs.1,332.80 each against the order's Rs.1,276.80 (+4.39%)","on_hold_since":"2026-10-05","may_release":[{"name":"Daniel Okafor","role":"purchase manager"},{"name":"Vikram Nair","role":"financial controller"}]}]}

TEXT   No, it can't be paid Friday as things stand. It's held for two reasons, and it was already due yesterday.

I assumed you meant **Voltway Cells Pvt. Ltd.** (AP/2026/03390, ₹2,83,08,672). Voltway Paints & Coatings also has an invoice 4471, but theirs is clear to pay.

**Why it's on hold (both holds since 5 Oct):**
1. **Quantity (H-QTY):** They billed 18,000 units, but stores accepted only 17,700. 300 units are billed but weren't accepted. Ganesh Pawar (stores) or Vikram Nair (financial controller) can release it.
2. **Price (H-PRC):** They billed ₹1,332.80 per unit, but the order price is ₹1,276.80. That's 4.39% over. Daniel Okafor (purchase manager) or Vikram Nair can release it.

By my own calculation (the system didn't give this figure), the invoice is about ₹16.4 lakh (incl. 18% GST) more than the accepted quantity at the order price.

**Can we pay it Friday?**
- Nothing on hold gets paid, so both holds have to be released first. Vikram Nair can release both.
- It's already late. The due date was **16 Nov**. The last run that would have paid it on time was 13 Nov, with a cutoff of 12 Nov.
- Even if both holds are cleared before this Friday's (20 Nov) cutoff, the payment will be a few days late. The system didn't give the cutoff for that run. If it follows last week's pattern, it's probably Thursday 19 Nov, but please check with AP.
- The system's "this Friday" field shows 30 Oct, which is clearly out of date. Don't rely on it.

**My recommendation:** Don't just release the holds and pay the full amount. Either get a credit note or revised invoice from Voltway Cells for the 300 short units and the price difference, or get Daniel Okafor to confirm that the higher price was agreed. Once one of those is done, Vikram Nair can release both holds and it can go in Friday's run.
```

**What Claude Code reports:**
- 4 model calls (`num_turns: 4`), 18.9 s.
- **Cost:** $0.1645 (list price, as Claude Code reports it).
- **Tokens:** input 10 + cache write 14,869 + cache read 69,937 = **84,816**; output **1,578**, of which 554 were thinking.

**How the four calls happened:**
- **Call 1** did not see my tool's definition at all. Claude Code lists MCP tools by name only, so the model first called `ToolSearch` to load `explain_hold`.
- **Calls 2 and 3** each called my tool once.
- **Call 4** wrote the reply.

## 3.2 Our harness: Ask Northbridge's loop

**Setup:**
- **Script:** `python part3_ours.py`.
- **Harness:** `ledgerline.experience.harness.AskNorthbridge`, stage `agent`, as the course's live app runs it. NB4's `Recorded` subclass keeps a copy of the messages at every model call.
- **Model:** `gemini:gemini-3.8-flash`, live, with no fallbacks.
- **Tools it saw:** `explain_hold` only, through the course's in-process MCP client.
- **System prompt** (written for this task):

```
You are Ask Northbridge, the assistant for Northbridge Cycles, Pune, a maker of e-bikes. You work inside
Northbridge's Ledgerline ERP for Emma Clarke (ECLARKE), purchase executive, with Emma's own Ledgerline permissions and
nobody else's. Today is Monday 26 October 2026.

How you work
- Every fact (invoice numbers, holds, amounts, dates, who may release a hold) comes from a tool. Never guess a number,
  a name or a date: look it up.
- If a tool says more than one invoice matches, ask Emma which one before you answer about it.
- If a tool returns ok=false, read next_step and follow it, or tell Emma plainly what to do.
- If Emma cannot do a step herself (releasing a hold, approving a payment), say who can.
- Short, plain replies: two to six lines, no tables. Money in rupees with Indian commas. No emoji.
```

**The transcript.** Emma's second line was only sent because the model asked which invoice.

```
EMMA   Why is Voltway's invoice 4471 on hold, and can we pay it Friday?

CALL   explain_hold {"supplier": "Voltway", "invoice_no": "4471"}

RESULT {"ok": true, "matches": [{"ap_no": "AP/2026/03409", "supplier": "Voltway Paints & Coatings", "invoice_date": "2026-10-20", "amount": 217120.0, "status": "clear to pay"}, {"ap_no": "AP/2026/03390", "supplier": "Voltway Cells Pvt. Ltd.", "invoice_date": "2026-10-02", "amount": 28308672.0, "status": "on hold"}], "next_step": "2 suppliers used invoice number 4471. Ask the user which: Voltway Paints & Coatings or Voltway Cells Pvt. Ltd."}

REPLY  Two suppliers have issued an invoice numbered 4471:
- Voltway Paints & Coatings (invoice date 20 Oct 2026, ₹2,17,120)
- Voltway Cells Pvt. Ltd. (invoice date 02 Oct 2026, ₹2,83,08,672)

Which supplier's invoice would you like me to look into?

       model calls 2 · tokens in 1,190 · out 120 · 23.89 s · Rs.0.0841 (the harness's own estimate)

EMMA   Voltway Cells, the battery packs.

CALL   explain_hold {"invoice_no": "AP/2026/03390", "supplier": "Voltway Cells Pvt. Ltd."}

RESULT {"ok": true, "supplier": "Voltway Cells Pvt. Ltd.", "ap_no": "AP/2026/03390", "status": "on hold", "invoice_no": "4471", "amount": 28308672.0, "due_date": "2026-11-16", "payment": {"last_run": "2026-11-13", "cutoff": "2026-11-12", "this_friday": "2026-10-30", "payable_this_friday": false, "why_not": "on hold; nothing is paid while an invoice is on hold"}, "holds": [{"code": "H-QTY", "what_is_wrong": "18,000 billed, 17,700 accepted", "on_hold_since": "2026-10-05", "may_release": [{"name": "Ganesh Pawar", "role": "stores"}, {"name": "Vikram Nair", "role": "financial controller"}]}, {"code": "H-PRC", "what_is_wrong": "billed at Rs.1,332.80 each against the order's Rs.1,276.80 (+4.39%)", "on_hold_since": "2026-10-05", "may_release": [{"name": "Daniel Okafor", "role": "purchase manager"}, {"name": "Vikram Nair", "role": "financial controller"}]}]}

REPLY  Voltway Cells invoice 4471 (₹2,83,08,672) is on hold for two discrepancies:
- Quantity mismatch (H-QTY): 18,000 billed vs 17,700 accepted; can be released by Ganesh Pawar (stores) or Vikram Nair (financial controller).
- Price mismatch (H-PRC): billed at ₹1,332.80 vs ₹1,276.80 on the PO; can be released by Daniel Okafor (purchase manager) or Vikram Nair.
It cannot be paid this Friday (30 October 2026) while holds remain open. Since it is due on 16 November 2026, the last Friday run to pay it on time is 13 November 2026 (cutoff 12 November).

       model calls 2 · tokens in 2,193 · out 227 · 6.41 s · Rs.0.1564 (the harness's own estimate)
```

**The context at every model call** (NB4's `show_context`). Tokens per part are measured with the same model. At every call they add up exactly to the provider's own `prompt_tokens`:

```
-- model call 1 of 4: prompt_tokens 434 --
   +    216  system prompt                    
   +    195  tool definitions (1)             
   +     23  user message                     Why is Voltway's invoice 4471 on hold, and can we pay it Friday?
     = 434 tokens in the context (matches prompt_tokens)
     model wrote (28 tokens): explain_hold({"supplier": "Voltway", "invoice_no": "4471"})
-- model call 2 of 4: prompt_tokens 756 --
   +    141  tool call                        [{"explain_hold": {"supplier": "Voltway", "invoice_no": "4471"}}]
   +    181  tool result                      {"ok": true, "matches": [{"ap_no": "AP/2026/03409", "supplier": "Voltw
     = 756 tokens in the context (matches prompt_tokens)
     model wrote (92 tokens): 'Two suppliers have issued an invoice numbered 4471:\n- Voltway Paints & Coatings (invoice date 20 Oct 2026, ₹2,'
-- model call 3 of 4: prompt_tokens 858 --
   +    102  assistant reply (+ the user's next message) Two suppliers have issued an invoice numbered 4471: - Voltway Paints &
   +   (with the part above)  user message                     Voltway Cells, the battery packs.
     = 858 tokens in the context (matches prompt_tokens)
     model wrote (41 tokens): explain_hold({"invoice_no": "AP/2026/03390", "supplier": "Voltway Cells Pvt. Ltd."})
-- model call 4 of 4: prompt_tokens 1,335 --
   +    114  tool call                        [{"explain_hold": {"invoice_no": "AP/2026/03390", "supplier": "Voltway
   +    363  tool result                      {"ok": true, "supplier": "Voltway Cells Pvt. Ltd.", "ap_no": "AP/2026/
     = 1,335 tokens in the context (matches prompt_tokens)
     model wrote (186 tokens): 'Voltway Cells invoice 4471 (₹2,83,08,672) is on hold for two discrepancies:\n- Quantity mismatch (H-QTY): 18,00'
Never in the context: tool.py, the Ledgerline services and their {rc, err_cd, msg, data} replies, the database, Emma's session and password, the MCP plumbing.
```

**My tool definition costs 195 tokens, 45% of the first call** (195 of 434):
- **The model received three things:** the name, the description and the input schema, as one function.
- **It never received:** the output schema, the annotations, the `_meta`, or the `example`.
- The definition is re-sent on all 4 calls: 780 tokens of the 3,383 read in total.

## 3.3 Comparison

| | Claude Code | Our harness |
|---|---|---|
| Model | claude-opus-5-5 | gemini-3.8-flash |
| Who wrote the loop and the system prompt | Anthropic | the course (`harness.py`) and me (`AP_SYSTEM`) |
| User turns | 1 | 2 (it asked which invoice) |
| Model calls | 4 | 4 (2 per turn) |
| Tool calls | 3: `ToolSearch`, then `explain_hold` ×2 | 2: `explain_hold` ×2 |
| Tokens in (all calls) | 84,816 (84,806 of them cached) | 3,383 |
| Tokens in (first call) | 20,587 | 434 |
| Tokens out | 1,578 (554 thinking) | 347 |
| Time | 18.9 s | 30.3 s (23.9 s for turn 1, the first live call) |
| Cost | $0.1645 (reported) | Rs.0.24 (the harness's own estimate) |
| How my tool's definition arrived | name only at first; the full definition after a `ToolSearch` call | in full, as one function, on every call |
| What the model read of each result | `structuredContent`, re-serialised as compact JSON | the result as JSON text |
| Did it follow `next_step` "Ask the user which" | **no**: it chose Voltway Cells itself, because only that invoice is on hold, and said so | **yes**: it listed both and asked |
| Did it know "today" | **no**: it used the real date, 17 Nov 2026 | **yes**: the system prompt says 26 Oct 2026 |
| Answer | right holds, people and gaps; wrong about lateness (see 3.4) | right on every point |

**What both models never saw:**
- `tool.py` and my policy table in it
- the three Ledgerline services and their `{rc, err_cd, msg, data}` envelopes (2,679 bytes for this answer)
- the hold log's legacy text (`QTY 18000 VS OPEN 17700`)
- the database, Emma's session
- the MCP messages themselves (`initialize`, `tools/list`)
- `annotations`, `_meta` and the `example`
- `capstone_seed.py`

Each model saw only my description and input schema, its own calls, and the 854-byte clean result.

**The comparison is not like for like.** The models differ, and Claude Code's 20,587-token first call is mostly its own system prompt and tool list, served from cache. What the comparison does show clearly is who controls what.
- **In my harness I set:** the date, the tone, the money format, the rule "ask which before you answer", and which tools exist.
- **In Claude Code I control only my tool:** its description, its schemas, and what its result says.

### One rule I can enforce only in my own harness

**An ambiguity gate.** When a tool returns `matches`, the harness stops the turn in code and shows Emma the choice. The model gets no further call in that turn.
- **Why it's needed:** my tool already says "Ask the user which" in `next_step`, and Claude Code read that and chose anyway. In Claude's harness a `next_step` is only a request.
- **How I would build it:** in `AskNorthbridge.respond()`, after each tool call:
  - If the parsed result has `"matches"`, append a short reply built from the matches ("Two invoices are numbered 4471: … Which one?") and `break` out of the loop before the next model call.
  - Emma's answer starts the next turn.
- **Why only here:** it is about ten lines in a loop I own. Claude Code's loop is Anthropic's, and nothing in my tool can stop it calling again.

The same is true of today's date. My harness puts Ledgerline's date in the system prompt. Claude Code has its own prompt with the real date, and I cannot change it.

## 3.4 One model error, with the tool's data right

**Claude Code got the date wrong.** The tool's result was correct for Ledgerline's date (Monday 26 October 2026): due 16 Nov, last run 13 Nov, cut-off 12 Nov, this Friday 30 Oct, not payable while on hold. Claude Code read the real date (17 November 2026) from its own environment, and then:
- said "it was already due yesterday"
- moved "this Friday" to 20 November and guessed its cut-off ("probably Thursday 19 Nov")
- told Emma that the tool's `this_friday: 2026-10-30` was "clearly out of date. Don't rely on it."

So the one figure it threw away was right, and its own were wrong for the business's date. Gemini, in my harness, had "Today is Monday 26 October 2026" in its system prompt and gave every date correctly.

**Two smaller points, both in Claude's favour:**
- **It said when it guessed.** It chose Voltway Cells itself, but told Emma: "I assumed you meant Voltway Cells Pvt. Ltd."
- **It flagged its own maths.** It said its ₹16.4 lakh figure was its own calculation, and the figure is right: 18,000 × 1,332.80 − 17,700 × 1,276.80 = 13,91,040, plus 18% GST = 16,41,427.

**What would catch the date error:**
- **In the tool:** the result should carry its own date, e.g. `"as_of": "2026-10-26"` (Ledgerline's `s.erp.today`), and the description should say every date is relative to it. A model reading `as_of` would not swap in its own clock. This is the same lesson as Lecture 4's currency slip: every field a model reads must say what it is, and "this Friday" is relative to a date the result never stated.
- **In the harness:** a check of the reply against the tool's numbers before it reaches Emma (Lecture 7). Any date in the reply that is not in the tool result, such as "20 Nov" or "19 Nov", gets flagged.

I have not changed the tool for this. Part 4 is where tool fixes get measured.

## How to reproduce

```
python run_part3.py                 # both harnesses (needs GEMINI_API_KEY and a signed-in Claude Code)
python run_part3.py --skip-ours     # only Claude Code
python part3_claude_summary.py logs/claude_turn1.jsonl
```
