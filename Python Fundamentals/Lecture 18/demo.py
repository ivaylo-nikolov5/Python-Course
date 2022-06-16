command = input()

while command != "end":
    reverse = ""
    for x in range(len(command)-1, -1, -1):
        reverse += command[x]

    print(f"{command} = {reverse}")

    command = input()

