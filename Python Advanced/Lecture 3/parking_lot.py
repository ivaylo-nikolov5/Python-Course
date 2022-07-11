def parking_lot(lines):
    cars = set()
    for _ in range(lines):
        car = input().split(", ")
        in_out = car[0]
        car_number = car[1]
        if in_out == "IN":
            cars.add(car_number)
        elif in_out == "OUT":
            if car_number in cars:
                cars.remove(car_number)

    if not cars:
        print("Parking Lot is Empty")
    else:
        print(*cars, sep="\n")


n = int(input())
parking_lot(n)