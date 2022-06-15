command = input()

courses = dict()
submissions = dict()
banned = []

while command != "exam finished":
    command = command.split("-")
    name = command[0]
    if "banned" in command:
        banned.append(name)

    else:
        course = command[1]
        points = command[2]

        if course not in submissions:
            submissions[course] = 1
        else:
            submissions[course] += 1

        if course not in courses:
            courses[course] = {name: points}
        else:
            if name not in courses[course]:
                courses[course][name] = points
            elif points > courses[course][name]:
                courses[course][name] = points

    command = input()

print(f"Results:")
for x in courses.values():
    for y in x:
        if y not in banned:
            print(f"{y} | {x[y]}")

print("Submissions:")

for x in submissions:
    print(f"{x} - {submissions[x]}")