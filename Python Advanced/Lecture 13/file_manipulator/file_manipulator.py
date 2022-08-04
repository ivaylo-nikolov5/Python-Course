import os


def create_func(name):
    open(name, "w").close()


def add_func(name, content):
    with open(f"{name}", "a") as file:
        file.write(f"{content}\n")


def replace_func(name, old, new):
    if not os.path.exists(name):
        print("An error occurred")
        return
    with open(name, "r+") as file:
        new_file_content = file.read().replace(old, new)
        file.seek(0)
        file.truncate()
        file.write(new_file_content)


def delete_func(name):
    if os.path.exists(name):
        os.remove(f"{name}")
        return
    print("An error occurred")


command = input()

while command != "End":
    command = command.split("-")

    action = command[0]
    file_name = command[1]

    if action == "Create":
        create_func(file_name)
    elif action == "Add":
        content = command[2]
        add_func(file_name, content)
    elif action == "Replace":
        old_string = command[2]
        new_string = command[3]

        replace_func(file_name, old_string, new_string)
    elif action == "Delete":
        delete_func(file_name)

    command = input()
