nums = input().split(", ")
nums_copy = []

for i in nums:
    i = int(i)
    if i != 0:
        nums_copy.append(i)
for i in nums:
    i = int(i)
    if i == 0:
        nums_copy.append(i)

print(nums_copy)