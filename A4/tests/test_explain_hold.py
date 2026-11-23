"""Tests for explain_hold (A4 Part 1, step 6). Plain asserts: run with `python tests/test_explain_hold.py`
or with pytest. Each test gets a fresh Ledgerline (fin_payables + my capstone's records), as Priya Shah (PSHAH)."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import jsonschema                                           # noqa: E402

from a4_setup import TOOL, USER, load_tool, new_erp         # noqa: E402
from ledgerline.erp.engine import SERVICES                   # noqa: E402
from ledgerline.toolbox import SPECS, Toolbox                # noqa: E402

NAME = load_tool()
OUT = jsonschema.Draft202012Validator(SPECS[NAME].spec["output_schema"])


def call(args, faults=None):
    erp = new_erp(faults)
    out = Toolbox(erp, USER, names=[NAME]).call(NAME, args)
    assert not list(OUT.iter_errors(out)), f"output schema broken: {[e.message for e in OUT.iter_errors(out)]}"
    return out, erp


def assert_contract(out, code=None):
    assert out["ok"] is False
    assert out["error"] and out["next_step"], "every failure says what went wrong and what to do"
    assert "ledgerline_code" in out
    if code is not None:
        assert out["ledgerline_code"] == code


def test_happy_path_two_holds_who_and_when():
    out, erp = call({"invoice_no": "4471", "supplier": "Voltway Cells"})
    assert out["ok"] and out["ap_no"] == "AP/2026/03390" and out["status"] == "on hold"
    assert [h["code"] for h in out["holds"]] == ["H-QTY", "H-PRC"], "both holds, not just the one the list shows"
    qty, prc = out["holds"]
    assert qty["what_is_wrong"] == "18,000 billed, 17,700 accepted"
    assert "+4.39%" in prc["what_is_wrong"]
    assert {p["name"] for p in qty["may_release"]} == {"Ganesh Pawar", "Vikram Nair"}
    assert {p["name"] for p in prc["may_release"]} == {"Daniel Okafor", "Vikram Nair"}
    pay = out["payment"]
    assert (pay["last_run"], pay["cutoff"], pay["this_friday"]) == ("2026-11-13", "2026-11-12", "2026-10-30")
    assert pay["payable_this_friday"] is False and "on hold" in pay["why_not"]
    assert all(SERVICES[r.svc].kind == "read" for r in erp.calls), "a read-only tool calls only read services"


def test_clean_result_not_the_envelope():
    out, _ = call({"invoice_no": "AP/2026/03390"})
    for legacy in ("rc", "err_cd", "msg", "data", "hold_cd", "sup_cd", "due_dt"):
        assert legacy not in out


def test_business_answer_two_suppliers_same_number():
    out, _ = call({"invoice_no": "4471"})
    assert out["ok"] is True, "two matches is an answer, not an error"
    assert {m["supplier"] for m in out["matches"]} == {"Voltway Cells Pvt. Ltd.", "Voltway Paints & Coatings"}
    assert "holds" not in out and "Ask the user which" in out["next_step"]


def test_refused_at_the_door_wrong_type():
    out, erp = call({"invoice_no": 4471})
    assert_contract(out, "")
    assert not erp.calls, "a bad argument never reaches Ledgerline"


def test_refused_at_the_door_missing_argument():
    out, erp = call({})
    assert_contract(out, "")
    assert not erp.calls


def test_refused_by_ledgerline_unknown_ap_number():
    out, _ = call({"invoice_no": "AP/2026/99999"})
    assert_contract(out, "ERR-AP-0001")


def test_unknown_invoice_number():
    out, _ = call({"invoice_no": "9999"})
    assert_contract(out, "")


def test_ledgerline_busy_retried_then_given_up():
    ok, _ = call({"invoice_no": "AP/2026/03390"}, faults={"ap_inv_get": {"mode": "error_before", "times": 1}})
    assert ok["ok"] is True, "one busy reply is retried"
    out, erp = call({"invoice_no": "AP/2026/03390"}, faults={"ap_inv_get": {"mode": "error_before", "times": 3}})
    assert_contract(out, "ERR-SYS-0503")
    assert sum(r.svc == "ap_inv_get" for r in erp.calls) == 3, "one try and two retries, then stop"



def test_busy_usr_get_is_an_outage_not_a_policy_change():
    """Ledgerline busy on usr_get is reported as an outage, never as 'GPAWAR is no longer in Ledgerline'."""
    out, _ = call({"invoice_no": "AP/2026/03390"}, faults={"usr_get": {"mode": "error_before", "times": 3}})
    assert_contract(out, "ERR-SYS-0503")
    assert "no longer" not in json.dumps(out)


def test_a_person_who_really_left_is_still_reported():
    """A person Ledgerline does not know (ERR-SEC-0003) is dropped from may_release, with the policy note."""
    erp = new_erp()
    erp.x("DELETE FROM app_user WHERE user_id='GPAWAR'")
    erp.db.commit()
    out = Toolbox(erp, USER, names=[NAME]).call(NAME, {"invoice_no": "AP/2026/03390"})
    assert out["ok"] is True and "GPAWAR is no longer in Ledgerline" in out["next_step"]
    assert {p["name"] for p in out["holds"][0]["may_release"]} == {"Vikram Nair"}


def test_lost_reply_gives_a_next_step_this_server_can_follow():
    """A lost reply gives a next_step for this read-only tool, never a tool this MCP server does not offer."""
    for svc in ("ap_inv_list", "ap_inv_get", "usr_get"):
        out, _ = call({"invoice_no": "4471", "supplier": "Voltway Cells"},
                      faults={svc: {"mode": "timeout_after_commit", "times": 3}})
        assert_contract(out, "TIMEOUT")
        assert "order_status" not in out["next_step"] and "safe to call it again" in out["next_step"]

if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_")]
    for n, f in tests:
        f()
        print("PASS", n)
    print(f"{len(tests)} passed")
