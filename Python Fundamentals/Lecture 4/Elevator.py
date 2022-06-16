import math
#reading the data
people = int(input())
capacity = int(input())

# people_left = people
# courses = 0

#loop

# while people_left > 0:
#     people_left -= capacity
#     courses += 1
#
# print(courses)

#or with using math library
result = math.ceil(people/capacity)

print(result)
