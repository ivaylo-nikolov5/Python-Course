def sorted_list(nums):
    for idx in range(len(nums)):
        for next_num in nums[idx + 1:]:
            if nums[idx] > next_num:
               smallest_num_idx = nums.index(next_num)
               nums[idx], nums[smallest_num_idx] = nums[smallest_num_idx], nums[idx]

    return nums


numbers = [int(x) for x in input().split()]
print(*sorted_list(numbers), sep=" ")
