n = int(input())

numbers_list = []

for i in range(n):
    numbers = int(input())
    numbers_list.append(numbers)

filtered_list = []
command = input()

for number in numbers_list:
    if command == "even":
        if number % 2 == 0:
            filtered_list.append(number)
    elif command == "odd":
        if number % 2 != 0:
            filtered_list.append(number)
    elif command == "positive":
        if number >= 0:
            filtered_list.append(number)
    else:
        if number < 0:
            filtered_list.append(number)

print(filtered_list)