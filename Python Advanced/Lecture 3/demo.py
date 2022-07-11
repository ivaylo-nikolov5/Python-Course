def softuni_party(guests):
    expected_guests = set()
    vip_guests = set()
    guests_that_came = set()

    for _ in range(guests):
        guest = input()

        if len(guest) == 8 and guest[0].isdigit():
            vip_guests.add(guest)
        elif len(guest) == 8:
            expected_guests.add(guest)

    guest = input()
    while not guest == "END":
        if guest[0].isdigit() and len(guest) == 8 and guest in vip_guests:
            vip_guests.remove(guest)
        elif len(guest) == 8 and guest in expected_guests:
            expected_guests.remove(guest)

        guest = input()

    print(len(vip_guests) + len(expected_guests))
    print(*vip_guests, sep="\n")
    print(*expected_guests, sep="\n")


n = int(input())
softuni_party(n)