def rate_func(command, rating_dict: dict, plants_dict: dict):
    plant = command[1]
    rating = float(command[3])
    rating_dict[plant].append(rating)



def update_func(command, plants_dict):
    plant = command[1]
    rarity = int(command[3])
    plants_dict[plant] = rarity


def reset_func(command, rating_dict, plants_dict: dict):
    plant = command[1]
    rating_dict[plant] = [0]


lines = int(input())

plants_dict = dict()
rating_dict = dict()


for x in range(lines):
    the_plant = input()
    the_plant = the_plant.split("<->")
    plant_name = the_plant[0]
    the_rarity = the_plant[1]

    plants_dict[plant_name] = the_rarity
    rating_dict[plant_name] = []

command = input()
while command != "Exhibition":
    command = command.split(" ")
    action = command[0]
    info = command[1]
    result = ""
    if command[1] in plants_dict and command[1] in rating_dict:
        if action == "Rate:":
            rate_func(command, rating_dict, plants_dict)
        elif action == "Update:":
            update_func(command, plants_dict)
        elif action == "Reset:":
            reset_func(command, rating_dict, plants_dict)
    else:
        print("error")
    command = input()


print("Plants for the exhibition:")
for x in plants_dict:
    print(f"- {x}; Rarity: {plants_dict[x]}; Rating: {sum(rating_dict[x])/ len(rating_dict[x]):.2f}")

