n = int(input("Number of transactions: "))
transactions = []
for i in range(n):
    print("\nTransaction", i + 1)
    tid = input("Transaction ID: ").strip().upper()
    amount = float(input("Amount: "))
    kind = input("Type (DEPOSIT/WITHDRAWAL): ").strip().upper()
    transactions.append((tid, amount, kind))

print("\nTRANSACTION AUDIT")
for i in range(len(transactions)):
    tid, amount, kind = transactions[i]
    flags = []
    if amount <= 0:
        flags.append("Invalid amount")
    if kind not in ("DEPOSIT", "WITHDRAWAL"):
        flags.append("Invalid type")
    if amount > 50000:
        flags.append("High-value review")
    duplicate = False
    for j in range(len(transactions)):
        if i != j and tid == transactions[j][0]:
            duplicate = True
    if duplicate:
        flags.append("Duplicate ID")
    if len(flags) == 0:
        print(tid, amount, kind, "VALID")
    else:
        print(tid, amount, kind, "FLAGGED:", ", ".join(flags))
