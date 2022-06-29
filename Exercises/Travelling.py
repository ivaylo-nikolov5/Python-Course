
destination = input()
while True:
    if destination == "End":
        break
    total = 0
    needed_money = float(input())
    while needed_money > total:
        income = float(input())
        total += income

    print(f"Going to {destination}!")
    destination = input()


