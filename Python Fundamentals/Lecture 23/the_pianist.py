def add_func(pieces: dict, command, piece):
    pianist = command[2]
    key = command[3]

    if piece in pieces:
        return f"{piece} is already in the collection!"
    else:
        pieces[piece] = [pianist, key]
        return f"{piece} by {pianist} in {key} added to the collection!"


def remove_func(pieces: dict, command, piece):
    if piece in pieces:
        pieces.pop(piece)
        return f"Successfully removed {piece}!"
    else:
        return f"Invalid operation! {piece} does not exist in the collection."


def change_key_func(pieces, command, piece):
    new_key = command[2]
    if piece in pieces:
        pieces[piece][1] = new_key
        return f"Changed the key of {piece} to {new_key}!"
    else:
        return f"Invalid operation! {piece} does not exist in the collection."



lines = int(input())
pieces = dict()

for x in range(lines):
    info = input().split("|")

    the_piece = info[0]
    composer = info[1]
    the_key = info[2]

    pieces[the_piece] = [composer, the_key]

command = input()

while command != "Stop":
    command = command.split("|")
    action = command[0]
    piece = command[1]
    result = ""

    if action == "Add":
        result = add_func(pieces, command, piece)
    elif action == "Remove":
        result = remove_func(pieces, command, piece)
    elif action == "ChangeKey":
        result = change_key_func(pieces, command, piece)

    print(result)
    command = input()

for x in pieces:
    print(f"{x} -> Composer: {pieces[x][0]}, Key: {pieces[x][1]}")
