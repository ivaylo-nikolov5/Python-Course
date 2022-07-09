import re

info = input()
pattern = r"(#|\|)([A-Z][a-z]+)( [A-Za-z]+)*\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"

regex = re.finditer(pattern, info)
calories = 0
products = []
for x in regex:
    if x.group(3) is not None:
        products.append(f"Item: {x.group(2)}{x.group(3)}, Best before: {x.group(4)}, Nutrition: {x.group(5)}")
    else:
        products.append(f"Item: {x.group(2)}, Best before: {x.group(4)}, Nutrition: {x.group(5)}")

    calories += int(x.group(5))

print(f"You have food to last you for: {calories // 2000} days!")

for x in products:
    print(x)