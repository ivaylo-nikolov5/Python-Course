def change_func(word, command):
    substring = command[1]
    replacement = command[2]

    word = word.replace(substring, replacement)

    return word


def insert_func(word: list, command):
    index = int(command[1])
    value = command[2]

    word = [x for x in word]
    word.insert(index, value)
    word = "".join(word)

    return word


def move_func(word, command):
    letters = int(command[1])
    word = word[letters:] + word[:letters]

    return word


def the_imitation_game(word):
    result = ""
    command = input()
    while command != "Decode":
        command = command.split("|")
        if command[0] == "ChangeAll":
            word = change_func(word, command)

        elif command[0] == "Insert":
            word = insert_func(word, command)

        elif command[0] == "Move":
            word = move_func(word, command)

        command = input()

    print(f"The decrypted message is: {''.join(word)}")


string = input()
the_imitation_game(string)