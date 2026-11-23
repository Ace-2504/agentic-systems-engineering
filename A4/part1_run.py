"""A4 Part 1: load explain_hold next to the shipped tools, lint it, call it, and measure what it returns.

    python part1_run.py            # prints the trace and writes logs/part1.json
"""
import json

import jsonschema

from a4_setup import TOOL, USER, load_tool, new_erp
from ledgerline.course.l4 import lint_tool, validate_args
from ledgerline.toolbox import SPECS, Toolbox

name = load_tool()
spec = SPECS[name].spec
out_validator = jsonschema.Draft202012Validator(spec["output_schema"])
log = {"lint": lint_tool(name), "cases": []}
print("lint_tool:", log["lint"])
print("jsonschema on {'invoice_no': 4471}:", validate_args(name, {"invoice_no": 4471}))


def envelope_bytes(erp, since):
    """Bytes of every legacy reply the tool caused, in Ledgerline's own {rc, err_cd, msg, data} envelope."""
    recs = [r for r in erp.calls if r.seq > since]
    sizes = [len(json.dumps({"rc": r.rc, "err_cd": r.err_cd, "msg": r.msg, "data": r.data}, default=str)) for r in recs]
    return [r.svc for r in recs], sizes


def case(label, args, faults=None, before=None):
    erp = new_erp(faults)
    if before:
        before(erp)
    tb = Toolbox(erp, USER, names=[name])
    n0 = len(erp.calls)
    out = tb.call(name, args)
    svcs, sizes = envelope_bytes(erp, n0)
    errs = [e.message for e in out_validator.iter_errors(out)]
    row = {"label": label, "args": args, "services_called": svcs, "service_bytes": sum(sizes),
           "result_bytes": len(json.dumps(out, default=str)), "output_schema_violations": errs, "result": out}
    log["cases"].append(row)
    print(f"\n## {label}\nargs: {json.dumps(args)}")
    print(f"Ledgerline calls ({len(svcs)}): {', '.join(svcs) or 'none'} · {sum(sizes):,} bytes in envelopes"
          f" -> {row['result_bytes']:,} bytes returned · output-schema violations: {len(errs)}")
    print(json.dumps(out, indent=1, default=str)[:1800])
    return out


def role_changed(erp):
    erp.x("UPDATE app_user SET role_cd='PUR-EXEC' WHERE user_id='GPAWAR'")
    erp.db.commit()


case("happy path: Voltway Cells' 4471", {"invoice_no": "4471", "supplier": "Voltway Cells"})
case("happy path by AP number", {"invoice_no": "AP/2026/03390"})
case("business answer, not an error: two suppliers used 4471", {"invoice_no": "4471"})
case("refused at the door: wrong type", {"invoice_no": 4471})
case("refused at the door: missing argument", {})
case("refused by Ledgerline: unknown AP number", {"invoice_no": "AP/2026/99999"})
case("refused by the tool: no invoice with that number", {"invoice_no": "9999"})
case("refused by the tool: number exists, supplier does not match", {"invoice_no": "4471", "supplier": "Acme"})
case("Ledgerline busy once: retried, then answered", {"invoice_no": "AP/2026/03390"},
     faults={"ap_inv_get": {"mode": "error_before", "times": 1}})
case("Ledgerline busy three times: retries used up", {"invoice_no": "AP/2026/03390"},
     faults={"ap_inv_get": {"mode": "error_before", "times": 3}})
case("Ledgerline reply lost three times: retries used up", {"invoice_no": "AP/2026/03390"},
     faults={"ap_inv_get": {"mode": "timeout_after_commit", "times": 3}})
case("policy table out of date: Ganesh no longer has the stores role", {"invoice_no": "AP/2026/03390"}, before=role_changed)

with open("logs/part1.json", "w") as f:
    json.dump(log, f, indent=1, default=str)
print("\nwritten logs/part1.json")
