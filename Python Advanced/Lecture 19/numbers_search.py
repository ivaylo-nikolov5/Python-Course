def numbers_searching(*args):
    result = []
    numbers = {}

    # finding repeating numbers
    for number in args:
        if number not in numbers:
            numbers[number] = 0
        numbers[number] += 1

    repeating_numbers = []
    for num in numbers:
        if numbers[num] > 1:
            repeating_numbers.append(num)

    repeating_numbers = list(sorted(repeating_numbers))
    args = list(set(sorted(args)))
    missing_num = 0
    # finding missing number

    for num in range(args[0], args[-1]):
        if num not in args:
            missing_num = num

    return [missing_num, repeating_numbers]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))


