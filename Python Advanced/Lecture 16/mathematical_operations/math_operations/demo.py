operations_dict = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "^": lambda a, b: a ** b
}

if __name__ == "__main__":
    print(operations_dict["/"](5, 0))