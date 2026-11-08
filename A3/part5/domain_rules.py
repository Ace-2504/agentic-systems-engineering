"""A3 Part 5, second pass: helpers shared by the notebook and the CI check (check_retrieval.py).

Rule 10 of Lecture 3 (handle versions and effective dates explicitly) is applied here, on top of the course's parser,
whose checks look for a SUPERSEDED status, an /old/ folder or an ISO date. This dataset writes "Effective from |
1 April 2026" and "Status | Approved" on every version, and puts validity dates inside spreadsheet rows.
"""
import collections
import dataclasses
import json
import pathlib
import re

from ledgerline.course.l3 import corpus as C
from ledgerline.course.l3 import evaluate as E

TODAY = "2026-11-09"  # the dataset's today (domain/README.md)
MONTHS = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august",
                                      "september", "october", "november", "december"], 1)}

# The dataset names each asker in words; the harness needs a role code. None of these is an HR role.
ROLES = {
    "Accounts payable (Priya Shah)": ("AP-EXEC", "Priya Shah, accounts payable"),
    "Purchasing (Emma Clarke)": ("PUR-EXEC", "Emma Clarke, purchasing"),
    "Stores (Ganesh Pawar)": ("STORES-PUNE", "Ganesh Pawar, stores"),
    "Tax manager (Meera Kulkarni)": ("TAX-MGR", "Meera Kulkarni, tax manager"),
    "Financial controller (Vikram Nair)": ("FIN-CTRL", "Vikram Nair, financial controller"),
    "Insurance desk": ("INS-DESK", "the Insurance desk"),
}


def files(root) -> list[str]:
    return sorted(f.replace("\\", "/") for f in C.list_files(root))


def parse(root, parser: str = "structured") -> list:
    return [u for rel in files(root) for u in C.parse_file(root, rel, parser=parser)]


def to_iso(s: str) -> str:
    """'1 April 2026' -> '2026-04-01'; '' if the text holds no such date."""
    m = re.search(r"(\d{1,2}) ([A-Za-z]+) (\d{4})", s or "")
    if not m or m.group(2).lower() not in MONTHS:
        return ""
    return f"{int(m.group(3)):04d}-{MONTHS[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"


def handle_versions(units: list, today: str = TODAY) -> tuple[list, dict]:
    """Rule 10. Per file: read the effective date in any written form; a document not yet in force is marked future;
    of two versions of the same document id that are both in force, the older is marked superseded. Per spreadsheet
    row: a row whose 'Valid until' date has passed, or whose 'Valid from' date is still ahead, says so in its text.
    The marks reach the answer model through the chunk header and the source's status line (corpus.status_line).
    Returns the new units (the course's units are not changed) and a report."""
    by_file = collections.defaultdict(list)
    for u in units:
        by_file[u.file].append(u)
    metas = {}
    for f, us in by_file.items():
        m = dict(us[0].meta)
        if not m.get("effective"):
            for u in us:
                hit = re.search(r"Effective from \| (\d{1,2} [A-Za-z]+ \d{4})", u.text)
                if hit:
                    m["effective"] = to_iso(hit.group(1))
                    break
        m["future"] = bool(m.get("future") or (m.get("effective") and m["effective"] > today))
        metas[f] = m
    groups = collections.defaultdict(list)
    for f, m in metas.items():
        if m.get("doc_id") and m.get("version"):
            groups[m["doc_id"]].append(f)
    superseded = {}
    for doc_id, fs in groups.items():
        live = [f for f in fs if not metas[f]["future"]]
        if len(live) > 1:
            newest = max(live, key=lambda f: (metas[f].get("effective") or "",
                                              [int(x) for x in metas[f]["version"].split(".")]))
            for f in live:
                if f != newest:
                    metas[f]["superseded"] = True
                    superseded[f] = newest
    out, rows = [], []
    for f, us in by_file.items():
        for u in us:
            text = u.text
            if u.fmt in ("xlsx", "csv"):
                until = re.search(r"Valid until: ([^;]+)", text)
                frm = re.search(r"Valid from: ([^;]+)", text)
                if until and to_iso(until.group(1)) and to_iso(until.group(1)) < today:
                    text += f" [NOT IN FORCE TODAY: valid only until {until.group(1).strip()}]"
                    rows.append((f, u.loc, "expired"))
                elif frm and to_iso(frm.group(1)) and to_iso(frm.group(1)) > today:
                    text += f" [NOT YET IN FORCE: valid from {frm.group(1).strip()}]"
                    rows.append((f, u.loc, "future"))
            out.append(dataclasses.replace(u, text=text, meta=metas[f]))
    return out, {"metas": metas, "superseded": superseded, "future": sorted(f for f, m in metas.items() if m["future"]),
                 "rows": rows, "versions": {d: sorted(fs) for d, fs in groups.items() if len(fs) > 1}}


class DomainGolden(E.Golden):
    """The course's Golden reads the Northbridge dump's eval/ folder; this reads my dataset and otherwise does the same
    (questions by id; files with identical bytes count as the same file)."""

    def __init__(self, root, qs, facts):
        import hashlib

        self.root, self.qs, self.facts = pathlib.Path(root), qs, facts
        self.by_id = {q["id"]: q for q in qs}
        self._same, shas = {}, {}
        for rel in files(self.root):
            shas.setdefault(hashlib.sha1((self.root / rel).read_bytes()).hexdigest(), []).append(rel)
        for group in shas.values():
            for r in group:
                self._same[r] = set(group)


def load_golden(path) -> list[dict]:
    """The 12 documentation questions, in the words their askers would type. The asker is mapped to a role code; the
    words are kept in q['asker']."""
    qs = []
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            q = json.loads(line)
            q["asker"] = q["asker_role"]
            q["asker_role"] = ROLES[q["asker"]][0]
            qs.append(q)
    return qs


def confidential_facts(units, facts_path) -> dict:
    """For the leak check: each fact about a confidential file, with that file's rupee amounts as the values that
    must never appear in an answer."""
    conf = sorted({u.file for u in units if u.meta.get("confidential")})
    amounts = {f: sorted(set(re.findall(r"Rs\.\s?\d[\d,]*", " ".join(u.text for u in units if u.file == f))))
               for f in conf}
    out = {}
    for line in pathlib.Path(facts_path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            f = json.loads(line)
            rel = f["file"].removeprefix("docs/")
            if rel in amounts:
                out[f["id"]] = {**f, "file": rel, "needles": amounts[rel]}
    return out
