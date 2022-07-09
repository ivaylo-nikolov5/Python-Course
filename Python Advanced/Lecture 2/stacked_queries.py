lines = int(input())

numbers = []

for _ in range(lines):
    command = input()
    if command == "2" and numbers:
        numbers.pop()
    elif command == "3" and numbers:
        print(max(numbers))
    elif command == "4" and numbers:
        print(min(numbers))
    elif command[0] == "1":
        _, number = command.split()
        numbers.append(number)

new_nums = []
while numbers:
    new_nums.append(numbers.pop())

print(*new_nums, sep=", ")