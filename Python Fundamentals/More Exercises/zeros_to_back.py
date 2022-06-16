nums = list(map(int, input().split(", ")))
for x in range(len(nums)):
    if nums[x] == 0:
        nums[x] = ""

blanks = nums.count("")
nums = [x for x in nums if x != ""]
for x in range(blanks):
    nums.append(0)

print(nums)