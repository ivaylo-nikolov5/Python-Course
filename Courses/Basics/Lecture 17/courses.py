def courses():
    command = input()
    courses_dict = {}
    while command != "end":
        command = command.split(" : ")
        course = command[0]
        name = command[1]

        if course not in courses_dict:
            courses_dict[course] = []

        courses_dict[course].append(name)

        command = input()

    for x in courses_dict:
        print(f"{x}: {len(courses_dict[x])}")
        for y in courses_dict[x]:
            print(f"-- {y}")

courses()