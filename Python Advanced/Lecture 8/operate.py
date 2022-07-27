def operate(operator, *args):
    result = 0
    if operator == "+":
        result = sum(args)

    elif operator == "-":
        result = args[0]
        for num in range(1, len(args)):
            result -= args[num]

    elif operator == "*":
        result = 1
        for num in args:
            result *= num

    else:
        result = args[0]
        for num in range(1, len(args)):
            result /= args[num]

    return result


print(operate("/", 9, 2, 1))
