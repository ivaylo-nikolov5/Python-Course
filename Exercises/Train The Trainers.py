jury = int(input())

average_grade = 0
presentations_counter = 0
presentation = input()

while presentation != "Finish":
    grade_counter = 0
    for i in range(jury):
        grade = float(input())
        presentations_counter += 1
        grade_counter += grade
        average_grade += grade
        if i == jury:
            break
    print(f"{presentation} - {grade_counter/jury:.2f}.")
    presentation = input()

print(f"Student's final assessment is {average_grade/presentations_counter:.2f}.")