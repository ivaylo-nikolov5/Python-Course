def groups(numbers):
    max_num = max(numbers)
    max_group = 10 * (max_num // 10)
    nums_copy = numbers
    for i in range(10, max_group + 11, 10):
        group = []
        for j in nums_copy:
            if j <= i:
                group.append(j)

        for k in group:
            if k in nums_copy:
                nums_copy.remove(k)

        print(f"Group of {i}'s: {group}")
        if not nums_copy:
            break


nums = list(map(int, input().split(", ")))
groups(nums)