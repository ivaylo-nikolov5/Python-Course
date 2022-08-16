from collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while bowls_of_ramen and customers:
    current_bowl = bowls_of_ramen.pop()
    current_customer = customers.popleft()

    if current_bowl > current_customer:
        bowls_of_ramen.append(current_bowl - current_customer)
    elif current_customer > current_bowl:
        customers.appendleft(current_customer - current_bowl)

if not customers:
    print(f"Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(bowl) for bowl in bowls_of_ramen)}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(cust) for cust in customers)}")