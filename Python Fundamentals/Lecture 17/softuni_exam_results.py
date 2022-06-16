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
        points = int(command[2])
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


print("Results:")
for i in courses.values():
    for x in i:
        if x not in banned:
            print(f"{x} | {i[x]}")
print("Submissions:")

for i in submissions:
    print(f"{i} - {submissions[i]}")


