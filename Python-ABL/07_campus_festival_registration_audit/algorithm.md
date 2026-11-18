# Algorithm: Campus Festival Registration and Financial Audit

1. Start.
2. Read the number of registration entries.
3. Initialize lists for registration IDs and paid amounts, sets for unique and duplicate IDs, and the actual collection total to zero.
4. For each registration:
   - Read the registration ID and amount collected.
   - Remove surrounding spaces and convert the ID to uppercase.
   - Store the ID and amount in their respective lists.
   - If the ID already exists in the unique-ID set, add it to the duplicate-ID set.
   - Otherwise, add the ID to the unique-ID set and add its payment to the actual collection total.
5. Read total sponsorship and total expenses.
6. Calculate expected registration revenue as number of unique IDs multiplied by 300.
7. Calculate final balance = actual collection + sponsorship - expenses.
8. Display unique participant count, expected revenue, actual collection counted once, duplicate IDs, sponsorship, expenses, and final balance.
9. If balance is positive, display SURPLUS; if negative, display DEFICIT; otherwise display BREAK EVEN.
10. Stop.
