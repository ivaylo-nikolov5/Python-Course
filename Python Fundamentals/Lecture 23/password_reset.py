def take_odd_func(string, command):
    string = [x for x in string]
    string = "".join([string[x] for x in range(len(string)) if x % 2 != 0])
    print(string)

    return string


def cut_func(string, command):
    index = int(command[1])
    length = int(command[2])

    string = string[:index] + string[index + length:]

    print(string)

    return string


def substitute_func(string, command):
    old_string = command[1]
    new_string= command[2]
    if old_string in string:
        string = string.replace(old_string, new_string)
        print(string)
    else:

        print("Nothing to replace!")

    return string


string = input()

command = input()
while command != "Done":
    command = command.split(" ")
    if command[0] == "TakeOdd":
        string = take_odd_func(string, command)
    elif command[0] == "Cut":
        string = cut_func(string, command)
    elif command[0] == "Substitute":
        string = substitute_func(string, command)

    command = input()


print(f"Your password is: {string}")
