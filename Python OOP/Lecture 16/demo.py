class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.number:
            raise StopIteration
        current = self.sequence[self.counter % len(self.sequence)]
        self.counter += 1
        return current

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')


