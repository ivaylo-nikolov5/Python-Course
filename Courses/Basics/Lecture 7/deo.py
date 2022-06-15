events = input().split("|")

coins = 100
energy = 100

is_closed = False

for i in events:
    split = i.split("-")
    action = split[0]
    num = int(split[1])
    if action == "rest":
        if energy + num > 100:
            print("You gained 0 energy.")
        else:
            energy += num
            print(f"You gained {num} energy.")
        print(f"Current energy: {energy}.")
    elif action == "order":
        if energy >= 30:
            energy -= 30
            coins += num
            print(f"You earned {num} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= num:
            coins -= num
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
