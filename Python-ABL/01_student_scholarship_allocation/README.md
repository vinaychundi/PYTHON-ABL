# Case Study 1: University Scholarship Allocation

## Problem statement
Evaluate applicants using aggregate marks, three subject marks, attendance and annual family income. List eligible applicants and rank them.

## Objectives
Practise input, type conversion, logical and relational operators, lists, tuples, loops and conditions.

## Assumptions
Eligibility requires aggregate >= 75, each subject >= 60, attendance >= 75 and family income <= Rs. 250000. Ranking is aggregate descending, attendance descending, then income ascending.

## Algorithm
1. Read the number of applicants and their details.
2. Check every eligibility condition.
3. Store eligible applicants and rejected names separately.
4. Repeatedly find the best eligible applicant using tie-break rules.
5. Display the merit list and rejected applicants.

## Flowchart
Start → Input applicants → Check eligibility → Store eligible/rejected → Rank eligible applicants → Display merit list → Stop.

## Pseudocode
```text
START
INPUT applicant details
IF all eligibility conditions are true
    ADD applicant to eligible list
ELSE
    ADD name to rejected list
REPEAT while eligible list is not empty
    FIND best applicant using ranking rules
    ADD best applicant to merit list
    REMOVE applicant from eligible list
DISPLAY merit list and rejected list
STOP
```

## Python source
See `../programs/01_scholarship_allocation.py`.

## Test cases
- Asha(88,80,75,90,90,180000): eligible.
- Balu(70,80,80,80,85,150000): not eligible.
- Chitra(82,70,75,80,90,300000): not eligible.

## Conclusion
Conditions check scholarship rules; lists and tuples store applicant data, and loops generate a ranked merit list.
