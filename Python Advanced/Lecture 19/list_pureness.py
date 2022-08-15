from collections import deque

def best_list_pureness(nums: list, rotations):
    nums = deque(nums)

    best_pureness = 0
    best_rotation = 0

    for rotation in range(rotations + 1):
        current_pureness = 0
        for num in range(len(nums)):
            current_pureness += nums[num] * num

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = rotation

        nums.rotate()

    return f"Best pureness {best_pureness} after {best_rotation} rotations"

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

