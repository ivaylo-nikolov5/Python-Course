employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
students_count = int(input())

hours = 0
per_hour = employee1 + employee2 + employee3
the_range = students_count

for i in range(1, the_range):
    if i % 4 == 0:
        hours += 1
    else:
        students_count -= per_hour
        hours += 1

    if students_count <= 0:
        break

print(f"Time needed: {hours}h.")

