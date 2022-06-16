first = int(input())
second = int(input())
point = int(input())

left = min(first, second)
right = max(first, second)

distance_left = abs(left - point)
distance_right = abs(right - point)

min_distance = min(distance_right, distance_left)

if point < left or point > right:
    print("out")
else:
    print("in")
print(min_distance)