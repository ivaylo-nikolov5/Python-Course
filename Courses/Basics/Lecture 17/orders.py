def orders():
    orders_dict = {}
    command = input()

    while command != "buy":
        command = command.split(" ")
        product = command[0]
        price = float(command[1])
        quantity = int(command[2])

        if product not in orders_dict:
            orders_dict[product] = [price, quantity]

        else:
            if price != orders_dict[product][0]:
                orders_dict[product][0] = price
            orders_dict[product][1] += quantity

        command = input()

    for x in orders_dict:
        total = orders_dict[x][0] * orders_dict[x][1]
        print(f"{x} -> {total:.2f}")


orders()