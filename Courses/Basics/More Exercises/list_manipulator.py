def min_max_func(nums, command, action):

    odds = [x for x in nums if x % 2 != 0]
    evens = [x for x in nums if x % 2 == 0]
    odd_even = command[1]
    index = ""

    if action == "max":

        if odd_even == "odd":
            if len(odds) == 0:
                index = "No matches"
            else:
                max_odd = max(odds)
                nums = list(reversed(nums))
                index = len(nums) - nums.index(max_odd) - 1
        else:
            if len(evens) == 0:
                index = "No matches"
            else:
                max_even = max(evens)
                nums = list(reversed(nums))
                index = len(nums) - nums.index(max_even) - 1

    else:
        if odd_even == "odd":
            if len(odds) == 0:
                index = "No matches"
            else:
                min_odd = min(odds)
                nums = list(reversed(nums))
                index = len(nums) - nums.index(min_odd) - 1
        else:
            if len(evens) == 0:
                index = "No matches"
            else:
                min_even = min(evens)
                nums = list(reversed(nums))
                index = len(nums) - nums.index(min_even) - 1

    return index


def first_last_func(nums, command, action):

    odds = [x for x in nums if x % 2 != 0]
    evens = [x for x in nums if x % 2 == 0]
    counter = int(command[1])
    odd_even = command[2]
    result = ""
    if counter > len(nums):
        return "Invalid count"
    else:
        if action == "first":
            if odd_even == "odd":
                if len(odds) >= counter:
                    result = odds[:counter]
                else:
                    result = odds

            else:
                if len(evens) >= counter:
                    result = evens[:counter]
                else:
                    result = evens
        else:
            if odd_even == "odd":
                if len(odds) >= counter:
                    result = odds[-counter:]
                else:
                    result = odds
            else:
                if len(evens) >= counter:
                    result = evens[-counter:]
                else:
                    result = evens

    return result


def exchange_func(nums, command):
    index = int(command[1])
    if index > len(nums) or index < 0:
        print("Invalid index")
    else:
        nums = list(nums[index + 1:] + nums[:index + 1])

    return nums


def list_manipulator(nums):
    command = input()
    while command != "end":
        command = command.split(" ")
        action = command[0]
        result = ""
        if action == "max" or action == "min":
            result = min_max_func(nums, command, action)

        elif action == "first" or action == "last":
            result = first_last_func(nums, command, action)

        elif action == "exchange":
            nums = exchange_func(nums, command)

        if result != "":
            print(result)

        command = input()

    print(nums)


numbers = list(map(int, input().split(" ")))
list_manipulator(numbers)
