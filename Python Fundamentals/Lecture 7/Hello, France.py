items = input().split("|")
budget = float(input())
profit = 0
new_item_prices = []
data_prices = []
condition = False

for item in items:
    current_item = item.split("->")
    type_of_product = current_item[0]
    price = float(current_item[1])
    condition = False
    if type_of_product == "Clothes":
        if price <= 50:
            condition = True
    elif type_of_product == "Shoes":
        if price <= 35:
            condition = True
    elif type_of_product == "Accessories":
        if price <= 20.50:
            condition = True

    if condition:
        if budget >= price:
            budget -= price
            profit += price * 0.4
            new_price = price + (price * 0.4)
            new_item_prices.append(new_price)
            data_prices.append(str(f"{new_price:.2f}"))

print(" ".join(data_prices))
print(f"Profit: {profit:.2f}")
if budget + sum(new_item_prices) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

