def recursive_array_sum(array, idx):
    result = 0

    if idx == len(array):
        return result

    return array[idx] + recursive_array_sum(array, idx + 1)


array = [int(num) for num in input().split()]

array_sum = recursive_array_sum(array, 0)
print(array_sum)


array_sum = 0

while array:
    array_sum += array.pop()

print(array_sum)


# ---------------------------------------------------------------------------------------------------------


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


number = int(input())

print(factorial(number))


factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(factorial)


# -----------------------------------------------------------------------------


def recursive_drawing(idx):
    if idx < 1:
        return

    print("*" * idx)

    recursive_drawing(idx - 1)

    print("#" * idx)


number = int(input())

recursive_drawing(number)

number = int(input())

temp = number

while temp > 0:
    print("*" * temp)
    temp -= 1

temp += 1

while temp <= number:
    print("#" * temp)
    temp += 1

# ---------------------------------------------------------------------------


