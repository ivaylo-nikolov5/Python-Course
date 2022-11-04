def bubble_sort(nums):
    for i in range(len(nums) - 1):
        moves = 0
        i = 0
        for j in range(i + 1, len(nums)):
            num1 = nums[i]
            num2 = nums[j]

            if num1 > num2:
                nums[i], nums[j] = nums[j], nums[i]
                moves += 1
            i += 1
        if moves == 0:
            return nums

    return nums


numbers = [int(x) for x in input().split()]
print(*bubble_sort(numbers), sep=" ")