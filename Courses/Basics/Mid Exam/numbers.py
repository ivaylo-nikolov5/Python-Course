def numbers(nums):
    length = len(nums)
    nums_sum = sum(nums)
    average = nums_sum / length
    nums = [x for x in nums if x > average]
    if len(nums) == 0:
        print("No")
    else:
        if len(nums) > 5:
            while len(nums) > 5:
                nums.remove(min(nums))
        nums = list(sorted(nums))
        nums.reverse()

        print(*nums, sep=" ")


integers = list(map(int, input().split(" ")))
numbers(integers)