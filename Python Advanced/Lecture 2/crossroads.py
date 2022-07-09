from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
crashed = False

command = input()
while not command == "END":
    cars.append(command)
    command = input()
passed_cars = 0
duration = green_light
while cars:
    if duration == 0:
        break

    if cars[0] == "green":
        duration = green_light
        cars.popleft()
    else:
        duration -= len(cars[0])
        if duration >= 0:
            cars.popleft()
            passed_cars += 1
        else:
            duration += free_window
            if duration >= 0:
                cars.popleft()
                passed_cars += 1
            else:
                car = cars[0]
                print("A crash happened!")
                print(f"{car} was hit at {car[duration]}.")
                crashed = True
                break
            duration = 0

if not crashed:
    print(f"Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
