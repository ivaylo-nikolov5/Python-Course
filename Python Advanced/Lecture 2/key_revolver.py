from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
prize = int(input())

shots = 0

while locks:
    shots += 1
    if bullets[-1] > locks[0]:
        print("Ping!")
    else:
        print("Bang!")
        locks.popleft()

    bullets.pop()

    if shots % barrel_size == 0 and bullets:
        print("Reloading!")

    if not bullets:
        break

if not locks:
    earned = prize - shots * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")