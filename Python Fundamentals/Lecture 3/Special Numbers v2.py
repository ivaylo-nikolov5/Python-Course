number = int(input())

for i in range(1, number + 1):
    working_number = i
    digit_sum = 0
    while working_number > 0:
        digit_sum += working_number % 10
        working_number = int(working_number / 10)

    is_special = digit_sum == 5 or digit_sum == 7 or digit_sum == 11

    print(f"{i} -> {is_special}")
