def josephus_permutation(nums, k):
    filtered = []
    counter = 0
    while len(nums) > 0:
        for x in range(1, len(nums)+1):
            counter += 1
            if counter % k == 0:
                filtered.append(nums[x-1])
                nums[x-1] = ""

        while "" in nums:
            nums.remove("")

    filtered = list(map(str, filtered))
    print(f"[{','.join(filtered)}]")


numbers = list(map(int, input().split(" ")))
num = int(input())
josephus_permutation(numbers, num)