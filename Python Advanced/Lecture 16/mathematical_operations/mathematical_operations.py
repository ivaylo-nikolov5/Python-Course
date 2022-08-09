from math_operations.math_operations import simple_operations

exp = input().split()

n = float(exp[0])
operator = exp[1]
m = float(exp[2])

res = simple_operations[operator]

print(f"{res(n, m):.2f}")