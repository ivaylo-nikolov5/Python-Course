from collections import deque

pumps = int(input())
stops = deque()

for _ in range(pumps):
    pump = [int(x) for x in input().split()]
    stops.append(pump)

for attempt in range(pumps):

    tank = 0
    failed = False

    for fuel, distance in stops:
        tank += fuel

        if tank < distance:
            failed = True
            break
        else:
            tank -= distance

    if failed is not True:
        print(attempt)
        break
    else:
        stops.rotate(-1)



