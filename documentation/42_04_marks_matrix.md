# Case Study 42: Student Marks Matrix Analysis

## Problem statement
Analyse student marks stored in a nested list. Calculate student totals and averages, subject averages, topper and low-performing subjects.

## Objectives
Practise nested lists, traversal, updating, arithmetic operators, loops, conditions and formatted output.

## Assumptions
Marks are between 0 and 100. A subject average below 50 is flagged as low. Each student has marks in all entered subjects.

## Algorithm
1. Read subjects and student names.
2. Store each student's marks in a nested list.
3. Replace invalid marks with zero.
4. Calculate each student's total and average and find the topper.
5. Calculate each subject average and flag low averages.

## Flowchart
Start → Input subjects/students → Build marks matrix → Calculate student results → Find topper → Calculate subject averages → Stop.

## Pseudocode
```text
START
INPUT subjects and students
FOR each student
    INPUT marks and STORE row in matrix
FOR each student row
    CALCULATE total and average
FIND student with highest total
FOR each subject column
    CALCULATE subject average
    IF average < 50, DISPLAY low-average warning
STOP
```

## Python source
See `../programs/04_marks_matrix.py`.

## Test case
Asha: Python 80, Maths 70; Balu: Python 40, Maths 60. Totals: 150 and 100. Subject averages: Python 60 and Maths 65.

## Conclusion
Nested lists represent the marks matrix. Nested loops calculate row and column statistics.
