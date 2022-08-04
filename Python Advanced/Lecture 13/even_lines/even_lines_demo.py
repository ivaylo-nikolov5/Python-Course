to_replace = ["-", ",", ".", "!", "?"]

with open("text.txt") as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            line = " ".join(list(reversed([el for el in line.split()])))
            for el in to_replace:
                line = line.replace(el, "@")

            print(line)
