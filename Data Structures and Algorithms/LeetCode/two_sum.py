nums = input()[1:-1].split(",")
nums = [int(x) for x in nums]

target = int(input())

for i in range(len(nums) - 1):
    for j in range(1, len(nums)):
        if nums[i] + nums[j] == target and j != i:
            print([i, j])
            break
