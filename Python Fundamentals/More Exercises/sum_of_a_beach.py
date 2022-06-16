string = input().lower()
words = ["sand", "water", "fish", "sun"]
counter = 0

for x in words:
    while x in string:
        if x in string:
            counter += string.count(x)
            string = string.replace(x, "")
        else:
            break
print(counter)
