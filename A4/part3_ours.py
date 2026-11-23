"""A4 Part 3, our harness: Emma's question on Ask Northbridge's own loop (ledgerline.experience.harness), live, with
the context captured at every model call and measured part by part (NB4 sections 6 and 7, on my tool).

    set GEMINI_API_KEY=...            (Windows: setx, or the shell's own env)
    python part3_ours.py              # writes logs/part3_ours.json and logs/part3_ours_context.txt

Model: gemini:gemini-3.8-flash (Google's API, GEMINI_API_KEY). Tools: explain_hold only, served over the course's
in-process MCP client, as Emma Clarke (ECLARKE). System prompt: AP_SYSTEM below, written for this task.
"""
import contextlib
import io
import json
import os

os.environ["LEDGER_LLM_MODE"] = "live"                      # every model call is real; nothing is replayed

from a4_setup import load_tool, new_erp                      # noqa: E402
from ledgerline.course.l4 import hands                       # noqa: E402
from ledgerline.experience import harness as H               # noqa: E402
from ledgerline.experience.players import guard_erp         # noqa: E402

MODEL = "gemini:gemini-3.8-flash"
H.CHAIN[:] = [MODEL]                                         # one model, no fallbacks: the comparison stays clean
hands.MODEL = MODEL                                          # the token measurements use the same model and route
hands.TOKEN_CASSETTE["A4_ours"] = "A4_ours_tokens"
USER = "ECLARKE"

AP_SYSTEM = """You are Ask Northbridge, the assistant for Northbridge Cycles, Pune, a maker of e-bikes. You work inside
Northbridge's Ledgerline ERP for Emma Clarke (ECLARKE), purchase executive, with Emma's own Ledgerline permissions and
nobody else's. Today is Monday 26 October 2026.

How you work
- Every fact (invoice numbers, holds, amounts, dates, who may release a hold) comes from a tool. Never guess a number,
  a name or a date: look it up.
- If a tool says more than one invoice matches, ask Emma which one before you answer about it.
- If a tool returns ok=false, read next_step and follow it, or tell Emma plainly what to do.
- If Emma cannot do a step herself (releasing a hold, approving a payment), say who can.
- Short, plain replies: two to six lines, no tables. Money in rupees with Indian commas. No emoji."""

TURN1 = "Why is Voltway's invoice 4471 on hold, and can we pay it Friday?"
TURN2 = "Voltway Cells, the battery packs."


def main():
    name = load_tool()
    erp = guard_erp(new_erp())                               # the lock the live app's harness expects
    a = hands.Recorded(erp, USER, "agent", names=[name], system=AP_SYSTEM, cassette="A4_ours")
    turns = []
    for text in (TURN1, TURN2):
        out = a.respond(text)
        turns.append({"user": text, "reply": out["reply"], "cards": out["cards"], "model_calls": out["model_calls"],
                      "tokens_in": out["tokens_in"], "tokens_out": out["tokens_out"], "seconds": out["seconds"],
                      "cost_inr": out["cost_inr"], "model": out["model"]})
        got_holds = any(isinstance(c["result"], dict) and c["result"].get("holds") for c in out["cards"])
        if got_holds:                                        # it already answered about Voltway Cells: no second turn
            break
    run = {"label": "A4", "cassette": "A4_ours", "turns": turns, "steps": a.steps, "tool_definitions": a.schemas}
    a.close()

    parts = hands.context_parts(run)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        hands.show_context(run, parts, width=110)
    text = buf.getvalue()
    print(text)
    for t in turns:
        print("EMMA:", t["user"])
        for c in t["cards"]:
            print("   call", c["tool"], json.dumps(c["args"]), "->", json.dumps(c["result"])[:200])
        print("   REPLY:", t["reply"])
        print(f"   model calls {t['model_calls']} · tokens in {t['tokens_in']:,} · out {t['tokens_out']:,} · "
              f"{t['seconds']} s · Rs.{t['cost_inr']}")
    tool_tok = next(p["tokens"] for p in parts if p["part"].startswith("tool definitions"))
    first = [s for s in run["steps"] if s["tools"] is not None][0]["prompt_tokens"]
    print(f"tool definitions: {tool_tok:,} tokens = {tool_tok / first:.1%} of the first call's {first:,}")

    os.makedirs("logs", exist_ok=True)
    with open("logs/part3_ours_context.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("logs/part3_ours.json", "w", encoding="utf-8") as f:
        json.dump({"model": MODEL, "system_prompt": AP_SYSTEM, "turns": turns, "parts": parts,
                   "steps": [{k: v for k, v in s.items() if k != "tools"} for s in run["steps"]],
                   "tool_definitions": run["tool_definitions"], "tool_definition_tokens": tool_tok,
                   "first_call_prompt_tokens": first}, f, indent=1, default=str)
    print("written logs/part3_ours.json")


if __name__ == "__main__":
    main()
