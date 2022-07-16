lines = int(input())

even_numbers = []

for _ in range(lines):
    even_numbers.append([x for x in [int(y) for y in input().split(", ")] if x % 2 == 0])

print(even_numbers)