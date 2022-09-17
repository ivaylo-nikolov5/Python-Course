class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.idx = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= 0:
            current = self.iterable[self.idx]
            self.idx -= 1
            return current
        raise StopIteration

reversed_list = reverse_iter("abcdef")
for item in reversed_list:
    print(item)



