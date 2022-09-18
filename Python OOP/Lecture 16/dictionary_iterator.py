class dictionary_iter:
    def __init__(self, obj: dict):
        self.obj = obj
        self.key_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.key_idx == len(self.obj):
            raise StopIteration
        keys = list(self.obj.keys())
        values = list(self.obj.values())
        result = (keys[self.key_idx], values[self.key_idx])
        self.key_idx += 1
        return result

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

