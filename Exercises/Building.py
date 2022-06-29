floors = int(input())
rooms = int(input())

type = ""

for f in range(floors, 0, -1):
    if f == floors:
        type = "L"
    elif f % 2 == 0:
        type = "O"
    else:
        type = "A"

    for r in range(0, rooms):
        print(f"{type}{f}{r} ", end="")
    print()