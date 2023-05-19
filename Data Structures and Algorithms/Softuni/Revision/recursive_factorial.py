def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


number = int(input())

print(factorial(number))


number = int(input())

factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(factorial)