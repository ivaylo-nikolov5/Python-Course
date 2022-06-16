numbers = input().split(" ")

filtered = []

for i in numbers:
    i = int(i)
    if i < 0:
        filtered.append(abs(i))
    else:
        filtered.append(-i)

print(filtered)
