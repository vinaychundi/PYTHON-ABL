# Case Study 14: Warehouse Inventory Reconciliation

## Problem statement
Compare opening stock, received quantity, dispatched quantity and physical closing stock. Identify shortages or surpluses and calculate replenishment.

## Objectives
Practise arithmetic operators, input validation, lists, tuples, loops and conditional statements.

## Assumptions
Expected closing stock = opening + received - dispatched. Reorder target is 20 units. All stock quantities must be non-negative.

## Algorithm
1. Read product details.
2. Skip records containing negative quantities.
3. Calculate expected closing stock and difference from physical stock.
4. Classify each product as MATCH, SHORTAGE or SURPLUS.
5. Calculate reorder quantity and display the report.

## Flowchart
Start → Input products → Validate quantities → Calculate expected stock → Compare physical stock → Display status and reorder quantity → Stop.

## Pseudocode
```text
START
INPUT number of products
FOR each product
    INPUT opening, received, dispatched, physical stock
    IF any quantity is negative
        SKIP record
    ELSE
        expected = opening + received - dispatched
        difference = physical - expected
        DETERMINE MATCH, SHORTAGE or SURPLUS
        CALCULATE reorder quantity
        DISPLAY result
STOP
```

## Python source
See `../programs/02_warehouse_inventory.py`.

## Test case
Pen: opening 50, received 20, dispatched 30, physical 38. Expected 40; difference -2 (shortage); reorder 0.

## Conclusion
Arithmetic and conditional statements reconcile stock. Tuples preserve each product record and a list stores all products.
