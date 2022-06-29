
total = 0

while True:
    income = input()

    if income == "NoMoreMoney":
        break
    elif float(income) < 0:
        print("Invalid operation!")
        break
    else:
        income = float(income)
        print(f"Increase: {income:.2f}")
        total += income

print(f"Total: {total:.2f}")