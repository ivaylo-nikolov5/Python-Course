data = input().split(" ")
food_dict = {}
for i in range(0, len(data), 2):
    food = data[i]
    quantity = int(data[i + 1])

    food_dict[food] = quantity

print(food_dict)
#
#or
#
products = input().split(" ")
product_dict = {products[x]: int(products[x+1]) for x in range(0, len(products), 2)}
print(product_dict)

