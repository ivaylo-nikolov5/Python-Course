def students():
    info = input()
    courses = dict()
    while ":" in info:
        explode = info.split(":")
        name = explode[0]
        student_id = explode[1]
        course = explode[2]

        if course not in courses.keys():
            courses[course] = dict()

        courses[course][student_id] = name

        info = input()

    info = info.replace("_", " ")

    for i in courses[info]:
        print(f"{courses[info][i]} - {i}")

students()
