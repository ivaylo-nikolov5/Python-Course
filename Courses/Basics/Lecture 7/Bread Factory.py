events = input().split("|")

energy = 100
coins = 100
cannot_handle = False

for action in events:
    current_event = action.split("-")
    event = current_event[0]
    number = int(current_event[1])
    if event == "rest":
        if energy >= 100:
            print(f"You gained 0 energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            cannot_handle = True
            break

if not cannot_handle:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
