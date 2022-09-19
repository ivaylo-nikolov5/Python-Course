class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.passed_iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration()
        current = self.passed_iterations * self.step
        self.count -= 1
        self.passed_iterations += 1
        return current

numbers = take_skip(2, 6)
for number in numbers:
    print(number)


