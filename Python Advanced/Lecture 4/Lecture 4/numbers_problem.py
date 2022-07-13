first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

command_lines = int(input())

for _ in range(command_lines):
    command = input().split()
    action = command[0]
    sequence = command[1]
    if action == "Add":
        nums = set(command[2:])
        nums = set(int(x) for x in nums)
        if sequence == "First":
            first.update(nums)
        else:
            second.update(nums)
    elif action == "Remove":
        nums = set(command[2:])
        nums = set(int(x) for x in nums)
        if sequence == "First":
            first.difference_update(nums)
        else:
            second.difference_update(nums)
    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
