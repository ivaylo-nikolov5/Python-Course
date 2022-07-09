from collections import deque

green_light_duration = int(input())
free_window = int(input())

command = input()
duration = green_light_duration

queue = deque()
crashed = False
passed_cars = 0

while not command == "END":
    queue.append(command)
    command = input()

while queue:
    car = queue[0]

    if car == "green":
        duration = green_light_duration
        queue.popleft()

    else:
        if duration == 0:
            break
        else:
            if duration > 0 and duration + free_window >= len(car):
                queue.popleft()
                duration -= len(car)
                passed_cars += 1
                if duration < 0:
                    break
            else:
                crashed = True
                print("A crash happened!")
                print(f"{car} was hit at {car[duration + free_window]}.")
                break

if not crashed:
    print(f"Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
