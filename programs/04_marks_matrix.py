ns = int(input("Number of students: "))
nsub = int(input("Number of subjects: "))
subjects = []
for j in range(nsub):
    subjects.append(input("Subject " + str(j + 1) + ": "))

names = []
marks = []
for i in range(ns):
    names.append(input("\nStudent name: "))
    row = []
    for j in range(nsub):
        mark = float(input("Marks in " + subjects[j] + ": "))
        if mark < 0 or mark > 100:
            print("Invalid mark. Entered as 0.")
            mark = 0
        row.append(mark)
    marks.append(row)

totals = []
print("\nSTUDENT PERFORMANCE")
for i in range(ns):
    total = 0
    for j in range(nsub):
        total = total + marks[i][j]
    totals.append(total)
    print(names[i], "Total:", total, "Average:", total / nsub)

if ns > 0:
    top = 0
    for i in range(1, ns):
        if totals[i] > totals[top]:
            top = i
    print("Top performer:", names[top])

print("\nSUBJECT AVERAGES")
for j in range(nsub):
    total = 0
    for i in range(ns):
        total = total + marks[i][j]
    average = total / ns
    print(subjects[j], average)
    if average < 50:
        print("Low average subject")
