import math

x = int(input())
w = int(input())
m = int(input())

total_by_course = w * m

needed_courses = math.ceil(x / total_by_course)

print(needed_courses)