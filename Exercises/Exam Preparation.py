bad_grades = int(input())

bad_grades_count = 0
grades_sum = 0
number_of_problems = 0
last_problem = ""
is_failed = True

while bad_grades_count < bad_grades:
    problem_name = input()
    if problem_name == "Enough":
        is_failed = False
        break
    last_problem = problem_name
    grade = int(input())
    if grade <= 4:
        bad_grades_count += 1
    grades_sum += grade
    number_of_problems += 1

if is_failed:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    print(f"Average score: {(grades_sum / number_of_problems):.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")