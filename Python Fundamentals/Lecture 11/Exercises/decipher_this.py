def decipher(message):
    for i in message:
        digits = [x for x in i if x.isdigit()]
        letters = [y for y in i if y.islower() or y.isupper()]
        to_char = chr(int("".join(digits)))
        letters[0], letters[-1] = letters[-1], letters[0]

        print(f"{to_char}{''.join(letters)}", end=" ")


string = input().split(" ")
decipher(string)
