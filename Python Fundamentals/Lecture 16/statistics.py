def statistics():
    products = dict()
    data = input(). split(": ")
    while data[0] != "statistics":
        product = data[0]
        quantity = int(data[1])
        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity

        data = input().split(": ")
    print("Products in stock:")
    for i in products:
        print(f"- {i}: {products[i]}")

    print(f"Total Products: {len(products)}")
    print(f"Total Quantity: {sum(products.values())}")

statistics()