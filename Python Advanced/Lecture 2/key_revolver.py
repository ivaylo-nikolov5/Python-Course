from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(map(int, input().split(" ")))
intelligence = int(input())

shots = 0
while locks:
    if not bullets:
        break
    if bullets[-1] <= locks[0]:

        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    bullets.pop()
    shots += 1
    if shots % gun_barrel_size == 0 and bullets:
        print("Reloading!")

if not locks:
    spent_money = intelligence - (shots * bullet_price)
    print(f"{abs(len(bullets))} bullets left. Earned ${spent_money}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")