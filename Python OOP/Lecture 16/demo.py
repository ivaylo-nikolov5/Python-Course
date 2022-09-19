def read_next(*args):
    for obj in args:
        for i in obj:
            yield i


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

