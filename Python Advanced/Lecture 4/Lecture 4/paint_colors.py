from collections import deque

substrings = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

colors = []

while substrings:
    first = substrings.popleft()
    second = substrings.pop() if substrings else ""
    result = first + second
    if result in main_colors or result in secondary_colors:
        colors.append(first + second)
        continue

    result = second + first
    if result in main_colors or result in secondary_colors:
        colors.append(second + first)
        continue

    first = first[:-1]
    second = second[:-1]

    if first:
        substrings.insert(len(substrings) // 2, first)
    if second:
        substrings.insert(len(substrings) // 2, second)


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

