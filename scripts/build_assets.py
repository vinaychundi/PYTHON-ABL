from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted
from reportlab.lib import colors
from xml.sax.saxutils import escape
import textwrap

ROOT = Path(__file__).resolve().parents[1]
PROGRAMS = ROOT / "programs"
DOCS = ROOT / "documentation"
SHOTS = ROOT / "screenshots"
SHOTS.mkdir(exist_ok=True)

samples = {
    "01_scholarship_allocation.py": "1\nAsha\n88\n80\n75\n90\n90\n180000\n",
    "02_warehouse_inventory.py": "1\nPen\n50\n20\n30\n38\n",
    "03_timetable_conflict.py": "2\nMath\nCSM-A\nR101\n9\n10\nPhysics\nCSM-A\nR102\n9\n11\n",
    "04_marks_matrix.py": "2\n2\nPython\nMaths\nAsha\n80\n70\nBalu\n40\n60\n",
    "05_transaction_audit.py": "2\nT01\n1500\nDEPOSIT\nT01\n60000\nDEPOSIT\n",
    "06_academic_risk.py": "1\nRavi\n40\n45\n50\n60\n40\n",
    "07_festival_audit.py": "2\nA1\n300\nA2\n300\n1000\n1200\n",
    "08_internship_ranking.py": "2\nAnu\n80\n75\n90\nBala\n60\n80\n90\n",
    "09_disaster_relief.py": "100\n2\nNorth\n80\n1\nSouth\n50\n2\n",
    "10_smart_campus.py": "1\n26CS01\nVinay\n2\n26CS01\n8\n10\n3\n26CS01\n85\n4\n26CS01\nTech Fest\n5\n6\n",
}

try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 15)
except OSError:
    font = ImageFont.load_default()

for index, program in enumerate(sorted(PROGRAMS.glob("*.py")), start=1):
    if program.name not in samples:
        continue
    result = subprocess.run(
        ["python", str(program)], input=samples[program.name],
        text=True, capture_output=True, timeout=20
    )
    if result.returncode:
        raise RuntimeError(f"{program.name} failed: {result.stderr}")
    output = result.stdout + result.stderr
    (SHOTS / f"{index:02d}_sample_output.txt").write_text(output, encoding="utf-8")
    lines = []
    for raw in output.splitlines():
        lines.extend(textwrap.wrap(raw, width=105) or [""])
    lines = lines[:42]
    image = Image.new("RGB", (1200, max(180, 100 + 27 * len(lines))), "#101820")
    draw = ImageDraw.Draw(image)
    draw.text((24, 18), f"PYTHON ABL | {program.stem}", fill="#8bd5ca", font=font)
    y = 62
    for line in lines:
        draw.text((24, y), line, fill="#f4f4f4", font=font)
        y += 25
    image.save(SHOTS / f"{index:02d}_output.png")

pdf_path = ROOT / "Python_ABL_Final_Report.pdf"
styles = getSampleStyleSheet()
title = ParagraphStyle("ABLTitle", parent=styles["Title"], alignment=TA_CENTER, fontSize=20, leading=25, spaceAfter=12)
subtitle = ParagraphStyle("ABLSubtitle", parent=styles["Normal"], alignment=TA_CENTER, fontSize=11, leading=16)
heading = ParagraphStyle("ABLHeading", parent=styles["Heading2"], fontSize=13, leading=17, spaceBefore=8, spaceAfter=6)
body = ParagraphStyle("ABLBody", parent=styles["BodyText"], fontSize=9, leading=12)
story = [
    Spacer(1, 35*mm),
    Paragraph("PYTHON PROGRAMMING", title),
    Paragraph("ACTIVITY-BASED LEARNING (ABL) – FINAL REPORT", title),
    Spacer(1, 8*mm),
    Paragraph("<b>Student:</b> Chundi Vinay Kumar", subtitle),
    Paragraph("<b>Roll Number:</b> 26001286", subtitle),
    Paragraph("<b>Branch:</b> CSM &nbsp;&nbsp;&nbsp; <b>Section:</b> 7", subtitle),
    Spacer(1, 12*mm),
    Paragraph("Ten selected case studies with algorithms, pseudocode, test cases and Python implementations", subtitle),
    PageBreak(),
]
for doc in sorted(DOCS.glob("*.md")):
    if doc.name == "SYLLABUS_MAPPING.md":
        continue
    story.append(Paragraph(escape(doc.stem.replace("_", " ").title()), heading))
    for line in doc.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            story.append(Spacer(1, 3))
        elif line.startswith("#"):
            story.append(Paragraph(escape(line.lstrip("# ").strip()), heading))
        elif line.startswith("- "):
            story.append(Paragraph("• " + escape(line[2:]), body))
        elif line.startswith("```"):
            continue
        else:
            story.append(Paragraph(escape(line), body))
    story.append(Spacer(1, 5*mm))
story.append(PageBreak())
story.append(Paragraph("Syllabus Mapping", heading))
mapping = DOCS / "SYLLABUS_MAPPING.md"
for line in mapping.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        story.append(Spacer(1, 3))
    elif line.startswith("#"):
        story.append(Paragraph(escape(line.lstrip("# ").strip()), heading))
    elif line.startswith("- "):
        story.append(Paragraph("• " + escape(line[2:]), body))
    else:
        story.append(Paragraph(escape(line), body))
SimpleDocTemplate(str(pdf_path), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm,
                  topMargin=17*mm, bottomMargin=17*mm,
                  title="Python ABL Final Report").build(story)
print("Generated report and 10 output screenshots.")
