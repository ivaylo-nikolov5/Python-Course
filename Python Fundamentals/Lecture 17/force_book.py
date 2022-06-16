def create_force_side(side, member, book):
    condition = [current_side for current_side in book if member in book[current_side]]

    if len(condition) == 0:
        if side not in book:
            book[side] = [member]
        else:
            book[side].append(member)

        return book


def create_force_user(side, member, book):
    for current_side in book:
        if member in book[current_side]:
            if len(book[current_side]) > 1:
                book[current_side].pop(member)
                break

            else:
                del book[current_side]
                break
    if side in book:
        book[side].append(member)
    else:
        book[side] = [member]
    print(f"{member} joins the {side} side!")

def force_book():
    command = input()
    book = {}

    while command != "Lumpawaroo":

        if "|" in command:
            command = command.split(" | ")
            side = command[0]
            member = command[1]
            create_force_side(side, member, book)

        elif "->" in command:
            command = command.split(" -> ")
            member = command[0]
            side = command[1]
            create_force_user(side, member, book)

        command = input()

    for data in book:
        print(f"Side: {data}, Members: {len(book[data])}")
        for name in book[data]:
            print(f"! {name}")

force_book()


#or

def force_side(command, sides: dict):
    command = command.split(" | ")
    side = command[0]
    user = command[1]
    is_inside = False

    for x in sides:
        for y in sides[x]:
            if user == y:
                is_inside = True

    if side not in sides and not is_inside:
        sides[side] = [user]

    elif is_inside:
        pass
    elif not is_inside:
        sides[side].append(user)


def force_user(command, sides: dict):
    command = command.split(" -> ")
    user = command[0]
    side = command[1]
    is_inside = False

    for x in sides:
        for y in sides[x]:
            if user == y:
                is_inside = True

    if is_inside and side not in sides:
        sides[side] = [user]

    elif is_inside:
        is_done = False
        for x in sides:
            for y in sides[x]:
                if user == y:
                    sides[x].remove(user)
                    is_done = True
                    break
            if is_done:
                break
        sides[side].append(user)

    elif not is_inside:
        sides[side].append(user)

    print(f"{user} joins the {side} side!")


def force_book():
    command = input()
    sides_dict = {}

    while command != "Lumpawaroo":
        if "|" in command:
            force_side(command, sides_dict)
        else:
            force_user(command, sides_dict)

        command = input()

    for x in sides_dict:
        if len(sides_dict[x]) != 0:
            print(f"Side: {x}, Members: {len(sides_dict[x])}")
            for y in sides_dict[x]:
                print(f"! {y}")


force_book()
