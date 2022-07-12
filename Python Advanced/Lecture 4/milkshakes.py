from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(x) for x in input().split(", ")])

milkshakes = 0
done = False

while chocolates and cups_of_milk:
    current_chocolate = chocolates[-1]
    current_cup_of_milk = cups_of_milk[0]
    if current_chocolate == current_cup_of_milk:
        chocolates.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        if current_chocolate <= 0 and current_cup_of_milk <= 0:
            chocolates.pop()
            cups_of_milk.popleft()
        elif current_cup_of_milk <= 0:
            cups_of_milk.popleft()
        elif current_chocolate <= 0:
            chocolates.pop()
        else:
            cups_of_milk.append(cups_of_milk.popleft())
            chocolates[0] -= 5

    if milkshakes == 5:
        done = True
        break

if done:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print("Milk: empty")

