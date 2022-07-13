from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))

shakes = 0

while chocolates and milk_cups and shakes < 5:
    chocolate = chocolates[-1]
    cup = milk_cups[0]

    if chocolate == cup:
        chocolates.pop()
        milk_cups.popleft()
        shakes += 1
    else:

        if chocolate <= 0 and cup <= 0:
            chocolates.pop()
            milk_cups.popleft()
            continue

        if chocolate <= 0:
            chocolates.pop()
            continue

        if cup <= 0:
            milk_cups.popleft()
            continue
        milk_cups.append(milk_cups.popleft())
        chocolates[0] -= 5
if shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
else:
    print("Milk: empty")