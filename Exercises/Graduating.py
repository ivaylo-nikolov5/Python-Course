name = input()

average_grade = 0
times_broke = 0
grade = 0

while grade != 12:
    year_grade = float(input())
    average_grade += year_grade

    if year_grade < 4:
        times_broke += 1

    if times_broke >= 2:
        break
    grade += 1

average_grade = average_grade / grade
if grade >= 12:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{name} has been excluded at {grade} grade")
