# Case Study 55: Tuple-Based Transaction Audit

## Problem statement
Audit transaction tuples containing transaction ID, amount and type. Detect duplicate IDs, invalid amounts, invalid types and high-value transactions.

## Objectives
Use tuples, tuple unpacking, strings and string methods, lists, membership testing, loops and conditions.

## Assumptions
Valid types are DEPOSIT and WITHDRAWAL. Amount must be positive. Amounts above Rs. 50000 are flagged for review.

## Algorithm
1. Read transaction ID, amount and type.
2. Normalize ID and type using string methods.
3. Store each transaction as a tuple.
4. Check amount, type, high-value threshold and duplicate ID.
5. Display VALID or FLAGGED with reasons.

## Flowchart
Start → Input transaction → Normalize strings → Store tuple → Validate fields and duplicate IDs → Display audit result → Stop.

## Pseudocode
```text
START
INPUT transactions
FOR each transaction tuple
    UNPACK ID, amount and type
    CREATE empty flags list
    CHECK amount and transaction type
    CHECK high-value threshold
    CHECK duplicate IDs
    DISPLAY VALID or FLAGGED
STOP
```

## Python source
See `../programs/05_transaction_audit.py`.

## Test cases
- T01, 1500, DEPOSIT: valid if ID is unique.
- T02, -500, WITHDRAWAL: invalid amount.
- Repeated ID: duplicate flag.

## Conclusion
Tuples store transaction records. String methods normalize entries, membership checks valid types, and loops detect duplicates.
