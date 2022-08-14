from collections import deque


def list_manipulator(nums: list, action, place, *args):
    nums = deque(nums)

    def remove_end(nums, args):
        if not args:
            nums.pop()
        else:
            for x in range(args[0]):
                nums.pop()

        return nums

    def add_end(nums, args):
        nums.extend(args)
        return nums

    def remove_beginning(nums,args):
        if not args:
            nums.popleft()
        else:
            for x in range(args[0]):
                nums.popleft()

        return nums

    def add_beginning(nums, args):
        args = list(args)
        for num in range(len(args)):
            nums.appendleft(args.pop())
        return nums

    if action == "add":
        if place == "end":
            nums = add_end(nums, args)
        else:
            nums = add_beginning(nums, args)
    else:
        if place == "end":
            nums = remove_end(nums, args)
        else:
            nums = remove_beginning(nums, args)

    return list(nums)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
