nums = [3,2,4]
target = 6

def linear_solution(nums, target):
    for i in range(len(nums) - 1):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target and j != i:
                print([i, j])
                break

def optimized_solution(nums, target):
    cache = {}

    for idx in range(len(nums)):
        num = nums[idx]
        if target - num in cache:
            return [cache[target - num], idx]

        cache[num] = idx

print(optimized_solution(nums, target))



