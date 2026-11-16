n = int(input("Number of applicants: "))
eligible = []
rejected = []
for i in range(n):
    print("\nApplicant", i + 1)
    name = input("Name: ")
    aggregate = float(input("Aggregate percentage: "))
    s1 = float(input("Subject 1 marks: "))
    s2 = float(input("Subject 2 marks: "))
    s3 = float(input("Subject 3 marks: "))
    attendance = float(input("Attendance percentage: "))
    income = float(input("Annual family income: "))
    if aggregate >= 75 and s1 >= 60 and s2 >= 60 and s3 >= 60 and attendance >= 75 and income <= 250000:
        eligible.append((name, aggregate, attendance, income))
    else:
        rejected.append(name)

# Repeatedly select the best remaining record using syllabus-level loops.
ranked = []
while len(eligible) > 0:
    best = 0
    for j in range(1, len(eligible)):
        a = eligible[j]
        b = eligible[best]
        if a[1] > b[1] or (a[1] == b[1] and a[2] > b[2]) or (a[1] == b[1] and a[2] == b[2] and a[3] < b[3]):
            best = j
    ranked.append(eligible[best])
    eligible.pop(best)

print("\nSCHOLARSHIP MERIT LIST")
for i in range(len(ranked)):
    name, marks, attendance, income = ranked[i]
    print(i + 1, name, marks, attendance, income)
print("Not eligible:", rejected)
