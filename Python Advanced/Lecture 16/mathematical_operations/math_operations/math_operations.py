def add_nums(a, b):
    return a + b


def sub_nums(a, b):
    return a - b


def mul_nums(a, b):
    return a * b


def div_nums(a, b):
    return a / b


def pow_nums(a, b):
    return a ** b


simple_operations = {
    "+": add_nums,
    "-": sub_nums,
    "*": mul_nums,
    "/": div_nums,
    "^": pow_nums
}