from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_capacity = [int(x) for x in input().split()]

wasted_liters = 0

while cups_capacity:
    if not bottles_capacity:
        break

    bottle = bottles_capacity[-1]
    cup = cups_capacity[0]

    if bottle < cup:
        cups_capacity[0] -= bottle

    else:
        wasted_liters += bottle - cup
        cups_capacity.popleft()

    bottles_capacity.pop()

if not cups_capacity:
    bottles_capacity = [str(x) for x in bottles_capacity]
    print(f"Bottles: {' '.join(bottles_capacity)}")
else:
    cups_capacity = [str(x) for x in cups_capacity]
    print(f"Cups: {' '.join(cups_capacity)}")

print(f"Wasted litters of water: {wasted_liters}")