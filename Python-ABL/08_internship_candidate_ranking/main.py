n = int(input("Number of candidates: "))
eligible = []
rejected = []
for i in range(n):
    print("\nCandidate", i + 1)
    name = input("Name: ")
    marks = float(input("Academic marks: "))
    assessment = float(input("Assessment score: "))
    attendance = float(input("Attendance: "))
    if marks >= 65 and assessment >= 60 and attendance >= 75:
        score = 0.4 * marks + 0.4 * assessment + 0.2 * attendance
        eligible.append((name, score, assessment, marks))
    else:
        rejected.append(name)

ranked = []
while len(eligible) > 0:
    best = 0
    for j in range(1, len(eligible)):
        a = eligible[j]
        b = eligible[best]
        if a[1] > b[1] or (a[1] == b[1] and a[2] > b[2]) or (a[1] == b[1] and a[2] == b[2] and a[3] > b[3]):
            best = j
    ranked.append(eligible[best])
    eligible.pop(best)

print("\nINTERNSHIP RANKING")
for i in range(len(ranked)):
    name, score, assessment, marks = ranked[i]
    print(i + 1, name, "Weighted score:", round(score, 2))
print("Not eligible:", rejected)
