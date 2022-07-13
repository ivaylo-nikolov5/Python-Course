from collections import deque

boxes = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = {}


while boxes and magic_values:
    box = boxes[-1]
    magic_value = magic_values[0]
    present = box * magic_value

    if present in presents:
        if presents[present] not in crafted_presents:
            crafted_presents[presents[present]] = 0

        crafted_presents[presents[present]] += 1

        boxes.pop()
        magic_values.popleft()

    elif present < 0:
        present = box + magic_value
        boxes.pop()
        magic_values.popleft()
        boxes.append(present)

    elif present > 0:
        magic_values.popleft()
        boxes[-1] += 15

    else:
        if box == 0 and magic_value == 0:
            boxes.pop()
            magic_values.popleft()
            continue

        if box == 0:
            boxes.pop()
            continue

        if magic_value == 0:
            magic_values.popleft()
            continue

if "Doll" in crafted_presents and "Wooden train" in crafted_presents or "Teddy bear" in crafted_presents and "Bicycle" in crafted_presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    print(f"Materials left: {', '.join(str(x) for x in reversed(boxes))}")

if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

for item, value in sorted(crafted_presents.items()):
    print(f"{item}: {value}")

