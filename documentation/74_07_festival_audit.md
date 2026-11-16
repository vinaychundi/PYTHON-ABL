# Case Study 74: Campus Festival Registration and Financial Audit

## Problem statement
Reconcile participant registrations, collected fees, sponsorship and expenses. Detect duplicate registration IDs and calculate the final balance.

## Objectives
Practise strings, string methods, lists, membership testing, arithmetic operators, loops and conditions.

## Assumptions
Registration fee is Rs. 300 per unique participant. Duplicate IDs are counted once. Sponsorship and expenses are non-negative.

## Algorithm
1. Read registration IDs and amounts collected.
2. Normalize registration IDs.
3. Use a set to identify unique and duplicate IDs.
4. Count the first payment for each unique ID.
5. Calculate expected revenue and final balance after sponsorship and expenses.

## Flowchart
Start → Input registrations → Normalize ID → Check set membership → Count unique payment → Input sponsorship/expenses → Calculate balance → Stop.

## Pseudocode
```text
START
INPUT registration entries
FOR each entry
    NORMALIZE registration ID
    IF ID already in unique set
        ADD ID to duplicate set
    ELSE
        ADD ID to unique set
        ADD payment to actual collection
INPUT sponsorship and expenses
CALCULATE expected revenue and final balance
DISPLAY audit
STOP
```

## Python source
See `../programs/07_festival_audit.py`.

## Test case
A1 pays 300; A2 pays 300; A1 appears again; sponsorship 1000; expenses 1200. Two unique participants, duplicate A1, final balance 400.

## Conclusion
Sets store unique registration identifiers and identify duplicates through membership testing.
