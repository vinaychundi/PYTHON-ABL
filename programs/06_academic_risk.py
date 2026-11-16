n = int(input("Number of students: "))
high = 0
medium = 0
low = 0
for i in range(n):
    print("\nStudent", i + 1)
    name = input("Name: ")
    m1 = float(input("Subject 1 marks: "))
    m2 = float(input("Subject 2 marks: "))
    m3 = float(input("Subject 3 marks: "))
    attendance = float(input("Attendance percentage: "))
    lab = float(input("Lab score: "))
    average = (m1 + m2 + m3) / 3
    risk_count = 0
    reasons = []
    if average < 50:
        risk_count = risk_count + 1
        reasons.append("Low marks")
    if attendance < 75:
        risk_count = risk_count + 1
        reasons.append("Low attendance")
    if lab < 50:
        risk_count = risk_count + 1
        reasons.append("Low lab score")
    if risk_count >= 2:
        category = "HIGH"
        high = high + 1
    elif risk_count == 1:
        category = "MEDIUM"
        medium = medium + 1
    else:
        category = "LOW"
        low = low + 1
    print(name, "Average:", average, "Risk:", category, "Reasons:", reasons)

print("Risk totals - High:", high, "Medium:", medium, "Low:", low)
