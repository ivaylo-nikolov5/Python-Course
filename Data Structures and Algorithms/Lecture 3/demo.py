def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (right + left) // 2
        mid_el = nums[mid_idx]

        if mid_el == target:
            return mid_idx

        if mid_el < target:
            left += 1
        else:
            right -= 1

    return -1


numbers = [int(x) for x in input().split()]
target = int(input())

print(binary_search(numbers, target))