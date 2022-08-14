from collections import deque


def stock_availability(products: list, command, *args):
    if command == "delivery":
        products.extend(args)
    elif command == "sell":
        products = deque(products)
        if not args:
            products.popleft()
        elif len(args) == 1 and str(args[0]).isdigit():
            for _ in range(args[0]):
                products.popleft()
        else:
            products = list(products)
            for order in args:
                for product in range(len(products)):
                    if order == products[product]:
                        products[product] = ""
            products = [x for x in products if x != ""]

    return list(products)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
