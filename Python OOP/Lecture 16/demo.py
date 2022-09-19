def fibonacci():
    num1 = 0
    num2 = 1
    yield num1
    yield num2
    while True:
        next_num = num1 + num2
        yield next_num
        num1 = num2
        num2 = next_num


generator = fibonacci()
for i in range(1):
    print(next(generator))

