# Algorithm: Smart Campus Management Simulation

1. Start.
2. Create an empty student list and an empty set of event registrations.
3. Repeat the menu until the user selects option 6:
   - Display the menu: add student, update attendance, update marks, event registration, summary, or exit.
   - Read the user's choice.
4. If choice is 1 (Add student):
   - Read and normalize the roll number.
   - Search the student list for an existing roll number.
   - If it exists, display a duplicate-roll message.
   - Otherwise, read and format the student's name, create a student record with zero attendance and marks, and add it to the list.
5. If choice is 2 (Attendance):
   - Read the roll number and search for the student.
   - If found, read classes attended and total classes.
   - Update attendance only if attended is non-negative and total classes is at least attended; otherwise display an error.
   - If not found, display a student-not-found message.
6. If choice is 3 (Marks):
   - Read the roll number and search for the student.
   - If found, read marks and update only when the value is between 0 and 100.
   - If not found, display a student-not-found message.
7. If choice is 4 (Event registration):
   - Read the roll number and event name.
   - Check that the student exists and that the (roll number, event) pair is not already registered.
   - Add the pair to the registration set if valid; otherwise display the appropriate error or duplicate message.
8. If choice is 5 (Summary):
   - Display each student's attendance percentage (when total classes is greater than zero) and marks.
   - Display all event registrations.
9. If choice is 6, display the exit message.
10. For any other choice, display an invalid-choice message.
11. Stop after the menu loop ends.
