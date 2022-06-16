def swap_multiply(nums: list, explode: list, action):
    num1 = int(explode[1])
    num2 = int(explode[2])
    if action == "swap":
        nums[num1], nums[num2] = nums[num2], nums[num1]
    elif action == "multiply":
        nums[num1] *= nums[num2]


def array_modifier(nums):
    command = input()
    while command != "end":
        explode = command.split(" ")
        action = explode[0]
        if action == "swap":
            swap_multiply(nums, explode, action)
        elif action == "multiply":
            swap_multiply(nums, explode, action)
        elif action == "decrease":
            nums = list(map(lambda x: x - 1, nums))

        command = input()

    print(*nums, sep=", ")


numbers = list(map(int, input().split(" ")))
array_modifier(numbers)
