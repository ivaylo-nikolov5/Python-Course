n1 = int(input())
n2 = int(input())
operation = input()

if operation == "+":
    sum = n1 + n2
    if (sum % 2) == 0:
        print(f"{n1} + {n2} = {sum} - even")
    else:
        print(f"{n1} + {n2} = {sum} - odd")
elif operation == "-":
    diff = n1 - n2
    if (diff % 2) == 0:
        print(f"{n1} - {n2} = {diff} - even")
    else:
        print(f"{n1} - {n2} = {diff} - odd")
elif operation == "*":
    mult = n1 * n2
    if (mult % 2) == 0:
        print(f"{n1} * {n2} = {mult} - even")
    else:
        print(f"{n1} * {n2} = {mult} - odd")

elif operation == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        division = n1 / n2
        print(f"{n1} / {n2} = {division}")
elif operation == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        devi = n1 % n2
        print(f"{n1} % {n2} = {devi}")








