age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys = 0
money = 0
next_birthday_money = 0
brother_money = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money += 10 + next_birthday_money
        next_birthday_money += 10
        brother_money += 1
    else:
        toys += 1

toys_sell_cash = toys * toy_price
money = (money + toys_sell_cash) - brother_money

diff = abs(washing_machine_price - money)

if money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
