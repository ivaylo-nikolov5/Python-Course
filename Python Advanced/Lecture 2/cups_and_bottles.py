from collections import deque

cups_capacity = deque(map(int, input().split()))
filled_bottles = list(map(int, input().split()))

wasted_liters = 0

while cups_capacity:
    if not filled_bottles:
        break

    if filled_bottles[-1] - cups_capacity[0] >= 0:
        wasted_liters += filled_bottles[-1] - cups_capacity[0]
        cups_capacity.popleft()
    else:
        cups_capacity[0] -= filled_bottles[-1]

    filled_bottles.pop()

if not cups_capacity:
    bottles = [str(x) for x in filled_bottles]
    print(f"Bottles: {' '.join(bottles)}")
else:
    cups = [str(x) for x in cups_capacity]
    print(f"Cups: {' '.join(cups)}")

print(f"Wasted litters of water: {wasted_liters}")