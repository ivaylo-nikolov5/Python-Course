def recursive_drawing(idx):
    if idx < 1:
        return

    print("*" * idx)

    recursive_drawing(idx - 1)

    print("#" * idx)


number = int(input())

recursive_drawing(number)