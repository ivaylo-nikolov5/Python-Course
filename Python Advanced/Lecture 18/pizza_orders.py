from collections import deque

total_pizzas = 0
is_failed = False

pizza_orders = deque(int(x) for x in input().split(", "))
employees = list(int(x) for x in input().split(", "))

while pizza_orders:
    if not employees:
        is_failed = True
        break

    current_pizza_order = pizza_orders[0]
    current_employee = employees[-1]

    if current_pizza_order <= 0 or current_pizza_order > 10:
        pizza_orders.popleft()
        continue

    if current_pizza_order <= current_employee:
        pizza_orders.popleft()
        total_pizzas += current_pizza_order
    else:
        total_pizzas += current_employee
        pizza_orders[0] -= current_employee

    employees.pop()


if not is_failed:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(el) for el in employees)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(el) for el in pizza_orders)}")



