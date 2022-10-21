from stack.exceptions import EmptyStack


class Stack:
    def __init__(self):
        self.__stack = []

    def get_stack(self):
        return self.__stack

    def push(self, item):
        self.__stack.append(item)

    def push_multiple_items(self, *items):
        for item in items:
            self.push(item)

    def pop(self):
        if not self.__stack:
            raise EmptyStack("You cannot pop an item from an empty stack!")
        item = self.__stack[-1]
        del self.__stack[-1]
        return item

    def peek(self):
        if not self.__stack:
            raise EmptyStack("The stack is empty!")
        return self.__stack[-1]

    def __add__(self, other):
        new_stack = self.__stack + other.__stack
        return new_stack
