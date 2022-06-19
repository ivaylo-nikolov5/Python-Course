def destination_mapper(info):
    destinations = []
    points = 0

    second_copy = info.split("=")
    if "/" in info or "=" in info:
        for x in second_copy:
            if "/" not in x and len(x) >= 3:
                is_valid = True
                for y in x:
                    if y.isdigit():
                        is_valid = False
                        break

                if is_valid:
                    destinations.append(x)
                    points += len(x)

        info_copy = info.split("/")

        for x in info_copy:
            if "=" not in x and len(x) >= 3:
                is_valid = True
                for y in x:
                    if y.isdigit():
                        is_valid = False
                        break

                if is_valid:
                    destinations.append(x)
                    points += len(x)

    print(f"Destinations: {', '.join(destinations)}")
    print(f"Travel Points: {points}")


information = input()
destination_mapper(information)