numbers = [int(x) for x in input().split(" ")]
new_stack = numbers[1:]
new_stack.append(numbers[0])
print(new_stack)