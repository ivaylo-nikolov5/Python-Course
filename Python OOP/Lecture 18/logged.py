def logged(function):
    def wrapper(*args):
        result = ""
        result += "you called " + function.__name__ + f"{args}"
        result += f"\nit returned {function(*args)}"
        return result
    return wrapper

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))


