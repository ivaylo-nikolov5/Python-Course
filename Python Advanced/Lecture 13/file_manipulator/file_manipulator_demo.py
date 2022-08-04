import os
from os import remove, path

command = input()

while command != "End":
    command = command.split("-")
    action = command[0]
    file_name = command[1]

    if action == "Create":
        open(file_name, "w").close()

    elif action == "Add":
        content = command[2]
        with open(file_name, "a") as file:
            file.write(f"{content}\n")

    elif action == "Delete":
        if os.path.exists(file_name):
            remove(file_name)
        else:
            print("An error occurred")


    elif action == "Replace":
        old = command[2]
        new = command[3]
        if not path.exists(file_name):
            print("An error occurred")
            command = input()
            continue
        with open(file_name, "r+") as file:
            new_content = file.read().replace(old, new)
            file.seek(0)
            file.truncate()
            file.write(new_content)


    command = input()