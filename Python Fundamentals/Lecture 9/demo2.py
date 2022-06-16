num = int(input())
num2 = int(input())

fact = 1
for i in range(num, num2, -1):
    fact = fact * i

print(fact)