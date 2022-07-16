n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
average = 0

for name in student_marks:
    if name == query_name:
        average = sum(student_marks[name]) / len(student_marks[name])
        break
print(f"{average:.2f}")
