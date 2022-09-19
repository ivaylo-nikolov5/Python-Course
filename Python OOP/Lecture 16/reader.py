from collections import deque


def read_next(*args):
    idx = 0
    while idx < len(args):
        current = deque(x for x in args[idx])
        while current:
            yield current.popleft()
        idx += 1


# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
#     print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
