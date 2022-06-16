def student_academy(lines):
    grades_dict = {}
    for x in range(lines):
        name = input()
        grade = float(input())

        if name not in grades_dict:
            grades_dict[name] = []

        grades_dict[name].append(grade)

    for x in grades_dict:
        average_grade = sum(grades_dict[x]) / len(grades_dict[x])
        if average_grade >= 4.5:
            print(f"{x} -> {average_grade:.2f}")


student_academy(int(input()))

