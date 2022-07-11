lines = int(input())
grades_dict = {}

for _ in range(lines):
    student, grade = input().split()
    if student not in grades_dict:
        grades_dict[student] = []

    grades_dict[student].append(float(grade))

for student, grades in grades_dict.items():
    average = sum(grades) / len(grades)
    print(f"{student} -> {' '.join(str(f'{x:.2f}') for x in grades)} (avg: {average:.2f})")


