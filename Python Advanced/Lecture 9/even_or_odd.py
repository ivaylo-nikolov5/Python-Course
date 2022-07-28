def even_odd(*args):
    command = args[-1]
    if command == "even":
        return [args[x] for x in range(len(args) - 1) if args[x] % 2 == 0]
    else:
        return [args[x] for x in range(len(args) - 1) if args[x] % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
