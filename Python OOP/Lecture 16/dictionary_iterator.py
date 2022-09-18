class dictionary_iter:
    def __init__(self, obj: dict):
        self.obj = obj
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.obj):
            raise StopIteration
        kvpt = list(self.obj.items())
        result = kvpt[self.idx]
        self.idx += 1
        return result

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)