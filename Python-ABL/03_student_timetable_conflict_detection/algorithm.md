# Algorithm: Student Timetable Conflict Detection

1. Start.
2. Read the number of timetable entries and create an empty schedule list.
3. For each entry, read course, student group, room, start hour, and end hour.
4. If start hour is below 0, end hour is above 24, or start hour is not earlier than end hour, display an invalid-time message and skip the entry.
5. Store each valid timetable entry.
6. Set the conflict counter to zero.
7. Compare every pair of distinct schedule entries:
   - Extract each entry's room, group, start time, and end time.
   - Check whether the time intervals overlap using start1 < end2 and start2 < end1.
   - If they overlap and either the room or student group is the same, increment the conflict counter and display the courses involved.
   - Display the applicable reason: same room and/or same student group.
8. If the conflict counter is zero, display that no conflicts were found; otherwise display the total conflicts.
9. Stop.
