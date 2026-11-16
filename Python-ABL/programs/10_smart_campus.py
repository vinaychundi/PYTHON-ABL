students = []  # [roll, name, attended, conducted, marks]
registrations = set()  # (roll, event)
choice = ""
while choice != "6":
    print("\nSMART CAMPUS MENU")
    print("1 Add student  2 Attendance  3 Marks")
    print("4 Event registration  5 Summary  6 Exit")
    choice = input("Choice: ")
    if choice == "1":
        roll = input("Roll number: ").strip().upper()
        found = False
        for record in students:
            if record[0] == roll:
                found = True
        if found:
            print("Roll already exists.")
        else:
            name = input("Student name: ").strip().title()
            students.append([roll, name, 0, 0, 0])
            print("Student added.")
    elif choice == "2":
        roll = input("Roll number: ").strip().upper()
        found = False
        for record in students:
            if record[0] == roll:
                attended = int(input("Classes attended: "))
                conducted = int(input("Total classes: "))
                if attended >= 0 and conducted >= attended:
                    record[2] = attended
                    record[3] = conducted
                    print("Attendance updated.")
                else:
                    print("Invalid attendance.")
                found = True
        if not found:
            print("Student not found.")
    elif choice == "3":
        roll = input("Roll number: ").strip().upper()
        found = False
        for record in students:
            if record[0] == roll:
                mark = float(input("Marks out of 100: "))
                if mark >= 0 and mark <= 100:
                    record[4] = mark
                    print("Marks updated.")
                else:
                    print("Invalid marks.")
                found = True
        if not found:
            print("Student not found.")
    elif choice == "4":
        roll = input("Roll number: ").strip().upper()
        event = input("Event name: ").strip().title()
        found = False
        for record in students:
            if record[0] == roll:
                found = True
        entry = (roll, event)
        if found and entry not in registrations:
            registrations.add(entry)
            print("Registration successful.")
        elif not found:
            print("Student not found.")
        else:
            print("Already registered.")
    elif choice == "5":
        print("\nSTUDENT SUMMARY")
        for record in students:
            roll, name, attended, conducted, marks = record
            percentage = 0
            if conducted > 0:
                percentage = attended / conducted * 100
            print(roll, name, "Attendance:", round(percentage, 2), "Marks:", marks)
        print("EVENT REGISTRATIONS")
        for entry in registrations:
            roll, event = entry
            print(roll, "->", event)
    elif choice == "6":
        print("Exiting campus system.")
    else:
        print("Invalid choice.")
