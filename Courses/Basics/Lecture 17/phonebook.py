def phonebook():
    command = input()
    numbers_dict = {}

    while not command.isdigit():
        command = command.split("-")
        name = command[0]
        number = command[1]

        numbers_dict[name] = number

        command = input()

    for i in range(int(command)):
        person = input()
        if person in numbers_dict:
            print(f"{person} -> {numbers_dict[person]}")
        else:
            print(f"Contact {person} does not exist.")


phonebook()
