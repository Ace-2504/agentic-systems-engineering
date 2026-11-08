"""Opens every file with code and checks (1) every gold quote is at the location given, (2) every must_contain string is
in the gold source, (3) every number or code in every document is in facts.jsonl. Writes check.txt."""
import os, sys, json, re, email, hashlib
import pypdf, docx, openpyxl

OUT = sys.argv[1]; DOCS = os.path.join(OUT, "docs")
norm = lambda s: re.sub(r"\s+", " ", str(s)).strip()
lines = []; ok = True
def log(s): lines.append(s); print(s)

def pdf_pages(f): return [norm(p.extract_text()) for p in pypdf.PdfReader(f).pages]
def docx_sections(f):
    secs, cur = {}, "(top)"
    for p in docx.Document(f).paragraphs:
        if p.style.name.startswith("Heading") or p.style.name == "Title":
            cur = norm(p.text); secs.setdefault(cur, ""); continue
        secs[cur] = secs.get(cur, "") + " " + norm(p.text)
    return {k: norm(v) for k, v in secs.items()}
def xlsx_row(f, sheet, row):
    ws = openpyxl.load_workbook(f, data_only=True)[sheet]
    return norm(" | ".join("" if c.value is None else str(c.value) for c in ws[row]))
def eml_body(f):
    m = email.message_from_binary_file(open(f, "rb")); return norm(m.get_payload(decode=True).decode())

def location_text(s):
    f = os.path.join(DOCS, s["file"])
    if not os.path.exists(f): return None, "file missing"
    if f.endswith(".pdf"):
        pages = pdf_pages(f)
        if not 1 <= s["page"] <= len(pages): return None, "page out of range"
        t = pages[s["page"] - 1]
        return t, ("" if norm(s["section"]) in t or any(norm(s["section"]) in p for p in pages) else "section heading not found")
    if f.endswith(".docx"):
        secs = docx_sections(f); return secs.get(norm(s["section"])), ("" if norm(s["section"]) in secs else "section not found")
    if f.endswith(".xlsx"): return xlsx_row(f, s["sheet"], s["row"]), ""
    if f.endswith(".eml"): return eml_body(f), ""
    return norm(open(f).read()), ""

log("CHECK 1 - gold quotes and must_contain strings (questions.jsonl)")
for line in open(os.path.join(OUT, "questions.jsonl")):
    q = json.loads(line); texts = []
    if not q["gold_sources"]:
        log(f"  {q['id']} {q['type']}: no gold sources (not_in_docs) - OK" if q["type"] == "not_in_docs" else f"  {q['id']}: NO SOURCES - FAIL")
        continue
    for s in q["gold_sources"]:
        t, warn = location_text(s)
        where = f"page {s['page']}" if "page" in s else (f"sheet {s['sheet']} row {s['row']}" if "sheet" in s else f"section '{s['section']}'")
        found = t is not None and norm(s["quote"]) in t
        words = len(s["quote"].split())
        ok &= found and words <= 25 and not warn
        log(f"  {q['id']} {q['type']}: quote in {s['file']} at {where}: {'FOUND' if found else 'NOT FOUND'}; {words} words{'; ' + warn if warn else ''}")
        texts.append(t or "")
    for m in q["must_contain"]:
        hit = any(m in t for t in texts); ok &= hit
        log(f"  {q['id']} must_contain '{m}': {'FOUND' if hit else 'NOT FOUND'}")
log(f"All quotes found: {'YES' if ok else 'NO'}")

log("")
log("CHECK 2 - every number and code in every document is in facts.jsonl")
facts = [json.loads(l) for l in open(os.path.join(OUT, "facts.jsonl"))]
TOK = re.compile(r"\d[\d,]*(?:\.\d+)?")
def toks(s):
    out = set()
    for t in TOK.findall(s):
        t = t.replace(",", "").rstrip(".")
        if re.fullmatch(r"\d+\.0", t): t = t[:-2]
        out.add(t.lstrip("0") or "0")
    return out
reg = set()
for fct in facts: reg |= toks(fct["fact"] + " " + fct["page_or_section"])
def doc_text(f):
    if f.endswith(".pdf"):
        return " ".join(re.sub(r"Page \d+ of \d+", "", p) for p in pdf_pages(f))
    if f.endswith(".docx"):
        return " ".join(re.sub(r"^\d+\.\s", "", p.text) for p in docx.Document(f).paragraphs)
    if f.endswith(".xlsx"):
        wb = openpyxl.load_workbook(f, data_only=True)
        return " ".join(str(c.value) for ws in wb for r in ws.iter_rows() for c in r if c.value is not None)
    if f.endswith(".eml"): return eml_body(f)
    return open(f).read()
bad_total = 0; nfiles = 0
for root, _, fs in os.walk(DOCS):
    for fn in sorted(fs):
        f = os.path.join(root, fn); nfiles += 1
        txt = doc_text(f)
        txt = re.sub(r"(?m)^\s*\d+(\.\d+)?\.?\s", " ", txt)          # list and section numbers at line start
        missing = sorted(t for t in toks(txt) if t not in reg)
        if missing:
            bad_total += len(missing); log(f"  {os.path.relpath(f, DOCS)}: not in registry: {missing}")
log(f"  {nfiles} files scanned; numbers or codes missing from the registry: {bad_total}")
ok2 = bad_total == 0

log("")
log("CHECK 3 - planted byte-identical duplicate")
h = {}
for root, _, fs in os.walk(DOCS):
    for fn in fs:
        p = os.path.join(root, fn); h.setdefault(hashlib.sha256(open(p, "rb").read()).hexdigest(), []).append(os.path.relpath(p, DOCS))
dups = [v for v in h.values() if len(v) > 1]
for v in dups: log(f"  identical: {v}")
log(f"  duplicate groups: {len(dups)}")

log("")
log(f"RESULT: quotes {'all found' if ok else 'FAILURES'}; registry {'complete' if ok2 else 'INCOMPLETE'}")
open(os.path.join(OUT, "check.txt"), "w").write("\n".join(lines) + "\n")
