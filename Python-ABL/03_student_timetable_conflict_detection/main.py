n = int(input("Number of timetable entries: "))
schedule = []
for i in range(n):
    print("\nEntry", i + 1)
    course = input("Course: ")
    group = input("Student group: ")
    room = input("Room: ")
    start = int(input("Start hour (0-23): "))
    end = int(input("End hour (1-24): "))
    if start < 0 or end > 24 or start >= end:
        print("Invalid time. Entry skipped.")
        continue
    schedule.append((course, group, room, start, end))

conflicts = 0
for i in range(len(schedule)):
    for j in range(i + 1, len(schedule)):
        c1, g1, r1, s1, e1 = schedule[i]
        c2, g2, r2, s2, e2 = schedule[j]
        overlap = s1 < e2 and s2 < e1
        if overlap and (r1 == r2 or g1 == g2):
            conflicts = conflicts + 1
            print("Conflict:", c1, "and", c2)
            if r1 == r2:
                print("Reason: Same room")
            if g1 == g2:
                print("Reason: Same student group")
if conflicts == 0:
    print("No timetable conflicts.")
else:
    print("Total conflicts:", conflicts)
