lines, columns = input().split(", ")

nums = []
total = 0
for _ in range(int(lines)):
    numbers = list(map(int, input().split(", ")))
    if len(numbers) == int(columns):
        nums.append(numbers)
        total += sum(numbers)

print(total)
print(nums)
