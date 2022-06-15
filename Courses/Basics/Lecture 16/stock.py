data = input().split(" ")
search = input().split(" ")

stock = dict()

for i in range(0, len(data), 2):
    product = data[i]
    quantity = int(data[i + 1])

    stock[product] = quantity

for i in search:
    if i in stock.keys():
        print(f"We have {stock[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")

#
#or
#
products = input().split(" ")
searched = input().split(" ")
product_dict = {products[x]: int(products[x+1]) for x in range(0, len(products), 2)}

for product in searched:
    if product in product_dict.keys():
        print(f"We have {product_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

