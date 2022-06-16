class Test:
    value = 52

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def sum_numbers(self, val3):
        return (self.val1 * self.val2) + val3


obj = Test(10, 5)
print(obj.sum_numbers(9))