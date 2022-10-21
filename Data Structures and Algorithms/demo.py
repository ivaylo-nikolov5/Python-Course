from stack.stack import Stack

stack = Stack()
stack.push(2)
stack.push(4)
stack.push(5)
stack.push(8)

stack2 = Stack()
stack2.push(1)
stack2.push(5)
stack2.push(7)
stack2.push(9)

print(stack + stack2)


