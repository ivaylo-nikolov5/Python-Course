# read the input

product = input().lower()
town = input().lower()
quantity = float(input())

if town == "sofia":
    if product == "coffee":
        print(quantity * 0.50)
    elif product == "water":
        print(quantity * 0.80)
    elif product == "beer":
        print(quantity * 1.20)
    elif product == "sweets":
        print(quantity * 1.45)
    else:
        print(quantity * 1.60)

if town == "plovdiv":
    if product == "coffee":
        print(quantity * 0.4)
    elif product == "water":
        print(quantity * 0.7)
    elif product == "beer":
        print(quantity * 1.15)
    elif product == "sweets":
        print(quantity * 1.30)
    else:
        print(quantity * 1.50)

if town == "varna":
    if product == "coffee":
        print(quantity * 0.45)
    elif product == "water":
        print(quantity * 0.70)
    elif product == "beer":
        print(quantity * 1.10)
    elif product == "sweets":
        print(quantity * 1.35)
    else:
        print(quantity * 1.55)
