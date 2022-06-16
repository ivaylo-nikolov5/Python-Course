number = int(input())
to_base = int(input())

result = ""
def num_to_base(num, base, res):
    res = ""
    while num != 0:
        left = num // base
        res += str(left)
    return res

print(num_to_base(number, to_base, result))














