stack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

other_stack = []

while stack:
    other_stack.append(stack.pop())

print(other_stack)