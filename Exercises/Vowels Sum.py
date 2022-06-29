word = input()

sum = 0
letter = ""

for i in word:
    if i == "a":
        sum += 1
    elif i == "e":
        sum += 2
    elif i == "i":
        sum += 3
    elif i == "o":
        sum += 4
    elif i == "u":
        sum += 5

print(sum)

