"""explain_hold: why a supplier invoice is on hold, who may release each hold, and by when (read only).

Input and output are described in tool.json next to this file.
Services: ap_inv_list (find the invoice), ap_inv_get (its holds), usr_get (check the people who may release)."""
import datetime as dt
import re

from ledgerline.agent.tools import ToolError, _ledgerline
from ledgerline.erp.engine import ServiceTimeout

# --------------------------------------------------------------------------- tables Ledgerline has no read service for
# Who may release each hold. Copied from AP policy POL-AP-001 v2.1, section 4.1 (effective 1 April 2026).
# Ledgerline keeps this in table ap_hold, which only the release check reads. Update this table when the policy changes.
RELEASERS = {
    "H-PRC": [("DOKAFOR", "PUR-MGR"), ("VNAIR", "FIN-CTRL")],
    "H-QTY": [("GPAWAR", "STORES"), ("VNAIR", "FIN-CTRL")],
    "H-GRN": [("PSHAH", "AP-EXEC"), ("VNAIR", "FIN-CTRL")],   # accounts payable, once the goods receipt is posted
    "H-DUP": [("VNAIR", "FIN-CTRL")],
}
ROLE_WORDS = {"PUR-MGR": "purchase manager", "FIN-CTRL": "financial controller", "STORES": "stores",
              "AP-EXEC": "accounts payable"}

# Ledgerline's invoice status codes, in words. "PO" here means posted (clear to pay), not purchase order.
STATUS_WORDS = {"HD": "on hold", "PA": "waiting for approval", "PO": "clear to pay", "PD": "paid",
                "RJ": "rejected", "CN": "cancelled"}

EARLY_DAYS = 7   # paying more than 7 days before the due date is an early payment (needs the financial controller)


# --------------------------------------------------------------------------- small helpers
def rupees(x):
    """1332.8 -> 'Rs.1,332.80'; 28308672 -> 'Rs.2,83,08,672' (Indian grouping: 3 digits, then 2s)."""
    whole, paise = f"{x:.2f}".split(".")
    head, tail = whole[:-3], whole[-3:]
    while len(head) > 2:
        tail, head = head[-2:] + "," + tail, head[:-2]
    text = (head + "," + tail) if head else tail
    return "Rs." + text + ("" if paise == "00" else "." + paise)


def either(names):
    """['A', 'B Pvt. Ltd.'] -> 'A or B Pvt. Ltd' (no double full stop when a sentence ends after it)."""
    return " or ".join(n.rstrip(".") for n in names)


def count(n):
    """18000 -> '18,000' (Indian grouping)."""
    return rupees(n)[3:]


def what_is_wrong(code, detail):
    """Rewrite Ledgerline's hold text (e.g. 'QTY 18000 VS OPEN 17700') in words."""
    m = re.fullmatch(r"QTY (\d+) VS OPEN (\d+)", detail or "")
    if code == "H-QTY" and m:
        return f"{count(int(m[1]))} billed, {count(int(m[2]))} accepted"
    m = re.fullmatch(r"RATE ([\d.]+) VS PO ([\d.]+) \(\+([\d.]+)%\)", detail or "")
    if code == "H-PRC" and m:
        return f"billed at {rupees(float(m[1]))} each against the order's {rupees(float(m[2]))} (+{m[3]}%)"
    m = re.fullmatch(r"NO GRN FOR (\S+)", detail or "")
    if code == "H-GRN" and m:
        return f"no goods receipt posted yet for order {m[1]}"
    m = re.fullmatch(r"LIKE (\S+)", detail or "")
    if code == "H-DUP" and m:
        return f"looks like a duplicate of {m[1]}"
    return f"Ledgerline says: {detail}"            # a format we have not seen: pass it on, do not guess


def fridays(today, due):
    """this_friday: the next run whose Thursday cut-off has not passed. last_run: the last Friday on or before due."""
    t, d = dt.date.fromisoformat(today), dt.date.fromisoformat(due)
    this_friday = t + dt.timedelta(days=(4 - t.weekday()) % 7)
    if this_friday - dt.timedelta(days=1) < t:     # today is Friday: today's cut-off was yesterday
        this_friday += dt.timedelta(days=7)
    last_run = d - dt.timedelta(days=(d.weekday() - 4) % 7)
    return this_friday, last_run


# --------------------------------------------------------------------------- the three steps
def find_invoice(s, invoice_no, supplier):
    """Turn what the user said into exactly one AP number, or a list of matches to ask about."""
    if invoice_no.upper().startswith("AP/"):
        return invoice_no.upper(), None
    rows = _ledgerline(s, "ap_inv_list", sup_inv_no=invoice_no)["rows"]
    # ap_inv_list matches part of the number (447 finds 4471), so keep only the exact number.
    exact = [r for r in rows if r["sup_inv_no"].strip().upper() == invoice_no.strip().upper()]
    if not exact:
        near = ", ".join(sorted({r["sup_inv_no"] for r in rows}))
        raise ToolError(f"No invoice numbered {invoice_no} in Ledgerline.",
                        f"Check the number with the user{'; close numbers: ' + near if near else ''}. "
                        "It may not be entered yet.")
    if supplier:
        picked = [r for r in exact if supplier.lower() in r["sup_name"].lower()]
        if not picked:
            names = either(r["sup_name"] for r in exact)
            raise ToolError(f"No invoice {invoice_no} from a supplier matching '{supplier}'.",
                            f"Invoice {invoice_no} exists from {names}. Ask the user which one.")
        exact = picked
    if len(exact) > 1:
        return None, exact
    return exact[0]["ap_no"], None


def releasers(s, code):
    """The people who may release this hold, checked against Ledgerline. Returns (people, problems)."""
    people, problems = [], []
    for user_id, role in RELEASERS.get(code, []):
        try:
            u = _ledgerline(s, "usr_get", user_id=user_id)
        except ToolError as e:
            if e.code != "ERR-SEC-0003":      # only "NO SUCH USER" means the person has left; a busy or failing
                raise                          # Ledgerline is an outage, reported as one, not a change of policy
            problems.append(f"{user_id} is no longer in Ledgerline")
            continue
        if u.get("role_cd") != role:
            problems.append(f"{u.get('name', user_id)} no longer has the {ROLE_WORDS[role]} role")
            continue
        people.append({"name": u["name"], "role": ROLE_WORDS[role]})
    return people, problems


def payment(status, holds, today, due):
    if status in ("paid", "rejected", "cancelled"):
        return None
    this_friday, last_run = fridays(today, due)
    why_not = None
    if holds:
        why_not = "on hold; nothing is paid while an invoice is on hold"
    elif status == "waiting for approval":
        why_not = "waiting for approval; it cannot go into a run until it is approved"
    elif (dt.date.fromisoformat(due) - this_friday).days > EARLY_DAYS:
        days = (dt.date.fromisoformat(due) - this_friday).days
        why_not = f"it would be paid {days} days early; that needs Vikram Nair's approval and a reason"
    if last_run < this_friday and why_not:
        why_not += f"; it is already past its last run before the due date ({last_run.isoformat()})"
    return {"last_run": last_run.isoformat(), "cutoff": (last_run - dt.timedelta(days=1)).isoformat(),
            "this_friday": this_friday.isoformat(), "payable_this_friday": why_not is None, "why_not": why_not}


# --------------------------------------------------------------------------- the tool
def run(s, invoice_no, supplier=None):
    """The tool. A lost Ledgerline reply (after the reads' own retries) comes back in the error contract with a
    next_step written for a read-only tool: it is safe to ask again."""
    try:
        return explain(s, invoice_no, supplier)
    except ServiceTimeout as e:
        raise ToolError(f"Ledgerline did not reply in time ({str(e).split(':')[0]}), even after retrying.",
                        "This tool only reads, so it is safe to call it again in a minute. "
                        "If it fails again, tell the user Ledgerline is not answering.", "TIMEOUT")


def explain(s, invoice_no, supplier=None):
    ap_no, matches = find_invoice(s, invoice_no, supplier)
    if matches:
        return {"ok": True,
                "matches": [{"ap_no": r["ap_no"], "supplier": r["sup_name"], "invoice_date": r["inv_dt"],
                             "amount": r["gross"], "status": STATUS_WORDS.get(r["status"], r["status"])}
                            for r in matches],
                "next_step": f"{len(matches)} suppliers used invoice number {invoice_no}. Ask the user which: "
                             + either(r["sup_name"] for r in matches) + "."}

    try:
        inv = _ledgerline(s, "ap_inv_get", ap_no=ap_no)
    except ToolError as e:
        if e.code == "ERR-AP-0001":
            raise ToolError(f"No invoice {ap_no} in Ledgerline.", "Check the AP number with the user.", e.code)
        raise
    # The supplier's name is not in ap_inv_get's reply; ap_inv_list has it.
    rows = _ledgerline(s, "ap_inv_list", sup_cd=inv["sup_cd"], sup_inv_no=inv["sup_inv_no"])["rows"]
    name = next((r["sup_name"] for r in rows if r["ap_no"] == inv["ap_no"]), inv["sup_cd"])

    holds, problems = [], []
    for h in inv["holds"]:                            # the full list; inv["hold_cd"] shows only the first hold
        if h["released_on"]:
            continue
        people, issues = releasers(s, h["hold_cd"])
        problems += issues
        holds.append({"code": h["hold_cd"], "what_is_wrong": what_is_wrong(h["hold_cd"], h["detail"]),
                      "on_hold_since": h["put_on"][:10], "may_release": people})

    status = STATUS_WORDS.get(inv["status"], inv["status"])
    out = {"ok": True, "supplier": name, "ap_no": inv["ap_no"], "status": status,
           "invoice_no": inv["sup_inv_no"], "amount": inv["gross"], "due_date": inv["due_dt"],
           "payment": payment(status, holds, s.erp.today, inv["due_dt"]), "holds": holds}
    if problems:
        out["next_step"] = ("AP policy 4.1 is out of date: " + "; ".join(problems)
                            + ". Ask Vikram Nair who releases these holds now.")
    return out
