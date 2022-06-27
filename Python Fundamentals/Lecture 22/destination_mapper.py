import re

pattern = r"(\=|\/)([A-Z][a-zA-Z]{2,})\1"
text = input()
regex = re.finditer(pattern, text)

points = 0
destinations = []

for x in regex:
    destinations.append(x.group(2))
    points += len(x.group(2))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")