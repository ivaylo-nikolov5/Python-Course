number = input()
largest = []
for x in number:
    largest.append(int(x))

largest = list(map(str, reversed(sorted(largest))))
print("".join(largest))
