# Algorithm: Tuple-Based Transaction Audit

1. Start.
2. Read the number of transactions and create an empty transaction list.
3. For each transaction:
   - Read the transaction ID, amount, and transaction type.
   - Remove surrounding spaces from the ID and convert it to uppercase.
   - Convert the transaction type to uppercase.
   - Store the transaction as a tuple.
4. For each transaction tuple:
   - Create an empty list of audit flags.
   - If amount is less than or equal to zero, add an invalid-amount flag.
   - If type is neither DEPOSIT nor WITHDRAWAL, add an invalid-type flag.
   - If amount is greater than 50000, add a high-value-review flag.
   - Compare its ID with every other transaction ID. If another transaction has the same ID, add a duplicate-ID flag.
5. If no flags were added, display the transaction as VALID.
6. Otherwise, display the transaction as FLAGGED with all applicable reasons.
7. Stop.
