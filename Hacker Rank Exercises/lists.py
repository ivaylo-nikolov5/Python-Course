lines = int(input())

nums = []

for _ in range(lines):
    command = input().split()
    action = command[0]
    if action == "insert":
        index = int(command[1])
        number = int(command[2])
        nums.insert(index, number)
    elif action == "append":
        number = int(command[1])
        nums.append(number)
    elif action == "remove":
        number = int(command[1])
        nums.remove(number)
    elif action == "pop":
        nums.pop()
    elif action == "reverse":
        nums = list(reversed(nums))
    elif action == "sort":
        nums = list(sorted(nums))
    elif action == "print":
        print(nums)

