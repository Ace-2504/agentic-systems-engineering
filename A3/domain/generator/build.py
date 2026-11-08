import os, sys, json, shutil, io
from xml.sax.saxutils import escape
from email.message import EmailMessage
sys.path.insert(0, os.path.dirname(__file__))
from content import F, P, TODAY, CO
from docs_text import PDFS, DOCX, XLSX, EML, MD

OUT = sys.argv[1]
DOCS = os.path.join(OUT, "docs")
shutil.rmtree(DOCS, ignore_errors=True)
os.makedirs(DOCS)

def path(key):
    p = os.path.join(DOCS, P[key]); os.makedirs(os.path.dirname(p), exist_ok=True); return p

# ------------------------------------------------------------------ PDF
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle

BODY = ParagraphStyle("b", fontName="Helvetica", fontSize=10.5, leading=15, spaceAfter=7)
H1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=13, leading=17, spaceBefore=12, spaceAfter=6)
H2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, leading=15, spaceBefore=6, spaceAfter=4)
TITLE = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=18, leading=23, spaceAfter=10)
CELL = ParagraphStyle("c", fontName="Helvetica", fontSize=9.5, leading=12.5)

def pdf(key, spec):
    meta, blocks = spec
    class NC(canvas.Canvas):
        def __init__(self, *a, **k):
            super().__init__(*a, **k); self._pages = []
        def showPage(self):
            self._pages.append(dict(self.__dict__)); self._startPage()
        def save(self):
            n = len(self._pages)
            for st in self._pages:
                self.__dict__.update(st)
                self.setFont("Helvetica", 8.5); self.setFillColor(colors.grey)
                self.drawString(18*mm, 287*mm, CO.upper())
                self.drawRightString(192*mm, 287*mm, f"{meta['code']} {meta['version']}")
                if "CONFIDENTIAL" in meta["status"]:
                    self.setFillColor(colors.red); self.drawCentredString(105*mm, 287*mm, "CONFIDENTIAL")
                    self.setFillColor(colors.grey)
                self.drawString(18*mm, 10*mm, f"{meta['code']} {meta['title']}")
                self.drawRightString(192*mm, 10*mm, f"Page {self._pageNumber} of {n}")
                super().showPage()
            super().save()
    story = [Paragraph(escape(meta["title"]), TITLE)]
    rows = [["Document", meta["code"]], ["Version", meta["version"]], ["Effective from", meta["effective"]],
            ["Owner", meta["owner"]], ["Approved by", meta["approver"]], ["Status", meta["status"]]]
    t = Table([[Paragraph(escape(a), CELL), Paragraph(escape(b), CELL)] for a, b in rows], colWidths=[40*mm, 120*mm])
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, colors.grey), ("BACKGROUND", (0, 0), (0, -1), colors.whitesmoke)]))
    story += [t, Spacer(1, 8)]
    for kind, val in blocks:
        if kind == "h1": story.append(Paragraph(escape(val), H1))
        elif kind == "h2": story.append(Paragraph(escape(val), H2))
        elif kind == "p": story.append(Paragraph(escape(val), BODY))
        elif kind == "table":
            w = 174*mm / len(val[0])
            tb = Table([[Paragraph(escape(str(c)), CELL) for c in r] for r in val], colWidths=[w]*len(val[0]), repeatRows=1)
            tb.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
                                    ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
            story += [tb, Spacer(1, 8)]
    doc = BaseDocTemplate(path(key), pagesize=A4, invariant=1, title=f"{meta['code']} {meta['title']} {meta['version']}",
                          author=CO, leftMargin=18*mm, rightMargin=18*mm, topMargin=20*mm, bottomMargin=18*mm)
    doc.addPageTemplates([PageTemplate(id="p", frames=[Frame(18*mm, 18*mm, 174*mm, 259*mm)])])
    doc.build(story, canvasmaker=NC)

for k, spec in PDFS.items():
    pdf(k, spec)

# ------------------------------------------------------------------ DOCX
import docx
for k, (title, secs) in DOCX.items():
    d = docx.Document()
    d.core_properties.title = title; d.core_properties.author = CO
    d.add_heading(title, 0)
    d.add_paragraph(f"{CO} | Procedures and forms")
    for head, paras in secs:
        d.add_heading(head, 1)
        for p in paras:
            d.add_paragraph(p)
    d.save(path(k))
# byte-identical duplicate
shutil.copyfile(path("PRC03"), path("PRC03DUP"))

# ------------------------------------------------------------------ XLSX
import openpyxl
from openpyxl.styles import Font
for k, sheets in XLSX.items():
    wb = openpyxl.Workbook(); wb.remove(wb.active)
    for name, rows in sheets.items():
        ws = wb.create_sheet(name)
        for r in rows: ws.append(r)
        for c in ws[1]: c.font = Font(bold=True)
        ws.freeze_panes = "A2"
        for col in ws.columns:
            ws.column_dimensions[col[0].column_letter].width = min(60, max(12, max(len(str(c.value or "")) for c in col) + 2))
    wb.properties.creator = CO
    wb.save(path(k))

# ------------------------------------------------------------------ EML and MD
for k, (frm, to, date, subj, body) in EML.items():
    m = EmailMessage(); m["From"] = frm; m["To"] = to; m["Date"] = date; m["Subject"] = subj
    m["Message-ID"] = f"<{k.lower()}.nbc@northbridgecycles.example>"; m.set_content(body)
    open(path(k), "wb").write(m.as_bytes())
for k, text in MD.items():
    open(path(k), "w").write(text)

# ------------------------------------------------------------------ facts.jsonl
with open(os.path.join(OUT, "facts.jsonl"), "w") as f:
    for fid, text, fkey, sec in F:
        f.write(json.dumps({"id": fid, "fact": text, "file": ("README.md" if fkey == "README" else "docs/" + P[fkey]),
                            "page_or_section": sec}, ensure_ascii=False) + "\n")
print("built", sum(len(fs) for _, _, fs in os.walk(DOCS)), "files")
