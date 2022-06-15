number_of_orders = int(input())
total_sum = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())

    price_for_current_order = price_per_capsule * days * capsule_count
    total_sum += price_for_current_order
    print(f"The price for the coffee is: ${price_for_current_order:.2f}")

print(f"Total: ${total_sum:.2f}")
