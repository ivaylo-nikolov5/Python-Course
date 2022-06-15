number = int(input())
n = list(map(str, bin(number)))
bit_zero = n[-2:-1]
print("".join(bit_zero))

