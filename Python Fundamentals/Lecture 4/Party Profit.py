group_size = int(input())
days = int(input())

coins = 0
companions = group_size

for day in range(1, days+1):
    if day % 10 == 0:
        companions -= 2

    if day % 15 == 0:
        companions += 5

    coins += 50 - (2 * companions)
    if day % 3 == 0:
        coins -= 3 * companions

    if day % 5 == 0:
        coins += 20 * companions
        if day % 3 == 0:
            coins -= 2 * companions

coins_per_companion = coins / companions

print(f"{companions} companions received {round(coins_per_companion)} coins each.")
