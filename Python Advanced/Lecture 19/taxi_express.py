from collections import deque

customers = deque(int(x) for x in input().split(", "))
taxis = list(int(x) for x in input().split(", "))

total_time = 0

while customers and taxis:
    current_customer = customers[0]
    current_taxi = taxis.pop()

    if current_customer <= current_taxi:
        customers.popleft()
        total_time += current_customer

if not customers:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(customer) for customer in customers)}")

