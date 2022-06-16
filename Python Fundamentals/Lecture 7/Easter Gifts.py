gifts = input().split(" ")
command = input()


while not command == "No Money":
    current_command = command.split(" ")
    action = current_command[0]
    product = current_command[1]
    if action == "OutOfStock":
        for i in range(len(gifts)):
            if product in gifts[i]:
                gifts[i] = "None"
    elif action == "Required":
        index = int(current_command[2])
        for i in range(len(gifts)):
            if index == i:
                gifts[i] = product
    elif action == "JustInCase":
        gifts[-1] = product

    command = input()

for i in gifts:
    if i == "None":
        gifts.remove(i)


print(" ".join(gifts))


