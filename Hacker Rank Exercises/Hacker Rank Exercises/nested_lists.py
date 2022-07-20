if __name__ == '__main__':
    students = int(input())
    lowest_grade = 99999999999.99
    students_list = []

    for _ in range(students):
        student = input()
        grade = float(input())
        students_list.append([grade, student])
        if grade < lowest_grade:
            lowest_grade = grade

    for student_index in range(students - 1):
        if students_list[student_index][0] == lowest_grade:
            students_list.pop(student_index)

    lowest_grade = students_list[0][0]
    students_with_lower_grades = []

    for student in students_list:
        if student[0] == lowest_grade:
            students_with_lower_grades.append(student[1])

    print(*sorted(students_with_lower_grades), sep="\n")
