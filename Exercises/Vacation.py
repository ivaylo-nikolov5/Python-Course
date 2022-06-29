needed_money = float(input())
available_money = float(input())

spending_days = 0
total_days = 0

while needed_money > available_money and spending_days < 5:
    action = input()
    amount = float(input())
    total_days += 1
    if action == "spend":
        available_money -= amount
        spending_days += 1
        if available_money < 0:
            available_money = 0
    else:
        available_money += amount
        spending_days = 0

if spending_days >= 5:
    print(f"You can't save the money.\n{total_days}")

if available_money >= needed_money:
    print(f"You saved the money for {total_days} days.")







