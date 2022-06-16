def memory_game(elements: list):
    elements = [x for x in elements if x != ""]
    command = input()
    moves = 0

    while command != "end":
        middle = len(elements) // 2
        explode = command.split(" ")
        int1 = int(explode[0])
        int2 = int(explode[1])
        moves += 1

        if int1 == int2 or int1 < 0 or int2 < 0 or int1 >= len(elements) or int2 >= len(elements):
            elements = elements[:middle] + [f"-{moves}a"] + [f"-{moves}a"] + elements[middle:]
            print("Invalid input! Adding additional elements to the board")
        else:
            if elements[int1] == elements[int2]:
                print(f"Congrats! You have found matching elements - {elements[int1]}!")
                elements[int1] = ""
                elements[int2] = ""
                elements = [x for x in elements if x != ""]
            else:
                print("Try again!")

        if len(elements) == 0:
            print(f"You have won in {moves} turns!")
            break

        command = input()

    if len(elements) != 0:
        print("Sorry you lose :(")
        elements = list(map(str, elements))
        print(" ".join(elements))


els = input().split(" ")
memory_game(els)
