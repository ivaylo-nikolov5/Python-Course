def fill_the_lines(text):
    result = []
    counter = 0
    for line in text.readlines():
        if counter % 2 == 0:
            result.append(line[:-1])
        counter += 1

    return result


def replacing_chars(lines):
    chars_for_replacing = ("-", ",", ".", "!", "?")

    for line in range(len(lines)):
        for char in chars_for_replacing:
            lines[line] = lines[line].replace(char, "@")

    return lines


def revering_the_lines(lines):
    new_lines = []

    for line in range(len(lines)):
        line = lines[line].split()

        line = list(reversed(line))

        new_lines.append(line)

    return new_lines


try:
    with open("text.txt") as text:
        # Filling the list with the strings
        lines = fill_the_lines(text)

        # Replacing the given characters with "@"
        lines = replacing_chars(lines)

        # Reversing the lines
        lines = revering_the_lines(lines)

        # Printing the final result
        for line in lines:
            print(*line, sep=" ")

except FileNotFoundError:
    print("Cannot find the searched file! :(")