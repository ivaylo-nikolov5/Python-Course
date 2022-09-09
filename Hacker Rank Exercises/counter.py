from collections import Counter

number_of_shoes = int(input())
shoe_sizes = [int(x) for x in input().split()]
customers = int(input())
total = 0

for _ in range(customers):
    size, price = [int(x) for x in input().split()]
    if size in shoe_sizes:
        shoe_sizes.remove(size)
        total += price

print(total)