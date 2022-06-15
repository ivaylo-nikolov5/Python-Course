string = input()

chars = {}

for i in string:
    if i != " " and i not in chars:
        chars[i] = 1
    else:
        chars[i] += 1

for i in chars:
    print(f"{i} -> {chars[i]}")
