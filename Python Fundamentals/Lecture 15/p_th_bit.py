number = int(input())
position = int(input())
to_binary = bin(number)
p = to_binary[-position-1]
print(p)
