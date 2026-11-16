# Case Study 23: Student Timetable Conflict Detection

## Problem statement
Represent class schedules using tuples and detect overlapping periods when the same room or student group is assigned.

## Objectives
Use tuples, tuple unpacking, nested loops, relational operators, logical operators and conditions.

## Assumptions
Time is entered as whole hours from 0 to 24. Intervals overlap when start1 < end2 and start2 < end1.

## Algorithm
1. Read course, group, room and start/end times.
2. Skip entries with invalid times.
3. Compare each schedule entry with every later entry.
4. Detect overlapping periods with the same room or student group.
5. Display each conflict and the total.

## Flowchart
Start → Input schedule → Validate times → Compare pairs → Conflict? → Display reason/count → Stop.

## Pseudocode
```text
START
INPUT schedule entries
FOR each pair of entries
    UNPACK tuple values
    CHECK time overlap
    IF overlap AND (same room OR same group)
        DISPLAY conflict and reason
DISPLAY total conflicts
STOP
```

## Python source
See `../programs/03_timetable_conflict.py`.

## Test case
Math, CSM-A, R101, 9-10; Physics, CSM-A, R102, 9-11. A conflict is reported because the group is the same.

## Conclusion
Tuple unpacking extracts timetable fields. Nested loops compare pairs and logical conditions detect clashes.
