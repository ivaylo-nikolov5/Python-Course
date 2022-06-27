def adding_heroes(dictionary):
    hero = input().split(" ")
    name = hero[0]
    hp = int(hero[1])
    mp = int(hero[2])
    dictionary[name] = [hp, mp]


def cast_func(command, hero, points, heroes_dict:dict):
    spell = command[3]
    if points <= heroes_dict[hero][1]:
        heroes_dict[hero][1] -= points
        return f"{hero} has successfully cast {spell} and now has {heroes_dict[hero][1]} MP!"
    else:
        return f"{hero} does not have enough MP to cast {spell}!"


def damage_func(command, hero, points, heroes_dict:dict):
    attacker = command[3]
    if points < heroes_dict[hero][0]:
        heroes_dict[hero][0] -= points
        return f"{hero} was hit for {points} HP by {attacker} and now has {heroes_dict[hero][0]} HP left!"
    else:
        heroes_dict.pop(hero)
        return f"{hero} has been killed by {attacker}!"


def recharge_func(hero, points, heroes_dict):
    if heroes_dict[hero][1] + points <= 200:
        heroes_dict[hero][1] += points
        return f"{hero} recharged for {points} MP!"
    else:
        new_points = 200 - heroes_dict[hero][1]
        heroes_dict[hero][1] = 200
        return f"{hero} recharged for {new_points} MP!"


def heal_func(hero, points, heroes_dict):
    if heroes_dict[hero][0] + points <= 100:
        heroes_dict[hero][0] += points
        return f"{hero} healed for {points} HP!"
    else:
        new_points = 100 - heroes_dict[hero][0]
        heroes_dict[hero][0] = 100
        return f"{hero} healed for {new_points} HP!"


def heroes_of_code(heroes):
    heroes_dict = dict()
    for x in range(heroes):
        adding_heroes(heroes_dict)

    command = input()
    while command != "End":
        result = ""
        command = command.split(" - ")
        action = command[0]
        hero = command[1]
        points = int(command[2])

        if action == "CastSpell":
            result = cast_func(command, hero, points, heroes_dict)
        elif action == "TakeDamage":
            result = damage_func(command, hero, points, heroes_dict)
        elif action == "Recharge":
            result = recharge_func(hero, points, heroes_dict)
        elif action == "Heal":
            result = heal_func(hero, points, heroes_dict)

        print(result)

        command = input()

    for x in heroes_dict:
        print(x)
        print(f"  HP: {heroes_dict[x][0]}")
        print(f"  MP: {heroes_dict[x][1]}")


heroes = int(input())
heroes_of_code(heroes)