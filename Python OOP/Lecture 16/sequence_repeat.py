class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        elif self.idx % len(self.sequence) == 0:
            self.idx = 0
        current = self.sequence[self.idx]
        self.number -= 1
        self.idx += 1
        return current

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

