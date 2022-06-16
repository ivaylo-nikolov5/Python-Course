def order(product, amount):
    if product == "coffee":
        return amount * 1.5
    elif product == "water":
        return amount * 1
    elif product == "coke":
        return amount * 1.4
    elif product == "snacks":
        return amount * 2


item = input()
quantity = int(input())
total = order(item, quantity)

print(f"{total:.2f}")