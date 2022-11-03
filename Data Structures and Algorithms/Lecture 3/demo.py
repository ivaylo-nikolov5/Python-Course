

numbers = [int(x) for x in input().split()]
target = int(input())

print(binary_search(numbers, target, 0, len(numbers)))