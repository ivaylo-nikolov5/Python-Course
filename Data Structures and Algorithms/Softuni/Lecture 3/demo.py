# def binary_search(nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left <= right:
#         mid_idx = (right + left) // 2
#         mid_el = nums[mid_idx]
#
#         if mid_el == target:
#             return mid_idx
#
#         if mid_el < target:
#             left += 1
#         else:
#             right -= 1
#
#     return -1
#
#
# numbers = [int(x) for x in input().split()]
# target = int(input())
#
# print(binary_search(numbers, target))


##################################################################################################


# def selection_sort(nums):
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             if nums[j] < nums[i]:
#                 nums[i], nums[j] = nums[j], nums[i]
#
#     return nums
#
#
# numbers = [int(x) for x in input().split()]
#
# print(*selection_sort(numbers), sep=" ")

# def bubble_sort(nums):
#     for i in range(len(nums)):
#         i = 0
#         swaps = 0
#         for j in range(1, len(nums)):
#             if nums[i] > nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 swaps += 1
#             i += 1
#
#         if swaps == 0:
#             return nums
#
#     return nums
#
#
# numbers = [int(x) for x in input().split()]
#
# print(*bubble_sort(numbers), sep=" ")

def quicksort(start, end, nums):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]
    quicksort(start, right - 1, nums)
    quicksort(right + 1, end, nums)


numbers = [int(x) for x in input().split()]

quicksort(0, len(numbers) - 1, numbers)
print(*numbers, end=" ")
