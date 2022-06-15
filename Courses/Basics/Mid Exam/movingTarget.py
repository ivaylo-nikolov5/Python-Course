def moving_target(nums):
    command = input()
    while command != "End":
        explode = command.split(" ")
        action = explode[0]
        index = int(explode[1])
        value = int(explode[2])
        if action == "Shoot" and 0 <= index < len(nums):
            current_target = nums[index]
            current_target -= value
            if current_target <= 0:
                nums.pop(index)
            else:
                nums[index] = current_target
        elif action == "Add":
            if 0 <= index < len(nums):
                nums.insert(index, value)
            else:
                print("Invalid placement!")

        elif action == "Strike":
            if index - value >= 0 and index + value < len(nums):
                nums = nums[:index - value] + nums[index + value + 1:]
            else:
                print("Strike missed!")

        command = input()
    nums = [x for x in nums if x > 0]
    nums = list(map(str, nums))
    print("|".join(nums))


numbers = list(map(int, input().split(" ")))
moving_target(numbers)