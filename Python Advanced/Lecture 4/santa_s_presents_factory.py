from collections import deque

boxes = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}

dolls = 0
wooden_trains = 0
teddy_bears = 0
bicycles = 0


while boxes and magic_values:
    box = boxes[-1]
    magic_value = magic_values[0]
    present = box * magic_value

    if present in presents:
        boxes.pop()
        magic_values.popleft()
        if presents[present] == "Doll":
            dolls += 1
        elif presents[present] == "Wooden train":
            wooden_trains += 1
        elif presents[present] == "Teddy bear":
            teddy_bears += 1
        else:
            bicycles += 1
    else:
        if present < 0:
            present = magic_value + box
            magic_values.popleft()
            boxes.pop()
            boxes.append(present)
        elif magic_value == 0 or box == 0:
            if magic_value == 0:
                magic_values.popleft()
            if box == 0:
                boxes.pop()
        elif present not in presents and present > 0:
            magic_values.popleft()
            boxes[-1] += 15


if dolls >= 1 and wooden_trains >= 1 or teddy_bears >= 1 and bicycles >= 1:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    boxes = list(reversed(boxes))
    print(f"Materials left: {', '.join(str(x) for x in boxes)}")

if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

if bicycles:
    print(f"Bicycle: {bicycles}")
if dolls:
    print(f"Doll: {dolls}")
if teddy_bears:
    print(f"Teddy bear: {teddy_bears}")
if wooden_trains:
    print(f"Wooden train: {wooden_trains}")
