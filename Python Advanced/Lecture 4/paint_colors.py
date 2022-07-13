from collections import deque

substrings = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

colors = list()

while substrings:
    first = substrings.popleft()
    last = substrings.pop() if substrings else ""
    result = first + last
    if result in main_colors or result in secondary_colors:
        colors.append(result)
        continue

    result = last + first
    if result in main_colors or result in secondary_colors:
        colors.append(result)
        continue

    first = first[:-1]
    last = last[:-1]

    if first:
        substrings.insert(len(substrings) // 2, first)
    if last:
        substrings.insert(len(substrings) // 2, last)

result = []
required_colors = {
    "orange": ["red", 'yellow'],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}
for color in colors:
    if color in main_colors:
        result.append(color)
    else:
        is_valid = True
        for required_color in required_colors[color]:
            if required_color not in colors:
                is_valid = False
                break

        if is_valid:
            result.append(color)

print(result)