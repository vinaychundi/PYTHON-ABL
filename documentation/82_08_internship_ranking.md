# Case Study 82: Multi-Criteria Internship Candidate Ranking

## Problem statement
Evaluate candidates using academic marks, assessment score and attendance. Rank qualified candidates using a weighted score and tie-break rules.

## Objectives
Use arithmetic, relational and logical operators, tuples, lists, loops and conditional statements.

## Assumptions
Eligibility: marks >= 65, assessment >= 60, attendance >= 75. Weighted score = 40% marks + 40% assessment + 20% attendance. Ties use assessment then marks.

## Algorithm
1. Read candidate details.
2. Check the eligibility thresholds.
3. Calculate weighted score for eligible candidates.
4. Repeatedly select the best remaining candidate using tie-break rules.
5. Display ranked and rejected candidates.

## Flowchart
Start → Input candidate → Check eligibility → Calculate weighted score → Rank eligible candidates → Display merit list → Stop.

## Pseudocode
```text
START
INPUT candidates
FOR each candidate
    IF all eligibility thresholds are met
        CALCULATE weighted score
        STORE candidate tuple
    ELSE
        STORE rejected name
REPEAT while eligible list is not empty
    FIND best candidate using score and tie-break rules
    ADD to ranked list and REMOVE from eligible list
DISPLAY ranked and rejected candidates
STOP
```

## Python source
See `../programs/08_internship_ranking.py`.

## Test cases
- Anu: marks 80, assessment 75, attendance 90 → eligible, score 80.
- Bala: marks 60, assessment 80, attendance 90 → not eligible.

## Conclusion
Conditions shortlist candidates and a loop-based selection process ranks tuples by weighted score.
