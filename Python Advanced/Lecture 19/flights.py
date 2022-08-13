def flights(*args):
    destinations_count = {}

    for flight_idx in range(0, len(args), 2):
        flight = args[flight_idx]
        if flight == "Finish":
            return destinations_count

        if flight not in destinations_count:
            destinations_count[flight] = 0

        destinations_count[flight] += args[flight_idx + 1]


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))