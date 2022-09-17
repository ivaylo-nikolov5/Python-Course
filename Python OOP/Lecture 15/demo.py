class vowels:
    def __init__(self, string):
        self.string = string
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < len(self.string):
            current = self.string[self.start]
            self.start += 1
            if current in "aeyuioAEYUIO":
                return current
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
