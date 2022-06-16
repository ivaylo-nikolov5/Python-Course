number = int(input())
n = list(map(str, bin(number)))
n.remove(n[0])
n.remove(n[0])
n = n >> 1
print(joined)