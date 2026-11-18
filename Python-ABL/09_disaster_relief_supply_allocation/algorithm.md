# Algorithm: Disaster Relief Supply Allocation

1. Start.
2. Read the available relief stock and number of affected areas.
3. Create an empty list for area records.
4. For each area, read its name, required units, and priority level.
5. If demand is negative or priority is outside 1 to 3, display an invalid-record message and skip the area.
6. Store each valid area as a record containing name, demand, and priority.
7. Process priority levels in order from 1 (urgent) to 3 (normal).
8. For each area matching the current priority:
   - If available stock is at least the demand, allocate the full demand.
   - Otherwise, allocate all remaining stock.
   - Subtract the allocation from available stock.
   - Calculate unmet demand = demand - allocation.
   - Display the area, priority, allocated units, and unmet units.
9. Display remaining stock.
10. Stop.
