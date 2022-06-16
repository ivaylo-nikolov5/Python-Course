country = input()
souvenir = input()
amount = int(input())


total = 0

is_invalid = False

if country == "Argentina":
    if souvenir == "flags":
        total = amount * 3.25
    elif souvenir == "caps":
        total = amount * 7.2
    elif souvenir == "posters":
        total = amount * 5.1
    elif souvenir == "stickers":
        total = amount * 1.25
    else:
        print("Invalid stock!")
elif country == "Brazil":
    if souvenir == "flags":
        total = amount * 4.2
    elif souvenir == "caps":
        total = amount * 8.5
    elif souvenir == "posters":
        total = amount * 5.35
    elif souvenir == "stickers":
        total = amount * 1.2
    else:
        print("Invalid stock!")
elif country == "Croatia":
    if souvenir == "flags":
        total = amount * 2.75
    elif souvenir == "caps":
        total = amount * 6.9
    elif souvenir == "posters":
        total = amount * 4.95
    elif souvenir == "stickers":
        total = amount * 1.1
    else:
        print("Invalid stock!")
elif country == "Denmark":
    if souvenir == "flags":
        total = amount * 3.1
    elif souvenir == "caps":
        total = amount * 6.5
    elif souvenir == "posters":
        total = amount * 4.8
    elif souvenir == "stickers":
        total = amount * 0.9
    else:
        print("Invalid stock!")
else:
    is_invalid = True

if not is_invalid:
    print(f"Pepi bought {amount} {souvenir} of {country} for {total:.2f} lv.")
else:
    print("Invalid country!")