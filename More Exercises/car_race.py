def car_race(cars):
    middle = len(cars) // 2
    left_car = cars[:middle]
    right_car = list(reversed(cars[middle + 1:]))
    left_time = cars[0]
    right_time = cars[-1]

    for x in range(1, len(left_car)):
        if left_car[x] == 0:
            left_time -= left_time * 0.2
        else:
            left_time += left_car[x]

    for x in range(1, len(right_car)):
        if right_car[x] == 0:
            right_time -= right_time * 0.2
        else:
            right_time += right_car[x]

    if left_time < right_time:
        print(f"The winner is left with total time: {left_time:.1f}")
    else:
        print(f"The winner is right with total time: {right_time:.1f}")


cars_time = list(map(int, input().split(" ")))
car_race(cars_time)
