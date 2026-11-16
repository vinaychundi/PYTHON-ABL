stock = int(input("Available relief units: "))
n = int(input("Number of affected areas: "))
areas = []
for i in range(n):
    name = input("Area name: ")
    demand = int(input("Required units: "))
    priority = int(input("Priority (1 urgent, 2 medium, 3 normal): "))
    if demand < 0 or priority < 1 or priority > 3:
        print("Invalid record. Skipped.")
        continue
    areas.append((name, demand, priority))

print("\nRELIEF ALLOCATION")
for level in range(1, 4):
    for item in areas:
        name, demand, priority = item
        if priority == level:
            if stock >= demand:
                allocation = demand
            else:
                allocation = stock
            stock = stock - allocation
            unmet = demand - allocation
            print(name, "Priority:", priority, "Allocated:", allocation, "Unmet:", unmet)
print("Remaining stock:", stock)
