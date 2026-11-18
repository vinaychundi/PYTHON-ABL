# Algorithm: Multi-Criteria Internship Candidate Ranking

1. Start.
2. Read the number of candidates and create empty eligible and rejected lists.
3. For each candidate:
   - Read name, academic marks, assessment score, and attendance.
   - Check whether marks are at least 65, assessment score is at least 60, and attendance is at least 75.
   - If all conditions are satisfied, calculate weighted score = 0.4 × marks + 0.4 × assessment + 0.2 × attendance, then store the candidate.
   - Otherwise, add the candidate's name to the rejected list.
4. Create an empty ranked list.
5. While eligible candidates remain:
   - Find the candidate with the highest weighted score.
   - For equal weighted scores, prefer the higher assessment score.
   - If still tied, prefer higher academic marks.
   - Move the selected candidate to the ranked list and remove them from eligible candidates.
6. Display the ranked candidates with their weighted scores.
7. Display the rejected candidates.
8. Stop.
