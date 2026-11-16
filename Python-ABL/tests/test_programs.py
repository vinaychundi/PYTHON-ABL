from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PROGRAMS = ROOT / "programs"

CASES = [
    ("01_scholarship_allocation.py", "2\nAsha\n88\n80\n75\n90\n90\n180000\nRavi\n68\n70\n65\n72\n80\n300000\n", ["SCHOLARSHIP MERIT LIST", "Asha", "Not eligible:", "Ravi"]),
    ("02_warehouse_inventory.py", "2\nLaptop\n50\n10\n45\n12\nMouse\n30\n5\n10\n25\n", ["Laptop", "SHORTAGE", "Reorder: 8", "Mouse", "MATCH"]),
    ("03_timetable_conflict.py", "2\nMath\nCSM-A\nR101\n9\n10\nPhysics\nCSM-A\nR102\n9\n11\n", ["Conflict: Math and Physics", "Same student group", "Total conflicts: 1"]),
    ("04_marks_matrix.py", "2\n2\nPython\nMaths\nAsha\n80\n70\nBalu\n40\n60\n", ["STUDENT PERFORMANCE", "Asha Total: 150.0", "Top performer: Asha", "SUBJECT AVERAGES"]),
    ("05_transaction_audit.py", "3\nT01\n1500\nDEPOSIT\nT01\n60000\nDEPOSIT\nT03\n-50\nCREDIT\n", ["TRANSACTION AUDIT", "Duplicate ID", "High-value review", "Invalid amount", "Invalid type"]),
    ("06_academic_risk.py", "2\nRavi\n40\n45\n50\n60\n40\nAnu\n85\n90\n88\n95\n90\n", ["Ravi Average: 45.0 Risk: HIGH", "Anu Average:", "Risk: LOW", "Risk totals - High: 1"]),
    ("07_festival_audit.py", "3\nA1\n300\nA2\n300\nA1\n300\n1000\n1200\n", ["Unique participants: 2", "Final balance: 400.0", "SURPLUS"]),
    ("08_internship_ranking.py", "2\nAnu\n80\n75\n90\nBala\n60\n80\n90\n", ["INTERNSHIP RANKING", "Anu", "Not eligible:", "Bala"]),
    ("09_disaster_relief.py", "100\n2\nNorth\n80\n1\nSouth\n50\n2\n", ["North Priority: 1 Allocated: 80", "South Priority: 2 Allocated: 20 Unmet: 30", "Remaining stock: 0"]),
    ("10_smart_campus.py", "1\n26CS01\nVinay\n2\n26CS01\n8\n10\n3\n26CS01\n85\n4\n26CS01\nTech Fest\n5\n6\n", ["Student added.", "Attendance updated.", "Marks updated.", "Registration successful.", "STUDENT SUMMARY", "Vinay"]),
]

def main():
    failures = []
    for filename, sample_input, expected in CASES:
        path = PROGRAMS / filename
        result = subprocess.run(
            [sys.executable, str(path)],
            input=sample_input,
            text=True,
            capture_output=True,
            timeout=20,
        )
        missing = [item for item in expected if item not in result.stdout]
        if result.returncode != 0 or missing:
            failures.append((filename, result.returncode, missing, result.stderr))
            print(f"FAIL {filename}: missing={missing}, exit={result.returncode}")
        else:
            print(f"PASS {filename}")
    if failures:
        print(f"\n{len(failures)} test(s) failed out of {len(CASES)}.")
        return 1
    print(f"\nAll {len(CASES)} program test cases passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
