n = int(input())
positive = []
negative = []
even = []
odd = []

for i in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    else:
        negative.append(number)
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

command = input()
print(eval(command))
