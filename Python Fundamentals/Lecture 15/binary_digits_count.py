number = int(input())
binary_digit = input()

binary_number = []

while number >= 1:
    binary_number.append(number % 2)
    number = number // 2

if binary_digit == "1":
    print(binary_number.count(1))
else:
    print(binary_number.count(0))
