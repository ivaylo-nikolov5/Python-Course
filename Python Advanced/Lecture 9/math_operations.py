def math_operations(*args, **kwargs):
    counter = 0
    for arg in args:
        if counter == 4:
            counter = 0

        if counter == 0:
            kwargs["a"] += arg
        elif counter == 1:
            kwargs["s"] -= arg
        elif counter == 2:
            if arg != 0:
                kwargs["d"] /= arg
        else:
            kwargs["m"] *= arg

        counter += 1

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))