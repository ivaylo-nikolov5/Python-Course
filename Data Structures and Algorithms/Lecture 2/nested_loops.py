def nested_loops(n, nums):
    if len(nums) == n:
        print(*nums, sep=" ")
        return
    for x in range(1, n + 1):
        nums.append(x)
        nested_loops(n, nums)
        nums.pop()

number = int(input())
nested_loops(number, [])