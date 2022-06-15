numbers = input().split(", ")
numbers = list(map(int, numbers))

indices = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        indices.append(i)

print(indices)
