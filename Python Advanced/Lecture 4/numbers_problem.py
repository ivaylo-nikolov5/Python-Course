def add_func(command):
    sequence = command[1]
    nums = command[2:]
    nums = set(int(x) for x in nums)
    if sequence == "First":
        sequence1.update(nums)
        return sequence1
    else:
        sequence2.update(nums)
        return sequence2


def remove_func(command):
    sequence = command[1]
    nums = command[2:]
    nums = set(int(x) for x in nums)
    if sequence == "First":
        sequence1.difference_update(nums)
        return sequence1
    else:
        sequence2.difference_update(nums)
        return sequence2


def check_func():
    if sequence1.issubset(sequence2):
        print("True")
    elif sequence2.issubset(sequence1):
        print("True")
    else:
        print("False")


sequence1 = set(int(x) for x in input().split())
sequence2 = set(int(x) for x in input().split())

command_lines = int(input())

for _ in range(command_lines):
    command = input().split()
    action = command[0]
    if action == "Add":
        add_func(command)
    elif action == "Remove":
        remove_func(command)
    elif action == "Check":
        check_func()

print(*sorted(sequence1), sep=", ")
print(*sorted(sequence2), sep=", ")
