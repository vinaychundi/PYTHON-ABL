from pathlib import Path
import subprocess, textwrap
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
PROGRAMS, DOCS, SHOTS = ROOT/"programs", ROOT/"documentation", ROOT/"screenshots"
SHOTS.mkdir(exist_ok=True)
samples = {
"01_scholarship_allocation.py":"1\nAsha\n88\n80\n75\n90\n90\n180000\n",
"02_warehouse_inventory.py":"1\nPen\n50\n20\n30\n38\n",
"03_timetable_conflict.py":"2\nMath\nCSM-A\nR101\n9\n10\nPhysics\nCSM-A\nR102\n9\n11\n",
"04_marks_matrix.py":"2\n2\nPython\nMaths\nAsha\n80\n70\nBalu\n40\n60\n",
"05_transaction_audit.py":"2\nT01\n1500\nDEPOSIT\nT01\n60000\nDEPOSIT\n",
"06_academic_risk.py":"1\nRavi\n40\n45\n50\n60\n40\n",
"07_festival_audit.py":"2\nA1\n300\nA2\n300\n1000\n1200\n",
"08_internship_ranking.py":"2\nAnu\n80\n75\n90\nBala\n60\n80\n90\n",
"09_disaster_relief.py":"100\n2\nNorth\n80\n1\nSouth\n50\n2\n",
"10_smart_campus.py":"1\n26CS01\nVinay\n2\n26CS01\n8\n10\n3\n26CS01\n85\n4\n26CS01\nTech Fest\n5\n6\n"}
try: font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",15)
except OSError: font=ImageFont.load_default()
for i,p in enumerate(sorted(PROGRAMS.glob("*.py")),1):
 out=subprocess.run(["python",str(p)],input=samples[p.name],text=True,capture_output=True,timeout=20)
 if out.returncode: raise RuntimeError(p.name+": "+out.stderr)
 result=out.stdout+out.stderr
 (SHOTS/f"{i:02d}_sample_output.txt").write_text(result,encoding="utf-8")
 lines=[]
 for raw in result.splitlines(): lines.extend(textwrap.wrap(raw,105) or [""])
 lines=lines[:42]
 im=Image.new("RGB",(1200,max(180,100+27*len(lines))),"#101820"); d=ImageDraw.Draw(im)
 d.text((24,18),f"PYTHON ABL | {p.stem}",fill="#8bd5ca",font=font)
 for k,line in enumerate(lines): d.text((24,62+25*k),line,fill="#f4f4f4",font=font)
 im.save(SHOTS/f"{i:02d}_output.png")
styles=getSampleStyleSheet()
title=ParagraphStyle("ABLTitle",parent=styles["Title"],alignment=TA_CENTER,fontSize=19,leading=24)
sub=ParagraphStyle("ABLSub",parent=styles["Normal"],alignment=TA_CENTER,fontSize=11,leading=16)
h=ParagraphStyle("ABLHeading",parent=styles["Heading2"],fontSize=12,leading=15,spaceBefore=7,spaceAfter=5)
b=ParagraphStyle("ABLBody",parent=styles["BodyText"],fontSize=8.5,leading=11)
story=[Spacer(1,30*mm),Paragraph("PYTHON PROGRAMMING",title),Paragraph("ACTIVITY-BASED LEARNING – FINAL REPORT",title),Spacer(1,10*mm),Paragraph("<b>Student:</b> Chundi Vinay Kumar",sub),Paragraph("<b>Roll Number:</b> 26001286",sub),Paragraph("<b>Branch:</b> CSM &nbsp;&nbsp; <b>Section:</b> 7",sub),PageBreak()]
for f in sorted(DOCS.glob("*.md")):
 story.append(Paragraph(escape(f.stem.replace("_"," ").title()),h))
 for line in f.read_text(encoding="utf-8").splitlines():
  if not line.strip(): story.append(Spacer(1,3))
  elif line.startswith("#"): story.append(Paragraph(escape(line.lstrip("# ").strip()),h))
  elif line.startswith("- "): story.append(Paragraph("• "+escape(line[2:]),b))
  elif line.startswith("```"): continue
  else: story.append(Paragraph(escape(line),b))
 story.append(Spacer(1,4*mm))
SimpleDocTemplate(str(ROOT/"Python_ABL_Final_Report.pdf"),pagesize=A4,rightMargin=17*mm,leftMargin=17*mm,topMargin=16*mm,bottomMargin=16*mm,title="Python ABL Final Report").build(story)
print("Generated the final PDF and 10 screenshots.")
