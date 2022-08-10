from math_operations.demo import operations_dict

expression = input().split()

a = float(expression[0])
operator = expression[1]
b = float(expression[2])

result = operations_dict[operator](a, b)

print(f"{float(result):.2f}")