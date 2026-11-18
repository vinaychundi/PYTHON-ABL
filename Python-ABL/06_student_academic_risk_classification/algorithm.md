# Algorithm: Student Academic Risk Classification

1. Start.
2. Read the number of students.
3. Initialize HIGH, MEDIUM, and LOW risk counters to zero.
4. For each student:
   - Read name, marks in three subjects, attendance percentage, and lab score.
   - Calculate the average of the three subject marks.
   - Initialize the risk-condition counter to zero and create an empty reasons list.
   - If average marks are below 50, increment the risk counter and record low marks.
   - If attendance is below 75, increment the risk counter and record low attendance.
   - If lab score is below 50, increment the risk counter and record low lab score.
   - If two or more risk conditions are present, classify the student as HIGH.
   - If exactly one condition is present, classify the student as MEDIUM.
   - If no conditions are present, classify the student as LOW.
   - Update the corresponding category counter.
   - Display the student's average, risk category, and reasons.
5. Display the total number of HIGH, MEDIUM, and LOW risk students.
6. Stop.
