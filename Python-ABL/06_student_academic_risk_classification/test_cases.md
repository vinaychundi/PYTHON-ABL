# Case Study 66: Student Academic Risk Classification

## Problem statement
Combine marks, attendance and laboratory scores to classify students into high, medium or low academic risk categories.

## Objectives
Use variables, arithmetic, logical and relational operators, lists, loops and nested decision-making.

## Assumptions
Risk indicators: average marks below 50, attendance below 75%, lab score below 50. Two or more indicators mean HIGH risk; one means MEDIUM; none means LOW.

## Algorithm
1. Read each student's three subject marks, attendance and lab score.
2. Calculate average marks.
3. Count low-mark, low-attendance and low-lab indicators.
4. Classify risk based on the number of indicators.
5. Display the student category and class totals.

## Flowchart
Start → Input marks/attendance/lab → Calculate average → Count risk indicators → Classify risk → Display category and totals → Stop.

## Pseudocode
```text
START
INPUT number of students
FOR each student
    INPUT marks, attendance and lab score
    CALCULATE average
    SET risk_count = 0
    INCREMENT count for each risk condition
    IF count >= 2 SET HIGH
    ELSE IF count == 1 SET MEDIUM
    ELSE SET LOW
    DISPLAY category
DISPLAY high, medium and low totals
STOP
```

## Python source
See `../programs/06_academic_risk.py`.

## Test cases
- Ravi: marks 40,45,50; attendance 60; lab 40 → HIGH.
- Sita: marks 70,60,65; attendance 70; lab 80 → MEDIUM.

## Conclusion
Multiple decision conditions identify risk factors. A counter records the number of indicators and classifies each student.
