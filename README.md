# Python Activity-Based Learning (ABL)

**Student:** Chundi Vinay Kumar  
**Roll Number:** 26001286  
**Branch:** CSM  
**Section:** 7  
**Subject:** Python Programming

## Selected case studies
1. University Scholarship Allocation
14. Warehouse Inventory Reconciliation
23. Student Timetable Conflict Detection
42. Student Marks Matrix Analysis
55. Tuple-Based Transaction Audit
66. Student Academic Risk Classification
74. Campus Festival Registration and Financial Audit
82. Multi-Criteria Internship Candidate Ranking
94. Disaster Relief Supply Allocation
100. Comprehensive Smart Campus Management Simulation

## Repository structure
- `programs/` — 10 executable Python source files.
- `documentation/` — problem statements, objectives, assumptions, algorithms, flowcharts, pseudocode, test cases, conclusions and syllabus mapping.
- `screenshots/` — generated sample-run screenshots and text outputs.
- `Python_ABL_Final_Report.pdf` — consolidated report generated from the case-study documentation.

## Syllabus coverage
- **Unit I:** Computational thinking, problem-solving, algorithms, flowcharts, Python fundamentals, data types, I/O, type conversion and operators.
- **Unit II:** Decision-making, loops, strings, formatting, patterns and functions.
- **Unit III:** Lists, nested lists, tuples, tuple unpacking, sets and membership testing.

## Run a program
Install Python 3 and run a program from the repository root, for example:

```bash
python programs/01_scholarship_allocation.py
```

## Generate the PDF and screenshots
The repository includes `scripts/build_assets.py` and a GitHub Actions workflow named **Build Python ABL report and screenshots**.

To generate or regenerate the report and 10 PNG output screenshots:
1. Open the repository's **Actions** tab.
2. Select **Build Python ABL report and screenshots**.
3. Choose **Run workflow** and confirm.
4. When the run succeeds, the generated PDF and screenshots are committed to the repository.

All programs use Python's built-in features. The asset-generation script uses Pillow and ReportLab in GitHub Actions.
