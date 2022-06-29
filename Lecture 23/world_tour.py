def add_stop_func(command, stops):
    index = int(command[1])
    string = command[2]
    if index < len(stops):
        second_half = stops[index:]
        stops = stops[:index] + string + second_half

    return stops


def remove_stop_func(command, stops):
    start_index = int(command[1])
    end_index = int(command[2])
    if start_index < len(stops) and end_index < len(stops):
        stops = stops[:start_index] + stops[end_index+1:]
    return stops


def switch_func(command, stops):
    old_string = command[1]
    new_string = command[2]
    if old_string in stops:
        stops = stops.replace(old_string, new_string)

    return stops


stops = input()

command = input()
while command != "Travel":
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        stops = add_stop_func(command, stops)
    elif action == "Remove Stop":
        stops = remove_stop_func(command, stops)
    elif action == "Switch":
        stops = switch_func(command, stops)

    print(stops)
    command = input()


print(f"Ready for world tour! Planned stops: {stops}")