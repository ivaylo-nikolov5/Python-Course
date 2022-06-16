def factorial(num):
    f = 1
    if num >= 1:
        for i in range(1, num + 1):
            f = f * i
        return f


num1 = int(input())
num2 = int(input())

result = factorial(num1) / factorial(num2)

print(f"{result:.2f}")