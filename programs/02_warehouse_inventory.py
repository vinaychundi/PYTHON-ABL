n = int(input("Number of products: "))
products = []
for i in range(n):
    print("\nProduct", i + 1)
    name = input("Product name: ")
    opening = int(input("Opening stock: "))
    received = int(input("Received: "))
    dispatched = int(input("Dispatched: "))
    physical = int(input("Physical closing stock: "))
    if opening < 0 or received < 0 or dispatched < 0 or physical < 0:
        print("Invalid negative quantity. Record skipped.")
        continue
    products.append((name, opening, received, dispatched, physical))

print("\nSTOCK RECONCILIATION")
for item in products:
    name, opening, received, dispatched, physical = item
    expected = opening + received - dispatched
    difference = physical - expected
    reorder = 0
    if physical < 20:
        reorder = 20 - physical
    if difference == 0:
        status = "MATCH"
    elif difference < 0:
        status = "SHORTAGE"
    else:
        status = "SURPLUS"
    print(name, "Expected:", expected, "Physical:", physical,
          "Difference:", difference, status, "Reorder:", reorder)
