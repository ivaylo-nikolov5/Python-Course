import re

text = input()
expression = r"(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"
matches = re.finditer(expression, text)

for x in matches:
    day = x.group("day")
    month = x.group("month")
    year = x.group("year")

    print(f"Day: {day}, Month: {month}, Year: {year}")