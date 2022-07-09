def plunder_func(cities_dict: dict, action, city):
    people = int(action[2])
    gold = int(action[3])

    cities_dict[city][0] -= people
    cities_dict[city][1] -= gold
    print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

    if cities_dict[city][0] <= 0 or cities_dict[city][1] <= 0:
        print(f"{city} has been wiped off the map!")
        cities_dict.pop(city)


def prosper_func(cities_dict, action, city):
    gold = int(action[2])
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        cities_dict[city][1] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {cities_dict[city][1]} gold.")


def pirates():
    cities_dict = dict()

    command = input()
    while command != "Sail":
        command = command.split("||")
        city = command[0]
        people = int(command[1])
        gold = int(command[2])
        if city not in cities_dict:
            cities_dict[city] = [people, gold]
        else:
            cities_dict[city][0] += people
            cities_dict[city][1] += gold

        command = input()

    action = input()
    while action != "End":
        action = action.split("=>")
        city = action[1]

        if action[0] == "Plunder":
            plunder_func(cities_dict, action, city)
        elif action[0] == "Prosper":
            prosper_func(cities_dict, action, city)

        action = input()

    if len(cities_dict) < 1:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")
    else:
        print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
        for x in cities_dict:
            print(f"{x} -> Population: {cities_dict[x][0]} citizens, Gold: {cities_dict[x][1]} kg")

pirates()

