from math import log

num = int(input())
base = input()

if base == "natural":
    res = log(num)
else:
    res = log(num, int(base))

print(f"{res:.2f}")
