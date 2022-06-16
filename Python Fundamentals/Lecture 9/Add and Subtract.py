def sum_numbers(a, b):
    return a + b


def subtract(sum_num, c):
    return sum_num - c


num1, num2, num3 = int(input()), int(input()), int(input())

print(subtract(sum_numbers(num1, num2), num3))