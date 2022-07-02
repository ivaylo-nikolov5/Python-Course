def drive_func(command, car, cars_dict: dict):
    distance = int(command[2])
    fuel = int(command[3])
    if fuel > cars_dict[car][1]:
        print("Not enough fuel to make that ride")
    else:
        cars_dict[car][0] += distance
        cars_dict[car][1] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

    if cars_dict[car][0] >= 100000:
        print(f"Time to sell the {car}!")
        cars_dict.pop(car)

    return cars_dict

def refuel_func(command, car, cars_dict):
    fuel = int(command[2])
    if cars_dict[car][1] + fuel > 75:
        fuel = 75 - cars_dict[car][1]
    cars_dict[car][1] += fuel
    print(f"{car} refueled with {fuel} liters")

    return cars_dict


def revert_func(command, car, cars_dict):
    miles = int(command[2])
    if cars_dict[car][0] - miles >= 10000:
        cars_dict[car][0] -= miles
        print(f"{car} mileage decreased by {miles} kilometers")
    else:
        cars_dict[car][0] = 10000



    return cars_dict



lines = int(input())

cars_dict = dict()

for x in range(lines):
    info = input().split("|")
    the_car = info[0]
    the_mileage = int(info[1])
    the_fuel = int(info[2])
    cars_dict[the_car] = [the_mileage, the_fuel]

command = input()

while command != "Stop":
    command = command.split(" : ")
    action = command[0]
    car = command[1]
    if action == "Drive":
        drive_func(command, car, cars_dict)
    elif action == "Refuel":
        refuel_func(command, car, cars_dict)
    elif action == "Revert":
        revert_func(command, car, cars_dict)

    command = input()

for x in cars_dict:
    print(f"{x} -> Mileage: {cars_dict[x][0]} kms, Fuel in the tank: {cars_dict[x][1]} lt.")