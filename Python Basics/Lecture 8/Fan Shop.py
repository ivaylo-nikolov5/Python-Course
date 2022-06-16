budget = int(input())
n = int(input())

spent_money = 0

for i in range(0, n):
    subject = input()
    if subject == "hoodie":
        spent_money += 30
    elif subject == "keychain":
        spent_money += 4
    elif subject == "T-shirt":
        spent_money += 20
    elif subject == "flag":
        spent_money += 15
    elif subject == "sticker":
        spent_money += 1
    else:
        pass

diff = abs(budget - spent_money)

if spent_money < budget:
    print(f"You bought {n} items and left with {diff} lv.")
else:
    print(f"Not enough money, you need {diff} more lv.")



