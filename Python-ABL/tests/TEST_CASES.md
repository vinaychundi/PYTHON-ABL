# Python ABL – Test Cases

This file documents the representative test cases used to verify the ten Python programs. Inputs are entered in the exact order requested by each program. The automated runner checks that each program completes successfully and that the expected result appears in its output.

| Test ID | Program | Scenario / input covered | Expected result |
|---|---|---|---|
| TC-01 | Scholarship allocation | One applicant meets all scholarship conditions; one fails the conditions | Asha appears in the merit list; Ravi appears under Not eligible |
| TC-02 | Warehouse inventory | One product has a shortage and needs reorder; another matches physical stock | Laptop is SHORTAGE with reorder 8; Mouse is MATCH |
| TC-03 | Timetable conflict | Two classes overlap for the same student group in different rooms | Conflict is reported and reason is Same student group |
| TC-04 | Marks matrix | Two students and two subjects; totals and averages are calculated | Asha is top performer; subject averages are displayed |
| TC-05 | Transaction audit | Duplicate transaction ID, high-value deposit, and invalid transaction data | Duplicate ID, High-value review, and Invalid amount/type flags appear |
| TC-06 | Academic risk | One student has multiple risk indicators; another performs well | Ravi is HIGH risk; Anu is LOW risk |
| TC-07 | Festival registration audit | Duplicate registration is counted once; sponsorship and expenses affect balance | 2 unique participants, final balance 400, SURPLUS |
| TC-08 | Internship ranking | One eligible candidate and one candidate below the academic threshold | Anu is ranked; Bala appears under Not eligible |
| TC-09 | Disaster relief allocation | Urgent area is served before medium-priority area with limited stock | North receives 80; South receives remaining 20 and reports unmet demand 30 |
| TC-10 | Smart campus | Add student, update attendance and marks, register for event, view summary | Student added; attendance and marks updated; registration successful |

## Test execution

From the repository root, run:

```bash
python Python-ABL/tests/test_programs.py
```

A successful run prints one PASS line per program and a final summary. The test runner uses only Python's standard library and does not modify the source programs.

## Evidence

The `screenshots/` folder contains a PNG execution screenshot and a plain-text console output capture for each program. The screenshots are generated after running the actual `.py` files with deterministic sample input.
