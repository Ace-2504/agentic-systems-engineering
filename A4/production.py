"""A4 Part 4: measure explain_hold against seven of the ten production criteria (Lecture 4, Section 10).

    python production.py               # all seven criteria -> logs/production.json and the printout

Every number comes from a fresh Ledgerline (fin_payables + my capstone's records) as Emma Clarke (ECLARKE).
"""
import json
import os
import random
import statistics
import subprocess
import sys
import time

import jsonschema

from a4_setup import HERE, load_tool, new_erp
from ledgerline.toolbox import SPECS, Toolbox

USER = "ECLARKE"
NAME = load_tool()
SPEC = SPECS[NAME].spec
OUT = jsonschema.Draft202012Validator(SPEC["output_schema"], format_checker=jsonschema.FormatChecker())
SERVED = {NAME}                                    # the only tool this MCP server offers
OTHER_TOOLS = [t for t in SPECS if t not in SERVED]
PAYLOAD_LIMIT = 4096                               # my agreed limit for one result: 4 KB, about 1,000 tokens
random.seed(4)


def fresh(faults=None):
    erp = new_erp(faults)
    return erp, Toolbox(erp, USER, names=[NAME])


def call(args, faults=None, erp_tb=None):
    erp, tb = erp_tb or fresh(faults)
    return tb.call(NAME, args), erp


def contract_problem(out):
    """None if the result is a clean answer or a business failure in the error contract; else what is wrong."""
    if not isinstance(out, dict) or "ok" not in out:
        return "not a result object"
    if out["ok"] is True:
        return None
    for k in ("error", "next_step", "ledgerline_code"):
        if k not in out:
            return f"failure without {k}"
    if out["ledgerline_code"] == "INTERNAL":
        return "a crash inside the tool"
    named = [t for t in OTHER_TOOLS if t in (out.get("next_step") or "")]
    if named:
        return f"next_step sends the model to {named[0]}, a tool this server does not offer"
    return None


def schema_errors(out):
    return [e.message for e in OUT.iter_errors(out)]


# ----------------------------------------------------------------------------- the inputs
def invoices():
    erp = new_erp()
    return [dict(r) for r in erp.q("SELECT ap_no, sup_inv_no, sup_cd FROM ap_inv")], erp


def real_args():
    rows, erp = invoices()
    names = {r["sup_cd"]: r["name"] for r in erp.q("SELECT sup_cd, name FROM supplier")}
    out = []
    for r in rows:
        out += [{"invoice_no": r["ap_no"]}, {"invoice_no": r["sup_inv_no"]},
                {"invoice_no": r["sup_inv_no"], "supplier": names.get(r["sup_cd"], "")}]
    return out


def fuzz_args(n_random=1500):
    inv = [None, "", " ", 4471, 4471.0, True, [], {}, ["4471"], "4471", " 4471 ", "4471\n", "ap/2026/03390",
           "AP/2026/03390", "AP/2026/", "AP/", "AP/2026/03390 ", "ap/2026/99999", "SV/0912", "sv/0912", "3815", "0",
           "-1", "x" * 10000, "4471" * 500, "'; DROP TABLE ap_inv;--", "४४७१", "🙂", "%", "_", "4471%", "*", "NULL",
           "AP/../../etc", "\u0000", "AP/2026/03374", "AP/2026/03301", "4471\t", "AP2026/03390", "ap / 2026 / 03390"]
    sup = [None, "", "Voltway", "voltway cells", "VOLTWAY CELLS PVT. LTD.", "Acme", 42, "x" * 5000, "%", "Paints"]
    cases = []
    for i in inv:
        for s in sup:
            a = {"invoice_no": i}
            if s is not None:
                a["supplier"] = s
            cases.append(a)
    cases += [{"invoice_no": "4471", "foo": 1}, {"supplier": "Voltway"}, {"invoice_no": "4471", "Supplier": "x"}]
    alphabet = "0123456789AP/-_ %'\"\\abcxyzअ🙂\n\t"
    for _ in range(n_random):
        s = "".join(random.choice(alphabet) for _ in range(random.randint(0, 40)))
        a = {"invoice_no": random.choice([s, "AP/2026/" + s, s.upper()])}
        if random.random() < 0.4:
            a["supplier"] = "".join(random.choice(alphabet) for _ in range(random.randint(0, 20)))
        cases.append(a)
    return cases


# ----------------------------------------------------------------------------- the criteria
def c1_schema():
    """Every ok result and every failure checked against output_schema, with date formats checked too."""
    results = [call(a)[0] for a in real_args() + fuzz_args(300)]
    bad = [(r, schema_errors(r)) for r in results if schema_errors(r)]
    in_ok = jsonschema.Draft202012Validator.check_schema(SPEC["input_schema"]) is None
    out_ok = jsonschema.Draft202012Validator.check_schema(SPEC["output_schema"]) is None
    return {"results_checked": len(results), "violations": len(bad), "both_schemas_valid": in_ok and out_ok,
            "examples": [{"result": r, "errors": e[:2]} for r, e in bad[:3]]}


def c2_reliability():
    cases = fuzz_args()
    problems = {}
    for a in cases:
        try:
            out = call(a)[0]
            p = contract_problem(out)
        except Exception as e:                                       # noqa: BLE001
            p = f"exception escaped: {type(e).__name__}"
        if p:
            problems.setdefault(p, []).append(a)
    n_bad = sum(len(v) for v in problems.values())
    return {"calls": len(cases), "outside_contract": n_bad, "share": round(n_bad / len(cases) * 100, 3),
            "kinds": {k: len(v) for k, v in problems.items()},
            "examples": {k: [str(x)[:120] for x in v[:2]] for k, v in problems.items()}}


def c3_latency(n=800):
    pool = real_args() + [{"invoice_no": "AP/2026/99999"}, {"invoice_no": "9999"}, {"invoice_no": 4471}]
    erp, tb = fresh()
    total, own = [], []
    for i in range(n):
        a = pool[i % len(pool)]
        n0 = len(erp.calls)
        t0 = time.perf_counter()
        tb.call(NAME, a)
        ms = (time.perf_counter() - t0) * 1000
        svc = sum(r.ms for r in erp.calls[n0:])
        total.append(ms)
        own.append(ms - svc)

    def pct(xs, p):
        xs = sorted(xs)
        return round(xs[min(len(xs) - 1, int(round(p / 100 * (len(xs) - 1))))], 3)
    return {"calls": n, "tool_own_ms": {"p50": pct(own, 50), "p95": pct(own, 95), "p99": pct(own, 99)},
            "with_ledgerline_ms": {"p50": pct(total, 50), "p95": pct(total, 95), "p99": pct(total, 99)},
            "limits_ms": {"p50": 50, "p95": 100, "p99": 200}}


def _clone(erp, table, key, value, **changes):
    cols = [c["name"] for c in erp.q(f"PRAGMA table_info({table})")]
    row = dict(erp.q(f"SELECT * FROM {table} WHERE {key}=?", value)[0])
    row.update(changes)
    erp.x(f"INSERT INTO {table}({','.join(cols)}) VALUES ({','.join('?' * len(cols))})", *[row[c] for c in cols])


def c5_payload():
    sizes = [len(json.dumps(call(a)[0], default=str)) for a in real_args()]
    pushed = {}
    for k in (10, 50, 200):
        erp, tb = fresh()
        for i in range(k):
            sup = f"VX-TST-{i:04d}"
            _clone(erp, "supplier", "sup_cd", "VC-EIN-0042", sup_cd=sup, name=f"Voltway Test Supplier {i:04d}")
            _clone(erp, "ap_inv", "ap_no", "AP/2026/03409", ap_no=f"AP/2026/9{i:04d}", sup_cd=sup)
        erp.db.commit()
        out = tb.call(NAME, {"invoice_no": "4471"})
        pushed[k] = {"bytes": len(json.dumps(out, default=str)), "rows": len(out.get("matches") or []),
                     "says_how_many": "total" in json.dumps(out) or "more" in (out.get("next_step") or "")}
    return {"largest_real_result_bytes": max(sizes), "limit_bytes": PAYLOAD_LIMIT,
            "same_number_from_many_suppliers": pushed}


def c6_timeouts():
    """A busy Ledgerline (ERR-SYS-0503), once (must recover) and three times (must fail inside the contract, with
    the right code and a next_step this server can act on), on every service the tool calls."""
    args = {"invoice_no": "4471", "supplier": "Voltway Cells"}
    base = call(args)[0]
    rows = []
    for svc in SPEC["services"]:
        for mode in ("error_before",):
            for times in (1, 3):
                out = call(args, faults={svc: {"mode": mode, "times": times}})[0]
                if times == 1:
                    ok = out == base
                    why = "" if ok else "a single fault was not recovered by the retry"
                else:
                    p = contract_problem(out)
                    code_ok = out.get("ok") is False and out.get("ledgerline_code") in ("ERR-SYS-0503", "TIMEOUT")
                    ok = p is None and code_ok
                    why = "" if ok else (p or ("answered as if nothing failed: " + (out.get("next_step") or "")[:110]
                                               if out.get("ok") else f"code {out.get('ledgerline_code')}"))
                rows.append({"service": svc, "fault": mode, "times": times, "pass": ok, "why": why,
                             "result": out if not ok else None})
    return {"tests": len(rows), "passed": sum(r["pass"] for r in rows),
            "failed": [{k: r[k] for k in ("service", "fault", "times", "why")} for r in rows if not r["pass"]],
            "failed_results": [r["result"] for r in rows if not r["pass"]][:2]}


def c8_regression():
    r = subprocess.run([sys.executable, str(HERE / "tests" / "test_explain_hold.py")], capture_output=True, text=True)
    passed = r.stdout.count("PASS ")
    total = passed + (0 if r.returncode == 0 else 1)
    return {"tests_passed": passed, "tests_run": total, "all_pass": r.returncode == 0,
            "failure": r.stderr.strip().splitlines()[-1] if r.returncode else ""}


def c9_mcp():
    env = {**os.environ, "FASTMCP_SHOW_CLI_BANNER": "false", "FASTMCP_LOG_LEVEL": "ERROR"}
    p = subprocess.Popen([sys.executable, str(HERE / "serve_explain_hold.py"), "--user", USER], stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, env=env, bufsize=1)

    def rpc(msg):
        p.stdin.write(json.dumps(msg) + "\n")
        p.stdin.flush()
        if "id" not in msg:
            return None
        while True:
            m = json.loads(p.stdout.readline())
            if m.get("id") == msg["id"]:
                return m
    checks = {}
    try:
        init = rpc({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
            "protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "a4-part4", "version": "1"}}})
        checks["initialize agrees 2025-06-18"] = init["result"]["protocolVersion"] == "2025-06-18"
        rpc({"jsonrpc": "2.0", "method": "notifications/initialized"})
        checks["ping answers {}"] = rpc({"jsonrpc": "2.0", "id": 2, "method": "ping"}).get("result") == {}
        tl = rpc({"jsonrpc": "2.0", "id": 3, "method": "tools/list"})["result"]["tools"]
        t = tl[0]
        checks["tools/list: one tool with name, description, inputSchema"] = (
            len(tl) == 1 and t["name"] == NAME and bool(t.get("description")) and "inputSchema" in t)
        try:
            jsonschema.Draft202012Validator.check_schema(t["inputSchema"])
            jsonschema.Draft202012Validator.check_schema(t["outputSchema"])
            checks["inputSchema and outputSchema are valid JSON Schema"] = True
        except jsonschema.SchemaError:
            checks["inputSchema and outputSchema are valid JSON Schema"] = False
        ok = rpc({"jsonrpc": "2.0", "id": 4, "method": "tools/call",
                  "params": {"name": NAME, "arguments": {"invoice_no": "4471", "supplier": "Voltway Cells"}}})["result"]
        v = jsonschema.Draft202012Validator(t["outputSchema"])
        checks["a good call: isError false, structuredContent fits outputSchema"] = (
            ok.get("isError") is False and not list(v.iter_errors(ok["structuredContent"])))
        checks["content text and structuredContent say the same"] = json.loads(ok["content"][0]["text"]) == ok["structuredContent"]
        bad = rpc({"jsonrpc": "2.0", "id": 5, "method": "tools/call",
                   "params": {"name": NAME, "arguments": {"invoice_no": "AP/2026/99999"}}})["result"]
        checks["a failed call: isError true, with the error contract"] = (
            bad.get("isError") is True and {"error", "next_step", "ledgerline_code"} <= set(bad["structuredContent"]))
        wrong = rpc({"jsonrpc": "2.0", "id": 6, "method": "tools/call",
                     "params": {"name": NAME, "arguments": {"invoice_no": 4471}}})
        checks["a wrong argument type: refused, not crashed"] = (
            "error" in wrong or wrong.get("result", {}).get("isError") is True)
        um = rpc({"jsonrpc": "2.0", "id": 7, "method": "tools/frobnicate"})
        checks["an unknown method: JSON-RPC error -32601"] = um.get("error", {}).get("code") == -32601
        ut = rpc({"jsonrpc": "2.0", "id": 8, "method": "tools/call", "params": {"name": "no_such_tool", "arguments": {}}})
        checks["an unknown tool: refused"] = "error" in ut or ut.get("result", {}).get("isError") is True
    finally:
        p.stdin.close()
        try:
            p.wait(10)
        except subprocess.TimeoutExpired:
            p.kill()
    return {"checks": len(checks), "passed": sum(checks.values()), "detail": checks}


if __name__ == "__main__":
    label = sys.argv[1] if len(sys.argv) > 1 else ""
    res = {"criteria": {}}
    for key, fn in [("1 schema", c1_schema), ("2 reliability", c2_reliability), ("4 latency", c3_latency),
                    ("5 payload", c5_payload), ("7 timeouts", c6_timeouts), ("8 regression", c8_regression),
                    ("9 mcp compliance", c9_mcp)]:
        t0 = time.perf_counter()
        res["criteria"][key] = fn()
        print(f"\n## {key}  ({time.perf_counter() - t0:.1f} s)")
        print(json.dumps(res["criteria"][key], indent=1, default=str, ensure_ascii=False)[:2500])
    out = f"production_{label}.json" if label else "production.json"
    with open(HERE / "logs" / out, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1, default=str, ensure_ascii=False)
    print(f"\nwritten logs/{out}")
