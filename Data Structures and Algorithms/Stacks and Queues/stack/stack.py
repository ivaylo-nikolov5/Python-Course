from stack.exceptions import EmptyStack


class Stack:
    def __init__(self):
        self.__stack = []

    def get_stack(self):
        return self.__stack

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if not self.__stack:
            raise EmptyStack("You cannot pop an item from an empty stack!")
        item = self.__stack.pop()
        return item
