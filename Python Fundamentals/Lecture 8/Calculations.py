action = input()
a = int(input())
b = int(input())



def calculator(action, a, b):
    if action == "multiply":
        return a * b
    elif action == "divide":
        return a / b
    elif action == "add":
        return a + b
    elif action == "subtract":
        return a - b

print(int(calculator(action, a, b)))