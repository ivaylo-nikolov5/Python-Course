import re

text = input()

expression = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"

matches = re.finditer(expression, text)

output = []

for x in matches:
    output.append(x.group())

print(*output, sep=" ")