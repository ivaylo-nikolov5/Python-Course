def insertion_sort(nums):
    for idx in range(len(nums)):
        for j in range(idx, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break

    return nums


numbers = [int(x) for x in input().split()]

print(*insertion_sort(numbers), sep=" ")