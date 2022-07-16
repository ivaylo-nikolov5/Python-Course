n = int(input())

nums = []

while n > 0:
    n -= 1
    nums.append(n)

nums = list(reversed(nums))
nums = [pow(x, 2) for x in nums]

print(*nums, sep="\n")