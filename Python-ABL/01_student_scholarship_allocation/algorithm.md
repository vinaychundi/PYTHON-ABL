# Algorithm: University Scholarship Allocation

1. Start.
2. Read the number of applicants.
3. Create empty lists for eligible and rejected applicants.
4. For each applicant:
   - Read name, aggregate percentage, three subject marks, attendance, and annual family income.
   - Check whether aggregate is at least 75, each subject mark is at least 60, attendance is at least 75, and income is at most 250000.
   - If all conditions are true, store the applicant's details in the eligible list; otherwise, store the name in the rejected list.
5. Create an empty merit-ranked list.
6. While eligible applicants remain:
   - Find the applicant with the highest aggregate.
   - For equal aggregates, prefer higher attendance.
   - If both are equal, prefer lower family income.
   - Move the selected applicant to the merit list and remove them from eligible applicants.
7. Display the scholarship merit list with rank and applicant details.
8. Display the rejected applicants.
9. Stop.
