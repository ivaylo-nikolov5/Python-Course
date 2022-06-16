def factorial(a, b):
    fact = 1
    for i in range(a, b, -1):
        fact = fact * i

    print(f"{fact:.2f}")


num1, num2 = int(input()), int(input())
factorial(num1, num2)


