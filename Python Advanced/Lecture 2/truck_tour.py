from collections import deque

oil_pumps = int(input())

stops = deque()

for _ in range(oil_pumps):
    pump = [int(x) for x in input().split()]
    stops.append(pump)

for attempt in range(oil_pumps):
    tank = 0
    failed = False

    for fuel, distance in stops:

        tank += fuel

        if distance > tank:
            failed = True
            break
        else:
            tank -= distance

    if not failed:
        print(attempt)
        break
    else:
        stops.append(stops.popleft())
