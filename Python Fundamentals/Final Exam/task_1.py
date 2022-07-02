message = input()

command = input()

while command != "Reveal":
    command = command.split(":|:")
    action = command[0]
    is_error = False
    if action == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]
    elif action == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
        else:
            is_error = True
            print("error")
    elif action == "ChangeAll":
        old = command[1]
        new = command[2]
        if old in message:
            message = message.replace(old, new)
    if not is_error:
        print(message)

    command = input()

print(f"You have a new text message: {message}")