def shopping_list(budget, **kwargs):
    counter = 0
    result = ""

    if budget < 100:
        return "You do not have enough budget."

    for product, price_quantity_pair in kwargs.items():
        if counter == 5 or budget <= 0:
            break

        price = price_quantity_pair[0]
        quantity = price_quantity_pair[1]
        total = price * quantity

        if total <= budget:
            budget -= total
            result += f"You bought {product} for {total:.2f} leva.\n"
            counter += 1

    return result

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


