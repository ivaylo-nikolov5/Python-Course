class vowels:
    VOWELS = "aeiouyAEIOUY"

    def __init__(self, obj):
        self.obj = obj
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.obj):
            current = self.obj[self.i]
            self.i += 1
            if current in vowels.VOWELS:
                return current
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
