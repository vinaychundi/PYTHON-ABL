n = int(input("Number of registration entries: "))
ids = []
paid_amounts = []
unique_ids = set()
duplicate_ids = set()
actual_collected = 0
for i in range(n):
    rid = input("Registration ID: ").strip().upper()
    paid = float(input("Amount collected: "))
    ids.append(rid)
    paid_amounts.append(paid)
    if rid in unique_ids:
        duplicate_ids.add(rid)
    else:
        unique_ids.add(rid)
        actual_collected = actual_collected + paid

sponsorship = float(input("Total sponsorship: "))
expenses = float(input("Total expenses: "))
expected = len(unique_ids) * 300
balance = actual_collected + sponsorship - expenses
print("\nFESTIVAL AUDIT")
print("Unique participants:", len(unique_ids))
print("Expected registration revenue:", expected)
print("Actual collection counted once:", actual_collected)
print("Duplicate IDs:", duplicate_ids)
print("Sponsorship:", sponsorship, "Expenses:", expenses)
print("Final balance:", balance)
if balance > 0:
    print("SURPLUS")
elif balance < 0:
    print("DEFICIT")
else:
    print("BREAK EVEN")
