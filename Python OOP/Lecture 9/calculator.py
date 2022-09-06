class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        res = 1
        for arg in args:
            res *= arg

        return res

    @staticmethod
    def divide(*args):
        res = args[0]
        for arg in args[1:]:
            res /= arg

        return res

    @staticmethod
    def subtract(*args):
        res = args[0]
        for arg in args[1:]:
            res -= arg

        return res


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
