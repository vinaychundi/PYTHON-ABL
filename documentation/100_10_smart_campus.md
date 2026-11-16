# Case Study 100: Comprehensive Smart Campus Management Simulation

## Problem statement
Build a menu-driven campus program integrating student records, attendance, marks and event registration.

## Objectives
Use loops, menu conditions, strings, lists, nested lists, tuples, tuple unpacking, sets and membership testing.

## Assumptions
Roll numbers are unique. Attendance values are non-negative and attended classes cannot exceed conducted classes. Marks are between 0 and 100.

## Algorithm
1. Display a menu until the user selects Exit.
2. Add a student after checking roll-number uniqueness.
3. Update attendance after validating class counts.
4. Update marks after validating the 0–100 range.
5. Register students for events while preventing duplicate registrations.
6. Display student and event summaries.

## Flowchart
Start → Display menu → Read choice → Execute selected operation → Return to menu → Exit choice? → Stop.

## Pseudocode
```text
START
INITIALIZE student list and registration set
WHILE choice is not Exit
    DISPLAY menu and INPUT choice
    IF Add student: validate unique roll and append record
    ELSE IF Attendance: find student and validate counts
    ELSE IF Marks: find student and validate marks
    ELSE IF Event: verify student and set membership
    ELSE IF Summary: display records and registrations
    ELSE IF Exit: terminate
    ELSE: display invalid choice
STOP
```

## Python source
See `../programs/10_smart_campus.py`.

## Test case
Add 26CS01, Vinay; update attendance 8/10; marks 85; register Tech Fest; display summary. Expected: 80% attendance, 85 marks and Tech Fest registration.

## Conclusion
The menu-driven program combines core syllabus concepts. Lists hold student records, tuples represent event registrations and a set prevents duplicate registrations.
