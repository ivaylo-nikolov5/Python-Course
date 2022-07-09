from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current_order = orders[0]
    if food < current_order:
        break

    else:
        orders.popleft()
        food -= current_order

if not orders:
    print("Orders complete")
else:
    orders = [str(x) for x in orders]
    print(f"Orders left: {' '.join(orders)}")
