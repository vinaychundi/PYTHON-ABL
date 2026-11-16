# Case Study 94: Disaster Relief Supply Allocation

## Problem statement
Allocate limited relief supplies to affected areas according to urgency priority and calculate unmet demand.

## Objectives
Use lists, tuples, loops, nested loops, range, arithmetic and relational operators, and if/elif/else.

## Assumptions
Priority 1 is most urgent, then 2, then 3. Input order is preserved within a priority. Allocation never exceeds demand or stock.

## Algorithm
1. Read available stock and affected area details.
2. Skip invalid demand or priority records.
3. Process areas in priority order from 1 to 3.
4. Allocate the minimum of remaining stock and area demand.
5. Calculate unmet demand and remaining stock.

## Flowchart
Start → Input stock and areas → Validate records → Process priority levels → Allocate stock → Calculate unmet demand → Display report → Stop.

## Pseudocode
```text
START
INPUT available stock and areas
FOR priority from 1 to 3
    FOR each area
        IF area priority matches
            ALLOCATE min(stock, demand)
            UPDATE stock
            CALCULATE unmet demand
            DISPLAY allocation
DISPLAY remaining stock
STOP
```

## Python source
See `../programs/09_disaster_relief.py`.

## Test case
Stock 100; North demand 80 priority 1; South demand 50 priority 2. North receives 80; South receives 20; unmet demand is 30.

## Conclusion
Nested loops process areas in priority order. Conditional statements allocate available stock without exceeding demand.
