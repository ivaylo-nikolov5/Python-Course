import re

text = input()

matches = re.finditer(r"\b\d{2}([\D\W])[A-Z][a-z][a-z]\1\d{4}\b", text)

output = []

for x in matches:
    output.append(x.group())

for x in output:
    x = x.split(x[2])
    print(f"Day: {x[0]}, Month: {x[1]}, Year: {x[2]}")

