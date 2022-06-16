n = int(input())

top_students = 0
four_to_five = 0
threee_to_four = 0
fail = 0
average = 0

for i in range(n):
    grade = float(input())
    if grade >= 5.00:
        top_students += 1
    elif 4.00 <= grade < 5.00:
        four_to_five += 1
    elif 3.00 <= grade < 4.00:
        threee_to_four += 1
    elif grade < 3.00:
        fail += 1
    average += grade

top_students_percent = 100 * top_students / n
four_to_five_percent = 100 * four_to_five / n
threee_to_four_percent = 100 * threee_to_four / n
fail_percent = 100 * fail / n
average_percent = average / n

print(f"Top students: {top_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {four_to_five_percent:.2f}%")
print(f"Between 3.00 and 3.99: {threee_to_four_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average_percent:.2f}")



