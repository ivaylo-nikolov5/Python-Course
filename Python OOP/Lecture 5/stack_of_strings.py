class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        if element.isalpha():
            self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        res = len(self.data) == 0
        return res

    def __str__(self):
        res = list(reversed(self.data))
        return "[" + ", ".join(res) + "]"


stack = Stack()
stack.push("hello")
stack.push("hi")
print(stack)
print(stack.pop())
print(stack.top())
print(stack.is_empty())
print(stack)