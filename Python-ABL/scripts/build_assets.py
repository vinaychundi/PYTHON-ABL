from pathlib import Path
import subprocess
from html import escape
from playwright.sync_api import sync_playwright
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from xml.sax.saxutils import escape as xml_escape

ROOT = Path(__file__).resolve().parents[1]
PROGRAMS, DOCS, SHOTS = ROOT / "programs", ROOT / "documentation", ROOT / "screenshots"
SHOTS.mkdir(exist_ok=True)
samples = {
"01_scholarship_allocation.py":"2\nAsha\n88\n80\n75\n90\n90\n180000\nRavi\n68\n70\n65\n72\n80\n300000\n",
"02_warehouse_inventory.py":"2\nLaptop\n50\n10\n45\n12\nMouse\n30\n5\n10\n25\n",
"03_timetable_conflict.py":"2\nMath\nCSM-A\nR101\n9\n10\nPhysics\nCSM-A\nR102\n9\n11\n",
"04_marks_matrix.py":"2\n2\nPython\nMaths\nAsha\n80\n70\nBalu\n40\n60\n",
"05_transaction_audit.py":"3\nT01\n1500\nDEPOSIT\nT01\n60000\nDEPOSIT\nT03\n-50\nCREDIT\n",
"06_academic_risk.py":"2\nRavi\n40\n45\n50\n60\n40\nAnu\n85\n90\n88\n95\n90\n",
"07_festival_audit.py":"3\nA1\n300\nA2\n300\nA1\n300\n1000\n1200\n",
"08_internship_ranking.py":"2\nAnu\n80\n75\n90\nBala\n60\n80\n90\n",
"09_disaster_relief.py":"100\n2\nNorth\n80\n1\nSouth\n50\n2\n",
"10_smart_campus.py":"1\n26CS01\nVinay\n2\n26CS01\n8\n10\n3\n26CS01\n85\n4\n26CS01\nTech Fest\n5\n6\n"
}

# Run each repository program with deterministic sample input and capture its real stdout.
runs = []
for i, program in enumerate(sorted(PROGRAMS.glob("*.py")), 1):
    if program.name not in samples:
        continue
    completed = subprocess.run(
        ["python", str(program)], input=samples[program.name],
        text=True, capture_output=True, timeout=20
    )
    if completed.returncode:
        raise RuntimeError(f"{program.name} failed: {completed.stderr}")
    output = completed.stdout + completed.stderr
    (SHOTS / f"{i:02d}_sample_output.txt").write_text(output, encoding="utf-8")
    runs.append((i, program, output))

# Render the captured, actual program output in Chromium and save genuine browser screenshots.
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
    for i, program, output in runs:
        page.set_content(f"""<!doctype html><html><head><meta charset="utf-8"><style>
        *{{box-sizing:border-box}}body{{margin:0;background:#eef2f7;color:#172033;font-family:Arial,sans-serif}}
        header{{background:#172033;color:#fff;padding:22px 38px;font-size:20px;font-weight:700}}
        main{{padding:30px 38px}}h1{{font-size:24px;margin:0 0 8px}}.meta{{color:#58657a;margin-bottom:22px}}
        .panel{{background:#fff;border:1px solid #d8deea;border-radius:12px;overflow:hidden;margin-bottom:20px}}
        .bar{{background:#e8edf5;padding:12px 18px;font-weight:700}}pre{{margin:0;padding:22px;font:16px/1.6 Consolas,monospace;white-space:pre-wrap;overflow-wrap:anywhere}}
        .success{{color:#147a45;font-weight:700;margin-top:8px}}footer{{color:#6b7485;font-size:13px;margin-top:22px}}
        </style></head><body><header>Python ABL | Execution Evidence</header><main>
        <h1>{i:02d}. {escape(program.name)}</h1>
        <div class="meta">Executed from the GitHub repository source · Python 3.12 · Exit code: 0</div>
        <section class="panel"><div class="bar">Actual program console output</div><pre>{escape(output)}</pre></section>
        <div class="success">✓ Program completed successfully</div>
        <footer>Python Activity-Based Learning · Screenshot captured from Chromium after real program execution</footer>
        </main></body></html>""", wait_until="load")
        page.screenshot(path=str(SHOTS / f"{i:02d}_output.png"), full_page=True)
    browser.close()

styles = getSampleStyleSheet()
title = ParagraphStyle("ABLTitle", parent=styles["Title"], alignment=TA_CENTER, fontSize=19, leading=24)
sub = ParagraphStyle("ABLSub", parent=styles["Normal"], alignment=TA_CENTER, fontSize=11, leading=16)
heading = ParagraphStyle("ABLHeading", parent=styles["Heading2"], fontSize=12, leading=15, spaceBefore=7, spaceAfter=5)
body = ParagraphStyle("ABLBody", parent=styles["BodyText"], fontSize=8.5, leading=11)
story = [
    Spacer(1, 30*mm), Paragraph("PYTHON PROGRAMMING", title),
    Paragraph("ACTIVITY-BASED LEARNING – FINAL REPORT", title), Spacer(1, 10*mm),
    Paragraph("<b>Student:</b> Chundi Vinay Kumar", sub),
    Paragraph("<b>Roll Number:</b> 26001286", sub),
    Paragraph("<b>Branch:</b> CSM &nbsp;&nbsp; <b>Section:</b> 7", sub), PageBreak()
]
for doc in sorted(DOCS.glob("*.md")):
    story.append(Paragraph(xml_escape(doc.stem.replace("_", " ").title()), heading))
    for line in doc.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            story.append(Spacer(1, 3))
        elif line.startswith("#"):
            story.append(Paragraph(xml_escape(line.lstrip("# ").strip()), heading))
        elif line.startswith("- "):
            story.append(Paragraph("• " + xml_escape(line[2:]), body))
        elif line.startswith("```"):
            continue
        else:
            story.append(Paragraph(xml_escape(line), body))
    story.append(Spacer(1, 4*mm))
SimpleDocTemplate(
    str(ROOT / "Python_ABL_Final_Report.pdf"), pagesize=A4,
    rightMargin=17*mm, leftMargin=17*mm, topMargin=16*mm, bottomMargin=16*mm,
    title="Python ABL Final Report"
).build(story)
print(f"Generated the final PDF and {len(runs)} Chromium-captured output screenshots.")
