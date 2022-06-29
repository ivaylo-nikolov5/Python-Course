width = int(input())
length = int(input())
height = int(input())

area = width * length * height
is_enough = True

cubic_meters = input()

while cubic_meters != "Done":
    cubic_meters = int(cubic_meters)
    area -= cubic_meters
    if area < 0:
        is_enough = False
        break

    cubic_meters = input()

if is_enough:
    print(f"{area} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(area)} Cubic meters more.")