# Algorithm: Warehouse Inventory Reconciliation

1. Start.
2. Read the number of products and create an empty product list.
3. For each product, read its name, opening stock, received quantity, dispatched quantity, and physical closing stock.
4. If any quantity is negative, display an invalid-record message and skip that product.
5. Store each valid product record.
6. For every stored product:
   - Calculate expected stock = opening stock + received quantity - dispatched quantity.
   - Calculate difference = physical closing stock - expected stock.
   - If physical stock is below 20, calculate reorder quantity = 20 - physical stock; otherwise set reorder quantity to zero.
   - If difference is zero, set status to MATCH.
   - If difference is negative, set status to SHORTAGE.
   - Otherwise, set status to SURPLUS.
7. Display expected stock, physical stock, difference, status, and reorder quantity for each product.
8. Stop.
