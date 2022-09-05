from itertools import product

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

result = list(product(a, b))
res = ""
for pair in result:
    res += f"{pair} "

print(res.strip())

