def softuni_parking(lines):
    register_dict = {}
    for x in range(lines):
        command = input().split(" ")
        name = command[1]

        if command[0] == "unregister":
            if name in register_dict:
                del register_dict[name]
                print(f"{name} unregistered successfully")
            else:
                print(f"ERROR: user {name} not found")
        else:
            plate = command[2]
            if name in register_dict:
                print(f"ERROR: already registered with plate number {register_dict[name]}")
            else:
                register_dict[name] = plate
                print(f"{name} registered {plate} successfully")

    for x in register_dict:
        print(f"{x} => {register_dict[x]}")


number_of_lines = int(input())
softuni_parking(number_of_lines)